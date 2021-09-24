Title: Two ways to share your toolbox with your pipelines 
Date: 2021-09-08
Category: Posts 
Tags: azure-devops,devops, pipelines, eliminate-waste
Slug: share-your-toolbox-with-pipelines
Author: Willy-Peter Schaub
Summary: Let us review two strategies to share scripts and config files with your Azure (YAML) Pipelines.

The need to share PowerShell Scripts or configuration files is a common requirement when working with Azure Pipelines. For example, pass a configuration file to the [WhiteSource](https://whitesource.atlassian.net/wiki/spaces/WD/pages/804814917/Unified+Agent+Overview) unified agent tool, or run a PowerShell script to invite Zombies created by the [Stryker](https://stryker-mutator.io/) mutation tool. 

![Inject](/images/share-your-toolbox-with-pipelines-1.png)

These are just two examples of a platter of common and re-usable features we need to **inject** into the flow of our Azure Pipelines.

Let us review two options. The first is the one we embraced on our boot-strap template, as documented in the [pipeline snowflakes](https://wsbctechnicalblog.github.io/why-pipelines-part1.html) series and the second is a simplification I will present to our pipeline working group to reduce complexity and waste.

> Requirement:
>
> _As an Azure Pipeline I want to download a toolbox package, so that I can re-use tested and well-known scripts, as well as verified configuration files._

# A la Universal Artifact

![UA](/images/share-your-toolbox-with-pipelines-2.png)

The [Universal Artifacts](https://docs.microsoft.com/en-us/azure/devops/artifacts/quickstarts/universal-packages?view=azure-devops) are probably one of the longest running feature previews in Azure DevOps. It allows you to store **anything** up to 4TB - although you should have a serious chat with yourself if your packages start growing beyond kilobytes in size. You want small and focused packages, that can be downloaded fast and do not dump any **waste** on your build agent.

![Pipeline](/images/share-your-toolbox-with-pipelines-5.png)

As shown above, we developed a universal artifact app-type blueprint that create a pipeline that publishes our toolbox, containing scripts and configuration files, to a development universal artifact and starts running security scans, irrespective from which branch the pipeline is triggered from. If triggered from a release/* branch, it involves our DevSecOps team in a security review and then deploys to an additional production universal artifact.

In our boot-strap.yml template, we download the universal package, which requires an average of **10 seconds**.

```
# ===========================================================================
# BOOTSTRAP TOOLBOX
# ===========================================================================
# Production Toolbox
- ${{ if and( ne( lower(parameters.loadDVTBox), 'yes'), or( eq( lower(parameters.bootstrapMode), 'init' ), eq( lower(parameters.bootstrapMode), 'runbuildingcodeonly' ), eq( lower(parameters.forceToolbox), 'true'))) }}:
  - task: UniversalPackages@0
    displayName: Bootstrap download toolbox
    inputs:
      command: 'download'
      downloadDirectory: '$(System.DefaultWorkingDirectory)/ToolboxRuntime'
      feedsToUse: 'internal'
      vstsFeed: '<FEED_GUID>'           # Automation.Pipeline.Templates
      vstsFeedPackage: '<PACKAGE-GUID>' # toolbox
      vstsPackageVersion: '*'
```

We run scripts from the package in our pipeline, for example, to publish telemetry from the boot-strap template.

```
- ${{ if eq( lower(parameters.bootstrapMode), 'init' ) }}:
  - task: PowerShell@2
    displayName: 'Bootstrap Telemetry START'
    inputs:
      filePath: '$(System.DefaultWorkingDirectory)/ToolboxRuntime/Scripts/AI/log-bootstrap-event-to-ai.ps1'
      arguments: -OperationId "$(Build.BuildNumber).$(Build.BuildId)" `
                 -Event  'Bootstrap' `
                 -Action 'Start' `
                 -BootstrapMode ${{parameters.bootstrapMode}} ` 
                 -ApplicationType ${{parameters.applicationType}} `
                 -ApplicationBlueprint ${{parameters.applicationBlueprint}} `
                 -PortfolioName ${{parameters.portfolioName}} `
                 -ProductName ${{parameters.productName}} `
                 -SourcesDirectory ${{parameters.sourcesDirectory}} `
                 -VerboseFlag ${{parameters.verbose}} `
                 -Previews ${{parameters.previews}} `
                 -ForceCheck ${{parameters.forceCheck}}
      failOnStderr: true
      pwsh: true
    continueOnError: true
```

And finally, we pass configuration files contained in the toolbox package, such as wss-unified-agent.config, when running security scans.

```
- script: java -jar wss-unified-agent.jar -c $(System.DefaultWorkingDirectory)/ToolboxRuntime/Config/DevSecOps/wss-unified-agent.config -apiKey ${{parameters.apiKeyAPI}} -product ${{parameters.whitesourceProductName}} -project ${{parameters.portfolioName}}.${{parameters.productName}} -logLevel DEBUG
  displayName: 'Bootstrap WhiteSource Unified Agent Scan'
  continueOnError: true
```

Works like a charm!

Do we need the universal artifact pipeline and the complexity of generating, publishing, and downloading the toolbox package? What happens when we **remove** it from our Azure Pipeline process?

# A la repository

![Code Repo](/images/share-your-toolbox-with-pipelines-3.png)

An alternative approach is to separate the toolbox, containing scripts and configuration files, into a separate Azure Repo. We must let the system know about the external repository so that we can integrate it into our pipeline.

```
- repository: Toolbox
  type: git
  name: 'Common/Automation.Scripts'
```

We then **check out** the contents of the external repository, relative to the agent's build directory (e.g. \_work\1). Default is the directory **s** and adds an average of **3 seconds** processing time to our pipeline.

> ![Waste](/images/share-your-toolbox-with-pipelines-6.png) 
>
> **WASTE ALERT** - (10-3) = 7 seconds of waste detected in the first Universal Artifact strategy!


```
- checkout: Toolbox
  path: tool-box
```

Tweak out template(s) to pickup the artifacts, such as the configuration file for the WhiteSource Unified Agent, from a different location.

```
$(Build.SourcesDirectory)
- script: java -jar wss-unified-agent.jar -c $(Build.SourcesDirectory)/tool-box/config/dev-sec-ops/wss-unified-agent.config -apiKey ${{parameters.apiKeyAPI}} -product ${{parameters.whitesourceProductName}} -project ${{parameters.portfolioName}}.${{parameters.productName}} -logLevel DEBUG
  displayName: 'Bootstrap WhiteSource Unified Agent Scan'
  continueOnError: true
```

The Azure Repo strategy has less **moving** parts, is **faster** and **simpler**, no?

# Which option do you prefer?

![Option](/images/share-your-toolbox-with-pipelines-4.png)

I wish we had comments enabled on our technical blog, so that we could have a vibrant discussion of the two presented and other options. In the interim, please DM me on [twitter](www.twitter.com/wpschaub) or [linkedin](www.linkedin.com/in/wpschaub), or better add a comment on the Twitter or LinkedIn post which nudged you to this article, to share your thoughts.


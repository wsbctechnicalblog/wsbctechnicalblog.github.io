Title: Part 3: Pipelines - Basic building blocks as templates and sprinkling on telemetry
Date: 2021-01-04
Category: Posts
Tags: azure-devops, devops, pipelines, x-as-code 
Slug: yaml-pipelines-part3
Author: Willy-Peter Schaub
Summary: With the support from all **people**, YAML templates support our five (5) core goals and pillars of our common engineering system.

Welcome back to the world of pipelines. In [part1](/why-pipelines-part1.html) we discussed "why" pipelines are valuable and introduced the new Azure DevOps YAML-based pipelines in [part2](/yaml-pipelines-part2.html). In this post we explore templates as invaluable building blocks and telemetry to gather essential insights.

---

# What is a YAML template?

Templates allow us to define reusable content, logic, and parameters, keeping our main pipeline definitions razor focused on the application and sharing common logic. Another advantage of templates, which we will exploit in part 7 of this adventure, is the ability to script and assemble pipelines at “queue” time.

Essentially, we can define reusable code in separate templates. We can include templates within templates and define four types of templates:
- **Stage** to define a set of stages of related jobs
- **Job** to define a collection of steps run by an agent
- **Step** to define a linear sequence of operations for a job
- **Variable** as an alternative to hard coded values or variable groups

> **NOTE** - Azure Pipelines currently support a maximum of 50 unique template files in a pipeline.

Here is an example template, that defines the reusable code to download a universal artifact containing configuration files, download and run the [WhiteSource](https://www.whitesourcesoftware.com/) unified code scanning agent:

```yml
parameters:
  portfolioName:         'unknown'
  productName:           'unknown'
  urlUnifiedAgent:       'https://github.com/whitesource/unified-agent-distribution/releases/latest/download/wss-unified-agent.jar'
  apiKeyAPI:             '<DEMO-KEY>'
  
steps:

- task: UniversalPackages@0
  displayName: Download pipeline universal artifact
  inputs:
    command:            'download'
    downloadDirectory:  '$(System.DefaultWorkingDirectory)/Artifact'
    feedsToUse:         'internal'
    vstsFeed:           '<DEMO-GUID>/<DEMO-GUID>' # automation templates
    vstsFeedPackage:    '<DEMO-GUID>'             # toolbox
    vstsPackageVersion: '*'

- script: curl -LJO ${{parameters.urlUnifiedAgent}}
  displayName: 'Download the latest WhiteSource Unified Agent'
  continueOnError: true

- script: java -jar wss-unified-agent.jar -c $(System.DefaultWorkingDirectory)/Artifact/Config/wss-unified-agent.config -apiKey ${{parameters.apiKeyAPI}} -product WorkSafeBC -project ${{parameters.portfolioName}}.${{parameters.productName}}
  displayName: 'WhiteSource Unified Agent Scan'
  continueOnError: true
```

Including the reusable code in your pipeline is simple:

```yml
  - template: Templates/DevSecOps/Whitesource.yml@AzDOTemplates
    parameters:
      portfolioName: 'DEMO.Samples'
      productName:   'WhiteSource'
```

# Why are we excited about YAML templates?

As discussed at the [DevOps Vancouver Meetup: April 2020](https://www.meetup.com/DevOps-Vancouver-BC-Canada/events/270150093/), anyone going through a digital transformation will acknowledge that we need to focus on products, process, and people. 

> “*DevOps is the union of people, process, and products to enable continuous delivery of value to our end users.*” – Donovan Brown

Our mandate is to **empower** people, standardize on the best products, and continuously improve processes to raise quality and security bars, efficiency, and reliability. We considered three options to drive a culture change with our continuous delivery pipeline infrastructure:

![Rules Apply](/images/moving-hundreds-of-pipeline-snowflakes-part3-1.png) We can enforce strict governance, standards, and rules, quickly stifling innovation and personal satisfaction.

![Rebellion](/images/moving-hundreds-of-pipeline-snowflakes-part3-2.png) We can continue to promote complete autonomy, leading to a product and process rebellion and creating a pile of technology mess that is hard and expensive to maintain.

![YingYang](/images/moving-hundreds-of-pipeline-snowflakes-part3-3.png) We can listen to what motivates and enables our Agile teams and work together to embrace organizational governance.

We opted for the latter to enable and inspire engineering teams to learn, grow, and innovate by sharing and encouraging proven patterns and practices through guardrails.

![CeS Balance](/images/moving-hundreds-of-pipeline-snowflakes-part3-4.png)

But, let us get back to the core question - "*Why are we excited about YAML templates?*". 

With the support from all **people**, which implies down (organizational leadership) and bottom up (engineering), YAML templates support our five (5) core goals and pillars of our common engineering system:

- Continuously **innovate** and enable users, with alignment to architecture, security and development **guardrails**.

- **Automation** to provide speed, consistency, and repeatable processes.
 
- **Enable** and **empower** users to create business value from ideation to production.

- Align with **security** guardrails to minimize vulnerabilities and enforce a secure collaboration and engineering system.  

- Keep it **simple** to create a system that can be supported, maintained, and improved with ease. 

--- 

# Reusable templates

As shown in the illustration below, from my rough notes, we defined two base blueprints. One that defines one stage, **multiple jobs** allowing parallel runs on separate agents, each with multiple steps.

The simpler and more recommended blueprint defines one stage, one job, with **multiple steps**.** It keeps things simple, running everything on one agent within the same context.

We are working on application-type specific quick-start blueprints, for example Angular, .NET Core, iOS application, and Azure Function application to make it even easier to get started and to encourage consistency.

![Blueprints and Templates Sketch](/images/moving-hundreds-of-pipeline-snowflakes-part3-5.png)

All our blueprints inject and rely on several templates, which are maintained in a secure repository - anyone can view, and anyone can suggest a change through a pull request.

Like the WhiteSource sample mentioned before, we have two **DevSecOps.yml** and **DevSecOpsInit.yml** templates which define the use of Dev**Sec**Ops tasks, such as SonarQube and WhiteSource tasks.

The **BuildingCode.yml** template defines the use of building code validations, such as duplicate code, end of life validations, and detection of surviving [Stryker](https://stryker-mutator.io/) mutants.

Lastly, the **bootstrap** template is the HEART of our new pipelines, using parameters and expressions to call the right validations for the known application types, which in turn injects the relevant templates and tasks when a pipeline is queued.

```yml
    - template: Templates/Bootstrap.yml@CDTemplates
      parameters:
        bootstrapMode:    'init'
        applicationType:  'dotnet'
        applicationGuid:  $(productGuid)
        portfolioName:    $(portfolioName)
        productName:      $(productName)
        sourcesDirectory: $(Build.SourcesDirectory)
```

---

# Remember to keep it simple

The power of YAML enables us to create invaluable pipeline definitions and abstract re-usable code in templates, as discussed. **BUT** we always urge our pipeline working group and our pipeline users to keep things **SIMPLE**, to ensure that we can innovate, scale, maintain the new world of continuous delivery pipelines, and empower both development and operations.

We hide the complexity in our bootstrap.yml template, which can be embraced in two ways:

1. Start with one of our blueprints and insert … COPY PASTE … the application specific YAML code.
2. Insert the blueprint template calls into existing YAML pipeline.
  
![Blueprints and Context](/images/moving-hundreds-of-pipeline-snowflakes-part3-6.png)

> **GOTCHA** -There is a need to run specific tasks within the same context. 

It is one of the reasons we call the blueprints differently in single-job and multi-job sample blueprints, as shown above. We need to ensure that SonarQube tasks, for example, run within the same job context as the build, and the building code after the test. When we run within the same context, we can also be more efficient by loading dependencies, such as source code, extensions, and configuration once.

---

# Telemetry gives us insight

To monitor, troubleshoot, and understand the flow of value in our continuous delivery pipelines we explored a few ways to extend the Azure Pipeline analytics with metrics from our pipeline blueprints and templates. The telemetry will enable us to measure **lead time**, **cycle time**, and **efficiency**, uncover waste, and continuously improve as discussed in [value stream mapping](https://www.tactec.ca/value-stream-mapping-vsm/).

We opted for Azure [Application Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview), calling a reusable PowerShell Core script in our templates to send the pipeline events, actions, and other data for future analysis.

```yml
- ${{ if eq( parameters.previews, 'true' ) }}:
  - task: PowerShell@2
    displayName: 'Building Code SonarQube Duplicate Code Validation Telemetry'
    inputs:
      filePath: '$(System.DefaultWorkingDirectory)/Toolbox/Scripts/AI/logBootstrapEventToAI.ps1'
      arguments: -OperationId   "$(Build.BuildNumber).$(Build.BuildId)" `
                 -Event         'Building Code' `
                 -Action        'Duplicate Code' `
                 -DuplicateCode "$(SQDCVars.codeMetricesTaskVar)"
      pwsh: true
    continueOnError: true     
```

> **NOTE** - The extract above shows how we use conditional ```${{ if ... }}``` to introduce previews into our operational pipelines. If ```parameters.previews``` is set to true, indicating that we are embracing preview logic, the telemetry script is included in our pipeline and called at run-time.

---

# What is next?

Now that we understand templates, we will look at the magic that has our Sec, in DevSecOps, smiling from ear to ear. See you in [part 4](yaml-pipelines-part4.html).

---

> Series Bread Crumbs | [Part 1, TOC](/why-pipelines-part1.html) | [Part 2](/yaml-pipelines-part2.html) | Part 3 | [Part 4](/yaml-pipelines-part4.html) | [Part 5](/yaml-pipelines-part5.html) | [Part 6](/yaml-pipelines-part6.html) | [Part 7](/yaml-pipelines-part7.html) | [Part 8](/yaml-pipelines-part8.html) | [Part 9](/yaml-pipelines-part9.html) | [Part 10](/yaml-pipelines-part10.html) | [Part 11](/yaml-pipelines-part11.html) |


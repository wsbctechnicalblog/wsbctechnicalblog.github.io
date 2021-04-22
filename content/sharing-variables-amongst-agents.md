Title: How to share variables amongst Azure Pipeline agents
Date: 2021-04-21
Category: Posts
Tags: Azure Pipelines, Tips
Slug: sharing-variables-amongst-agents
Author: Willy-Peter Schaub
Summary: As per documentation, output variables can be used across stages in an Azure YAML-based pipeline. I will share a few turbulent moments we experienced while troubleshooting this feature in one of our pipeline blueprints.

The Azure Pipelines have evolved at a blistering pace during the past 2-3 years. Features we dreamt of, like passing variables between [stages](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/stages?view=azure-devops&tabs=yaml), was a big NO-NO in 2019. We had to use convoluted workarounds to save variables to storage and reloading them in the upstream stages. Not supportive of our goal for simplicity. 

---

# Opportunity leads to requirement

> ![Breaking News](/images/sharing-variables-amongst-agents-2.png)
> In May 2020, the following release notes created excitement: "_Output variables may now be used across stages in a YAML-based pipeline._"

This opened exciting opportunities for us, such as retrieving the solution's semantic version using the [GitTools](https://github.com/GitTools), and sharing it with upstream stages.

> Our git-tools-git-version.yml template

```yml
parameters:
- name:     versionSpec
  type:     string
  default:  '5.x'
- name:     useConfigFile
  type:     boolean
  default:  false
- name:     configFilePath
  type:     string
  default:  ''
- name:     updateAssemblyInfo
  type:     boolean
  default:  false
- name:     updateAssemblyInfoFilename
  type:     string
  default:  ''
  
steps:
  - task: gitversion/setup@0
    displayName: Install GitVersion
    inputs:
      versionSpec: ${{parameters.versionSpec}}

  - task: gitversion/execute@0
    displayName: Use GitVersion
    inputs:
      useConfigFile:                ${{parameters.useConfigFile}}
      configFilePath:               ${{parameters.configFilePath}}
      updateAssemblyInfo:           ${{parameters.updateAssemblyInfo}}
      updateAssemblyInfoFilename:   ${{parameters.updateAssemblyInfoFilename}}
```

Here is a visual of our hypothetical pipeline. 

> Core issue - pass versionToolkit variable from CI to CD stages
>
> ![Pipeline ownership](/images/sharing-variables-amongst-agents-1.png)

We retrieve the semantic version using the git-tools-git-version.yml template in our **ContinuousIntegration** (CI) stage. Now that we can share the version with our continuous deployment (CD) pipeline stages, we have a requirement to pass the version for tasks, such as updating a Universal Artifact, as shown below.

> Publish Universal Artifact using the version

```yml
          steps:
            - script: echo Toolkit Version = $(currentVersion)
            - task: UniversalPackages@0
              name: Create_DV_Universal_Package
              inputs:
                command: 'publish'
                publishDirectory:       $(Agent.BuildDirectory)/drop
                feedsToUsePublish:      'internal'
                vstsFeedPublish:        $(developmentStageFeedPublish)
                vstsFeedPackagePublish: $(developmentStagePackagePublish)
                versionOption:          'custom'
                versionPublish:         $(versionToolbox)
```

---

# Setting the versionToolbox Variable

After retrieving the semantic version, we run an inline PowerShell Core script to create an output variable, called **versionToolkit**, in the **ContinuousIntegration** stage.

> Create Development stage-specific versionToolkit version

```yml
    - task: PowerShell@2
      name: setToolkitVersion
      displayName: "Set Toolkit Version"
      inputs:
        targetType: 'inline'
        script: Write-Host "##vso[task.setvariable variable=versionToolkit;isOutput=true]$(GitVersion.MajorMinorPatch)"
```

Next, we move to the **Development** stage and create a stage variable, which is set to the value of versionToolkit calculated in the **ContinuousIntegration** stage.

As per documentation, the output variables are produced by steps inside of jobs and the format of the dependency variable is: **stageDependencies.\<stageName\>.\<jobName\>.outputs['\<stepName\>.\<variableName\>']**

> Create **Development** stage-specific versionToolkit version

```yml
- stage:         'Development'
  dependsOn:
  - ContinuousIntegration
  variables:
    versionToolkit: $[ stageDependencies.ContinuousIntegration.ContinuousIntegration.outputs['setToolkitVersion.toolkitVersion'] ]
```

In our case the originating stage and job share the same name **ContinuousIntegration**, hence the ...ContinuousIntegration.ContinuousIntegration... repetition.

The **versionToolkit** version is then passed to the deployment steps, such as the Universal Artifact update task mentioned earlier on. 

The relatively simple solution works like a charm :)

---

# Frustration reigns

Next we move to the **Production** stage and implement the same (identical) logic.

Unfortunately, we get an empty **versionToolkit** variable. 

![WHY](/images/sharing-variables-amongst-agents-3.png)
Why is the version not flowing, as expected?

I dabbled with several options, such as passing the variable from stage to stage. While some worked with normal jobs, they crumbled with the use of [Deployment Jobs](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/deployment-jobs?view=azure-devops), and failed our simplicity rule. A few trying stories for another day.

Back to our **production** stage.

> **Production** Stage

```yml
- stage:         'Production'
    dependsOn:
    - SecurityScans
    - SecurityReview
    variables:
      versionToolbox: $[ stageDependencies.ContinuousIntegration.ContinuousIntegration.outputs['setToolkitVersion.versionToolbox'] ]
    pool:
      vmImage:     $(productionStageVmImage)
    jobs:
    - deployment:  'Production'
```

Can you spot the issue?

---

# After rain comes sunshine

I was pacing up and down our marina, sipping a hot chocolate, when a background thread triggered. “_How does the pipeline know that Production stage has a dependency on ContinuousIntegration stage?_”

I tried the following change:

```yml
  - stage:         'Production'
    dependsOn:
    - ContinuousIntegration
    - SecurityScans
    - SecurityReview
    variables:
      versionToolbox: $[ stageDependencies.ContinuousIntegration.ContinuousIntegration.outputs['setToolkitVersion.versionToolbox'] ]
    pool:
      vmImage:     $(productionStageVmImage)
    jobs:
```

**BINGO!** Adding line 3, ```- ContinuousIntegration```, fixed the stageDependency and the **versionToolbox** was set to the version set in the **ContinuousIntegration** stage.

To conclude, here is my complete experimentation pipeline I used to try random ideas and validate assumptions, such as the above-mentioned change.

> Experimentation sample

```yml
stages:
- stage: Build
  displayName: Build stage
  jobs:
  - job: Build
    pool:
      vmImage: 'windows-latest'
    displayName: Version Check
    continueOnError: false
    steps:

      - task: gitversion/setup@0
        displayName: Install GitVersion
        inputs:
              versionSpec: 5.x
      - task: gitversion/execute@0
        displayName: Use GitVersion

      - script: echo $(GitVersion.SemVer)

      - task: PowerShell@2
        name: setCurProjVersion
        displayName: "Collect Application Version ID"
        inputs:
          targetType: 'inline'
          script: Write-Host "##vso[task.setvariable variable=curProjVersion;isOutput=true]$(GitVersion.SemVer)"

- stage: Deploy
  displayName: Deploy stage
  dependsOn: Build
  variables:
    curProjVersion1: $[ stageDependencies.Build.Build.outputs['setCurProjVersion.curProjVersion'] ]
  jobs:
   - job: Deploy
     pool:
       vmImage: 'windows-latest'
     steps: 
      - task: PowerShell@2
        name: setCurProjVersion
        displayName: "Collect Application Version ID"
        inputs:
          targetType: 'inline'
          script: Write-Host "##vso[task.setvariable variable=curProjVersion;isOutput=true]$(curProjVersion1)"
      - task: PowerShell@2
        inputs:
          targetType: 'inline'
          script: Write-Host $(curProjVersion1)

- stage: Parallel
  displayName: Parallel
  dependsOn: Build
  variables:
    curProjVersion1: $[ stageDependencies.Build.Build.outputs['setCurProjVersion.curProjVersion'] ]
  jobs:
  - job: 
    pool:
      vmImage: 'windows-latest'
    steps: 
      - script: echo $(curProjVersion1)

- stage: Deploy2
  displayName: Deploy2 stage
  dependsOn: 
  - Deploy
  - Parallel
  variables:
    curProjVersion1: $[ stageDependencies.Deploy.Deploy.outputs['setCurProjVersion.curProjVersion'] ]
    curProjVersion2: $[ stageDependencies.Build.Build.outputs['setCurProjVersion.curProjVersion'] ]
  jobs:
  - job: 
    pool:
      vmImage: 'windows-latest'
    steps: 
      - script: echo $(curProjVersion1)
      # next variable is empty as dependsOn is missing  - Build.
      - script: echo $(curProjVersion2)

- stage: Deploy3
  displayName: Deploy3 stage
  dependsOn:
  - Build
  - Deploy
  - Parallel
  variables:
    curProjVersion1: $[ stageDependencies.Deploy.Deploy.outputs['setCurProjVersion.curProjVersion'] ]
    curProjVersion2: $[ stageDependencies.Build.Build.outputs['setCurProjVersion.curProjVersion'] ]
  jobs:
  - job: 
    pool:
      vmImage: 'windows-latest'
    steps: 
      - script: echo $(curProjVersion1)
      - script: echo $(curProjVersion2)
```

Have fun passing variables!

---

Reference information
- [Jobs can access output variables from previous stages](https://docs.microsoft.com/en-us/azure/devops/release-notes/2020/sprint-168-update#jobs-can-access-output-variables-from-previous-stages).
Title: How to share variables amongst Azure Pipeline agents
Date: 2021-04-21
Category: Posts
Tags: Azure Pipelines, Tips
Slug: sharing-variables-amongst-agents
Author: Willy-Peter Schaub
Summary: According to documentation, output variables can be used across stages in an Azure YAML-based pipeline. We will share a few turbulent moments we experienced while troubleshooting this feature in one of our pipeline blueprints.

The Azure Pipelines have evolved at a rapid pace during the past 2-3 years. Features we dreamt of, like passing variables between [stages](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/stages?view=azure-devops&tabs=yaml), was a big NO-NO in 2019; unless you used a convoluted workaround to save variables to disk and reloading them in the upstream stages. In May 2020, the following text raised a lot of eyebrows of joy: "_Output variables may now be used across stages in a YAML-based pipeline._."

---

# Opportunity leads to requirement

This opened a lot of opportunities for us, such as retrieving the solution's semantic version using the [GitTools](https://github.com/GitTools), and sharing it with upstream stages.

> here is our git-tools-git-version.yml template

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

We retrieve the semantic version using the git-tools-git-version.yml template in our ContinuousIntegration (CI) stage. The upstream Development, Staging, and Production stages need the variable to set the version of the universal artifact we are updating as part of the continuous deployment (CD) phase.

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

Sounds simple, right?

---

# Setting the versionToolbox Variable

After retrieving the semantic version, we run an inline PowerShell Core script to create an output variable, called **versionToolkit**.

```yml
    - task: PowerShell@2
      name: setToolkitVersion
      displayName: "Set Toolkit Version"
      inputs:
        targetType: 'inline'
        script: Write-Host "##vso[task.setvariable variable=versionToolkit;isOutput=true]$(GitVersion.MajorMinorPatch)"
```

So far so good, we are nearly done :)

Before we leave, we implement some YAML magic to create a stage variable, which is set to the value of the above versionToolkit.

> Create stage-specific versionToolkit version

```yml
- stage:         'Development'
  dependsOn:
  - ContinuousIntegration
  variables:
    versionToolkit: $[ stageDependencies.ContinuousIntegration.ContinuousIntegration.outputs['setToolkitVersion.toolkitVersion'] ]
```

Output variables are produced by steps inside of jobs and the  format of the dependency variable is **stageDependencies.\<stageName\>.\<jobName\>.outputs['stepName.variableName']**. In our case the originating stage and its job share the same name ContinuousIntegration; hence the ...ContinuousIntegration.ContinuousIntegration... stutter.

The solution worked like a charm. Today, we can go home (or leave our home office) on time.

---

# Frustration reigns

TBD

---

# After rain comes sunshine

TBD

---

Reference information
- [Jobs can access output variables from previous stages](https://docs.microsoft.com/en-us/azure/devops/release-notes/2020/sprint-168-update#jobs-can-access-output-variables-from-previous-stages).
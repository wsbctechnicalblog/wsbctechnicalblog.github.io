Title: Azure DevOps Pipeline Blueprints - Exploring the git-tools-git-version.yml template
Date: 2025-01-17
Category: Posts
Tags: azure-devops, pipelines, engineering
Slug: azure-pipeline-blueprints-explore-version
Author: Willy-Peter Schaub
Summary: Drilling Deeper: A Closer Look at the Blueprint git-tools-git-version.yml Template.

We continue our deep dive into the details of our [AzureDevOps.Automation.Pipeline.Templates.v2](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2) open source blueprint repo. Today we are going to explore the [templates/utilities/git-tools-git-version.yml](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/templates/utilities/git-tools-git-version.yml) template that is used by our continuous integration (CI) pipeline phase to calculate the semantic version of our codebase using the [gitversion.net](https://gitversion.net) open source project and generate a unique name for each pipeline instance based on this version.

> ![drilling](../images/azure-pipeline-blueprints-explore-version-1.png)

>
> "**From git log to SemVer in no time.**" - [gitversion.net](https://gitversion.net).
> GitVersion is a tool that generates a Semantic Version number based on your Git history. It can be used for various purposes, such as stamping a version number on artifacts produced during build1. GitVersion is flexible, configurable, and can be used in Continuous Server pipelines.
>

Also refer to:

- [Azure DevOps Pipeline Blueprints - Exploring the start template](/azure-pipeline-blueprints-explore-start.html).
- [Pipelines - Why bother and what are our nightmares and options?](/why-pipelines-part1.html) blog series.

---

# Today's topic - git-tools-git-version.yml

The [templates/utilities/git-tools-git-version.yml](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/templates/utilities/git-tools-git-version.yml) template has its roots in our v1 generic template era, which dates back three years. It leverages [gitversion.net](https://gitversion.net) to calculate the semantic version—a powerful open-source project that has proven invaluable in our workflows. We highly recommend taking a closer look at ABC, as it offers essential features that streamline versioning processes. We are deeply grateful to its authors for providing such a valuable tool.

```
# --------------------------------------------------------------------------
# GitTools GitVersion Template
# --------------------------------------------------------------------------
# See https://aka.ms/yaml for Azure DevOps Pipeline documentation
# 
# Special template to enable YAML pipeline users to switch to WhiteSource
# until they switch to the new blueprint-based templates
# --------------------------------------------------------------------------
# IMPORTANT !!! The GitVersion tasks must be the first to run in pipeline.
# --------------------------------------------------------------------------
# EXAMPLE USAGE:
# 
# resources:
#   repositories:
#   - repository: UtilityTemplates
#     type: git
#     name: 'Common-Engineering-System/AzureDevOps.Automation.Pipeline.Templates'
#       ref: refs/heads/master
#
# stages:
# - stage: ContinuousIntegration
#   displayName: Continuous Integration
#   jobs:
#   - job: ContinuousIntegration
#     steps:
#     - template: Templates/Utility/git-tools-git-version.yml@UtilityTemplates
#       parameters:
#         versionSpec:                '5.x'
#         useConfigFile:              true
#         configFilePath:             '$(Build.SourcesDirectory)\Src\GitVersion.yml'
#         updateAssemblyInfo:         true
#         targetPath:                 $(Build.SourcesDirectory)/$(Build.Repository.Name)
#
# --------------------------------------------------------------------------

parameters:
- name:     portfolioName
  type:     string
  default:  ''  # TODO: to be removed once this parameter is not optional
- name:     productName
  type:     string
  default:  ''  # TODO: to be removed once this parameter is not optional
- name:     versionSpec
  type:     string
  default:  '5.11.x' # switch from 5.6.3 to 5.11.x as default
- name:     useConfigFile
  type:     boolean
  default:  false
- name:     targetPath
  type:     string
  default:  $(Build.SourcesDirectory)/$(Build.Repository.Name)
- name:     configFilePath
  type:     string
  default:  ''
- name:     updateAssemblyInfo
  type:     boolean
  default:  false
- name:     updateAssemblyInfoFilename
  type:     string
  default:  ''
- name:     additionalArguments
  type:     string
  default:  ''
  
steps:
  - task: gitversion/setup@3 
    displayName: Install GitVersion
    inputs:
      versionSpec: ${{parameters.versionSpec}}

  - task: gitversion/execute@3
    displayName: Use GitVersion
    inputs:
      targetPath:                   ${{parameters.targetPath}}
      useConfigFile:                ${{parameters.useConfigFile}}
      configFilePath:               ${{parameters.configFilePath}}
      updateAssemblyInfo:           ${{parameters.updateAssemblyInfo}}
      updateAssemblyInfoFilename:   ${{parameters.updateAssemblyInfoFilename}}
      additionalArguments:          ${{parameters.additionalArguments}}

  - powershell: |
      Write-Host "##vso[task.setvariable variable=semVersion;isOutput=true]$(GitVersion.MajorMinorPatch)"
      Write-Host "##vso[task.setvariable variable=patchVersion;isOutput=true]$(GitVersion.Patch)"
    name:         setSemVersion
    displayName:  Set Semantic Version
    failOnStderr: true

  - ${{ if and(ne(parameters.portfolioName, ''), ne(parameters.productName, '')) }}: # TODO: to be removed once portfolioName and productName parameters are not optional
    - powershell: |
        $BuildNumber = "${{parameters.portfolioName}}_${{parameters.productName}}_$(GitVersion.MajorMinorPatch)_$(Get-Date -format yyyyMMdd).$(Get-Date -format HHmmss).$(Build.SourceBranchName)"
        Write-Host "##vso[build.updatebuildnumber]$BuildNumber"
      displayName: Update Build Number
      failOnStderr: true

```

---

# Drill-down

The first two steps of the template **setup** the [gitversion.net](https://gitversion.net) tool and then **run** the tool to generate the Semantic Versioning (SemVer). 

**Semantic versioning** is a widely used versioning system that follows the format MAJOR.MINOR.PATCH, where:

- **MAJOR**: Incremented for incompatible changes.
- **MINOR**: Incremented for backward-compatible new features.
- **PATCH**: Incremented for backward-compatible bug fixes.

```
  - task: gitversion/setup@3 
    displayName: Install GitVersion
    inputs:
      versionSpec: ${{parameters.versionSpec}}

  - task: gitversion/execute@3
    displayName: Use GitVersion
    inputs:
      targetPath:                   ${{parameters.targetPath}}
      useConfigFile:                ${{parameters.useConfigFile}}
      configFilePath:               ${{parameters.configFilePath}}
      updateAssemblyInfo:           ${{parameters.updateAssemblyInfo}}
      updateAssemblyInfoFilename:   ${{parameters.updateAssemblyInfoFilename}}
      additionalArguments:          ${{parameters.additionalArguments}}
```

The third step is a ```PowerShell``` command sets two variables in an Azure DevOps pipeline to make them available for subsequent tasks.

```
powershell: |
      Write-Host "##vso[task.setvariable variable=semVersion;isOutput=true]$(GitVersion.MajorMinorPatch)"
      Write-Host "##vso[task.setvariable variable=patchVersion;isOutput=true]$(GitVersion.Patch)"
    name:         setSemVersion
    displayName:  Set Semantic Version
    failOnStderr: true
```

- ```##vso[task.setvariable variable=semVersion;isOutput=true]``` is an Azure DevOps-specific logging command to set a variable that can be accessed by other tasks in the pipeline. 
- ```variable=semVersion``` and ```variable=patchVersion``` are the names of the variables being set, the former containing the MAJOR.MINOR and the latter the PATCH pert of the SemVer.
- ```isOutput=true``` makes the variable available as an output variable for other pipeline jobs.
- ```$(GitVersion.MajorMinorPatch)``` is a reference to a variable output from the GitVersion tool, which contains the calculated semantic version numbers.

The last step is conditional, if and only if both the portfolio and product names are blank. It is another ```PowerShell``` command that formats and sets the ```$BuildNumber```, which is a predefined Azure Pipeline variable that represents the build number assigned to your pipeline run.

```
  - ${{ if and(ne(parameters.portfolioName, ''), ne(parameters.productName, '')) }}: # TODO: to be removed once portfolioName and productName parameters are not optional
    - powershell: |
        $BuildNumber = "${{parameters.portfolioName}}_${{parameters.productName}}_$(GitVersion.MajorMinorPatch)_$(Get-Date -format yyyyMMdd).$(Get-Date -format HHmmss).$(Build.SourceBranchName)"
        Write-Host "##vso[build.updatebuildnumber]$BuildNumber"
      displayName: Update Build Number
      failOnStderr: true
```

---

# Questions

### For my team

- Q1: We refer to portfolios and applications, not portfolios and products in our naming guidelines. Should we not align our v2 CI/CD blueprint templates accordingly?

### For you

- Q2: Are your using the [gitversion.net](https://gitversion.net) tool? If yes, which version and with which CI/CD Server?

---

Any questions or suggested improvements?

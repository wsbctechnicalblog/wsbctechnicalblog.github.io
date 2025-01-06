Title: Azure DevOps Pipeline Blueprints - Exploring the git-tools-git-version.yml template
Date: 2025-01-17
Category: Posts
Tags: azure-devops, pipelines, engineering
Slug: azure-pipeline-blueprints-explore-version
Author: Willy-Peter Schaub
Summary: Drilling Deeper: A Closer Look at the Blueprint git-tools-git-version.yml Template.

We continue our deep dive into the details of our [templates/utilities/git-tools-git-version.yml](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/templates/utilities/git-tools-git-version.yml) open source blueprint templates. Today we are going to explore a template that is used by our continuous integration (CI) pipeline phase to calculate the semantic version of our codebase using the [gitversion.net](https://gitversion.net) open source project and generate a unique name for each pipeline instance based on this version.

> ![drilling](../images/azure-pipeline-blueprints-explore-version-1.png)

>
> "**From git log to SemVer in no time.**" - [gitversion.net](https://gitversion.net).
> GitVersion is a tool that generates a Semantic Version number based on your Git history. It can be used for various purposes, such as stamping a version number on artifacts produced during build1. GitVersion is flexible, configurable, and can be used in Continuous Server pipelines.
>

Also refer to:

- [Azure DevOps Pipeline Blueprints - Exploring the start template](/azure-pipeline-blueprints-explore-start.html).
- [Pipelines - Why bother and what are our nightmares and options?](/why-pipelines-part1.html) blog series.

---

# Today's topic - git-tools-git-version.yml.yml

The [templates/utilities/git-tools-git-version.yml](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/templates/utilities/git-tools-git-version.yml) template has its roots in our v1 generic template era, which dates back three years. It leverages ABC to calculate the semantic version—a powerful open-source project that has proven invaluable in our workflows. We highly recommend taking a closer look at ABC, as it offers essential features that streamline versioning processes. We are deeply grateful to its authors for providing such a valuable component.

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

TBD

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

TBD

```
powershell: |
      Write-Host "##vso[task.setvariable variable=semVersion;isOutput=true]$(GitVersion.MajorMinorPatch)"
      Write-Host "##vso[task.setvariable variable=patchVersion;isOutput=true]$(GitVersion.Patch)"
    name:         setSemVersion
    displayName:  Set Semantic Version
    failOnStderr: true
```

TBD

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

- Q1: TBD

### For you

- Q2: TBD

---

Any questions or suggested improvements?

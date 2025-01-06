Title: Azure DevOps Pipeline Blueprints - Exploring the git-tools-git-version.yml template
Date: 2025-01-22
Category: Posts
Tags: azure-devops, pipelines, engineering
Slug: azure-pipeline-blueprints-explore-version
Author: Willy-Peter Schaub
Summary: Drilling Deeper: A Closer Look at the Blueprint info-version.yml Template.

We continue our deep dive into the details of our [AzureDevOps.Automation.Pipeline.Templates.v2](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2) open source blueprint repo. Today we are going to explore the [templates/utilities/info-version.yml](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/templates/utilities/info-version.yml) template, designed to capture and present detailed information about the pipeline instance, facilitating security reviews and enabling future analysis.

> ![drilling](../images/azure-pipeline-blueprints-explore-info-1.png)

Also refer to:

- [Azure DevOps Pipeline Blueprints - Exploring the start template](/azure-pipeline-blueprints-explore-start.html).
- [Azure DevOps Pipeline Blueprints - Exploring the version template](/azure-pipeline-blueprints-explore-version.html).
- [Pipelines - Why bother and what are our nightmares and options?](/why-pipelines-part1.html) blog series.

---

# Today's topic - info-version.yml

Today we peek into the [templates/utilities/info-version.yml](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/templates/utilities/info-version.yml) template which has one purpose - capture information about the pipeline instance for future reference.

```
# --------------------------------------------------------------------------
# info-version Template
# --------------------------------------------------------------------------
# See https://aka.ms/yaml for Azure DevOps Pipeline documentation
# 
# --------------------------------------------------------------------------

parameters:
# mandatory parameters
- name:     modeElite
  type:     boolean
- name:     applicationBlueprint
  type:     string
- name:     applicationType
  type:     string
# default parameters
- name:     vGuid
  type:     string
  default:  '__TODO_ADD_UNIQUE_GUID__HERE__'
- name:     vVersion
  type:     string
  default:  '2.0'
  
steps:
    - script: echo "${{parameters.modeElite}}:${{parameters.applicationBlueprint}}:${{parameters.applicationType}}:${{parameters.vGuid}}:${{parameters.vVersion}}
      name:         BootstrapInfo
      displayName:  Bootstrap Info
    - task: PowerShell@2
      inputs:
        targetType: 'inline'
        script: |
          Write-Host "##vso[task.setvariable variable=bootStrapModeElite;isOutput=true]${{parameters.modeElite}}"
          Write-Host "##vso[task.setvariable variable=bootStrapBlueprint;isOutput=true]${{parameters.applicationBlueprint}}"
          Write-Host "##vso[task.setvariable variable=bootStrapType;isOutput=true]${{parameters.applicationType}}"
          Write-Host "##vso[task.setvariable variable=bootStrapGuid;isOutput=true]${{parameters.vGuid}}"
          Write-Host "##vso[task.setvariable variable=bootStrapVersion;isOutput=true]${{parameters.vVersion}}"
        failOnStderr: true
        pwsh: true
      name:         BootstrapVars
      displayName:  Bootstrap Vars

# --------------------------------------------------------------------------
# Generate pipeline info and save it to a JSON file
# --------------------------------------------------------------------------
    - task: PowerShell@2
      displayName:  Bootstrap generate pipeline info
      inputs:
        targetType: 'inline'
        pwsh: true
        script: |
          $variablesData = [PSCustomObject]@{
              bootStrapModeElite = "${{parameters.modeElite}}"
              bootStrapBlueprint = "${{parameters.applicationBlueprint}}"
              bootStrapType = "${{parameters.applicationType}}"
              bootStrapGuid = "${{parameters.vGuid}}"
              bootStrapVersion = "${{parameters.vVersion}}"
          }

          $json = $variablesData | ConvertTo-Json
          $jsonFilePath = "$(Agent.TempDirectory)/pipe-info.json"
          $json | Out-File -FilePath $jsonFilePath
          Write-Host "JSON file saved to $jsonFilePath"
          
    # Publish pipeline info
    - task: PublishBuildArtifacts@1
      displayName: Bootstrap publish pipeline info
      inputs:
        PathtoPublish: "$(Agent.TempDirectory)/pipe-info.json"
        ArtifactName: 'pipe-info'
```

---

# Drill-down

The second step is a ```PowerShell``` command sets five variables in an Azure DevOps pipeline to make them available for subsequent tasks.

```
    - task: PowerShell@2
      inputs:
        targetType: 'inline'
        script: |
          Write-Host "##vso[task.setvariable variable=bootStrapModeElite;isOutput=true]${{parameters.modeElite}}"
          Write-Host "##vso[task.setvariable variable=bootStrapBlueprint;isOutput=true]${{parameters.applicationBlueprint}}"
          Write-Host "##vso[task.setvariable variable=bootStrapType;isOutput=true]${{parameters.applicationType}}"
          Write-Host "##vso[task.setvariable variable=bootStrapGuid;isOutput=true]${{parameters.vGuid}}"
          Write-Host "##vso[task.setvariable variable=bootStrapVersion;isOutput=true]${{parameters.vVersion}}"
        failOnStderr: true
        pwsh: true
      name:         BootstrapVars
      displayName:  Bootstrap Vars
```
For example:

- ```##vso[task.setvariable variable=bootStrapModeElite;isOutput=true]``` is an Azure DevOps-specific logging command to set a variable that can be accessed by other tasks in the pipeline. 
- ```bootStrapModeElite``` is the name of the variable being set. In this case it is the variable that defines whether we are serious about quality (true) or noe (false).
- ```isOutput=true``` makes the variable available as an output variable for other pipeline jobs.
- ```parameters.modeElite``` is a reference to a parameter that is passed around the templates.

>
> ![alert](../images/alert-tiny.png)
>
> Refer to [Gotchas when sharing variables with Azure DevOps stages and jobs](/sharing-variables-with-stages-and-jobs.html) is you are planning to share the variables amongst jobs and stages.
>

While these variables work seamlessly for reuse within YAML-based pipelines or across different jobs, we encountered an issue with our classic Azure Pipelines, which consist of a YAML-based continuous integration (CI) pipeline and an older, classic release pipeline for continuous delivery. The variables did not flow between the new and legacy environments, and modifying thousands of legacy release pipelines was simply not feasible.

This brings us to the second half of the template, which creates a json file with the variables and their values, and publishes them to the Azure Pipeline artifacts. The Powershell task runs an ```inline``` script that creates a PowerShell custom object ```$variablesData``` with properties that are populated using template parameters.

The scripts last four steps performs the following steps:

- Converts the ```$variablesData``` object to **JSON** format.
- Defines the file path for the JSON file in the agent's temporary directory.
- Writes the JSON content to the specified file.
- Outputs a message indicating the file path where the JSON file was saved.

```
    - task: PowerShell@2
      displayName:  Bootstrap generate pipeline info
      inputs:
        targetType: 'inline'
        pwsh: true
        script: |
          $variablesData = [PSCustomObject]@{
              bootStrapModeElite = "${{parameters.modeElite}}"
              bootStrapBlueprint = "${{parameters.applicationBlueprint}}"
              bootStrapType = "${{parameters.applicationType}}"
              bootStrapGuid = "${{parameters.vGuid}}"
              bootStrapVersion = "${{parameters.vVersion}}"
          }

          $json = $variablesData | ConvertTo-Json
          $jsonFilePath = "$(Agent.TempDirectory)/pipe-info.json"
          $json | Out-File -FilePath $jsonFilePath
          Write-Host "JSON file saved to $jsonFilePath"
```

Lastly, the template publishes the ```pipe-info.json``` file located in the agent's temporary directory as a build artifact named ```pipe-info```. Going forward, our quality and security automation, as well as the 2AM incident root cause analysis, can find the pipeline information such as how serious we were about quality, the application-type blueprints used, the suggested application type, and the blueprint template version.

```
    # Publish pipeline info
    - task: PublishBuildArtifacts@1
      displayName: Bootstrap publish pipeline info
      inputs:
        PathtoPublish: "$(Agent.TempDirectory)/pipe-info.json"
        ArtifactName: 'pipe-info'
```

That is it for today!

---

# Questions

### For my team

- Q1: What other information should we save in the ```pipe-info``` artifact?

### For you

- Q2: What other information is important for your CI/CD pipelines to track quality and governance?

---

Any questions or suggested improvements?

Title: Azure DevOps Pipeline Blueprints - Exploring the Continuous Delivery (CD) templates
Date: 2025-02-05
Category: Posts
Tags: azure-devops, pipelines, engineering
Slug: azure-pipeline-blueprints-explore-cd
Author: Willy-Peter Schaub
Summary: Drilling Deeper: A Closer Look at the Blueprint Continuous Delivery (CD) Templates.

We continue our deep dive into the details of our [AzureDevOps.Automation.Pipeline.Templates.v2](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2) open source blueprint repo. Today we are going to explore the [blueprints/universal-artifact/azure-pipeline-universal-artifact-cd.yml](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/blueprints/universal-artifact/azure-pipeline-universal-artifact-cd.yml) and [blueprints/universal-artifact/azure-pipeline-universal-artifact-cd-stage.yml](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/blueprints/universal-artifact/azure-pipeline-universal-artifact-cd-stage.yml) templates, which are part of our Universal Azure Artifact templates.

> ![drilling](../images/azure-pipeline-blueprints-explore-cd-0.png)

Also refer to:

- [Azure DevOps Pipeline Blueprints - Exploring the start template](/azure-pipeline-blueprints-explore-start.html).
- [Azure DevOps Pipeline Blueprints - Exploring the version template](/azure-pipeline-blueprints-explore-version.html).
- [Azure DevOps Pipeline Blueprints - Exploring the info template](/azure-pipeline-blueprints-explore-info.html).
- [Azure DevOps Pipeline Blueprints - Exploring the QA Scan templates](/azure-pipeline-blueprints-explore-qa-scans.html).
- [Pipelines - Why bother and what are our nightmares and options?](/why-pipelines-part1.html) blog series.
- [How to share variables amongst Azure Pipeline agents](/sharing-variables-amongst-agents.html).
- [Gotchas when sharing variables with Azure DevOps stages and jobs](/sharing-variables-with-stages-and-jobs.html).

---

# Today's topics - azure-pipeline-universal-artifact-cd.yml and azure-pipeline-universal-artifact-cd-stage.yml templates

Today we start with the [blueprints/universal-artifact/azure-pipeline-universal-artifact-cd.yml](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/blueprints/universal-artifact/azure-pipeline-universal-artifact-cd.yml) template which is triggered by the ```*-control.yml``` template, which controls the Continuous Delivery (CD) flow, and calls the various review, security, and QA scans.

> **azure-pipeline-universal-artifact-cd.yml.yml**

```
parameters:
- name:     stage
  type:     object
  
stages:

# -----------------------------------------------------------------------------------------------------
# DEVELOPMENT STAGE
# -----------------------------------------------------------------------------------------------------
- ${{ if eq(parameters.stage.development.config.active, true) }}:
  - template: /blueprints/universal-artifact/azure-pipeline-universal-artifact-cd-stage.yml@CeBlueprints
    parameters:
      name:                           Development
      displayName:                    Development (DV)
      config:                         ${{parameters.stage.development.config}}
      dependsOn:
      - ContinuousIntegration

# -----------------------------------------------------------------------------------------------------
# SYSTEM TEST STAGE
# -----------------------------------------------------------------------------------------------------
- ${{ if eq(parameters.stage.systemTest.config.active, true) }}:
  - template: /blueprints/universal-artifact/azure-pipeline-universal-artifact-cd-stage.yml@CeBlueprints
    parameters:
      name:                           SystemTest
      displayName:                    System Test (SY)
      config:                         ${{parameters.stage.systemTest.config}}
      dependsOn:
      - ContinuousIntegration
      - ${{ if eq(parameters.stage.development.config.active, true) }}:
        - Development

# -----------------------------------------------------------------------------------------------------
# SECURITY AUTOMATION STAGE
# -----------------------------------------------------------------------------------------------------
- template: /templates/dev-sec-ops/azure-pipeline-security-auto.yml@CeBlueprints
  parameters:
    applicationBlueprint: ${{parameters.stage.securityAutomation.applicationBlueprint}}
    modeElite:            ${{parameters.stage.securityAutomation.modeElite}}
    dependsOn:
    - ContinuousIntegration
    - ${{ if eq(parameters.stage.development.config.active, true) }}:
      - Development
    - ${{ if eq(parameters.stage.systemTest.config.active, true) }}:
      - SystemTest

# -----------------------------------------------------------------------------------------------------
# QA SCANS STAGE
# -----------------------------------------------------------------------------------------------------
- template: /templates/qa/azure-pipeline-qa-scans.yml@CeBlueprints
  parameters:
    applicationBlueprint: ${{parameters.stage.qaScans.applicationBlueprint}}
    modeElite:            ${{parameters.stage.qaScans.modeElite}}
    dependsOn:
    - ContinuousIntegration
    - ${{ if eq(parameters.stage.development.config.active, true) }}:
      - Development
    - ${{ if eq(parameters.stage.systemTest.config.active, true) }}:
      - SystemTest


# -----------------------------------------------------------------------------------------------------
# SECURITY REVIEW STAGE
# -----------------------------------------------------------------------------------------------------
- ${{ if or(eq(variables['Build.SourceBranch'], 'refs/heads/release'), startsWith(variables['Build.SourceBranch'], 'refs/heads/release/')) }}:
  - template: /templates/dev-sec-ops/azure-pipeline-security-review.yml@CeBlueprints
    parameters:
      applicationBlueprint: ${{parameters.stage.securityReview.applicationBlueprint}}
      stageEnvName:         ${{parameters.stage.securityReview.envName}}
      dependsOn:
      - ContinuousIntegration
      - ${{ if eq(parameters.stage.development.config.active, true) }}:
        - Development
      - ${{ if eq(parameters.stage.systemTest.config.active, true) }}:
        - SystemTest
      - SecurityAutomation

# -----------------------------------------------------------------------------------------------------
# STAGING STAGE
# -----------------------------------------------------------------------------------------------------
- ${{ if and(eq(parameters.stage.staging.config.active, true), or(eq(variables['Build.SourceBranch'], 'refs/heads/release'), startsWith(variables['Build.SourceBranch'], 'refs/heads/release/'))) }}:
  - template: /blueprints/universal-artifact/azure-pipeline-universal-artifact-cd-stage.yml@CeBlueprints
    parameters:
      name:                           Staging
      displayName:                    Staging (ST)
      config:                         ${{parameters.stage.staging.config}}
      dependsOn:
      - ContinuousIntegration
      - ${{ if eq(parameters.stage.development.config.active, true) }}:
        - Development
      - ${{ if eq(parameters.stage.systemTest.config.active, true) }}:
        - SystemTest
      - QAScans
      - SecurityAutomation
      - SecurityReview

# -----------------------------------------------------------------------------------------------------
# PRE-PROD AUTOMATION SCANS STAGE
# -----------------------------------------------------------------------------------------------------
- ${{ if and(eq(parameters.stage.production.config.active, true), or(eq(variables['Build.SourceBranch'], 'refs/heads/release'), startsWith(variables['Build.SourceBranch'], 'refs/heads/release/'))) }}:
  - template: /templates/pre-prod/azure-pipeline-pre-prod-automation.yml@CeBlueprints
    parameters:
      applicationBlueprint: ${{parameters.stage.preProdAutomation.applicationBlueprint}}
      modeElite:            ${{parameters.stage.preProdAutomation.modeElite}}
      dependsOn:
        - ContinuousIntegration
        - ${{ if eq(parameters.stage.development.config.active, true) }}:
          - Development
        - ${{ if eq(parameters.stage.systemTest.config.active, true) }}:
          - SystemTest
        - QAScans
        - SecurityAutomation
        - SecurityReview
        - ${{ if eq(parameters.stage.staging.config.active, true) }}:
          - Staging

# -----------------------------------------------------------------------------------------------------
# PRODUCTION STAGE
# -----------------------------------------------------------------------------------------------------
- ${{ if and(eq(parameters.stage.production.config.active, true), or(eq(variables['Build.SourceBranch'], 'refs/heads/release'), startsWith(variables['Build.SourceBranch'], 'refs/heads/release/'))) }}:
  - template: /blueprints/universal-artifact/azure-pipeline-universal-artifact-cd-stage.yml@CeBlueprints
    parameters:
      name:                           Production
      displayName:                    Production (PR)
      config:                         ${{parameters.stage.production.config}}
      dependsOn:
      - ContinuousIntegration
      - ${{ if eq(parameters.stage.development.config.active, true) }}:
        - Development
      - ${{ if eq(parameters.stage.systemTest.config.active, true) }}:
        - SystemTest
      - QAScans
      - SecurityAutomation
      - SecurityReview
      - ${{ if eq(parameters.stage.staging.config.active, true) }}:
        - Staging
      - PreProdAutomation
```

This template, as shown above, triggers the [blueprints/universal-artifact/azure-pipeline-universal-artifact-cd-stage.yml](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/blueprints/universal-artifact/azure-pipeline-universal-artifact-cd-stage.yml) template for each deployment stage.

> **azure-pipeline-universal-artifact-cd-stage.yml**

```
parameters:
- name:     name
  type:     string
- name:     displayName
  type:     string
- name:     config
  type:     object
  default:  []
- name:     dependsOn
  type:     object
  default:  []

stages:

# -----------------------------------------------------------------------------------------------------
# STAGE
# -----------------------------------------------------------------------------------------------------

- stage:         ${{parameters.name}}
  displayName:   ${{parameters.displayName}}
  ${{ if ne(length(parameters.dependsOn), 0) }}:
    dependsOn:
      - ${{ each stage in parameters.dependsOn }}:
        - ${{stage}}
  variables:
      currentVersion: $[ stageDependencies.ContinuousIntegration.ContinuousIntegration.outputs['setSemVersion.semVersion'] ]
  pool:
    vmImage:     ${{parameters.config.nameVM}}
  jobs:
  - deployment:  ${{parameters.name}}
    environment: ${{parameters.config.nameEnv}}
    strategy:
      runOnce:
        deploy:
          steps:
          - script: echo Toolkit Version = $(currentVersion)
          # For release we enforce the toolkit version
          - ${{ if or(eq(variables['Build.SourceBranch'], 'refs/heads/release'), startsWith(variables['Build.SourceBranch'], 'refs/heads/release/')) }}:
            - task: UniversalPackages@0
              name: Create_Universal_Package
              inputs:
                command: 'publish'
                publishDirectory:       $(Agent.BuildDirectory)/drop
                feedsToUsePublish:      'internal'
                vstsFeedPublish:        ${{parameters.config.feedPublish}}
                vstsFeedPackagePublish: ${{parameters.config.packagePublish}}
                versionOption:          'custom'
                versionPublish:         $(currentVersion)
          # For non-release we increment the minor version so that we do not have to tag for DV feeds
          - ${{ if not(or(eq(variables['Build.SourceBranch'], 'refs/heads/release'), startsWith(variables['Build.SourceBranch'], 'refs/heads/release/'))) }}:
            - task: UniversalPackages@0
              name: Create_Universal_Package
              inputs:
                command: 'publish'
                publishDirectory:       $(Agent.BuildDirectory)/drop
                feedsToUsePublish:      'internal'
                vstsFeedPublish:        ${{parameters.config.feedPublish}}
                vstsFeedPackagePublish: ${{parameters.config.packagePublish}}
```

---

# Drill-down

### azure-pipeline-universal-artifact-cd.yml nuggets

Let us take a look at the ```azure-pipeline-universal-artifact-cd.yml``` blueprint template, which defines the deployment and validation stages, specifying when they are triggered and in what sequence. The first YAML snippet is part of an Azure DevOps pipeline configuration, specifically handling conditional deployment for the Production stage in a universal artifact deployment pipeline.

> **Gem 1**

```
- ${{ if and(eq(parameters.stage.production.config.active, true), or(eq(variables['Build.SourceBranch'], 'refs/heads/release'), startsWith(variables['Build.SourceBranch'], 'refs/heads/release/'))) }}:
  - template: /blueprints/universal-artifact/azure-pipeline-universal-artifact-cd-stage.yml@CeBlueprints
    parameters:
      name:                           Production
      displayName:                    Production (PR)
      config:                         ${{parameters.stage.production.config}}
      dependsOn:
      - ContinuousIntegration
      - ${{ if eq(parameters.stage.development.config.active, true) }}:
        - Development
      - ${{ if eq(parameters.stage.systemTest.config.active, true) }}:
        - SystemTest
      - QAScans
      - SecurityAutomation
      - SecurityReview
      - ${{ if eq(parameters.stage.staging.config.active, true) }}:
        - Staging
      - PreProdAutomation
```

Let us break it down.

- The YAML snippet runs only if ```parameters.stage.production.config.active``` is **true** (enabled in the *-config.yml file and if the build source branch is ```refs/heads/release``` or any sub-branch under ```refs/heads/release/```, for example refs/heads/release/v1.2.3.
- Uses the ```azure-pipeline-universal-artifact-cd-stage.yml``` template and passes parameters like name, displayName, and the config object.
- Establishes dependencies on multiple preceding stages to dictate the execution sequence and inherit variables from earlier stages, as outlined in [How to share variables amongst Azure Pipeline agents](/sharing-variables-amongst-agents.html) and [Gotchas when sharing variables with Azure DevOps stages and jobs](/sharing-variables-with-stages-and-jobs.html).

### azure-pipeline-universal-artifact-cd-stage.yml nuggets

Next, let us peek into the template used by the ```*-cd.yml``` template.

> **Gem 2**

```
- name:     config
  type:     object
  default:  []
- name:     dependsOn
  type:     object
  default:  []
```

This YAML snippet defines two parameters:

- The ```config``` parameter is by default an empty array, but in our case stores pipeline configuration settings.
- The ```dependsOn``` parameter, also by default an empty array, specifies dependencies between stages/jobs, determining execution order.

> **Gem 2**

```
  variables:
      currentVersion: $[ stageDependencies.ContinuousIntegration.ContinuousIntegration.outputs['setSemVersion.semVersion'] ]
```

This line defines a pipeline variable named currentVersion, which retrieves its value from the calculated version as we discussed in [Azure DevOps Pipeline Blueprints - Exploring the version template](/azure-pipeline-blueprints-explore-version.html).

- The first ```ContinuousIntegration``` refers to the stage name.
- The second ```ContinuousIntegration``` refers to the job name within that stage.
- ```setSemVersion``` refers a step within the job.
- ```semVersion``` is the output variable from that task.

> ***Gem 3**

```
- ${{ if or(eq(variables['Build.SourceBranch'], 'refs/heads/release'), startsWith(variables['Build.SourceBranch'], 'refs/heads/release/')) }}:
  - task: UniversalPackages@0
    name: Create_Universal_Package
    inputs:
      command: 'publish'
      publishDirectory:       $(Agent.BuildDirectory)/drop
      feedsToUsePublish:      'internal'
      vstsFeedPublish:        ${{parameters.config.feedPublish}}
      vstsFeedPackagePublish: ${{parameters.config.packagePublish}}
      versionOption:          'custom'
      versionPublish:         $(currentVersion)
```

This YAML snippet defines a conditional step publishes a Universal Package to an internal feed when triggered from a release branch, using:

- The ```UniversalPackages``` task to publish artifacts.
- Upload the package from ```$(Agent.BuildDirectory)/drop```.
- The feed and package details aprovided via ```parameters.config```.
- Using ```$(currentVersion)```, as set in the ContinuousIntegration stage, to set the custom version.

That is a wrap for today.

---

# Questions

### For my team

- Q1: Every time I look at the per app-type control and cd blueprint template, I wonder - can we not standardize and share common templates?

### For you

- Q2: How are you dealing with the cd phase of your pipeline and integration of infrastructure as code (IaC)? 

---

Any questions or suggested improvements?

Title: Azure DevOps Pipeline Blueprints - Exploring the QA Scan template9s)
Date: 2025-01-XX
Category: Posts
Tags: azure-devops, pipelines, engineering
Slug: azure-pipeline-blueprints-explore-qa-scans
Author: Willy-Peter Schaub
Summary: Drilling Deeper: A Closer Look at the Blueprint Quality Assurance (QA) Scan Templates.

We continue our deep dive into the details of our [AzureDevOps.Automation.Pipeline.Templates.v2](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2) open source blueprint repo. Today we are going to explore the [templates/qa/azure-pipeline-qa-scans.yml](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/templates/qa/azure-pipeline-qa-scans.yml) and [templates/qa/qa-scans-cd.yml](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/templates/qa/qa-scans-cd.yml) templates, designed to run the quality assurance validations.

> ![drilling](../images/azure-pipeline-blueprints-explore-qa-scans-1.png)

Also refer to:

- [Azure DevOps Pipeline Blueprints - Exploring the start template](/azure-pipeline-blueprints-explore-start.html).
- [Azure DevOps Pipeline Blueprints - Exploring the version template](/azure-pipeline-blueprints-explore-version.html).
- [Azure DevOps Pipeline Blueprints - Exploring the info template](/azure-pipeline-blueprints-explore-info.html).
- [Pipelines - Why bother and what are our nightmares and options?](/why-pipelines-part1.html) blog series.

---

# Today's topics - azure-pipeline-qa-scans.yml and qa-scans-cd.yml

Today we peek into the [templates/qa/azure-pipeline-qa-scans.yml](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/templates/qa/azure-pipeline-qa-scans.yml) template which is triggered be the continuous delivery (cd) template and has one purpose, to trigger the [templates/qa/qa-scans-cd.yml](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/templates/qa/qa-scans-cd.yml) and in fiture, other QA templates.

> azure-pipeline-qa-scans.yml

```
parameters:
- name:     dependsOn
  type:     object
  default:  []
- name:     applicationBlueprint
  type:     string
- name:     modeElite
  type:     boolean
  default:  false

stages:
# ---------------------------------------------------------------------------
# QUALITY ASSURANCE SCANS STAGE
# ---------------------------------------------------------------------------
- stage:         'QAScans'
  displayName:   'Quality Assurance (QA)'
  dependsOn:
  - ${{ each stage in parameters.dependsOn }}:
    - ${{stage}}
  pool:
    vmImage:      'ubuntu-latest'
  jobs:
  - job:          'QAScans'
    steps:
    # List all environment variables within this agent
    - bash: 'env | sort'
      displayName: Bootstrap Dump env variables
    
    # Inject the QA scans template into the pipeline
    - template:   /templates/qa/qa-scans-cd.yml@CeBlueprints
      parameters:
        applicationBlueprint: ${{parameters.applicationBlueprint}}
        modeElite:            ${{parameters.modeElite}}
```
> qa-scans-cd.yml

```
parameters:
- name:     applicationBlueprint
  type:     string
- name:     modeElite
  type:     boolean
  default:  false
  
steps:
# ---------------------------------------------------------------------------
# QA AUTOMATION FOR LOWER (NON-PROD) ENVIRONMENTS STAGE
# ---------------------------------------------------------------------------
- ${{ if not(or(eq(variables['Build.SourceBranch'], 'refs/heads/release'), startsWith(variables['Build.SourceBranch'], 'refs/heads/release/'))) }}:
  - script: echo 'QA CD Lower Environment Automation Placeholder ****************************************'
  - script: echo applicationBlueprint = ${{parameters.applicationBlueprint}}
  - script: echo modeElite = ${{parameters.modeElite}}
  
  - ${{ if eq( lower(parameters.applicationBlueprint), 'azure-function' ) }}:
    - script: echo deal with qa scan relevant to azure-function application type

  - ${{ if eq( lower(parameters.applicationBlueprint), 'nuget-package' ) }}:
    - script: echo deal with qa scan relevant to nuget-package application type

  - ${{ if eq( lower(parameters.applicationBlueprint), 'universal-artifact' ) }}:
    - script: echo deal with qa scan relevant to universal-artifact application type

  - ${{ if eq( lower(parameters.applicationBlueprint), 'reliable-web-app' ) }}:
    - script: |
              '$(Build.SourcesDirectory)/AzureDevOps.Automation.Pipeline.Toolbox.v2/toolbox/scripts/quality-assurance/robot-install.ps1'
              robot --outputdir %BUILD_ARTIFACTSTAGINGDIRECTORY% --timestampoutputs --log mylog.html --report NONE -x RESULTSET-robottests.xml %BUILD_SOURCESDIRECTORY%\toolbox\quality-assurance\RobotScripts\HealthCheck.robot
    

  - ${{ if and(ne(lower(parameters.applicationBlueprint),'universal-artifact'), ne(lower(parameters.applicationBlueprint),'nuget-package'), ne(lower(parameters.applicationBlueprint),'reliable-web-app'), ne(lower(parameters.applicationBlueprint),'azure-function')) }}:
    - script: echo UNKNOWN application type

# ---------------------------------------------------------------------------
# QA AUTOMATION FOR HIGHER (PROD) ENVIRONMENTS STAGE
# ---------------------------------------------------------------------------
- ${{ if or(eq(variables['Build.SourceBranch'], 'refs/heads/release'), startsWith(variables['Build.SourceBranch'], 'refs/heads/release/')) }}:
  - script: echo 'QA CD Higher Environment Automation Placeholder ****************************************'
  - script: echo applicationBlueprint = ${{parameters.applicationBlueprint}}
  - script: echo modeElite = ${{parameters.modeElite}}

  - ${{ if eq( lower(parameters.applicationBlueprint), 'azure-function' ) }}:
    - script: echo deal with qa scan relevant to azure-function application type

  - ${{ if eq( lower(parameters.applicationBlueprint), 'nuget-package' ) }}:
    - script: echo deal with qa scan relevant to nuget-package application type

  - ${{ if eq( lower(parameters.applicationBlueprint), 'universal-artifact' ) }}:
    - script: echo deal with qa scan relevant to universal-artifact application type

  - ${{ if and(ne(lower(parameters.applicationBlueprint),'universal-artifact'), ne(lower(parameters.applicationBlueprint),'nuget-package'), ne(lower(parameters.applicationBlueprint),'azure-function')) }}:
    - script: echo UNKNOWN application type

# ---------------------------------------------------------------------------
# QA AUTOMATION FOR LOWER AND HIGHER (PROD) ENVIRONMENTS STAGE
# ---------------------------------------------------------------------------
- script: echo 'QA CD Lower and Higher Environment Automation Placeholder ***********************************'

- ${{ if eq( lower(parameters.applicationBlueprint), 'azure-function' ) }}:
  - script: echo deal with qa scan relevant to azure-function application type

- ${{ if eq( lower(parameters.applicationBlueprint), 'nuget-package' ) }}:
  - script: echo deal with qa scan relevant to nuget-package application type

- ${{ if eq( lower(parameters.applicationBlueprint), 'universal-artifact' ) }}:
  - script: echo deal with qa scan relevant to universal-artifact application type

- ${{ if and(ne(lower(parameters.applicationBlueprint),'universal-artifact'), ne(lower(parameters.applicationBlueprint),'nuget-package'), ne(lower(parameters.applicationBlueprint),'azure-function')) }}:
  - script: echo UNKNOWN application type
```

---

# Drill-down

TBD

```
TBD
```

That is it for today!

---

# Questions

### For my team

- Q1: Should we consider removing the conditional logic examples and instead adding them only when needed for specific app-type blueprints? This could help reduce noise and improve clarity.

### For you

- Q2: TBD

---

Any questions or suggested improvements?

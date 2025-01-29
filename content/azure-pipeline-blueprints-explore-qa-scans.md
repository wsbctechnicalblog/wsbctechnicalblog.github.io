Title: Azure DevOps Pipeline Blueprints - Exploring the QA Scan templates
Date: 2025-01-29
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

Today we peek into the [templates/qa/azure-pipeline-qa-scans.yml](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/templates/qa/azure-pipeline-qa-scans.yml) template which is triggered by the continuous delivery (cd) template and has one purpose, to trigger the [templates/qa/qa-scans-cd.yml](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/templates/qa/qa-scans-cd.yml) and in fiture, other QA templates.

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

### azure-pipeline-qa-scans.yml nuggets

This template is triggered by our *cd-yml template, ensures the necessary dependencies are in place, and then hands off control to the qa-scans.yml template.

> **Gem 1**

```
  dependsOn:
  - ${{ each stage in parameters.dependsOn }}:
    - ${{stage}}
```

The YAML snippet defines dependencies for a stage in a pipeline dynamically. It allows for flexible, parameter-driven pipeline configuration, enabling reuse of templates for multiple scenarios without hardcoding dependencies.

**dependsOn** keyword

- Specifies which stages in the pipeline must be completed successfully before this stage can run, ensuring the pipeline respects the execution order and dependency hierarchy.

**Dynamic Dependencies**

- ```${{ each stage in parameters.dependsOn }}``` iterates over the values in the parameters.dependsOn array.
- ```${{ stage }}``` resolves each value in the array to dynamically populate the dependsOn list.

**Example**

If the parameters.dependsOn contains ['Build', 'Test'], the snippet will resolve to:

```
dependsOn:
  - Build
  - Test
```

This means the current stage will only execute after both the Build and Test stages are completed. 

> **Gem 2**

```
    # List all environment variables within this agent
    - bash: 'env | sort'
      displayName: Bootstrap Dump env variables
```

This gem runs a Bash script to print, sort, and display all environment variables in pipeline logs. It is useful for debugging or validating environment setup in CI/CD pipelines.

- **bash**: Specifies a Bash script task in the pipeline.
- **env | sort**: Lists and sorts all current environment variables alphabetically.
- **displayName**: Adds a label in the pipeline UI to describe what this step does.

### qa-scans.yml

For this template, we focus on a single conditional statement from the many available options.

```
- ${{ if or(eq(variables['Build.SourceBranch'], 'refs/heads/release'), startsWith(variables['Build.SourceBranch'], 'refs/heads/release/')) }}:
```

This gem is a conditional expression that checks whether the current build branch matches specific conditions - whether we are dealing with a **release** branch. In the template we have a section where users can run app-type specific tasks if we are dealing with a **release** branch, or any **other** branch, or both.

That is it for today - but an ear on the ground - we have an interesting v2.1 update coming.

---

# Questions

### For my team

- Q1: Should we consider removing the conditional app-type logic examples and instead adding them only when needed for specific app-type blueprints? This could help reduce noise and improve clarity.

### For you

- Q2: How do you abstract your user interface, user experience, and other testing in the continuous delivery pipelien flow (shift right), after the continuous integration pipeline flow (shift left)is complete? 

---

Any questions or suggested improvements?

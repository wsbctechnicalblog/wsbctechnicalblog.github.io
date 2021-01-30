Title: Part 5: Pipelines - Blueprints to fuel consistency and enablement
Date: 2021-01-28
Category: Posts
Tags: Azure-Pipelines, DevOps
Slug: yaml-pipelines-part5
Author: Willy-Peter Schaub
Summary: @.

Welcome back to another installment of our exciting pipeline journey, as outlined in [part 1](/why-pipelines-part1.html). After covering some of the gems and magic in [part 5](/yaml-pipelines-part5.html) we will take a peek at our pipeline blueprints.

---

# What do we mean with pipeline blueprints?

If you ask 13 software engineers to cook a continuous delivery pipeline, you are likely to get more than 13 variations. Although this enables innovation, it distracts the engineers from their core responsibility to continuously delivering functional code and value. More concerning the variations of artworks (pipelines) hamper reuse and bloat support and maintenance costs.

Similar to the the building-blueprint counterpart, our **generic** and **application-type** pipeline blueprints define templates that allow rapid and consistent creation of unlimited number of continuous delivery pipeline copies. Let us have a look at a few of our blueprints.

---

# Generic blueprints

We have defined two generic blueprints. One defines a one stage, multiple jobs pipeline, allowing parallel runs on separate agents, each with multiple steps. The more simpler and recommended blueprint defines a one stage, one job, with multiple steps pipeline. It keeps things simple, running everything on one agent. 

Both blueprints call our **bootstrap** template, which in injects other templates introducing DevSecOps scans such as SonarQube and WhiteSource, as well as custom built **building code** scripts and products, based on queue-time parameters.

> Azure-Pipeline-Steps.yml flow
> ![Azure-Pipeline-Steps.yml](/images/moving-hundreds-of-pipeline-snowflakes-part5-1.png)

As shown, the blueprint defines a pipeline that runs within the same **job** context, in a single **stage**. It injects the **bootstrap** template with an **init** parameter, to inject initialisation templates, with tasks such as **SonarQube Prepare**.

> Example: SonarQube Prepare for .NET applications
```yml
# --------------------------------------------------------------------------
# SONARQUBE - dotnet
# --------------------------------------------------------------------------
- ${{ if eq( parameters.applicationType, 'dotnet' ) }}: 
  - task: SonarQubePrepare@4
    displayName: 'SonarQube Prepare'
    inputs:
      SonarQube:      ${{parameters.sonarQubeService}}
      scannerMode:    'MSBuild'
      projectKey:     ${{parameters.sonarQubeProjectKey}}
      projectName:    ${{parameters.sonarQubeProjectName}}
    continueOnError:  true
```

At the end of the continuous integration (CI) part of the pipeline, the blueprints injects the **bootstrap** template with a **run** parameter, to inject tasks such as **SonarQube Analyze**, **SonarQube Publish**, **WhiteSource**, and **Building Code** validations. Single jobs are the most efficient as dependencies, such as source code, extensions, and the bootstrap toolbox only need to be loaded once.

Here is the latest version of this blueprint:

> Azure-Pipeline-Steps.yml source code
```yml
trigger:
  batch: true
  branches:
    include:
    - '*'
  paths:
    exclude:
    - pipeline

# Semantic version as per Azure DevOps Naming Conventions.
name:
  $(portfolioName)_$(productName)_$(GITVERSION_MAJORMINORPATCH)_$(date:yyyyMMdd).$(date:HHmmss).$(Build.SourceBranchName)

# Configure the default agent pool and image to use for your pipeline
pool:
  name:                 'Azure Pipelines'
  vmImage:              'windows-latest'

# Variables
variables:
  BuildConfiguration:   Release
  BuildPlatform:        'Any CPU'
  templateVersion:      1.0.9
  portfolioName:        'TODO REPLACE WITH PORTFOLIO NAME'
  productName:          'TODO REPLACE WITH PRODUCT NAME'
  productGuid:          'TODO REPLACE WITH A NEW GUID WITHOUT BRACKETS'

# Repository resources
resources:
  repositories:
  # =======================================================================
  # SKULL & CROSS-BONES - DO NOT COMMENT OUT, OR REMOVE THIS SECTION
  - repository: CDTemplates
    type: git
    name: 'Common-Engineering-System/AzureDevOps.Automation.Pipeline.Templates'
  # =======================================================================

# --------------------------------------------------------------------------
# START OF BUILD and TEST STAGE
# - GitVersion task looks at your Git history and works out the semantic 
#   version of the commit being built.
# --------------------------------------------------------------------------
stages:
- stage: ContinuousIntegration
  displayName: Continuous Integration
  jobs:
  - job: ContinuousIntegration
    steps:
    - task: gitversion/setup@0
      displayName: Install GitVersion
      inputs:
        versionSpec: '5.x'

    - task: gitversion/execute@0
      displayName: Use GitVersion
        
# --------------------------------------------------------------------------
# PREREQUISITES
# - Run steps that have to run before the build here, for example NPM, NuGet
# --------------------------------------------------------------------------
#   TODO Insert your scripts, steps, and tasks here and remove this comment
 
# ==========================================================================
# BOOTSTRAP VALIDATION, STAGE: CI_BOOTSTRAP_INIT
# SKULL & CROSS-BONES - DO NOT COMMENT OUT, OR REMOVE THIS SECTION
# ==========================================================================
    - template: Templates/Bootstrap.yml@CDTemplates
      parameters:
        bootstrapMode:    'init'
        applicationType:  'TODO REPLACE WITH SUPPORTED TYPE' # dotnet, angular
        applicationGuid:  $(productGuid)
        portfolioName:    $(portfolioName)
        productName:      $(productName)
        sourcesDirectory: $(Build.SourcesDirectory)
# ==========================================================================

# --------------------------------------------------------------------------
# CONTINUOUS INTEGRATION BUILD
# - Run steps/tasks to build your solution here. 
# - Move initialisations (NPM, NuGet,...) to PREREQUISITES section
# --------------------------------------------------------------------------
#  TODO Insert your scripts, steps, and tasks here and remove these comments

# --------------------------------------------------------------------------
# CONTINUOUS INTEGRATION TEST
# - Run steps/tasks to test your solution here
# --------------------------------------------------------------------------
#   TODO Insert your scripts, steps, and tasks here and remove this comment

# --------------------------------------------------------------------------
# PUBLISH
# - Publish the build and test artifacts
# --------------------------------------------------------------------------
#   TODO Insert build and test artifact publication tasks
  
# ==========================================================================
# BOOTSTRAP VALIDATION, STAGE: CI_BOOTSTRAP
# SKULL & CROSS-BONES - DO NOT COMMENT OUT, OR REMOVE THIS SECTION
# ==========================================================================
    - template: Templates/Bootstrap.yml@CDTemplates
      parameters:
        bootstrapMode:    'run'
        applicationType:  'TODO REPLACE WITH SUPPORTED TYPE' # dotnet, angular
        applicationGuid:  $(productGuid)
        portfolioName:    $(portfolioName)
        productName:      $(productName)
        sourcesDirectory: $(Build.SourcesDirectory)
# ==========================================================================
```

Engineers can **copy-paste** this blueprint into their application repository, look for **TODO**s, update and fine-tune the pipeline as needed. Sections which should not be deleted or changed are enclosed in skull & cross-bones markers. **Simple!**

The other **generic** template, Azure-Pipeline-Jobs.yml, enables engineers to craft multi-job pipelines, enabling features such as parallelism. 

> Azure-Pipeline-Jobs.yml flow
> ![Azure-Pipeline-Jobs.yml](/images/moving-hundreds-of-pipeline-snowflakes-part5-2.png)

As shown, the blueprint defines two jobs, one including the **initialisation** and **build** sections, and the other the **test** section. Some tasks, such as the **SonarQube** tasks have to run within the same job context, which is why the blueprint injects the bootstrap template three times. As before, the first injects the **bootstrap** template with an **init** parameter, to inject initialisation templates, with tasks such as **SonarQube Prepare**. The second injects the **bootstrap** template with a **devsecopsonly** parameter, which magically injects all of the DevSecOps scans, such as **SonarQube Analyse**, **SonarQube Publish**, and **WhiteSource**. The remaining templates, such as the **Building Code** are only injected at the end when the third call is made to the **bootstrap** template with the **buildingcodeonly** parameter.

To summarise, we are trying to simplify our pipeline environment and empower both development and operations with these blueprints. 

**But**, we can do better!

---

# App-type Blueprints 

TBD

---

# Enabling continuous innovation and rapid change 

TBD

---

# Enabling automation 

TBD

---

# What is next?

We have covered the continuous integration (CI), also referred to as build, pipelines though the lens of YAML. Next, we will explore continuous deployment CD). See you in part 6.


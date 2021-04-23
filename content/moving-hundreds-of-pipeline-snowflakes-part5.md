Title: Part 5: Pipelines - Blueprints to fuel consistency and enablement
Date: 2021-01-28
Category: Posts
Tags: Azure Pipelines, DevOps, Pipeline as Code
Slug: yaml-pipelines-part5
Author: Willy-Peter Schaub
Summary: Think of **blueprints** and associated **templates** as re-usable LEGO blocks, ranging from a bag of "do it yourself" blocks, to complex and detailed kits, such as the Imperial Star Destroyer.

Welcome back to another installment of our exciting pipeline journey, as outlined in [part 1](/why-pipelines-part1.html). After covering some of the gems and magic in [part 4](/yaml-pipelines-part4.html) we will peek at our pipeline blueprints.

---

# What do we mean with pipeline blueprints?

If you ask 13 software engineers to cook a continuous delivery pipeline, you are likely to get more than 13 variations. Although this enables innovation, it distracts the engineers from their core responsibility to continuously delivering functional code and value. More concerning the variations of artworks (pipelines) hamper reuse and bloat support and maintenance costs.

Like the building-blueprint counterpart, our **generic** and **application-type** pipeline blueprints define templates that allow rapid and consistent creation of unlimited number of continuous delivery pipeline copies. Let us have a look at a few of our blueprints.

---

# Generic blueprints

We have defined two generic blueprints. One defines a one stage, multiple jobs pipeline, allowing parallel runs on separate agents, each with multiple steps. The simpler and more recommended blueprint defines a one stage, one job, with multiple steps pipeline. It keeps things simple, running everything on one agent. 

Both blueprints call our **bootstrap** template, which injects other templates introducing DevSecOps scans such as SonarQube and WhiteSource, as well as custom built **building code** scripts and products, based on queue-time parameters.

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

With application-type, in short app-type, blueprints we are taking the continuous integration (CI) pipelines light-years further in terms of our goals for **simplicity**, **security**, **enablement**, and **consistency**. Each app-type blueprint, based on our pipeline champion Said Akram's (@said-akram-wcbbc) ingenious proof-of-concept, consists of a **starter** template, an **app-type** template, and a reference **sample** implementation, as shown below.

> App-type blueprint parts
>
> ![Azure-Pipeline-Jobs.yml](/images/moving-hundreds-of-pipeline-snowflakes-part5-7.png)

The **starter** template allows our engineers to configure their continuous integration pipeline, after they **copy-paste** it into their application repository. This is the only moving part that is copied and becomes part of the application code base.

> SAMPLE - Azure Function **starter** template
```yml
trigger:
  batch: true # batch changes if true; start a new build for every push if false
  branches:
    include:
    - '*' # Trigger on all branches

resources:
  repositories:
  - repository: CDAppTemplates
    type:       git
    name:       'Common-Engineering-System/AzureDevOps.Automation.Pipeline.AppTemplates'

# Semantic version as per Common Engineering Naming Conventions.
name:
  $(portfolioName)_$(productName)_$(GITVERSION_MAJORMINORPATCH)_$(date:yyyyMMdd).$(date:HHmmss).$(Build.SourceBranchName)

# VARIABLES
variables:
  portfolioName:    'TODO REPLACE WITH PORTFOLIO NAME' # e.g. StarWars
  productName:      'TODO REPLACE WITH PRODUCT NAME' # e.g. Imperial.Star-Destroyer

extends:
  template: Templates/AzureFunction/azureFunctionTemplate.yml@CDAppTemplates
  parameters:
    updateAssemblyInfo:     false # Optional. Options: true | false. Whether to update versions in the AssemblyInfo files
    netCoreVersion:         'TODO REPLACE WITH .NET CORE VERSION' # e.g. 3.1.x
    applicationGuid:        'TODO REPLACE WITH A NEW GUID WITHOUT BRACKETS' # e.g. 257929e89c69471083efb51899b42bdb
    portfolioName:          $(portfolioName)
    productName:            $(productName)
    restoreBuildProjects:   '**/*.csproj'
    vstsFeed:               '11111111-2222-3333-4444-555555555555' # _NuGet feed
    buildConfiguration:     'Release'
```

The **starter** template **extends** the pipeline with the **app-type** template, in our example the azureFunctionTemplate.yml. With this **magic** we introduce the template [**extend**](https://docs.microsoft.com/en-us/azure/devops/pipelines/security/templates?view=azure-devops#use-extends-templates) feature, which sprinkles a dash of **security** on our pipelines, as we can now check that a pipeline is extended from a trusted template in [environment](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/environments?view=azure-devops) and [service connection](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops&tabs=yaml) approvals and checks. 

> Required template checks
>
> ![Azure-Pipeline-Jobs.yml](/images/moving-hundreds-of-pipeline-snowflakes-part5-4.png)

The **app-type** template is visible, but not modifiable for the owner of the pipeline. We abstract the entire continuous integration (CI) process from the engineers, which promotes **consistency**, delegates **responsibility** for the implementation to our common engineering system team, and **encourages** engineers to be razor-focused on their application. The complexity of injecting our **bootstrap** and associated templates, task sequence, stage and job context, and pipeline plumbing we discussed in previous parts, is abstracted (hidden). 

Let us briefly review this with a visual.

> Azure-Pipeline-Steps.yml Custom Template
>
> ![Azure-Pipeline-Jobs.yml](/images/moving-hundreds-of-pipeline-snowflakes-part5-5.png)

With the **custom** blueprints the starter template presents a much larger exposure area, where we can observe template drift, vulnerability injections, and complexity that the engineering teams should not have to worry about. As discussed, the latest **bootstrap** and associated templates are pulled from the ```*.Templates``` repository and injected into the pipeline instance at queue time.

Time to reiterate ... we can do better!

> AzureFunctionTemplate.yml Starter Template
>
> ![Azure-Pipeline-Jobs.yml](/images/moving-hundreds-of-pipeline-snowflakes-part5-6.png)

With the **app-type** blueprints, the starter template has a much smaller exposure area. The latest **app-type** template is pulled from the ```*.AppTemplates``` repository, which in turn injects the latest **bootstrap** and associated templates from the ```*.Templates``` repository.

You should appreciate the magic of the YAML pipelines by now!

---

# Enabling continuous innovation and rapid change 

We always start our YAML awareness and training workshops with the following scenario and question: "*Assume we have 1000 classic pipelines and 1000 YAML pipelines, and we need to make a change to one of the pipeline tasks that takes approximately 1 minute. How long will it take us to change all of the classic pipelines and all of the YAM pipelines?*"

We then give everyone 5 minutes to discuss and place their bets. Discussions vary, but usually include reference to mind-numbing classic pipeline editor, [Task groups](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/task-groups?view=azure-devops), code search and replace, followed by vibrant debates and eventually stunned silence ... the proverbial "room full of crickets."

It is a trick question, because it depends on how the pipelines are designed, which can vary from minutes to days of effort. 

What should be evident, however, is that any change will be **faster**, **simpler**, and **safer** to make if the **consistency** of our pipelines is high, and the **exposure area** is small. 

We recently received a request from DevSecOps to change all our pipelines to always run the DevSecOps scans, instead of just as part of pull request validation builds. It literally took us minute to create a feature branch, tweak the bootstrap template, and validate the change with a collaborative pull request. Once merged into the *.Templates repository, all new pipeline instances showcased the new default behaviour. DevSecOps were happy and the engineering teams unaware of any change.

---

# Enabling automation 

Lastly, we realised that our self-service automation goal is also no longer a distant dream. The app-type templates enable us to ask the engineering teams a few questions, then run automation that creates a new application repository and pipeline in seconds - and consistently! That, however, is a story for another day in Part 7: Self-service automation - A dream turns into reality q;)

---

# What is next?

We have now covered the continuous integration (CI), also referred to as build, pipeline though the lens of YAML. You can think of the **blueprints** and associated **templates** as re-usable LEGO blocks, ranging from a bag of "do it yourself" blocks, to complex and detailed kits, such as the Imperial Star Destroyer.

> LEGO Imperial Star Destroyer kit
>
> ![LEGO Image](/images/moving-hundreds-of-pipeline-snowflakes-part5-3.png) 

Next, we will explore continuous deployment (CD). See you in part 6 (coming soon).

---

> Series Bread Crumbs | [Part 1, TOC](/why-pipelines-part1.html) | [Part 2](/yaml-pipelines-part2.html) | [Part 3](/yaml-pipelines-part3.html) | [Part 4](/yaml-pipelines-part4.html) | [Part 5](/yaml-pipelines-part5.html) | [Part 6](/yaml-pipelines-part6.html) | [Part 7](/yaml-pipelines-part7.html) |  [Part 8](/yaml-pipelines-part8.html) |


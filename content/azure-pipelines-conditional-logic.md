Title: Azure Pipelines Conditional Logic
Date: 2022-12-28
Category: Posts 
Tags: azure-devops, pipelines, oss, tips
Slug: azure-pipelines-conditional-logic
Author: Willy-Peter Schaub
Summary: Make your YAML pipelines more versatile with conditional expressions.

Let us review why and how we use conditional expressions in our [v2 application-type pipeline blueprints](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2).

---

# What is a conditional expression and why is it "cool"?

You can use the ```if```, ```elseif```, and ```else``` clauses to conditionally assign values or, as discussed in this blog post, conditionally run a step when a condition is met. 

![Intersection](../images/azure-pipelines-conditional-logic-1.png)

Conditions are defined using [Expressions](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/expressions?view=azure-devops) and built-in [Functions](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/expressions?view=azure-devops#functions). We have made heavy use of conditional expressions to define what our blueprints assemble at queue (run) time, which is not only a powerful concept, but also allows us to tick off a couple of **classic** Azure Pipeline security risks. 

```
# VARIABLES
variables:
- ${{ if ne(parameters.suppressCD, true) }}:
  - template: /deploy/${{ lower(parameters.portfolioName) }}/${{ lower(parameters.productName) }}-config.yml@CeConfiguration
```

In the example above, we include a [variable template]() if, and only if, the ```suppressCD``` parameter is not set to ```true```. Note that we are intentionally turning every character in the variable template e to lowercase using the ```lower``` [function](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/expressions?view=azure-devops#lower).

---

# Examples in our blueprints

## Conditional Quality Assurance and Security Scans

As described in our recent [Azure Pipelines Blueprint QA Integration](/azure-pipelines-blueprint-qa-integration.html) post, our pipelines are designed to target a **lower** and **higher** environment, whereby the higher is locked down and only included when the artifact originates from a ```release``` branch.

![Typical CI/CD pipeline](../images/azure-pipelines-blueprint-qa-integration-1.png)

Let us peel the example below, layer by layer, which is the template we are using for both the [Security Automation](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/templates/dev-sec-ops/security-scans-auto.yml) and [Quality Assurance (QA)](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/templates/qa/qa-scans-cd.yml) stages.

- The conditional expression example ```${{ if or(eq(variables['Build.SourceBranch'], 'refs/heads/release'), startsWith(variables['Build.SourceBranch'], 'refs/heads/release/')) }}:``` decides if part of the template is included, by checking if the source branch is named ```release``` or ```release/*```, where ```*``` is a semantic version using the MAJOR.MINOR format. For example: ```release/1.3```.
- The template is divided into three sections of ```steps```, the steps to run for **LOWER** environment artifacts, the steps for the **HIGHER** environment artifacts, and the steps to run for both the **LOWER+HIGHER** environments. All implemented using ```conditional expressions```.
- In the lower, higher, and both lower+higher placeholders, the conditional expression example ```${{ if eq( lower(parameters.applicationBlueprint), 'azure-function' ) }}:``` allows us to define application-specific steps to be run.

```
parameters:
- name:     applicationBlueprint
  type:     string
- name:     modeElite
  type:     boolean
  default:  false
  
steps:
# ------------------------------------------------------
# QA AUTOMATION FOR LOWER (NON-PROD) ENVIRONMENTS STAGE
# ------------------------------------------------------
- ${{ if not(or(eq(variables['Build.SourceBranch'], 'refs/heads/release'), startsWith(variables['Build.SourceBranch'], 'refs/heads/release/'))) }}:
  - script: echo 'QA CD Lower Environment Automation Placeholder ***'
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

# ------------------------------------------------------
# QA AUTOMATION FOR HIGHER (PROD) ENVIRONMENTS STAGE
# ------------------------------------------------------
- ${{ if or(eq(variables['Build.SourceBranch'], 'refs/heads/release'), startsWith(variables['Build.SourceBranch'], 'refs/heads/release/')) }}:
  - script: echo 'QA CD Higher Environment Automation Placeholder ***'
  - script: echo applicationBlueprint = ${{parameters.applicationBlueprint}}
  - script: echo modeElite = ${{parameters.modeElite}}
  ... rinse and repeat ...

# ------------------------------------------------------
# QA AUTOMATION FOR LOWER AND HIGHER (PROD) ENVIRONMENTS STAGE
# ------------------------------------------------------
- script: echo 'QA CD Lower and Higher Environment Automation Placeholder ***'
```

Simple, but powerful!

## Boot-Strap Flow

![boot-strap.yml](../images/azure-pipelines-conditional-logic-3.png)

Our [boot-strap](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/templates/boot-strap.yml) template is our secret sauce that injects **DevSecOps**, **Building Code**, **Toolkits**, and **Application Insights** steps into our continuous integration (CI) pipeline.

In the 80's I would have written the boot-strap logic as a gigantic [Assembler](https://en.wikipedia.org/wiki/Assembly_language) or [V2/PLM](https://en.wikipedia.org/wiki/PL/M) switch statement. Back to the future, we have conditional YAML expression that make the experience a lot more readable and user friendly q;-)

Here is a short extract from our ```bootstrap``` template where we checkout our toolbox and call our Application Insights logging steps if the ```bootstrapMode``` is set to ```init```.

```
... snipped code ...

======================================================
# BOOTSTRAP TOOLBOX
======================================================
# Production Toolbox
- ${{ if or( eq( lower(parameters.bootstrapMode), 'init' ), eq( lower(parameters.bootstrapMode), 'runbuildingcodeonly' )) }}:
  - checkout: git://Common-Engineering-System/AzureDevOps.Automation.Pipeline.Toolbox.v2

======================================================
# BOOTSTRAP AI LOGGING
======================================================
- ${{ if eq( lower(parameters.bootstrapMode), 'init' ) }}:
  - task: PowerShell@2
    displayName: 'Bootstrap Telemetry START'
    inputs:
      filePath: '$(Build.SourcesDirectory)/AzureDevOps.Automation.Pipeline.Toolbox.v2/toolbox/scripts/application-insights/log-bootstrap-event-to-ai.ps1'
      arguments: -OperationId "$(Build.BuildNumber).$(Build.BuildId)" `
                 -Event  'Bootstrap' `
                 -Action 'Start' `
                 -BootstrapMode ${{parameters.bootstrapMode}} ` 
                 -ApplicationType ${{parameters.applicationType}} `
                 -ApplicationBlueprint ${{parameters.applicationBlueprint}} `
                 -PortfolioName ${{parameters.portfolioName}} `
                 -ProductName ${{parameters.productName}} `
                 -SourcesDirectory ${{parameters.sourcesDirectory}} `
                 -VerboseFlag ${{parameters.verbose}} `
                 -ForceCheck ${{parameters.forceCheck}}
      failOnStderr: true
      pwsh: true
    continueOnError: true

... snipped code ...
```

## Conditional Templates

The last example is an extract from the [azure-pipeline-nuget-package-ci.yml](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/blueprints/nuget-package/azure-pipeline-nuget-package-ci.yml) where we conditionally load a ```portfolioName/productName``` specific or a ```default``` variable template based on the value of the ```useDefaultConfig``` parameter.

```
# VARIABLES
variables:
- ${{ if and( ne(parameters.suppressCD, true), ne(parameters.useDefaultConfig, true) ) }}:
  - template: /deploy/${{ lower(parameters.portfolioName) }}/${{ lower(parameters.productName) }}-config.yml@CeConfiguration
- ${{ if and( ne(parameters.suppressCD, true), eq(parameters.useDefaultConfig, true) ) }}:
  - template: /deploy/default.config/nuget-package-config.yml@CeConfiguration
```

---

# Lastly, a spacing GOTCHA!

Finally, let us look at a common gotcha. YAML is **very** space sensitive and the indents are important. For example, only the first two ```script``` steps are part of the conditional expression context. The third ```script```, which is not indented will be run irrespective of the conditional expression result.

We strongly recommend you use [Visual Studio Code](https://code.visualstudio.com/) to give visual cues of your code and grouping thereof and the Azure Pipeline YAML [Validate](https://johnlokerse.dev/2022/02/07/validating-yaml-using-azure-devops-or-cli/) feature to validate that your syntax is correct. 

```
- ${{ if not(or(eq(variables['Build.SourceBranch'], 'refs/heads/release'), startsWith(variables['Build.SourceBranch'], 'refs/heads/release/'))) }}:
  - script: echo 'Security CD Lower Environment Automation Placeholder ***'
  - script: echo applicationBlueprint = ${{parameters.applicationBlueprint}}
- script: echo modeElite = ${{parameters.modeElite}}
```
That is, it for today folks! Ping me on [@wpschaub](https://twitter.com/wpschaub) if you have any questions or feedback. 


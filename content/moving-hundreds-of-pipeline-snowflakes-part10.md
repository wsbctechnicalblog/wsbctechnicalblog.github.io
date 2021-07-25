Title: Pipelines - Meet our second-generation app-type blueprints
Date: 2021-07-24
Category: Posts
Tags: automation, azure-devops, pipelines, x-as-code
Slug: yaml-pipelines-part10
Author: Willy-Peter Schaub
Summary: Our quest for continuous improvement, simplicity, consistency, enablement, and automation has taking us into a realm of Azure Pipelines that amaze even our most critical engineers. 

---

In [Self-service automation - A dream turns into reality](/yaml-pipelines-part9.html) we explored the nifty automation script we used to demonstrate our application-type blueprints to our engineering teams. The feedback was positive, as shown by the session score and the net performance score (NPS) for our common engineering system and sets high expectations for future innovation.

![Stars](/images/moving-hundreds-of-pipeline-snowflakes-part10-1.png) ![NPS](/images/moving-hundreds-of-pipeline-snowflakes-part10-2.png)

Let us review the latest blueprints, we refer to as our second-generation app-type blueprints, and a checklist we use to build new ones.

---

# 2nd Generation app-type blueprint

The diagram looks intimidating at first, but the power and simplicity will become evident as we unpack the pieces. If you have been following our adventure from the days of the generic blueprints, you will appreciate the improvement and simplicity - 18 lines of YAML and less than a handful of tokens to update that engineers must worry about.

Although [Self-service automation - A dream turns into reality](/yaml-pipelines-part9.html) sets up **everything** for our engineers, it helps to know about all the ingredients and how they are mixed to create magic.


> app-type blueprint architecture
>
> ![blueprints](/images/moving-hundreds-of-pipeline-snowflakes-part10-3.png)


( 1 ) azure-pipeline-< app-type >-**start**.yml template, where * is a placeholder for azure-pipeline. 


> azure-pipeline-azure-function-**start**.yml template example

```
# --------------------------------------------------------------------------
# WorkSafeBC Multi-Stage Blueprint-Based Pipeline Design Practice
# --------------------------------------------------------------------------
# See https://aka.ms/yaml for Azure DevOps Pipeline documentation
#
# Azure Function blueprint v2
# --------------------------------------------------------------------------
# HOW TO USE
#   - Copy the content of this file to 
#     'pipelines/azure-pipelines-<portfolio>-<program>-start.yml' under the 
#     root folder of your repo
#   - Look for TODO and update / fine-tune as needed
# --------------------------------------------------------------------------

trigger:
  batch: true # batch changes if true; start a new build for every push if false
  branches:
    include:
    - '*' # Trigger on all branches

resources:
  repositories:
  - repository: CeSTemplates
    type:       git
    name:       'Common-Engineering-System/AzureDevOps.Automation.Pipeline.Templates'

extends:
  template: /Blueprints/azure-function/azure-pipeline-azure-function-control.yml@CeSTemplates
  parameters:
    netCoreVersion:     '3.1.x' # e.g. 2.x, 3.1.x
    portfolioName:      '__TODO_PORTFOLIO__'
    productName:        '__TODO_PRODUCT__'
    azFuncProjectName:  '__TODO_AZURE_FUNCTION_PROJECT_NAME__' # e.g. CeS.Sample.AzureFunction
    suppressCD:         true # Allow eng. run a CI/build while CD is configured
```

( 2 ) azure-pipeline-< app-type >-**control**.yml template, our new wheelhouse, and **extends** the app-type *-start.yml template above. As implied by the name, the template is the app-type cookbook. It pulls the configuration from the ( 3 ) azure-pipeline-< app-type >-**config**.yml template, injects the continuous integration pipeline, and then the continuous deployment template.

( 4 ) azure-pipeline-< app-type >-**ci**.yml template, defines the continuous integration steps and injects the ( 5 ) **boot-strap**.yml template, which is covered in [Part 3: Pipelines - Basic building blocks as templates and sprinkling on telemetry](/yaml-pipelines-part3.html). It is where the builds and tests are run, followed by automated scans to verify the latest codebase before opening the deployment gates. "Trust but verify" as Kevin would say.


> **COFFEE BREAK**
>
> *Our DevSecOps team recently decided to suspend one of the security scans, SonarQube, to rebuild their server and create a new database from scratch. Our engineers supporting our classic unified Azure Pipelines, as mentioned in [Part 1: Pipelines - Why bother and what are our nightmares and options](/why-pipelines-part1.html), are faces with the mammoth task of updating more than 1000 pipelines. Our pipeline working group only had to update one YAML template, submit, review, and complete a pull-request ... and voila 200+ blueprint-based pipelines no longer ran the SonarQube task. Minutes versus a mind-numbing waste of time.*


( 6 ) azure-pipeline-< app-type >-**cd**.yml template, defines the continuous deployment steps to validate with automated tests and deploy to one or more environments. As shown in the diagram above, the template includes the ( 7 ) **security-scans**.yml template, and the ( 8 ) azure-pipeline-< app-type >-cd-**stage**.yml template. The latter includes the actual recipe for deployment and assumes that all environments are the same. 


> **WHAT IF ENVIRONENTS ARE DIFFERENT?**
>
> *The start and control templates support the concept of injecting custom templates for the continuous integration and deployment steps. In future we will use the same concept to support default and custom QA templates. See code snippet below.* 

```
...
# --------------------------------------------------------------------------
# START OF PIPELINE
# If user overrides the customCITemplate with a custom template
# --------------------------------------------------------------------------
- ${{ if ne(parameters.customCITemplate, 'blueprint') }}:
  - template: /Operations/Custom/CI/${{parameters.customCITemplate}}.yml
    parameters:
      ciParameter: ${{parameters.customCIParameter}}

- ${{ if eq(parameters.customCITemplate, 'blueprint') }}:
  - template: /Blueprints/azure-function/azure-pipeline-azure-function-ci.yml@CeSTemplates
    parameters:
      netCoreVersion:     ${{parameters.netCoreVersion}}
      portfolioName:      ${{parameters.portfolioName}}
      productName:        ${{parameters.productName}}
      azFuncProjectName:  ${{parameters.azFuncProjectName}}
      verbose:            ${{parameters.verbose}}
      forceToolbox:       ${{parameters.forceToolbox}}
      previews:           ${{parameters.previews}}
      loadDVTBox:         ${{parameters.loadDVTBox}}
...
```

( 9 ) Our **standardisation**.yml line, which separates the pipeline instance, and the shared templates. Engineering is accountable for the former and the common engineering system for the latter.

( 10 ) **extends**, the hidden gem that empower our consistency and security guardrails. We use the [set required templates](https://github.com/MicrosoftDocs/azure-devops-docs/blob/master/docs/pipelines/security/templates.md#set-required-templates) feature to verify and enforce that all our production pipelines extend from one of the *-control.yml templates stored in our AzureDevOps.Automation.Pipeline.**Templates** repo.

---

# Building a new blueprint

![blueprints](/images/moving-hundreds-of-pipeline-snowflakes-part10-4.png)

Now that we know the ingredients of our gourmet template stew, let us conclude with a checklist how our engineers create a new blueprint. 

## Cook a new blueprint

Create a new ...

1. Feature branch in our AzureDevOps.Automation.Pipeline.Templates repository and a DRAFT pull request to start **collaborating** with the pipeline working group. It is important to use the latest and greatest ingredients and consider shared templates where possible to avoid **waste**.
2. azure-pipeline-< app-type >-**start**.yml template ( feel free to copy-paste from an existing template).
3. azure-pipeline-< app-type >-**control**.yml template.
4. azure-pipeline-< app-type >-**config**.yml template.
5. azure-pipeline-< app-type >-**ci**.yml template.
6. azure-pipeline-< app-type >-**cd**.yml and an associated azure-pipeline-< app-type >-cd-**stage**.yml template.
7. Publish the pull request to trigger validation build(s), validate policies, and invite operations, security, and working group reviewers.

## Taste the automation

Take a few more steps further to enable automation ...

1. Create a AzureDevOps.Automation.Pipeline.Sample.< app-type > repository with a sample app-type specific sample.
2. If you have custom tokens that need to be updated by the automation script:
    - Create a feature branch in AzureDevOps.Automation.Scripts repository
    - Update the /azure-devops-pipelines/demo-blueprints/drop-the-mic.ps1 script
    - Submit a pull request.
3. Run the automation script, as covered in [Part 9: Self-service automation - A dream turns into reality](/yaml-pipelines-part9.html) to verify that the following magic happens:
    - New repo is created in the specified Azure DevOps.
    - New pipeline is created in the new repo.
    - New config template is added to the Automation.Pipeline.Templates repo in the /Operations/Config folder.
    - The sample from the AzureDevOps.Automation.Pipeline.Sample.< app-type  is copied to the new repository.
    - Run new pipeline to validate the continuous integration part of the new pipeline.


Simple, no?

---

# What is next?

We continue to create new blueprints to cover all our existing application-types, which include good old Cobol, and new application-types emerging from our architecture runway. 

Watch this space for more exciting news.

---

> Series Bread Crumbs | [Part 1, TOC](/why-pipelines-part1.html) | [Part 2](/yaml-pipelines-part2.html) | [Part 3](/yaml-pipelines-part3.html) | [Part 4](/yaml-pipelines-part4.html) | [Part 5](/yaml-pipelines-part5.html) | [Part 6](/yaml-pipelines-part6.html) | [Part 7](/yaml-pipelines-part7.html) | [Part 8](/yaml-pipelines-part8.html) | [Part 9](/yaml-pipelines-part9.html) | Part 10 |


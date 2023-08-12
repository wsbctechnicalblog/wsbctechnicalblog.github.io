Title: <TRY KEEP TITLE SIMILAR TO SLUG WITHOUT - AND SENTENCE CASING>
Date: 2023-08-21
Category: Posts
Tags: azure-devops, pipelines, engineering
Slug: azure-pipeline-yaml-refactor
Author: Willy-Peter Schaub
Summary: Seizing the chance to enhance and optimize our CI/CD/IaC pipelines.

I understand that you may have been delving into our open-source endeavor, which revolves around Azure Pipelines for continuous integration and continuous delivery, employing YAML-based methodologies. If this initiative has not caught your attention yet, I highly recommend acquainting yourself with our  source project, focused on YAML-based continuous integratuion and continuous delivery Azure Pipelines. If not, you better explore our open-source [WorkSafeBC Common Engineering](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2) project as a starting point.

For those who are new to this concept, I have compiled a selection of blog links that you might find valuable for a comprehensive understanding:
- [Part 1: Pipelines - Why bother and what are our nightmares and options?](https://wsbctechnicalblog.github.io/why-pipelines-part1.html)
- [Azure DevOps Pipeline OSS v2.1 Flow](https://wsbctechnicalblog.github.io/azure-devops-pipeline-oss-v2-1-flow.html)
- [Azure Pipelines Blueprint QA Integration](https://wsbctechnicalblog.github.io/azure-pipelines-blueprint-qa-integration.html)

---

# OK, Why are we here?

Indeed, we are currently in the process of integrating infrastructure-as-code (IaC) into our v2 blueprints. This advancement entails the inclusion of a substantial number of parameters within our variable template files. As a consequence, a series of sleepless nights has ensued for our team. To provide a visual depiction, please refer to the illustration below, where the newly added components are represented in pink.

> ![IaC](../images/ azure-pipeline-yaml-refactor.png) 

If we have a quick look at the basic [101 sample variable template](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/blueprints/__101__/azure-pipeline-__101__-config.yml) you will notice that we have a **FLAT** configuration file.

```
variables:

# --------------------------------------------------------------------
# Blueprint: __101__
#
# If you are not going to use all stages, as below, you can suppress them by simply commenting out
# or removing their entire configuration section.
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# DEVelopment Stage
# --------------------------------------------------------------------
- name:  developmentStageName
  value: 'Development' # Do not change stage name value
- name:  developmentStageEnvName
  value: '<TBD>'
- name:  developmentStageVmImage
  value: '<TBD>'
# TODO Add your variables here

# --------------------------------------------------------------------
# System Test Stage
# --------------------------------------------------------------------
- name:  systemTestStageName
  value: 'SystemTest' # Do not change stage name value
- name:  systemTestStageEnvName
  value: '<TBD>'
- name:  systemTestStageVmImage
  value: '<TBD>'
# TODO Add your variables here

# --------------------------------------------------------------------
# Security Review Stage
# --------------------------------------------------------------------
- name:  securityReviewStageEnvName
  value: '<TBD>'

# --------------------------------------------------------------------
# Staging Stage
# --------------------------------------------------------------------
- name:  stagingStageName
  value: 'Staging' # Do not change stage name value
- name:  stagingStageEnvName
  value: '<TBD>'
- name:  stagingStageVmImage
  value: '<TBD>'
# TODO Add your variables here

# --------------------------------------------------------------------
# PRODuction Test Stage
# --------------------------------------------------------------------
- name:  productionStageName
  value: 'Production' # Do not change stage name value
- name:  productionStageEnvName
  value: '<TBD>'
- name:  productionStageVmImage
  value: '<TBD>'
# TODO Add your variables here
```

As a result, each time a new parameter is introduced, it necessitates an update to the [control template](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/blueprints/__101__/azure-pipeline-__101__-control.yml) to incorporate and transmit the extra parameter. This process has proven to be exasperating, labor-intensive, prone to errors, and ultimately, not a sustainable approach. It's far from straightforward and, therefore, presents a significant challenge.

---

# Exploring options

<TBD>

# My pull request and future solution (I hope)

<SOLUTION>

# What is the im[pact on our open-source project?

<IMPACT ON OSS>

---

<CLOSE - SUMMARY >


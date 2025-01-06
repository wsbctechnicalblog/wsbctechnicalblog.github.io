Title: Azure DevOps Pipeline Blueprints - Exploring the start template
Date: 2025-01-15
Category: Posts
Tags: azure-devops, pipelines, engineering
Slug: azure-pipeline-blueprints-explore-start
Author: Willy-Peter Schaub
Summary: Drilling Deeper: A Closer Look at the Blueprint Start Template.

I have decided to dive into our Azure Pipeline blueprints, explore the nitty gritty, and highlight a few nuggets for discussion. Today, we will start with the Start Template, focusing on the [blueprints/__101__/azure-pipeline-__101__-start.yml](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/master/blueprints/__101__/azure-pipeline-__101__-start.yml) file in our open-source [AzureDevOps.Automation.Pipeline.Templates.v2](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2) repo. I will also pose a few questions for my team to consider as we review and refine our approach.

---

# Today's topic - *-start.yml

@@

```
# --------------------------------------------------------------------------
# WorkSafeBC Multi-Stage Blueprint-Based Pipeline Design Practice
# --------------------------------------------------------------------------
# See https://aka.ms/yaml for Azure DevOps Pipeline documentation
#
# __101__ Blueprint
# --------------------------------------------------------------------------
# HOW TO USE
#   - Name file azure-pipeline-__TODO_PORTFOLIO__-__TODO_PRODUCT__-__101__-start.yml
#   - Copy file to 'pipelines/' under the root folder of your repo
#   - Look for TODO and update / fine-tune as needed
#   - In AzureDevOps.Automation.Pipeline.Configuration.v2 repo, configure
#     your associated /deploy/__TODO_PORTFOLIO__-__TODO_PRODUCT__-config.yml
#     configuration file.
# --------------------------------------------------------------------------

trigger:
  batch: true
  branches:
    include:
    - refs/heads/release/*
  paths:
    include:
    # TODO: Replace __token__ and remove this comment
    - /__TODO_FOLDERNAME__ 
    exclude:
    - ReadMe.md     # Excluding changes to the Readme.me file (case dependent?)
    - README.md
    - readme.md
    
resources:
  repositories:
  - repository: CeBlueprints
    type:       git
    name:       '__TODO_INSERT_AZURE_DEVOPS_NAME_HERE__/AzureDevOps.Automation.Pipeline.Templates.v2'

extends:
  template: blueprints/__101__/azure-pipeline-__101__-control.yml@CeBlueprints
  parameters:
    portfolioName:   '__TODO_PORTFOLIO__'
    productName:     '__TODO_PRODUCT__'
    publishFolder:   '__TODO_FOLDERNAME__'
    suppressCD:      true # Allow engineering to do an immediate CI/build while CD is being configured
```

---

# Drill-down

@@resources

@@extends

---

# Questions

- Q1: Should the branches not include ```refs/heads/release/*``` as well?

---

Any questions or suggested improvements?

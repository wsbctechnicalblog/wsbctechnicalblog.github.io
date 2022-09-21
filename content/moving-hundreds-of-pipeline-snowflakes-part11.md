Title: Our road to OSS Blueprints - Suppress CD when pipeline runs within Pull Request
Date: 2022-09-21
Category: Posts
Tags: automation, azure-devops, pipelines, x-as-code
Slug: yaml-pipelines-part11
Author: Willy-Peter Schaub
Summary: A glimpse at our OSS progress and how we use the same pipeline in and out of pull requests. 

---

# Open Sourcing our Application-type CI/CD Blueprints

We are on the home stretch to open source our v2 application-type CI/CD blueprints. In fact, we only have one last optimization story enabler to complete, before we will start setting up an OSS repository in GitHub. Thank you for your patience **Said** - we are close!

---

# Using the same Application-type CI/CD Blueprints as Pull Request (PR) Validation Build 

## suppressCD parameter

Why do we want to suppress the continuous delivery (CD) part of our CI/CD blueprint-based pipelines?

Pipeline is triggered:

- By self-service automation, when the configuration is not yet configured.
- By development team that is not ready to deploy yet.
- As a validation **build** within a pull request, where you only want the continuous integration (CI) to run.

In our ```*start.yml``` template we have the optional **suppressCD** parameter:

```
extends:
  template: blueprints/__101__/azure-pipeline-__101__-control.yml@CeBlueprints
  parameters:
    portfolioName:   '__TODO_PORTFOLIO__'
    productName:     '__TODO_PRODUCT__'
    publishFolder:   '__TODO_FOLDERNAME__'
    suppressCD:      true # Allow engineering to do an immediate CI/build while CD is being configured
    modeElite:       false
```

When set to **true**, this part of the *control.yml is **not** processed. 

```
- ${{ if and(ne(parameters.suppressCD, true), ne(lower(variables['Build.SourceBranchName']), 'merge')) }}:
  - template: /blueprints/__101__/azure-pipeline-__101__-cd.yml@CeBlueprints
```

As a result the CD part of the pipeline will not be injected at queue time.

## Suppress CD within PR

The optional parameter works well, until you are ready to deploy your solution and you set ```suppressCD = false```. In this case the validation build in a pull request would trigger both the continuous integration (CI) and continuous delivery (CD) pipeline phases. 

This explains this code snippet at the end of the ```*-CI.yml``` template, which suppresses the CD part if the pipeline was triggered by a pull request ("merge"):

```
- ${{ if eq(lower(variables['Build.SourceBranchName']), 'merge') }}:
  - script: echo CD part of the pipeline is suppressed for pull request validation builds! 
    displayName: PR Validation CD Suppression Alert
```

![magic](/images/yaml-pipelines-part11.png)

It goes hand-in-hand with the second half of the conditional statement after the suppressCD check, as above. The source branch name will be **merge** if the build originated as a pull request merge validation build.

A simple, but powerful trick!

---

> Series Bread Crumbs | [Part 1, TOC](/why-pipelines-part1.html) | [Part 2](/yaml-pipelines-part2.html) | [Part 3](/yaml-pipelines-part3.html) | [Part 4](/yaml-pipelines-part4.html) | [Part 5](/yaml-pipelines-part5.html) | [Part 6](/yaml-pipelines-part6.html) | [Part 7](/yaml-pipelines-part7.html) | [Part 8](/yaml-pipelines-part8.html) | [Part 9](/yaml-pipelines-part9.html) | [Part 10](/yaml-pipelines-part10.html) | Part 11 |


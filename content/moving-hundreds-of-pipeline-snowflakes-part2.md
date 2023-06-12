Title: Part 2: Pipelines - Introduction, variables and why spaces matter
Date: 2020-12-21
Category: Posts
Tags: azure-devops, devops, pipelines, x-as-code 
Slug: yaml-pipelines-part2
Author: Willy-Peter Schaub
Summary: The new Azure DevOps YAML pipelines have been the focus of innovation, enabling engineering to treat pipelines as code.

We continue our continuous delivery pipeline journey by switching gears from the unified pipelines to the new YAML-syntax pipelines. 

---

# Why the YAML course change?

Do not get me wrong, the Unified pipelines introduced in [Part 1: Pipelines - Why bother and what are our nightmares and options](/why-pipelines-part1.html) are phenomenal and will continue to serve us for quite some time. However, we realised that the unified pipelines are based on the json-based user interface pipelines. Microsoft refers to these pipelines as **classic interface** and there have been no improvements for many sprints in the Azure DevOps [timeline](https://docs.microsoft.com/en-us/azure/devops/release-notes/features-timeline). This is a **RISK** as the technology is becoming stale.

![Classic Pipeline](/images/moving-hundreds-of-pipeline-snowflakes-part2-1.png)

In turn, the new Azure DevOps YAML-syntax pipelines have been the focus of innovation, enabling engineering to treat pipelines as code, use templates to promote consistency, efficiency, innovation, and quality, and last, but not least, combine continuous integration and deployment into one pipeline.

![YAML Pipeline](/images/moving-hundreds-of-pipeline-snowflakes-part2-2.png)

---

# YAML Overview

YAML is a mature human-readable data-serialization language, originally proposed by Clark Evans in 2001. It is often referred to as “yet another markup language” and “YAML ain’t markup language.

When we look at the [Azure DevOps YAML](https://aka.ms/yaml) pipelines, the pipeline configuration language has been kept structurally YAML. That is exciting!

> BOOKMARK the gem [https://aka.ms/yaml](https://aka.ms/yaml) URL!

---

# YAML Basics

Let us ask Azure Pipelines for a new YAML-syntax pipeline to explore. By default, Azure DevOps generates the following starter pipeline for us:

## Our first pipeline

```yml
# Starter pipeline
# Start with a minimal pipeline that you can customize to build and deploy your code.
# Add steps that build, run tests, deploy, and more:
# https://aka.ms/yaml

trigger:
- main

pool:
  vmImage: 'ubuntu-latest'

steps:
- script: echo Hello, world!
  displayName: 'Run a one-line script'

- script: |
    echo Add other tasks to build, test, and deploy your project.
    echo See https://aka.ms/yaml
  displayName: 'Run a multi-line script'
```

It is evident that:
- It is triggered on changes on the **main** branch.
- It is queued on the latest **ubuntu** agent pool - other options include macOS and Windows.
- It runs two steps, hosted in one stage, containing one job.

Simple!

## Variables

Next, we will explore two key YAML topics: **Variables** and **Parameters**.

- Every variable is really a key:value pair.
  - Simple variable syntax example
    ```yml
    variables:
      name: WSBC
    ```
  - Explicit key:value syntax example
    ```yml
    variables:
    - name:  myvariable
      value: WSBC 
    ```
- The key is the name of the variable, and it has a **string** value. 
- The variable is processed at **run** time.
- To dereference a variable, simply wrap the key in ```$()```.
- There are several types of variables, whereby pipelines do not distinguish between these types. 
  - Inline variables
  - Variable groups
  - Template variables
  - Pipeline variables
  - Predefined Azure DevOps agent and build [variables](https://docs.microsoft.com/en-us/azure/devops/pipelines/build/variables?view=azure-devops&tabs=yaml)

> **NOTE** - Explicit syntax is required when you mix variable types. For example:
>
> ```yml
>  variables:
>  - name:     myvariable
>    value:    WSBC
>  - group:    myVariableGroup
>  - template: myVariableTemplate.yml
> ```

## Parameters

- Parameters can be used in templates and pipelines. They allow us to deal with complex objects and combine parameters and expressions to create complex scenarios.

  ```yml
  parameters:
  - name: parameterSample
    type: string
    default: sunshine
    values:
    - sunshine
    - moonlight
    - aurora
  ```
- Unlike variables, parameters are defined as key value pairs where the value can be of **any type**.
- To dereference a parameter, simply wrap the key in `${{}}`.
- The variable is processed at **queue** time.

Powerful magic!

## Our second YAML pipeline

Now that we understand variables and parameters, let us create our second YAML pipeline and first template. No need to panic, you have not missed anything - we will explore templates in more detail in Part 3 of this series.

```yml
variables:
  keyFinal: 'Bingo!'
  keyRef:   'keyFinal'

steps:
  - script: echo $(${{variables.keyRef}})
  - script: echo $(${{ variables.keyRef }})
  - script: echo $( ${{ variables.keyRef }} )
  - template: template.yml
    parameters:
      test: ${{variables.keyRef}}
```

Did you notice that we assigned the value to the keyFinal variable, but are using keyRef throughout the sample? By using the queue-time ${{}} resolution, we are changing the first script to the following during queue time:

```yml
variables:
  keyFinal: 'Bingo!'
  keyRef:   'keyFinal'

steps:
  - script: echo $(keyFinal)
  - script: echo $(keyFinal)
  - script: echo $( keyFinal )
  - template: template.yml
    parameters:
      test: keyFinal
```

## Our first template

Like parameters the template is injected and processed at **queue** time.

```yml
parameters:
  test : 'defaultKey'  

steps:
  - script: echo here we go

  - script: echo ${{ parameters.test }}
  - script: echo $( parameters.test ) 
  - script: echo $(keyRef)
  - script: echo $( keyRef )
  - script: echo $( KeyRef )
  - script: echo $( ${{ parameters.test }} )
  - script: echo $(${{ parameters.test }})
  - script: echo $(${{parameters.test}})
```

I recommend that you create the sample pipeline and run it. Does it display what you expected? If yes, you can skip the YAML Gotchas, otherwise read on.

## Generated echo output

Take note of the fourth, fifth, and sixth echo in the template. You may expect that the output will be the same ... but:

- Fourth ```echo $(keyRef)``` displays ```keyFinal``` as expected.
- Fifth  ```echo $( keyRef )``` displays ```command not found``` ... too many spaces. 
- Sixth  ```echo $( KeyRef )``` displays ```command not found``` ... YAML is case-sensitive and too many spaces.

```
Bingo!
Bingo!
... command not found
here we go
keyFinal
... command not found
keyFinal
keyRef: command not found
KeyRef: command not found
keyFinal command not found
Bingo!
Bingo!
```

---

# YAML Gotchas, such as spaces

For example, alignment of your definition is critical. Just like in the Cobol and Fortran days, a space too many or too few will throw errors, that are often difficult to decipher. As shown in the simple example, these two statements look the same, however, the second has too many spaces and fails:

```yml
  - script: echo $(${{ variables.keyRef }})
  - script: echo $( ${{ variables.keyRef }} )
``` 

Likewise, the following example looks innocent at a quick glance, but the first and third script will fail as it is indented few and one too many spaces respectively:

```yml
steps:
 - script: echo $(${{variables.keyRef}})
  - script: echo $(${{variables.keyRef}})
   - script: echo $(${{variables.keyRef}})
``` 

Yaml is a very positional and pedantic language!

> **TIP** - Use the **validate** feature in the Azure Pipeline editor to help you unearth some of the gremlins.

![YAML Pipeline](/images/moving-hundreds-of-pipeline-snowflakes-part2-4.png)

---

# Common language

With the various names popping up - classic, unified, YAML, and multi-stage - it is important to define and use a common language when talking about pipelines. Within the context of Azure DevOps pipelines, we suggest and use the following in these technical blogs:

| TERMINOLOGY | DESCRIPTION |
|-------------|-------------|
| Classic Unified Pipeline |	Unified pipeline design practice, defined by WSBC, based on the user interface (Classic) Azure Pipeline to promote a consistent CICD pipeline. |
| Multi-stage YAML-syntax Pipeline |	Unified YAML experience to create an Azure Pipeline to do CI, CD, or CI and CD, and store the pipeline configuration as part of the source code. |
| Multi-stage Blueprint-based Pipeline | Unified pipeline design practice, defined by WSBC, based on the multi-stage YAML-syntax pipeline to promote a consistent, secure, and extensible CI/CD pipeline. |
| Continuous Exploration (CE)	| Continuous analysis of an idea or hypothesis, customer feedback, or market research through rapid prototyping. OODA – Observe, Orient, Decide, Act. |
| Continuous Integration (CI)	| Continuously collaboration, validation, and merging of code changes. Also known as a continuous and automated “Build”. |
| Continuous Deployment (CD) | Ability to use the output from the CI to build and deploy the new known good build to **one** environment automatically – for example, deploy straight to production. |
| Continuous Delivery (CD) | Ability to use the output from the CI to build and deploy the new known good build to **one** or **more** environments automatically – for example, deploy to multiple rings. |
| Release on Demand (RoD) | Ability to make changes available to customers all at once, or selectively in response to feedback or business needs. |

# What is next?

If erroneous spaces do not rattle you, we are ready to jump into [part 3](yaml-pipelines-part3.html) to explore the power of templates and how we are cooking up a storm of re-usable magic.

---

> Series Bread Crumbs | [Part 1, TOC](/why-pipelines-part1.html) | Part 2 | [Part 3](/yaml-pipelines-part3.html) | [Part 4](/yaml-pipelines-part4.html) | [Part 5](/yaml-pipelines-part5.html) | [Part 6](/yaml-pipelines-part6.html) | [Part 7](/yaml-pipelines-part7.html) | [Part 8](/yaml-pipelines-part8.html) | [Part 9](/yaml-pipelines-part9.html) | [Part 10](/yaml-pipelines-part10.html) | [Part 11](/yaml-pipelines-part11.html) |



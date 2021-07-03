Title: Azure DevOps Experimentation - YAML Conditionals, Parameters, and Triggers
Date: 2021-04-28 13:13
Category: Posts
Tags: azure-devops, pipelines, tips
Slug: experiment-yaml-1
Author: Willy-Peter Schaub
Summary: Snippets of common questions and issues from Azure Pipeline workshops and support calls. Today's snippet includes conditionals, parameters, and triggers. 

If you are an avid user of the YAML-based Azure Pipelines, you will be aware that the language can be very pedantic when it comes to too many or too few spaces. In fact, we have been mulling over a broken pipeline for (what felt like) hours, only to realise that we were misaligned by **one** space. Fortunately, both the YAML editor in both Azure DevOps and Visual Studio Code, as well as the **Validate** features are continuously improving.

Let us park the spaces topic and focus on conditionals, parameters, and triggers, using this simple sample code.

> Experimentation Sample Code

```yml
trigger:
- none

parameters:
- name: branch
  displayName: 'Branch Name'
  type: string
  default: release
  values:
  - rElEaSe
  - ReLeAsE
  - Release
  - release
  - master

pool:
  vmImage: windows-latest

variables:
  keyFinal: 'Bingo!'
  keyRef:   'keyFinal'
  keyTest:  ${{variables.keyRef}}

steps:
- script: echo 1. Hello, world!
  displayName: 'Welcome'

# Referencing
- script: echo 2. $(keyTest)
- script: echo 3. $(${{variables.keyRef}})

# Run-time Parameters
- script: echo Branch = ${{parameters.branch}}

# Lower
- ${{ if eq( lower(parameters.branch), 'release' ) }}:
  - script: echo Bingo!

# Release only
- ${{ if or( eq(variables['Build.SourceBranch'], 'refs/heads/release'), startsWith(variables['Build.SourceBranch'], 'refs/heads/release/')) }}:
  - script: echo Release!
``` 

# Triggers

You can configure a trigger to fire **manually**, **never**, or as **changes** are made to selected branches, tags, and folders.

> ![Learning](/images/experiment-yaml-1-1.jpg)

- If you remove the trigger all together, the pipeline will be triggered if **any** change is made to any **folder** or **branch**. 
- If you want to have a **manually** triggered pipeline, you must configure ```- none```, as in today's sample code.

See [Triggers](https://docs.microsoft.com/en-us/azure/devops/pipelines/yaml-schema?view=azure-devops&tabs=schema%2Cparameter-schema#triggers) for details.

---

# Parameters

You can use parameters in templates and pipelines, as visualised on our [YAML Generic Blueprint-based Pipeline Quick Reference](https://wsbctechnicalblog.github.io/moving-hundreds-of-pipeline-snowflakes-qr-1.html) and documented in detail in the [YAML Schema](https://aka.ms/YAML).

> ![Learning](/images/experiment-yaml-1-1.jpg)

- Parameter key:value pairs are evaluated at **queue** time.
- You can define a pipeline parameter, as in the sample code above.
- When you run the sample pipeline, you can select from the available values, as shown:

> ![Run pipeline](/images/experiment-yaml-1-2.png)

See [Parameters](https://docs.microsoft.com/en-us/azure/devops/pipelines/yaml-schema?view=azure-devops&tabs=schema%2Cparameter-schema#parameters) for details.

---

# Variables

You can add static values, reference variable groups, or insert  variable templates into your pipeline.

> ![Learning](/images/experiment-yaml-1-1.jpg)

- Variable key:value pairs are evaluated at **run** time.
- Echo 1 is boring, but we must say hello!
- Echo 2 displays the value of **keyTest**, which was set to the same value as **keyRef**
  > Output:**keyFinal**.
- Echo 3 is the one that is a bit more interesting. It is changed to $(keyFinal) at queue time, which demonstrates a rudimentary use of **reference** values. I had to write and run the sample to get my head around the code - try it yourself! 
  > Output: **Bingo!**

See [Variables](https://docs.microsoft.com/en-us/azure/devops/pipelines/yaml-schema?view=azure-devops&tabs=schema%2Cparameter-schema#variables) for details.

---

# Conditionals

Lastly, conditions can be used to determine whether tasks should execute or if code or entire template are injected into the pipeline at queue time.

> ![Learning](/images/experiment-yaml-1-1.jpg)

- ```# Lower``` demonstrates how to include tasks if certain conditions are met. In our sample, we check if the selected ```parameters.branch``` is equal to 'release'. If yes, Bingo!
- Note how we convert the parameter to lowercase before doing the comparison, so that any combination of casing for ```release``` will meet the condition.
- ```Release only``` demonstrates how to include tasks if and only if the origin source branch matches ```refs/heads/release``` or starts with ```refs/heads/release/```.

We make extensive use of conditions in our blueprints and re-usable toolkit templates. 

See [Expressions](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/expressions) for details.

---

We are done for today. 

Hope these snippets are adding value and looking forward to your candid feedback. See you in the next experiment.

```


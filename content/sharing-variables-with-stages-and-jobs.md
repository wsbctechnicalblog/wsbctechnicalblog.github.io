Title: Gotchas when share variables with Azure DevOps stages and jobs
Date: 2021-07-08
Category: Posts
Tags: azure-devops, pipelines, tips
Slug: sharing-variables-with-stages-and-jobs
Author: Willy-Peter Schaub
Summary: Understanding and avoiding gotchas that may keep you up at 2AM, troubleshooting YAML-based Azure Pipelines

I assume that you have read our [How to share variables amongst Azure Pipeline agents](/sharing-variables-with-stages-and-jobs.html), which shared a few turbulent moments we experienced while troubleshooting this feature earlier this year. With this post we continue our troubleshooting excursion to highlight a few gotchas that have caused lots of head scratching.

---

# Core Syntax

Here are two reminders to tattoo on your forearm, when referencing variables:

- Within a stage, map variables as: ```dependencies.<stage>.<job>.outputs['<step>.<name>']```
- Across stages, map variables as: ```stageDependencies.<stage>.<job>.outputs['<step>.<name>']```

Let us lift the pipeline bonnet and explore.

---

# STEP 1: Define a variable to be shared

We define three variables, named secretValue1, secretValue2, and secretValue3 in our job called StageOneJobOne. Note that we explicitly name two of the steps and leave one as default. Sounds simple, but this will bite is later on.

```
  - job: StageOneJobOne
    pool:
      vmImage: 'windows-latest'
    steps:
    - bash: echo "##vso[task.setvariable variable=secretValue1;isOutput=true]BINGO-1!"
      name: SetVariable1
    - bash: echo "##vso[task.setvariable variable=secretValue2;isOutput=true]BINGO-2!"
    - bash: echo "##vso[task.setvariable variable=secretValue3;isOutput=true]BINGO-3!"
      name: SetVariable3
    - task: DutchWorkzToolsAllVariables@1
```

The last task, which unfortunately only runs on a Windows-based agent, uses the [Display all variables](https://marketplace.visualstudio.com/items?itemName=dutchworkz.DisplayAllVariables) extension, which displays all variables that are available during your Build or Release. It is an exceptional troubleshooting companion and we find all three of our variables listed as individual variables, and as part of the VSTS_PUBLIC_VARIABLES collection. 

> Extract from task log

```
...
BASH_SECRETVALUE2: BINGO-2!
...
SETVARIABLE1_SECRETVALUE1: BINGO-1!
SETVARIABLE3_SECRETVALUE3: BINGO-3!
...
VSTS_PUBLIC_VARIABLES: ["agent.TempDirectory",...,"SetVariable1.secretValue1",...,"Bash.secretValue2",...,"SetVariable3.secretValue3"...]
VSTS_SECRET_VARIABLES: ["system.accessToken"]
...
```

If you cannot resolve a variable, add this task to determine if and in which shape it is included. As you may have noted our three variables are mapped slightly differently. The two generated  by the explicitly names step have inherited the step names ```SetVariable1``` and ```SetVariable3```, whereas the other assumed the default task name, ```Bash```. Assumptions one of the evil roots of the infamous 2AM-calls!

---

#STEP 2: Reference variable in another job with the same stage

Next we reference  the variables in another job and echo their values.

```
  - job: StageOneJobTwo
    dependsOn: StageOneJobOne
    pool:
      vmImage: 'ubuntu-latest'
    variables:
      var1: $[ dependencies.StageOneJobOne.outputs['SetVariable1.secretValue1'] ]
      # Gotcha #1
      var2: $[ dependencies.StageOneJobOne.outputs['secretValue2'] ] 
    steps:
    - script: echo $(var1)
    - script: echo $(var2)
      name: GOTCHA_1
```

Looking at the stage log, we immediately notice that our first ```var1``` variable has been resolved as expected, the second ```var2``` variable is blank?!?

> ![Gotcha1](/images/sharing-variables-with-stages-and-jobs-1.png)

If you refer back to your forearm and look at the tattoo for mapping a variable within the stage, you realise we are missing the step name. It is fairly easy to pinpoint this GOTCHA when you use the tools at your disposal, such as the [Display all variables](https://marketplace.visualstudio.com/items?itemName=dutchworkz.DisplayAllVariables) extension and the trustworthy log files.

---

#STEP 3: Reference variable in another job in a different stage

Next we reference the variables in another job from another stage and echo the value. The sample shows the use of a stage and a job variable and highlights the importance of using your second tattoo, which uses **stageDependencies...** instead of **dependencies...** we used before. In fact the sample intentionally uses both, to welcome GOTCHA #2.

```
- stage: StageTwo
  dependsOn: StageOne
  variables:
    varStage: $[ stageDependencies.StageOne.StageOneJobOne.outputs['SetVariable1.secretValue1'] ]
  jobs:
  - job: StageTwoJobOne
    pool:
      vmImage: 'windows-latest'
    variables:
      var2: $[ stageDependencies.StageOne.StageOneJobOne.outputs['SetVariable1.secretValue1'] ]
      var3: $[ dependencies.StageOne.StageOneJobOne.outputs['SetVariable1.secretValue1'] ]
    steps:
    - task: DutchWorkzToolsAllVariables@1
    - script: echo $(varStage)
    - script: echo $(var2)
    - script: echo $(var3)
      name: GOTCHA_2
```

Looking at the job's log file, we immediately notice the GOTCHA.

> ![Gotcha2](/images/sharing-variables-with-stages-and-jobs-2.png)

---

# Troubleshooting Checklist

When things go belly up with your variables, I recommend that you:

1. Look at the job logs and check if variables have been prepared correctly.
2. Run on a Windows-based agent and [Display all variables](https://marketplace.visualstudio.com/items?itemName=dutchworkz.DisplayAllVariables).
3. Check that your steps creating the variables have a **name**.
4. Check that your steps referencing the variables use the correct **mapping** as per the tattoo on your forearm.

---

Last, but not least, here is the complete sample code for the pipeline we experimented with.

```
stages:

# ##################################################################################################
# STAGE ONE
# ##################################################################################################
- stage: StageOne
  jobs:
  # ------------------------------------------------------------------------------------------------
  # STAGE 1 JOB 1
  # ------------------------------------------------------------------------------------------------
  - job: StageOneJobOne
    pool:
      vmImage: 'windows-latest'
    steps:
    - bash: echo "##vso[task.setvariable variable=secretValue1;isOutput=true]BINGO-1!"
      name: SetVariable1
    - bash: echo "##vso[task.setvariable variable=secretValue2;isOutput=true]BINGO-2!"
    - bash: echo "##vso[task.setvariable variable=secretValue3;isOutput=true]BINGO-3!"
      name: SetVariable3
    - task: DutchWorkzToolsAllVariables@1

  # ------------------------------------------------------------------------------------------------
  # STAGE 1 JOB 2
  # ------------------------------------------------------------------------------------------------
  - job: StageOneJobTwo
    dependsOn: StageOneJobOne
    pool:
      vmImage: 'ubuntu-latest'
    variables:
      var1: $[ dependencies.StageOneJobOne.outputs['SetVariable1.secretValue1'] ]
      # Gotcha #1
      var2: $[ dependencies.StageOneJobOne.outputs['secretValue2'] ] 
    steps:
    - script: echo $(var1)
    - script: echo $(var2)
      name: GOTCHA_1

  # ------------------------------------------------------------------------------------------------
  # STAGE 1 JOB 3
  # ------------------------------------------------------------------------------------------------
  - job: StageOneJobThree
    dependsOn: 
    - StageOneJobOne
    - StageOneJobTwo
    condition: eq(dependencies.StageOneJobOne.outputs['SetVariable1.secretValue1'], 'BINGO-1!') 
    pool:
      vmImage: 'macOS-latest'
    variables:
      var1: $[ dependencies.StageOneJobOne.outputs['SetVariable1.secretValue1'] ]
    steps:
    - script: echo $(var1)

  # ------------------------------------------------------------------------------------------------
  # STAGE 1 JOB 4
  # ------------------------------------------------------------------------------------------------
  - job: StageOneJobFour
    dependsOn: 
    - StageOneJobOne
    - StageOneJobTwo
    pool: server
    variables:
      var1: $[ dependencies.StageOneJobOne.outputs['SetVariable1.secretValue1'] ]

# ##################################################################################################
# STAGE TWO
# ##################################################################################################
- stage: StageTwo
  dependsOn: StageOne
  variables:
    varStage: $[ stageDependencies.StageOne.StageOneJobOne.outputs['SetVariable1.secretValue1'] ]
  jobs:
  - job: StageTwoJobOne
    pool:
      vmImage: 'windows-latest'
    variables:
      var2: $[ stageDependencies.StageOne.StageOneJobOne.outputs['SetVariable1.secretValue1'] ]
      var3: $[ dependencies.StageOne.StageOneJobOne.outputs['SetVariable1.secretValue1'] ]
    steps:
    - task: DutchWorkzToolsAllVariables@1
    - script: echo $(varStage)
    - script: echo $(var2)
    - script: echo $(var3)
      name: GOTCHA_2
```


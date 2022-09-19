Title: Part 4: Pipelines - Magic of queue time assembly
Date: 2021-01-13
Category: Posts
Tags: azure-devops, devops, pipelines, x-as-code 
Slug: yaml-pipelines-part4
Author: Willy-Peter Schaub
Summary: We can use the power of the new multi-stage YAML pipelines to make even our most critical security engineers smile from ear to ear.

Welcome back to our exciting pipeline journey, as outlined in [part1](/why-pipelines-part1.html). It is time to move from theory to practice and explore some of the magic that is pushing us from the classic to the new YAML-based Azure Pipelines.

---

# Re-usable Templates

In [Part 3: Pipelines - Basic building blocks as templates and sprinkling on telemetry](/yaml-pipelines-part3.html) we covered YAML pipelines and why they are so exciting. Ardent classic pipeline supporters will argue that [Task Groups](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/task-groups?view=azure-devops) offer the same feature as YAML templates - I would argue similar, but not the same. Why? Both allow us to abstract pipeline logic into re-usable containers, which can be included in pipeline definitions.

Where the YAML-template take us a huge stride further is magic #2 we are covering later in this post and the fact that template are version controlled and exposed to change, review, and collaboration through [Pull Requests](https://docs.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops).

For example, when we plan to make fundamental and potentially pipeline breaking changes to our pipelines, we can build and test the change continuously, while collaborating with the rest of the pipeline working group in an all-embracing pull request. Only once all guardrails are met and everyone is satisfied that we have a quality change, will the pull request be approved, and the changes merged into our master branch to be consumed.

---

# Magic #1 - Parameter driven pipeline

Let us start looking at some of the magic, starting with a small, yet powerful feature of parameters.

![Master PR Merge](/images/moving-hundreds-of-pipeline-snowflakes-part4-3.png)

You can define parameters in your main template, as shown in the above illustration on the left. As discussed in [Part 2](/yaml-pipelines-part2.html) we define parameters as key/value paid and optionally add a list of values, as well as a default.

The magic appears when you run the pipeline. As shown on the right in the above illustration, the parameter(s) are included as run-time and editable pipelines values. So cool!

---

# Magic #2 - Queue Time Pipeline Assembly 

With classic pipelines what you design and what you see in the pipeline editor, is what you will queue and what the agent pools get to process. And yes, we can add conditional steps by using custom conditions, such as ```ne(variables['Agent.JobStatus'], 'SuceededWithIssues)```, but whether the conditions are met, the tasks will be included in the queued pipeline.

With the multi-stage pipelines this is where magic #2 enters the building, because conditional expressions are validated at queue time to **inject** or **ignore** parts of the templates. The following image shows the **same** pipeline queued - on the left (1) it runs with 14 steps and on the right (2) with 24 steps. The same pipeline ... what is going on?!?

> Same pipeline, same definition, different context!
> ![Master PR Merge](/images/moving-hundreds-of-pipeline-snowflakes-part4-1.png)

Upon closer inspection we notice a (3) **Bootstrap Validation Suppression Alert** in the first (1) pipeline run, which is our current behaviour for builds run outside a pull request. On the right we see the same pipeline run (2) within the context of a pull request validation build, which **injects** (4) SonarQube, (5) WhiteSource, and (6) our Building Code. It is important to emphasise that the pipeline on the left does not include the additional steps, optimising the runtime processing and keeping the logs focused and simple.

The magic is based on conditional expressions, as the following extract I pulled from our bootstrap template. It instructs the Azure Pipeline queuing feature to only inject the template if ( we are in the "run" mode, and ( the source branch is "merge" or forceCheck is true ) ). 

```yml
- ${{ if and(eq( parameters.bootstrapMode, 'run' ), or(eq(variables['Build.SourceBranchName'], 'merge'), eq( parameters.forceCheck, 'true'))) }}:
  - template: SampleFolder/SampleTemplate.yml
```

If the conditional expression is not met, the template is **not** injected, and the template contents omitted from the queued pipeline. 

---

# Magic #3 - Cannot override guardrails

Remember [artifact filters](https://docs.microsoft.com/en-us/azure/devops/pipelines/release/deploy-multiple-branches?view=azure-devops#:~:text=Azure%20Pipelines%20%7C%20Azure%20DevOps%20Server%202019%20Artifact,stage%20only%20when%20those%20filter%20conditions%20are%20met.)? A great way to protect deployment stages in classic pipelines from artifacts built from untrusted branches - "*Applying the artifact filter to a specific branch results in the artifact deploying to a specific stage only when those filter conditions are met.*" - docs.microsoft.com

Unfortunately, as our security engineers remind us on a regular basis, these can be overridden by users with the right permission. Something that promises to be and should be immutable, can mutate as needed - not cool!

Looking forward, however, we can use the power of the new multi-stage YAML pipelines to make even our most critical security engineers smile from ear to ear ... and that is no easy feat!

Watch this quick video for a demo of the power, sorry magic, of the new pipelines.

[![Master PR Merge](/images/moving-hundreds-of-pipeline-snowflakes-part4-2.png)](https://youtu.be/DWuDqCM1t6A) [1:52]

Here is an extract from our demo pipeline. Note that unlike in prior examples, we have no conditional expression to determine whether to inject the template or not.

```yml
# DEV Stage
#
# EXAMPLE - INJECT STAGE
- template: Templates/Samples/DeploymentStage.yml@CDTemplates
  parameters:
    stageID:         'CD_Development'
    stageName:       'CD Development'
    vmImage:         'ubuntu-latest'
    envName:         'DPMSDP Development Environment'
# SY Stage
#
# EXAMPLE - INJECT STAGE
- template: Templates/Samples/DeploymentStage.yml@CDTemplates
  parameters:
    stageID:         'CD_System_Test'
    stageName:       'CD System Test'
    vmImage:         'windows-latest'
    envName:         'DPMSDP System Test Environment'
# ST Stage
#
# EXAMPLE - INJECT STAGE
- template: Templates/Samples/DeploymentStageR.yml@CDTemplates
  parameters:
    stageID:         'CD_Stage'
    stageName:       'CD Stage'
    vmImage:         'ubuntu-latest'
    envName:         'DPMSDP Stage Environment'
# PROD Stage
#
# EXAMPLE - INJECT STAGE
- template: Templates/Samples/DeploymentStageR.yml@CDTemplates
  parameters:
    stageID:         'CD_Production'
    stageName:       'CD Production'
    vmImage:         'macOS-latest'
    envName:         'DPMSDP Production Environment'
```
> ![Alert](/images/alert-tiny.png)
>
> The last deployment uses the macOS pool, which created a few migraines for us that are worth pointing out. If you peruse [Microsoft-hosted agents](https://docs.microsoft.com/en-us/azure/devops/pipelines/agents/hosted?view=azure-devops&tabs=yaml#networking) you will note two potential issues:
>
> - "*Agents that run macOS images are provisioned on Mac pros. These agents always run in US and Europe irrespective of the location of your Azure DevOps organization. If data sovereignty is important to you and if your organization is not in one of these geographies, then you should not use macOS images*"
> - "*Our Mac IP ranges are not included in the Azure IPs above, though we are investigating options to publish these in the future.*"
>
> Not a DevSecOps friendly agent pool - we have an open support ticket. If you want to know more or have more information, ping me!

In this case we are using conditional expressions in the DeploymentStage**R**.yml template, which protects the higher environments ending with **Stage** and **Production** from all branches other than the **release** branch. In the following conditional expression example we only allow deployments to the higher environments from the release branch. 

```yml
- ${{ if and( or( endsWith(parameters.stageName,'Stage'), endsWith(parameters.stageName,'Production')), eq(variables['Build.SourceBranchName'], 'release')) }}:
```

> ![Alert](/images/alert-tiny.png)
>
> If you are using release/* as your release branch, for example release/1.0.13, you need to change the last part of the conditional statement to something like ```startsWith(variables['Build.SourceBranch'], 'refs/heads/release/')```.

Combined with **Approvals and checks** of [Service connections](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops&tabs=yaml) and [Environments](https://docs.microsoft.com/en-us/azure/devops/pipelines/process/environments?view=azure-devops) the demonstrated magic allows us to align our pipelines with all our goals, such as alignment, consistency, enablement, and **security**. 

Simplicity is a goal that will drive our future pipeline endeavors and define our success, because with all the power and flexibility of YAML, it is all too easy to create another ocean of complex and potentially unmaintainable pipelines.

---

# What is next?

Now that we appreciate the power and some of the magic, we can shift gears to our blueprints. See you in [part 5](yaml-pipelines-part5.html).

---

> Series Bread Crumbs | [Part 1, TOC](/why-pipelines-part1.html) | [Part 2](/yaml-pipelines-part2.html) | [Part 3](/yaml-pipelines-part3.html) | Part 4 | [Part 5](/yaml-pipelines-part5.html) | [Part 6](/yaml-pipelines-part6.html) | [Part 7](/yaml-pipelines-part7.html) |  [Part 8](/yaml-pipelines-part8.html) | [Part 9](/yaml-pipelines-part9.html) | [Part 10](/yaml-pipelines-part10.html) | [Part 11](/yaml-pipelines-part11.html) |


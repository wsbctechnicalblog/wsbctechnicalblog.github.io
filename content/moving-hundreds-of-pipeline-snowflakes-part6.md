Title: Part 6: Pipelines - Gotcha! The generic blueprint-based YAML pipeline simplicity
Date: 2021-02-28
Category: Posts
Tags: Azure-Pipelines, DevOps
Slug: yaml-pipelines-part6
Author: Willy-Peter Schaub
Summary: Neither the bootstrap nor generic templates are rocket science, and the YAML-based pipelines are as complex as **you** make them.

Welcome back to another installment of our exciting pipeline journey, as outlined in [part 1](/why-pipelines-part1.html). After introducing the blueprint templates on [part 5](/yaml-pipelines-part5.html), it is time to emphasise that these new YAML-based pipelines are not complex if applied correctly.

---

# Why this post?

@TBD@

---

# Generic pipeline value streams

"_*_A job is a collection of steps run by an agent or on a server. Jobs can run conditionally and might depend on earlier jobs._*_" - [yaml-schema](https://docs.microsoft.com/en-us/azure/devops/pipelines/yaml-schema?view=azure-devops&tabs=schema%2Cparameter-schema#job)

When you add SonarQube to your pipeline, you know (or will find out) that the SonarQube **Prepare**, **Analyse**, and **Publish** steps must run in the same job context as the **build**. This is not a new constraint and applies to the **Classic**, **YAML out-of-the-box**, and our **Blueprint-based** Azure Pipelines.

The **simplest** pipeline you can configure is a single-job pipeline, which runs your **build**and **test** steps, the **DevSecOps** steps (SonarQube, WhiteSource), and the **BuildingCode** steps within one and the same job 1 context, as shown below.

> Single Job Pipeline
> ![Single Job Pipeline](/images/moving-hundreds-of-pipeline-snowflakes-part6-1.png)

When you split your pipeline into two jJobs you have two separate job contexts. Similar to the single-job you could run both the **DevSecOps** and the **BuildingCode** steps within the same job 1 context. Alternatively you could run the **DevSecOps** in the job 1 context and the **BuildingCode** steps in the job 2 context, as shown below. 

> Dual Job Pipeline
> ![Dual Job Pipeline](/images/moving-hundreds-of-pipeline-snowflakes-part6-2.png)

The same strategies apply to pipelines with 3 or more jobs. As you increase the number of jobs, you can embrace parallelism, introduce job dependencies, and isolate steps in separate contexts. 

> Multi Job Pipeline
> ![Multi Job Pipeline](/images/moving-hundreds-of-pipeline-snowflakes-part6-3.png)

Remember, "_with power, comes great responsibility_" and we inherit complexity and throw simplicity out of the window. In fact, you can create a really powerful, but also complex and hard to maintain and support pipeline. The choice is **yours**!

---

# Bootstrap template demystified

We covered the basics and the power of YAML templates in previous parts of this pipeline series.

 Our **Bootstrap** template is a standard YAML template with conditional statements. Visualise the internals as a **switch** statement, which injects templates containing steps, based on the **bootstrapMode** parameter passed.

The following table summarises the currently available **bootstrapmode**s, the template and associated steps it injects into your pipeline at queue time.

| BOOTSTRAPMODE    | INJECT TEMPLATE   | RUN STEPS                                             |
|------------------|-------------------|-------------------------------------------------------|
| init             | DevSecOpsInit.yml | SonarQube Prepare                                     |
| devsecopsonly    | DevSecOps.yml     | SonarQube Analyse, SonarQube Publish, and WhiteSource |
| buildingcodeonly | BuildingCode.yml  | BuildingCode Scripts, such as Stryker                 |
| run              | DevSecOps.yml **and** BuildingCode.yml | SonarQube Analyse, SonarQube Publish, WhiteSource, and BuildCode |

Here is a visualisation of the above table for the visual minds.

> Bootstrap Template and Bootstrap Modes
> ![Bootstrap](/images/moving-hundreds-of-pipeline-snowflakes-part6-6.png)

> **TIP** <br/>
> Our Bootstrap.yml templates is a standard YAML-template, as are the templates it injects at queue time. There is no hidden cloak and dagger technology or additional complexity! 

```yml
- template: Templates/Bootstrap.yml@CDTemplates
  parameters:
    bootstrapMode:    'init'
    applicationType:  'TODO REPLACE WITH SUPPORTED TYPE' # dotnet, angular
    applicationGuid:  $(productGuid)
    portfolioName:    $(portfolioName)
    productName:      $(productName)
    sourcesDirectory: $(Build.SourcesDirectory)
```

You now have the **option** of including the Bootstrap.yml template instead of explicitly including SonarQube, WhiteSource, and Building Code steps. Note I say **option**, not that you must do it one way or the other. 

Similar to Software-as-a-Service (SaaS) solutions you can delegate these steps and accountability to the Bootstrap.yml template, which is enhanced, maintained and supported by our pipeline working group. The choice is **yours**!

---

# Generic Blueprint templates demystified

@TBD@

> Single Job Pipeline
> ![Single Job Pipeline](/images/moving-hundreds-of-pipeline-snowflakes-part6-4.png)

@TBD@

> Dual Job Pipeline
> ![Dual Job Pipeline](/images/moving-hundreds-of-pipeline-snowflakes-part6-5.png)

---

# What is next?

Now that we all agree that neither the bootstrap nor generic templates are rocket science, and that YAML-based pipelines are as complex as **you** make them, we can move ahead with the adoption of our new pipelines. 

- [X] Consistent pipelines
- [X] Enable engineers
- [X] Simple pipelines

But wait, there is more ... in the next part 7, my colleague Said will introduce the next generation of blueprints which are even simpler, supporting our goals for consistency and enablement. 

See you in part 7 (coming soon).

---

> Series Bread Crumbs | [Part 1, TOC](/why-pipelines-part1.html) | [Part 2](/yaml-pipelines-part2.html) | [Part 3](/yaml-pipelines-part3.html) | [Part 4](/yaml-pipelines-part4.html) | [Part 5](/yaml-pipelines-part5.html) | Part 6 | 


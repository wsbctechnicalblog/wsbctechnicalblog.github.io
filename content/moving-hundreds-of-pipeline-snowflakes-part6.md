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

We have received feedback from the engineering teams and our inspect and adapt workshops, that YAML pipelines are complex and require a steep learning curve. 

Perhaps I am biased, but I disagree. My four cents (points):

- YAML pipelines are more intuitive to engineers familiar with code.
- Apart from the visual value, the Classic pipeline editor adds no value to the editing experience. Adding a step in a YAML pipeline is as simple  (similar) as adding a step in a classic pipeline.
- If all else fails, create your Azure Pipeline in your editor of choice and export to YAML. That is how we started many moons ago and a great way to get familiar with the [YAML schema](https://docs.microsoft.com/en-us/azure/devops/pipelines/yaml-schema).
- When you start using pre-packaged templates, covered in [part 4](/yaml-pipelines-part4.html), [part 5](/yaml-pipelines-part5.html) and revisited herein, the adoption of YAML pipelines becomes a no-brainer. 

> "_Simplicity is the ultimate sophistication_" - Leonardo da Vinci

---

# Generic pipeline value streams

Let us take a few steps back and take a quick look at an Azure Pipeline from a high altitude. Each pipeline is made of one or more stages, each of which is a collection of related jobs, each of which is a collection of steps.

> Azure Pipeline from space
> ![Pipeline](/images/moving-hundreds-of-pipeline-snowflakes-part6-0.png)

Let us skip stages, zoom in, and start at the point of jobs, as shown above.

"_*_A job is a collection of steps run by an agent or on a server. Jobs can run conditionally and might depend on earlier jobs._*_" - [yaml-schema](https://docs.microsoft.com/en-us/azure/devops/pipelines/yaml-schema?view=azure-devops&tabs=schema%2Cparameter-schema#job)

When you add SonarQube to your pipeline, you know (or will find out) that the SonarQube **Prepare**, **Analyse**, and **Publish** steps must run in the same job context as the **build**. This is not a new constraint and applies to the **Classic**, **YAML out-of-the-box**, and our **Blueprint-based** Azure Pipelines.

The **simplest** pipeline you can configure is a single-job pipeline, which runs your **build** and **test** steps, the **DevSecOps** steps (SonarQube, WhiteSource), and the **BuildingCode** steps within one and the same job 1 context, as shown below.

> Single Job Pipeline
> ![Single Job Pipeline](/images/moving-hundreds-of-pipeline-snowflakes-part6-1.png)

When you split your pipeline into two jobs you have two separate job contexts. Similar to the single-job you could run both the **DevSecOps** and the **BuildingCode** steps within the same job 1 context. Alternatively, you could run the **DevSecOps** in the job 1 context and the **BuildingCode** steps in the job 2 context, as shown below. 

> Dual Job Pipeline
> ![Dual Job Pipeline](/images/moving-hundreds-of-pipeline-snowflakes-part6-2.png)
With multiple jobs you can embrace parallelism, introduce job dependencies and flows, isolate steps in separate job contexts, and run steps on different agent specifications (Linux, Windows, macOS) - all in one pipeline.

> Multi Job Pipeline
> ![Multi Job Pipeline](/images/moving-hundreds-of-pipeline-snowflakes-part6-3.png)

Remember, "_with power, comes great responsibility_". As we embrace complexity, we throw simplicity out of the window. In fact, as with the pile of LEGO blocks analogy we used in [part 5](/yaml-pipelines-part5.html), you can create really powerful, but also complex and hard to evolve and maintain pipelines. The choice is **yours**!

> WHAT and HOW you build is up to you...
> ![LEGO](/images/moving-hundreds-of-pipeline-snowflakes-part6-7.jpg)

---

# Bootstrap template demystified

We covered the basics and the power of YAML templates in previous parts of this pipeline series.

 Our **Bootstrap** template is a standard YAML template with conditional statements. Visualise the internals as a **switch** statement, which injects templates containing steps, based on the **bootstrapMode** parameter passed.

The following table summarises the currently available bootstrap **modes**, the **templates**, and associated **steps** it injects into your pipeline at queue time.

| BOOTSTRAPMODE    | INJECT TEMPLATE   | RUN STEPS                                             | TEMPLATE OWNED BY  |
|------------------|-------------------|-------------------------------------------------------|--------------------|
| init             | DevSecOpsInit.yml | SonarQube Prepare                                     | DevSecOps |
| devsecopsonly    | DevSecOps.yml     | SonarQube Analyse, SonarQube Publish, and WhiteSource | DevSecOps |
| buildingcodeonly | BuildingCode.yml  | BuildingCode Scripts, such as Stryker                 | Engineering Practices | 
| run              | DevSecOps.yml **+** BuildingCode.yml | SonarQube Analyse, SonarQube Publish, WhiteSource, and BuildCode | DevSecOps and Engineering Practices |

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

Similar to Software-as-a-Service (SaaS) solutions you can delegate these steps and accountability to the Bootstrap.yml template, which is continuously enhanced, maintained and supported by our pipeline working group. The choice is **yours**!

---

# Generic Blueprint templates demystified

Our **Azure-Pipeline-Steps.yml** is a generic blueprint that implements the single job pipeline we discussed and includes two calls to the **bootstrap.yml** template to **init**ialise the DevSecOps steps and to **run** the DevSecOps and Building code steps.

> Single Job Pipeline
> ![Single Job Pipeline](/images/moving-hundreds-of-pipeline-snowflakes-part6-4.png)

All you need to do, is find the **TODO** placeholders to update relevant parameters and insert your build and test steps. You can explore the **Azure-Pipeline-Steps.yml** blueprint in [Part 5: Pipelines - Blueprints to fuel consistency and enablement](https://wsbctechnicalblog.github.io/yaml-pipelines-part5.html).

Our **Azure-Pipeline-Jobs.yml** is a generic blueprint that implements the multi job pipeline we discussed and includes three calls to the **bootstrap.yml** template to **init**ialise the DevSecOps steps and run the **devseconlyinit** within the same job context. Lastly, it runs the **buildingcodeonly** steps in a different job context.

> Dual Job Pipeline
> ![Dual Job Pipeline](/images/moving-hundreds-of-pipeline-snowflakes-part6-5.png)

As with the Azure-Pipeline-Steps.yml blueprint, you then search for the **TODO** placeholders and update relevant parameters and insert your build and test steps. It is that simple!

The genetic blueprints work well for new pipelines. If you already have a YAML-based pipeline, you can include the bootstrap.yml template into your existing pipeline. The choice is **yours**!

---

# Blueprint-related questions

Here are a few of the top questions we have received from engineering to date.

## Q1: Who owns our pipeline blueprints?

![Pull Request](/images/moving-hundreds-of-pipeline-snowflakes-part6-8.png)

Our common engineering system pipeline working group, a cluster of engineers representing architecture, development, operations, and security have joint forces to pursue our quest for **automation**, **consistency**, **security**, **simplicity**, and **alignment** with our guardrails (a friendlier term for governance). While we are all accountable for the blueprints and templates discussed herein, DevSecOps owns the DevSecOps*.yml templates and Engineering Practices the BuildingCode templates and associated scripts.

## Q2: How can engineers make changes to the blueprints?

![Pull Request](/images/moving-hundreds-of-pipeline-snowflakes-part6-9.png)

Using the [pull request](https://docs.microsoft.com/en-us/azure/devops/repos/git/pull-requests) workflow, engineers can discuss blueprint and template changes and agree to merge them once all stakeholders approve. We strive for complete transparency, allowing everyone to view the blueprints and associated templates, and contribute towards the continuous innovation of our YAML templates.

## Q3: Why are we so fixated on the consistency and simplicity goals?

![Pull Request](/images/moving-hundreds-of-pipeline-snowflakes-part6-10.png)

Infrastructure as code (IaC) is typically associated with the process of managing and provisioning computer data centers through machine-readable configuration files. The aim is to deprecate physical hardware configuration and interactive configuration tools. 

Within the context of our common engineering system, we are striving to use infrastructure as code to provision our continuous delivery pipelines and associated services as well. While the classic Azure Pipelines are powerful and well established, they are configured using a graphical configuration tool and tend to become hard to maintain and enhance over time.

The switch to YAML-based Azure Pipelines is enabling us to version control and store the pipelines as machine- and human-readable configuration code. We refer to this as **pipeline as code (PaC)**. If and only if we manage to create a consistent infrastructure of pipelines, using templates and blueprints, we not only enable our engineering teams, but take the first steps towards self service automation.

But, that is a vast topic for another day. Back to our YAML pipelines.

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


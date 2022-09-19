Title: Part 7: Pipelines - There is more! Simplicity and enablement, courtesy of the app-type blueprint-based YAML pipelines
Date: 2021-04-12
Category: Posts
Tags: azure-devops, devops, pipelines, x-as-code 
Slug: yaml-pipelines-part7
Author: Said Akram
Summary: Do you want to own two or seventy five dozen lines of pipeline code per application? The choice is yours!

Welcome back to another installment of pipeline wizardry. In [part 6](/yaml-pipelines-part6.html) we covered the simplicity of the generic blueprint-based YAML pipeline and mentioned that there is more magic. Welcome to our application-type blueprints!

---

# Why we teleported our generic blueprints one level higher

In [Pipeline-as-code wrapped with Pull Requests](/pipelines-as-code-pr.html) we explore infrastructure-as-code and the concept of pipeline-as-code and mention that each engineer building a continuous integration pipeline write an average of 900+ lines of json or YAML configuration ... per pipeline. Using generic blueprints, we managed to reduce this repetitive and thus wasted effort of engineering to 100+ lines of configuration code. A massive improvement, not only in terms of engineering effort, but also re-use and consistency of an ever-growing infrastructure of pipelines that needs to be nurtured and innovated continuously.

Our pipeline working group, made up of passionate engineers from architecture, security, development, infrastructure, release management, and site reliability engineering, agreed that we need to do better. As we have a handful of application architecture and technology-stacks, we also agreed that consistency, automation, and continuous innovation should form the foundation to self-service automation. 

> When we want to power up an electronic device, we plug it into the power grid and flip the on switch. None of us are interested in generating the power ourselves, or the local substation with an autonomy mindset.

That said, we are surprised at the outcome of a poll on Twitter and a LinkedIn, where we asked engineers if they want full or partial ownership of their pipelines, or self-service. Less than 50% are interested in self-service automation!?!

> Combined results from Twitter and LinkedIn quick polls as at 2021.03.30 23:13
>
> ![Pipeline ownership](/images/moving-hundreds-of-pipeline-snowflakes-part7-1.png)

Some conspiracies we noticed in the polls and discussions with engineering:

- *You are influencing engineering on how they should work by centralizing pipeline templates!*
  - **No**, we are allowing engineering to collaborate, innovate, and influence each other.
  - In fact, we are enabling the organization to package your hard earned experience and guardrails in re-usable templates.
- *You cannot possibly create a template for every scenario!*
  - **Fully agree**, especially as we are continuously innovating.
  - But, we can create templates and blueprints for common scenarios and re-use templates to quick-start the outliers. 
- *You should not abstract and hide the pipelines from engineering!*
  - **Fully agree**. As covered in [Pipeline-as-code wrapped with Pull Requests](/pipelines-as-code-pr.html), everyone can view the templates and blueprints and anyone can submit changes to existing templates or recommend new ones. The only thing we mandate is the use of pull requests to guard the template and blueprint repositories.

We will explore the real clincher, self-service automation, in a future planned post "*Self-service automation - A dream turns into reality*". In the meantime, rest assured that engineers are free to use their creativity to craft their precious snowflakes till the cows come home. We are here to enable and guide through continuous innovation, manifestos, and guardrails.

![Back on track](/images/moving-hundreds-of-pipeline-snowflakes-part7-3.png)

Let us get back on track. Why are we taking our generic blueprints, covered in [Part 6: Pipelines - Gotcha! The generic blueprint-based YAML pipeline simplicity](/yaml-pipelines-part6.html) and [Part 7: Pipelines - There is more! Simplicity and enablement, courtesy of the app-type blueprint-based YAML pipelines](/yaml-pipelines-part7.html), to another level? To reduce the engineering effort to ~28 lines of pipeline configuration. That is a saving of 97% of repetitive and often mind-numbing configuration engineering.

Have we caught your attention? If yes, read on.

---

# Unveiling our Application-Type Blueprints

With application-type, in short app-type, blueprints we are taking the continuous integration (CI) pipelines light-years further in terms of our goals for simplicity, security, enablement, and consistency. Each app-type blueprint, consists of a **starter** template, an **app-type** template, and a reference **sample** implementation, as shown below.

> Blueprint Architecture
>
> ![Blueprint Architecture](/images/moving-hundreds-of-pipeline-snowflakes-part7-2.png)

- The **starter** template allows you to configure your continuous integration pipeline. This is the only moving part that is copied and becomes part of your application code base, protected by your branch policies and your team-level pull request workflow.
- The **app-type** template abstracts the entire continuous integration (CI) process, our generic blueprints and integration with our bootstrap template, promoting consistency, delegates responsibility for the implementation to our common engineering system team, and encourages you to be razor-focused on your application. Anyone can view the blueprints (transparency) and everyone can submit a pipeline working group pull request to continuously innovate the blueprints (we are one).
- The **example** implementation of a starter and app-type template, sample application, and pipeline is self-explanatory. Handy awareness and validation aid.

Here is an example of our Azure Function starter template:

```yml 
trigger:
  batch: true # batch changes if true; start a new build for every push if false
  branches:
    include:
    - '*' # Trigger on all branches

resources:
  repositories:
  - repository: AppTemplates
    type:       git
    name:       'CeS/AzureDevOps.Automation.Pipeline.AppTemplates'

# Semantic version as per Azure DevOps Naming Conventions.
name:
  $(portfolioName)_$(productName)_$(GITVERSION_MAJORMINORPATCH)_$(date:yyyyMMdd).$(date:HHmmss).$(Build.SourceBranchName)

# VARIABLES
variables:
  portfolioName:    'TODO REPLACE WITH PORTFOLIO NAME' # e.g. CeS
  productName:      'TODO REPLACE WITH PRODUCT NAME' # e.g. Samples.AzureFunction

extends:
  template: Templates/AzureFunction/AzureFunctionTemplate.yml@AppTemplates
  parameters:
    netCoreVersion:         'TODO REPLACE WITH .NET CORE VERSION' # e.g. 3.1.x
    applicationGuid:        'TODO REPLACE WITH A NEW GUID WITHOUT BRACKETS' # e.g. 257929e89c69471083efb51899b42bdb
    portfolioName:          $(portfolioName)
    productName:            $(productName)
```

In case you have not counted yourself: A mere twenty-two (22) lines of configuration code, with only four (4) TODO that require minimal effort!

> "*It took me a few minutes to setup our entire continuous deployment (CD) proof-of-concept (PoC) environment, after which I was able to focus on the CD experiments. I am Said's App-type blueprints #1 fan!*" - [Willy Schaub](https://www.linkedin.com/in/wpschaub/)

Another nugget you may have missed in the platter of configuration code, is the **extends** template. It enables [Security through templates](https://docs.microsoft.com/en-us/azure/devops/pipelines/security/templates?view=azure-devops) and allows us to set a required template check gate for resources and environments. More on that when we share our CD PoC results.
 
--- 

# Don't repeat yourself

As software engineers, we try to avoid code duplication. Each time we spot a code used in two or more methods, we fix it by moving the code into its own method and calling that method from all of the places where it was originally used.

The same DRY principle can be applied to Continuous Integration (CI) build pipelines. As covered in [Part 5: Pipelines - Blueprints to fuel consistency and enablement](/yaml-pipelines-part5.html), we use pipeline blueprints to define reusable content.

Even if we have thousands of build pipelines, we only have a few application architectures. Our app-type templates can serve a big part of the applications we have. For the rest of the applications, we can create custom YAML based pipelines.

# Pipeline As a Service

As a software developer, do I want to own (i.e. create and maintain) the pipelines to build and deploy my application? My answer is **NO**.

I will be glad to let another team take that responsibility while I focus on creating value for the business by delivering quality software.

As long as I have access to the build pipeline templates and able to suggest changes, I will not lose my ability to do my work and troubleshoot issues if any.

# How to implement your pipeline using the App-Type Blueprints

This is where both the effort of creating new continuous integration (CI) build pipelines and writing this post becomes **simple**.

![How-to](/images/moving-hundreds-of-pipeline-snowflakes-part7-4.png)

1. Copy the content of the **starter** template from the CeS/AzureDevOps.Automation.Pipeline.Templates repository (aka the sample above).
2. Rename the app-type template from azure-pipelines-<TYPE>.yml as needed (an optional step).
3. Look for TODO and update / fine-tune as needed.

Other than running your pipeline, you are **DONE**! 

---

# What if an App-Type Blueprint is not available?

If our pipeline working group achieves a 75% coverage of all our current pipeline scenarios, such as Azure Artifact packages, .NET Core, or Angular applications, we will start celebrating. 

In the meantime, and to cover the remaining 25% there will always be an application type for which there is no blueprint, or a snowflake that requires something special.

![404](/images/moving-hundreds-of-pipeline-snowflakes-part7-5.png)

Our engineers have a simple flowchart if they cannot find a suitable blueprint in our template repository:

1. Create a custom **starter** and **app-type** blueprint from scratch or tweaking an existing blueprint. Latter is recommended.
1. Submit a **Pull Request** with your **starter** template to our CeS Templates repo.
1. Submit a **Pull Request** with your **app-type** template to our CeS AppTemplates repo. 
1. Collaborate with the pipeline working group to release your changes with the common engineering system.

**SIMPLE**, yet powerful wizardry!

---

# What is next?

We will report back on our proof-of-concept and associated experiments to extend the app-type continuous integration (CI) build pipeline blueprints to include continuous deployment (CD).

See you soon in Part 8: Pipelines - From CI to CD and beyond in one pipeline.

---

> Series Bread Crumbs | [Part 1, TOC](/why-pipelines-part1.html) | [Part 2](/yaml-pipelines-part2.html) | [Part 3](/yaml-pipelines-part3.html) | [Part 4](/yaml-pipelines-part4.html) | [Part 5](/yaml-pipelines-part5.html) | [Part 6](/yaml-pipelines-part6.html) | [Part 7](/yaml-pipelines-part7.html) | [Part 8](/yaml-pipelines-part8.html) | [Part 9](/yaml-pipelines-part9.html) | [Part 10](/yaml-pipelines-part10.html) | [Part 11](/yaml-pipelines-part11.html) |


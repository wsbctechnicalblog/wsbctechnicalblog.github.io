Title: Back to Basics: Why are we moving to v2 CI/CD Blueprints for Azure Pipelines?
Date: 2024-02-16
Category: Posts 
Tags: agile, azure-devops, pipelines, 101
Slug: back-to-basics-why-are-we-moving-to-v2-blueprints
Author: Willy-Peter Schaub
Summary: Understanding why we are disabling classic Azure Pipelines and embracing YAML-based Azure Pipelines.

We covered our move from classic to YAML-based Azure Pipelines in a detailed series, which begins at [Part 1: Pipelines - Why bother and what are our nightmares and options?](/yaml-pipelines-part1.html) and  triggered in our open-source initiative as covered in posts such as [Our road to OSS Blueprints - Suppress CD when pipeline runs within Pull Request](https://wsbctechnicalblog.github.io/yaml-pipelines-part11.html), [Azure Pipelines Blueprint QA Integration](https://wsbctechnicalblog.github.io/azure-pipelines-blueprint-qa-integration.html) and [Azure DevOps Pipeline OSS v2.1 Flow](https://wsbctechnicalblog.github.io/azure-devops-pipeline-oss-v2-1-flow.html). 

In this post, I will only answer the question of **WHY** and let you peruse our other posts for the implementation details.

---

# WHY are we moving away from and disabling classic Azure Pipelines?

The following image shows that **Classic** pipelines are the new name for the pipelines that started with MSBuild in Team Foundation Server (TFS) 2005, developed to XAML-based pipelines in TFS 2010, and finally to visual JSON-based pipelines in TFS 2015. 

> ![Classic](/images/back-to-basics-why-are-we-moving-to-v2-blueprints-0.png)

In 2013 Microsoft added the InRelease product, from InCycle Software, to include deployment in the build tools. The visual editor to create and configure the Classic Azure Pipelines was a useful feature for engineers who had problems with the changes of MSBuild, XAML, and JSON formats.

We are leaving the Classic pipelines behind for these reasons:  

- The term "**classic**" does not convey innovation or long-term support confidence.
- Although the **visual editor** is quite user friendly, the json it creates behind the scenes is complicated. A basic hello world classic build pipeline creates a JSON file of a 170+ lines. The same thing in YAML, takes around 20 lines, or less.
- The differences between classic **build** and **release** Azure Pipelines and especially their related REST APIs.
- The **operational effort and cost** to maintain hundreds of classic Azure Pipelines is huge. Operational automation has worked well, but also taken a lot of time - time we could use to enable our engineers. 
- Ensuring **consistency** and **standardization** in pipeline configurations and permissions is hard, leading to many unique (snowflakes) pipelines, which again take away from innovation.

>
> ![Alert](/images/back-to-basics-batch-size-alert.png)
>
> By the end of this year, our classic pipelines will be locked, so teams can still use them, but not modify them or make new ones.
>

---

# WHY are we moving to YAML-based Azure Pipelines?

The YAML pipeline introduced an exciting new era, launching in early 2019 with TFS 2019. It signaled a CI/CD solution designed from scratch on an INNOVATIVE whiteboard.

The main benefits of switching to YAML are:  

- **Simplicity** - instead of cluttering your **classic**** release pipelines with everything you can think of, the YAML pipelines focus on your essential steps to build and deploy your solution.  
- ***-as-code** - allows us to adopt pipeline-as-code (p-a-c) and configuration-as-code (c-a-c).  
- **Enable engineers** to evaluate and suggest improvements and innovations, based on transparency, and using a familiar tool - "pull requests".  
- **Re-use by using templates**.  
- **Centralized management** - Environments give us centralized control. It is simpler to manage checks in one place for an environment, like production, than to do it individually for each **classic** pipeline.

---

# WHY are we promoting our v2 CI/CD Azure Pipeline blueprints?

**Self-service automation** is the solution that lets engineers do things by themselves without needing help from someone else who knows the process or has the permissions. We showed our engineers that they can “click” a button, have a cup of coffee, and self-service does the following in less than 30 seconds:  

- Make a new Azure Repo, using a **consistent** name pattern.
- Put an application-type sample solution in the Azure Repo, that uses guardrails, guidelines, and shared components, like **consistent** logging package.
- Put an application type v2 CI/CD blueprint, that creates a **consistent** integration (build) and deployment workflow.
- Run the pipeline, which builds the sample application to validate the environment.

When the engineers come back from their coffee break, they can start working on features, knowing that they have a **consistent**, **standardized**, and **working** environment. **Empowerment!**  

Self-service automation hides the automation, complexity, process, and does the automation for the engineer. It should be as easy as a vending machine. Pick what you want; press a button; and it's done.  

Additional benefit? Security, quality, and operational scanning, monitoring, and troubleshooting are much **easier** and **cost effective**.

>
> ![Alert](/images/back-to-basics-batch-size-alert.png)
>
> Our **application-type v2 CI/CD Blueprints** are designed to support and enhance automation, which requires processes that are stable and consistent and allows them to be quick and simple. This is why we are prioritizing and developing this innovation. 

---

I hope that this post clarifies the **WHY**. If not, let us have a discussion below.


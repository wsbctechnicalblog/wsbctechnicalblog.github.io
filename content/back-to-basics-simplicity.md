Title: Why Automation Needs People to Truly Thrive
Date: 2025-01-13
Category: Posts 
Tags: automation, engineering
Slug: back-to-basics-simplicity
Author: Willy-Peter Schaub
Summary: Cutting Through the Chaos: Why Simplicity is the Ultimate Software Superpower!

**Simplicity** in software engineering is a core principle! It is crucial for productivity, scalability, sustainability, and maintainability. Its super powers include (sorted alphabetically and not a comprehensive list):

- Allows engineers to focus on solving problems and delivering value, rather than managing complex solutions.
- Empowers engineers to work more efficiently and concentrate on important tasks, rather than spending time on repetitive activities.
- Keeps guardrails and governance, such as pull-request guardrails and quality governance, effective without constant churn and required tweaks.
- Reduces the technology and technical debt footprint of your solutions.
- Simpler solutions make it easier to gather feedback and iterate ion innovations.
- Reduces complexity, ensuring that our codebase stays clean and easy to maintain.

Simplicity in software engineering involves removing unnecessary complexity to enable **faster delivery**, **better quality**, and more **satisfied engineers**. It supports continuous delivery, ****empowers** engineers, and makes systems **resilient** to future changes.

---

# VAPOUR-WARE

When an idea emerges, it is assessed with a critical question: **What is the value, and is it needed today?** 

If there is **no clear value**, the idea is discarded without incurring sunk costs. If there is **future potential but no immediate need**, the idea is added to the Azure DevOps backlog under the "Ideas" or "Scrapyard" area paths for future consideration.

Cool ideas can quickly become unused, costly features that complicate maintenance. This clutter hinders governance and delays meaningful improvements for engineers and business stakeholders.

Our goal is to deliver value by focusing on essential engineering processes and products. We prioritize current engineer needs, stakeholder investments, and avoid adding unnecessary complexity.

We focus on **what matters**, not vaporware.

---

# EXAMPLE - v2 Generic Multi-Job Template

### From brilliant idea to blunder:a lesson in over-engineering

Let me share a humbling example of one of my early ideas for our YAML-based pipelines which seemed great but ended up being a major mistake, hindering innovation and wasting resources.

> ![Excitement](../images/back-to-basics-simplicity-1.png) 

In the early days of our [AzureDevOps.Automation.Pipeline.Templates.v2](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2) open-source project, we were excited about creating reusable templates. We compared single-job to multi-job templates, aiming for flexibility and efficiency, as discussed in [Part 6: Pipelines - Gotcha! The generic blueprint-based YAML pipeline simplicity](/yaml-pipelines-part6.html). These have now evolved into generic-steps and generic-jobs in our open-source project.

It all seemed brilliant—until reality set in.

What we had created was **far more complex than necessary**, introducing **hidden maintenance costs** and **slowing down engineers** who just needed a simple, reliable way to run pipelines. The initial excitement gave way to frustration as our generic templates became a **monolith of unnecessary abstraction**, requiring **constant upkeep** without delivering the expected value.

### The allure of parallel jobs: a costly temptation

Our engineers often chose the **generic-jobs template** over the simpler option. The allure of running **parallel jobs** in Azure Pipelines, similar to **multi-threading**, was too strong. More parallel jobs should mean we can complete more tasks, faster.

Well … **yes, in theory**. But at what cost?

> ![Excitement](../images/back-to-basics-simplicity-2.png) 

The result was complex pipelines, starved Azure Agent Pools, and an increasing need for additional hosted parallel jobs—which come at a **cost**. What began as an effort to optimize workflows turned into a significant use of resources, both in terms of engineering capacity and budget.

We are frequently asked to assist with a pipeline based on the generic-jobs template. We often find the complexity challenging and return it to the engineers, deciding that the time investment is substantial. **Switch to generic-steps and enjoy your favorite brew** while you wait a bit longer for your pipeline to complete more economically. It is a matter of minutes, not hours, and the minutes you lose, you gain in hours of troubleshooting and maintenance you never have to worry about.

### Hoping to be wiser

This experience taught us a vital lesson: **Not every “cool idea” is worth pursuing**. The key is to balance **innovation with simplicity** and to avoid creating **vapourware—ideas** that sound impressive but ultimately add more complexity than value. As a result we have removed the generic-jobs template option from our self-service and will gradually retire the template.

---

Do you agree?


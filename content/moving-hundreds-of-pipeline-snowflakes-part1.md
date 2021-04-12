Title: Part 1: Pipelines - Why bother and what are our nightmares and options?
Date: 2020-12-19
Category: Posts
Tags: Azure-Pipelines, DevOps 
Slug: why-pipelines-part1
Author: Willy-Peter Schaub
Summary: Pipelines enable engineering to continuously deliver value, map and improve their processes and workflows, promoting consistency and reliability across the organisation.

In this series we are going to invite you on our journey of grappling with hundreds of inconsistent and often conflicting continuous delivery pipelines, to evolving to unified pipelines, template-driven pipelines, and eventually self-service automation. We will break down our journey into these multiple parts:

- Part 1: Pipelines - Why bother and what are our nightmares and options? (this)
- [Part 2: Pipelines - Introduction, variables and why spaces matter](/yaml-pipelines-part2.html)
- [Part 3: Pipelines - Basic building blocks as templates and sprinkling on telemetry](/yaml-pipelines-part3.html)
- [Part 4: Pipelines - Magic of queue time assembly](/yaml-pipelines-part4.html)
- [Part 5: Pipelines - Blueprints to fuel consistency and enablement](/yaml-pipelines-part5.html)
- [Part 6: Pipelines - Gotcha! The generic blueprint-based YAML pipeline simplicity](/yaml-pipelines-part6.html)
- [Part 7: Pipelines - There is more! Simplicity and enablement, courtesy of the app-type blueprint-based YAML pipelines](/yaml-pipelines-part7.html)

Coming soon:

- Part TBD: Pipelines - From CI to CD and beyond in one pipeline
- Part TBD: Self-service automation - A dream turns into reality

---

# Why Pipelines?

> *"Continuous Delivery Pipeline Value Stream Mapping The Continuous Delivery Pipeline (CDP) represents the workflows, activities, and automation needed to shepherd a new piece of functionality from ideation to an on-demand release of value to the end user."* - © Scaled Agile, Inc.

As eluded to by the quote from Scaled Agile, we are not talking about pipelines to carry oil, but pipelines that help us automate continuous integration and delivery tasks. Examples include the automation of guardrail automations, such as SonarQube, WhiteSource, and Building Code scans and validations.

![CICD Pipeline](/images/moving-hundreds-of-pipeline-snowflakes-part1-1.png)

Pipelines enable engineering to continuously deliver value, map and improve their processes and workflows, promoting consistency and reliability across the organisation.

# Snowflakes

A healthy DevOps mindset promotes the line of autonomy. Above the line the organization defines its vision and governance to ensure alignment with regulatory, legal, and other requirements. Below the line the engineering teams own their process, with full autonomy to plan WHO, WHEN, and HOW they will accomplish their work.

If, however, there is a lack of blueprints, design practices, and governance, each team will design and develop their pipelines slightly differently. 

The outcome are unique **snowflakes** that promote rapid evolution (positive) and a diversity of pipelines that can become hard to maintain, support, and innovate (negative).

![CICD Pipeline](/images/moving-hundreds-of-pipeline-snowflakes-part1-2.jpg)

With hundreds of continuous delivery pipelines the **Sec** and **Ops** in DevSecOps began to buckle detecting and fixing vulnerabilities and other guardrail leaks.

# Emergence of Unified Pipelines

In 2018 we decided to grab the pipelines by their valves to tackle the spread of unique pipeline patterns by defining an **Unified** [Azure Pipeline](https://docs.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines?view=azure-devops#:~:text=%20Does%20Azure%20Pipelines%20work%20with%20my%20language,code%20to%20multiple%20targets.%20Targets%20include...%20More%20) design pattern. The pattern promoted the following principles:

- Automate everything automatable
- Build once

> We encourage engineering teams to create a **release** build artifact, with debug symbols published to our symbol server.

- Continuous integration and delivery
- Continuous streamlining and improvement
- Maintain one build definition

> Instead of a developer and release pipeline, create **one** unified pipeline that locks down the higher environments.

- Maintain one release pipeline definition
- Scan for vulnerabilities early, often, and fail fast
- Streamlined approvals

> By optimising our approvals, we cut down on the complexity and delay, we inherited from previous years, decades, ... 

- Test early, often, and fail fast
- Traceability and observability of releases

> Nobody wants a *"where did this build come from"* treasure hunt when joining a 2AM incident call.

What followed was a mind-numbing and expensive era of aligning all snowflakes to the unified design pattern, using the Azure Pipelines GUI editor to manipulate the pipeline json-based configuration. Even though we are using re-usable [Task Groups](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/task-groups?view=azure-devops#:~:text=In%20Azure%20Pipelines%2C%20you%20can%20version%20your%20own,is%20appended%20to%20the%20task%20group%20version%20number.) and [Variable Groups](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/variable-groups?view=azure-devops&tabs=yaml) we had to invest thousands of error-prone clicks - there has to be a better way!?!

We managed to persue our goals of **aligning** with architecture and security guardrails; **consistency** through design practices, automation, and collaboration; **simplicity** to create maintainable pipelines; and **enabling** and **empowering** our common engineering system.

# Hackathon triggers a course change

A radical hackathon idea in 2019 investigated latest technology trends that promised pipeline-as-code, templates, and other facinating features that promise to enable our ultimate goal of self-service automation. Our hackathon idea was not amongst the winners, but is one of the few ideas that continued to simmer and change the world of our continuous delivery pipelines.

It triggered a pipeline working group, awareness workshops, and even four laptop stickers to highlight unified pipeline, multi-stage, CI+CD, and self-service automation champions.

![CICD Pipeline](/images/moving-hundreds-of-pipeline-snowflakes-part1-3.png)

Welcome YAML based pipelines, which we will introduce in [part 2](yaml-pipelines-part2.html) of this series.

---

> Series Bread Crumbs | Part 1, TOC | [Part 2](/yaml-pipelines-part2.html) | [Part 3](/yaml-pipelines-part3.html) | [Part 4](/yaml-pipelines-part4.html) | [Part 5](/yaml-pipelines-part5.html) | [Part 6](/yaml-pipelines-part6.html) | [Part 7](/yaml-pipelines-part7.html) | [Part 8](/yaml-pipelines-part8.html) |


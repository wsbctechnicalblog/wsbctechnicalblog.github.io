Title: Self-service automation - A dream turns into reality
Date: 2021-06-30
Category: Posts
Tags: Azure Pipelines, DevOps, Pipeline as Code
Slug: yaml-pipelines-part9
Author: Willy-Peter Schaub
Summary: Automate a “hello world in less than 1min”, also referred to as our “walking skeleton”.
Welcome back to another installment of pipeline wizardry. We are changing gears from the nuts and bolts, to the automation we can achieve using the blueprint-based pipelines. Faster your seat belts!

---

# The dream

Our automation working group had a vision to build an engineering process that could generate a “Hello world in less than 1min”, aka walking skeleton, to decimate engineering process lead lines and enable our engineering teams.

> Option 1 - Manual and humanoid driven engineering process
>
> ![Manual](/images/moving-hundreds-of-pipeline-snowflakes-part9-1.png)

Our engineering process is not unique. It starts with an idea. Engineering creates a new repository for the code artifacts, and a continuous integration and deployment pipeline. As engineers require elevated permissions to generate the repo and pipeline artifacts, other engineers and departments get engaged as part of the process to ensure consistency, security, and alignment with guardrails (governance). 

As frustrating as it may sound, it can take **hours to days**, until the engineering team can finally start adding and building their code.

> Option 2 - Automated and humanoid enabled engineering process
>
> ![Manual](/images/moving-hundreds-of-pipeline-snowflakes-part9-2.png)

Our envisaged engineering process is radically different. Engineering visits a self-service portal, captures data to describe what they need, and the **click a button**. The engineering process should be created through automation, the repo should contain an application-type sample, and by the time the engineering team blinks, the pipelines should be running to validate the setup using the sample code. 

Machines (automation) can do repetitive tasks much better and faster than we can, they stick to the instructions to ensure that we do not have to validate consistency and guardrail alignment.

Our dream, as mentioned, is to enable the engineering team within 1 minute. 

---

# Community View

> Option 2 - Automated and humanoid enabled engineering process
>
> ![Manual](/images/moving-hundreds-of-pipeline-snowflakes-part9-3.png)

We polled the twitter and LinkedIn community and realized that we are not alone. An average of **33**% of users tolerate hours and **36**% of users days to get a basic project environment assembled. 

**That is unacceptable!**

---

# Our drop-the-mic demo

We demonstrated the following engineering process using a recipe of Git, Azure DevOps REST API, and a PowerShell automation script, developed and mob-reviewed by our automation working group:

- Query Azure DevOps Project information
- Create an Azure Repo (Git)
- Clone our AzureDevOps.Automation.Pipeline.Templates and the app-type specific AzureDevOps.Automation.Pipeline.Sample.* repository
- Clone the newly created repository
- Add the app-type *-start.yml template to the new repo
- Add the app-type sample code to the new repo
- Push local changes to the Azure Repo
- Create a new pipeline, linked to the *-start.yml template in the new repo
- Run the new pipeline

When we shared a recording of the demo with engineering, there were a few gob-smacked faces when the penny dropped that our "less 1min dream" could evolve into a "less than 20 seconds engineering process".

> Hello world automation demo
>
> ![Demo](/images/moving-hundreds-of-pipeline-snowflakes-part9-4.png)

Here is our automation script we used for the demo.

```
TBD
```

---

# Gob-smacked?

> gob-smacked (excited) yet?
>
> ![Gobsmacked](/images/moving-hundreds-of-pipeline-snowflakes-part9-5.png)

---

# What is next?

We need to expand our library of application-type blueprints and in parallel expand the automation script to support the new app-types. In parallel we need to move the automation script to be run by Azure Pipelines to support queueing, and add a user-friendly service portal to "click the button."

Watch this space for more exiting progress.

---

> Series Bread Crumbs | [Part 1, TOC](/why-pipelines-part1.html) | [Part 2](/yaml-pipelines-part2.html) | [Part 3](/yaml-pipelines-part3.html) | [Part 4](/yaml-pipelines-part4.html) | [Part 5](/yaml-pipelines-part5.html) | [Part 6](/yaml-pipelines-part6.html) | [Part 7](/yaml-pipelines-part7.html) | [Part 8](/yaml-pipelines-part8.html) | Part 9 |


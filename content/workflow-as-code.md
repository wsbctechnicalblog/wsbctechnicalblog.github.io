Title: Workflow-as-code
Date: 2021-03-05
Category: Posts
Tags: Agile, DevOps, infrastructure as code, workflow as code, Continuous Integration (CI), Continuous Delivery (CD)
Slug: workflow-as-code
Author: Alex Bunardzic
Summary: Configuring complex workflows that govern Continuous Integration and Continuous Delivery must only be allowed by making changes to the YAML source files; GUI tools must be prohibited
 
Majority of software applications available on the market today offer self-serve capabilities to end users. Those self-serve capabilities are mostly focused on automating the chores related to various paperwork processes. Browsing product and service catalogs, picking items and ordering them via automated checkout process. In addition to that, there are alternate automated scenarios that enable end users to cancel their actions, repeat them, request refunds, etc.
 
A smaller portion of such typical mainstream software applications are focused on automating the workflow. Oftentimes we see that the business operations workflow is not a simple straight line from start to finish. Depending on the business policy rules, workflows may take a number of twists and turns. Automating such complex rules is no small feat, which is why we're not seeing that many self-serve workflow applications on the market today. Unlike with simple automation of the paperwork representing straightforward business transactions, workflows tend to get more convoluted.
 
## How are self-serve business applications implemented?
 
Experience has shown that the majority of end users prefer to do self-serve tasks by operating a Graphical User Interface (GUI). Such interface often mimics real life paperwork (i.e. replicating paper forms in electronic format etc.)
 
When it comes to offering workflow solutions, it has also been demonstrated that end users prefer to do the self-serve activities via Graphical User Interfaces. The flow of various documents and forms gets represented with artifacts or simulacra resembling real world pipes. Those pipes, when put together in certain configurations, form various pipelines.
 
Many users are by getting familiar with the concept of manipulating pipelines in order to perform the self-serve activities of configuring non-trivial workflows.
 
## Problem statement
 
So far, the self-serve model we've described looks perfectly reasonable and even quite desirable. So where's the problem?
 
While it is perfectly reasonable to hide the formalized complexities of the automation from end users (they are not trained to operate complex systems using rigorous formal reasoning), when it comes to enabling software engineers to operate complex software systems, Graphical User Interface is not a good way to do it.
 
And yet, for some reason we see a lot of platforms drag the GUI mindset back into the inner circles of software engineering teams. And the problem then becomes the fact that software engineers get conditioned to use GUI for configuring complex workflows needed for Continuous Integration (CI) and Continuous Delivery (CD).
 
Why is that a problem? When using GUI, engineers are directly touching the materialized infrastructure. That is a very bad idea. To illustrate, let's imagine a scenario where a software engineer would log in to the live production system that's running the application binary (compiled) code. Imagine that engineer being privileged to go directly to the live binary code, and using some GUI tool, start making changes to the live code in production!
 
That situation will cause panic. Making untested changes to the live code is a surefire recipe for disaster.
 
The only legitimate way software engineering teams could make changes to the production code is if they make changes not to the materialized binary code, but only to the code representation -- the actual source code.
 
Source code by itself cannot perform any operations. It must be compiled and the compiled code must be then built first. Those operations must happen within regulated Continuous Integration and Continuous Delivery workflows. Those workflows consist of a number of strict business policy rules that govern the quality of the proposed code change. If the quality is substandard (i.e. the code does not pass all the tests that are baked into the workflow), the proposed change gets rejected.
 
## Replace GUI with code
 
Workflow, that is represented by the GUI, must be removed and in its place we must put the source code. Typically, when it comes to configuring the integration and delivery workflows, we opt for YAML code.
 
The challenge now is to retrain software engineers from knowing how to use GUIs to configure the workflow rules to mastering YAML needed to accomplish the same self-serve automation.
 
No one should be allowed to touch the materialized computing artifact (such as the implemented workflow engine) with their 'bare hands' (by 'bare hands' we mean direct access to the implemented machinery via a GUI tool).
 
It is therefore urgent to rush and get rid of all GUI tools that enable software engineers to perform self-serve workflow configuration activities. Instead, we must switch wholesale to learning how to use YAML properly.
 
## What are the advantages of workflow-as-code?
 
Just by the virtue of disabling engineers from touching the workflow machinery directly, we ensure that any changes to the workflow get implemented through official channels. When a team decides to make changes to the workflow, they cannot do it directly. They must first create a workflow feature branch, make proposed changes in isolation, test them, then open a Pull Request (PR), proposing these changes get merged to the main trunk. The PR gets reviewed by the stakeholders on the CI/CD workflow, and if approved, they will get merged and then materialized as an implemented workflow.
<br /><br />
 
Title: Why release on demand?
Date: 2024-01-19
Category: Posts 
Tags: azure-devops, engineering, automation
Slug: why-release-on-demand
Author: Willy-Peter Schaub
Summary: Exploring the deployment rings, continuous delivery and deployment, to discuss release on demand. 

Before I get into the main subject of this blog post – why our goal is to release on demand – I want to quickly talk about deployment rings, continuous delivery and deployment, and what they mean. These topics are all connected in the DevOps DNA and backed by Azure DevOps, the foundation of our software development lifecycle (SDLC).

---

# Deployment Rings - managing impact!

The concept of ring-based deployment, initially introduced in Jez Humble's "Continuous Delivery" as canary deployments, strategically minimizes the impact on end users by incrementally and systematically rolling out changes in production. Employing deployment rings allows for a thorough assessment of the impact, often referred to as the "blast radius," achieved through meticulous observation, testing, telemetry analysis, and crucially, user feedback. 

> ![Rings](/images/engineering-practices-why-release-on-demand-1.png)

This approach, used to deploy Azure DevOps, enables the gradual deployment of binary bits, facilitating the concurrent operation of multiple production releases. For more detail, peruse [Deploying new releases: Feature flags or rings?](https://opensource.com/article/18/2/feature-flags-ring-deployment-model).

---

# Continuous Delivery and Deployment - deploying to one or more environments!


In the distant year of 2016, I sought insights from my ALM Ranger colleague to delineate the distinction between continuous delivery and continuous deployment. 

Here is what [Donovan Brown](https://www.linkedin.com/in/darquewarrior/) had to say: "_Continuous Delivery is the ability to use the output from the CI to build and deploy the new known good build to **one or more environments** automatically. There is a subtle difference between Continuous **Delivery** and Continuous **Deployment**. The latter is to a single environment. A small team might only implement Continuous Deployment because each change goes directly to production. Continuous Delivery is moving code through **several** environments, ultimately ending up in production, which may include automated UI, load and performance tests and approvals along the way._"

PS: Donovan is also the author of the infamous definition of DevOps I am still using to this day - [What is DevOps](https://www.donovanbrown.com/post/what-is-devops). Collectively, we acknowledged the prevailing notion that DevOps transcends being a product; it is not something one can simply purchase or install. Yet, this perception took an interesting turn with the advent of Azure DevOps.

---

# Deployment versus Release - giving the business and users a choice!

**Deployment** is the process of moving a build or application from one environment to another. It involves copying files, configuring settings, and setting up the infrastructure necessary for the application to run. In Azure DevOps, deployment usually refers to the tasks involved in taking an artifact and installing it in different environments such as development, testing, and production.  

**Release**, on the other hand, is the process of making a version of your application available to users or customers. It is the end result of the development and testing process and signifies that a particular set of features or changes is ready for production use.

---

# Why Release on Demand?

TBD

---

# References

- [Applying DevOps to a Software Development Project](https://learn.microsoft.com/en-us/archive/msdn-magazine/2016/august/devops-applying-devops-to-a-software-development-project) / August 2016
- [VSTS - The Road to Continuous Delivery with Visual Studio Team Services](https://learn.microsoft.com/en-us/archive/msdn-magazine/2017/connect/vsts-the-road-to-continuous-delivery-with-visual-studio-team-services) / December 2017
- [Deploying new releases: Feature flags or rings?](https://opensource.com/article/18/2/feature-flags-ring-deployment-model) / February, 2018
- [Any Language, Any Platform with Azure DevOps Projects](https://learn.microsoft.com/en-us/archive/msdn-magazine/2018/may/devops-any-language-any-platform-with-azure-devops-projects) / May 2018


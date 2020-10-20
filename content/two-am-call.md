Title: Shift LEFT and RIGHT to take yourself off the humbling 2AM calls.
Date: 2020-10-24 13:13
Category: Posts
Tags: DevOps, DevOps Mindset
Slug: shifft-left-2am-call
Author: Willy-Peter Schaub
Summary: Three DevOps mindset epiphanies reference the infamous 2AM call!

During the **Getting started with a DevOps mindset session** at the CSI Lab in January 2019, we discussed four epiphanies. Three referenced the infamous 2AM call, as shown below.

![Epihanies](/images/two-am-call-1.png)

# What's the 2AM call?

When a user reports an issue, telemetry insights identifies an anomaly, or a circuit breaker detects a potential overload, an incident is generated. On detection of the incident a call is initiated to engineers on call, also referred to as designated response individuals, who jump on the call to identify the root cause, capture vital evidence, work on a mitigation hot fix, document the incident transparently, and work with the feature teams (pods, tribes,...) to ensure that the incident never re-occurs. The reason it is called the 2AM call is that it usually happens when we're entering the REM sleep at 2AM.

> EPIPHANY 2 - The 2AM Call is a great motivation for quality

It is obvious that no one wants to wake up at 2AM. Experiencing the 2AM call once or twice, is typically enough motivation for any of us to look for ways to improve our solution and avoid getting the dreaded call.

> EPIPHANY 3 - Teams that take ownership of features from ideation to deprecation are typically involved in the least 2AM calls.

# Why does SHIFT LEFT + SHIFT RIGHT reduce the 2AM calls?

![Epihanies](/images/two-am-call-2.png)

## SHIFT LEFT

The core idea is to perform tasks such as testing, security scanning, user experience reviews, and code reviews as early as possible in the continuous integration and deployment life cycle as possible. 

![Quick Poll](/images/two-am-call-3.png)

> Snapshot of our quick poll - What is important to automate for a healthy DevOps environment?

Automation is key to the **shift left** practice allowing us to integrate the tasks seamlessly in the engineering system.

![Quick Poll](/images/two-am-call-4.png)

The above snippet is from a pull request validation build that shows that 71,283 unit tests were validated in less than 7 minutes.  Similarly, continuous integration builds can perform credential, security, and other scans, allowing us to validate the quality of a feature early and continuously, identify issues early, and either fix or fail fast before we commit ourselves to a deployment.

## SHIFT RIGHT

Contrary to practices such as testing and security scanning, which we want to perform as early and often as possible, we want to defer the configuration deployments as long as possible - SHIFT configuration RIGHT. Explore how to generate ONE build, deploy to MANY environments, simplify build artifact traceability and remote debug, as needed ... it is possible!

## BUT, WHY DOES IT REDUCE THE 2AM CALL?

PEOPLE are the hardest part of any transformation! Innovating continuously to improve the PROCESS and PRODUCTS (tools) is the easy part. 

> EPIPHANY 3 - We need to ensure that engineers see the value for SHIFT LEFT

If you SHIFT LEFT with testing and security, the engineers, the PEOPLE, will initially push back as the pull request validation builds take longer and associated logs and alert noise increase dramatically.  However, running 70,000 unit tests with every build, as shown above, eventually raises the quality of the solution. It's like a train that takes a while to pick up speed. Once in motion, the momentum will dramatically improve key performance indicators (KPI), such as **lead time for change**, **mean time to recover**, and especially **change failure rate**.

**CAUTION** - KPIs are often not meaningful to all stakeholders. For example, mentioning a 2,604 times **faster mean time to recover** metric is probably viewed with more skepticism than excitement by many business stakeholders.

![Endangered](/images/two-am-call-5.png) 

A reduction in incidents and 2AM calls, however, is an easy one to unpack for everyone - especially for on-call engineers now snoozing next to silent pagers and mobile phones.


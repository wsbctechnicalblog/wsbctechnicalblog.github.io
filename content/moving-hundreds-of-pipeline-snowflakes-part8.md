Title: Part 8: Pipelines - From CI to CD and beyond in one pipeline
Date: 2021-04-13
Category: Posts
Tags: Azure Pipelines, DevOps, Pipeline as Code
Slug: yaml-pipelines-part8
Author: Willy-Peter Schaub
Summary: Continuous Deployment seems important. It deploys new features, bug and hot fixes, which we can release to our delighted customers on demand.

Welcome back to another installment of pipeline wizardry. In [part 7](/yaml-pipelines-part7.html) we wrapped up our application-type continuous integration (CI) pipeline. OK, we have nailed the build, but what about continuous deployment (CD)?

---

# Why do we care about continuous deployment?

In previous posts we covered the world of Continuous Integration (CI), which builds and validates your latest code in your source control repository. With Continuous Delivery (CD) we deploy the artifact from the CI build to one or more environments. 

In the MSDN article, [Applying DevOps to a Software Development Project](https://docs.microsoft.com/en-us/archive/msdn-magazine/2016/august/devops-applying-devops-to-a-software-development-project), I emphasised the subtle difference between Continuous Delivery (CD) and Continuous Deployment (CD): "_The latter is to a single environment. A small team might only implement Continuous Deployment because each change goes directly to production. Continuous Delivery is moving code through several environments, ultimately ending up in production, which may include automated user interface (UI), load and performance tests and approvals along the way._" Note that both have the TLA (two|three lettered acronym) CD ... confusing, right? Oh, how I loathe acronyms q;-(

OK, so Continuous Deployment seems important. It **deploys** new features, bug and hot fixes, which we can **release** to our delighted customers on demand.

> **NOTE** - The use of "continuous" implies that both the continuous integration and continuous deployment engineering processes are fully automated!

After being flabbergasted with the innovation, [simplicity and enablement, courtesy of the app-type blueprint-based YAML pipelines](/yaml-pipelines-part7.html), I expected a world of frustration and pain to embrace the blueprints within the context of Continuous Deployment.

Here is our story.

---

# Tweaks to the Application-type CI Blueprints

TBD

---

# Making sure our Security Engineers are happy

TBD

---

# Mulling over environments and/or service connection approvals

TBD

---

# Are our engineers losing control over their pipeline?

TBD

---

# What is next?

TBD

---

> Series Bread Crumbs | [Part 1, TOC](/why-pipelines-part1.html) | [Part 2](/yaml-pipelines-part2.html) | [Part 3](/yaml-pipelines-part3.html) | [Part 4](/yaml-pipelines-part4.html) | [Part 5](/yaml-pipelines-part5.html) | [Part 6](/yaml-pipelines-part6.html) | [Part 7](/yaml-pipelines-part7.html) | Part 8 |  


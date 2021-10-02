Title: Why I loathe when engineers use TLAs, such as CD vs CD!
Date: 2021-10-01
Category: Posts 
Tags: learning, pipelines, eliminate-waste
Slug: why-i-hate-tlas
Author: Willy-Peter Schaub
Summary: The use of TLAs creates subpar collaboration, unnecessary confusion, and unintended waste.

When last were you sitting in a discussion, lost in a bombardment of TLAs (**t**hree-**l**ettered-**a**cronyms)? In engineering, especially software engineering, we have an abundance of acronyms which is the norm for us, but the kiss of confusion and one of the core reasons collaboration with our non-**IT** stakeholders is so challenging.


>
> **IT** = **I**nformation **T**echnology in the context of this post. It could be mistaken for **i**nternet **t**imes, **i**nternational **t**rade, **i**ncome **t**ax, **i**nitial **t**est, **I** **t**hink, etc.
>

---

# Seek Clarity!

![Confusion](/images/why-i-hate-tlas-1.png)

In our common engineering team, we are spearheading several cool initiatives, such as optimization of meetings (a future topic) and the avoidance of TLAs or FLAs - three, four, and five lettered acronyms. Instead, when writing, we practice the recommended way of first mentioning the full meaning, followed by the acronym, for example Information Technology (IT).

 When collaborating verbally we encourage everyone to "read" the TLA, but "speak" the expanded form. In other words, when we read "IT is fun", we say "Information Technology is fun."

![Happy](/images/why-i-hate-tlas-2.png)

A simple way to change the most complex and confusing conversation, to a **simple** and **easy to understand** collaboration.

---

# So, what is CD versus CD?

Continuous Delivery (CD) is similar, but not the same as Continuous Deployment (CD). Although ```CD == CD```, there is a subtle difference.

![Continuous Delivery](/images/why-i-hate-tlas-3.png)

**Continuous Delivery** deploys the release artifacts to several environment, such as development, system test, staging, and production, or deployment rings. See [Act 3 in Navigating DevOps through Waterfalls](https://www.tactec.ca/ndtw-resources) and [Feature flags or Rings](https://opensource.com/article/18/2/feature-flags-ring-deployment-model) for details.

![Continuous Deployment](/images/why-i-hate-tlas-4.png)

**Continuous Deployment** deploys the release artifacts to a single environment and each change goes directly to production. Using [Hypothesis-driven Development](https://opensource.com/article/19/6/why-hypothesis-driven-development-devops), for example, you can separate the deploy from the release using **Feature Flags**, hiding the changes until it is time to release them for prime time.

Imagine if you are sitting in a production release planning meeting and mistake **CD** for **CD** - welcome 2AM production incident meeting(s) :( Compared to have clarity whether the release is based on Continuous Delivery or Continuous Deployment - enjoy a night of uninterrupted quality sleep :) The choice is yours!

---

# Keep it simple and avoid waste!

In conclusion, having a common and clear language, void of the infamous TLAs, energizes collaboration and avoids waste such as frustration, confusion, overwhelming [loss of space crafts in translation](https://www.simscale.com/blog/2017/12/nasa-mars-climate-orbiter-metric/), or worse [unrecognized waste](https://twitter.com/mcsee1/status/1443597775346839557?s=20).


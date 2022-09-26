Title: Built-in Quality
Date: 2022-09-30
Category: Posts
Tags: azure-devops, eliminate-waste, pipelines, tips
Slug: built-in-quality
Author: Willy-Peter Schaub
Summary: Ensuring that our solutions meet quality guardrails and governance from ideation to deprecation.

Post-deployment analysis, audits and inspection does not improve quality - it is usually too late, resulting in spectacular failures. While we can learn from these failures, they tend to be expensive and reputation busters - remember, first impressions last!

![Crash](/images/built-in-quality-1.png)

Quality must be built-in from the moment a team has an idea until the feature or product is deprecated. Also, it is the responsibility of all stakeholders, such as development, operations, architecture, security, and business. It should therefore come as no surprise that built-in quality is the North Star of our EDO Common Engineering [Center of Enablement](https://wsbctechnicalblog.github.io/ceremony-overview.html).

Let me explore three (3) of many parts of the **built-in quality** puzzle in our common engineering system.

---

# Pull Request

I covered many of the myths of pull requests in [why we use pull requests with our trunk-based branching strategies](https://wsbctechnicalblog.github.io/branching-pull-request.html) and like [Mike Kaufman's](X) definition "_the pull request integration helps you to keep your main branch clean and detect issues before merging and making the code analysis part of the review process_", in his [Accelerate DevOps with GitHub](https://www.amazon.ca/Accelerate-DevOps-GitHub-software-performance/dp/1801813353) book.

The [Azure DevOps Pull Requests](https://sec.ch9.ms/ch9/151a/ba7ad81b-ed67-4dfc-a9fb-4ebf323e151a/CONN17T184_high.mp4) are one piece of our arsenal to be pro- not re-active and help us raise the quality bar through automated validations and a pair of human eyeballs, if and only if required. When we change our [Azure Pipeline blueprints](https://wsbctechnicalblog.github.io/yaml-pipelines-part10.html), for example, stakeholders from common engineering, operations, security, and/or site reliability engineering are looped in if the change impacts their area of responsibility.

> **TIP** - Pull Requests are autonomous stewards of our [Guardrails](TBD) and complement our peer-programming, by creating awareness of our engineering efforts across differing engineering disciplines. Fosters **resilience**!  

---

# Application-type CI/CD Blueprints

One of our great innovations, the [Azure Pipeline blueprints](https://wsbctechnicalblog.github.io/yaml-pipelines-part10.html), deliver **consistency**, **standardization**, foster **collaboration**, all of which contribute to the built-in quality. A neat side effect is that they also enable **self-service automation**, removing mind-numbing and error prone processes - it is a **win**:**win**.

![Template](/images/built-in-quality-5.png)

With the blueprints, made up of a collection of re-usable templates, most of our big rocks of continuous innovation, enablement, and built-in quality are ticked off in our continuous integration (CI) and delivery (CD) pipelines.

> **TIP** - Watch this space. We will open source our blueprints on GitHub soon!

---

# Pathfinders

![Soldier](/images/built-in-quality-3.png)

In the armed forces pathfinders are specialized troops inserted to perform a reconnaissance to gather information, setup and operate drop zones. They share their specialized skills and gather intelligence.

![Engineer](/images/built-in-quality-4.png)

In our world, we insert our engineers to software delivery teams to share their expertise, steward Guardrails, gather information on challenges and how we can improve our common engineering ecosystem to empower all engineers.

By understanding our stakeholders and sharing our learnings with the engineers, we ensure that we continuously improve the built-in quality of both our common engineering system and our products. It is another **win**:**win**!

---

> **HINT**, **HINT** ... I hope that our Quality Assurance engineers will create a follow-on post to explore how we build-in and validate quality through our quality assurance services. 

![Pencil](/images/built-in-quality-2.png)

Watch the space for more in-depth content on **built-in quality** and our engineering **practices**. Our software development practice lead is busy sharpening his blogging pencils q;-) 


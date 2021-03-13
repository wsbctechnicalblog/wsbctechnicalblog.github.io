Title: Wandering down memory lane - feature flags
Date: 2021-03-12
Category: Posts
Tags: Azure-Pipelines, DevOps
Slug: memory-lane-feature-flags
Author: Willy-Peter Schaub
Summary: Use feature flags to fine-tune each release in production.

More memory lane content pulled from my personal blog, before it is deprecated in favour of this technical blog.

--- 

# DevOps vancouver Meetup January 2019

We had a really great turnout and a vibrant meetup hosted by [Andre Kaminski](https://www.meetup.com/DevOps-Vancouver-BC-Canada/members/44231812/), featuring three topics in January 2019:

- Entropy in DevOps Teams: Andrew Rose
- The Virtues of Being T-shaped: Kyle Young
- Progressive Exposure Using Feature Flags: [Willy Schaub](https://wsbctechnicalblog.github.io/pages/authors.html)

> ![Pipeline](/images/memory-lane-feature-flags-3.png)

You can find a copy of my feature flags presentation [HERE](https://1drv.ms/b/s!AoTKFn7kQntwmop6lYMUH2ki07YkpA). Ping me if the link is blocked by your firewall.

---

# Top 6 FAQs from my talk

## What's DevOps and what's the link to the session?

> DevOps, by [Donovan Brown](https://www.donovanbrown.com/post/what-is-devops)
>
> ![Pipeline](/images/memory-lane-feature-flags-5.png)

Link to the [January 2019](https://www.meetup.com/DevOps-Vancouver-BC-Canada/events/257318843/) session and [photos](https://www.meetup.com/DevOps-Vancouver-BC-Canada/photos/29645676/).

## When should I use rings versus feature flags?

I think of a **package** when using the ring-based deployment model to deploy a release and a small **screwdriver** to "tweak" feature flags to fine-tune the release. See [Deploying new releases: Feature flags or rings?](https://opensource.com/article/18/2/feature-flags-ring-deployment-model) for more details.

## How do I manage the technical debt introduced by feature flags?

**KEEP IT SIMPLE!** Define technical governance to clearly define who owns the feature flags, when and how to remove feature flags and the associated technical debt,  and scenarios that are suitable for feature flags. See [What's the cost of feature flags?](https://opensource.com/article/18/7/does-progressive-exposure-really-come-cost) for more details.

## Who owns feature flags?

> ![Pipeline](/images/memory-lane-feature-flags-2.png)

Most feature flags are scoped to a business feature, backed by a business case, and delivering value, which places the ownership of the feature flag switch with the business. Some feature flags are scoped to an operational feature, which places the ownership with operations (Ops).

## What do we mean with "Do not hide non-production ready code behind feature flags"?

Production ready implies hat we have met an agreed quality bar and are confident to release the feature to production. It does not mean feature ready, as we may expose a production ready minimally viable product to perform experiments and A|B testing. Risk of hiding non-production ready code behind feature flags is high - it's easy to flip a switch and expose incomplete,unstable, of security breeches by mistake

## Why the product we introduced at the meetup?

You need to investigate and create your own opinion, but here are a few highlights from our evaluation:

- It's a Software as a Service (**SaaS**)
- **Simple** administration
- Support for **experimentation**
- Feature flag **dependency management**
- Identify **stale flags**
- **Rules** to manage exposure and blast radius
- ... and much more!

## Can you tell me more about circuit breakers?

> ![Pipeline](/images/memory-lane-feature-flags-4.png)

[Hystrix](https://github.com/Netflix/Hystrix/wiki) evolved out of resilience engineering work that the Netflix API team began in 2011. See [A Rough Path](https://aka.ms/bh-ff-sos), by Brian Harry for an example, where circuit breakers could have protected us from an Operational meltdown, caused by simply "flipping a flag".

---

# Two epiphanies

> ![Pipeline](/images/memory-lane-feature-flags-6b.png)
>
> ![Pipeline](/images/memory-lane-feature-flags-7b.png)

---

# Last, but not least, our feature flag manifesto

On our common engineering site, we have a collection of verbal declaration of intentions, motives, or views of the issuer, for processes and products.

Here is a copy of our feature flag manifesto.

> ![Pipeline](/images/memory-lane-feature-flags-1.png)

The worlds of our [pipelines](/why-pipelines-part1.html) and feature flags are likely to collide when we innovate our ability to **release on demand**. See you there!


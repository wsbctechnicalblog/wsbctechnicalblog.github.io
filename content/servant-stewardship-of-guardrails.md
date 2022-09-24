Title: Servant stewardship of guardrails
Date: 2022-09-21
Category: Posts 
Tags: engineering, learning, innovation
Slug: servant-stewardship-of-guardrails
Author: Willy-Peter Schaub
Summary: You can chose between governance, policies, or standards, or collaborate with us through guardrails.

We covered this topic before in [can we enact governance through engineering-friendly manifestos and guardrails?](/governance-manifestos-guardrails.html) ... but recent experiences emphasis the need for a quick refresher. First, let us compare the difference between governance, policies, standards, and what we refer to as guardrails.

Listed from most to least formal:

- **Governance** - "_Is the process of interactions through the laws, norms, power or language of an organized society over a social system (family, tribe, formal or informal organization, a territory or across territories)." - [Wikipedia](https://en.wikipedia.org/wiki/Governance)
- **Policy** - "_Is a deliberate system of guidelines to guide decisions and achieve rational outcomes. A policy is a statement of intent and is implemented as a procedure or protocol. Policies are generally adopted by a governance body within an organization_" - [Wikipedia](https://en.wikipedia.org/wiki/Policy)
- **Technical Standards** - "_An established norm or requirement for a repeatable technical task which is applied to a common and repeated use of rules, conditions, guidelines or characteristics for products or related processes and production methods, and related management systems practices._" - [Wikipedia](https://en.wikipedia.org/wiki/Technical_standard)

If you have work with engineers, especially those with an Agile and healthy DevOps mindset, pushing the boundaries through experimentation and innovation is common. Governance, policies, and standards are frowned upon as they generally **restrict** (opposite of empower) rapid innovation.

---

# What about Guardrails?

Our vision is to **Empower engineering through consistent and standardized processes, practices, and products, within guardrails.** We collaborate with experts from different disciplines in our centers of enablement to identify, introduce, and support processes, engineering principles, and products and create **guardrails**. We do not enforce but recommend guardrails to ensure that we reduce the risk of non-compliance and last-minute "stop the bus" decisions.

> A **guardrail** is a less formal version of technical standards which are **recommended**, not **enforced**. The basic content describes the **WHAT** the guardrail is about, **WHY** is it important, and **HOW** to apply it.

When I cover guardrails, I ask engineers to visualize a bridge.

![Bridge](../images/servant-stewardship-of-guardrails-1.png)

We are your servant stewards of guardrails to support you to cross the bridge safely and swiftly. If, however, you decide to climb on or climb over the guardrails, you are on your own. In other words, do not call us  if someone's hair is on fire, you are sitting in an infamous 2AM-call, or a failed security review stops you from deploying a mission critical release.

---

# WS.Infrastructure?!?

I recently received an email with a request to migrate a repository named ``WS.Infrastructure`` to another Azure DevOps project. Here is what went through my mind as IO read the email:

- _Hmmm, what does the TLA (two lettered acronym) **WS** mean? **W**illy **S**chaub, **W**indows **S**ervice, **W**ater **S**tation, ...?_
- _Let me peek into the repository and look at the **Infrastructure** stuff ... but there is no typical infrastructure stuff. A platter of long-lived feature branches with NuGet packages focused on infrastructure._

Had the creator of the repository reviewed our naming guidelines and branching strategy guardrails, we would have a deployable master branch and a user-friendly repository name. For example ``CrossCutting.NuGet.Infrastructure`` would be a lot more intuitive.

This is a very simple example of not operating within our guardrails, which **WASTES** a lot of valuable engineering time on guess-work, creates an **ERROR-PRONE** bridge crossing, and does not empower engineers who have to takeover the artifacts when the creators move on.


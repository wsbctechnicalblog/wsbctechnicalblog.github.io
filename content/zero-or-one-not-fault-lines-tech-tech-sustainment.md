Title: Zero or One, not Fault Lines - Technology, Technical, versus Sustainment Battle
Date: 2026-03-23
Category: Posts 
Tags: engineering, journal
Slug: zero-or-one-not-fault-lines-tech-tech-sustainment
Author: Willy-Peter Schaub
Summary: Stop Funding the Wrong Work: The Sustainment vs EOL Upgrade Headache

Over the last few weeks, I have been analysing the effort to upgrade solutions are coming through as excessive. This is not a finger-pointing exercise. It is a clarity exercise. If we cannot trust the data, we cannot defend the strategy, protect the funding, or credibly report progress.

> ![Zero or One, not Fault Lines Journal](../images/zero-or-one-not-fault-lines-introduction-to-the-journal-0.png) 

Here is the problem in plain language: we keep blending three different types of work into one bucket, and then we wonder why the EOL programmes look “expensive” and “slow”. In practice, that confusion creates real harm, because it hides where the effort is truly going, it drains End-Of-Life) funding, and it gives leadership a distorted view of whether we are reducing risk or simply paying interest on backlog.

The core distinction (the one rule that matters)

>
> If the work makes the solution upgrade-ready, it is **sustainment**.
> If the work performs the upgrade, it is **EOL remediation**.
>

That boundary is already reflected in how we talk about readiness, guardrails, and “doing the right thing, at the right time, all the time”. Our pre-flight mindset is explicit: paved roads and standards, supported frameworks, vulnerability baselines, measurable quality outcomes, and automation that prevents surprises. Those are readiness activities. They are not the upgrade itself.

## Sustainment (including technical debt remediation)

Sustainment is the work that keeps a solution operable, supportable, and ready for change. It is stabilisation and incremental improvement. It is where you pay down the friction that makes upgrades painful.

Typical sustainment activities:

- Refactoring brittle or over-complex code
- Improving unit and regression coverage, including automation
- Removing deprecated libraries
- Architecture clean-up
- Preparing a solution so that an upgrade can be executed safely

This aligns with our baseline expectation: quality gates, vulnerability reduction, and test discipline before we do anything high-impact.

## Technical debt (what it is, not how you fund it)

Technical debt is not a project. It is the nature of the work: internal code, architecture, automation, and quality gaps that increase risk, slow delivery, and raise long-term cost. Technical debt exists regardless of whether a vendor EOL date is approaching.

In other words: “technical debt” is often what sustainment is addressing. It is not automatically “EOL work” simply because an EOL programme exists. This is exactly why we emphasise test coverage, quality baselines, and guardrails. Building safety and repeatability so that upgrades become predictable, not heroic. [Discussion...on Session | Meeting]

## Technology debt / EOL remediation (execution only)

EOL remediation is the act of moving from an unsupported or soon-to-be unsupported platform to a supported one.

Typical EOL execution activities:

- Executing the framework upgrade (for example, a .NET version upgrade)
- Resolving compatibility issues directly caused by the version change
- Validating the upgraded solution in supported environments

Caution! When the solution is not upgrade-ready, the work to make it ready is **sustainment**. Treating readiness work as EOL execution inflates EOL cost, hides sustainment demand, and undermines our ability to demonstrate risk reduction through disciplined delivery.

A simple geek picture (because we need fewer debates and more consistency)

```
┌──────────────────────────┐
│        Sustainment       │
│  (Readiness and quality) │
│                          │
│ • Refactoring            │
│ • Test automation        │
│ • Architecture cleanup   │
│ • Upgrade preparation    │
└──────────────┬───────────┘
               │ Upgrade-ready solution
               ▼
┌──────────────────────────┐
│  Technology EOL Upgrade  │
│  (Execution only)        │
│                          │
│ • Version upgrade        │
│ • Compatibility fixes    │
│ • Supported runtime      │
└──────────────────────────┘
```

This is not academic. It is how we protect funding, measure progress, and avoid repeating the “late discovery, late scramble, high cost” pattern we have all experienced.

Why I am stressing about this (and why you should care)

- **Cost transparency** - When sustainment is logged as EOL execution, we create the illusion that EOL work is inefficient. In reality, we are often doing two jobs at once: first making the solution safe to touch, then upgrading it. The cost is real, but the classification is wrong, and wrong classification leads to wrong decisions. 
- **Funding protection** - EOL programmes exist to remove exposure from unsupported platforms. If we use that funding to bankroll general readiness work, we will eventually run out of runway before we reduce the risk we promised to reduce. That is how programmes get labelled as “failing”, when the true failure was categorisation discipline.
- **Engineering behaviour** - We get what we measure. If timesheets reward “charging it somewhere that has budget”, we will train the organisation to do exactly that. If we reinforce the correct distinction, we create better behaviours: earlier testing, stronger guardrails, fewer surprises, and faster execution when it is time to upgrade. That is stakeholder experience and risk reduction in action.

Share the rule widely:

>
> If it makes the upgrade possible, it is **sustainment**. If it performs the upgrade, it is EOL **technology debt**.
>

Over to the you: **do you have the same headache?**
I want to hear from you, because I suspect this is not unique to us.

If you have solved this well, please share your approach with the community. If you are still wrestling with it, share the pain points. Either way, we will all benefit from consistent practices that improve cost transparency, protect EOL funding, and accurately report progress, while strengthening stakeholder experience through predictable delivery. 

A closing thought (because it is worth repeating)

>
> Discipline is not bureaucracy. Discipline is how we buy speed and confidence.
> When we classify work correctly, we get better decisions, better funding outcomes, and better engineering behaviour.
>

Enjoy your favourite brew. I will savour my hot chocolate and raise it to disciplined engineering, sound judgement, and value‑driven progress.


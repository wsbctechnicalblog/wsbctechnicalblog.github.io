Title: Embracing Legacy, AI, and the Road to EOL Modernisation
Date: 2026-02-02
Category: Posts 
Tags: engineering, automation, ai
Slug: engineering-practices-legacy-and-eol-solutions
Author: Willy-Peter Schaub
Summary: Why the Future of Engineering Isn’t Only Greenfield, and How Artificial Intelligence Is Transforming Our Upgrade Strategy

The rain was absolutely relentless on Saturday morning. I found myself staring across the Fraser River, hiding from the downpour, and letting my thoughts drift toward our modernisation and re‑engineering of a large collection of legacy and end‑of‑life solutions. It is easy to romanticise the world of greenfield development. New frameworks. Clean architectures. Untouched code. However, the systems that intrigue me most are those quietly lingering in sustainment mode, faithfully running our ecosystems, often overlooked in favour of newer and shinier pursuits.

>
> ![Fraser River](../images/engineering-practices-legacy-and-eol-solutions-1.png)
>

These systems carry history, decisions, technical debt, innovation scars, and, most importantly, context. Modernising them is not only a technical challenge. It is an engineering adventure.

# The Surge of New Insights from Proof‑of‑Concepts

Over recent weeks, several engineers have been running proof‑of‑concepts with a wide range of technologies, including Quality Assurance tooling, Angular, .NET, AI platforms, and the new Microsoft Visual Studio Moderniser. Their findings have already produced invaluable insights. Keep an eye on this space—there will be a flood of posts from the engineering teams sharing lessons, patterns, cautions, and wins.

As part of my own evaluations, I witnessed remarkable progress in products and processes, especially where Artificial Intelligence (AI) is amplifying our engineering capability. For the first time in years, we can seriously entertain the idea of migrating certain legacy solutions into the modern world without radical re‑engineering or complete rewrites.

AI‑enabled tools now:

- migrate and refactor code faster than we can,
- map dependencies we did not know existed,
- support human‑in‑the‑loop decision making,
- pause and request engineering insight when they reach ambiguity,
- and significantly reduce risk and cost compared to traditional manual uplift strategies.

From a stakeholder experience, risk reduction, and cost avoidance standpoint, this shift is profound.

# Two Sides of the AI Coin

Naturally, the engineering community is not unanimous.

I have heard:

- “The tools are too slow.”
- “I do not trust their recommendations.”
- “They generate more code than we can possibly validate without asking the tools to validate themselves.”

These concerns are not only valid. They are vital. Blind reliance is not engineering. Skepticism is healthy. Trust must be earned through method, evidence, rigorous validation, and shared experience.

# AI as an Architectural Advisor

AI is not just supporting code migration. It is now capable of evaluating and comparing front‑end technologies, architectural approaches, and long‑term strategic options. We can feed it experience, repositories, history, and market signals. It synthesises insights in minutes that previously required weeks and sometimes months of engineering debate.

For example, when I asked O365 Copilot for a technology‑alignment recommendation, it responded within seconds with the following:

- **Full‑stack .NET:** Blazor Web App (mix of Server and WASM per feature) with ASP.NET Core for minimal cross‑stack friction and better governance.
- **Enterprise Single‑Page Applications:** Angular for strong structure and security at scale, or React with Next.js for ecosystem and hiring advantages.
- **Server‑rendered portals:** Razor Pages for excellent CRUD performance, SEO needs, and minimal client‑side complexity.

The clarity of this analysis, generated based on context extracted from our ecosystem, in seconds, cannot be ignored.

# A New Chapter of Collaboration

I would like to close with three questions for our technical and innovative engineering community, with the hope that they will spark meaningful dialogue:

1. How do you validate and trust the outcomes of Artificial Intelligence (AI) within your engineering ecosystem?
2. What is your long‑term strategy for your aging legacy solutions? Do you migrate, refactor, re‑engineer, rewrite, keep them as they are, or simply let them fade away?
3. Do you have success stories or open‑source examples of Blazor‑based front‑end solutions that could inspire and guide .NET-focused sustainment teams?

>
> Looking forward to your learnings and insights, to fuel discussions and perhaps contribute to a future [DevOps Vancouver meetup](https://www.meetup.com/devops-vancouver-bc-canada) topic.
>


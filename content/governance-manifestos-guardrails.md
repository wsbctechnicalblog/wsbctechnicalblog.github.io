Title: Can we enact governance through engineering friendly manifestos and guardrails?
Date: 2021-05-18
Category: Posts
Tags: Engineering Practices
Slug: governance-manifestos-guardrails
Author: Willy-Peter Schaub
Summary: The best way to create an engineering revolt is to enforce governance with the big stick.

One of many challenges of pursuing a healthy DevOps mindset is finding harmony between the need for organizational governance and autonomous engineering teams. Merriam-Webster defines **Governance** as “_the act or process of governing or overseeing the control and direction of something_”. It comes in many forms such as architecture, infrastructure, development, security, operations, bureaucracy, and legislation. A healthy portion of governance raises quality and trust, but tends to stifle autonomy and innovation. Rules are rules!

> ![Governance](/images/moving-hundreds-of-pipeline-snowflakes-part3-1.png)

On the other hand, if we have minimal or no governance, we can experience an engineering revolt which introduces a variety of engineering snowflakes, duplication of effort, and technical debt that grows like a vicious virus. For example, when we ask engineering why we have hundred of applications and thousands of CI/CD pipelines, we get a shrug of shoulders and everyone moves on. Everyone but the operations and site reliability engineering teams, because they inherit an endless variety of technical solutions, code rot, complexity, and declining return on investments. So, which way should we pivot the scale?

> ![Revolt](/images/moving-hundreds-of-pipeline-snowflakes-part3-2.png)

You guessed it, we must nurture a balance between governance and autonomy. It fuels innovation, risk taking, and passion. Easier said than done!

> ![YingYang](/images/moving-hundreds-of-pipeline-snowflakes-part3-3.png)

---

# Quest for balance

![Hat](/images/governance-manifestos-guardrails-4.png)

When I put on my engineering hat, the word **governance** triggers tension and at times even an urge to revolt.

For that reason we prefer using engineering friendlier language such as **manifestos** and **guardrails**.

- **Manifesto** – “_a written statement declaring publicly the intentions, motives, or views of its issuer_” (Merriam-Webster), such as [Manifesto for Agile Software Development](https://agilemanifesto.org/) and [DevOps Core Values](https://www.tactec.ca/devops-core-values/).

> ![Agile](/images/governance-manifestos-guardrails-1.png)

> ![DevOps](/images/governance-manifestos-guardrails-2.png)

- **Guardrails** – “_a railing guarding usually against danger_” (Merriam-Webster), such as the sides of a bridge, 200m above a raging George, or naming guidance.

For our common engineering system we have collaborated with security and operations to define a library of guardrails, such as:

> ![DevOps](/images/governance-manifestos-guardrails-3.png)

Here is an extract from our naming guidelines guardrail, with recommendations (not policies, rules, or standards) for Active Directory group names. 

```markdown
Active Directory Group Names

Review AD AAD Security Groups for a list of organizational, project, and team-level groups.

- Guidelines
  - AzureDevOps_<Department>_<Project>[_<Team>]_<Role> format.
  - Avoid spaces. Use underscore (_) instead.
  - Prefix with 3rdParty for artifacts containing third-party resources.
- Examples
  - AzureDevOps_IT_CeS_ProjectAdministrators
  - AzureDevOps_Training_AgilePlanning_ReleaseApprovers
```

So now that we have autonomous engineering teams and are all using ~~politically~~ engineering correct language, we should all be focused on continuously delivering value and delighting our end-users. No?

---

# Manifestos and guardrails are wolves in sheep skins

TBD

---

# Why not embrace Manifesto and Guardrail Mobbing?

What is mobbing? TBD

Enacting governance through engineering friendly manifestos and guardrails! TBD

What do YOU think?
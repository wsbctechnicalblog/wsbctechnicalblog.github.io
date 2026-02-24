Title: Mastering the Art of Prompting: Pre-.NET10 Upgrade Analysis
Date: 2026-02-24
Category: Posts 
Tags: ai, learning
Slug: ai-fundamentals-prompts-pre-dotnet-10-upgrade-analysis
Author: Andreas Mertens
Summary: How We Use GitHub Copilot to Validate Application Health Ahead of a .NET Upgrade

Upgrading a core technology stack is never just a technical exercise. It is a stakeholder experience challenge, a risk management exercise, and a cost avoidance opportunity. Before committing to a .NET upgrade, we need a clear, evidence‑based view of the health of our applications and the effort required to move forward with confidence.

In this post, I will offer a practical peek into how we analyse application health using GitHub Copilot as an assistive capability, not a shortcut. We focus on understanding code quality, dependency risk, architectural debt, and upgrade readiness across our portfolio. GitHub Copilot helps us accelerate discovery, highlight patterns, and surface potential issues earlier, allowing our teams to spend more time on judgement, decision‑making, and remediation.

> ![Analysis Image](../images/ai-fundamentals-prompts-pre-dotnet-10-upgrade-analysis-1.png) 

# Getting Started

1. Open the solution in Visual Studio.
2. In Copilot Chat, select Claude Sonnet 4.5, and make sure you are starting a new chat session.
3. Copy the contents of the Pre-DotNet10 Upgrade Analysis.md, see below, file into the chat session and execute it.

Copilot should now generate an analysis markdown file, detailing changes that should be performed prior to the .Net 10 upgrade.

It isn't necessary to clean up everything, but I would recommend fixing any of the reported Critical and High severity issues that are reported:

1. Ask Copilot to fix the Critical issues that were listed in the analysis
2. If Copilot asks any questions, answer as appropriate.
3. Once the issues are addressed by Copilot, always make sure to review the changes, make sure they make sense.
4. Also do a full rebuild, verifying that the changes are not causing any build issues.
5. If the changes are generating a lot of warnings, you can also ask Copilot to correct these as well.
6. Finally, you may find that Copilot has skipped some of the issues, usually due to the time / effort required to correct. You may ask Copilot to address these anyways, one at a time. For any that you wish to defer, ask Copilot if not fixing these issues might have an impact on the .Net 10 Upgrade. If it does, you may still need to deal with this manually or with Copilot assistance.
7. Repeat steps 1-6 for the High severity issues.

>
> Remember to always commit after a set of changes, in case you need to roll back any changes that are not working.
>

Once you have reached this point, you can perform the .Net 10 Upgrade:

1. Right-click the solution in the Solution Explorer of Visual Studio, select Modernize
2. In the Copilot chat window, select Upgrade .Net Framework
3. Confirm that you want to upgrade to .Net 10. Copilot will also be able to create a new branch for the upgrade changes, but you can instruct it to stay with your current branch if you prefer.
4. Copilot will do three stages:

```
    - Analysis
    - Create Tasks plan
    - Execute the plan
```

5. Tell Copilot to proceed with the Analysis, which will generate an analysis.md document. Once it has completed the analysis, review the document. You can ask Copilot to make changes if necessary. Commit the changes when you are ready to proceed.
6. Tell Copilot to proceed with creating the tasks/plan document. As with the analysis, review the document, ask Copilot to change as necessary and commit the changes.
7. Tell Copilot to execute the plan. At this point Copilot will work through the list of tasks in the plan document. It will periodically run scripts or builds, in which case it will ask for permission to proceed. You can decide whether to grant it permission just once, per the chat session, or always. The upgrade will take some time to process, but eventually Copilot will announce when it is done.
8. Be sure to review the changes and perform any validation on the application. You may also find that the changes have created more warnings - if so, you can ask Copilot to correct this or work them on your own if desired.

As always, ensure that you commit all changes.

# Pre-DotNet10 Upgrade Analysis.md

```
**IMPORTANT: Do *not* perform any upgrade, target‑framework change, migration, or modernization step that modifies the project to .NET 10 or any other TFM.  

Do *not* create an upgrade plan.  
Do *not* apply the Upgrade Assistant pipeline.  

This session is strictly for a *pre‑upgrade cleanup and assessment only*.**

I want you to operate in **analysis‑only mode** and perform **pre‑upgrade cleanup for .NET 8 → .NET 10**, without performing the upgrade itself.

**Your tasks:**

1. **Analyze the entire solution** (projects, code, config, Dockerfiles, dependencies).
2. **Identify cleanup tasks ONLY**, such as:
    - Removal of deprecated patterns
    - Replacement suggestions for obsolete APIs
    - Outdated or problematic packages
    - Unsafe code patterns for .NET 10
    - Breaking‑change hotspots that need remediation
    - Project file hygiene (Nullable, ImplicitUsings, no preview features, redundant properties)
3. **Do NOT change the TargetFramework**, SDK version, or apply migration steps.
4. **Do NOT suggest preview SDKs or preview versions**.
5. **Do NOT generate or apply an upgrade plan.**

**Output Requirements — Produce a Markdown report:**

Generate a single Markdown document with:

**A) Ranked and grouped list of cleanup items**

- Group by **Severity**: Critical / High / Medium / Low
- Group by **Category**: Dependencies, APIs, Auth, Containers, Build/Config, Code Quality
- For each item include:
    - Description of the issue
    - Why it matters for .NET 10
    - Suggested fix (with code examples if applicable)
    - Rough **time estimate** in developer‑hours
    - Severity ranking
    - File(s) and line(s) where applicable

**B) A “changes to be made” section**

Use diff‑style blocks or bullet points describing exactly what should be changed, but **do not apply them yourself**.

**C) A “recommended pre‑upgrade plan” section**

This is *not* an upgrade plan — instead describe:

- The order in which cleanup should be performed
- Any blockers that must be removed before upgrade
- Validation steps (tests, build, etc.)

**Restrictions:**

- This is **strictly a pre‑upgrade cleanup assessment**.
- Do **not** perform or trigger the upgrade itself.
- Do **not** rewrite project files except to describe what needs to be changed.
- Do **not** modify csproj or package versions automatically.
- Do **not** propose TFM changes — only cleanup tasks.

When complete, output the full Markdown file.
```

# Final Thought

In the end, GitHub Copilot proves its value not as an autopilot, but as a productivity wingman that sharpens thinking, accelerates insight, and keeps quality firmly in focus. It helps teams move faster without cutting corners, turning complex codebases into navigable terrain and early signals into informed decisions. Like a trusted astromech in the hangar, it supports health checks, highlights risk before it becomes impact, and enables confident preparation for what comes next. Used well, GitHub Copilot becomes a stargate to quality solutions: **reducing risk**, **avoiding unnecessary cost**, and **improving the stakeholder** experience by ensuring that speed and discipline advance together, not in opposition.


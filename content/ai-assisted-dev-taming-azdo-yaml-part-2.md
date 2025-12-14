Title: AI Assisted Development – Taming Azure Pipeline YAML (Part2)
Date: 2025-12-19
Category: Posts 
Tags: ai, engineering
Slug: ai-assisted-dev-taming-azdo-yaml-part-2
Author: Willy-Peter Schaub
Summary: Artificial Intelligence post the thunderous impact of an asteroid colliding with our moon … 

OK, in [AI Assisted Development – Taming Azure Pipeline YAML](/ai-assisted-dev-taming-azdo-yaml.html) I was flabbergasted by the supporting role that GitHub Copilot could plan. If you have not read that post, do so now - I will wait.

---

# Part 2 - Where the real fun starts

In the past, I had to manually copy and paste every single innovation from one blueprint—specifically the __101__ blueprint—into all the others. It was a tedious, mind-numbing process that felt like a guaranteed way to introduce errors. Honestly, it was the kind of work that makes you question your life choices.

Then I thought, why not let GitHub Copilot handle this for me? So I gave it a shot. Here is what I asked: 

```
- Please review the git history.
- Review the changes made to the templates in the __101__ folder.
- Focus on the logic around azure DevOps agent pools and vmimage.
- Apply the same changes to the universal-artifact folder.
- Validate all changes.
- Explain all the changes you have made.
- Suggest improvements for future consideration.
Thank you.
```

And here is what Copilot came back with:

> ![github copilot](../images/> ![bots](../images/ai-assisted-dev-taming-azdo-yaml-part-2-1.png) 

And here is more of the copilot's journal:

```
Git history review

- Key commits impacting `__101__` pool logic:
  - 4e11edb: Renamed security review stage parameters; removed redundant env name 
    vars.
  - 3de0d4e, 8506828: Introduced coalesce for pool/image params; added dynamic 
    agent pool and vmImage configuration.
  - 5a26779: Updated blueprint version to 2.2.0 in start templates.

- Pattern established in `__101__`:
  - CI stage: conditional pool—include vmImage only when set; otherwise omit for 
    self-hosted.
  - CD stage: same conditional pattern; namePool and nameVM provided from config 
    via control.yml.

Validation of __101__ (post your patches)

- azure-pipeline-__101__-ci.yml: Correct conditional pool using 
  ${{ if ne(parameters.vmImage, '') }}; self-hosted omits vmImage.
- azure-pipeline-__101__-cd-stage.yml: Correct conditional pool with 
  namePool/nameVM.
- azure-pipeline-__101__-control.yml: Passes jobPool/vmImage to CI and 
  namePool/nameVM to each CD stage via coalesce(...). Security/QA/PreProd 
  automation use the same approach.
- azure-pipeline-__101__-config.yml: Security review and automation variables 
  now correctly named (securityReviewStagePool, securityReviewStageVmImage, 
  etc.). Looks consistent.

Applied changes to universal-artifact

- Updated CI pipeline to match __101__ conditional pool pattern:
- File: azure-pipeline-universal-artifact-ci.yml
- Changes:
  - Replaced hardcoded pool with:
     - ${{ if ne(parameters.vmImage, '') }} → pool: 
       name=${{ parameters.jobPool }}, vmImage=${{ parameters.vmImage }}
     - ${{ else }} → pool: name=${{ parameters.jobPool }}
  - Outcome: Supports both hosted and self-hosted agents.

- Updated CD stage template to include pool name and conditional vmImage:
  - File: azure-pipeline-universal-artifact-cd-stage.yml
Changes:
  - Replaced pool: vmImage: ${{parameters.config.nameVM}} with conditional 
    block:
    - If nameVM not empty: set both namePool and nameVM.
    - Else: set only namePool.
  - Outcome: Matches __101__ pattern and correctly handles self-hosted 
    agents.

- Wired control template to pass pool/image values consistently:
  - File: azure-pipeline-universal-artifact-control.yml
  - Changes:
    - CI parameters: added jobPool and vmImage using 
      coalesce(variables.ciStagePool, 'Azure Pipelines') and 
      coalesce(variables.ciStageVmImage, 'ubuntu-latest').
    - CD stage parameters: added namePool and wrapped nameVM in 
      coalesce(...) for all stages (development, systemTest, staging, 
      production, CanadaCentral, CanadaEast).
    - Embedded stages (securityReview, securityAutomation, qaAutomation, 
      preProdAutomation): added namePool with coalesce(...) and retained 
      conditional vmImage.
    - Outcome: All stages now accept pool name and optional vmImage, 
      consistent with __101__.

Validation

- Static validation: No YAML or linter errors detected in updated 
  universal-artifact files.
  - Checked: azure-pipeline-universal-artifact-ci.yml, 
    azure-pipeline-universal-artifact-cd-stage.yml, 
    azure-pipeline-universal-artifact-control.yml.
- Behavioral expectation:
  - Hosted agents: vmImage non-empty → pool includes vmImage.
  - Self-hosted agents: set corresponding *StageVmImage to '' in 
    config or omit → pool omits vmImage.

Improvements for future consideration

- Centralize pool defaults:
  - Add top-level defaults per blueprint (e.g., defaultPool, 
    defaultVmImage) and let stage-specific variables override—reduces 
    duplication.
- Validation template:
  - Create a small reusable template to verify that when a custom 
    pool is used, vmImage is empty; and for hosted pools, vmImage is 
    set—fail fast with clear messages.
- Consistent OS images:
  - Align default images across blueprints (ubuntu-latest vs 
    windows-latest) based on toolchain needs; document per blueprint.
- Parameterize pool/image in start templates:
  - Expose ciStagePool/ciStageVmImage in *-start.yml to encourage 
    explicit selection at pipeline creation.

What I changed

- Added conditional pool logic to universal-artifact CI and CD stage
  templates, mirroring __101__.
- Ensured control wiring passes both namePool and nameVM per stage 
  using coalesce(...).
- Added jobPool/vmImage to universal-artifact CI invocation to support 
  dynamic agent selection.
- Enforced that embedded automation stages also receive namePool and 
  nameVM.

Optional next steps

- Do you want me to update azure-pipeline-universal-artifact-config.yml 
  to include *StagePool variables (like developmentStagePool etc.) and 
  align with the new control wiring? I can add those with sensible 
  defaults and a brief comment explaining hosted vs self-hosted 
  configuration.
```

After confirming with a resounding YES, here is the rest of the copilot's journal:

```
Acknowledged. Plan: Review git changes in __101__, apply the same 
pool/vmImage logic to universal-artifact, validate, then explain 
changes and suggest improvements.

Progress: Reviewed __101__ git history and templates, replicated the 
conditional pool logic across universal-artifact, and validated YAML. 
Next, I’ll summarize what changed and future improvements.

Summary of git history review for __101__

- Key changes:
  - Introduced dynamic pool/image via coalesce(...) and conditional 
    pool blocks (commits 3de0d4e, 8506828).
  - Cleaned up security review parameter names and redundancy (4e11edb).
  - Updated start templates to blueprint version 2.2.0 (5a26779).
- Pattern confirmed:
  - CI uses ${{ if ne(parameters.vmImage, '') }} to include vmImage; 
    self-hosted agents omit vmImage.
  - CD stage uses ${{ if ne(parameters.config.nameVM, '') }} to 
    include vmImage with namePool; else only namePool.

Changes applied to universal-artifact

- Updated CI template to support dynamic pool/image with conditional 
  logic:
  - File: azure-pipeline-universal-artifact-ci.yml
  - Changes:
    - Replaced hardcoded pool with conditional blocks:
      - If parameters.vmImage not empty: pool: 
        name=${{ parameters.jobPool }}, 
        vmImage=${{ parameters.vmImage }}
      - Else: pool: name=${{ parameters.jobPool }}
    - Mirrors the __101__ CI pattern to support hosted and 
      self-hosted agents.
- Updated CD stage template to include namePool and conditional 
  vmImage:
  - File: azure-pipeline-universal-artifact-cd-stage.yml
  - Changes:
    - Replaced pool: vmImage: ${{parameters.config.nameVM}} with:
      - If nameVM not empty: pool: 
        name=${{parameters.config.namePool}}, 
        vmImage=${{parameters.config.nameVM}}
      - Else: pool: name=${{parameters.config.namePool}}
  - Aligns with __101__ CD stage behavior for self-hosted support.
- Wired control to pass pool/image to CI and all CD stages:
  - File: azure-pipeline-universal-artifact-control.yml
  - Changes:
    - CI invocation: added jobPool and vmImage using 
      coalesce(variables.ciStagePool, 'Azure Pipelines') and 
      coalesce(variables.ciStageVmImage, 'ubuntu-latest').
    - For each deployment stage (DV, SY, ST, PR, Canada 
      Central/East): added namePool via 
      coalesce(variables.*StagePool, 'Azure Pipelines') and 
      wrapped nameVM with coalesce(..., 'ubuntu-latest').
    - Embedded stages (Security Review, Security Automation, 
      QA Automation, PreProd Automation): added namePool with 
      coalesce(...) and retained conditional vmImage. This 
      ensures consistent agent configuration across all stages.
- Added missing configuration variables to match the new wiring:
  - File: azure-pipeline-universal-artifact-config.yml
  - Changes:
    - Added CI variables: ciStagePool, ciStageVmImage.
    - Added stage pool variables for all environments: 
      developmentStagePool, systemTestStagePool, 
      stagingStagePool, productionStagePool, 
      productionCanadaCentralStagePool, 
      productionCanadaEastStagePool.
    - Added security review and automation pools/images: 
      securityReviewStagePool, securityReviewStageVmImage, 
      securityAutomationStagePool, securityAutomationStageVmImage, 
      qaAutomationStagePool, qaAutomationStageVmImage, 
      preProdAutomationStagePool, preProdAutomationStageVmImage.
    - Defaults set to 'Azure Pipelines' and 'ubuntu-latest' to 
      mirror __101__ and allow easy override. For self-hosted, 
      set the corresponding *StageVmImage to ''.

Validation

- Static checks: No YAML errors reported in updated files:
  - azure-pipeline-universal-artifact-ci.yml
  - azure-pipeline-universal-artifact-cd-stage.yml
  - azure-pipeline-universal-artifact-control.yml
  - azure-pipeline-universal-artifact-config.yml
- Behavioral expectation:
  - Hosted agents: pool name + image used.
  - Self-hosted agents: pool name only; vmImage omitted when the 
    config value is set to empty.

Suggestions for future improvements

- Defaults centralization:
  - Define top-level defaultPool and defaultVmImage per blueprint 
    and reference them with coalesce(...) to reduce duplication 
    and ease global changes.
- Automated validation:
  - Add a validation step/template that asserts: if namePool is a 
    custom self-hosted pool, nameVM must be empty; for hosted 
    pools, nameVM must be set—fail fast with clear messaging.
- Consistent OS defaults:
  - Standardize on ubuntu-latest unless Windows agents are 
    required; document rationale per blueprint.
- Start templates:
  - Expose CI pool/image in *-start.yml to make agent selection 
    explicit at creation time.
```

# I am truly impressed!

Not only did my binary sidekick make all the changes, but it also double-checked everything and nailed it perfectly. Every single update was spot-on. I did not have to babysit the process or fix anything afterward. That is impressive.

This is a perfect example of how you can unlock immediate value with GitHub Copilot—no need to dive into Agentic AI or get lost in the whole “Vibe Coding” rabbit hole just yet. Start small, start smart, and let the tools do the heavy lifting.

Step by step, and suddenly you are working smarter, not harder.


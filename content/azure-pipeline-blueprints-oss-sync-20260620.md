Title: OSS SYNC 20260620 - Self Hosted Flexibility Production Guard Rails
Date: 2026-06-20
Category: Posts 
Tags: azure-devops, pipelines, engineering
Slug: azure-pipeline-blueprints-oss-sync-20260620
Author: Willy-Peter Schaub
Summary: Stage-level pool control, backward-compatible configuration, and stronger production deployment protection across the v2 blueprints.

With Pull request [#38](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/pull/38) merged, we are pleased to share the latest update to our Azure DevOps Pipeline Blueprints. Version 2.2.0 strengthens two areas that matter in practice: deployment flexibility and production safety.

This release introduces support for both Microsoft-hosted and self-hosted agents across the blueprint stages, while also tightening protection around production deployments. The result is a more adaptable blueprint set that helps teams work within their operational constraints without weakening delivery guard-rails.

# Why this matters

This update improves the day-to-day usability of the blueprints for teams that need to run workloads on specific agent pools, while reducing the risk of misconfigured production deployments.
In short, this release helps us:

- support more hosting models without cloning or forking pipeline logic
- keep configuration explicit and easier to reason about
- preserve backward compatibility for existing consumers
- reduce the possibility of an unintended production release caused by an incorrect environment name

# What changed

##Self-hosted agent pool support across all stages

All major pipeline stages now support self-hosted agents by conditionally omitting vmImage when the value is blank.

A compile-time guard using ${{ if ne(..., '') }} selects the correct pool structure, which means the same blueprint can now work cleanly with both 
Microsoft-hosted and self-hosted agent pools.

This applies across the key stages, including:

- Continuous Integration
- Continuous Delivery
- Security
- Quality Assurance
- Pre-production

Outcome: teams can redirect execution to a self-hosted pool without rewriting stage logic.

## Explicit pool variable per stage

Each stage configuration now has its own explicit *StagePool variable declared alongside the existing *StageVmImage variable in the relevant *-config.yml file.
Examples include:

- ciStagePool
- developmentStagePool

This gives teams a single and predictable place to control where a stage runs.

Outcome: configuration becomes more transparent, more maintainable, and easier to override without hidden behaviour.

## Variable rename with backward compatibility

The variable ciVmImage has been renamed to ciStageVmImage for consistency with the broader stage-based model.

To avoid breaking existing pipelines, the control template now uses:

```yaml
coalesce(variables.ciStageVmImage, variables.ciVmImage, 'windows-latest')Show more lines
```

This means existing consumers can continue to function without immediate configuration changes.

Outcome: we improve naming consistency without forcing disruptive migration work.

## Production stage environment-name guard

We have added an additional production safety check across all three production stages:

- Production
- Canada Central
- Canada East

This applies to the following Continuous Delivery blueprint families:

- azure-function
- nuget-package
- webapp

These production stages now also require:

```yaml
endsWith(config.envName, '-production-pr')
```

This ensures that a misconfigured environment name does not accidentally satisfy the production deployment path.

Outcome: stronger production guard-rails and reduced risk from configuration drift or naming mistakes.

## @CeBlueprints reference fix

The __101__ blueprint had a missing @CeBlueprints repository suffix in the Canada East production stage template reference.
That has now been corrected.

Outcome: improved consistency and reduced risk of reference resolution issues in the affected production path.

## Example configuration pattern

Below is a simplified example of the new stage configuration approach:

```yaml
- name: ciStagePool
  value: 'Azure Pipelines'
- name: ciStageVmImage
  value: 'windows-latest'
```

This keeps the pool and image explicit, stage-scoped, and easy to redirect when needed.

## Example control logic pattern

Below is the core idea behind the new conditional pool handling:

```yaml
${{ if ne(parameters.config.nameVM, '') }}:
  pool:
    name: ${{ parameters.config.namePool }}
    vmImage: ${{ parameters.config.nameVM }}
${{ else }}:
  pool:
    name: ${{ parameters.config.namePool }}
```

If a virtual machine image is provided, the stage uses it.

If it is blank, the blueprint emits only the pool name, which is the correct behaviour for self-hosted agents.

## Example backward compatibility pattern

To preserve compatibility with existing consumers, the control template now resolves the Continuous Integration image using coalesce:

```yaml
${{ coalesce(variables.ciStageVmImage, variables.ciVmImage, 'windows-latest') }}
```

This gives us a clean migration path while maintaining operational continuity.

## Why this release is important

This is a practical maturity release.

It does not merely add features. It makes the blueprints easier to adopt in real enterprise environments, where teams often need:

- self-hosted agent routing
- explicit and localised stage control
- consistent naming
- safer production release conditions

That combination improves stakeholder experience, reduces operational risk, and avoids the cost of custom pipeline divergence.

## Final thoughts

This release continues the v2 blueprint journey towards consistency, resilience, and safer delivery by default.

Flexible execution matters. So do strong production guard-rails.

Version 2.2.0 gives us both.

What else can, should, or must we strengthen as part of the Azure DevOps Pipeline Blueprints?


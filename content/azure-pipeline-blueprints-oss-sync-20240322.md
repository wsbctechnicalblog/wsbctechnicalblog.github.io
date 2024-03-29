Title: Azure DevOps Pipeline Blueprints - Open Source Software Sync 20240322
Date: 2024-04-01
Category: Posts
Tags: azure-devops, pipelines, engineering
Slug: azure-pipeline-blueprints-oss-sync-20240322
Author: Willy-Peter Schaub
Summary: Second update to complete the **101** simplification.

This open-source update is minor, but aligns our NuGet-Package blueprint with the recent [Azure DevOps Pipeline Blueprints - Open Source Software Sync 20240318](https://wsbctechnicalblog.github.io/azure-pipeline-yaml-refactor-parameter-objects.html) simplifications. Now all blueprints are consistent!

---

>
> [Click here to view the associated Pull Request](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/pull/27)
>

Changes:

- **blueprints/nuget-package/azure-pipeline-nuget-package-cd-stage.yml** - eplace the configuration variables with the ```config``` object, which encapsulates an array of data structures.. 
- **blueprints/nuget-package/azure-pipeline-nuget-package-cd.yml** - 
Replace the conditionals using ```text``` stage names with ```boolean``` stage validations for a simpler and less error-prone approach.
- **blueprints/nuget-package/azure-pipeline-nuget-package-config.yml** - remove the stage names designated as ```text``` and replace them with ```boolean``` values.
- **blueprints/nuget-package/azure-pipeline-nuget-package-control.yml** - instead of passing individual configuration variables, create an array of config ```objects``` and pass it instead. 
- **blueprints/nuget-package/azure-pipeline-nuget-package-start.yml** - change ```suppressCD``` from false to true to facilitate self-service automation, allowing the injection of a placeholder config template qhich would break the continuous delivery (CD).

---

What else can/should/must we consider as part of our blueprints? Thoughts?

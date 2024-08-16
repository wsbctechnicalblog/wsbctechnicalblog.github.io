Title: Azure DevOps Pipeline Blueprints - Open Source Software Sync 20240816
Date: 2024-08-19
Category: Posts
Tags: azure-devops, pipelines, engineering
Slug: azure-pipeline-blueprints-oss-sync-20240816
Author: Willy-Peter Schaub
Summary: Improving the configuration file user experience.

We have been silent for a while because we have been busy with operations, technology debt reduction, and self-service automation. We will share more on that later. In this update, we have tackled an issue that has bothered us for months, and more importantly causing some concern among our engineers using the v2 CI/CD blueprints.

# LOOKING BACK

We stored all our configuration templates in a separate repository called **\*.Configuration.v2**, protected by branch policies and monitored by our common engineering and security teams. This caused annoying delays when the team needed to change configurations and get reviews that added little value.

# LOOKING FORWARD

We moved the **\*-config.yml** from the **\*.Configuration.v2** repository to the same one where the team's application code and pipeline are tracked. The **\*-control.yml** line referencing the file changed from:

```
variables:
- ${{ if ne(parameters.suppressCD, true) }}:
  - template: /deploy/${{ lower(parameters.portfolioName) }}/nuget-package-config.yml@CeConfiguration
```

To:

```
variables:
- ${{ if ne(parameters.suppressCD, true) }}:
  - template: /deploy/${{ lower(parameters.portfolioName) }}.${{ lower(parameters.productName) }}-config.yml@self
```

>
> Note the **@self** which highlights that we refer to the repository where the original pipeline was found.
>

We also removed the following line from all **\*-start.yml** templates:

```
  - repository: CeConfiguration
    type:       git
    name:       '__TODO_INSERT_AZURE_DEVOPS_NAME_HERE__/AzureDevOps.Automation.Pipeline.Configuration.v2'
```

The only exception is the NuGet v2 CI/CD blueprint, where the **\*-start.yml** template remains unchanged and allows loading the centralized configuration file from **\*.Configuration.v2** or from the same repository as the team's code and pipeline.

```
- ${{ if and( eq(parameters.suppressCD, false), eq(parameters.useDefaultConfig, true) ) }}:
  - template: /deploy/default.config/nuget-package-config.yml@CeConfiguration

- ${{ if and( eq(parameters.suppressCD, false), eq(parameters.useDefaultConfig, false), eq(parameters.usePortfolioConfig, true) ) }}:
  - template: /deploy/${{ lower(parameters.portfolioName) }}/nuget-package-config.yml@CeConfiguration

- ${{ if and( eq(parameters.suppressCD, false), eq(parameters.useDefaultConfig, false), eq(parameters.usePortfolioConfig, false) ) }}:
  - template: /deploy/${{ lower(parameters.portfolioName) }}.${{ lower(parameters.productName) }}-config.yml@self
```

# OUTCOME

Now, the pipeline and its configuration templates are version controlled and managed by the same team that owns the code, making the process simpler and more efficient.

---

>
> [Click here to view the associated Pull Request](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/pull/29)
>

Changes:

- All **blueprints/wepapp/azure-pipeline-\*-control\*.yml** templates have been updated.
- All **blueprints/wepapp/azure-pipeline-\*-start\*.yml** templates have been updated.

---

What else can/should/must we consider as part of our blueprints? Thoughts?

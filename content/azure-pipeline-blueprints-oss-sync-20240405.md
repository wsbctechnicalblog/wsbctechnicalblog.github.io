Title: Azure DevOps Pipeline Blueprints - Open Source Software Sync 20240405
Date: 2024-04-10
Category: Posts
Tags: azure-devops, pipelines, engineering
Slug: azure-pipeline-blueprints-oss-sync-202403405
Author: Willy-Peter Schaub
Summary: Adding a new blueprint - webapp.

This open-source update adds the new **webapp** blueprint to our collection of templates and blueprints. It can be used to build and deploy any web-based .Net application to be deployed as an Azure App Service.

---

>
> [Click here to view the associated Pull Request](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/pull/28)
>

Changes:

- New web-app blueprint, which we use for web **apps**, web **apis**, with **Razor** or **Blazor**.
- **blueprints/wepapp/azure-pipeline-webapp-cd-stage.yml** - new
- **blueprints/webapp/azure-pipeline-webapp-cd.yml** - new.
- **blueprints/webapp/azure-pipeline-webapp-ci.yml** - new.
- **blueprints/webapp/azure-pipeline-webapp-config.yml** - new.
- **blueprints/webapp/azure-pipeline-webapp-control.yml** - new. 
- **blueprints/webapp/azure-pipeline-webapp-start.yml** - new.

---

What else can/should/must we consider as part of our blueprints? Thoughts?

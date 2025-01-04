Title: Azure DevOps Pipeline Blueprints - Open Source Software Sync 20250105
Date: 2025-01-10
Category: Posts
Tags: azure-devops, pipelines, engineering
Slug: azure-pipeline-blueprints-oss-sync-2025-01-05
Author: Willy-Peter Schaub
Summary: Refresh the toolbox and templates with 2024 enhancements.

We have focused on improving our v2 CI/CD app blueprints and the associated v2 toolbox.

# TOOLBOX

@@We have implemented validations in our building-code.yml template, which now ensures that unit tests are present, have been run, and will eventually validate that all tests have passed. As part of these changes, we decided to:

-	@@ 


```
@@
```

# WHY?

@@This change aims to avoid repeatedly triggering the building code with every commit within a pull request when using the pipeline as a validation build due to the lengthy runtime of the building code.

Changes:

> ![Toolbox](../images/azure-pipeline-blueprints-oss-sync-2025-01-05-01.png)

>
> ![Alert](../images/alert-tiny.png)
>
> The Robot files do not adhere to our lower-case-kebab naming guidelines. We will publish a bug-fix update shortly.
> 

---

# TEMPLATES

@@We have implemented validations in our building-code.yml template, which now ensures that unit tests are present, have been run, and will eventually validate that all tests have passed. As part of these changes, we decided to:

-	@@AILog gone
- @@modeElite=true
- @@Unit Tests 
- @@Update Task versions - next update we will use built-in yaml syntax
- @@Version info - pipe-info


```
@@
```

# WHY?

@@This change aims to avoid repeatedly triggering the building code with every commit within a pull request when using the pipeline as a validation build due to the lengthy runtime of the building code.

Changes:

> ![Templates](../images/azure-pipeline-blueprints-oss-sync-2025-01-05-02.png)

---

What else can/should/must we consider as part of our blueprints? Thoughts?

Title: How to suppress selected logic when running PR validation pipelines
Date: 2021-10-04
Category: Posts
Tags: pipelines, tips, x-as-code
Slug: suppress-pipeline-as-code-for-pr
Author: Willy-Peter Schaub
Summary: Solving the pipeline-as-code "chicken or the egg" challenge by suppressing selected logic 

With our app-type CI/CD pipeline blueprints we are consolidating the continuous integration (CI) and continuous delivery (CD) pipelines into one pipeline. When you peruse [Part 10: Pipelines - Meet our second generation app-type blueprints](/yaml-pipelines-part10.html) you will get an overview of our new pipelines which are **powerful** ... with a twist.


---

# The Twist
By consolidating both the continuous integration and delivery logic, we made the pipelines unsuitable to be used as validation pipelines in our Pull Request policies. Why? 

Assume you are creating a pull request to apply a hotfix to a release branch. When the pull request triggers your pipeline, it must wait until the pipeline is complete - which means we must build and deploy to all environments, including production, before the validation pipeline completes. Obviously a "chicken or the egg" and **not** a desired solution.


---

# The Fix

We therefore applied a minor fix (or feature) to our blueprints.

```
# --------------------------------------------------------------------------
# DEPLOYMENT
# 2021.10.04 WS Suppress CD on "merge" so that we can use PR validation builds
# --------------------------------------------------------------------------
- ${{ if and(ne(parameters.suppressCD, true), ne(parameters.customCDTemplate, 'blueprint'), ne(lower(variables['Build.SourceBranchName']), 'merge')) }}:
  - template: /Operations/Custom/${{parameters.customCDTemplate}}.yml
    parameters:
      cdParameter: ${{parameters.customCDParameter}}
```

The ```ne(lower(variables['Build.SourceBranchName']), 'merge')``` part of the code suppresses the conditional logic if the pipeline run originates from a Pull Request merge validation build.

At this stage we suppress all post-build logic to keep it **simple** but can shift the conditional logic by a few lines to allow the deployment to the **development** stage, while suppressing others.

**Simple**, but powerful!


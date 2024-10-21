Title: Azure DevOps Pipeline Blueprints - Open Source Software Sync 20241019
Date: 2024-10-19
Category: Posts
Tags: azure-devops, pipelines, engineering
Slug: azure-pipeline-blueprints-oss-sync-20241019
Author: Willy-Peter Schaub
Summary: Refactor the building code calls.

We have focused on developing new v2 CI/CD app blueprints and enhancing our continuous integration flow.

# MINOR CHANGE

We have implemented validations in our building-code.yml template, which now ensures that unit tests are present, have been run, and will eventually validate that all tests have passed. As part of these changes, we decided to:

-	Remove the ```buildingCodeMode: 'Validate'  # Validate | Enforce``` parameter since it was not utilized, and the modeElite parameter can determine whether to issue a warning or fail the validations.
-	Clean up the conditionals to ensure the building-code.yml template is always executed outside of a pull request and not executed within a pull request unless the forceCheck parameter is set to true. 

Here is the new building-code calling conditionals:

```
# By default we do NOT run the building code if we are within the context of a pull request
- ${{ if and(eq( lower(parameters.bootstrapMode), 'runbuildingcodeonly' ), and(eq(lower(variables['Build.SourceBranchName']), 'merge'), eq( parameters.forceCheck, false))) }}:
  - script:      echo Building Code Validations are suppressed by default to optimize pull request builds.  Set parameters.forceCheck = true to force the building code to run in the pull request.
    displayName: Bootstrap Building Code Validation Suppression Alert

# User can force the building code to run within the context of a pull request
- ${{ if and(eq( lower(parameters.bootstrapMode), 'runbuildingcodeonly' ), and(eq(lower(variables['Build.SourceBranchName']), 'merge'), eq( parameters.forceCheck, true))) }}:
  - template:    building-code/building-code.yml@CeBlueprints
    parameters:
      applicationType:        ${{parameters.applicationType}}
      portfolioName:          ${{parameters.portfolioName}}
      productName:            ${{parameters.productName}}
      applicationBlueprint:   ${{parameters.applicationBlueprint}}
      verbose:                ${{parameters.verbose}}
      modeElite:              ${{parameters.modeElite}}
      modeAILog:              ${{parameters.modeAILog}}

# If we are not within the context of a pull request (brach <> merge) then we run the building code
- ${{ if and(eq( lower(parameters.bootstrapMode), 'runbuildingcodeonly' ), ne(lower(variables['Build.SourceBranchName']), 'merge')) }}:
  - template:    building-code/building-code.yml@CeBlueprints
    parameters:
      applicationType:        ${{parameters.applicationType}}
      portfolioName:          ${{parameters.portfolioName}}
      productName:            ${{parameters.productName}}
      applicationBlueprint:   ${{parameters.applicationBlueprint}}
      verbose:                ${{parameters.verbose}}
      modeElite:              ${{parameters.modeElite}}
      modeAILog:              ${{parameters.modeAILog}}
```

# WHY?

This change aims to avoid repeatedly triggering the building code with every commit within a pull request when using the pipeline as a validation build due to the lengthy runtime of the building code.

You have the option to modify or reverse this process if desired.

---

>
> [Click here to view the associated Pull Request](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/pull/30)
>

Changes:

- All **templates/boot-strap.yml** template has been updated.

---

What else can/should/must we consider as part of our blueprints? Thoughts?

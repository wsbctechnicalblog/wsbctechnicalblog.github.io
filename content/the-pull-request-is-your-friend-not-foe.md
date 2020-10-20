Title: Pull Request is your friend not foe!
Date: 2020-10-19 13:13
Category: Posts
Tags: AzDO, Azure Repos, Git
Slug: pull-requests-friend
Author: Willy-Peter Schaub
Summary: There is a debate around the value of pull requests (PR), fueled by unfortunate misunderstandings.

_"The primary reason we use PRs is to encourage quality in the commits that are made to our code repositories"_ - [GitHub Pull request Etiguette](https://gist.github.com/mikepea/863f63d6e37281e329f8)

# Start simple

Let us start with a simple branching strategy, with one "always" deployable target branch (master/main/trynk), and a short-lived feature branch, as shown below.

![Feature Branch](/images/Pull-Request-is-your-friend-not-foe-1.jpg)

1. Create a short-lived feature branch.
2. Work on new work or a bug fix.
3. Merge (commit) changes to the target branch.
4. Continuous Integration (CI) build is triggered.

![Caution](/images/Pull-Request-is-your-friend-not-foe-2.png)

Simple, but potentially dangerous. As the CI build is triggered after changes have been committed to the target branch, we could have a broken build and an undeployable branch. To make matters worse, anyone creating a new feature branch from an undeployable branch has just inherited a lot of unproductive pain!

# Embrace the four-eyes principle

![Four-Eyes Principle](/images/Pull-Request-is-your-friend-not-foe-3.jpg)

The four-eyes principle requires that any change is validated by at least four eyes, in other words, by at least two people. With [Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/user-guide/what-is-azure-devops?view=azure-devops) we can define [Branch Policies](https://docs.microsoft.com/en-us/azure/devops/repos/git/branch-policies-overview?view=azure-devops) to protect target branches, such as requiring:

- Minimum number of reviewers (required and optional)
- Linked work items (adds the context and traceability)
- Resolved comments (all discussions and recommendations actioned)
- Limited merge types
- Successful build (which includes security scans, tests, etc.)
- Thumbs up from other services

> We can require some or all of the above policies.

# Welcome Pull Request

> Pull Request is a change validation workflow, not a feature of the version control service.

![Welcome](/images/Pull-Request-is-your-friend-not-foe-4.png)

When we define one or more branch policies, we enforce them on [Pull Requests](https://docs.microsoft.com/en-us/azure/devops/repos/git/pull-requests?view=azure-devops), making it impossible for anyone to commit changes to our target branch without passing pre-defined validations.

> By excluding minimum number of reviewers and setting our pull request to auto-complete, we could commit our changes without any human intervention if and only if we pass all other validations. But, that is a topic for another day.

Let us walk through the same branching strategy, as above, and observe how the Pull Request enables (optional) collaboration and required validations.

![Pull Request Workflow](/images/Pull-Request-is-your-friend-not-foe-5.jpg)

1. Create a short-lived feature branch.
2. Work on new work or a bug fix.
3. Create a **DRAFT** pull request, which enables collaboration, work item linking, and manual build validation policies.
4. When we are ready to have our pull request reviewed and completed, we can **PUBLISH** our draft pull request.
5. Pre-defined optional and required reviewers are assigned and notified, policies are evaluated, and voting is enabled. The validation builds are triggered and perform a pre-merge validation - if the build(s) fail, the Pull Request cannot be completed.
6. When all policies are met, the Pull Request can be completed.
7. Associated changes are merged to the target branch.
8. Which, as before, triggers the continuous integration (CI) build.

We do not have to create a DRAFT Pull Request. Instead, we can combine steps 3 and 4 above.

> Recommendation 1 - Create one build definition and re-use it for both the validation and the CI build. Consistent and simple!

> Recommendation 2 - Run security scans, such as SonarQube and WhiteSource, Tests, and other quality validations in either the validation or CI build. We chose to run all validations when the common build is triggered as a validation build as we need the results to review the changes effectively. See YAML sample below.

The advantages of Pull Requests are evident:
- Collaboration is enabled fostering sharing of experience, learning, and recording of discussions.
- Guardrail are validated and enforced
- Automation of validations, which could (or not) include humanoid involvement

# YAML Sample
Last, but not least, here is the above mentioned extract from one of our YAML pipelines. The conditional code ensures that custom validations are injected into our build only if it was triggered as a validation build in a Pull Request.

```
# VALIDATIONS
- ${{ if  eq(variables['Build.SourceBranchName'], 'merge') }}:    
  - template: DSO/InjectValidations.yml
```

Thoughts?

<br />
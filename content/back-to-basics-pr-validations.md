Title: Back to Basics: Pull-Request (PR) Validations
Date: 2024-02-12
Category: Posts 
Tags: azure-devops, engineering
Slug: back-to-basics-pr-validations
Author: Willy-Peter Schaub
Summary: Why run a validation build in your pull-request?

[Azure DevOps](https://azure.microsoft.com/en-us/products/devops/) provides powerful [Azure Repos](https://azure.microsoft.com/en-us/products/devops/repos/), which in turn support feature-rich pull requests, which allow us to perform supervised changes, reviews, and code merges. Again we covered pull requests in previous blog posts, such as [Why we use pull requests with our trunk-based branching strategies](https://wsbctechnicalblog.github.io/branching-pull-request.html), [Pull Request empowered by engineering practices](https://wsbctechnicalblog.github.io/pull-request-empowered-by-engineering-practices.html), and [https://wsbctechnicalblog.github.io/pull-requests-friend.html](https://wsbctechnicalblog.github.io/pull-requests-friend.htm), which allows us to be laser focused on "why bother with a validation build?"

# WHY do we enforce branch policies?

Azure DevOps makes sure that our engineering process follows the technical governance with consistent policies. 

> ![PR Types](/images/back-to-basics-pr-validations-1.png)

The illustration depicts three of many possible pull request workflows. In the first one, we make a feature branch, change the code, and commit the changes directly or through a pull request, without any supervision. The second one adds a **human code** review, which can be used for verification, peer reviews, knowledge sharing, and collaboration. Although this reduces the chance of a failure after the merge, we depend on the review to be careful, not just a “click.” The third flow adds a **verification** step, where we can include **automated validations** defined as branch policies, such as minimum number of reviewers, security and other scan results, and linking the code changes to one or more work items. 

Branch policies set at the Azure repos root and tightened at the repo level are applied in the pull-request validations and improve quality and alignment with guardrails, policies, and/or governance.

For example, we always require these as a minimum:

- Case Sensitivity to prevent case-sensitivity conflicts.
- Reserved Names to prevent forbidden file and folder names.
- Maximum path length to prevent paths that may exceed Windows or Linux path lengths.
- Minimum number of reviewers. (2)
- Requestor can approve. (No)
- Reset code reviewer votes when there are recent changes. (Yes)
- Check for linked work items. (Yes)
- Check for comment resolution. (Yes)

And we suggest:

- Build validation

See [Branch policies and pull requests](https://learn.microsoft.com/en-us/azure/devops/repos/git/about-pull-requests?view=azure-devops#branch-policies-and-pull-requests) for more details on branch policies.

# WHY do we recommend a validation build?

Simple ...

> ![Add BUild Validation](/images/back-to-basics-pr-validations-2.png)

By adding a verification build, as shown, we can ensure that all the criteria have been met, and that the changes are buildable. We have more confidence that the continuous integration build will not break unexpectedly after the merge.

# WHY v2 CI/CD Blueprints complement PR validations

The v2 CI/CD blueprints have many features and innovations, which you should explore. As explained in [Our road to OSS Blueprints - Suppress CD when pipeline runs within Pull Request](https://wsbctechnicalblog.github.io/yaml-pipelines-part11.html), the blueprints can detect when they run in a pull request (as a validation build) and only do the CI part and skip the CD part. This lets teams use the **same pipeline** for both the build validation and the continuous integration and delivery. **Simple!**

---

Thoughts? Questions? Start a discussion below.


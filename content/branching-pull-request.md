Title: Why we use pull requests with our trunk-based branching strategies
Date: 2022-04-01
Category: Posts 
Tags: engineering, version-control
Slug: branching-pull-request
Author: Willy-Peter Schaub
Summary: Busting a few process myths around branching strategies and pull-requests

If you want to ignite a debate in a pub, casually start chatting about politics. In a [virtual] room of software engineers, gently mention branching strategies and pull requests. In both scenarios you can sit back and enjoy the vibrant chain reaction of experiences, opinions, and myths. In this brief article I will share our experience, our [standardization](/consistency-standardization.html) of branching strategies, our use of [pull requests](/pull-requests-friend.html) and bust a few myths along the way.

---

# Branching Strategies

There are many, such as [trunk-based](https://trunkbaseddevelopment.com/), [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow), [GitHubFlow](https://githubflow.github.io/), and derivations as documented by the former [Microsoft ALM/DevOps Rangers](https://vsardata.blob.core.windows.net/projects/TFS%20Version%20Control%20Part%201%20-%20Branching%20Strategies.pdf) and [Microsoft Docs](https://docs.microsoft.com/en-us/azure/devops/repos/git/git-branching-guidance?view=azure-devops).

We have been experimenting with GitFlow and Trunk-based branching strategies and are supporting both as part of our common engineering ecosystem and associated guardrails (aka governance). Based on a push for consistency and standardization we are recommending the [trunk-based](https://trunkbaseddevelopment.com/) branching strategy, with release branches, as used by the Azure DevOps product team.

WHY?

- It is simple.
- It has been adopted by our engineering teams.
- It fits well with our [app-type blueprint](/yaml-pipelines-part10.html) initiative.

![TIP](../images/branching-pull-request-1.png) 
I am NOT saying that is the best strategy but based on experimentation it fits our **people**, **process**, and **products**.

> MYTH 1 - One branching strategy is better than another!
>
> _There is no silver bullet! Avoid the debates and invest time to experiment with a few of the common branching strategies, to determine the best fit for your PEOPLE, PROCESS, and PRODUCTS._ 

See [trunk-based release from branch](https://trunkbaseddevelopment.com/branch-for-release/) for the variant that we are using, based on learning from the [Microsoft Azure DevOps](https://medius.studios.ms/Embed/Video/THR2017?sid=THR2017) team. It is a strategy that works well for the 1-2 pizza sized teams, as well as product teams with hundreds to thousands of engineers.

> MYTH 2 - Trunk-based branching strategy is suited only for small and experienced teams!
>
> _The [Microsoft Azure DevOps](https://medius.studios.ms/Embed/Video/THR2017?sid=THR2017) and [Microsoft Office](https://devblogs.microsoft.com/devops/improving-azure-devops-cherry-picking/) are two very large teams that demonstrate the trunk-based branching strategy scales from small and rapid experimentation and innovation teams, to large product-based teams._

The takeaway for you is that the answer to "_what branching strategy is ideal for you?_" is "_it depends on the outcome of your experiments!_"

---

# Pull Requests

Which brings us to pull requests (PRs), which enable us to change, review, and merge code. You can add policies to your PRs to enable code quality in key branches using policies, validation builds, code-quality and security scans. I trust you all want to protect key branches such as trunk/master/main, which should always be stable and deployable.

> MYTH 3 - Pull-requests slow down your continuous integration value stream!
>
> _A pull request takes as long as you and your process allow it to sit in a corner to gather dust. We encourage our engineers to track the lead and cycle times of pull requests using the [Pull Request Completion Report](https://marketplace.visualstudio.com/items?itemName=OneLuckiDev.prApprovalReport&targetId=dc216ba3-25e9-46a8-823a-fb77a81f2a9f) and to **collaborate** with their peers to ensure that pull requests do not go stale._

Make sure you have a working agreement for pull requests, because **you** decide how long the average lead and cycle times are for your pull requests. In our case:

- **Code-quality**, **security-scans**, and **validation build(s)** take minutes at the worst. 
- Code review for **learning** can be done in parallel without affecting the lead and cycle times, so no delays.
- **Branch policy checks**, such as must be linked to work items and all comments must be addressed, is instantaneous.
- If feature branches are **short-lived**, **collaboration** is healthy, and code changes constrained to agreed feature(s), the code reviews are also in the territory of minutes.

So, we are talking about minutes to add immense value and ensure that the changes we commit to trunk/master/main branch are quality and will not break. If your average pull request lead time is in the hours to days, you need to map your pull request value stream and find the **WASTE**.

> MYTH 4 - Pull-requests are manual gates
>
> _In theory a pull request (in Azure DevOps) could be all automated, based on policies, validation builds, and other validations. It is as manual and/or automated as YOU decide to configure your policies and guardrails._

If you wonder whether it is a sin to use pull requests with trunk-based branching strategies, read [continuous code review](https://trunkbaseddevelopment.com/continuous-review/) and watch the [trunk-based development](https://medius.studios.ms/Embed/Video/THR2017?sid=THR2017) video. 

> MYTH 5 - Trunk-based branching strategy and use of pull requests is a NO-NO!
>
> _"In theory" the trunk-based strategy is based on short-lived feature branches and merging changes directly with the trunk/master/main branch. Using a pull request as a pre-merge validation does not change the strategy, it merely injects a final countdown checkpoint before you commit your code changes to the "always deployable" trunk/master|main branch. It is an opportunity to move your scale of **trust**, not a matter of changing the branching strategy._

---

For branching strategies and the use of pull requests there is no silver bullet. Once you realize that consistency and standardization trumps personal preference and variations, you can pick the branching strategy and the use of pull-requests (or not) that empowers your engineers and organization. 


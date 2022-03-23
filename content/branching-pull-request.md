Title: Why we use pull requests with our trunk-based branching strategies
Date: 2022-04-01
Category: Posts 
Tags: engineering, version-control
Slug: branching-pull-request
Author: Willy-Peter Schaub
Summary: Busting a few process myths around branching strategies and pull-requests

If you want to ignite a debate in a pub, casually start chatting about politics. In a [virtual] room of software engineers, gently mention branching strategies and pull requests. In both scenarios you can sit back and enjoy the vibrant chain reaction of experiences, opinions, and myths. In this brief article I will share our experience, our [standardization](/consistency-standardization.html) of branching strategies, our use of [pull requests](/pull-requests-friend.html), and bust a few myths along the way.

---

# Branching Strategies

TBD

> MYTH 1 - Trunk-based branching strategy is suited only for small and experienced teams!
>
> _The [Microsoft Azure DevOps](https://medius.studios.ms/Embed/Video/THR2017?sid=THR2017) and [Microsoft Office](https://devblogs.microsoft.com/devops/improving-azure-devops-cherry-picking/) are two very large teams that poof that the trunk-based branching strategy scales from small and rapid experimentation and innovation teams, to large product-based teams._

> MYTH 2 - One branching strategy is better than another!
>
> _There is no silver bullet! Avoid the debates and invest time to experiment with a few of the common branching strategies, to determine the best fit for your PEOPLE, PROCESS, and PRODUCTS._ 

---

# Pull Requests

TBD

> MYTH 3 - Pull-requests slow down your continuous integration value stream!
>
> _A pull request takes as long as you and your process allow it to sit in a corner to gather dust. We encourage our engineers to track the lead and cycle times of pull requests using the [Pull Request Completion Report](https://marketplace.visualstudio.com/items?itemName=OneLuckiDev.prApprovalReport&targetId=dc216ba3-25e9-46a8-823a-fb77a81f2a9f) and to **collaborate** with their peers to ensure that pull requests do not go stale._

> MYTH 4 - Pull-requests are manual gates
>
> _In theory a pull request (in Azure DevOps) could be all automated, based on policies, validation builds, and other validations. It is as manual and/or automated as YOU decide to configure your policies and guardrails._

> MYTH 5 - Trunk-based branching strategy and use of pull requests is a NO-NO!
>
> _"In theory" the trunk-based strategy is based on short-lived feature branches and merging changes directly with the master branch. Using a pull request as a pre-merge validation does not change the strategy, it merely inject a final countdown checkpoint before you commit your code changes to the "always deployable" master|main branch. It is an opportunity to move your scale of **trust**, not a matter of changing the branching strategy._

---

For branching strategies and the use of pull requests there is no silver bullet. Once you realize that consistency and standardization trumps personal preference and variations, you can pick the branching strategy and the use of pull-requests (or not) that empowers your engineers and organization. 


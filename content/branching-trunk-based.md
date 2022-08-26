Title: Trunk-based branching strategy without the bells and whistles
Date: 2022-08-31
Category: Posts 
Tags: engineering, version-control
Slug: branching-trunk-based
Author: Willy-Peter Schaub
Summary: Keeping it simple and avoiding the soul quenching politics

We pickup from the [Why we use pull requests with our trunk-based branching strategies](/branching-pull-request.html) virtual chat, where we discussed [pull requests](/pull-requests-friend.html) and briefly touched on trunk-based development. This article is based on a script I prepared for an upcoming innovation workshop, where we will lift the bonnet to explore our blueprints and

## Why?

> ![Why](/images/branching-trunk-based-1.png)

It is one of many branching strategies, our recommended strategy, and the norm with our [application-type blueprint](./yaml-pipelines-part10.html)-based pipelines to enable **consistency** and **standardization**.

> ![Reasons](/images/branching-trunk-based-2.png)

By merging **small** and **frequent** updates (short-lived feature branches) to a core **trunk**, master, or main branch, we streamline merging, integration of code, enable continuous integrations, automated tests, continuous code reviews, and automated validations. We guard the trunk to maintain a **green** source of truth, ready to deploy at any commit.

Trunk-based development is a proven and common practice among high-performing DevOps teams, often complemented by feature flags and/or ring-deployments to deploy continuously and release on demand – our future vision. 

---

# Getting started

> ![Trunk](/images/branching-trunk-based-3.png)

We start with a trunk, that has a hypothetical version of MAJOR 0, MINOR 1, and PATCH 0, aka **0.1.0**. ome point we create a feature branch to build a new feature and another feature branch to address a bug.

When we are ready to deploy we merge our changes back to the **stable** trunk. As discussed in [Why we use pull requests with our trunk-based branching strategies](/branching-pull-request.html), we are stopped by the branch policies that demand a code review by one or more reviewers, closed comments, linked work items, a clean validation build, and healthy code and security scans.

We could, but we will not, argue that with trunk-based development we should be able to commit directly to the **trunk**. Theoretically **yes** - if we are part of a high-performance and high-trust team we can commit **directl** to the trunk, however, in my 35+ years of engineering I have had the priviledge of working for such a team two or three times.have a small, mature, and experienced team that **trusts** 

When our code has been proven GREEN the changes are merged to the trunk and versioned 0.1.1, followed by the bug fix changes, versioned 0.1.2.

---

# Release branch

> ![Trunk+Release](/images/branching-trunk-based-4.png)

When we are ready to deploy, we create a label and a release branch from the label, which triggers our continuous integration and delivery pipeline.

> ![Hotfix-1](/images/branching-trunk-based-5.png)

After we deploy to production the unthinkable happens ... we detect a bug! 

If **not** serious, we add it to our technical debt and to be fixed with the next feature work.

---

# Hotfix - Option 1

If **serious**, we create a HOTFIX on the trunk and merge it back to the release branch, which in turn triggers another production deploy.

>
> Note that you can perform the merge to trunk and the release branch with one pull request, using the [PR Multi-Cherry-Pick](https://marketplace.visualstudio.com/items?itemName=1ESLighthouseEng.pr-multi-cherry-pick) extension, developed by the Microsoft Office team. This tool allows you to use the git cherry-pick operation to apply changes to multiple branches.
>

---

# Hotfix - Option 2

Another option is to apply the hotfix to the release branch and then merge it back to **trunk**. 

> ![Hotfix-2](/images/branching-trunk-based-6.png)

Which option is better? You decide and you pick your strategy!

The **trunk-based** branching strategy is straight-forward, well-suited for the 2-pizza sized product team, and lays a solid foundation for our quest for continuous delivery and release on demand. 

Remember, keep it **SIMPLE**!


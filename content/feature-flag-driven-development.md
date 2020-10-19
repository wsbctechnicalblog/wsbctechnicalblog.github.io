Title: Feature-flag Driven Development (FFDD)
Date: 2020-09-04 11:10
Category: Posts
Tags: Feature-flag
Slug: feature-flag-driven-development
Author: Alex Bunardzic
Summary: Replace physical modularity with logical modularity


Experts say that repo branching workflow is poor man’s modularization (by experts I mostly refer to Martin Fowler and his team of deep thinkers). What do we mean by branching being poor man’s modularization?

## Well modularized repo

Let’s examine how change management propagates in a repo that has been properly modularized from the get go:

A new feature needs to be added to the product, which necessitates change to the codebase. Because the code is fully modularized, it is closed to any changes related to the new feature, but is at the same time open for any changes that would extend its feature set (the Open/Closed Principle, part of the SOLID package).

The new feature will thus be coded by adding brand new modules. Barely any line of existing code will have to be modified, since the new feature would be a plugin.

## Poorly modularized repo

A code that is poorly modularized will have to be modified (sometimes heavily) in order to introduce a new feature into the product.

Any time two or more people are working on the same block of code, they introduce a moving target. Changes made to the same codebase may result in a conflict. That conflict potentially arises at the time when we are trying to retrofit new code into the existing codebase. Those are the dreaded merge conflicts.

## Why do we branch in the first place?

The main reason we copy the existing code base and turn it into a feature branch is to protect the healthy master branch from getting corrupted. Teamwork often necessitates that two or more feature branches get created during sprint, and that means that there is an ongoing work that is happening in parallel. When the time comes to bring the new changes to the healthy branch, some of those new changes may mutually collide.

So the caution we exercise by branching is introducing unwanted risks of creating merge conflicts.

## How to avoid merge conflicts?

During the workflow described above, it is not really possible to avoid potential merge conflicts. But we can certainly minimize potential conflicts.

It all boils down to timing. When we take a copy of the healthy branch and go away and begin making changes to the code, the clock starts ticking. The longer we wait to bring our changes to the healthy branch, the greater that chances that someone else had already made changes to it that may collide with our changes.

That is one of the main reasons why best practices advocate short-lived branches. The shorter the lifespan of a branch, the smaller the risk of having merge conflicts. And lesser merge conflicts mean quicker value delivery and lesser churn.

And of course, merge conflicts are of much lower possibility in well modularized codebases, as we have already discussed above.

## Feature flags

Much as Martin Fowler et al claim that branching is poor man’s modularization, it is also possible to say that branching is poor man’s feature flags. So what are feature flags?

Feature flags could be viewed as logical branching. While physical branches, as they are practiced in modern engineering mostly using git, require making a physical copy of the repo and giving it a unique name, feature flags could be used without necessarily having to make a physical copy. When using Feature-Flag Driven Development (FFDD), we simply leave the existing code intact and write new modules that get conditionally called. The conditional logic is binary, and is governed by the feature flag (which could be either in on or in off state). If the flag is in the on state, the new code will get executed. Otherwise, execution continues as usual (old code runs).

FFDD enables us to add potentially risky changes to the healthy codebase, without going through the song and dance of trying to merge the changes and risking merge conflicts. This technique then enables us to quickly ship new features in stealth mode. Our regular customer population will not get affected, since they will still be using the old, tested codebase. But our QA can then safely assess and evaluate the risks and potential merits of the new code. That activity would be the equivalent of the Pull Request in the branch-driven development discipline. If the PR of the code under the feature flag passes the muster, the old code gets decommissioned and the new code becomes the healthy version of the codebase.

<br /><br />
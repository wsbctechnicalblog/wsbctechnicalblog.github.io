Title: Renaming Git Branches in Azure DevOps: A Simple Task, Eight Easy Steps, and Mild Despair
Date: 2026-02-25
Category: Posts 
Tags: engineering,azure-devops, version-control
Slug: engineering-practices-branch-rename
Author: Willy-Peter Schaub
Summary: How a One-Character Change Turned into a Full-Contact Git Exercise

Every so often, we decide to “clean things up”. In this particular episode of organisational optimism, the goal was innocent enough: rename all branches from

`Release/<branch-name>`
to
`release/<branch-name>`

Lowercase. Consistent. Civilised.
What could possibly go wrong?

> ![<SAMPLE PIC>](../images/engineering-practices-branch-rename-1.png)

# Challenge 1: Case Sensitivity, or “Git Knows Better Than You”

>
> The first obstacle is that we often believe that `Release/1.0` and `release/1.0` are two entirely different branches. As far as your local file system is concerned, they may very well be the same thing, or not. 
>

Git, in turn, is case-sensitive. This leads to confusion, errors, and a general sense that you have personally offended your version control system.

Microsoft documents this behaviour clearly, including why Azure Repos enforces it and why case-only changes are problematic:
[Git case sebsitivity](https://learn.microsoft.com/en-us/azure/devops/repos/git/case-sensitivity?view=azure-devops).

The short version: Git is right, the file system is awkward, and you are caught in the middle.

# Challenge 2: There Are No Branch Folders

>
> Despite what the slash in `Release/1.0` suggests, Git does not have branch folders.
> There is no Release directory. There is no tree. There is no hierarchy.
> 

The `<folder>` portion of a branch name is merely a naming convention. It is a label. A polite fiction. A comforting illusion we all agree to maintain so that we can pretend our repositories are tidy.

Internally, Git stores branches as references. The slash just happens to look like a folder, much like a cardboard box looks like furniture.

# Challenge 3: There Is No Rename Feature

>
> There is no `rename branch` button.
>

Not in Git. Not in Azure DevOps. Not anywhere sensible.

This is presumably because renaming a branch would be too easy, too humane, and would deprive future engineers of valuable character-building experiences.
So instead, we simulate a rename by creating new branches and deleting old ones. Carefully. Repeatedly. With feeling.

# The Only Way Forward

Because Git refuses to acknowledge that `Release` and `release` are “basically the same thing”, on Azure DevOps with case-sensitivity disabled, we need an intermediate step. A neutral ground. A diplomatic buffer.
Let us call it `Temp`.

### Step 1: Clone the Repository

```
git clone https://dev.azure.com/your-org/your-project/_git/your-repocd your-repo
```

### Step 2: Rename Release/* to Temp/* Locally

Fetch all branches first:

```
git fetch --all
```
Rename the branch you are currently on:

```
git branch -m Release/1.0 Temp/1.0
```

Repeat this for all branches under `Release/*`:

```
git branch -m Release/1.1 Temp/1.1
git branch -m Release/2.0 Temp/2.0
...
```

### Step 3: Push the `Temp/*` Branches to Azure DevOps

```
git push origin Temp/1.0git push origin Temp/1.1git push origin Temp/2.0Show more lines
```

### Step 4: Delete the Release/* Branches from Azure DevOps

```
git push origin --delete Release/1.0
git push origin --delete Release/2.0
```

At this point, the repository no longer contains Release/*. Everyone takes a deep breath.

### Step 5: Re-clone the Repository

Yes, really. This avoids local case-confusion and reference residue.

```

cd ..
rm -rf your-repo
git clone https://dev.azure.com/your-org/your-project/_git/your-repo
cd your-repo
git fetch --all
```

### Step 6: Rename Temp/* to release/*

```
git branch -m Temp/1.0 release/1.0
git branch -m Temp/2.0 release/2.0
...
```

### Step 7: Push the `release/*` Branches to Azure DevOps

```
git push origin release/1.0
git push origin release/2.0
...
```

### Step 8: Delete the Temp/* Branches from Azure DevOps

```
git push origin --delete Temp/1.0
git push origin --delete Temp/2.0
...
```

# Final Thoughts

What began as a simple case change turned into a multi-stage choreography involving temporary branches, multiple pushes, deletions, and a ceremonial re-clone.

Git is powerful. Azure DevOps is correct. The process is logical.

It is also impressively unintuitive.

I sincerely hope that someone out there has a better idea.


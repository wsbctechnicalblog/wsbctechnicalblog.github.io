Title: The clash of Azure DevOps Kanban fields and Shared Area Paths
Date: 2020-10-22 13:13
Category: Posts
Tags: AzDO, Azure-Boards
Slug: shared-area-paths
Author: Willy-Peter Schaub
Summary: Shared area paths can introduce inconsistency and confusion.

Azure Boards Kanban fields are powerful and valuable. Used in the land of shared Area Paths they can, however, introduce inconsistency and confusion that are hard to isolate and explain.

# Let us explore a simple example 

We define a few area paths for a hypothetical project, named **Boards Chaos**. The Board Chaos area and its sub-paths are allocated to the default Boards Chaos team. Area A1, with sub-paths, and area A2, with sub-paths, are assigned to team A and B respectively. 

![Board Chaos](/images/clash-of-azdo-kanban-fields-and-shared-area-paths-1.png)

> **NOTE** that the Boards Chaos team shares area A1 and its sub-paths with team A, and area A2 and its sub-paths with team B. Assigning area Board Chaos and sub-paths to the default team is a subtle configuration, but allows us to demonstrate the challenge of shared area paths.

**Team A** creates three stories and pulls A.1 and A.2 into the **Active** column.

![Team A Board](/images/clash-of-azdo-kanban-fields-and-shared-area-paths-2.png)

**Team B** creates three stories, and pulls B.1, B.2, and B.3 into the **Active**, **Resolved**, and **Closed columns**.

![Team B Board](/images/clash-of-azdo-kanban-fields-and-shared-area-paths-3.png)

When we switch to team **Board Chaos**, we notice that the team has customized their board, renaming the Active column to In-flight, and adding the Area 51 and Answer 42 columns. All of these three columns map to the Active work item state.

So far so good - if you ignore the **Board C...** **Active** field on the card.

![Team Chaos Board](/images/clash-of-azdo-kanban-fields-and-shared-area-paths-4.png)

Board Chaos team drags cards A.1 from In-flight to **Area 51**, and A.2 to **Answer 42**.

![Area 51](/images/clash-of-azdo-kanban-fields-and-shared-area-paths-5.png)

The team's board looks as expected, again as long as you ignore the field **Board C...** **Active** field on the cards.

![Board Chaos](/images/clash-of-azdo-kanban-fields-and-shared-area-paths-6.png)

# Oh, Oh, we have a problem

When the team looks at their product backlog, the anomaly becomes evident. Why are the Board Column values for B.1, A.1, and A.2 Active and not **In-flight**, **Area 51**, or **Answer 42**?!? 

![Incorrect Board Column Values](/images/clash-of-azdo-kanban-fields-and-shared-area-paths-7.png)

Here is a view of Team A and the default team next to each other. Now look at the **Board C** ... field on the cards, all of which point to Team A's **Active** column.

![Team A and Chaos side by side](/images/clash-of-azdo-kanban-fields-and-shared-area-paths-8.png)

What is going on?!?

# Works as designed

By design, the team with the longest area path wins the clash and dictates the values for the Kanban Board Column, Done, and Lane fields. In our setup, teams A and B have the longer area paths and win. **Board Chaos/A1** from team A, for example, is longer than Board Chaos/ from the default team.

If we have a scenario of shared area paths of equal depth, we will have non-deterministic results. Not in scope for this simple walk-through.

As a result the cards show the Kanban field value Active for Team A on Board Chaos' board, not values **In-flight**, **Area 51**, **Answer 42** as expected. 

So, how can we avoid this unexpected feature?

# Tips to avoid the "oh, oh" moments

![Oh Oh Moment](/images/clash-of-azdo-kanban-fields-and-shared-area-paths-9.png)

## Avoid shared areas

Stay away away from overlapping area path ownership. As this behavior is "as expected" and "works as designed", we do not expect future features to work seamlessly. 

> See https://msdn.microsoft.com/Library/vs/alm/Work/scale/scaled-agile-framework on guidance to setup enterprise projects.

## Share read-only areas

Keep teams in their own contained, for example (1) Team A in Area A1 and (2) Team B in Area A2. If you need a shared area path, for example, (3) to raise awareness of and triage bugs use it as a read-only area and (4) reassign bugs to their respective area paths.

![Shared Area Paths](/images/clash-of-azdo-kanban-fields-and-shared-area-paths-10.png)

## Focus on your context

Focus on the work item types that are relevant to you and your team. If you are doing portfolio planning you should restrict your views of shared areas to **Initiatives**, **Epics**, and **Features**. If you are part of the development, you should focus on Stories or Backlog Items.

In other words **keep it simple***!



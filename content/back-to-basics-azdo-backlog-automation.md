Title: Automate Azure DevOps work item state transitions like a Pro
Date: 2024-06-17
Category: Posts 
Tags: agile, azure-devops, learning, 101
Slug: back-to-basics-azdo-backlog-automation
Author: Willy-Peter Schaub
Summary: Maintain your backlog by changing the status of work items according to the status of their subitems.

When I review our Azure DevOps (AzDO) backlogs and team settings, I sometimes ask myself why teams do not tidy up their backlogs to prevent subtle, but significant state inconsistencies. 

> ![Anomalies](/images/back-to-basics-azdo-backlog-automation-0.png)

As shown, I often encounter parents in a **new** or **active** state, with all their children in a **closed** state – are we expecting more children or has the parent been overlooked? Alternatively we see parents in a **new** state and children in an **active** state – have we wrongly started work, mistakenly moved the child work item into an active state, or has the parent again been neglected?

Maybe the AzDO team snuck in a new and useful feature to the product as part of the **New Boards Hubs** preview feature and the teams do not know yet. I will assume this to be the case and show you 3 easy steps to create magic.  

1. Turn on the New Boards Hubs preview feature.

    > ![New Board](/images/back-to-basics-azdo-backlog-automation-1.jpg)

2. Check your Team Settings and look at Automation – Rules.

    > ![Settings](/images/back-to-basics-azdo-backlog-automation-2.jpg)

3. Set up how you want to automate your parent work item states.  

    > ![Automation](/images/back-to-basics-azdo-backlog-automation-3.jpg)

Do steps 2 and 3 for each backlog level that needs this great feature.  

That is all – enjoy the **magic**.

>
> **IMPORTANT NOTES**:
>
> 1. Automation is **team** specific.
> 2. Automation is **backlog-level** specific.
> 3. Automation only triggers for work items that **belong to the same team**!
>

A special note for my colleague **Pam**:

>
> **IMPACT ON PORTFOLIO AND SCORECARD BACKLOGS**:
>
> Number 3 in above notes affects our portfolio and scorecard backlogs. The automation will not work when linked children from other AzDO projects and/or teams are closed, if they are attached to portfolio or scorecard parents.
>

For more information read [Automate work item state transitions](https://learn.microsoft.com/en-us/azure/devops/boards/backlogs/automate-work-item-state-transitions?view=azure-devops).

---

# Related [AzDO](https://azure.microsoft.com/en-us/products/devops) Board posts

- [Agile Boards Tips](/agile-boards-tips.html)
- [Azure Boards Tips - Stop messing with our backlog!](/azure-boards-tips-stop-messing-with-our-backlog.html)
- [Azure Boards Tips for Operations Teams](/azure-boards-tips-operations-team.html).
- [Azure Boards Tips - Retain hierarchy with filter](/azure-boards-tips-retain-hierarchy-with-filter.html)

---

Have you discovered and are you enjoying this nifty automation rule?


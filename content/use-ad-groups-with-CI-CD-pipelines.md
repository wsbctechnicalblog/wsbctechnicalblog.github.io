Title: Use Active Directory Groups in your unified classic CI CD pipelines
Date: 2020-10-20 13:13
Category: Posts
Tags: azure, azure-devops, pipelines
Slug: ad-groups-for-ci-cd-pipelines
Author: Willy-Peter Schaub
Summary: Instead of managing permissions for users in Azure DevOps, we use Azure Active Directory groups to fine tune permissions

The CI/CD pipeline is a DevOps practice for delivering code changes more frequently, consistently, and reliably. It enables Agile teams to increase deployment frequency, decrease lead time for change, change failure rate, and mean time to recovery key performance indicators, thereby improving quality and delivering value faster.

# Let us use Active Directory (AD) security groups

After our dream for One CI/CD pipeline to rule them all we decided to go one-step further and simplify the classic release pipeline security using Active Directory (AD) groups. Instead of assigning and managing permissions for users in Azure DevOps, we use Azure Active Directory groups to fine tune permissions. For example, we have project specific super users AD groups that grant elevated permissions to edit release pipelines and the development and system test stages.

![Classic Pipeline](/images/use-ad-groups-with-CI-CD-pipelines-1.png)
> Empower the Agile Development Team to own development and system test stages

Bookmark the Azure DevOps DRIFT project, which will enable you to monitor and remediate configuration drift, for example to automatically remove explicit user accounts added to an AD driven security model.

# Why AD groups?

The value of using AD groups depends on your environment. In our case the benefits are:

- AD groups and memberships are centrally **managed** and **audited**.
- AD group membership is track than individual user accounts spread across multiple Azure DevOps services and projects.
- Azure DevOps users are empowered to request group membership using an existing process, rather than relying on the Azure DevOps project collection and project administrators.
- Simplifies automation of pipeline generation and configuration.

![Simplicity](/images/use-ad-groups-with-CI-CD-pipelines-2.png)

# Let us use email-enabled Active Directory (AD) security groups

However, wait, we can go a step further and use mail-enabled AD security groups for pre- and post-stage pipeline approvals.

![Post deployment conditionse](/images/use-ad-groups-with-CI-CD-pipelines-3.png)

Use email-enables security groups for stage approvals
We replace the individual users highlighted in yellow with Release Approval AD groups.

![CI CD pipelines](/images/use-ad-groups-with-CI-CD-pipelines-4.png)
> Simplify stage approvals with email-enabled AD security groups

Why are there no stage approval notifications?
We realized that some of our email-enabled AD security groups received no notifications and spend time with Microsoft support to identify the root cause(s).

You have to ensure that the AD security groups:

- Are **mail-enabled** and authorized to receive external emails.
- Have **View Releases** permissions on release and definitions.
- Have a subscription that is enabled for the group(s).

The second bullet is the one that caught us off guard. If the permission is missing the Azure DevOps Pipeline event/notification service filters out the account's notifications. When notifications are filtered, no email is sent for impacted group(s) - silence prevails.

Make sure that your email-enabled AD security groups are members of your project **Contributors or Readers**, which by default, have the View Releases permission.

# What Is Next?

This is likely one of the last posts on classic CI/CD pipelines. Watch the space for unified multi-stage YAML-based pipeline learnings.



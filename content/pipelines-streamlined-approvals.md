Title: Streamlining your pipeline approvals, without flooding DevSecOps with noise
Date: 2021-03-13
Category: Posts
Tags: azure-devops, eliminate-waste, pipelines, tips
Slug: pipelines-streamlined-approvals
Author: Willy-Peter Schaub
Summary: Back to the future, to optimize the Classic Azure Pipeline approvals.

To improve our deployment frequency, reduce our lead time for change, and avoid unnecessary release stress, we have invested a lot of time reviewing processes and products. In this post I am **NOT** covering the magic of YAML-based pipelines (see [magic of queue time assembly](https://wsbctechnicalblog.github.io/yaml-pipelines-part4.html) for details), but am focusing on the classic Azure Release Pipelines.

>
> DEPLOYMENT FREQUENCY - determines how many deployments are made to ****production**.
>
> LEAD TIME FOR CHANGE - is the average time between receiving a feature request and deploying it to **production**.
>

# Streamlined approvals

![Streamlined Approvals](/images/pipelines-streamlined-approvals-1.png)

As shown, we assume we have a release pipeline that deploys artifacts received from the continuous integration (build) pipeline to a development, system test, canary, and production environment. Deployment to the development environment is automatic, whereas we have gates before can deploy to the system test, canary, and production environments.

For each gate we use one or more Azure Active Directory (AAD) groups to define the group of users who are authorized to approve the deployment. See [use gates and approvals to control your deployment](https://docs.microsoft.com/en-us/azure/devops/pipelines/release/deploy-using-approvals?view=azure-devops).

You may or should be frowning at this point, because anything that is deployed to the system test environment automatically triggers the Security Review. In our environment this lead to agitated Security Engineers who were inundated with security review request across hundreds of release pipelines.

![Unhappy DevSecOps](/images/pipelines-streamlined-approvals-3.png)

Let us reduce the number of security reviews which are WASTEful and check back with DevSecOps.

---

# Artifact filters

![Artifact Filters](/images/pipelines-streamlined-approvals-2.png)

TBD

![Happy DevSecOps](/images/pipelines-streamlined-approvals-4.png)

---

# Mulling over the future approvals

TBD


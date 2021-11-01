Title: Streamlining your pipeline approvals, without flooding DevSecOps with noise
Date: 2021-03-13
Category: Posts
Tags: azure-devops, eliminate-waste, pipelines, tips
Slug: pipelines-streamlined-approvals
Author: Willy-Peter Schaub
Summary: Back to the future, to optimize the Classic Azure Pipeline approvals.

To improve our deployment frequency, reduce our lead time for change, and avoid unnecessary release stress, we have invested a lot of time reviewing processes and products. In this post I am **NOT** covering the magic of YAML-based pipelines (see [magic of queue time assembly](https://wsbctechnicalblog.github.io/yaml-pipelines-part4.html) for details) but am focusing on the classic Azure Release Pipelines.

>
> DEPLOYMENT FREQUENCY - determines how many deployments are made to ****production**.
>
> LEAD TIME FOR CHANGE - is the average time between receiving a feature request and deploying it to **production**.
>

# Streamlined approvals

![Streamlined Approvals](/images/pipelines-streamlined-approvals-1.png)

As shown, we assume we have a release pipeline that deploys artifacts received from the continuous integration (build) pipeline to a development, system test, canary, and production environment. Deployment to the development environment is automatic, whereas we have gates before can deploy to the system test, canary, and production environments.

For each gate we use one or more Azure Active Directory (AAD) groups to define the group of users who are authorized to approve the deployment. See [use gates and approvals to control your deployment](https://docs.microsoft.com/en-us/azure/devops/pipelines/release/deploy-using-approvals?view=azure-devops).

You may or should be frowning at this point, because anything that is deployed to the system test environment automatically triggers the Security Review. In our environment this led to agitated Security Engineers who were inundated with security review request across hundreds of release pipelines.

![Unhappy DevSecOps](/images/pipelines-streamlined-approvals-3.png)

Let us reduce the number of security reviews which are WASTEful and check back with DevSecOps.

---

# Artifact filters

The eye of the storm is created as we are passing all the artifacts down the release pipeline, regardless from which source repository branch it originated from. In other words, security engineers were triggered for changes that were not ready for prime time (production).

![Artifact Filters](/images/pipelines-streamlined-approvals-2.png)

By adding an **artifact filters** allow us to create a first line of defense against artifacts that were generated from source repository branches that are not trusted in production and therefore do not require a security review. We only allow artifacts originating from **release** branches to trigger a security review and trundle down the pipeline.

>
> ![Happy DevSecOps](/images/pipelines-streamlined-approvals-5.png)
> Artifact filters can be overridden if you have relevant permissions. If you need a "**you shall not pass**" checkpoint, you should investigate the YAML-based pipelines as mentioned above.
>

See [Branch and Artifact Filters in Azure Pipelines](https://medium.com/objectsharp/branch-and-artifact-filters-in-azure-pipelines-83d4256ada98), by Dave Lloyd, for a great overview of artifact filters. 

![Happy DevSecOps](/images/pipelines-streamlined-approvals-4.png)

We now have less WASTE, which makes me happy, and a lot less security reviews, which improved our security engineers' mood and ability to be laser focused on potential production deployments.

---

# Mulling over the future approvals

>
> _"Constantly think about how you could be doing things better. Keep questioning yourself."_ - Elon Musk
>

We take this quote to heart and have been mulling over our streamlines approval process. When we map a pipeline to a value stream it becomes evident that all of the gates and the security review contribute to our **Lead time for change** - WASTE.

Where we can, we ...

- Reduce the number and the sequence of approvals.
- Automate validations and approvals.

Leaving us with security review, which is based on automated vulnerability and quality scans and a few pairs of security engineer eyeballs. My colleague Kevin and I have been chatting about the [NEXUS](https://nexus-card.ca/)-type border control process, which may allow us to expedite parts of the security reviews based on **trust**. Watch this space for updates.


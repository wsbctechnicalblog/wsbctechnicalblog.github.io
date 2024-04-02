Title: Technology Framework Monitor - Open Source Software Sync 20240322
Date: 2024-04-02
Category: Posts
Tags: azure-devops, pipelines, engineering
Slug: azure-tfm-oss-sync-20240322
Author: Willy-Peter Schaub
Summary: The broader our scanning efforts, the more technical debt we uncover, enabling proactive resolution.

The ongoing evolution of our Technology Framework Monitor (TFM) open-source project empowers us to expand our horizons in identifying end-of-life products and detecting engineering practice drift. In this latest update, we have integrated [Azure Pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines?view=azure-devops) referencing and exploration logic. Our next step involves adding support for NODE scans and automating Azure DevOps work item generation for identified issues.

---

>
> [Click here to peruse associated Pull Request](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Technology-Framework-Monitor/pull/27)
>

Changes as documented by Andreas Mertens encompasses four main changes:

1. Addition of YAML and Classic Build pipeline scans.
2. Incorporation of Classic Release pipeline scans.
3. Resolution of a bug causing duplicate File records. Previously, the FileID for a file was mistakenly considered a hash code, leading to duplication. This has been rectified by using the Path to uniquely identify files in the repository.
4. Identification and resolution of a database connection leak. The base (DBCore) of all connections has been made IDisposable, ensuring proper disposal once the connection's work is completed.

>
> **UPDATE**: A known issue with Classic Release pipelines, particularly regarding Artifacts, has been addressed in the code update. The auto-generated code from JSON contained a reference to internal information as a field, which has been removed for clarity and security.
>

---

What else can/should/must we consider as part of our TFM product? Thoughts?

Title: Technology Framework Monitor - Open Source Software Sync 20240510
Date: 2024-05-10
Category: Posts
Tags: azure-devops, pipelines, engineering
Slug: azure-tfm-oss-sync-202400510
Author: Willy-Peter Schaub
Summary: Shake Off the Dust: Our TFM Software Spring Cleaning!

The ongoing evolution of our Technology Framework Monitor (TFM) open-source project empowers us to expand our horizons in identifying end-of-life products and detecting engineering practice drift. In this latest update, we have performed tons of spring cleanups. Our next step involves adding support to detect drift from our engineering practices.

---

>
> [Click here to peruse associated Pull Request](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Technology-Framework-Monitor/pull/31)
>

Changes as documented by Andreas Mertens encompasses three main changes:

1. **Eliminated Dead Weight**: Purged unused code, resolved null warnings, and adhered to naming conventions. Enhanced project stability by incorporating AssemblyVersion and AssemblyFileVersion attributes into the AssemblyInfo.cs file. Updated NuGet package versions for optimal performance. Implemented a more efficient method, sourced from StackOverflow, to delete repositories after processing. Streamlined code for clarity, eliminating unnecessary warnings and informational messages.

2. **Data Optimization**: Introduced a new database view - ReportsScan - refining data presentation from the Reports table, excluding select fields and introducing Timestamp for enhanced insights. Transitioned smoothly from EntityFramework to EntityFrameworkCore, necessitating a revamp of the ProjectScannerSaveToSqlServer project. Enhanced the DbCore class to manage disposal and monitor open connections effectively.

3. **Fine-Tuning**: Empowered the main executable with parameters for single scan phases, enhancing flexibility. Addressed scenarios where repositories are disabled or not downloaded, providing clear console comments for troubleshooting. Improved performance by adding an index to the Reports table, optimizing the ReportScan view for faster access."

---

What else can/should/must we consider as part of our TFM product? Thoughts?

Title: Engineering Practice Nuggets
Date: 2023-01-18
Category: Posts 
Tags: code-quality, design, engineering, technical-excellence
Slug: EngineeringPractice-1
Author: Martin M. Lacey
Summary: Nuggets of Knowledge and Best Practices in Software Engineering

When we design, build, and deploy software we aim to apply patterns and learned best practices in order to produce
consistent and robust solutions that are of the highest quality and lowest possible technical dept (burden to maintain).

These powerful nuggets of knowledge, patterns and practices, and key areas that we are evolving and 
improving will be the subject matter explored with the goal to invigorate 
vibrant collaboration and innovation, and indeed experimentation and tenacity 
when things don't go as desired.


---
# Metrics and Quantitative Measures
In addtion to the four standard DevOps metrics:
* Deployment Frequency —How often an organization successfully releases to production
* Lead Time for Changes —The amount of time it takes a commit to get into production
* Change Failure Rate —The percentage of deployments causing a failure in production
* Time to Restore Service —How long it takes an organization to recover from a failure in production

We have begun the process of calculating various metrics on software created at
WSBC, using SonarQube in the build and deploy pipelines.
These will soon be augmented by Stryker to generate mutant test cases and validate them, 
as well as the Roslyn Analyzer for further code analysis.  

These measurements are calculated when the pipeline for a product is
invoked, providing us with statistical data that we can use to gauge the quality
improvements over time.

---
# Engineering Capability Maturity
We are now developing a Capability Maturity Model for Software Engineering Practices 
at WSBC, similar to the Maturity Model for Agile practices combined with CMM for 
Software - and supported by Scaled Agile Framework for the Enterprise (SAFe).  

We are working to identify the capabilities at each level and how to measure them, 
and how to put processes in place or refine existing processes  to support their 
improvement and cultivate an open culture of experiment-fail-learn and 
share as discussed in [Fail, Learn, Reset!](https://wsbctechnicalblog.github.io/fail-learn-reset.html).

---
# EDO Ce Recommended Product Catalog
The EDO Recommended Product Catalog is getting a radical facelift, with a cool 
new periodic-table style layout with pop-up cells that clearly describe the 
product and purpose and current version.  Clicking on the tile opens a modal 
dialog describing the product in full, with links to download either from 
ServiceNow or the product own download page.

We are busily creating Phase II, enabling a Search capability and populating the
table cells based on a query to live *editable* data in SharePoint.

In a future post, we will dig deeper into the Product Catalog; how it has evoloved 
to support and enhance our development teams navigation, education, and adoption of
technology recommended for our development community.

---

Watch this space for bi-weekly Engineering Practice updates, latest developments, and recommended
best practices, techniques, patterns, and methods recommended for building
the next generation of interconnected loosely-coupled systems and services in our 
*Software Factory Vision*.

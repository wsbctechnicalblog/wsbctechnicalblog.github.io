Title: <TRY KEEP TITLE SIMILAR TO SLUG WITHOUT - AND SENTENCE CASING>
Date: 2023-08-21
Category: Posts
Tags: azure-devops, pipelines, engineering
Slug: azure-pipeline-yaml-refactor
Author: Willy-Peter Schaub
Summary: Seizing the chance to enhance and optimize our CI/CD/IaC pipelines.

I understand that you may have been delving into our open-source endeavor, which revolves around Azure Pipelines for continuous integration and continuous delivery, employing YAML-based methodologies. If this initiative has not caught your attention yet, I highly recommend acquainting yourself with our  source project, focused on YAML-based continuous integratuion and continuous delivery Azure Pipelines. If not, you better explore our open-source [WorkSafeBC Common Engineering](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2) project as a starting point.

For those who are new to this concept, I have compiled a selection of blog links that you might find valuable for a comprehensive understanding:
- [Part 1: Pipelines - Why bother and what are our nightmares and options?](https://wsbctechnicalblog.github.io/why-pipelines-part1.html)
- [Azure DevOps Pipeline OSS v2.1 Flow](https://wsbctechnicalblog.github.io/azure-devops-pipeline-oss-v2-1-flow.html)
- [Azure Pipelines Blueprint QA Integration](https://wsbctechnicalblog.github.io/azure-pipelines-blueprint-qa-integration.html)

---

# OK, why are we here?

Indeed, we are currently in the process of integrating infrastructure-as-code (IaC) into our v2 blueprints. This advancement entails the inclusion of a substantial number of parameters within our variable template files. As a consequence, a series of sleepless nights has ensued for our team. To provide a visual depiction, please refer to the illustration below, where the newly added components are represented in pink.

> ![IaC](../images/ azure-pipeline-yaml-refactor.png) 

If we have a quick look at the basic [101 sample variable template](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/commit/eee9e2e895e8869e1f4fc8e7b55b1973b469351f#diff-34a1ea16e45e933dd3f78d78dd2752204483355a45237fb33d7a31b1bb51e383) you will notice that we have a **FLAT** configuration file.

```
variables:

# --------------------------------------------------------------------
# Blueprint: __101__
#
# If you are not going to use all stages, as below, you can suppress them by simply commenting out
# or removing their entire configuration section.
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# DEVelopment Stage
# --------------------------------------------------------------------
- name:  developmentStageName
  value: 'Development' # Do not change stage name value
- name:  developmentStageEnvName
  value: '<TBD>'
- name:  developmentStageVmImage
  value: '<TBD>'
# TODO Add your variables here

# --------------------------------------------------------------------
# System Test Stage
# --------------------------------------------------------------------
- name:  systemTestStageName
  value: 'SystemTest' # Do not change stage name value
- name:  systemTestStageEnvName
  value: '<TBD>'
- name:  systemTestStageVmImage
  value: '<TBD>'
# TODO Add your variables here

# --------------------------------------------------------------------
# Security Review Stage
# --------------------------------------------------------------------
- name:  securityReviewStageEnvName
  value: '<TBD>'

# --------------------------------------------------------------------
# Staging Stage
# --------------------------------------------------------------------
- name:  stagingStageName
  value: 'Staging' # Do not change stage name value
- name:  stagingStageEnvName
  value: '<TBD>'
- name:  stagingStageVmImage
  value: '<TBD>'
# TODO Add your variables here

# --------------------------------------------------------------------
# PRODuction Test Stage
# --------------------------------------------------------------------
- name:  productionStageName
  value: 'Production' # Do not change stage name value
- name:  productionStageEnvName
  value: '<TBD>'
- name:  productionStageVmImage
  value: '<TBD>'
# TODO Add your variables here
```

As a result, each time a new parameter is introduced, it necessitates an update to the [control template](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2/blob/eee9e2e895e8869e1f4fc8e7b55b1973b469351f/blueprints/__101__/azure-pipeline-__101__-control.yml) to incorporate and transmit the extra parameter. This process has proven to be exasperating, labor-intensive, prone to errors, and ultimately, not a sustainable approach. It is far from straightforward and, therefore, presents a significant challenge and **WASTE**.

---

# Exploring options

### YAML update August 13, 2013

Over the long weekend, I enjoyed a delightful blend of relaxation and productivity. In between moments of unwinding with videos and tending to our adorable 10-week-old Dachshund puppy, I found myself immersed in the world of re-coding our ```__101__``` blueprint templates. Little did I know that this seemingly innocent endeavor would lead me on a tumultuous journey of debugging challenges.

Azure DevOps YAML, unfortunately, proved to be an intricate maze to navigate. One perplexing discovery was that it steadfastly refuses to accommodate variables of the object type or arrays of objects. The reasoning behind this limitation remains elusive, but take my word for it – this kind of support is conspicuously absent and an area in the binary space that I will defer for another rainy day.

This experience has taught me that even in the realm of coding, surprises abound. Despite the setbacks, I'm determined to continue refining our blueprint templates and conquering the intricacies of Azure DevOps YAML. Who knows what other insights and discoveries await as I press on with determination?

> 
> **LEARNING 1** - Defining YAML objects or array of objects as variables in an Azure Pipeline variable template is a no-go! You can do it with parameters, not variables.
>

### YAML update August 14, 2023

Following yet another early morning coding expedition and a debugging session that spanned the lunchtime hours, I made a pivotal decision. I opted to roll back our variable template to its simpler form, opting for straightforward variables. To address the array of objects within objects, I ingeniously integrated them as parameters within the control template. While this solution may not epitomize perfection, it undoubtedly provided a remedy for the crash debacle that had marred the weekend.

> 
> **LEARNING 2** - Simplify in small steps, not in a big bang. Otherwise you may embrace lots of debugging and unwinding of code changes.
>

Moreover, the ripple effect of this adjustment extended its benefits to the Continuous Deployment (CD) stage templates. Looking ahead, this approach promises to streamline the Infrastructure as Code (IaC) stage templates as well. These incremental strides within the realm of YAML Pipelines might seem small in scale, yet they represent a significant leap forward for our blueprint endeavors.

Initiating the submission of a draft pull request, I now find myself in a state of anticipation, eagerly awaiting the candid feedback of my colleagues. The outcome holds the promise of insights that will undoubtedly enrich the project and refine its trajectory q;-)

### YAML update August 15, 2023

<TBD>

---

# Revision of the proposed solution
### Changes in our ```__101__``` *-**control**.yml template

<TBD>

### Changes in our ```__101__``` *-**cd**.yml template

<TBD>

### Changes in our ```__101__``` *-**cd-stage**.yml template

<TBD> 

# What is the impact on our open-source project?

<IMPACT ON OSS>

---

<CLOSE - SUMMARY >


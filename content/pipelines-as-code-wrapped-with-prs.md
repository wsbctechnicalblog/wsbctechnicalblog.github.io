Title: Pipeline-as-code wrapped with Pull Requests
Date: 2021-03-13
Category: Posts
Tags: Azure-Pipelines, DevOps, IaC
Slug: pipelines-as-code-pr
Author: Willy-Peter Schaub
Summary: @@TBD@@

@TBD@

# Pipelines-as-code ... what?

@TBD@

The pipelines as code technique emphasizes that the configuration of delivery pipelines that build, test and deploy our applications or infrastructure should be treated as code; they should be placed under source control and modularized in reusable components with automated testing and deployment. As organizations move to decentralized autonomous teams building microservices or micro frontends, the need for engineering practices in managing pipelines as code increases to keep building and deploying software consistent within the organization. 

Infrastructure as code (IaC) is the process of managing and provisioning computer data centers through machine-readable definition files, rather than physical hardware configuration or interactive configuration tools.

---

# Benefit #1 - Transparency

@TBD@

---

# Benefit #2 - Everyone can contribute

@TBD@

---

# Benefit #3 - Automation

@TBD@

Engineering Practices

This need has given rise to delivery pipeline templates and tooling that enable a standardized way to build and deploy services and applications. Such tools use the declarative delivery pipelines of applications, adopting a pipeline blueprint to execute the underlying tasks for various stages of a delivery lifecycle such as build, test and deployment; and they abstract away implementation details.

Self-service automation

A self-service kiosk is an interactive terminal that facilitates an action or displays a piece of information and automate, eliminate or streamline wait or cost by giving customers the control to get things done on their own terms.

---

# Benefit #4 - Focus engineering on business code

@TBD@

Azure Function = 300 lines of pipeline code
Generic Blueprint-based = 122 lines of code
App-Type Blueprint-based = 28 lines of code - difference of 272 lines of code - 927 pipelines * 272 = 252,144 lines of code

> 927 pipelines * 272 pipeline code = 252,144 minimal business value lines of code
>
> ![WASTE](/images/pipelines-as-code-wrapped-with-prs-1.png)

---

# Wrap-up

@TBD@

You can continue to build your own pipelines, tinker with knobs, dials, configurations and products, and remember to innovate all pipelines continuously - do-it-yourself (DIY). Alternatively, you can focus on your business code and let the pipeline engineers focus on your pipelines - pipelines-as-a-service. The choice is **yours**. 


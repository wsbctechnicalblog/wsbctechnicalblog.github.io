Title: Back to Basics: Open Source Software (OSS)
Date: 2024-02-XX
Category: Posts 
Tags: azure-devops, pipelines, oss, engineering
Slug: back-to-basics-oss
Author: Willy-Peter Schaub
Summary: Raising awareness of our open-source projects for knowledge sharing.

Our open-source software (OSS) projects, [wsbctechnicalblog](https://github.com/wsbctechnicalblog/wsbctechnicalblog.github.io), [Azure DevOps Automation Pipeline Templates](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2), and [Technology Framework Monitor](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Technology-Framework-Monitor), are readily available on GitHub, and we are committed to their ongoing development whenever time and opportunities allow. The first OSS project and the most evident is our technical blog, serving as a platform where we share fundamental principles, insights, and advanced knowledge gathered throughout our bits and bytes journeys. We share whatever we feel is important to our fellow Agile, DevOps, and Software Engineering communities, fostering collaboration and continual learning.

---

# Azure DevOps Automation Pipeline Templates

[Pipelines - Meet our second-generation app-type blueprints](https://wsbctechnicalblog.github.io/yaml-pipelines-part10.html) touches on the core rationale behind our investment in this OSS project. When tasked with creating a continuous delivery pipeline, soliciting input from 13 software engineers is akin to inviting a multitude of perspectives, potentially resulting in more than 13 different approaches. While this diversity underscores autonomy and fosters innovation, it can inadvertently divert our delivery teams from their primary obligation of consistently delivering functional code and value. 

>
> ![Pipeline status](/images/back-to-basics-oss-1.png)
>

Moreover, the drift and sprawl of pipeline configuration snowflakes complicates reuse and inflates support and maintenance overheads and cost of ownership. Analogous to architectural blueprints, our standardized pipeline templates — both generic and application-specific — facilitate the swift and uniform creation of countless delivery pipelines. This approach champions:

- **Consistency**: Using predefined pipeline templates, we ensure uniformity across our delivery processes. This consistency minimizes errors and discrepancies, fostering predictability and reliability in our software delivery lifecycle.
- **Standardization**: Standardized pipeline blueprints establish a common framework for development teams to follow. This alignment streamlines collaboration, simplifies onboarding of new team members, and enhances overall efficiency by reducing the need for custom solutions.
- **Self-Service Automation**: Using predefined pipeline templates empower us to create and delivery software development lifecycle [Azure Repos](https://learn.microsoft.com/en-us/azure/devops/repos/?view=azure-devops) and [Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/?view=azure-devops). Using self-service automation, teams can rapidly iterate on their development environment, reducing dependency on centralized resources and accelerating time to market.
- **Security**: By integrating security best practices into our pipeline blueprints, we embed security measures directly into the software delivery process. This proactive approach helps identify and mitigate security vulnerabilities early in the development cycle, enhancing the overall resilience and robustness of our applications.

>
> ![Callout](/images/back-to-basics-batch-size-alert.png)
>
> **EXPLORE** our [Application-type CI/CD blueprint template](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Automation.Pipeline.Templates.v2) OSS project, collaborate, and continuously improve the templates with us. 
>

To get an insight into WHY we engineered these blueprints, HOW they evolved, and HOW we use them, please refer to the [Part 1: Pipelines - Why bother and what are our nightmares and options?](/why-pipelines-part1.html) series. We are also working on a v2 blueprint cookbook, which we may self-publish this year - watch this space.

---

# Technology Framework Monitor (TFM)

The Technology Framework Monitor project is a side project by [Andreas Mertens](TBD), who wanted to help us find out the use of outdated versions of .NET that are used by solutions in hundreds of Azure Repos. The TFM product will go through and collect information on every project in an Azure Developer Operations organization, or repository, check the files inside, and then save the data collected into a Microsoft Standard Query Language (SQL server database.

Some features of the TFM product are to do a scan that will go through projects with different file extensions, get a file list, and store information in the SQL database. The file list information gathered can include which .NET version, .nuget package versions, npm package versions and more depending on the configuration settings. The data being published is stored in the SQL server database for analysis and reporting purposes.

>
> ![TFM Observation](/images/back-to-basics-oss-2.png)
>

In 2023, we were lucky to work with Andreas and two BCIT students, Daniel Chellapan and [Samuel Tjahjadi]( https://www.linkedin.com/in/samuel-tjahjadi-952b03205/), on a special project to refactor and open-source the project, once again sharing our learnings and an OSS solution that serves as a pivotal tool to address several critical issues within software development, including:

- **Outdated Products**: Identify and flag end-of-life (EoL) technologies, such as out of support versions of .NET, across various solutions stored in Azure Repositories. By pinpointing these outdated products, development teams can prioritize updates and ensure they are leveraging the latest features, performance enhancements, and security patches.
- **Technical Debt**: Detection of technical debt allows teams to identify areas where shortcuts or temporary solutions have been implemented, leading to increased complexity and maintenance overhead. Addressing technical debt early helps prevent future development bottlenecks and ensures the long-term sustainability of software systems.
- **Poor Software Development Practices**: Through its scanning capabilities, TFM sheds light on poor software development practices, such as inconsistent naming conventions, out-of-support dependencies, and unhealthy branching strategies. By surfacing these practices, teams can implement corrective measures, enforce coding standards, and foster a culture of continuous improvement, ultimately leading to higher-quality software products.

>
> ![Callout](/images/back-to-basics-batch-size-alert.png)
>
> **EXPLORE** our [Technology Framework Monitor](https://github.com/WorkSafeBC-Common-Engineering/AzureDevOps.Technology-Framework-Monitor) OSS project, collaborate, and continuously improve the templates with us. 
>

Since then, we have to keep telling Andreas to add a technical enabler card to our team’s backlog, as he explores more innovations to improve the product, our software development lifecycle, and automation of technical debt. There is a plethora of fantastic ideas for enhancing TFM (Technology Framework Monitor). I will take a pause here and pass the baton over to Andreas to delve into these potential improvements further.

---

Handing over to [Andreas Mertens](TBD), who will start blogging on this blog on these open source topics. He will lift and explore the bits and bytes under the bonnet! 
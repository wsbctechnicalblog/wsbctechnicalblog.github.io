Title: Improving DORA metrics
Date: 2022-04-29 13:13
Category: Posts
Tags: devops, metrics, eliminate-waste
Slug: improving-dora-metrics
Author: Shay Vannery
Summary: We would like to plan how to track and empower engineering to increase deployment frequency, and reduce lead time for change, MTTR, and change failure rates.

Streamlining software delivery can seem deceptively simple. Technology consultants (like myself) are quick to tout the trending new tool or methodology that can magically solve all of an organization’s woes. Though tools, automations and practices can help to a large extent, there is no alternative to holistically and critically examining one’s own organizational practices and value streams.

---

# 1.0 Map the value stream for each application

A **value stream** is the set of actions that take place to add value to a customer from the initial request through realization of value by the customer.

Every organization has a somewhat unique set of actions that must occur to get a user story from the Ideation phase into the hands of the end-user. This value stream has likely been developed over many years, by several groups of people with differing priorities. It is imperative to examine said value stream periodically to ensure it is free of redundancies; and updated to better fit present-day organizational priorities and goals.

> **Bonus Tip** 
>
> Applications come in different shapes, sizes and forms. It is worthwhile to re-examine your value streams on an application/ component level; as what works for a highly-visible, complex end-user facing application might be overkill for a simpler, back-end service or job.

---

# 2.0 Measure baseline metrics for each application & set SMART goals

**What is not measured, cannot be improved.** What is not improved, is always degraded.

Before embarking upon an improvement journey, it is critical to examine where we currently stand. The purpose of this baselining activity is to assess current levels, and to be able to articulate where we’re headed; with real quantitative data.  Enthusiastic teams have a tendency to aspire for grandiose goals like “Zero defects in Production”. Though admirable; it is best to set goals that are Specific, Measurable, Achievable, Realistic and Time-bound at this stage.

---

# 3.0 Analyze commonalities and patterns

Real data obtained from steps 1.0 and 2.0 above will undoubtedly reveal commonalities and patterns. Some of these may have been obvious; but now we have proof and can make decisions driven by data. This data can help identify bottlenecks and repetitive manual tasks ripe for automation. Such an approach will ensure maximum return on investment.

---

# 4.0 Identifying barriers

Now, let’s assume that the organization has bought into the efficacy of DORA metrics; and the teams consider it a worthwhile endeavor to try and improve upon them. 
Each organization and each team must ask themselves some questions. These are just indicative examples:

## 4.1 Deployment Frequency

Increasing deployment frequency has its benefits. Teams deploying changes to Production frequently stand to benefit from quicker end-user feedback, quicker detection of bugs and defects, fewer conflicts, and easier recovery from unintended consequences. Reducing batch sizes is the easiest way teams can achieve more frequent deployments. However, this might not be a viable option for (say) monolithic legacy applications. Answering some of these questions could likely reveal the path to increasing deployment frequency:

1. Are we slicing feature stories finely enough? Can we slice them finer?
2. Are there application architecture constraints?
3. Are there infrastructure/ test environment constraints? 
4. Are there resource/ staffing constraints?
5. Is there a lot of rework happening? Why?
6. Any external factors?

Deployment Frequency is by far the easiest metric to measure. This information could be gathered manually at the team level, or in an automated fashion from the deployment pipeline. Task tracking tools like JIRA or Azure Boards have effective tagging, filtering and reporting mechanisms to simplify gathering and disseminating this metric at scale. 

## 4.2 Lead time for change

There are different ways to scope lead time for change. For the sake of this conversation; let’s assume lead time begins the moment a developer starts working on a change; and ends the moment the change is available to an end-user. Reducing lead time allows an organization to pivot quickly, and act upon changing requirements with agility. Answering some of these questions could help identify barriers to reduce lead times:

1. See 4.1.2 & 4.1.3. (architecture/ infrastructure constraints)
2. Is the DEV/TEST methodology conducive to quick lead times?
3. Is the delivery pipeline automated? Are there further opportunities to automate?
4. Are there redundancies in the pipeline?

Change Lead time can be tracked manually at the team level. It can also be broadly measured with the help of the deployment pipeline. If set up correctly, the deployment pipeline can also provide deeper and more granular insights into the lead times at various pipeline stages. 

## 4.3 Change Failure Rate (CFR)

Change failure rate is the percentage of deployments that lead to downtime, or serious issues in a given time period. The definition of “failure” may vary from team to team. For the sake of this conversation, let’s assume a failed deployment refers to a deployment that had to be rolled back from production, or required a hotfix to resolve a high-severity incident. Though it is easy to guess root cause of failures by relying on anecdotal evidence or gut-feel, it is best to make improvements by asking questions like:

1. Are testing best practices consistently followed across the SDLC?
2. Are test cases comprehensive enough to detect issues in lower environments?
3. Are lower environments similar enough to production to allow for reliable test results? 

Depending on how a rollback is initiated, Change Failure Rate can potentially be tracked at the repository level. This would require each hotfix/ remediation build to be labelled as such in (say) GitHub. However, if the rollback protocol is not managed via the deployment pipeline, or if the failure is remediated using a manual hotfix; service management tools like ServiceNow can help record and measure CFR. 
  
## 4.4 Mean Time To Recovery (MTTR)

Mean time to Recovery or Mean time to Resolution is the average amount of time required to recover from a failure. For the sake of continuity; let’s define failure as explained in 4.3 (CFR). If the application requires high-availability and high-resiliency, MTTR becomes the most important metric to track and improve. Answering some of these questions could help identify barriers to improving MTTR:

1. How are issues (errors/ defects/ outages) detected today?
2. How are incidents routed to the appropriate resolution teams?
3. Do development teams have expected Service Levels objectives and indicators codified?
4. Are resolution teams aware of the mitigation protocol?
5. Are resolution teams empowered to resolve issues and make quick decisions?

Similar to Change Failure Rate, MTTR can be complex to measure. At the risk of oversimplifying this nuanced process, teams may rely on monitoring and observability platforms to capture the start and end times of an incident. Depending on the nature of the issues; Application Insights within Azure Monitor or even PagerDuty can be leveraged to measure MTTR. 

---

# 5.0 Prioritize and eliminate barriers

As a proponent of a data-driven decision making culture, I have avoided prescriptive approaches to improving DORA metrics. It is best to contemplate the barriers on a team level, or better still, an application level; and focus on dismantling these barriers in a methodical and purposeful way guided by priority and return on investment. 

That said, most of the identified barriers can likely be classified into the following categories (in order of difficulty):

1. Skill/Knowledge constraints
2. Process constraints
3. Budgetary constraints
4. Architecture/ Infrastructure limitations

---

# 6.0 Conclusion

It is likely that some of the barriers we encountered can be eliminated by coaching team members on existing organizational protocols and widely accepted engineering best practices around development, testing, deployment, monitoring, error detection and mitigation. Communities of Practice must make contin (this sentence appears incomplete)

If it emerges that changes to processes are required, these changes must be meticulously recorded, observed and measured as an experiment. The results must be peer reviewed and widely distributed within the organization, so as to foster a culture of experimentation and continuous improvement.

Organizations must examine time and investment budgets and ensure there are appropriate allocations for learning, experimentation, knowledge sharing and technical debt. If required, monolithic applications must be pared down and eventually replaced with micro-services that are conducive to modern-day technological advances. It is now possible to achieve levels of uptime and resiliency that were unheard of even 5 years ago. Let’s work together to ask questions, celebrate successes and failures alike, and continue to deliver exceptional value to our end users on time, every time.

---

**Related References**

- [2021 Accelerate State of DevOps report addresses burnout, team performance](https://cloud.google.com/blog/products/devops-sre/announcing-dora-2021-accelerate-state-of-devops-report)
- [Metrics importance](/metrics-importance.html)

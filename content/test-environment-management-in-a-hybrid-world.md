Title: Test Environment Management in a hybrid world
Date: 2022-10-12
Category: Posts 
Tags: engineering, testing, release
Slug: test-environment-management-in-a-hybrid-world
Author: Shay Vannery
Summary: Test Environments are a critical component of any software development lifecycle.

 Correctly configured test environments can help detect bugs, errors & other issues early in a controlled setting; saving the development team time, effort, money and stress. And yet, test environments are often an after-thought. 

# Problems with Test Environment Management

Traditional test environment management is a cumbersome and labor-intensive process. In an organization with a complex technological landscape, this means keeping track of hundreds of applications, related configurations and attributes in complex spreadsheets. 

As static environments are dependent upon humans for upkeep & maintenance, these environments become inconsistent over time leading to less reliable test results. This sometimes leads to bugs & errors escaping to the Production environment undetected, despite running a battery of tests. Misconfigured environments also make it difficult to troubleshoot and pinpoint the source of bugs and errors. 

In complex organizations like ours, test environments are a shared resource; and can become a bottleneck. As specific applications and tests may require specific environment configurations, teams sometimes have to wait for test environments to become available. This unfortunately causes delays to program delivery or to teams skipping critical SDLC stages. Shared test environments usually have access and permission gates to ensure environment sanctity, but this further slows down the delivery cadence due to the added overhead of coordination, communication & compliance tracking. 

As we continue along our Cloud journey, we are becoming less and less dependent on physical, static environments that we have to maintain and manage. It is now possible to have entirely “ephemeral” short-lived environments that are instantly generated with specific code, configuration and conditions required for a specific purpose; and destroyed once the purpose is served. 

# Ephemeral Environments

An ephemeral environment is just a virtual replica of an environment. Infrastructure-as-Code (IaC) makes it possible to make environment creation an automated stage in a pipeline. For instance, an environment can be created with specific configurations, and specific test-data, triggered by a pull request. This environment can be staged and shared with other stakeholders like business/ UAT teams as desired, and destroyed once the tests have run successfully. This theoretically enables teams to have an infinite number of environments running in parallel, thereby eliminating the need for manual environment coordination, tracking & booking. Parallel independent test environments also enable us to eliminate access gates & manual approvals entirely; thereby speeding up program delivery. 

Since environments can be configured for any purpose, separate environments can be configured for QA tests, integration tests, load and performance tests, training, staging etc. in parallel as and when needed; we have the opportunity to sharply pare down a lengthy software development life cycle that runs in series due to infrastructure limitations.

Ephemeral environments can also save an organization money, as the “environments” can be “turned off” when computing resources are not being utilized.

# Configuration Management Database (CMDB)

In an ephemeral world, the importance of maintaining a single-source-of-truth increases even further. A purpose driven environment is only useful if it is correctly configured with the appropriate attributes and conditions. Most configuration management databases are just glorified spreadsheets; just as reliant upon manual upkeep and intervention. They are error-prone, difficult to scale and must be reviewed for consistency and accuracy. For a CMDB to be truly effective, it necessitates constant and ideally automated updates. Modern CMDB tools enable configuration changes to be automatically discovered and tracked across on premise servers and cloud infrastructure using scheduled scans.  

# Conclusion

Test Environment Management is a critical component of modern day software delivery. If leveraged properly, using a combination of modern tools and the right processes, it can make a considerable difference in the quality and efficiency of the delivery life cycle. 


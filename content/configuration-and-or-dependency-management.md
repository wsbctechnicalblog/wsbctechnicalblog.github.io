Title: Configuration and/or Dependency Management
Date: 2023-05-26
Category: Posts 
Tags: engineering
Slug: configuration-and-or-dependency-management
Author: Willy-Peter Schaub
Summary: What am I missing? Is this not a common dependency challenge?

I do not have experience in this area and am slowly, but surely, losing my marbles as no-one seems to have an answer.

---

# System Center Configuration Manager  to the rescue ... or not?

Yes, we are using System Center Configuration Manager, to report on the health of our virtual servers, installed products, and missed patches. In essence, we know exactly WHAT is installed and WHAT is vulnerable - that is a goo thing, no?

> ![Installed applications](../images/configuration-and-or-dependency-management-1.png) 

# Team Framework Monitor

We have also developed a tool, called Team Framework Monitor (TFM), which we recently open-sourced. See [TBD](/TBD) for details. Using the tool, we regularly scan all our [Azure DevOps](TBD) repositories to produce a report of applications, their dependencies, and whether any of their dependencies are end-of-live (EOL) - another precious gem, no?

> ![Application codebase](../images/configuration-and-or-dependency-management-2.png) 

# Dependency Management Dilemma

> ![The challenge](../images/configuration-and-or-dependency-management-3.png)

---

How are YOU solving this challenge? Do you have any case studies of organizations that have mastered this challenge?

Comment below and let us start an interesting discussion!


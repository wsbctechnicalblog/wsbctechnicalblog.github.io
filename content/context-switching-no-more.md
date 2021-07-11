Title: Stop the context switching, reduce waste, and focus on value
Date: 2021-07-11
Category: Posts
Tags: learning, tips
Slug: context-switching-no-more
Author: Willy-Peter Schaub
Summary: A work-life balance is important, however, I believe that stopping waste and focusing on value is just as pivotal!

I start working on an automation script. It has a purpose, I am starting to master my PowerShell skills, and my brain is thriving on autonomy. A pop-up on Microsoft Teams catches my attention, as three more email notifications pop-up. The phone rings ... someone's hair is on fire. I remember that I promised my colleague to send a summary of the recent 80-days worth of Application Insights data, just as I get pulled into a meeting ad short notice and without any context.

> ![Stress](/images/context-switching-no-more-1.png)

Can you visualize yourself in this situation? Do you realise that there were six (6) context switches in the previous (nd short) paragraph?

When the binary dust settles, I often cannot remember where it all started, what I was working on, and why. Loss of **focus**, **quality**, and **mastery** - **STOP**!

---

# Context Switch

If you know the basic processor architecture and have a knowledge of assembler, you will understand that a context switch is not trivial.

The currently executing process registers, program counters, and operating system data are saved, a new process is scheduled and starts executing. Or in pseudocode:

- movel: copy arguments from stack to mewmory
- pushl: Save registers (edp, ebc, esi, edi, ...)
- movel: Switch stacks
- popl: load new registers

A context is the contents of a CPU's registers and program counter at any point in time. Context switching can happen due to the following reasons: When a process of high priority comes in the ready state. In this case, the execution of the running process should be stopped and the higher priority process should be given the CPU for execution.

In a switch, the state of the process currently executing must be saved somehow, so that when it is rescheduled, this state can be restored.

---

# Stop Waste, focus on Value

## EMail Recommendations

## Phone Recommendations

## Meeting Recommendations

---

X


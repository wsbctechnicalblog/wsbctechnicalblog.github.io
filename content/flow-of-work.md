Title: Systems thinking and the flow of work
Date: 2021-12-15
Category: Posts
Tags: quality, technical-excellence, estimates
Slug: flow-of-work
Author: Alex Bunardzic
Summary: Speeding up software development may not speed up the delivery

![Yoda](../images/yoda.png)

_Everyone is busy and yet few things are ever finished._ -Anonymous

Delivery of the planned workload often appears unpredictable. Let’s examine what processes contribute to that lack of reliable predictability.

## How reliable are the estimates?

If the expected delivery fails to materialize, usually the first suspect is poor estimates. If the team bids on a certain feature and estimates it at one timeboxed cycle (i.e., one iteration), but the feature gets delivered after three or four iterations, the team’s ability to accurately estimate is placed under suspicion.

However, the team is only one component of a larger system, and the delivery workflow travels throughout the entire system. A team cannot reliably predict how will the workflow get processed throughout the system.

A larger, more holistic system view is needed if we are to understand the overall delivery process. Without gaining such insights, we will continue to be somewhat mystified why is our workflow slow and unpredictable.

## Ask developers to work faster

Because of the lack of the insight into the overall working of the entire system, the bottlenecks may get wrongly identified. What we see typically happen is development gets erroneously perceived as the bottleneck. The slowness of delivery gets attributed to the pace of software development. Management attempts to address these ‘bottlenecks’ by either hiring more staff, or by purchasing more advanced tools, or by retraining the staff, or the combination thereof.

What that amounts to is basically asking software development staff to work faster. The thinking is that if the developers were to pick up the speed by certain level of magnitude (say, by 50%), then the value delivery will improve in speed by 50%.

A good time to take a closer look into this line of reasoning.

## Software delivery queues

Software development is always done in isolation. The reason is that changes done to the software code are always assumed to be somewhat faulty. It is much more likely that a change made to the source code is less than optimal. Because of that, we instigate processes in the form of delivery queues. These queues/quality gates are created to make sure software does not get released without inspection.

Queues are, by their very nature, speed bumps. Their only job is to slow down the delivery.

Why the need to slow down? As mentioned, we don’t trust raw changes to the software, and thus enforce points of inspection.

## Software delivery loops

Putting speed bumps on the road to releasing software improves our chances of delivering quality products. However, to blindly assume a happy path and smooth sailing, where all changes get carefully inspected and vetted by the gatekeepers, would be overly optimistic and naïve. More likely than not, the inspection will catch some issues with the proposed changes. When that happens, the proposed change gets sent back to authors. This sendoff then creates a loop.

It would also be overly optimistic to assume that it’s always a single loop. Not every request for a fix gets done to the gatekeepers’ satisfaction. We often see the loop (i.e., back to the authors) occur more than once. Try again!

## Queues and loops eat up the cycles

The inspection process is never instantaneous. When the requested change arrives at the inspection queue, it is extremely unlikely that the gatekeepers responsible for inspecting the change are immediately available to look at it. They’re busy servicing other requests. The newly arrived change request must “take a number” and then wait in the queue for the number to be called.

How long will the wait be? There is no definitive, precise answer to that question. It depends on many things, most of them completely unpredictable.

The team who is planning to release their changes is now forced to leave their changes alone; they then either start idling (which causes the management to frown – low utilization rates), or they get to work on something else. The wait time spent in the queue is wasting precious cycles. Not only are the teams waiting, but customers are also waiting for the new functionality/feature/fix.

What happens when the gatekeepers finally get to work on the request? They will spend some time examining it, and that time could be substantial. The outcome could be positive (i.e., everything a-okay, go to the next gated phase), or negative (i.e., “we found a defect, sending it back to the team who authored it and now need to fix it”).

Now we have a loop. The team who authored the defect receives the request for fixing it, and places it on their queue (“take a number”). Since they are busy working on something else, the request needs to wait for the team to free up their time and attend to it.

How long is that wait time going to be? There is no definitive, precise answer. It depends on many things, many of those things also unpredictable.

## Will speeding up the development make a significant impact?

If we were to trace the time spent on handoffs (i.e., idling in the queue, waiting for the next available inspectors, reassigning the team to work on something else while they’re waiting) as well as trace the time spent on examining/inspecting the change, plus the time spent on looping back with requests to fix the discovered issues, we will notice that it tends to be of a higher order of magnitude larger compared to the time spent developing software.

Since any time spent waiting in the queue is unproductive time, we should go ahead and label it as waste (waste of time). Waste is to be avoided, however in the current model of software development process, such waste seems unavoidable. Our challenge then is to try to reduce it. Reduce the unproductive time.

The added stress caused by this mode of working causes another waste – cognitive dissonance that arises from the frequent context switching. The flow of the work gets interrupted, teams get frustrated, customers place additional pressure by complaining about the sluggish speed of delivery.

Is it possible to speed up the development process? Definitely – there is always room for improvement. But is that going to make a significant dent in the overall speed of delivery? Probably not.

The real improvement will happen when we focus on reducing the unproductive idling. Instead of investing time and effort in finding ways to speed up the development, it may be better to work on reducing the queue wait time, eliminating the loops, and minimizing the context switching stress.

Once we remedy the queuing, inspecting, and looping time waste, speeding up the development process will start showing significant improvements. But not before the remedial intervention.

## Would more precise estimating help?

The assumption that every development task can be precisely estimated still leaves the problem of unpredictable idling time caused by queues and loops. As we’ve seen, the grand total time spent on making the change and then seeing that change in production is quite unpredictable. It doesn’t really help knowing how long predictable activities will take if we have no way of knowing how long unpredictable activities will take.

## What is the solution?

The only plausible solution to this challenge is to strive to reduce, minimize, or even eliminate queues and loops. If we get to the point where we do not need handoffs, there would be no need for queues caused by asynchronous inspection. Once that happens, estimating individual software development tasks will make more sense, as it will offer closer approximation of the delivery time.
Title: The problem with big batches
Date: 2022-01-11
Category: Posts
Tags: quality, eliminate-waste, agile, devops, no-estimates
Slug: the-problem-with-big-batches
Author: Alex Bunardzic
Summary: Improve the predictability of delivering business value by reducing the utilization rates

![Big batch](../images/batch.png)

**Note:** This article is largely a summary of the [brilliant thread](https://twitter.com/d_stepanovic/status/1480941814895063045) by [Dragan Stepanovic](https://twitter.com/d_stepanovic)

We are learning how to transform organizational culture from focusing on measuring and tracking **outputs** to focusing on measuring and tracking **outcomes**. Immature practices tend to focus on measuring and tracking outputs for the simple reason that outputs are much easier to measure and track. Traveling along the trajectory of the least resistance, our need to **reduce uncertainties** and **increase predictability** is leading us to latch onto whatever is immediately available for measuring and tracking.

However, we slowly but surely learn that outputs almost never correlate to or map on to outcomes. For example, if we are measuring and tracking number of lines of code that a software development team produces in a unit of time, we will have hard time proving that the more lines of code the team produces, the better the outcomes.

Similar reasoning applies to measuring and tracking number of work items completed, number of user story points delivered, number of stories closed, number of features shipped, and so on.

If we agree that outcomes matter far more than outputs, we are faced with the challenge: how do we measure outcomes?

## Business value

A useful **Key Performance Indicator (KPI)** for measuring the outcomes is often referred to as **business value**. What is business value?

Maybe it’s easier to say what business value is not. For example, it is clearly obvious that number of lines of code produced in the unit of time cannot by any stretch of imagination be viewed as being business value. Same goes for number of work items completed, number of user story points completed, and so on.

Business value needs to be associated or correlated with measurable impacts. Such as, for example, improved customer satisfaction. Or increased revenue stream. Or improved profit margins. Or reduced cost of doing business. Or enhanced reputation on the market.

## Delivery of Business Value

Once we set our sights on delivering business value, we naturally strive to maximize the throughput of said value. If a little bit of business value is desirable, then naturally more business value is much more desirable.

Now, that way of thinking could turn into a slippery slope. And it all has to do with **batch sizes**. Humour me for a few moments.

Sizeable business value immediately suggests a big chunk of work. A big chunk of work immediately suggests big risk. But since we’re talking value, the risk may be worth taking, after all.

And so, we go back to the problem of increasing predictability. Predictability is tightly coupled with the uncertainty of “when will desired business value be delivered?” No one has the crystal ball, and since we live in the world riddled with **V**olatility, **U**ncertainty, **C**omplexity, and **A**mbiguity (**VUCA**), we know that predictability is a tricky proposition.

Knowing that, how do we commence work needed to deliver business value? We tend to **maximize resource utilization**.

Where is the problem in that? The problem is potentially twofold.

## Are big batches chockful of value?

One assumption when maximizing the business value is that loading up various features and functionality into a single batch means that we’re expecting customers to find everything we deliver in a big batch valuable.

That is a risky assumption. Without receiving customer feedback, we cannot be sure if the functionalities and features we delivered are being perceived as valuable by the customers.

And because customers will get presented with a big batch of changes, it will be difficult at that point to collect much needed, precise feedback. The change is overwhelming.

More likely than not, some of the features and functionality delivered in the big batch will not make any impact (some sources quote that around 60% of big batches contain dubious value, on average). Which, in the final analysis, reads as waste.

Not everything shipped in the big batch is going to be valuable to the customers. That being the case, why bother cramming so much assumed value in?

We may spend some time in our office daydreaming about the features and functionalities our customers may find valuable. But without shipping those hypothetical features and functionality into customers’ hands and collecting feedback from them, we have no way of knowing.

## Is high utilization rate the quickest way to deliver value?

It may make sense to organize the system in such a way that all resources at our disposal are utilized to the maximum. Never a dull moment may appear as the most prudent way to go. After all, we are employing top shelf experts and products, tools, and platforms. Why not take advantage of that phenomenal potential, and go full bore when creating business value?

That approach, as common-sense as it appears to be, poses certain challenges. The nature of work in a fully loaded organization is such that it results in a lot of **wait time**, instead of resulting in a lot of **work time**.

It is for that reason that it is not recommended to strive toward a fully loaded organization.

Value stream delivery crews quickly recognize this problem (too much idling time in a fully loaded organization). It is not difficult to spot long wait times. To deliver almost any change, the requesting teams are instructed to “take a number” and patiently wait for their number to be called.

Another problem with that arrangement is related to measuring and tracking. Most tools and practices are geared toward only measuring the **work time**. None of the existing processes seem keen on capturing and tracking **wait times**.

That bias gives a skewed perspective on how the work is progressing. In the end, the entire operation gets perceived as being **extremely unpredictable**, because wait times don’t prominently figure in the tracking reports. Everyone’s eyes seem to be glued to tracking the time spent working, not tracking time spent waiting.

We see that high utilization rates create a lot of speed bumps in the process (everyone is fully loaded; requests need to wait for their turn). Those speed bumps contribute to the unpredictability of the delivery. High utilization rates are not the best way for the quickest delivery of desired value.

## Dealing with unpredictability

Unpredictability of delivery is highly undesirable. How do we deal with that?

We ask people who work in a fully loaded system to give us **estimates**. The thinking is that precise estimates will enable us to better predict when will the desired business value be shipped to the customers.

When we ask for estimates, what we mean is estimates of **effort**, not of the wait time. However, seeing how unpredictable wait times are in a fully loaded system, estimates of effort cannot deliver any reasonable degree of predictability. We often hear “your guess is as good as mine” when asking some team to tell us when will the value be delivered. The team is not being difficult when they reply in that fashion; they are merely signaling the undeniable fact that wait times in a fully loaded system are grossly unpredictable.

And if we switch the focus and ask the teams to estimate the wait times instead of estimating the effort, that would be a losing proposition, because no one can estimate that with any degree of accuracy.

This impasse creates problems. We expect teams to provide estimates and in that way, we put them between the rock and the hard place. Teams know that, due to the nature of working in a fully loaded system, whatever estimate they come up with, will be incorrect. That knowledge damages psychological safety and erodes the trust in the organization.

Estimating the effort needed to deliver business value in a fully loaded system is therefore poor person’s attempt to achieve predictability and minimize/eliminate uncertainty. As such, it always delivers poor results.

## What’s the solution?

The only leverage point for reducing uncertainty and increasing predictability lies in **reducing the utilization rates** in the system.

What is achieved by reducing the utilization rates (i.e., by avoiding setting up a fully loaded system)? Reduction in the utilization rates increases the **flow through the system**.

How do we reduce the utilization rates? By reducing the batch sizes!

Instead of daydreaming of building and delivering a big splash product that will woo the market, it is advisable to switch focus on very small hypotheses. Each small hypothesis proposes hypothetical value that we can swiftly deliver, probe, and test on the market.

By following that model, we preempt the unpleasant question “when will it be done?” If we are releasing in very short bursts (almost daily), no one will have the time to stop and ask for estimates. Why? Because we’re too busy working, delivering value.
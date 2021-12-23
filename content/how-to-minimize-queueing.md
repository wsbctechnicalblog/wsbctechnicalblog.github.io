Title: How to minimize queueing
Date: 2021-12-23
Category: Posts
Tags: quality, technical-excellence, eliminate-waste, estimates
Slug: how-to-minimize-queueing
Author: Alex Bunardzic
Summary: Adopt the humble approach to only work in smallest possible batches with limited work-in-progress

![Queue](../images/queue.png)

In my previous post [Systems thinking and the flow of work](https://wsbctechnicalblog.github.io/flow-of-work.html), I tried to describe the sluggish/unpredictable software delivery caused by queueing and looping. Adding speed bumps introduces unwanted wait time that is exacerbated by frequent requests for retries. A gated phase, a quality inspection gate, often finds fault with proposed changes and asks the authoring team to try again. Those retries add significant amount of waste to the process.

How to avoid such unwanted delays? There are a few ideas that may help:

1. Insist on getting clear expectations
1. Insist on vertically slicing the expected delivery
1. Insisting on starting together, working together, finishing together
1. Insist on smallest possible batches

Let’s examine these ideas.

## Insist on getting clear expectations

While it may seem obvious that clear expectations are needed, every now and then we receive expectations that are somewhat muddled. By muddled I mean not carefully thought through. The rationale is that it is quicker to start building the hypothesized solution than it is to spend extra time hammering out the expectation.

The problem is that oftentimes it is a false math to assume so. Rushing to implement a half-baked expectation tends to result in bloat. We will see later in this article why is bloat extremely wasteful.

Another problem is that muddled expectation may send us off on a wild geese chase. I will use an example from my career to illustrate that pattern (names will be withheld to protect the innocent):

I was once consulting for a large organization whose Credit department was experiencing series of issues. To cut the long story short, that department somehow could not properly balance their books. The ledger was for some reason always off, and that was causing a lot of churn.

I did initial interview with stakeholders and was informed that the reason the processing in their department was often so wrong boiled down to inadequate software system they were using at that time, as well as down to staff errors – ‘fat fingers’ data entry mistakes and so on. They would like me to help them design better software solution that would preclude human data entry errors and also set the books straight.

Makes sense. So, I started drilling deeper into the business domain, to understand business policy rules and document the expectations with regards to various use cases.

That’s where the muddled expectations started entering the picture. I was getting several half-baked, imprecise use cases. Such muddled use cases could not be tested, and as such could not be automated.

Naturally, I pressed upon the stakeholders to provide me with clearer expectations. To which I started receiving annoyed responses, such as “I don’t know; you are the software developer, you figure it out!”

It was clear to me, at that point, that the entire project was a no go, and I gracefully bowed out.

Moral of the story – insisting on crisp and clear expectations is necessary. Without it, we cannot even know if it makes sense to continue being engaged on the project.

## Insist on vertically slicing the expected delivery

Once the expectation is clearly stated, it is important to abstain from overbidding. Instead of knee-jerk agreeing to implement the expectation as it is stated, it is more prudent to investigate the possibility of vertically slicing it. Commit to delivering the solution iteratively, rather than in one big fell swoop. Explain to the stakeholders that the intention is to engage them in swift and frequent delivery. Such approach is needed to gather quick and valuable feedback from them.

In my experience, stakeholders tend to appreciate such transparency and such proactive engagement. The upside is that it will give the delivery team much better chances of attaining predictive delivery of value.

## Insisting on starting together, working together, finishing together

Once the expectation has been vertically sliced, abstain from assigning individual tasks to individual team members and asking them to scatter and work in parallel, in isolation. Instead, attempt to start as a whole team. Look into the vertically sliced expectation, decide which aspect of the implementation is of the highest priority, then get together and start working on it as a team. Every member who has the so-called ‘skin in the game’ should be present from the get-go. This is important so that every member has a full understanding and a complete grasp of what is going on in the process of building.

Continue working in such fashion. The ideal model is synchronous collaboration, sometimes called ‘keyboardless programming’. In this mode of collaboration, decisions regarding the design of the system are made by team members who are **not** sitting at the keyboard. The implementation of those decisions is performed by the so-called “driver”. Another important aspect of such mode of working is **continuous rotation**; every 5 minutes or so, the driver gets up and joins the navigators, while someone else steps in and becomes the driver.

Eventually, the mob programming session described above reaches the stage where all team members agree that the solution has reached the “shippable state”. At that point, they finish together and move on to working on the next slice.

## Insist on smallest possible batches

The secret sauce to avoiding queuing and retries is in the art of crafting small batches. Let’s first define what is meant by ‘batch’:

A batch is defined as a group of items that move together from one step to the next step in the process.

What is meant by ‘item’? Typically, an item denotes a unit of change that affects the system. It could be a code diff or a configuration diff.

The more of these items (i.e., diffs) we bundle up and push into the integration and delivery workflow, the larger the batch we must deal with.

Consider a smallest possible batch: a single item comprising a single diff (such as, for example, a one-line correction in the code syntax). When such batch arrives for inspection, it is so light-footed and innocuous that it will be a breeze to approve.

Compare that with a large batch that contains hundreds of items, each item consisting of dozens or even hundreds of diffs. Obviously, when such bloated batch arrives at the inspection gate, it will cause a lot of consternation. And rightly so. Alarm bells go off, red flags are raised, and the inspection crew now need to roll up their sleeves and pour over the minutia of that batch. They now have their work cut out for them, and it may take days, even weeks, until the batch either gets cleared (“good to go to the next gated phase”) or gets sent back for a retry (“better luck next time!”).

And of course, such large batch necessitates long wait queuing times. While the inspection crew is heads down examining the bloated batch, nothing else is moving in the queue. We now have a serious bottleneck.

## Benefits of small batches

There are numerous benefits of working in small batches. Here I will quickly list some of them:

- Reduction in errors
- Faster feedback
- Reduction in deployment risk
- Increase in frequency of delivering customer value
- Reduction in mean time to recover in case of defects
- Improvement in psychological safety
​​​​​​​

Small batches introduce small, localized changes. That approach reduces the risk of damaging the system operations, as the small change is contained, and the blast radius is quite limited.

Customers also benefit as they get to enjoy the value sooner than they would if the teams worked with large batches.
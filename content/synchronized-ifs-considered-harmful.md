Title: Synchronized 'if' statements considered harmful
Date: 2021-04-08
Category: Posts
Tags: Extreme Programming
Slug: synchronized-if-statements-considered-harmful
Author: Alex Bunardzic
Summary: Duplicated imperative conditional logic leads to proliferation of bugs

[Edsger Dijkstra's](https://en.wikipedia.org/wiki/Edsger_W._Dijkstra) famous letter ["Go To Statement Considered Harmful"](https://dl.acm.org/doi/10.1145/362929.362947) was published 53 years ago in the March 1968 _Communications of the Association for Computing Machinery (ACM)_.

Today, no one uses **go to** statements anymore. The practice was proven harmful, and the pernicious **go** to statement was replaced by more appropriate statements as part of the structured programming vocabulary.

Upon closer inspection, though, it turns out that **go to** statement by itself is not that harmful, after all. It simply implements a jump from one statement in the code to another statement in the code. But, so do structured programming language constructs that replaced the **go** to statement. Statements such as **return**, **break**, **continue**. Those statements also implement a jump from one statement in the code to another statement in the code.

Knowing that, why did Dijkstra think **go to** was so harmful, while **return**/**break**/**continue** etc. aren’t harmful?

## Cognitive dissonance

What Dijkstra had noticed back in 1968 is the discrepancy between how we think and how computers work. We seem to focus most of our thinking toward orienting ourselves in space. We like to read and draw maps, and indicate things that are near or far, over here or over there, etc.

On the other hand, we don’t seem that well versed in thinking along temporal dimension. Time indicates change, and we mostly dislike change, as it threatens to unsettle us from our familiar comfort zones. We prefer spatial coordinates as they indicate something solid, firm, unchangeable, non-threatening.

Computers work in the exact opposite fashion. When a computer program runs, it unfolds in time. First this statement gets executed, then that statement, and so on. But these execution steps do not necessarily follow in linear fashion.

Still, when we read a source code that comprises a computer program, we reason in spatial terms. We start from the top of the page (or top of the screen) and then we parse the code-as-text one line at the time, going sequentially. Until we reach the end of the source code file.

Trouble is, that’s not how the program behaves. When a program runs, it makes all kinds of hyper-space leaps and bounds. It does not follow any neatly laid out spatial map.

Imagine a dancing competition where contestants would take snapshots of them dancing and would then send those snapshots to the jury. The jury would review the submitted snapshots and would then announce the winner of the dancing competition.

Or, imagine a cooking competition where contestants would take snapshots of them making food and would then send those snapshots to the jury. The jury would review the submitted snapshots and would then announce the best chef.

When we are reviewing a snapshot of the source code, we are equally reducing a very dynamic situation (i.e. a running program) to the set of static freeze-frame snapshots. It gives us a very unrealistic picture of how the program behaves and what is it capable of (this is especially obvious when we examine static snapshots of the code that is doing asynchronous processing).

## Go to is only harmful when combined with if statements

**Go to** statement by itself is no different than other control flow statements. It interrupts the linear flow (i.e. after executing current statement, it steps into the statement on the next line below). But so do other flow control statements that were introduced as part of structured programming with the intent to eliminate **go to** statements.

So, why is it then that Dijkstra considered **go to** harmful? The reason is that only when **go to** gets combined with **if** statements that we create a fertile breeding ground for bugs. For example, if we say:

```
if(orderTotal > 500.00 go to line 10)
```

that type of control flow has the potential to result in buggy code.

Without the conditional statement (the **if**) having a simple statement:

```
go to line 10
```

is not problematic. Why? Because it is not conditionally controlling the flow of execution. It is simply directing the flow without checking for any specific values.

Knowing this, one wonders why is it that Dijkstra did not declare **if** statements harmful? The reason is probably that back in 1968, Dijkstra was able to clearly define structured programming discipline, but he did not have the tools at his disposal that would enable him to define the discipline needed for removing the **if** statements. Back then, the concept of object programming was still nascent.

Today, we have well entrenched knowledge of object-oriented programming, and have great methodologies for replacing imperative **if** statements with more sophisticated code constructs.

## Business policy rules must be declared in very visible places

The most volatile (and most critical) parts of the app code are the parts that automate business policy rules. Those policy rules are governed by conditional logic (i.e. _if in this moment the state of the app is such-and-such, then the following expected transformation of values must occur_). Because business policy rules are in constant flux, teams are incessantly making changes to the already changed code.

It is those changes that offer the most fruitful opportunity for authoring bugs. What is the reason for this frequent bug authoring?

Most of the time the unwanted effects of the change to the code happen if the conditional logic is duplicated. The same logic gets implemented in more than one module/method. This duplication creates opportunities for missing or misplacing the necessary changes.

If we have implemented imperative conditional logic by using **if-else** statements in some module or method, chances are that there will be some other module or method where the exact same conditional logic will be needed. As the program runs, at various times it will need to make a processing decision based on that specific conditional logic.

The trouble begins when those varying modules and methods need to be maintained. The business policy rule has changed, and now our code must mirror that change. Being able to make the necessary change in all the affected methods and/or modules is often riskier than it may seem.

We often call these duplicate instances of conditional logic **synchronized ifs**. If one **if** statement needs to change, all other synchronized **if** statements must change at the same time. Which could quite often be a challenge.

We must therefore abandon synchronized **ifs** and abstract conditional logic away into a single source of truth. The trick is choosing proper abstraction to accomplish that task. Which is the topic for another blog post.
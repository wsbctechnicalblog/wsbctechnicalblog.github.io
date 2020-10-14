Title: The cost of avoiding change
Date: 2020-10-03 10:20
Category: Software, Change
Tags: TDD, CI
Slug: the-cost-of-avoiding-change
Author: Alex Bunardzic
Summary: Change is stressful and risky, but avoing it is even riskier

Software engineers are notorious for being averse to change. We prefer the steady state, stability. The reason we prefer steady state lies in the fact that systems we are building tend to be complex. Complexity breeds brittleness, and so we are keen on doing everything possible to avoid building brittle systems. Who could blame us?

## City on the Hill

When engineering a system, we tend to think about it in terms of an endpoint (let’s call that endpoint City on the Hill). This idealized city needs to be defined rigorously. After all, that’s what engineering is all about – rigor.

After we’ve defined it, we optimize the process of building it offline. Once it’s built, we confirm that it’s done (using our Definition of Done yardstick). We then push it online, move into it, and never change it again (if we need to make any changes, we’d be admitting that we haven’t defined it rigorously to begin with).

## Efficiency

The central idea of efficiency is that changing something is a waste. Why did we build the thing in the first place if we are to turn around and change it? Wouldn’t doing that mean that we didn’t actually know how to build our City on the Hill? Why not build our system correctly to begin with? Anything else would be grossly inefficient.

## Change is bad

According to the above reasoning, change is bad. It is wasteful and inefficient. Pushed to its limit, this ‘change is bad’ sentiment blossoms into full-blown ‘change is to be feared’ mindset.

Our City on the Hill ideal implies finality. Upon reaching our final destination, the reason to ever consider change is only if we realize that we have hit the wrong target. And that means utmost defeat (the ultimate inefficiency and waste).

## All complexity at the beginning and all reward at the end

The City on the Hill approach to software engineering makes our profession extremely hard. We frontload all the complexity at the very beginning of the project. We ‘kitchen sink’ the project: since we only get one shot to make it right, we’d better create a laundry list of all the features we will ever need.

Working on the detailed laundry list of all the features is a complex process. And it does not deliver any rewards. It may take days, weeks, even months to get to the end of job. And once we get there, we reap no rewards. All we have to show for is a pile of documents and diagrams – zero shippable software. The work on building shippable software has yet to commence. And it is only at the very end, once we ship the finished City on the Hill product, that we get any rewards for this gargantuan effort.

## Gold-plating the parts

The pressure of having only one shot at building our City on the Hill forces us to gold-plate all parts we’re building. We feel compelled to make each part better than it has to be in order to do its job. We are at that point playing the prediction game – maybe in the future this function will have to be integrated with another system, and because we won’t be making any changes to it later on, let’s make sure now it is sufficiently generalized. Or, add those bells and whistles that only one in thousand users ever notices, let alone makes any use of it.

## Fear of imperfections

The ‘kitchen sink’ laundry list of features, where each part must be gold-plated, results in code that is far more complex than it needs to be. That naturally leads to lack of understanding. Lack of understanding leads to lack of confidence. That lack of confidence makes development slower because of the looming finality – do it once and make sure you do it right!

Such attitude results in the fear of imperfection. The fear of being wrong tends to lead to paralysis. Suddenly, the stakes of any decision made by the engineers seem incredibly high. Trying things and experimenting is viewed as wasting precious time and resources.

## Death march

The finality of the City on the Hill approach leads to very late validation. By the time we catch any issues with our gold-plated parts and how they struggle to integrate, the goodwill has already been largely spent. All the hard work invested in taming considerable complexities rarely pays off if we adopt the ‘failure is not an option’ mentality.

We cannot confirm whether the code we’re building actually implements our City until all pieces are in. Five-to-midnight is the worst time to discover we have problems. That is the point of maximum stress, as we are on the collision course to our deadline.

## Break the workload into parallel chunks?

To avoid the looming death march described above, we often see workload being divided into independent chunks to be worked on in parallel. Sounds reasonable on the surface, until we take a closer look and factor-in the cost of control needed to coordinate and synchronize independent strains of work. Managing that kind of parallelism is a tall order. Out of sheer necessity, management introduces ‘wait states’ and ‘sync points’. The independent development suddenly ceases to be independent, as it must become strictly lockstep. Copious documents, emails, tickets and handoffs start proliferating, slowing everything down to a crawl.

## Rework Avoidance

Avoiding change leads to avoiding rework. Any attempt at making something must be done in such a way that there would never be any need for rework. Make it right from the get go, on the first attempt.

The cost of avoiding rework is best expressed in the cost of late failures. Those dreadful five-to-midnight failures are extremely costly; not only that, but they leave very little room for rework. By the time we realize that things are not gelling as expected, it is often too late for attempting any rework.

## Switch to partial delivery

In order to evade the exorbitant cost of rework avoidance, we must pivot and embrace change via partial delivery. Embracing change necessitates innovation, experimenting, trying things out. The only way to do that effectively is to cultivate the ‘fail early’ mindset. Failure is desirable because it prompts us to fix it while it is still easy to do so.

## Conclusion

Avoiding change, while very tempting and perfectly natural, usually ends up being very costly. Fear of failure is preventing innovation and experimentation by stifling change. The only way to avoid paying such exorbitant price is to embrace the change, embrace failure, but do it in an incremental fashion. Small steps, each one focused on partial delivery. That way, success is assured.
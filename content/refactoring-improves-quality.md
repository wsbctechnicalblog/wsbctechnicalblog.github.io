Title: Refactoring saves time and increases quality
Date: 2021-07-22
Category: Posts
Tags: agile, code, devops, learning, quality, eliminate-waste
Slug: refactoring-saves-time-and-increases-quaity
Author: Alex Bunardzic
Summary: Design is not a static construct, it evolves by refactoring as we keep changing the code

When creating an application, we feel a strong urge to envision a perfect design of the system we intend to build. After all, we have many decades of collective experience in designing systems, and why not leverage that vast body of knowledge?

That line of reasoning would work perfectly if the systems we’re building were confectionary products that are standardized and normalized. However, years of experience teach us that pretty much each and every system we’re building is somehow unique. Despite many attempts to standardize and normalize software applications, we haven’t seen much useful advances in that area.

It is for that reason that we cannot blindly apply previously successful designs to a new system we are building. It is more prudent to work on the design that emerges as we are creating software.
This is not to say that the initially envisioned ‘perfect’ design is a waste; it is a good guidepost, something to inform and guide our initial reasoning. But as we proceed with the building activities, we discover that the initial design quickly becomes obsolete.

## Why redesign?

Consider an example from nature: a caterpillar is perfectly designed to devour vast amounts of foliage. So, given such perfect design, why go for a redesign?

Well, eating vast amounts of foliage is sufficient for survival, but not sufficient for reproduction. There is a design flaw that got discovered in the ‘perfect’ design of a caterpillar.

To reproduce, a caterpillar must find a mate. And the only way a caterpillar could find a mate is if he refactors himself into a butterfly. A butterfly is designed to search the sky for others of his own species.

Any design, no matter how perfect it may appear to be, sooner or later must be redesigned. Technical term for that redesign in software is refactoring.

## What if we don’t refactor?

Teams often feel disdain toward refactoring because it eats up precious cycles. Wouldn’t it be more desirable to spend scarce time on building new useful features?

But that line of reasoning is false economy. Churning new features as if we’re following a construction/manufacturing model and producing widgets on an assembly line doesn’t work well in software development. We are better advised to follow knowledge/service ecology models. And those models differ significantly from the manufacturing model where once established patterns are reliably repeatable. In knowledge/service ecology models, experimentation is the key and reliably repeatable patterns are a rare exception, rather than a rule.

If we choose not to refactor, we quickly accumulate bad design. It doesn’t take long on a brand-new software development project to start noticing rapidly mounting redundancy. Code duplication is rampant, and that anti-pattern is a surefire signal that we are heading into a defect-and-malfunctioning territory. Before we know it, the precious time we have carved up for building new features gets completely eaten up by the time teams spend fighting fires. Not a good position to be in.

So, how to fight it? There is no other way to fight treacherous redundancy but by merciless refactoring.
Another bad smell on the rapidly advancing project is unused functionality. Seemingly innocuous, this ‘deadwood code’ is actually very dangerous because it slows teams down. Makes it difficult to separate signal from the noise. Refactoring is the only way to keep mounting deadwood code from sticking around. Getting rid of the unused code is one of the most important aspects of refactoring.

Designs quickly become obsolete under the pressure of newly discovered details that were unknown during the times the design was formulated. Any design, no matter how fit for purpose it may be, need to be constantly reviewed and rejuvenated.

Avoid needless clutter and complexity. Make sure that everything is expressed once and only once. It is not possible to ensure that principle if we’re not refactoring.

Refactoring is time well spent. Never postpone refactoring activities. Never project refactoring tasks for some time into the future. The time is now!


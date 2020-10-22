Title: Collective code ownership
Date: 2020-10-22 16:24
Category: Posts
Tags: DevOps, code
Slug: collective-code-ownership
Author: Alex Bunardzic
Summary: Teams share collective responsibility and therefore collectively own the code

_"In XP we don't do what we believe, we do what our measurements tell us.”_ Ron Jeffries

Value stream delivery is largely based on automating business processes. In order to continuously deliver value, businesses invest in functionality. DevOps engineers are largely responsible for implementing desired functionality.
So we see that functionality is an asset. Businesses are willing to invest heavily in optimizing that asset. And the way the asset (i.e. functionality) is delivered is via shipping code.

Now for the twist of lime: while functionality is obviously an asset, shipping code isn’t. Not only is shipping code not an asset, it is actually a liability. Once shipped, code needs constant babysitting. If code is not engineered properly, babysitting the shipped code may result in spiraling costs. No business will ever feel comfortable with such liability.

In Extreme Programming (XP) we have a slightly different mantra (that basically talks about the same equation): Code is nothing, stories are everything.

## Who does the code belong to?

In DevOps, code belongs to the product (i.e. a bundle of functionalities). Code never belongs to an individual engineer. Code may shortly belong to a project, but a product typically outlives any project, so it’s more accurate to say that code belongs to the product.
Collective ownership is often a counter-intuitive concept in software engineering, as it annuls the authorship. In traditional software development shops, workload is divvied up among engineers, and each engineer writes their own code in complete isolation. And because they write their own code, they are responsible for it, they own it, they run with it, they live and die by it.

In software development shops that have evolved from the traditional shops, workload is not compartmentalized into mini silos. No silos, no turfs, no fiefdoms. In such shops, workload is centered on user stories. And each user story belongs to the entire team. That way, we avoid painting ourselves in a corner by isolating engineers from each other and then having to herd cats (with all the frightening overhead of coordinating, overseeing, synchronizing, judging and implementing correctional actions).

And since each user story belongs to the team (i.e. there is no individual, named author of a user story), the code implementing that user story also belongs to the team. That way, there are no individual authors of any line of code, of any code statement.

## How does that work in daily practice?

Collective code ownership may play out in variety of scenarios:

1.	Engineers work in isolation
2.	Engineers engage in pair programming (each pair works in isolation)
3.	Engineers engage in mob programing

In case where engineers work in isolation (i.e. each engineers goes away and spends some time coding in complete isolation from the team), collective ownership manifests in the full freedom to access, open and modify any block of code in the product repo. There are no silos, no barriers – we are talking full blown open source paradigm.

In case of pair programming, similar concept applies: the repo is fully open for examination, modification and merging the changes. Same as an individual engineer doesn’t own any part of the code pulled from the repo, a pair of engineers also do not own any part of the code.
In case of mob programming, collaboration between engineers happens in real time. Coding happens in brief spurts (governed by the ‘musical chairs’ rotation where the person making the changes by typing and the person navigating the changes typically spend no more than 5 minutes per mini session). As the driver (i.e. person entering the changes) and the navigator (person, or persons instructing the driver) keep rotating, at the end of the coding session pretty much every team member has touched the code. Collectively, the team has made the most optimal decisions regarding which changes to the code to commit, push and merge to the trunk. Authorship becomes moot in such practice.

## What are the prerequisites of collective code ownership?

It may not be advisable to jump in head first into collective code ownership before establishing rules of the game. In a nutshell, here are the minimum requirements for teams to successfully engage in collective code ownership:

- The team has collectively created and agreed upon the coding standards
- The team is fully committed to using code management tool (git!)
- The team is doing full-on TDD, ideally also doing stringent mutation testing
- The team is using powerful IDE (Visual Studio or VS Code)
- The team is actively pursuing continuous integration (CI)

In addition to the above, it is important for all engineers on the team to agree to participate/contribute to the work needed to implement aspects of the functionality that may not be everyone’s area of interest. For example, a back-end engineer may not be interested in some front-end technologies, but is agreeable to participate and pick up some skills by working with domain experts on the team. Cross-training/cross-pollination goes a long way toward creating a highly performing team.

Collective code ownership works best for small size teams, famously described as “two pizzas teams”. Any team that cannot be fed with two pizzas brings along added complexity; the overhead needed for maintaining team cohesion may exceed the benefits of cultivating collective code ownership.

## Conclusion

DevOps software engineering discipline is founded on the team concept. A team is not a group. A team is based on the concept of collective responsibility. And since each team works with user stories and turns those stories into shipping code, team collectively owns user stories as well as the code that implements them.
In a healthy team, when something goes wrong it is never “I thought SHE was going to take care of that!” Rather, it is “What do we have to do to fix that/take care of that?”

<br /><br />
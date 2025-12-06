Title: From Continuous Delivery to Release on Demand
Date: 2025-12-12
Category: Posts 
Tags: engineering, feature-flags
Slug: back-to-basics-from-continuous-delivery-to-release-on-demand
Author: Willy-Peter Schaub
Summary: How to Hand Over the Release Steering Wheel to the business.

I have been thinking hard about our journey with continuous delivery. It really has been a solid ride. But now, here we are, standing on the edge of a whole new frontier: release on demand. This is more than just a technical change. It is a full-on cultural shift, and I am not joking. The question, simple as it is, packs a punch: Should we go for canary releases, release rings, and feature flags so that the business, not the engineers, holds the reins when it comes to making the call on when to release?

> ![Principles and Practices](../images/back-to-basics-from-continuous-delivery-to-release-on-demand-1.png) 

If you are wondering why I am a bit cautious, I reckon you should go back to those earlier pieces: [Rough Patch, by Brian Harry](https://devblogs.microsoft.com/bharry/a-rough-patch/), [Deploying new releases: Feature flags or rings?](https://opensource.com/article/18/2/feature-flags-ring-deployment-model), and [What's the cost of feature flags?](https://opensource.com/article/18/7/does-progressive-exposure-really-come-cost).

>
> **Feature flags are dead simple** – just a straightforward if/else statement, nothing fancy. But, managing and keeping those flags going over time, that is where the real fun starts, and to be honest, that is also where things can get a bit risky. It is not just about flipping a switch. It is about staying on top of all those little toggles, making sure you do not end up with a mess down the line. So, while the code itself is easy-peasy, the challenge really kicks in once you must track, clean up, and make sure your flags do not trip you up later. **That is where the journey gets interesting.**
>

Our goal is clear. We want to roll out new features quickly, safely, and to the right people at just the right time. It is all about timin. Once a feature goes live, we need to keep an eye on things, spot any smoke early, and jump in to sort out issues fast. Whether it is a rogue feature causing trouble or a wild innovation that does not stick with people, we want to be ready. Monitoring and being able to roll back is key. That is what keeps the blast radius nice and tight and gives us peace of mind when pushing out new stuff.

There are other goals on our list too, and they matter just as much. We want to spark some proper experimentation in production. We want to dive in and analyse behaviour, learn from what we see, and adapt quickly. That is how we keep ourselves in the game and stay relevant to the folks using our products.

> ![Principles and Practices](../images/back-to-basics-from-continuous-delivery-to-release-on-demand-2.png)

Now, let us talk about feature flags. They have always been a bit of an afterthought, right? But **what if we flipped that whole mindset upside down?** What if we started every new feature with a flag right from the get-go? Imagine wrapping every feature in its own flag, so it is ready to switch on or off instantly. Of course, we would need a proper, reliable, and fast feature flag engine room. It must be bulletproof and sustainable, no doubt. But the upsides? Absolutely massive. We would get controlled releases, safer rollbacks, real-time insights into what is working (and what is not), and business folks would be making the big decisions, not just the engineers fiddling with code.

We need to figure out how to …

- **Make those feature flags a part of our design from day one.** Every new thing should sit behind a flag, ready to be toggled at a moment’s notice, no redeployment needed. That is proper flexibility, and it puts the power in your hands.
- **Use telemetry and dashboards to sniff out any odd behaviour as soon as it pops up.** Pair that with some automated rollback plans so if things go pear-shaped, so that we can keep the blast radius small and under control.
- **Build easy-to-use dashboards where product owners can take the wheel.** Let them control the flags and decide when a feature goes live. Engineers build the machine, but it is the business that should be steering it down the road.

Or find a software-as-a-service (SaaS) solution that can fast-track our processes and products.

This is our shot to lead big and bold, no half measures. Forget waiting for everything to be perfect. Just start where we are. Pick one feature, wrap it in a flag, run it through a ring. Build up that muscle. Give our business the power to own its releases. Engineers are here to enable, not to hold the keys to the kingdom. Release on demand is not just a pipe dream. It is a choice we can make right now. So, what are we waiting for? 

What are your thoughts and experiences with release on demand



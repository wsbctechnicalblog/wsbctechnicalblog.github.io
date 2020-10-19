Title: Benefits of boundaries
Date: 2020-10-19 10:20
Category: Posts
Tags: TDD, CI
Slug: benefits-of-boundaries
Author: Alex Bunardzic
Summary: Simple isn't easy, but it is the only way to build anti-fragile systems

_Things break on a small scale all the time, in order to avoid large-scale generalized catastrophes.”_ — Nassim Nicholas Taleb

Right on the heels of our PI Planning session, I’d like to continue the discussion on the merits of imposing and maintaining boundaries. To recapitulate what we talked about thus far:

- Systems are under constant stress (regulatory changes, market shifts, pandemics, customer expectations drift, and also plain old digital rot)
- Monoliths are brittle, and are first to crumble under the stresses and shocks of relentless change
- System resilience is 100% dependent on the system architecture
- System architecture can enable a system to survive stress
- Three main types of system architecture:
- **Robust architecture**
- **Agile architecture**
- **Anti-fragile architecture**
- Anti-fragile architecture is the most advanced/biggest bang for the buck
- It hinges on boundaries
- It is anti-fragile because it enables the system to function by safely engaging in trial-and-error
- It focuses on small problems
- It allows only small errors to occur
- It puts pressure on the system without jeopardizing it
- When the pressure gets fixed and removed, the system grows stronger than before (e.g. Netflix Chaos Monkey anti-fragile architecture)
- It enables the business to embrace change

## Why bother introducing boundaries?

There is plenty of field evidence illustrating the fact that any large, complex system that works according to expectations was once a small, simple system that gradually evolved into a larger one. Conversely, there is no evidence that a system that started as large and complex ever reached the point of being fully functional.

As a small, simple system evolves and grows, it can only do so by containment. The most fundamental principle of software design is to separate things that change from things that stay the same. This isolation (containment) is not a one-time event. Keeping things contained/isolated is an ongoing design activity which must occur every step of the way.

And the only way to keep things contained is to introduce and maintain boundaries.

## Would any boundaries do?

The short (and not so sweet) answer is: no. The hardest (and most powerful) trick is knowing where and how to erect boundaries. That knowledge is what separates experienced experts from dilettante software designers.

Let's have a quick look into a system that was architected using the wrong boundaries pattern:

![Incorrect boundaries pattern](/images/boundaries1.png) 

What is wrong with the above picture? Infrastructure layers should never be used to create boundaries for top level modules.

Let’s now look into a system that was architected using proper boundaries pattern:
 
![Proper boundaries pattern](/images/boundaries2.png) 

## Boundary fitness

As difficult as it often may be to create proper boundaries (it takes a lot of experience before one is capable of designing the system correctly), it is much, much harder to keep the boundaries intact.

As the system evolves, there is a strong tendency to break the boundaries. It is very tempting, as we are developing new features (or extending existing features) to take shortcuts and try to access modules that belong to isolated layers. Any time we do that, we are diluting the separation of concerns.

Boundary fitness is therefore expressed as a metric of how much of the important architectural characteristics remain preserved as the system evolves. Protecting the purity of the boundaries is of paramount importance. Whenever we encounter a system that is flakey and riddled with defects, upon closer examination we see that many, sometimes all architectural boundaries have been violated.

For example, a typical anti-pattern often goes like this:

![Boundaries anti-pattern](/images/boundaries2.png) 

We must never make cross-boundary calls. But that is easier said than done, because in the heat of the battle, we reach for an easy solution and see that crossing over to another domain is a quick win. We do it, and thus incur technical debt. And more likely than not, that debt never gets paid off.

## Conclusion

It is important to avoid the Big Plan Upfront approach to building software systems. It is much more advisable to start small, and maintain small isolated parts of a larger system. Correctly choosing the boundaries ensures we start on the right footing. The biggest challenge, however, is maintaining the pristine domains within the system. It takes strong discipline to resist the urge to cross the boundaries in order to accomplish quick and dirty wins.

<br /><br />
Title: Don’t let your code talk to strangers
Date: 2020-10-24 10:20
Category: Posts
Tags: TDD, CI
Slug: dont-let-your-code-talk-to-strangers
Author: Alex Bunardzic
Summary: Closer look into the principle of least knowledge

We have discussed the crucial effect that cost of change has on the quality of the delivered business value. If the delivered value is expensive to change, it loses its attractiveness. In such cases, it quickly morphs from an asset into liability. We certainly don’t want to find ourselves in such disadvantageous position.

Generally speaking, the most frequent cause of unchangeable code is tight coupling. During the early stages of development, coupling comes naturally, almost spontaneously. And at that stage, it appears quite harmless. We continue adding capabilities to our solution, and things appear to be going swimmingly.

But there often comes a moment when we realize that we need to rearrange our code due to the newly arrived requirements or findings. It is at that point that tight coupling rears its ugly head and makes us realize that we have all but painted ourselves into a proverbial corner.

Tight coupling has many underlying causes and anti-patterns. Today, we are going to take a closer look into one such anti-pattern – code talking to strangers.

## Principle of least knowledge

Tight coupling happens when our code knows way more than is needed in order to do the job. At a first glance, knowing more than is needed doesn’t sound undesirable. What could be wrong with possessing excessive knowledge?

Let’s try to illustrate what could get wrong by indulging in excessive knowledge by following a trivial example. Suppose we have a line of code that looks something like this:

`objectA.GetObjectB().GetObjectC().DoSomeSpecificThing();`

In the line above, we see `objectA` (i.e. an instance of `classA`) getting `objectB` (an instance of `classB`). That’s perfectly fine, but the issue now arises due to the fact that `objectA` is using `objectB` not because `objectB` can provide some useful capability/service to `objectA` (which would be the normal case). `objectA` is getting `objectB` merely in order to expressly get to `objectC`. Once `objectA` gets a handle on `objectC`, it can ask `objectC` to do some specific thing.

Why is that problematic? Granted, it is obvious that to `objectA` a once or twice removed `objectC` is a stranger. We do we say that `objectC` is a stranger to `objectA`? If `objectC` was a friend to `objectA`, there clearly would be no need for `objectA` to get to talk to `objectC` by first talking to `objectB`. But in this case, objectA can only engage in a ‘friend of a friend’ type of interaction. And that’s when the problem with tight coupling begins!

We see therefore that tight coupling materializes when we endow our code with unnecessary knowledge. In our code, objectA has the absolutely necessary knowledge of how to talk to its friend, `objectB`. But instead of leaving it like that, we succumbed to the temptation to teach our code that there exists another object, `objectC`, and although that object is not immediately available to our `objectA`, it is available via our network of friends. So now our objectA gets saddled with excessive knowledge of having to know how to get to `objectC` and how to ask it to perform some specific action.

This is too much knowledge, and such excessive knowledge is making things tightly coupled, bloated and brittle.

## Where is brittleness coming from?

In the above example, we perceive tight coupling in the form of an underlying assumption: every `objectB` has access to `objectC`. That is a dangerous assumption, as we may discover later on, after we’ve created a lot of code that relies on the above chaining of method calls that in some instances `objectB` may not have access to `objectC`. Maybe someone had refactored the code and had completely removed the association between `objectB` and `objectC`. Having to go and find all instances of the legacy code and adjust them to the new situation is a potential breeding ground for bugs. Often times there are slight variation in how are instantiated objects called (no one is guaranteeing that every developer will consistently name instance of `classA` `objectA` etc.) No regex on earth could be crafted that will guarantee to fish all these minor variations out. So we’d be left to manually pour over reams of code, trying to find all instances of such chained calls and then fix them manually.

That’s brittleness to the umpteenth degree. And a vast breeding ground for all kinds of bugs.

## Only talk to your immediate friends

To avoid the terrible anti-pattern of promiscuously talking to strangers, our code should embrace a very important constraint – talk only to your immediate friends.

In the above case, `objectA` should only confine itself to talking to objectB. If there is some useful capability/functionality that some stranger (e.g. `objectC`) possesses that `objectA` desperately needs, let `objectB` be the broker between `objectA` and `objectC`. That way, our code becomes simple, future proof, unperturbable (and also easy testable).

Let’s indulge in another quick example. Suppose we have an instance of a class `Driver`, and that driver is steering an instance of a class `Vehicle`). The way we implement steering is to allow the driver to talk to strangers; for example, if the driver wants to steer left, the code looks like this:

`driver.GetVehicle().GetSteeringMechanism().SteerLeft();`

The `driver` is talking to its immediate friend (`vehicle`) in order to gain access to a stranger (an instance of the class `SteeringMechanism`), so that the driver can directly manipulate the steering mechanism by sending it the command to steer left.

This is the illustration of tight coupling in action. Suppose later on the instance of class SteeringMechanism (which was an instance of an automobile steering mechanism) gets replaced by an instance of a sail boat. On a sail boat, the steer left command has the opposite effect from the same command sent to a steering wheel in the car. Which means, we have inadvertently created a bug.

So it is important to avoid tight coupling. Always limit the amount of knowledge your objects have. That way, your code will be clean, testable, deterministic and bug free.

<br /><br />
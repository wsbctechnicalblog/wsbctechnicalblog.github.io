Title: Cultivate apathy for details to enable refactoring
Date: 2021-10-15
Category: Posts
Tags: technical-excellence
Slug: apathy-for-details
Author: Alex Bunardzic
Summary: Give equal care to the code structure as you would give to the code behaviour

![Law of Demeter](../images/law-of-demeter.png)

Code behaviour cannot be implemented without having code structure. On the other hand, code structure that does not implement meaningful and useful behaviour is worthless. It thus becomes apparent that code behaviour and code structure go together – it is not possible to separate one from another.​​​​​​​

Since code structure is never visible to end-users, the tendency is to assign much higher value to the code behaviour than to the code structure. From the business operations side of things, the most pressing question is always _Why_? Why are we planning to make changes to our system? There’s got to be a valid business case for spending precious time, money, and effort on making proposed changes.

Once the business case is justified, we move into the _What_ phase. What do we need to change in our system so that the business case gets fulfilled?

It is this _What_ stage of development that defines the expected change in the behaviour of the system. Maybe we need to change the behaviour of the system in such way that it allows end-users to apply for a promotional discount? Now that we know what needs to get done, there is an urgent pressure to do it.

That leads us to the _How_. While our discussions and concerns around the _What_ had helped define the _expected behaviour_ (i.e., the desired functionality), when it comes to deciding _How_ to do it, we realize that there are many ways to skin a cat. And here is where the trouble can potentially begin.

How to implement the agreed-upon behaviour is the sole responsibility of the code structure. We could implement it in a simple, straightforward way, or we could implement it in a convoluted, unnecessarily complex way. There are many possible ways to implement the same behaviour of the code. Having cleared the questions around the _Why_ and the _What_, we are now discussing the _Way_.

## Substandard structure causes substandard behaviour
From the business operations standpoint, the most valuable way to implement the desired behaviour is the quickest, cheapest way. However, such approach usually belies false economy.

If the desired behaviour, once implemented, is never going to change, one could argue that the cheapest, quickest, dirtiest way to implement it makes sense. However, it is extremely rare that newly added behaviour to the system never changes.

Change in software is inevitable. Creating a substandard structure of the code results in inability to safely accommodate upcoming unavoidable changes. As such, what little gets saved upfront by not caring about the quality of the code structure, gets quickly eaten up by the exorbitant costs of having to make subsequent changes to the code. Not only that, but the changes to a lousy code structure tend to introduce a lot of bugs, defects, and breakages.

Overall, not paying attention to the quality of the code structure (the _Way_) results in the substandard behaviour of the system. It becomes brittle, unreliable, non-performant, and quickly turns from being an asset into becoming a liability.

## Enable refactoring
Almost all knowledge-based activities are based on refactoring. We typically start any project by crafting the first draft. That first draft is far from being anywhere near good, but it’s a great starting point. We throw in quick outlines and paint with a broad brush (we approximate). Then we iterate. We make a second pass (either working on our own or collaborating on the project in a team). The second pass increases the resolution of the information provided in the document we are working on. That gradual increase in the precision of information is what we refer to as ‘refactoring’.

Regardless of the type of the project we may be collaborating on (i.e., a financial plan, a technology roadmap, an important planning event, etc.), we never create a publishable version on the first pass. We must keep reworking our initial draft, adding more details, removing clumsy/cumbersome statements, and so on. We proceed piecemeal, step-by-step.

After several iterations (i.e., refactoring sessions), we eventually arrive at a satisfactory version of our deliverable. It is finally ready to be published.

There is absolutely no reason why writing software code should be any different. And yet, for some strange reason, we meet many software engineers who feel that refactoring is a waste of time. Some people think that good programmers must know how to write well-structured code on the first try.

That mindset is very damaging to the quality of the delivery. It insists on ignoring the quality of the code structure and instead spending all the time only on implementing the desired behaviour of the code. The argument for such irresponsible practice is that since end-users will never see the code structure, why should we worry about its quality?

It’s like saying “Since average drivers will never get to see the inside of the car engine, why worry about its quality? Instead, we should pour all our efforts into making the attractive exterior and interior, plus do an amazing paint job and add an awesome stereo system, heated leather seats, and so on!”

## Why enable refactoring?
The key to enabling easy, risk-free refactoring is to practice _apathy for details_. What do we mean by that? Maybe a hypothetical example could illustrate the concept better:

Imagine a person arriving at the checkout in a supermarket and the cashier asks them to pay for their groceries. The person reaches into their pocket and takes out their car keys and gives the keys to the cashier. The cashier is confused, and the person says: “I’m parked in the stall 17, red Honda Accord. Go to my car, open the passenger side door, open the glove compartment, find my jacket in there, reach into the bottom right jacket pocket, grab my wallet, take out the cash and please leave the change in!”

Naturally, the cashier would refuse to do that. Why? Because the cashier has _apathy for details_. Simply put, the cashier only wants the money bills (the _What_) and is absolutely not interested in the process by which that money arrives at their hands (disinterested in the _How_).

If we structure our code in such a way that it always refuses to know the annoying details (the _How_), it will be easy to refactor it without any risk. If, on the other hand, we structure our code in such a way that it is hungry for details, we end up with tightly coupled code that is brittle, expensive, and risky to modify. Which is to say, we paint ourselves in the corner.

## How to enable refactoring
The best way to enable refactoring is to write code that is _structure-shy_. If the code is disinterested in knowing more details than is necessary, such code remains loosely coupled (easy and risk-free to change).

Yes, but how to make sure the code we write is _structure-shy_? The recommended way is to abstain from writing any code before we have created a client who will consume that code.

To create the first client of the yet-to-be-written code, we focus on the _expected behaviour_. The _expected behaviour_ should be obtained via a single step. The client should be able to ask the system to do something, and that ask should be a simple step. The system will then go away, do some processing behind the scenes, and return with the expected values.

What we’ve described above is what is technically known as an interface, or an API.

A quality interface/API is always _structure-shy_. It does not care about the _How_, only cares about the _What_.
To create the client before we create the code that will serve the client’s expectations, we resort to writing microtests. Microtests are focused on small, atomic steps where the client sends one request to the system, and then, after receiving a response, asserts whether the response matches the initial expectation. That way, the client verifies that the behaviour of the system is still as expected.

The _structure-shy_ code is now freely open for radical refactoring. With each refactoring step (i.e., a change made to the code structure), we run the clients (i.e., microtests) to confirm that nothing broke with that change and that the system still behaves as expected.
Title: Fail, Learn, Reset!
Date: 2023-01-11
Category: Posts 
Tags: engineering, learning, innovation
Slug: fail-learn-reset
Author: Willy-Peter Schaub
Summary: "Failure is a good option. If you are not failing, you are not trying hard enough." - Elon Musk

Last year, I tried hard to encourage everyone in my team and our group to accept failure as an opportunity to learn. I am so passionate about the value of failure, that I will continue to eradicate the **fear of failure** with our engineers. 

> _"There is a silly notion that failure is not an option at NASA. Failure is an option here. If things are not failing, you are not innovating enough."_ - Elon Musk

---

# Good and bad failures

Just like cholesterol, there are **BAD** and there are **GOOD** failures. 

We must minimize the **BAD**** failures, originating from context switching, stress, ignoring guardrails, and guidance, as they typically impact user experience and work:life balance. As we want to continuously deliver value to delighted end-users, we need to take the bad failures very seriously.

Maximize the **GOOD** failures, generally originating from experiments, which promote innovation and learning, and help us raise our built-in quality bar.

---

# Create psychological safety!

For a team to embrace **FAILURES**, psychological safety and support from the leadership is pivotal. If engineers must comply with metrics and performance reviews that do not support the value of failure, you will observe **zero** traction by your team(s) to even consider the option of failure.

Encourage safe and vibrant collaboration, to combat the imposter syndrome. In other words, we are all equal and what is discussed by the team stays with the team, until everyone is comfortable to share the context, the core issue, and the learnings after picking up the pieces and performing a retrospective on a FAILURE.

You need an ecosystem based on **TRUST**, and encourage everyone to be open-minded, respectful, and empathetic. 

Once these ingredients are stirred into the secret sauce of your team, you are ready to share your failures.

---

# Accept and learn from your failures

I shared my top three failures with management and our engineers not only to showcase that no-one is invincible or perfect, but to encourage everyone to do the same. Here are the failures I shared:

- In the late 80’s I was working on a new encryption hardware module and integrating the service into a banking system in Switzerland. The project FAILED with spectacular operating system lockups, resulting in me flying to the US for the first time. I had a huge opportunity to debug and patch the [Convergent Technologies Operating System](https://en.wikipedia.org/wiki/Convergent_Technologies_Operating_System) (CTOS) operating system kernel together with its creators. Finding the root cause for the operating system lockup was a phenomenal learning experience for all of us and as a result I also fell in love with Assembler and V2PLM programming.

- In 2013 we toggled a feature flag in Team Foundation Service (now known as Azure DevOps) at a major conference. It did not go well … we blew up Azure and spent weeks fixing Azure DevOps. We learned about handling transient faults and avoiding similar failures with retries, throttling, and circuit breakers, and even created vibrant collaboration and trust by being transparent. My [3 ways to handle transient faults for DevOps](https://opensource.com/article/19/9/transient-faults-devops) article is one of the outcomes, as is my caution for dark launches and feature flags. Also read Brian Harry's [A bad day](https://devblogs.microsoft.com/bharry/bad-day/) blog post for more details.

- At WorkSafeBC, I recently blew up our v1 blueprints with a two-space indent in one of our YAML templates which silenced WhiteSource, I repeatedly get the expense field in TRRs incorrect, and just recently mixed up two ServiceNow requests, creating the wrong team, in the wrong project, for the wrong users. What I am learning from these, is that **context-switching is BAD**, and that **focus** is worth every Penny.

I could go on and on and on, but my top three hiccups are enough for this post.

---

# Experiment, fail, learn, act!

The following illustration summarizes my thoughts on **FAILURES**:

> ![loop-of-failure](/images/fail-learn-reset.png)   

1. We need to run **experiments** to test ideas, proposed innovations, or minimally viable products (MVP) to evaluate if we achieve desired results (PASS) or not (FAIL).
2. Either way we can **act** upon invaluable **learnings**, either reiterating on the experiment or focusing on the next.
3. It is all about continuously **learning** and delivering **value**. 

To create and support an ecosystem based on **TRUST** and one that embraces the **learn from failures** mindset we need:

1. The leadership to create **psychological safety** by enabling everyone to fail without the fear of retribution or bad reviews. This is my next challenge to address.
2. Engineers need to eradicate the **imposter syndrome** through vibrant, open-minded, respectful, and empathetic collaboration. We have been driving this through our [collaboration ceremonies](https://wsbctechnicalblog.github.io/ceremony-overview.html). 

What are your thoughts on failure?


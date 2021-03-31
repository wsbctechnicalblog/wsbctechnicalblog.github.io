Title: Extreme Programming 25 Years Later
Date: 2021-03-31
Category: Posts
Tags: Extreme Programming, XP, Agile, DevOps
Slug: xp-25-years-later
Author: Alex Bunardzic
Summary: Extreme programming keeps going strong 25 years after its launch

Extreme Programming (XP) was a revolutionary movement launched by Kent Beck in 1996. According to Beck, XP was a political statement. Back in the mid-1990s, software quality was being outsourced to the QA departments. Programmers were doing their part by writing software to the best of their ability but would then delegate the quality of their products to testers.

Beck disagreed with that approach and felt that quality is everyone’s responsibility. He launched Extreme Programming as a political statement which expresses full and unreserved commitment to unwavering high quality and professionalism in software engineering.

## How did XP improve software engineering discipline?

Today, 25 years after Beck launched his political statement, we are seeing incredibly impressive improvements in our profession. The initial launch made strong waves which are being felt to this day. Let’s look at some of the obvious improvements that XP brought to the table.

### Continuous deployment (CD)

Back in the 1990s, deployment was sporadic (non-continuous). Teams working under the waterfall development paradigm were being driven by the Big Plan Upfront. That upfront plan was fleshed out to such levels of detail that it would predict the exact deployment date. That date was typically scheduled far into the future (oftentimes 6, 8, 12 or even 24 months in the future).

Beck had raised many eyebrows at Chrysler in 1996 when he was put in charge of their software engineering and declared that teams will be deploying every three weeks. Such aggressive schedule was unheard of (the most daring teams were deploying every three to six months at best). But he pushed through and stuck to his guns and demonstrated that it was possible to do the regular deployments on a three weeks cadence. How did he manage to do that? He instigated the discipline of Extreme Programming.

25 years ago, deploying software every three weeks did seem extreme indeed, so the name Extreme Programming stuck (today, Beck somewhat regrets choosing that name, but that’s a discussion for another micro learning episode).

Today, we see many teams deploying much more frequently than every three weeks. Many manage to do it every week, or even every day. Some even do it more than once per day. In the most extreme cases of Extreme Programming, we see teams deploying code every second! (https://www.zdnet.com/article/how-amazon-handles-a-new-software-deployment-every-second/)

### Testing in production

Continuous deployment presents an opportunity to test changes in production. If we’re deploying to production many times per day, we get a chance to truly run our software through its paces right there, in the real world.

When Beck was formulating his Extreme Programming approach, he said he was guided by one simple principle:

“I want the code to run all the time!”

What better way to fulfill that guiding principle than to run and test the code in a live environment?

Yes, but what about potential defects? Wouldn’t deploying changes to production so that we could test them potentially harm us? The answer lies in mastering feature flags (we already discussed this topic in another micro learning episode).

### No bugs

Rather than chasing bugs, our time is better spent not writing them in the first place. TDD and shift left are methodologies that underpin XP and are our best weapon against bugs. All bugs are authored and minimizing/eliminating sloppy authorship inevitably results in minimizing/preventing bugs.

Consequently, we cannot consider any story actually completed until the code that implements the story is in production, tested, and proven to be bug free.

### No backlog

XP teams adopt a default answer to any feature request. That default answer is “No”. The rationale is that if ideas for features (i.e. hypotheses) are indeed important, they will

come up again. Only in such cases is the request for feature (hypothesis) going to be taken up for work.

This approach eliminates bloat. The rationale is that maintaining a long backlog is a waste. Identify the most important thing right now and then work on it. If while working on it something more important emerges, stop working on the current thing and attend to the more important one. Keep going in the same fashion. Iterate.

### No estimates

Estimating a required effort by counting story points amounts to measuring the output instead of measuring the outcome. Wrong metric.

Some teams switch from counting story points to counting number of stories delivered. Which is also a meaningless metric.

If teams are already doing the best they can, and are working on the most important thing that the time, and are deploying as soon as possible, what’s the point in estimating? Time spent estimating is a waste, and that time could be better spent attending to most important things (i.e. working software that meets customers’ needs).

### Data driven

System cannot evolve in the absence of business hypotheses. What are the sources of those hypotheses? Backlogs, predictions, Big Plan Upfront? A better, more reliable option is to use data. Collecting data by interviewing customers and end-users, exploring logs and devising razor-sharp telemetry is a better way to evolve the business.

### Improvement boards

Improvement boards are based on the improvement kata (pioneered in Toyota). Improvement kata is based on the discoveries that occur along the way. This approach requires that participants do not hold on to the sense of certainty that is based on any prescribed perspective. Rather, the emphasis is on innovation and experimentation. The experiments are published on the Improvement board, which then serves as a reminder, an inspiration, an invitation to collaboration, lessons learned, etc.

### Mob programming

The original collaboration model that XP introduced (pair programming) has been expanded and improved by introducing mob programming. Mob programming is not possible without practicing TDD.

### Throwing code away

Functionality is an asset; code is a liability. In XP, functionality gets encoded in test scripts. As such, those test scripts are a definitive asset. In TDD, test scripts drive the implementation of the code.

Testability is the highest value, while code is disposable. Some teams are discovering that it helps if we stop viewing implementation code as an asset, and if we often dispose of it and write it again guided by the tests.

### Limit work-in-progress

When teams adopt a ‘no bugs’ mindset, they work following Edward Deming’s formula: “Quality comes not from inspection, but from improvement of the production process.” The only way to improve the production process is to limit work in progress. Limiting work in progress means eliminating interruptions.

When teams have full control of their work environment (i.e. teams own their work), there is no need to multitask.

### Hackathons

Incremental improvements are not giving organizations much needed competitive edge. To survive and thrive, organizations need to continuously engage in experimenting with completely new ideas. Innovations are mandatory, and our InnoFest is an excellent illustration of the viability and the importance of that approach.

### DevOps

As developers start doing daily deployments, they get heavily involved with operations. By doing that, DevOps quickly turn into product support team. There is then only one small step from working as a product support team to becoming THE product team.

### Conclusion

Extreme Programming has proven not only that it has amazing staying power (25 years and going strongly) but also that it can evolve in unexpected and surprisingly powerful ways. All the major improvements that happened in XP during the past 25 years serve one single purpose: running the code all the time.

The future of XP looks bright. By speeding up the delivery while minimizing/eliminating defects, it is poised to continue enabling business automation and offering unprecedented competitive advantage through increased flexibility.
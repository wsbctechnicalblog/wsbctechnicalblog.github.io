Title: Start together work together finish together
Date: 2021-05-07 23:59
Category: Posts
Tags: Extreme Programming, XP, Agile, DevOps
Slug: start-together-work-together-finish-together
Author: Alex Bunardzic
Summary: Speed up the delivery process by avoiding queuing and needless looping

**Note**: This article was inspired by the amazing research [John Cutler](https://blog.amplitude.com/author/john-cutler) keeps doing

Every organization starts any software development initiative by examining the opportunities and then selecting the highest priority ones. Once that selection happens, teams move on to work on formulating the expectations. What is the proposed system supposed to offer to the paying customers/end users?
 
Formulated expectations get formalized as user stories, which in turn get vertically sliced and worked on in a typical combination of iterative/incremental fashion. Once fully tested, the expectations get released and the system runs in production environment. Rinse, repeat.
 
## Traditional waterfall approach
 
In the familiar waterfall scenario, each of the above described phases get done in strict isolation following the incremental model. At each gated phase, proposed changes get formulated, reviewed, signed off and then frozen. Change management insists that once frozen, expectations cannot be revisited. We move forward in strictly incremental fashion (i.e. we only possibly iterate at the stages 4 and 5). The gated phases typically happen in the following order:
 
1. **Opportunity selection** (once selected and signed off, the opportunity gets slated for implementation of the solution which will harvest its potential)
1. **Formulating the expectations** (typically, the expectations get formulated as a laundry list of features); once formulated, the workload gets planned and then the expectations get handed off to the design team
1. **Design the solution**; teams take careful approach to design the system which will meet all the signed off and frozen expectations; once the design is finished and reviewed, it gets signed off and frozen – change management precludes any further changes to the signed off design
1. **The build team gets the design blueprints and commences the build activities**; since no changes to the design nor to the expectations are permitted at that stage, the only team that is busy is the team building the solution
1. **Once the build team reaches the ‘code complete’ stage, the built solution is handed off to the testing team**; the process waits while the testers examine the solution and if any defects or malfunctioning that are deemed as show-stoppers are found, the built solution is pushed into the queue, looping it back to the build team to fix the issues
1. Finally, after obtaining the clearance from the testers and other stakeholders, **the operations team releases the solution to production**
7. Once in production, the **SRE specialists take over and are running the system**

## Why abandon/revise the waterfall model?
 
Software development industry at large seems to lean aggressively toward abandoning the above described waterfall model. What are the reasons for such abandonment?
 
1. **Slow in the making**: waterfall increments take time. Significant effort is needed at each stage of the game. Long stretches of time needed to complete each stage create large overheads necessary to coordinate, synchronize and manage the teams.
1. **Meagre utilization**: each gated phase takes significant time to complete while blocking all other teams from working on the solution. While teams responsible for opportunity selection are working hard on identifying and prioritizing useful opportunities, business analysts, architects, designers, coders, testers, sysadmins, security specialists, SREs etc. are idling. As the process moves from one gated phase to another, upstream and downstream teams remain underutilized, waiting for their turn to do something useful.
1. **Unrealistic expectations**: time waits for no one, and while initially it may have seemed that identified opportunities have the potential to strengthen company’s position on the market, if the organization runs on sluggish processes the shift in the market and political climate is at danger of going unnoticed. By the time the organization finally releases the solution, chances are that it lags and the company may discover that the solution is inadequate, sometimes even harmful.
1. **Insufficient quality**: betting the future on formulating the Big Plan Upfront means that the engineers claim they have all the knowledge necessary to correctly architect, design, implement and test the proposed solution. That is rarely the case and waiting until the very last moment to test the already built solution is not the optimal way to ensure technical excellence.

## What are the alternatives to the waterfall model?
 
A stock answer is agile processes, but there are several stages of maturity in agile:
 
1. **Simplest (or classic) agile**: combine the build and test gated phases into a single phase, run by a single team. Testers/security experts are not waiting on coders to get to the ‘code complete’ stage but are instead working side-by-side with the coders, helping with testing every diff.
1. **Agile that removes the release silo**: combine the build, test, and release gated phases into a single phase run by a single team. Testers working side-by-side with coders while release specialists move into continuously releasing the tested diffs.
1. **Agile that includes designers as team members**: all the above specialists (coders, testers, release engineers) work together while also including designers into the team. That way, designers get to respond to the issues discovered by the coders and testers during the process of building and verifying.
1. **Agile as DevOps**: the above team, consisting of designers, coders, testers, and release engineers, adds SREs and other operations specialists to the team. They all work together on issues discovered along the way.
1. **Agile as Feature Factory**: the above team begins tight collaboration with business engineers who work on creating and modifying the expectations. As the team moves forward and discovers issues with the current state of design, technical excellence etc., the team feeds the details back into the business engineers who adjust the expectations.
1. **Agile as Product Team with “mini CEO”**: The last remaining gated phase silo (**Opportunity selection**) gets removed and the “mini CEO” becomes involved in the process of building the system. Selected opportunities are not cast in stone anymore but remain open to be examined by the “mini CEO” and reviewed to accommodate discovered market pressures.
1. **Product Team**: the entire team (i.e. the Whole Team) collaborates in real time on continually adding value to the organization. The team is actively engaged in seeking valuable opportunities and solving problems that arrive while attempting to provide automated systems that harvest identified opportunities.
 
Ideally, the best results and the most optimal utilizations are achieved when the whole team starts together, works together, and finishes together.
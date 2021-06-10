Title: Why we should (not) care about Pipelines!?!
Date: 2021-06-15
Category: Posts
Tags: DevOps, Azure Pipelines
Slug: meetup-devops-meetup-wsbc-pipeline-story
Author: Willy-Peter Schaub
Summary: Enabling engineering to continuously build, validate, and deploy secure solutions to delight our customers

On Tuesday, [June 15th 2021](https://www.meetup.com/DevOps-Vancouver-BC-Canada/events/278727555/), we picked-up where we off with the “Common Engineering System at WorkSafeBC“ session, on the [April 2020](https://www.meetup.com/DevOps-Vancouver-BC-Canada/events/270150093/) meetup.

> ![INTRO](/images/meetup-devops-meetup-wsbc-pipeline-story-intro-1.png)

 We shared our insight into our ambitious journey to consolidate hundreds of inconsistent continuous delivery pipeline snowflakes into state of the art pipeline-as-code, based on YAML and re-usable templates. Here is our story!

# WHY?

> ![WHY](/images/meetup-devops-meetup-wsbc-pipeline-story-why-2.png)

[Donovan Brown](https://www.donovanbrown.com/post/what-is-devops) defines DevOps as the “the union of PEOPLE, PROCESS and PRODUCTS to enable the **continuous** delivery of value to our CUSTOMERS”. The word continuous implies that we **automate everything automatable**, move repetitive tasks to machines, and enable engineering to focus on delighting our customers with features. 

With today’s disruption so prevalent and there being such a critical demand for speed of change, the [agents of chaos](https://www.tactec.ca/ndtw-resources/) created guardrails defined by five essential values for the DevOps mindset.

One value encourages us to innovate and improve beyond repeatable processes by reducing waste and not doing things with no value or purpose.

As alluded to by the checklist, we are not talking about pipelines to carry oil, but an enabler to automate continuous integration and delivery tasks. 

We embraced the Azure Pipelines and standardized on the unified pipeline which helped us build once, deploy the same build artifact to different environments, and streamline our manual approvals.

We were in technology heaven … … until our automated weekly pipeline reports unearthed a scary und unnerving reality.

Over 3000 pipeline definitions, growing at an alarming rate, and creating a pile of sh…ocking technical debt.

Autonomy inspired a variety of snowflakes, some of which introduced alarming vulnerabilities, and a growing number of release rejections by security.

Microsoft began referring to the user interface based Azure Pipelines as CLASSIC and there were clear signs that the technology was becoming stale. Rot was setting in and we started to experiment with the YAML-based Azure Pipelines in two consecutive hackathons. We did not catch the attention of business and won no prize, but …… we embarked on an exciting journey after adding alignment, consistency, simplicity, security, flexibility and transparency to our pipeline checklist.

Read [Part 1: Pipelines - Why bother and what are our nightmares and options?](/yaml-pipelines-part1.html) for more details.

---

# WHAT?

> ![WHAT.1](/images/meetup-devops-meetup-wsbc-pipeline-story-what-3.png)

We embraced the new YAML-based Azure Pipelines, based on a mature and human readable data serialization, originally proposed by Clark Evans in 2001.

It is often referred to as “yet another markup language” and “YAML ain’t markup language.

What was exciting is that the Azure DevOps YAML pipelines are structurally YAML. Microsoft introduced no deviation or snowflake and forked the Azure DevOps pipeline repository to build their GitHub pipelines. This is like applying a protective anti-rust coating on our Azure DevOps pipelines and opening exciting coexistence and migration opportunities.

[Jenkins](https://www.jenkins.io/doc/book/pipeline-as-code/) introduced the term "pipelines as code”.

It is a technique that treats the pipeline configuration as code, placed under version control, packaged in reusable components, and automated deployment and testing ... comparable to infrastructure as code and the golden fleece for our pipeline adventure.

Transparency is considered one of the core ingredients to Agile and Lean development, as well as a healthy DevOps mindset … it fosters TRUST. Pipeline as code enables us to place all pipeline artifacts in source control repositories, which can be viewed by all our engineers … there are no secrets!

We enable our engineers to contribute to our common engineering system by submitting pipeline changes and innovations through the pull request workflow … we are centralizing, not standardizing.

We enable our engineers by injecting re-usable templates when they queue their Azure Pipelines … sprinkling the concept of shift-left automatically and consistently.

In our hackathons and proof-of-concepts we highlighted not only the RISK of rotting technology, but engineering distractions and focus on waste, instead of VALUE.

A typical YAML-based CI pipeline for an Azure Function requires 300 lines of code. With 927 CI pipelines, this amounts to 278,100 lines of code that engineering need to craft … more than Photoshop 1.0 and just less than the Quake 3 engine. In my humble opinion, this is a huge pile of waste.

Our first-generation generic blueprint-based pipelines reduced this to 113,094 lines of CI code and to 25,956 lines of CI/CD code using our second-generation app-type blueprint-based pipelines.

I recommend you read parts [Part 3: Pipelines - Basic building blocks as templates and sprinkling on telemetry](/yaml-pipelines-part3.html), [Part 4: Pipelines - Magic of queue time assembly](/yaml-pipelines-part4.html), [Part 5: Pipelines - Blueprints to fuel consistency and enablement](/yaml-pipelines-part5.html), and [Part 6: Pipelines - Gotcha! The generic blueprint-based YAML pipeline simplicity](/yaml-pipelines-part6.html) of our pipeline series on our technical WorkSafeBC blog for more information.

Templates allow us to define reusable CI and CD tasks, keeping our main pipeline definitions razor focused.

They enable us to script and assemble pipelines at “queue” time.

And most important, instead of editing hundreds of classic pipelines in a GUI editor … which can be mind numbing and is error prone … we edit one template to make a change such changing guardrails, which once saved … is automatically injected into all pipelines that are queued thereafter.

Magic!

Again, refer to our technical WorkSafeBC blog, pipeline series, [Part 7: Pipelines - There is more! Simplicity and enablement, courtesy of the app-type blueprint-based YAML pipelines](/yaml-pipelines-part7.html) for details on our 1st generation blueprints.

As a software developer, do I want to own, for example create and maintain, the pipelines to build and deploy my application? 

My answer is NO.

I will be glad to let another team take that responsibility while I focus on creating value for the business by delivering quality software. I just want access to the build pipeline templates and an ability to suggest changes, so that I can learn, innovate, and troubleshoot issues if any.

The 1st generation app-type blueprints introduces re-usable application type continuous integration blueprints , which typically require me to update a git of configuration and I am done with my pipeline.

Some more magic is the “extend template” which allows us to verify that a pipeline is based on a known and trusted template. If not, it is automatically rejected by the service connection and/or environment checkpoints … at run time.

But, there is more.

> ![WHAT.2](/images/meetup-devops-meetup-wsbc-pipeline-story-what-4.png)

If you read [Part 8: Pipelines - Pipelines - From CI to CD and beyond in one pipeline](/yaml-pipelines-part8.html) of pipeline series, on our technical WorkSafeBC blog, you will be amazed with our 2nd generation app-type blueprints, which are in EARLY PREVIEW in two of our engineering environments.

The 2nd generation has the same magic as 1st generation we just discussed, but for both continuous integration … CI … and continuous deployment … CD.

And no, we are not standardizing and hiding the implementation. Thanks to pipeline as code and the way we have structured our pipelines and template repository, all engineers can review all templates and submit improvements via a pull request.

If the proposed change is within our guardrails we innovate. If not, we organize a discussion between the engineer suggesting the change and DevSecOps enforcing out guardrails. If none is open to discuss or compromise, we terminate the pull request with “Kevin said so.” More about that in a minute.

We have not yet realized our dream for self-service automation.

We are, however, at a point where our blueprint-based pipelines are automation enablers, consistent, and simple. 

The pipeline working group is collaborating with the automation working group to build a “Hello world in less than 1min” world!

While you vTravel home after today’s meetup, ponder whether you would prefer working in <C> this humanoid driven world … or <C> this humanoid enabled world?

---

# HOW 

HOW we managed, and at times battled, to grok the intricacies of YAML and evolve the emerging application-type blueprint-based pipelines is beyond the scope of today’s chat and a discussion for another day.

In the meantime, feel free to connect to us via twitter or LinkedIn to discuss your questions after today’s meetups and the HOW.

Next, I would like to invite my colleague Said to jump in and give you a quick demo and a glimpse of the pipeline-as-code magic. 

> ![HOW](/images/meetup-devops-meetup-wsbc-pipeline-story-how-5.png)

TBD

## Through a Software Development Engineers' Lens

![Said Akram](/images/Said-mug.jpeg)

TBD

---

Kevin, why are the pipelines so important to security and why have you been smiling from ear to ear, ever since the blueprints emerged from the pipeline working group?

## Through a DevSecOps Lens

![Kevin Schwantje](/images/Kevin-mug.jpeg)

TBD

---

# What is next?

Hopefully, we will return to the meetup with the automation success stories soon. We will demonstrate that it takes seconds, not hours to days, to create a new repository, add sample code, 2nd generation app-type blueprint-based CI/CD pipeline, tie everything together, and queue a continuous integration build for the newly created environment. Our colleague, [Alex Bunardzic](/pages/authors.html) calls it the "walking skeleton" q;-)

If you have any question or feedback, please ping us on twitter [@saidakram007](https://twitter.com/saidakram007), [@604kev](https://twitter.com/604kev), and [@wpschaub]https://twitter.com/wpschaub)


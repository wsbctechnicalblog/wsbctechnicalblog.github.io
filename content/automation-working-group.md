Title: Introducing the Automation Working Group
Date: 2021-04-29
Category: Posts
Tags: agile, automation, code, devops, workflow
Slug: automation-working-group
Author: Alex Bunardzic
Summary: Any system operation we can perform manually can be fully automated by writing scripts

The only reason we make changes to the software is to be able to test the hypothesis. No one makes any changes to software just because they’re bored, or to show signs of inane activity. Changing the software behaviour/functionality is a very risky business, and we must have a very good reason for doing so.
 
Once the behaviour of the software has changed, it cannot be tested for usefulness unless it gets deployed to production. Without deploying changed software to production, our jobs would be meaningless.
 
Knowing that, we furthermore realize that the true measure of software quality is frequency of deployments. The more frequently we deploy changed software to production, the better the chances that we will improve the quality of software.
 
## How to expedite frequency of deployment?
 
The accidental complexity of modern computing platforms is nothing short of staggering. To develop, configure and deploy fully functional software products to the cloud requires many intricate steps. Each of those steps requires high level of expertise.
 
It is therefore a small wonder that the process of deployment could get so involved and convoluted that it takes a lot of time from the moment changed software gets approved to the moment when we see approved changes in production. And the longer it takes to deploy changed software to production, the worse off we are in terms of value delivery.
 
## Is there a way to expedite this process?
 
In a word – yes. The tried and tested way is to focus on **automation**. There are many manual tasks, steps and chores that can be reliably automated. With such automation we not only shorten the time it takes to deploy to production; we also increase the quality by reducing the chances of human errors.
 
In addition, we remove waste by increasing the testability of the automated process. It’s a win-win situation where tedious and error-prone manual chores get replaced by air-tight automated scripts, leaving human operators with more time to devote to improving processes that cannot possibly be automated.
 
## How to automate repetitive tasks?
 
In the olden days, when most of software developers worked in isolation, we had a specialized role called sysadmin. I remember in my younger days chatting with sysadmins and enquiring about their work. One sysadmin colleague told me:
 
> “Have you experienced times when you were forced to perform a long, arduous and complex task on the command line and couldn’t wait to get to the end of job?”

> To which I replied:

> “Yes, for sure, I think everyone went through that, one time or another. Those are extremely unpleasant situations where I feel like I’m walking on eggshells which makes me very apprehensive of every step I make.”

> “There you go.” replied my colleague. “You have just described what my job is. My job is to make sure you never again go through such a trying experience. What I do is I write scripts that automate all the steps you were taking so gingerly. My goal is to make sure you never ever have to go through the same unpleasant and unnerving experience.”
 
One lesson I learned from my sysadmin coworkers is that almost everything we need to do on a computer will need to be done again. Maybe later the same day, maybe the next day, maybe the next month, but for sure sometime in the future. There are no one-off operations on the computer.
 
That lesson stuck with me. And helped me fully understand the importance of automation.
 
So, when it comes to automation, the most common way to automate manual tasks we do on a computer is to write scripts.
 
Of course, the first thing a trained computer programmer will ask is: why use scripts when we can automate by writing computer programs? A canned answer to that question is: we need a way to tell computers what we want them to do, and in that regard scripts (be it PowerShell scripts or Bash scripts etc.) are no different than compiled binary code.
 
## Why is the ability to write scripts essential?
 
We all use computers daily, and we operate them either by mousing around the GUI or by typing commands on the command line. As mentioned above, pretty much none of those tasks we do are ever one-off tasks. We will have to repeat those tasks later in our daily work. Such repetition is not only counter-productive, it is risky as it brings with it the inevitable human error (oftentimes referred to as the ‘fat fingers errors’).
 
It is therefore very desirable to gain skills in automating repetitive, tedious tasks by declaring them in a script.
 
Today, as we’ve progressed from the old-fashioned siloed separation of programmers from system operations, we are enjoying the benefits of the DevOps culture and the DevOps mindset. There are no more demarcation lines drawn between teams that develop software and teams that deliver and operate that software. In addition to knowing how to develop software, we must learn how to operate it by automating everything that is possibly automatable. We cannot rely anymore on the expertise of sysadmins, for the simple reason – we are now sysadmins!
 
## WSBC Automation Working Group
 
Seeing how crucially important the ability to automate repetitive and error-prone tasks is to our organization, I have decided to form a task force that will focus on raising the bar when it comes to automating critical processes. The working group is presently in the process of formation and early discussions around formulating the charter and the agenda.
 
In addition to focusing on finding the biggest bang for the buck/lowest hanging fruit to be tackled for automation, the Automation Working Group will also make plans for hands-on workshops. We are planning to learn the ins and outs of shell scripting by engaging in mob programming sessions.
 
I am excited about this initiative, as I think it can truly help us move the needle and speed up our delivery.
Title: Enable Agile, Kanban, Scrum, or SAFe with Azure DevOps
Date: 2021-05-05 13:13
Category: Posts
Tags: agile, azure-devops
Slug: agile-planning-choice
Author: Willy-Peter Schaub
Summary: Use Azure Boards to visualise a variety of **processes** using the **Agile** process in a single Azure DevOps project.

When you create an Azure DevOps project you must select Basic, Agile, Scrum, or CMMI as the process that all teams within the process will be working with. If you peruse the documentation you will read that Basic is the most lightweight, Scrum is the next most light-weight, Agile supports many Agile method terms, and Capability Maturity Model Integration (CMMI) supports formality. Give CMMI a miss and select **Agile** as your process!

---

# The choice is yours!

In [Navigate DevOps through Waterfalls](https://www.tactec.ca/ndtw-resources/) the agents of chaos (AoC) promote a healthy DevOps mindset, which is based on a set of [core value](https://www.tactec.ca/devops-core-values/), the script definition "_DevOps is the union of people, process, and products to enable continuous delivery of value to our end users._", by [Donovan Brown](https://www.donovanbrown.com/post/what-is-devops), and a strong push against talking about Agile DevOps.

I am one of the agents of chaos, #13, and strongly believe that DevOps is a mindset, not dependent on Agile, not just about automation, and strengthened by people following a process. In this post, I would like to focus on the latter, process, and demonstrate that you can use whatever process or processes that enable your team(s), using [Azure DevOps](https://docs.microsoft.com/en-us/azure/devops).

---

# Let us compare the non-CMMI processes

Let us have a quick peek at these processes, within the scope of Azure DevOps (AzDO).

### Basic

Choose Basic when your team wants the simplest model supported by AzDO. It uses a limited set of work item types, such as **Issues**, **Tasks**, and **Epics** to track work and suits teams looking for a simple process or if you are focused on other AzDO services.

### Scrum

Suitable for teams practicing Scrum, as defined by the [Scrum organization](https://www.scrum.org/)

### Agile

Suitable for teams with an Agile planning mindset inspired by the [Agile Alliance](https://www.agilealliance.org/)], increasing the set of work items to **Epics**, **Features**, **User Stories**, **Bugs**, **Tasks**, and **Issues**.

> ![Agile Planning](/images/agile-planning-choice-1.png)

---

# What about Kanban and SAFe?

**Kanban**, which stands for signboard or billboard in Japanese), is based on a scheduling system for lean manufacturing, just-in-time manufacturing (JIT), and suitable for teams focused on operations. There is no out-of-the-box process for Kanban. Depending on the work item types you are looking for, you can use either the Basic, Scrum, or Agile AzDO process.

**SAFe**, aka Scaled Agile Framework, comes in a variety of flavours, such as Essential, Large Solution, Portfolio, and Full. As with Kanban, there is no out-of-the-box process, but you can use the Agile process, with a few work item type customisation, and extensions such as [@Scale](https://solidify.dev/products/scaleX).

---

# Setting up a demo environment

We opted to create a demo environment on Azure DevOps, to help us with Agile planning workshops and to demonstrate the support for Agile, Kanban, and SAFe. Let us know if you are interested in the customisations we made to the Agile process, as I will focus on visualisation in this post.

## Iterations

The **Iterations** project configuration is the magic dust that allows us to create **one** AzDO project to demonstrate an  **Agile**, **Kanban**, and **SAFe** experience.

> Each program increments (PI) is made up of five two-week iterations
>
> ![Agile Planning](/images/agile-planning-choice-2.png)

## Kanban Board

I will start with Kanban, which is close my heart, and helps us visualise our work, limit work in progress, focus on flow, and continuously improve our process.

> Kanban Board
>
> ![Agile Planning](/images/agile-planning-choice-3.png)

In fact, the Kanban Board, aka View as Board, is available in all projects and their teams, irrespective of which process was chosen when creating the AzDO project.

You will notice that we are using **FIRE**, **FiXED**, and **STANDARD** swimlanes to track different type of work.

- **FIRE** tracks work where someone's hair is on fire and the issue(s) needs a root cause analysis and resolution posthaste.
- **FiXED** tracks work which must be completed during a predefined iteration or completed by a specific date, based on business, compliance, or other team plans. Although we are a team with a Kanban mindset, we support other mindsets and dependencies. You guessed right; we use program increments, iterations, and tags to track the WHEN.
- **STANDARD** tracks our standard work, with a focus on finishing and getting things done with quality.

> Notice the Kanban, Scrum, Agile, and SAFe DNA in the way we track our work?

## Plan View a la Agile

For Agile I would like to showcase two views, starting with the **Portfolio View** useful to visualise a top-down view of your backlog and associated work.

> Portfolio Plan
>
> ![Agile Planning](/images/agile-planning-choice-4.png)

The other view is **Plans**, which is currently in Preview. It allows you to visualise work for multiple work item types and teams.

> Plans
>
> ![Agile Plans](/images/agile-planning-choice-5.png)

It also has handy visual cues when work items have **unhealthy** dependencies, as in this example where the successor must be completed before the predecessor ... back to the future?!?

> Plans with unhealthy dependencies
>
> ![Pland Unhealthy Liks](/images/agile-planning-choice-6.png)

It also allows you to click on cards with dependencies to see visual lines of the actual dependencies.

> Plans with dependency links
>
> ![Plans Dependency Links](/images/agile-planning-choice-7.png)

What is missing at the time of this writing, hint hint Microsoft, are visual cues of which cards have **healthy** dependencies, so that we do not have to click through dozens of cards to find them!

## Plan View a la SAFe

OK, we demonstrated that we could use the same team to host teams with a Kanban and an Agile mindset and visualise their work. What about SAFe?

Let us use another illustration to speak a few words for us.

> Plans showing portfolio, program, and team levels
>
> ![Plans SAFe](/images/agile-planning-choice-8.png) 

Using the same Plans view, we can visualise the portfolio, program, and team backlogs, using three teams. The Portfolio team is not mapped to any increments, the Program team is mapped to the program increments, and the Teams are mapped to iterations, allowing us to visualise the entire backlog in three different sub-views.

---

# Conclusion

I hope this quick glimpse into our Azure DevOps based demo project, demonstrates that you can use the **product** to visualise a variety of **processes** using the **Agile** process in a single AzDO project. There are a number of views we have not covered, such as the backlog view, taskboard, Feature timeline, and Epic Roadmap. Explore [Azure Boards](https://azure.microsoft.com/en-us/services/devops/boards/) for more details.

For the sceptics, I will conclude with the complete backlog with the test data, from the one and only backlog within the AzDO project, which we viewed through different team/area path lenses.

Thanks for listening.

---

# Above mentioned TEST DATA (CSV) - FYI

```
ID,Work Item Type,Title,Assigned To,State,Tags,Area Path,Iteration Path
267244,Epic,Print Advertising,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
267245,Epic,Digital Marketing,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
267246,Epic,Media (Television & Radio) ,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
267248,Feature,Winter and Spring Direct mail ,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
267249,Feature,Spring Brochures ,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
267250,Feature,Flyers ,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268503,Epic,Authentication,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 98
268504,Epic,Profiling,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 98
268505,Epic,Job Matches,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 98
268506,Epic,Application Tracking ,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 98
268508,Feature,Successful Login,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 98
268509,Feature,Single Sign On,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 98
268510,Feature,Registration,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 98
268512,Feature,Document Uploading,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 98
268513,Feature,Parse Resume Content,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 98
268514,Feature,Manage Profile ,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 98
268515,Feature,Connect to External Job Sites,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 98
268517,Feature,Match Job Positions to Profile ,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 98
268518,Feature,Search for Job Positions,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 98
268519,Feature,Apply to Job Position ,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 98
268520,Feature,Manage Application (employer) ,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 98
268522,Feature,Manage Application (applicant) ,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 98
268524,User Story,Job Search Platform would like a New User to register via Email and Password ,,Closed,MOBILE,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 99
268527,User Story,Job Search Platform would like to create and share the Password rules to a new user who is trying to sign up,demo@demo.com,Closed,WEB,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 99
268548,User Story,Job Search Platform would like the New user to Verify their Email address,demo@demo.com,Active,DEPENDENCY,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 99
268605,User Story,Job Search Platform would like the New user to Verify their Phone number ,demo@demo.com,Active,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 99
268606,User Story,Job Search Platform would like the New user to receive a Welcome Email and Message ,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 21\Iteration 101
268607,User Story,Job Search Platform would like user to be able to use their Google sign-in to sign up on their website,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 21\Iteration 101
268608,User Story,Job Search Platform would like user to be able to use their Facebook sign-in to sign up on their website,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 21\Iteration 103
268609,User Story,Job Search Platform would like user to be able to use their Twitter sign-in to sign up on their website,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 21\Iteration 101
268741,User Story,Job Search Platform would like the new user to be able to login successfully using their Email ID and Password,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 21\Iteration 104
268746,User Story,Job Search Platform would like their user to be intimated when their Login/Password Expires ,demo@demo.com,Active,BLOCKER,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 21\Iteration 102
268760,User Story,Job Search Platform would like the user to be able to change their password,demo@demo.com,Active,PRIORITY,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 21\Iteration 103
268761,User Story,Job Search Platform wants the new user to be able to Upload PDF document to their profile,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 21\Iteration 103
268762,User Story,Job Search Platform wants the new user to be able to Upload Docx files to their profile,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 21\Iteration 101
268770,User Story,Job Search Platform would like the user to be able to Create (and Record) Employment history section,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 21\Iteration 102
268775,User Story,Job Search Platform would like the user to record their Education history,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 21\Iteration 104
268929,Feature,Spring and Summer Issues for Magazines,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268930,Feature,Winter & Spring Newsletters,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268931,Feature,Winter Social Media Marketing,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268932,Feature,Winter Email Marketing (online newsletters) ,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268933,Feature,Search Engine Optimization,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268934,Feature,Search Engine Marketing,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268936,Feature,Television Ad Campaign for Spring and Summer ,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268937,Feature,Radio Ad Campaigns for Spring and Summer,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268939,User Story,Shortlist Postal Codes for Mail marketing,demo@demo.com,Closed,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268940,User Story,Communicate and align with Canada Post to coordinate the mails for the respective postal codes,demo@demo.com,Resolved,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268941,User Story,Decide theme for monthly mail,demo@demo.com,Active,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268942,User Story,Design/create the content of the mail ,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268943,User Story,Print the mail letters,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268944,User Story,Package and deliver monthly mail to Canada Post for distribution ,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268945,User Story,Decide themes for the Posts on Facebook and Twitter for next 2 weeks,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268946,User Story,Analyze Twitter Audience response,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268959,User Story,Check Google Algorithm Update ,demo@demo.com,Active,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268960,User Story,Track Search Engine Ranking,demo@demo.com,Active,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268961,User Story,Add new Keywords to adWords Campaign ,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268963,User Story,Change Social Media Cover Pages,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268964,User Story,Create Monthly Newsletter  for XXX 202X ,demo@demo.com,Active,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268965,User Story,Blog Post on this month's new Features,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268967,User Story,Try a new mail management system,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268968,User Story,Create high level Plan for TV Campaign for the summer,,New,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268969,User Story,Fix 404 Errors,demo@demo.com,Active,,zDemo_Agile_Planning\Agile Kanban,zDemo_Agile_Planning\PI 20\Iteration 98
268972,Task,Write the Code,,Closed,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 98
268973,Task,Test and Debug,,Closed,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 98
268975,Task,Deploy to Prod,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 98
269262,Epic,Search for Flights,demo@demo.com,Active,,zDemo_Agile_Planning\SAFe\Portfolio,zDemo_Agile_Planning\PI 20\Iteration 98
269263,Epic,Purchase Tickets ,,New,,zDemo_Agile_Planning\SAFe\Portfolio,zDemo_Agile_Planning\PI 20\Iteration 98
269264,Epic,Manage Upgrades ,,New,,zDemo_Agile_Planning\SAFe\Portfolio,zDemo_Agile_Planning\PI 20\Iteration 98
269265,Epic,Check-in for flights ,,New,,zDemo_Agile_Planning\SAFe\Portfolio,zDemo_Agile_Planning\PI 20\Iteration 98
269266,Epic,Improve user experience ,,New,,zDemo_Agile_Planning\SAFe\Portfolio,zDemo_Agile_Planning\PI 20\Iteration 98
269275,Epic,Promotion and Rewards ,,New,,zDemo_Agile_Planning\SAFe\Portfolio,zDemo_Agile_Planning\PI 20\Iteration 98
269918,User Story,Job Search Platform would like the user to record their Skill sets,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 21\Iteration 104
272948,User Story,Job Search Platform would like the user to be able to edit Profile information,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning
272965,User Story,Job Search Platform would like their user to connect their profile with LinkedIn,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning
272966,User Story,Job Search Platform would like their user to connect their profile with Indeed,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning
272977,User Story,Job Search Platform would like Automatically match job positions to users' (latest) profiles ,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning
272978,User Story,Job Search Platform would like Automatically match latest job positions to specific criteria,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning
272982,User Story,Job Search Platform would like the user to be able to search for Job positions by Industry or domain ,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning
272983,User Story,Job Search Platform would like the user to be able to search for Job positions by employer,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning
272988,User Story,Job Search Platform would like the user to be able to search for Job positions by skill,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning
273016,User Story,Job Search Platform would like to intimate the employer about a new application that is received,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning
273019,User Story,Job Search Platform would like to send a confirmation email to the applicant once a position is applied for,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning
273022,User Story,Job Search Platform would like the employer to be able to shortlist the various applications received,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning
273030,User Story,Job Search Platform would like to Employer to be able to invite users for interview,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning
273033,User Story,Job Search Platform would like the employer to be able to mark Job positions as hired as necessary,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning
273035,User Story,"Job Search Portal would like the employer to be able to Reject a Job application, as necessary",,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning
273036,User Story,"Job Search Portal would like the employer to be able to save a Job application for later, as necessary",,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning
274602,Feature,Search Criteria ,demo@demo.com,Closed,,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 20\Iteration 99
274603,Feature,UX For Search,demo@demo.com,Closed,,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 20\Iteration 98
274604,Feature,Filter,demo@demo.com,Resolved,WEB,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 20
274605,Feature,Sort,demo@demo.com,Resolved,MOBILE; WEB,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 21
274606,Feature,Price Change,demo@demo.com,Resolved,DEPENDENCY,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 20\Iteration 98
274607,Feature,Class Change,demo@demo.com,Resolved,,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 20\Iteration 98
274608,Feature,Change Connecting Flights,demo@demo.com,Active,,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 20\Iteration 98
274609,Feature,Select/Add to Cart,demo@demo.com,Active,BLOCKER,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 20\Iteration 98
274610,Feature,Review Flight Details,,New,,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 20
274611,Feature,Registration,demo@demo.com,Active,,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 20\Iteration 98
274612,Feature,Payment,,New,,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 20\Iteration 98
274613,Feature,Authentication and Check-in,,New,,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 20\Iteration 98
274614,Feature,Communication,,New,,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 20\Iteration 98
274616,Feature,Newsletters ,,New,,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 20\Iteration 98
274617,Feature,Airline Miles ,,New,,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 20\Iteration 98
274618,Feature,Membership Card,,New,,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 20\Iteration 98
274619,Feature,Customer Care,,New,,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 24
274620,Feature,Feedback Mechanisms,,New,,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 24
274621,Feature,Cancellations and Refund,,New,,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 20\Iteration 98
274622,Feature,Analytics ,,New,,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 20\Iteration 98
274853,User Story,"As a user, I want to be able to search any flight from a particular city to another for a date range",,Closed,,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 20\Iteration 97
274854,User Story,"As a user, I want to be able to choose either one way or Return (two way) flights",,Closed,,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 20\Iteration 98
274855,User Story,"As I user, I want to be able to search flights for multiple passengers",,Closed,,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 20\Iteration 99
274887,User Story,"As a User, I should be able to filter the flights by time of departure and time of arrival at the destination ",,Closed,,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 20\Iteration 99
274891,User Story,"As a user, I want to see the search results page with filters so that I can easily choose my desired flight",,New,,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 20\Iteration 99
274892,User Story,"As a user, I would like to see a clean landing page/homescreen where I can easily add details of my travel",,Closed,,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 20\Iteration 99
274893,User Story,"As a user, I want the site to be simple and intuitive, without overcrowding the screen with unnecessary information",demo@demo.com,Resolved,BLOCKER,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 20\Iteration 98
274894,User Story,"As a user, I would like to view the flights in order of lowest to highest fares",,New,,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 20\Iteration 98
274895,User Story,"As a user, I would like to order the flights that are direct on the top and then with the increasing number of connecting flights ",,New,,zDemo_Agile_Planning\SAFe\Program,zDemo_Agile_Planning\PI 20\Iteration 98
274897,User Story,"As a user, I would like to be informed of cheapest fares 2 days before and after my travel date, so that I can alter my plan if needed",demo@demo.com,Resolved,,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 21\Iteration 104
274898,User Story,"As a user, I would like to be notified if the current lowest fare changes so that I can always be informed of price changes ",demo@demo.com,Active,,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 21\Iteration 105 (Plus 1)
274899,User Story,"As a user, I would like to be informed if I have a chance to get a free upgrade to a higher class ",demo@demo.com,Active,DISCUSSION,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 21\Iteration 104
274900,User Story,"As a user, I would like to be notified if there are discounts or offers running for class upgrades ",,New,,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 22\Iteration 106
274902,User Story,"As a user, I would like to be notified if my connecting flight on a booked itinerary changes ",,New,,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 21\Iteration 105 (Plus 1)
274903,User Story,"As a user, I would like to be able to add a connecting flight from my arrival destination ",,New,,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 22\Iteration 107
274910,User Story,"As a user, I would like to be able to change the connecting flight to a different stop, with necessary price changes",,New,,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 22\Iteration 106
274930,User Story,"As a user, I would like the option of continuing to make a booking in ""Guest Mode"" so that I can book a ticket without signing in",,New,,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 21\Iteration 102
274931,User Story,"As a user, I would like to sign in with my credentials so I can maintain a history of my travel bookings",,New,,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 21\Iteration 103
274933,User Story,"As a Stakeholder, we would like to collect passenger booking details through ""Guest Mode"" so we can establish contact with them in the future",,New,,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 21\Iteration 104
274982,User Story,"As a User, I would like to be able to select the flight option that I see in the Search List ",,New,,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 21\Iteration 101
274983,User Story,"As a User, I would like to review the flight details before proceeding to payment ",,New,,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 21\Iteration 103
274984,User Story,"As a User, I would like to view baggage and any policies with respect to my selection in my 'cart'",,New,,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 21\Iteration 104
274987,User Story,"As a User I would like to have a smooth and easy way of making an online payment, so that I can get through my transaction without hassles",,New,,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 21\Iteration 105 (Plus 1)
274989,User Story,"As a User, I would like to have multiple payment choices like Credit/Debit card, Paypal etc. to make my payment",,New,,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 22\Iteration 106
274990,User Story,"As a User, I should be given the option of saving my card details for easy payments in future",,New,,zDemo_Agile_Planning\SAFe\Teams\Team 1,zDemo_Agile_Planning\PI 22\Iteration 107
275014,Task,Create Sample Text,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 99
275015,Task,Create Interface to record Phone number,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 99
275016,Task,Test the sending of Text,,New,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 99
275017,Task,Create Fields for Email and Password,,Closed,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 99
275018,Task,Create Backend Tables for recording Email and Password,,Closed,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 99
275020,Task,Create ID to recognize each user's credentials,,Closed,,zDemo_Agile_Planning\Agile Standard,zDemo_Agile_Planning\PI 20\Iteration 99
277681,Epic,Airline Vendor Management,,New,,zDemo_Agile_Planning\SAFe\Portfolio,zDemo_Agile_Planning\PI 20\Iteration 100 (Plus 1)
```
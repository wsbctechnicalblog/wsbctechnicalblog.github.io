Title: When should we automate tests
Date: 2022-01-19
Category: Posts
Tags: learning, testing, devops
Slug: when-should-we-automate-tests
Author: Aditya Chourasiya

Summary: This article is gist of brainstorming session among QA team(Mohita Kataria, Midhi Naidu and Aditya Chourasiya) at WorkSafeBC

   Automation is advised when tests are **prone to human error** or **complex** or if they need **repeating**, **reporting** , **execution speed** and ofcourse fetch good **return on investment**. 
   
   On the conterary, test cases for aesthetics, accessibility, one-time, urgent non-regression(hotfixes), exploratory, with unpredictable results and/or with less return on investment,  should not be automated. 
   
<img src="../images/chapline-automation.gif">

# Let's dive in reasons and examples

 These are few reasons to automate (not in order)
- **Repeating** - Apart from typical regression suite this will include running large number of tests, multi platform, multi browser, performance tests, overnight tests or tests with big set of data.
- **Critical path** - If the user action sequence / path or application function is critical to your business, it's recommended to automate.
- **Prone to human error** - large number of data fields, complex technical steps like Database test, Security tests should be automated.
- **Reporting** - Legal, audit, low confidence or high stake tests should be automated for reporting and logs.
- **Execution speed** - parallel and automated execution can help run all sort of test much faster, however planning, automation, triage may take more time depending on type of tests.
- **Return on investment** - While there is no exact number, as a rule of thumb anytime you're saving more money with automation, you should.

 These are few reasons not to automate (not in order)
- **Aesthetics** - User experience , look and feel, colour and images verification require complex human context and interpretation.
- **Accessibility** - Similar to aesthetics, accessibility, usablity, language, grammer etc should be verified manually
- **One-time** - Urgent non-regression hotfix, non-critical, or very small changes can/may be manually verified  
- **Unpredictable results** - Exploratory, time delay tests, random tests can/will rely on manual execution
- **Inadequate return on investment** - Automated test for short lived products, small scale development, duplicate tests should be avoided 

# Summary and invite 
While ability and enthusiasm to automate is important, it is more important to know when to automate and avoid [gold plating](https://en.wikipedia.org/wiki/Gold_plating_(project_management)). I will link the video for discussion in next commit. Thank you for reading. Please feel free to submit a pull request to suggest any changes.


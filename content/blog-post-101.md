Title: Our quest to share our knowledge with the world, keeping it interesting and informal
Date: 2021-07-02
Category: Posts 
Tags: learning
Slug: blog-post-101
Author: Willy-Peter Schaub
Summary: Understand how to navigate and create content for our technical blog.

As an engineer I expect that everyone has the genetic building blocks to (want to) continuously and relentlessly improve, innovate, experiment, and collaborate.

![Engineer](../images/blog-post-101-1.png) 

Collaboration is essential as two or more brains are better than one, exchange ideas, knowledge, experience, and to come up with better ideas and ways of solving problems for today and tomorrow.

All of the above, without letting your ego get in the way, being scared to fail or ask a question, not afraid of seeking candid feedback. 

Our WorkSafeBC technical blog is one of many channels (or hammer) that helps us collaborate and share our experiences and knowledge with everyone. In this short post, I will focus on how to find content relevant to you, and if you are a WorkSafeBC engineer, to create your first post. 

# What do our categories and tags mean?

![Tags](../images/blog-post-101-2.png) 

We **tag** our technical blog posts to allow you, the reader, to find and focus on content that is relevant and valuable to you. It is important to focus on what is valuable to you and skip the "bile".

Here is a list of tags we use when creating new content:

| TAG | FOCUS   |
|-----|---------|
| agile | Agile, Kanban, SAFe, and other frameworks to plan, track, and collaborate across teams. |
| architecture | Software architecture. | 
| automation | Automate repetitive tasks and processes. |
| azure | Microsoft [Azure](https://azure.microsoft.com). |
| azure-devops | Microsoft [Azure DevOps](https://azure.microsoft.com/en-us/services/devops/) services. |
| code | Software coding.
| devops | The union of people, process, and products to enable continuous delivery of value to our end users. - [Donovan Brian](https://www.donovanbrown.com/post/what-is-devops) |
| engineering | Software engineering. |
| event | Meetup, training, workshop, and other event gatherings. |
| feature-flags | Separating deploy from release through feature toggles / flags. |
| learning | Continuous learning. |
| pipelines | Continuous integration, deployment, delivery, YAML, and other interesting topics to build, test, and deploy our software solutions. |
| posters | Quick reference posters and cheat sheets. |
| quality | Technical excellence and quality of engineering solutions to add value, not complexity. |
| security | "Trust, but verify " to avoid and function under malicious attacks. |
| tdd | Test-driven Development. |
| testing | Test to raise the quality bar and deploy with confidence. |
| tips | Tips and tricks. |
| version-control | Secure, version, and collaborate to build better code. |  
| workflow | Streamline repetitive tasks and processes.
| xp | Extreme programming ( XP) software development methodology. |

The list is reviewed as we review new content. Although we are open for change, for example adding new tags or renaming existing tags, we want to keep the churn and number of tags to an absolute minimum.

![Category](../images/blog-post-101-4.png) 

We are starting to also **categorise** our content to add a different lens for you to use to find relevant content. Here is a list of categories we use:

| CATEGORY | MEANING |
|----------|---------|
| Events   | Specific updates covering events, such as meetups and workshops. |
| Posts    | Updates by our engineers and other interesting individuals, sharing their knowledge with the world. |

Thoughts? How can we improve our tags and categories? Please ping me on [@wpschaub](https://twitter.com/wpschaub) and help us improve our content.

# Create your first post

![Tags](../images/blog-post-101-3.png) 

> [Blog Interesting - 32 Ways to Keep Your Blog from Sucking](https://www.hanselman.com/blog/blog-interesting-32-ways-to-keep-your-blog-from-sucking), by Scott Hanselman!

If you are working with or you are a WorkSafeBC engineer, you have invaluable technical knowledge and experience to share! Here is a 7-step checklist to get you started:

-  Understand [markdown](https://www.markdownguide.org/). Our blog posts, such as this one, are developed using the simple and easy-to-use markup language.
- Collaborate with the **WSBC Technical Blog Content Discussion** working group, which you can locate in Microsoft Teams.
- Clone our [wsbctechnicalblog-wsbctechnicalblog.github.io](https://github.com/wsbctechnicalblog/wsbctechnicalblog.github.io) repository.
- Create a feature branch ```<yourname>/<title>```, for example willys/blog-post-101. Do not use your primary, 2, or 5-ID!
- Create a new markdown file in the ```/content```, for example ```/content/blog-post-101.md``` and add the metadata header at the start, which will be used when your gem is converted to a live HTML page.

```
Title: <catchy title>
Date: YYYY-MM-DD
Category: <Events|Posts>, as above mentioned 
Tags: <Tags> comma separated, as above mentioned
Slug: Your <file-name> without the .md
Author: <FirstName> <LastName>
Summary: <Quick summary of what post is about>.
```

- Create your content using the editor of your choice n- mine is Visual Studio Code.
- Create a pull request and submit your changes for review and collaboration.

![Tags](../images/blog-post-101-5.png) 

Done!

# One, two, or more authors?

![Tags](../images/blog-post-101-6.png) 

Unfortunately, we can only define one author in the metadata, however, you can co-author a post with a colleague or with a member from our **WSBC Technical Blog Content Discussion** working group. We are more than happy and keen to assist you, even as an unknown ghost writer. 

Just collaborate with us, ask questions (_the only one that is bad is the one you never ask_), and do not hesitate to ask for help.

# To conclude

If you are a reader of our technical blog post, please to not hesitate to give us candid feedback to help us improve our content. 

If you are a WorkSafeBC'tonian, this post will hopefully serve as an inspiration for you to start and to keep on blogging. We are waiting for your call and/or your pull request!

![Tags](../images/blog-post-101-7.png) 


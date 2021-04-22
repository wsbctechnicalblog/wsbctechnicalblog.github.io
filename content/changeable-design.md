Title: Only changeable design is good design
Date: 2021-04-22
Category: Posts
Tags: Agile, Design, Programming
Slug: only-changeable-design-is-good-design
Author: Alex Bunardzic
Summary: Why is changeable design desirable and what's preventing us from achieving it

I started my coding career in August 1990. Back then, it was customary to write code in full isolation. My first paid job was writing COBOL applications to run on IBM midrange computers. The programs I was writing were monoliths that included everything, from database operations to green screen operations in one big, humongous program (unbeknownst to me, even back then I was a ‘full stack’ developer).
 
Back then, the only design activities I was aware of doing was the database design (attempting to achieve the 3rd normal form). After a relatively short stint with COBOL I moved into the desktop-centric fat-client/server world (C++, SQL Server and Windows NT), and then into Java and web development. At that point, it became obvious that without having good design skills, we tended to quickly end up with a [Big Ball of Mud](https://en.wikipedia.org/wiki/Big_ball_of_mud#In_computer_programs) systems.
 
## Traditional design
 
Traditionally speaking, design is something we work on and then when finished, it gets delivered. Ideally, by finishing the design activities, we hope to have achieved the most optimal design. As such, the design reaches its final form and is not to be further modified.
 
The goal is to deliver non-volatile design, and in most real-life situation that goal makes perfect sense.
 
## Software design
 
Interestingly, software design does not work the same way as when designing material objects. Software is by its very nature and by intent malleable and pliable (hence the word ‘soft’ as part of its name). As such, software is supposed to be volatile. If software solution hardens, it immediately becomes useless.
 
## What prevents changeable software design?
 
A non-surprising answer to this question is that the lack of design skills prevents us from producing changeable design (duh!)

Back in the <strike>good</strike> old days (before Extreme Programming arrived on the scene) I was spending years writing code all by myself. Not surprisingly, I’ve spent all those years not learning much about software design. Of course, unbeknownst to me, I was stuck in the much-dreaded Expert Beginner state.
 
Luckily, after joining a mature team of software engineers, I started getting exposed to pair programming and continuous code reviews. Boy, was I in for a shock at that juncture! What I considered good coding practices was shredded to pieces by my older and more experienced peers.
 
But the pain was worth enduring, because I was finally set on the path of continuous improvement. No pain, no gain, but in hindsight, the pain of being heavily scrutinized by my peers was truly worth it. So, a few factors that contribute to preventing us from producing changeable software are (in no particular order):
 
1. Lack of real communication with peers
1. Rework avoidance
1. Lack of regard for testability
1. Absence of Continuous Integration
 
Let’s quickly review the above four factors.
 
## Lack of real communication with peers
 
Working in isolation by being assigned a ticket or a work item by the managers/scrum masters is not a good way to write software. If the only communication with peers happens during the 15 minutes of daily standups, the quality of the solution will suffer because the design will most likely end up being rigid, difficult, and risky to change. Which is never a good position to be in.
 
## Rework avoidance
 
Hoping in vain to be able to deliver a solution that will be correct on the first try is extremely unrealistic. However, oftentimes the organizational culture is centered around rework avoidance (i.e. “if it’s worth doing at all, then it must be done right on the first try”).
 
Software is not like that. Software development activities fail if they attempt to mimic activities focused on building material objects. Software development is more akin to writing an essay. If you recall from the school days, when we’re writing an essay, we always start form the first draft, and then iterate, refining the draft until we get the draft into a more presentable shape. In other words, we keep doing the rework on our draft (we keep changing the design and the content we’ve already changed), because we are aware that it is not possible to produce quality design and content on the first pass.
 
In software, we call that rework refactoring. Without constant refactoring (i.e. doing it every step of the way), it is not possible to produce changeable design.
 
## Lack of regard for testability
 
Not all software developers have testability as the most important part of their discipline. Some leave testing to a separate, independent teams (QA). Developing software with such mindset prevents changeable software design.
 
When adding source code statements to the repo without first designing the intended code behaviour for testability, the resulting design is tightly coupled. Any tightly coupled system is not testable. And not being testable, it poses serious risks to making changes to it. That way, we end up with the design that is not changeable.
 
## Absence of Continuous Integration
 
Working in isolation fosters the large batches approach. A developer takes a user story or a task to work on and disappears from the radar to spend long hours writing code. Such approach typically results in having many changes made to the code without any regard to the other changes that have possibly been made to the code by other peers working in isolation.
 
When the time eventually comes to put all those changes together to assemble a working system, we often learn that the changed code does not work. We then must scramble to somehow resolve those conflicts, and in the process produce a lot of half-baked design. Which results in a design that is difficult and risky to change.
 
## How to achieve changeable design?
 
Simply put, to achieve changeable design we must make sure to avoid factors that prevent us from delivering changeable design. In practical terms, the recommended approach is:
 
1. Replace asynchronous communication with real-time collaboration (pair and mob programming)
1. Practice continuous refactoring
1. Adopt full-on TDD, service virtualization and BDD
1. Integrate all changes continuously
 
Title: Make yourself interruptible
Date: 2022-01-05
Category: Posts
Tags: quality, technical-excellence, TDD, eliminate-waste, agile, devops
Slug: make-yourself-interruptible
Author: Alex Bunardzic
Summary: Adopt humble approach when creating software products by making yourself open to interruptions

![Interrupt](../images/Interrupt.png)

Let's take one simple example: suppose I'm a programmer writing code and I use Notepad to do it. I can lock myself in my office and keep writing code in the Notepad for hours without being interrupted. I'm a professional programmer and I know what I'm doing, right?

Suppose now I upgrade from Notepad to a sophisticated code editor. If I continue writing code the way I used to do with Notepad, I will start getting interrupted. Why? Because sophisticated code editors are opinionated and will push back if I attempt to write syntactically incorrect code. Notepad, on the other hand, couldn't care less if the code I wrote is correct or not.

Suppose now I upgrade to an even more sophisticated code editor that on every diff runs all tests in the background. The moment any test fails, the editor interrupts my coding session and demands that I fix the failing test.

Suppose now I upgrade to an even more sophisticated code editor that on every diff runs all tests in the background, and when all tests pass it runs mutation testing. If there are any surviving mutants, it interrupts my coding session and demands that I kill all surviving mutants before I could continue writing code.

All those interruptions are extremely desirable if we care at all about the quality of our work.

## Are interruptions slowing us down?

Common sense thinking is prone to viewing interruptions as a speed bump. If I know exactly what I’m doing, what’s the point in me being interrupted? My flow will slow down, and the delivery will inevitably suffer.

Few years ago, I went to IKEA and purchased a large bookshelf. Brought it home, unpacked it, and studied the instruction sheet. Since I’m an engineer by training, I was confident that I completely understood the prescribed process of assembling the shelf.

I jumped into action and spent a few hours working on the big shelf without any interruptions. When I was finished and stood the shelf up, I realized that I have assembled it incorrectly – it looked the way a normal shelf would look when viewed in a mirror! Obviously, the shelf was not safe to use in such botched shape, so I had to disassemble it and then reassemble it following the instruction sheet very carefully.

So, what was happening now that I realized the importance of respecting and following the instruction sheet to the letter? I started getting many, many interruptions while I was working on it. Those interruptions were slowing down the flow of work. I had to stop my work, put down the tools and the parts of the shelf I was holding in my hands, bring the instruction sheet up to my attention, and study it carefully before making the next decision. That took some extra time.

However, overall, I finished the shelf in less than half the time it took me originally to assemble it, realize it was botched, disassemble it, and then waste time on few expletives.

I now apply the same approach to creating software. I welcome interruptions. Any time I make a change to the code, I invite the system to run and let me know if my change broke anything. If it did, I reset the system to its previous working state, and try again. If it didn’t break anything, I continue confidently, knowing that the software I’m creating is always in its fully functional state.

And that, in my experience, is the fastest way to work and release software.
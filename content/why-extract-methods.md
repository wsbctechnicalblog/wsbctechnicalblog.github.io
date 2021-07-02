Title: Why extract methods when modifying legacy code?
Date: 2020-10-16 10:20
Category: Posts
Tags: code, quality, testing
Slug: why-extract-methods
Author: Alex Bunardzic
Summary: Legacy code is hard to test, so extract methods by writing micro tests

Allow me a bit of introspection. I’ve been in Software Engineering field for 30 years. During those 30 years I modified a lot of legacy software. Here is how I would typically do it:

Over the years I have formed certain habits when working with legacy code. Because on most projects I get paid to deliver working software that is easy to maintain, I cannot afford the luxury of taking my sweet time trying to fully understand the legacy code I am about to modify. So I tend to skim. Skimming the code helps me quickly identify relevant portions in the repo. It is a race with time, and I don’t have cycles at my disposal to dwell on less relevant minutia. I’m always going for the most relevant area in the code. Once I find it, I slow down and start analyzing it.

I rely heavily on IDEs (power tools). Doesn’t matter which power tool, these days they’re all pretty much capable of doing the same thing. What’s important to me is the ability to quickly find where functions are called and where variables are used.

Sooner or later, after I’m done skimming the code and analyzing the code segment I’m intending to change, I identify a place where I want to insert some code. Now that I understand the meaning of the classes, components, objects involved in performing the function, I first write a test.

Following that, I write code to make the test pass. I type the name of the object I intend to use, and then press the period (dot, or “.”) key. Immediately, IDE responds with giving me a full list of methods defined for that object. All those methods are callable from the location where my cursor is.

I then pick the method that makes sense to me. I fill in the blanks (i.e. supply values for the expected arguments/parameters), save the change, and run the test. If the test passes, I’m done with that micro change.

The above activity typically gets repeated many times per hour. Throughout the workday, it is not unusual to see the above activity repeated dozens, even hundreds of times.

I believe the above description of the way I modify software is not unique to the way I formed my work habits. I believe it describes a typical flow that many (I’d even say most) software engineers adhere to.

## A few observations

The first thing that is apparent after observing the above described way of modifying legacy software is the absence of any work on documentation. Experience has shown that software developers very rarely spend time reaching out for documentation. Time spent preparing the documentation and generating it to produce HTML-style online documents is time wasted.

Instead, most developers rely solely upon power tools (IDEs). And rightly so (IDEs never lie, as they always offer the real-time picture of the system we are modifying; documentation is more often than not stale).

Another thing worth noticing is that developers don’t read the source code the way it was written. When writing code from scratch (first pass), many developers tend to write in long functions. Source code tends to bunch up. Bunching code up makes it easier to read and reason about on the first pass, and also makes it easier to debug. But after the first pass is finished, people rarely, if ever, consume the code the way it was written. If we catch ourselves reading a whole function from beginning to end, it is most likely due to the fact that we have exhausted all other options and have no choice but to slow down and read the code in a pedestrian way. However, in my experience, that slow and orderly reading of the code seldom happens.

## Problems caused by the bunched up code

If we were to leave the code as it was written during the first pass (i.e. long functions, a lot of bunched up code to enable easy initial understanding and debugging), it would render IDEs powerless. If we cram all capabilities an object can offer in a single giant function, later on when trying to utilize that object, IDEs will be of no help. IDEs will only show the existence of one method (which will probably contain a large list of parameters providing values that enforce the branching logic inside that method). So we won’t know how to really use that object unless we open its source code and read its processing logic very carefully. And even then, our heads will probably hurt.

Another problem with hastily cobbled up, ‘bunched up’ code is that its processing logic is not testable. While we can still write an end-to-end test for that code (input values and the expected output values), we have no way of knowing if the bunched up code is doing any other potentially risky processing. Also, we have no way of testing for edge cases, unusual scenarios, difficult-to-reproduce scenarios etc. That renders our code untestable. Which is a very bad thing to live with.

## Break up bunched up code by extracting methods

Long functions/methods are always a sign of muddled thinking. When a block of code contains numerous statements, it usually means that it is doing way too much processing. Cramming a lot of processing in one place typically means we haven’t carefully thought things through.

One need not look further than into how companies are typically organized. Instead of having hundreds of employees working in a single department, companies tend to break up into numerous smaller departments. That way, it is much clearer where responsibilities lie.

Software code is no different. An application exists in order to automate a lot of intricate processing. Processing gets broken into a number of smaller steps, so each step must be mapped onto a separate, isolated block of code. We create such separate, isolated and autonomous block of code by extracting methods. We take a long, bulky block of code and break it up by extracting responsibilities into separate blocks of code.

## Extracted methods enable better naming

Software code is written by developers, but in actuality it is much more often consumed (i.e. read) by developers than it is written.

When consuming software code, it helps if the code is expressive. Expressiveness boils down to proper structure and proper naming. Consider the following statement:

`if((x && !y) && !b) || (b && y) && !(z >= 65))`

It would be literally impossible to understand the meaning and the intention of the above statement without actually running the code and stepping through it with a debugger. Such activity is what we call GAK (Geek at Keyboard). It is 100% unproductive, and is quite wasteful.

Here is where extract method and naming come to the rescue. Take the complex statement contained within the if statement, extract it into its own method, and give that method a meaningful name. For example:

`public bool IsEligible(bool b, bool x, bool y, int z) {`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`return ((x && !y) && !b) || (b && y) && !(z >= 65);`

`}`

Now replace the ugly if statement with a more readable statement:

`if(IsEligible(b, x, y, z))`

Of course, we should also replace dumb one character variable names with more meaningful names to improve readability.

## Reuse in legacy code

Experience shows that any functionality that is not extracted and properly named and moved to the most reasonable class will never be reused. Extract method fosters frequent reuse, which goes a long way toward improving code quality.

## Testing the legacy code

Writing tests for the existing code is hard and feels less rewarding than doing TDD. Even after we identify that there should be several tests that ensure production code works as expected, when we realize that production code has to be changed to enable testing, we often decide to skip writing tests. Our goals to deliver testable code slowly but surely keep diminishing.

Writing tests for the legacy code is tedious because it often requires to spend a lot of time and code to set up the preconditions. That’s the opposite of how we write tests when doing TDD, where time spent on writing preconditions is minimal.

Best way to make legacy code testable is to practice the extract method approach. Locating a block of code nested in loops and conditionals and extracting it will enable us to write small precise tests. Such tests on extracted functions improve not only the testability of the code, but also the understandability. If legacy code now becomes more understandable thanks to extracting methods and writing legible tests, chances of introducing any defects are drastically reduced.

## Conclusion

Most of the discussion pertaining to extracting methods would not be necessary when we’re doing TDD. Writing one test first and then making the test pass, then scanning that code for more insights into how the code should be structured and improved, making improvements, and finally making changes part of the code base will guarantee that there will be no need to worry about extracting methods. Since legacy code usually means code that was not crafted following TDD methodology, we are forced to adopt a different approach. In my experience, extract methods gives us the biggest bang for the buck when it comes to modifying legacy code while avoiding risks of breaking the functionality.

<br /><br />
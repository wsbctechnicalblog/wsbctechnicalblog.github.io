Title: Incremental and Iterative Development – what’s the diff?
Date: 2021-03-19
Category: Posts
Tags: Incremental-development, Iterative-development, Agile, DevOps
Slug: incremental-and-iterative-development
Author: Alex Bunardzic
Summary: Visual example illustrating the fundamental differences between incremental and iterative development process.

I oftentimes hear people discuss development methodologies and mention incremental and iterative approaches. When I ask for further clarification, it surprises me how frequently people conflate the two methodologies. I hear “well, they’re just two words denoting the same thing”.

Which is far from being true. Let’s now examine what makes one development process iterative and another development process incremental, and let’s then look into what makes them so fundamentally different.
<br /><br />
## Iterative development

According to the dictionary, to iterate implies “to perform or utter repeatedly”. Repetition is the essence of iteration. In software engineering, we often call iteration by another name – rework.

This distinction sometimes gets misinterpreted, so I’d like to illustrate what is meant by the expression ‘iterative development’, and I’d like to use a series of visual examples.

Let’s start with the first iteration (or a first pass). The initial draft may look something like this:

![Mona Lisa Iteration 1](/images/monalisa/monalisa1.png)

Since the above draft is very vague and unclear, we need to revisit our first draft and do a bit of rework, in the hopes of adding some clarity:

![Mona Lisa Iteration 2](/images/monalisa/monalisa2.png)

The picture now is a little bit clearer, but still it is obvious it needs more work (rework). So we iterate, and the third iteration looks like this:

![Mona Lisa Iteration 3](/images/monalisa/monalisa3.png)

A bit better, yeah? Still, quite fuzzy. Let’s do the fourth iteration:

![Mona Lisa Iteration 4](/images/monalisa/monalisa4.png)

Ah okay, maybe now with the fourth iteration some eagle-eyed people can already recognized what are we making? Still, needs more rework. On to the fifth iteration:

![Mona Lisa Iteration 5](/images/monalisa/monalisa5.png)

Oh, that kind of looks familiar. Just to be sure, let’s do more rework; iteration 6:

![Mona Lisa Iteration 6](/images/monalisa/monalisa6.png)

It’s a portrait of a woman, and maybe even a very famous portrait. Let’s add more details; iteration 7:

![Mona Lisa Iteration 7](/images/monalisa/monalisa7.png)

Aha, looks like Leonardo da Vinci’s famous Mona Lisa! Definitely. But it looks quite crude – we need to do some more rework. Iteration 8:

![Mona Lisa Iteration 8](/images/monalisa/monalisa8.png)

Now there’s no doubt – it is Mona Lisa! If we squint we can definitely be sure. But it lacks a lot of detail still. Iteration 9:

![Mona Lisa Iteration 9](/images/monalisa/monalisa9.png)

The details are starting to emerge. Still looks amateurish. More rework; iteration 10:

![Mona Lisa Iteration 10](/images/monalisa/monalisa10.png)

The expression on Mona Lisa’s face is now visible. Let’s keep going; iteration 11:

![Mona Lisa Iteration 11](/images/monalisa/monalisa11.png)

Almost there! Still somewhat pixelated, we will circle back one more time to increase the resolution. Iteration 12:

![Mona Lisa Iteration 12](/images/monalisa/monalisa12.png)

Voila! That’s it. Gradual refinement delivers the masterpiece!
<br /><br />
## Incremental development

According to the dictionary, to increment means “an increase or addition, especially one of a series on a fixed scale”.

Let’s illustrate incremental development using Da Vinci’s Mona Lisa.

First increment:

![Mona Lisa Increment 1](/images/monalisa/monalisaincrement1.png)

Second increment:

![Mona Lisa Increment 2](/images/monalisa/monalisaincrement2.png)

Third increment:

![Mona Lisa Increment 3](/images/monalisa/monalisaincrement3.png)

Fourth increment:

![Mona Lisa Increment 4](/images/monalisa/monalisaincrement4.png)

Fifth increment:

![Mona Lisa Increment 5](/images/monalisa/monalisaincrement5.png)

Sixth increment:

![Mona Lisa Increment 6](/images/monalisa/monalisaincrement6.png)

And so on…
<br /><br />
## What are the differences between iterative and incremental development?

I hope that the visual illustrations above are helpful in driving the salient points home. Let’s enumerate the differences:

- Unlike iterative development, which starts with the whole picture (the whole system), incremental development starts from one fixed part of the system
- Unlike iterative development, which outlines the whole system in very crude strokes, incremental development works on an isolated fixed part of the system until is fully done (following the Definition of Done, or DoD)
- Unlike iterative development, which is based on relentless rework, incremental development forbids rework, and only moves on to work on the next part of the system once the previous part is fully fleshed out and frozen for any further changes

<br />
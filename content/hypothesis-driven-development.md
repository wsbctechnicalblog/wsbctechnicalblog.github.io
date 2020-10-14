Title: Hypothesis-Driven Development
Date: 2020-10-13 12:20
Tags: TDD, CI
Slug: hypothesis-driven-development
Author: Alex Bunardzic
Summary: Developing a feature without formulating a hypothesis is like shooting in the dark

_“The only way it’s all going to go according to plan is if you don’t learn anything.”_ -Kent Beck

Experimentation is the foundation of the scientific method, which is a systematic means of exploring the world around us. But experimentation is not only reserved for the field of scientific research. It has its central place in the world of business too.

Most of us are by now familiar with the business methodology called Minimum Viable Product (**MVP**). This Minimum Viable Product is basically just an experiment. By building and launching MVPs, business operations are engaging in a systematic means of exploring the markets.

If we look at market leaders today, we learn that they’re not doing projects anymore. The only thing they’re doing is experiments. **Customer discover**y** and **Lean strategies** are used to test assumptions about the markets. Such approach is equivalent to Test-Driven Development (**TDD**), which is the process we are intimately familiar with. In TDD, we write the hypothesis first (the test). We then use that test to guide our implementation. Ultimately, product or service development is no different than TDD – we first write a hypothesis, that hypothesis guides our implementation which serves as measurable validation of the hypothesis.

## Information discovery

Back in the pre-agile days, requirements gathering was an important activity that used to always kick-off the project. A bunch of SMEs used to get assigned on the project, and were tasked with gathering the requirements. After a prolonged period of upfront information discovery, the gathered requirements got reviewed and, if agreed upon, signed off and frozen. No more changes allowed!

Back then it seemed a perfectly reasonable thing to do. The fly in the ointment always kicked in once the build phase commenced. Sooner or later, as the project progresses, new information comes into the light of day. Suddenly, what we initially held as incontrovertible truth, gets challenged by the newly acquired information and evidence.

But the clincher was in the gated phases. Remember, once requirements get signed off, they get frozen. No more changes, no scope creep allowed. Which means, newly obtained market insights get willfully ignored.

Well, that’s kind of a foolish neglect. More often than not, the newly emerging evidence could be of critical importance to the health of the business operation. Can we afford to ignore it? You be we cannot! We have no recourse other than to embrace the change.

It is after a number of prominent fiascos in the industry that many software development projects switched to the agile approach. With agile, information discovery is partial. With agile we never claim that we have gathered the requirements, and are now ready to implement them. We keep discovering information and implementing it at the same time (we embrace the change). We do it in tiny steps, keeping our efforts interruptible and steerable at all times.

How to leverage the scientific method

Scientific method is empirical and consists of performing the following steps:

- Step 1: make and record careful observations

- Step 2: perform orientation with regards to observed evidence

- Step 3: formulate a hypothesis, including measurable indicators for hypothesis evaluation

- Step 4: design an experiment that will enable us to test the hypothesis

- Step 5: conduct the experiment (i.e. release the partial implementation)

- Step 6: collect the telemetry that results from running the experiment

- Step 7: evaluate the results of the experiment

- Step 8: accept or reject the hypothesis

- Step 9: go to Step 1

## How to formulate a hypothesis

When switching from projects to experiments, traditional user story framework (As a/I want to/So that) is proving insufficient. The traditional user story format does not expose the signals needed in order to evaluate the outcomes. Instead, old school user story format is focused on outputs.

The problem with doing an experiment without first formulating a hypothesis is that there is a danger of introducing a bias when interpreting the results of an experiment. Defining the measurable signals that will enable us to corroborate our hypothesis must be done before we conduct the experiment. That way, we can remain completely impartial when interpreting the results of the experiment. We cannot be swayed by wishful thinking.

The best way to proceed with formulating a hypothesis is to use the following format:

**We believe** [this capability]

**Will result in** [this outcome]

**We will have the confidence to proceed when** [we see a measurable signal]

## Working software is not a measure of progress

Output-based metrics and concepts (Definition of Done, acceptance criteria, burndown charts, and velocity) are good for detecting working software, but fall miserably when it comes to detecting if working software adds value.

“Done” only matters if it adds value. Working software that doesn’t add value cannot be declared “done”.

## The forgotten column

Technology-centric projects break activities down into four columns:

1. Backlog of ideas

2. Analysis

3. In progress

4. Shipped

The above structure is based on the strong belief that all software that works is valuable. That focus must now shift toward continuously delivering real value, something that serves customers. Agilists value outcomes (value to the customers) over features.

The new breakdown for hypothesis-driven development looks something like this:

<table>
<tr>
  <th>
    <td><strong>Ideas backlog</strong></td>
    <td><strong>Analysis</strong></td>
    <td><strong>In progress</strong></td>
    <td><strong>Shipped</strong></td>
    <td><strong>Achieved desired outcome</strong></td>
  </th>
  </tr>
  <tr><td>&nbsp;</td>
  <td>Hypothesis 11</td><td>Hypothesis 20</td><td>Hypothesis 2</td><td>Hypothesis 1</td><td></td>
  </tr>
  <tr><td>&nbsp;</td>
  <td>Hypothesis 12</td><td>Hypothesis 21</td><td>Hypothesis 5</td><td>Hypothesis 5</td><td></td>
  </tr>
  <tr><td>&nbsp;</td>
  <td>Hypothesis 13</td><td></td><td></td><td>Hypothesis 10</td><td></td>
  </tr>
  <tr><td>&nbsp;</td>
  <td>Hypothesis 14</td><td></td><td></td><td></td><td></td>
  </tr>
  <tr><td>&nbsp;</td>
  <td>Hypothesis 15</td><td></td><td></td><td></td><td></td>
  </tr>
  <tr><td>&nbsp;</td>
  <td>Hypothesis 16</td><td></td><td></td><td></td><td></td>
  </tr>
  <tr><td>&nbsp;</td>
  <td>Hypothesis 17</td><td></td><td></td><td></td><td></td>
  </tr>
  <tr><td>&nbsp;</td>
  <td>Hypothesis 18</td><td></td><td></td><td></td><td></td>
  </tr>
  <tr><td>&nbsp;</td>
  <td>Hypothesis 19</td><td></td><td></td><td></td><td></td>
  </tr>
</table>

All eyes must remain peeled on the **Achieved desired outcome**.
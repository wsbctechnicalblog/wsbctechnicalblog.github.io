Title: How to create deterministic tests
Date: 2021-11-09
Category: Posts
Tags: technical-excellence, delivery-on-demand, continuous-delivery, tdd
Slug: deterministic-tests
Author: Alex Bunardzic
Summary: Quality of automated tests is the most important aspect of continuous delivery

![Law of Demeter](../images/nondeterministic.jpg)

In my previous post [Do not automate anything unless you automate the tests](/automate-tests.html) I discussed the importance of having full test coverage for any automated operation in the system. This episode will elaborate on that by looking into factors that enable automated tests to run deterministically.

Generally speaking. there are two types of tests:

1. Exploratory tests
1. Automated tests

Exploratory tests are not part of the continuous delivery flow. Usually performed by QA engineers (in collaboration with other team members), these tests are experimental in nature and are focused on disrupting the system _status quo_. The aim of exploratory tests is to expose potential vulnerabilities in the automated system. If vulnerabilities get discovered during the exploratory testing spike, a remedy solution gets engineered and implemented. The system thus grows more resilient, less fragile.

Automated tests, on the other hand, are part and parcel of the continuous delivery flow. As a matter of fact, continuous delivery is not possible without a comprehensive suite of automated tests.

Continuous delivery is only possible if automated tests that are underpinning the delivery are deterministic. If the automated tests are not 100% deterministic, engaging in continuous delivery becomes risky. If the risk compounds, we are at the danger of experiencing outages and defects caused by the continuous delivery. Once that starts happening, we would be forced to discontinue the continuous delivery, and would fall back to the slow and sluggish scheduled delivery model.

## What are deterministic tests?

Deterministic tests are tests that are repeatable. If we have a test that delivers certain results when we run it, and then if we run it again it delivers different results, that test is not deterministic.

Tests that are not deterministic are not only useless, but they are also harmful. They have capacity to mislead us. As such, non-deterministic tests must be avoided at all cost. It is better not having any tests than having non-deterministic tests.

## How to recognize non-deterministic tests?

It is relatively straightforward to detect non-deterministic tests. If a test we are creating or modifying/examining depends on some other tests, it is a clear sign that it is a non-deterministic test.

Any tests that depend on some sequence of events that are scheduled outside of the body of the test are non-deterministic. Automated tests must be immune to any sequence of events that happen in the system under test.

In addition to that, any test that depends on hidden inputs is a non-deterministic test. A typical example would be a test that depends on the system clock. System clock is a hidden input, which means that at the time the test gets executed, it is impossible to predict the value of that input. A system clock provides the test with the value (usually in milliseconds). That value changes with the passage of time (every millisecond that value is different). The test whose assertion depends on that hidden value cannot ever be deterministic.

Similarly, tests that rely on any other non-explicit values (entering the test via a network, or some I/O operation) are non-deterministic. Also, tests that depend on some value that is part of the shared mutable state are non-deterministic tests. Such tests must be banned from the repo.

## Create only quality tests

As we’ve seen, not all automated tests are equally valuable. Some are downright harmful. Our goal is to hone our skills to only create high value, high quality automated tests. That way we will pave the way to the ultimate engineering goal – delivery on demand, not on the predefined schedule.

## So, what are quality tests?

To begin with, each test must isolate **one failure mode only**. A test that detects and measures two or more failure modes is low quality test.

What is one failure mode? It is a single expectation of how we intend the system to behave. A quality test should never combine two or more such expectations. For example, we must never create a test that expects the system to calculate monthly installment rate AND craft the notification message to the client. Those are two separate expectations, and those expectations must have two separate automated tests.

It goes without saying that the above two separate tests are completely independent of each other. We must make sure to create our expectations in such a way that the sequence of execution does not matter.

Next thing to strive for is speed. As we keep creating more and more such isolated automated tests, we want to be able to run them at will. The decision when to run all tests should never be an issue. All tests must always run, without incurring any speed bumps. Ideally, any time we make any changes to our system, we must run all tests. That means that tests must be designed to run in memory. No suite of tests should take more than several seconds to run.

The onus is therefore on us, the designers of automated tests, to pay close attention to how are we going to design them so that they don’t consume more than few seconds of running time. Being able to get to that level of design skills takes a lot of practice. It is therefore recommended that engineers attend TDD Dojo sessions where they can gain those skills by working together (mob programming).

If we are running all tests after we make any change to our system, that implies that all tests are repeatable. Any time tests run they produce identical results. I was at one point managing a software development department that released faulty code to production. During the _postmortem_ we discovered that engineers have disabled some tests in the pipeline. When asked why, they replied that the tests were failing which was preventing them from releasing the code to production. When asked why those tests were failing, the engineers replied: “There were some TEMPORAL dependencies!”

‘Temporal dependencies’ is just a fancy phrase for ‘tests are not isolated; they are not independent’. Meaning, they are poor quality tests.

Moral of the story: it is crucially important to make sure that each test is completely isolated and independent from any other events in the system.

## Conclusion

Automated tests should be viewed as the Oracle. They should be able to predict the future. If we go to the Oracle and ask: “Is it safe to release this code to production?”, the Oracle must be able to give us a clear Yes or No answer. If all tests pass, that’s the Oracle’s Yes answer. If even one test fails, that the Oracle’s No answer.

If the Oracle answers with Yes (i.e., all test pass), and if we deploy to production but then the deployed code blows up, we lose confidence in the Oracle. We realize that the Oracle is flaky and is not capable of predicting the future. When that happens, we start feeling reluctant when it comes to writing automated tests. What’s the point in wasting time on writing those tests if they cannot tell us if it’s safe to proceed or not?

It is for that reason that we must make our automated tests fully deterministic. Tests that always behave according to the expectations regardless of the conditions (i.e., the underlying computing machinery, the time of day, week, month, year, the network status, the I/O operations, presence of shared mutable values, etc.) are deterministic tests. They support a predictable system. Such predictable system is completely immune to any perturbations that may occur in the operating environment. The magic word that makes that happen is _isolation_.

Once we get to that level of technical excellence, we can safely engage in continuous delivery (a.k.a. delivery on demand).
Title: Client-side expressiveness and security
Date: 2021-05-28
Category: Posts
Tags: DevSecOps, FrontEndDevelopment, CloudOps, Security
Slug: client-expressiveness-and-security
Author: Alex Bunardzic
Summary: The importance of properly securing client-side applications has never been more urgent!

>_“In the beginning was the hyperlink, and the hyperlink was with the web, and the hyperlink was the web. And it was good.” -Anonymous_

Modern web development demands heavy client-side processing logic. The days of simple HTML forms with the Submit button are long gone; nowadays, end-users expect feature-rich functionality available in their browsers.

Sounds great, right? Yes, but what about that pesky little browser? It’s a well-known fact that all browsers are notorious for being **untrusted computing environments**.

## What do we mean by ‘untrusted computing environment’?

If we are to enable client-side expressiveness (i.e. enable front-end developers to implement sophisticated and elaborate processing of business policy rules), we must give developers advanced, powerful tools. So, what’s wrong with that? Giving sophisticated, powerful tools to developers sound like a great way to improve quality and productivity.

True, however the problem is that giving those tools to our developers also means we are giving the same tools to potentially hostile end-users.

How is that possible? Well, the inherently untrusted computing environment, such as a web browser, opens the possibility of easily hacking into our system and exploiting various loopholes. Web browser is a very permissive application which allows anyone to inspect and examine what is going on under the hood.

## How does client-side processing logic work?

Front-end applications need to request values that are stored on the back end. Then, once the requested values are delivered in the response, the front-end app displays the values to the end user and awaits further action initiated by the user. The user can make some modifications to the displayed values and then request that those modifications be processed and stored on the back end. The front-end app accomplishes that by sending the request back to the server.

In the early days of web apps, the above described processing logic on the client was implemented using plain vanilla HTML. Soon after the e-commerce revolution picked up, it became obvious that such static, pedestrian way of processing business policy rules was woefully insufficient and inadequate. The client-side apps had to be enhanced by some custom processing logic. Enter JavaScript in the browser.

With JavaScript running in the browser, suddenly the sophistication levels of the front-end apps exploded. The old thin client/fat server model got turned on its head and we started building elaborate fat client/thin server models. A [Single Page Application (SPA)](https://en.wikipedia.org/wiki/Single-page_application) was born. Endless scrolling. Desktop-like user experience in the browser.

## Where is the problem?

Unlike desktop apps, which execute the processing logic using compiled, binary code that is not publicly available, web apps (SPAs) execute the processing logic using the scripted code that is publicly available. Being publicly available, it becomes exploitable. Security therefore gets easily compromised.

For example, let’s examine the situation where front-end developers are collaborating with back-end developers who are building APIs. Front-end dev notices: “This page needs _customer id_ and _full name_; could you please create an API end-point with the response format ```{first_name; last_name}```, given the value of _customer_id_?”

The API developers oblige and enable the client to send the query that specifies _customer id_ and returns customers _full name_. Like so:

```json
{
   customer(id: 123456789) {
        first_name,
        last_name
   }
}
```

This expressive power given to the front-end developer is also the expressive power given to the end-users who may be keen on exploring those powers. Some of those end-users could potentially be hostile users. It is difficult to imagine a computing environment that could be less secure than a web browser. Which means that expressive front-end development platforms produce a field day for malicious/hostile end-users.

This creates a huge problem: almost anything our front-end developer can do hostile users can do as well. A hostile user can easily figure out the API by inspecting HTTP Requests (in general, a very easy task not requiring advanced reverse engineering skills). Once the API has been grasped, hostile user can doctor the above query as follows:

```json
{
   customer(id: 123456789) {
        first_name,
        last_name,
        credit_card_number
   }
}
```

Ouch! Even if the end-user is not hostile (could be merely curious), the properly secured system should never allow such query to be successfully executed.

But what if it becomes a legitimate query? What if the business policy rule changes and is now allowing for the query to return the credit card number? How does the system prevent users from prying into other users’ credit card numbers?

The only way to assure proper security is to implement client-side processing logic that is sensitive to the field-level security. The system processing the query must know who is sending the query and what exactly is being asked. May sound simple at first but knowing how typically even a regular business rule may involve a lot of data elements/fields, things quickly mushroom and become exceedingly complicated. Before we know it, we have produced breeding ground for bugs.

## Increasing client-side expressiveness is risky

The more power is given to the client-side UI developers, the more security headaches get produced to worry about. New developments in the client-side technology ([GraphQL](https://graphql.org/), [gRPC](https://grpc.io/), etc.) offer amazing expressive powers to front-end developers. But with that power comes huger risk as well as huge responsibility. The power tools modern front-end developers have at their disposal are a veritable double-edged sword. That sword cuts both ways – enables developers to build amazing client-side apps while those power tools at the same time open a can of security worms.

One way to gain insight into the dangers of having such power tools running inside the browser is to compare it to the situation where users could send SQL queries direct to the back-end database from the browser. We have extremely valid reason to make such technology illegal on the browser, so how come we don’t have the same or similar concerns with **GraphQL**, **gRPC**, and other similar power tools?

## Enter DevSecOps

The DevOps revolution happened over 10 years ago and nowadays we are seeing regular DevOps teams rapidly evolving to the new levels of maturity -- DevSecOps and CloudOps. This higher level of maturity demands upgrading our engineering skills. One of the absolutely critical skill upgrades must happen in the area of security. The reason for that was, I hope, clearly presented in this article.

It is therefore paramount that front-end development efforts be closely aligned with the DevSecOps practices. Otherwise organizations are running huge risks of getting compromised by unethical hacking.
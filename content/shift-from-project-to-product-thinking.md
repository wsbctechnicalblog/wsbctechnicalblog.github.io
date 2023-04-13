Title: Shift from project to product thinking
Date: 2023-04-14
Category: Posts 
Tags: agile, learning
Slug: shift-from-project-to-product-thinking
Author: Andre Kaminski
Summary: The problem is not with projects but with project-focused thinking

## The shift from Project to Product thinking – why is it important

You probably have heard of the ‘project to a product mind shift’ that became a new buzzword over the last few years. But do you really need it, and why?

To address this, let me start with the name ‘DevOps.’ It consists of two words – Development and Operations.

The first one – Development – is pretty straightforward. This is what we do when working on projects. But the second one is a bit more complicated. The Operations part starts already when the first MVP (Minimum Viable Product) is released, while the team continues working on the following MVP. However, when the project ends (all MVPs were delivered), the operations will continue.

When I was starting my career (and this was a couple of decades ago), my mentor told me that every 6 to 8 years, software applications should be redeveloped. There was a good reason for that. It took about a year to develop and launch a product. Then the product went into sustainment and operations mode. Usually, this was done by a different team. This, in turn, when a production issue was identified’ led to complaints that the first team delivered a poor-quality application, and this team now needed to ‘save the world’ and fix the issues. At the same time, the sustainment team had to add new features requested mostly by sales and marketing teams. Often these features were done for a small market segment and sometimes didn’t make sense in the larger product picture. But sales deals and money talk. After three years, it was a ‘spaghetti’ code with a set of switches for various customers, and every new version had to be recompiled with a ‘#PRAGMA’ statement (remember that this was many years ago 😊). Around year 4, the team already spent more time fixing issues than adding more business features. Why was that? Because, at the time, we thought about a product as static. This is similar to buying a Toyota Corolla model, and besides normal maintenance, you try to add some additional fancy gauges and modify the engine. The result couldn’t be good, and most of the time, it wasn’t. So, after several years, you had to buy a new car with those fancy features.

> ![Car](../images/shift-from-project-to-product-thinking-1.png)

---

## So what’s wrong with projects? 

Actually, nothing. The problem is not with projects but with project-focused thinking.

Projects are usually temporary, ranging from a few months to a few years. They have clearly defined start and end. We often assemble an ad-hoc delivery team. Each time this new team needs to go through all phases of team development (forming, storming, norming, and performing in Tuckman’s model). As soon as the project is finished, the team disperses. And so does the accommodated product knowledge.

The projects are also linear in nature. Even in the agile world, the sequence of events is repetitive.

They represent user experience when the project is initiated, and that vision becomes static.

The projects are also part of the bigger product picture but are more isolated. The project team rarely considers how the product will grow in the future.

The project is finished when the product is created. The projects are managed by how closely they adhere to the plan. Success is measured by triple constraints – time, money and scope, and usually, all three are fixed.

---

## So why product thinking?

For one, the **products are continuous**. The vision will change depending on market conditions and customer needs, and the product’s new features will be delivered by MVPs. This means that products have a way longer time span than the projects. And if built correctly, the application’s life span can be decades rather than years (when using, for example, microservices). This timeline is from the cradle to the grave, from MVP 1 to product decommissioning.

We also need to consider the entire system, including the non-functional requirements like maintainability or stability, infrastructure, continuous monitoring, and the ability to add new or remove old features. And these are driven by market conditions or unpredictable customer needs.

System thinking also encourages continuous innovation. In 2004, Greg Linden, a developer at Amazon, suggested to his boss to implement a feature – called “Customers Who Bought This Item Also Bought.”  His boss didn’t think that this was a good idea. Greg, however, took a risk and implemented the functionality anyway. This move led to a significant increase in sales. Amazon doesn’t publish results by how much, but we can guess that it was a major contributor to company revenues that jumped from $5.3 B in 2003 to $6.9 B a year later.

The **product teams are long-standing teams**. They are the same team that started building the application, and they continue to add new functionality while supporting it. Since the team is already well established, they are usually at the ‘performing’ stage of the team lifecycle, making them more efficient at delivering new features. The deep expertise that they developed over time allows them to address problems and issues relatively quickly.

The success metrics of product teams are – the frequency of business value delivery and its impact on the customers.

But there are more benefits when shifting to product thinking. It allows the teams to build less and validate more often, correcting the course if needed. They are effective in quick adjustments to align with market trends and ever-changing customer needs. It allows the business and product managers to make measurable investments while working together with the DevOps teams. Focus in such team shifts from the amount of work done to the impact. Lastly, in many organizations, IT is perceived as a cost center. With the shift to product thinking, IT becomes a value center.

I like this quote from Anthony Crain, CPrime, that summarizes it all:

>	When a company moves from projects to products, they are changing the focus of every person in the organization from a short-term "let's get this project done and move on to the next" perspective to a long-term ownership perspective


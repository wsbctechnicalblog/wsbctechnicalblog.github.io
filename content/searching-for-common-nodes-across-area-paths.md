Title: Searching for common nodes across area paths
Date: 2020-10-21 13:13
Category: Posts
Tags: AzDO, Azure Boards, Tip
Slug: area-paths-and-nodes
Author: Willy-Peter Schaub
Summary: Common question to find area path text in work items answered.

Let us assume that you have a common node, for example architecture runway, in a number of Azure DevOps area paths. 

A common question in such a setup is "what are all the architecture runway work items?". 

**Simple**, create a query that searches for all the known area paths:

![Area Paths](/images/searching-for-common-nodes-across-area-paths-1.png)

Simple? It is not a query that can scale or that anyone wants to maintain, because the only options we have for Area Paths is the equals (=) or under 
operator. Imagine you walk up to a project containing hundreds of area paths and you need to build such a query from scratch ... run!

**Stop!** There is another way, using the Node Name:

![Node Names](/images/searching-for-common-nodes-across-area-paths-2.png)

Go [here](https://docs.microsoft.com/en-us/azure/devops/boards/queries/query-by-area-iteration-path?view=azure-devops#node-name-and-keyword-based-queries) for more gems and information!


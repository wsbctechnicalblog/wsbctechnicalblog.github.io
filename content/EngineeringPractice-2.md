Title: Engineering Practice Nuggets - Naming Conventions
Date: 2023-01-18
Category: Posts 
Tags: agile, architecture, code, code-quality, design, engineering, technical-excellence, tdd, tips, learning, innovation
Slug: EngineeringPractice-2
Author: Martin M. Lacey
Summary: Naming Convention Nuggets of Knowledge and Best Practices

# What's in a Name?

How we name and categorize things conveys meaning and intent - what it *is* and possibly *how* it should be used.  All
in the aim of improving clarity of purpose and understanding its nature, and how it should be used.

When we talk about software, we are specifically addressing naming conventions and standards, patterns that
can be exploited for automation and autonomous actions.  We are not talking about naming our children or pets in unique
or playful ways; this should be avoided in our software and thought of as an anti-pattern.  

---
# Why are Naming Conventions Important?

We define conventions and standards so that the purpose and intent of the an object variable can be inferred (i.e. its *Name*), and indeed
be anticipated; that is where automation glory can be realized.  To get there, conventions must be adopted and applied organization-wide - 
across all products, projects, and development teams.  It is more important to define a convention and *stick with it*, than it is
to pick the *best* one - it may come down to style preferences and patterns that everyone agrees on.

Naming conventions can apply to all *things* in your software; for folders, files, variables, classes, methods, and even project files and solutions.
Deciding on and following your convention is a cornerstone to creating great software.  When you adopt and follow an 
organization-wide standard *Nameing Convention* you will experience the following benifits:

* Smooth Operation - When your data is easy to find, it is easy to extract the required knowledge and make decisions based on it. There won’t be any delay in getting information, and this ensures smooth administration in your organization without any bottlenecks.
* Better Version Control - Information gets constantly updated in an organizational setting. To make sure you are using the most recent version, you need to tag it accordingly in your file name. This helps you avoid errors associated with outdated knowledge.
* Save Time and Money - When you avoid duplication through proper naming conventions, you can save a lot of time and money. You won’t have to spend time looking for lost files and there will be no need to create new versions of already existing files.
* Automation - you can anticipate file and folder names, enabling process automation such as build pipelines and code scans

There are other pillars in creating exceptional software as well, and we'll
explore those is upcoming articles.

Lets explore these standards, and the patterns that we use *by convension* to improve our software and unlock automation.

---
# Date Convention 
Dates are so common, we run into it just about every day :).  

We need a standard way to represent a date, since it can be used in filename and 
data we generate such as processing and event logs.  Some examples could be YYMMDD or YYYYMMDD, following a descreasing scope pattern.  Additional,
you might optionally include a time component suffix as well HHMMSSmmmm.

---
# Case Convention
When we create *things* that have compound names - names that contain multple words combined into a single string - we may want to deliniate
where each word begins. There are several popular conventions to apply Capital Letters and remove or replace blanks.

* Camel Case (camelCase) - This involves capitalizing all words except the first word and removing the space in between them. For instance, 'product table id' can be written as productTableId.

* Pascal Case (PascalCase) - This involves capitalizing all words in the name, including the first, and removing the space in between them. For instance, 'product table id' can be written as ProductTableId.

* Snake Case (snake_case) - This type of naming combines words simply by replacing the space with an underscore (_). The same example used above can be written as product_table_id.

* Kebab Case (kebab-case) - This is similar to the snake case except the underscore is replaced with a dash (-). For the file name used above, the Kebab case name can be written as product-table-id.

---
# Special Characters
It is probably best if you also include in your Naming Convention rules for what characters are valid to be used.  Some characters
have special meaning in some circumstances and should be avoided - such as the ampersand (@), dashes, backward and forward slashes.
When you use those special characters - any one can have implied meaning and create unexpected behaviours, so it is best to avoid them all together.
If you adopt the rule of only using Alpha-numerics, you will be well prepared for such situations.

---

# Standard Terms
You should also being a library of standard terms, with their encoded (Naming Convention applied) definition and usage.  When defining
a name for an object - consult the library of standar terms first to see if words you want to use have been standardized on.  If it is
there, use it; if it is not, add it.

*Remeber* this is organization wide set of terms used for all sofware endevours - be careful when selecting terms that mean the same
across all development teams.


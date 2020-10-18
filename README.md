# WorkSafeBC Technical Blog

## What is WorkSafeBC Technical Blog?

A publishing platform focused on showcasing cutting edge accomplishments of WorkSafeBC Software Engineering Teams.

## Can I contribute to WorkSafeBC Technical Blog?

WorkSafeBC Technical Blog is an open source platform that is open for collaboration. To propose an article to be published on WorkSafeBC Technical Blog, you need to be an engineer who works at WorkSafeBC.

## How can I contribute to WorkSafeBC Technical Blog?

To begin, you need Git installed on your computer. 

You can then clone WorkSafeBC Technical Blog by running the following command:

`git clone https://github.com/wsbctechnicalblog/wsbctechnicalblog.github.io.git`

Change directory to where you cloned the repo and create a new branch:

`git checkout -b my-branch`

Make changes to it (i.e. create a new blog post), add changed files, and commit to your local repo. Then push changes to the remote repo, and open a Pull Request.

## How do I write a blog post for WorkSafeBC Technical Blog?

It is mandatory that a blog post starts with _meta information_ (i.e. **Title**, **Date**, **Catgory**, **Tags**, **Slug**, **Author** and **Summary**):

- **Title:** My super title
- **Date:** 2020-10-03 10:20 
- **Category:** Software, TDD, etc.
- **Tags:** software-engineering, dot-net, etc.
- **Slug:** my-super-post
- **Author:** Your Name 
- **Summary:** Short version for index and feeds

For the post body, use markdown (you can also mix markdown with HTML).
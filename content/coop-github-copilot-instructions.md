Title: Coding Standards Made Simple: Harness GitHub Copilot
Date: 2025-12-08
Category: Posts 
Tags: ai, coop, engineering
Slug: coop-github-copilot-instructions
Author: Nicholas Januar
Summary: The Challenges with Copilot Out of the Box

AI tools like GitHub Copilot and ChatGPT appear very smart at generating code, but they don’t know your team’s coding standards out of the box. Think of Copilot as a smart coworker, it’s powerful but it doesn’t know your team’s rules until you teach them.

> ![Android receiving instructions](../images/coop-github-copilot-instructions-1.png)

Most teams have unique coding standards, for example, naming conventions, documentation structure and format, folder structure, architectural patterns, etc. Copilot, by default, does not know these preferences; it generates code based on general patterns they’ve learned from their data sources. This can lead to inconsistencies when your team has a preferred or standard code conventions.

For example:

- Angular Component Generation: Many teams use CLI commands for consistency in folder structure and configurations. Copilot might not use CLI and generate the components manually, leading to inconsistencies.
-	NgRx State Management: Teams often scaffold the NgRx boilerplate code using CLI. Copilot might write inline state logic or manually create the store files, leading to inconsistencies in structure or code standards.

# So how do we solve this? 

You could teach Copilot your standards on every prompt, but that isn’t practical. Instead, define your standards inside Custom Instruction Files.

GitHub Copilot has a feature called Custom Instructions, which lets you “give Copilot additional context on how to understand your project and how to build, test and validate its changes." (Adding repository custom instructions for GitHub Copilot - GitHub Docs). In other words, these instruction files are where you can define your team’s coding conventions, architectural patterns, and project details that Copilot should know.


# So how do Custom Instructions work? 

The first step is to create a `.github` folder at the root of your project.

Then, there are two ways to apply custom instructions:

1. `.github/copilot-instructions.md` – This file will be automatically applied to all files in your project
2. `.github/instructions/*.instructions.md` – This file will be applied to specific files using the applyTo glob pattern in frontmatter (e.g., `applyTo: "**/*"` for all files, or `applyTo: "**/*.tsx"` or `applyTo: "**/*.yaml"` for specific file types)

To address the two challenges we stated above, in the instruction files we direct copilot to run the CLI command instead of manual generation. Below is the actual instruction we’ve put in the file:

```
**Generate Angular component with NgRx store**: When creating a component that needs state management, you MUST run ALL THREE commands in sequence (replace `my-counter` with the actual component name):

 - **Step 1**: `npx ng g c my-counter` (creates the component)
 - **Step 2**: `npx ng g m my-counter/store/my-counter-store --flat` (creates the store module)
 - **Step 3**: `npx ng g @ngrx/schematics:feature my-counter/store/my-counter -m my-counter-store --interactive false` (creates the store feature)
```

# Our Setup Example

When we set up the instruction files, we focused on three main goals:

-	Easy to read
-	Easy to maintain
-	Scalable for future improvements

Here’s the structure we used for Angular projects:

```
.github/
├── copilot-instructions.md          # Main entry point & overview
└── instructions/
    ├── UI-general.instructions.md   # Core Angular & UI patterns
    ├── UI-button.instructions.md    # Button styling standards
    ├── UI-checkbox.instructions.md  # Checkbox component patterns
    ├── UI-text-input.instructions.md # Text input standards
    ├── UI-table.instructions.md     # Table component patterns
    ├── UI-modal-window.instructions.md # Modal dialog patterns
    ├── UI-pagination.instructions.md # Pagination component
    ├── UI-ngrx.instructions.md      # NgRx store patterns
    ├── UI-ngrx-form.instructions.md # NgRx forms integration
    ├── UI-ngrx-ajax.instructions.md # Ajax/API call patterns
    └── UI-ngrx-modal-window.instructions.md # Modal + NgRx
```

Each instruction file focuses on a specific area, such as general UI patterns, button styles, or NgRx store patterns.

We found that breaking up instructions into smaller files makes them easier to read, maintain, and get updated.

# Summary

To summarize, GitHub Copilot is powerful, but without guidance, it will generate code based on general best practices. Use Custom Instruction files to teach Copilot about your team’s coding standards.

# Additional Resources

- [Adding repository custom instructions for GitHub Copilot - GitHub Docs](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions?tool=vscode)
- [Introducing the Awesome GitHub Copilot Customizations repo - Microsoft for Developers](https://developer.microsoft.com/blog/introducing-awesome-github-copilot-customizations-repo)

Real example on how developers behind Visual Studio Code set up their instruction files: [vscode/.github at main · microsoft/vscode](https://github.com/microsoft/vscode/tree/main/.github)


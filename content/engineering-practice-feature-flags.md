Title: Engineering Practice Feature Flags
Date: 2025-02-21
Category: Posts 
Tags: code, code-quality, engineering, technical-excellence
Slug: engineering-practice-feature-flags
Author: Martin M. Lacey
Summary: Feature Flags Part 1 - How To Keep Trunk-Based Branching Reliable

# What are Feature Flags?


> ![software bug-bear - feature flag misunderstandings](/images/engineering-practice-feature-flags-3.jpg)

Well, we've discussed this in several historical issues of our technical blog, but it continues to be a bug-bear! It is therefore important to revisit and see where we are with our thinking. See the reference section at the end of this blog for our prior thoughts on this subject; the balance of this blog is a further evolution and analysis, with options on how to address implementation details.  In a subsequent post, I will get into concreate examples demonstrating patterns discussed here. 

Feature flags are a powerful technique in software engineering for managing the exposure of partially implemented or experimental functionality while maintaining a stable production environment. 
As we have discussed in prior blogs, we recommend trunk-based branch management - see [Mastering Software Development: A Deep Dive into Trunk-Based Pull Request Workflow](https://wsbctechnicalblog.github.io/engineering-practices-pull-request-v2.html) / Dec 2023
.  As a refresher, here is the repository management pattern we suggest and follow:
> ![Visualizing the branching strategy](/images/engineering-practice-feature-flags-1.png)

 ![Caution](/images/engineering-practice-feature-flags-2.png) The trunk, typically master branch, is not only our source of truth, but must also be deployable to production via a release branch at any time. Features merged to master that are not ready for release, must be tagged, hidden by feature flags, and deployable to any environment. This is crucial when multiple teams share an application and its repository.
Below, I outline best practices for using feature flags effectively, managing older code that lacks SOLID principles, ensuring good design in new applications, and structuring story slicing to avoid long-lived feature branches.

---

# 1. Best Practices for Using Feature Flags

Feature flags (also called feature toggles) enable dynamic control over feature availability in different environments without deploying new code. Effective use of feature flags helps teams continuously integrate changes while mitigating risks.

## Types of Feature Flags
- **Release Toggles** - Temporarily control unfinished features, allowing incremental development.
- **Experiment Toggles** - Enable A/B testing to compare feature performance and behavior with a subset of users.
- **Ops Toggles** - Used for operational controls, such as enabling circuit breakers or graceful degradation, such as logging levels or feature activation.
- **Permission Toggles** - Control access to features based on user roles or permissions.
- **Kill Switches** - Disable features in production to prevent issues or security vulnerabilities.
- **Configuration Toggles** - Modify feature behavior without code changes, such as changing thresholds or timeouts.
- **Time-Based Toggles** - Enable features based on time, such as seasonal promotions or holiday themes.

## Best Practices
- **Default to Off** - Features should be disabled by default to prevent accidental exposure of unfinished or experimental features.
- **Keep Flags Short-Lived** - Remove flags once features are stable and released to avoid technical debt.
- **Use a Flag Management System** - Centralize flag management to improve visibility and governance, ensure consistency and avoid conflicts.
- **Monitor and Audit** - Track flag usage and performance to identify issues and optimize feature delivery.
- **Enable Gradual Rollouts** - Use percentage-based rollouts to limit the impact of issues and gather feedback from a subset of users.
- **Ensure Flags are Configurable at Runtime** - Allow flags to be toggled without code changes or restarting services to respond quickly to issues or changes.
- **Automate Testing** - Include flag testing in automated test suites to ensure consistent behavior across environments.

---

# 2. Managing Older Code Without SOLID Design

Older codebases often lack SOLID principles (Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion). This makes integrating feature flags and refactoring difficult.

## Challenges

- **Monolithic Architecture** - Large, tightly coupled codebases make it challenging to isolate and test features.
- **Spaghetti Code** - Complex, interdependent code with unclear responsibilities and dependencies.
- **Lack of Dependency Injection** - Hard-coded dependencies and global state make it difficult to introduce new functionality and toggle features dynamically. 
- **Lack of Tests** - Inadequate test coverage makes it difficult to validate changes and ensure backward compatibility.
- **Legacy Dependencies** - Outdated libraries, frameworks, or third-party services that limit modernization efforts.

## Strategies for Managing Older Code
- **Introduce Facades & Wrappers** - Create an abstraction layer around legacy code to introduce feature toggles without deep modifications.
- **Apply the Strangler Pattern** - Incrementally refactor and replace legacy components with modern, feature-flag-enabled code. 
- **Use Adapter Patterns** - Introduce adapters to bridge between legacy and modern code, enabling feature flag integration.
- **Refactor Opportunistically** - Break down monolithic components into smaller, testable units to introduce SOLID principles and feature flags.  Whenever modifying old code for a new feature, apply SOLID principles gradually. 
- **Use Inversion of Control (IoC) for Flags** - Inject feature toggles through configuration rather than scattering conditionals across the codebase; introduce dependency injection and IoC containers to manage feature flags and dependencies dynamically.
---

# 3. Importance of Good Design in New Applications
 
A well-architected system makes feature flags easier to implement and reduces long-term complexity.

## Key Design Considerations
- **Modular Architecture** - Use microservices, plugins, or clean architecture to isolate features.
- **Separation of Concerns** - Divide functionality into distinct layers (presentation, business logic, data access) to improve maintainability and testability.
- **Dependency Injection (DI)** - Use IoC containers to manage dependencies and enable feature toggles without code rewrites.
- **Test-Driven Development (TDD)** - Write tests before implementing features to ensure code quality and enable continuous integration.
- **Event-Driven Design** - Use events and messaging to decouple components and enable asynchronous processing, allowing features to be toggled dynamically without affecting core workflows.
- **Clear API Boundaries** - Define clear interfaces and contracts between components to enable feature flagging at the API level; avoid tightly coupled dependencies that complicate feature flag implementations.
- **Well-Defined Domain Model** - Use domain-driven design to model business logic and entities, enabling feature flags to be applied at the domain level and reducing cross-cutting concerns; helps in slicing stories (discussed below) for smaller, incremental changes.

---

# 4. Effective Story Slicing to Avoid Long-Lived Feature Branches

One of the biggest risks in feature flagging is accumulating long-lived feature branches, leading to merge conflicts and integration issues.

## Why Avoid Long-Lived Feature Branches?
- **Integration Hell** - Merging long-lived branches can be complex and error-prone, leading to conflicts and regressions.  The longer a branch exists, the harder it is to merge.
- **Delayed Feedback** - Long-lived branches delay feedback from stakeholders and users, increasing the risk of misalignment, hidden defects, and wasted effort.
- **Reduced Velocity** - Long-lived branches slow down development velocity, making it harder to deliver value quickly and respond to changing requirements.
- **Reduced Collaboration** - Long-lived branches isolate developers and teams, reducing collaboration and knowledge sharing, which can unknowingly introduce conflicts.
- **Increased Technical Debt** - Long-lived branches accumulate technical debt, making it harder to maintain and evolve the codebase.
- **Risk of Abandonment** - Long-lived branches increase the risk of features being abandoned or postponed indefinitely due to integration challenges.
- **Complex Dependencies** - Long-lived branches introduce complex dependencies and make it harder to isolate and test features independently.
- **Inconsistent Code Quality** - Long-lived branches can lead to inconsistent code quality and practices, making it harder to maintain and scale the codebase.
- **Increased Rework** - Long-lived branches increase the likelihood of rework and refactoring, as requirements change and conflicts arise.


## Best Practices for Story Slicing
- **Slice Stories Vertically** - Break down features into small, vertical slices that deliver end-to-end functionality, enabling incremental development and feedback.
- **Use Feature Flags** - Use feature flags as early as possible to hide incomplete functionality and enable continuous integration and deployment.
- **Deliver Value in Small Increments** - Instead of developing an entire feature in one go, break it into deployable slices.
- **Use UI Stubs & Mocks** - If backend functionality isn't ready, implement UI components with placeholders.
- **Adopt Trunk-Based Development** - Encourage frequent integration to main branches, reducing the reliance on long-lived feature branches.
---

# Conclusion 

Feature flags are essential for modern software engineering but require disciplined management. When dealing with legacy code, introduce feature flags with minimal refactoring - progressively improving the design. New applications should follow SOLID principles and a modular architecture to facilitate easy feature toggling. 
Finally, effective story slicing ensures that teams can continuously integrate work, avoiding long-lived branches and maintaining high development velocity.

# References
- [Mastering Software Development: A Deep Dive into Trunk-Based Pull Request Workflow](https://wsbctechnicalblog.github.io/engineering-practices-pull-request-v2.html) / Dec 2023
- [Mastering Software Development: A Deep Dive into Feature Flags](https://wsbctechnicalblog.github.io/engineering-practices-feature-flags.html) / Dec 2023
- [Feature Toggles (aka Feature Flags)](https://martinfowler.com/articles/feature-toggles.html) by Martin Fowler
- [Feature Flags Best Practices](https://www.optimizely.com/feature-management/feature-flags/) by Optimizely
---

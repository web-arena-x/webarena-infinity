# How to use Linear: Small teams

Linear is best paired with our philosophy on how teams should work, [The Linear Method](https://linear.app/method). We are building Linear to support the core elements of the software development lifecycle: Planning and Building exceptional products.

**This guide**

* **Is tailored for:** admins and owners at smaller companies, like startups at the earliest stages and smaller agencies
* **And covers:** how to set up your Linear workspace, and make the most of Linear's features

---

## Setting up your workspace

### **Plan recommendation**

Our Basic Plan provides 5 teams, unlimited uploads, unlimited Issues and admin roles.

You should consider the Business Plan if:

* You’re running an external Slack community, or customer facing Slack channels, and want to convert Slack messages into Linear Issues (see [Asks](https://linear.app/features/asks)).
* You already have a large volume of tickets coming in via support tools (Intercom, Zendesk, Front) and want to connect them to the product development workflow ([Support integrations](https://linear.app/integrations#customer-experience))
* You need to invite external guests to work on Projects, like contractors or freelancers ([Guest accounts](https://linear.app/changelog/2022-07-14-guest-accounts)), or [Sub-teams](https://linear.app/docs/sub-teams) for an additional layer of organization.

### Key integrations to setup

* [GitHub](https://linear.app/integrations/github) & [GitLab](https://linear.app/integrations/gitlab): to automate status updates and review PRs in Linear
* [Slack](https://linear.app/docs/slack): create issues from Slack and share project updates

↳ [See all integrations](https://linear.app/integrations)

### **Organizing Teams**

Mimic your org chart and establish teams by function — such as Engineering, Design, and Marketing — and use [Sub-teams](https://linear.app/docs/sub-teams) to reflect specialized teams under those, like backend or frontend development, or a team working on a specific feature.

![Sub-teams](https://webassets.linear.app/images/ornj730p/production/533d9155ce1ddbfc57cd0bc273537c5445675781-1148x467.png?q=95&auto=format&dpr=2)

Invite your team to the workspace via a unique link, email, or bulk CSV upload.

↳ Doc: [Learn more about Teams](https://linear.app/docs/teams)

> [!NOTE]
> **Top tip**: [Share this with your team once added to help them spin up on Linear](https://linear.app/docs/joining-your-team-on-linear)

### **Configure workflows**

While Linear’s default settings are designed to help you focus and move fast, we understand that you'll want to adapt core features to your way of working.

* [Statuses](https://linear.app/docs/configuring-workflows) that your Issues will move through as work progresses
* Configure sprint-like structure with [Cycles](https://linear.app/docs/use-cycles)
* Manage how your team handles incoming requests, like customer feedback and bugs, with [Triage](https://linear.app/docs/triage)
* Create custom templates for [Issues](https://linear.app/docs/issue-templates), [Projects](https://linear.app/docs/project-templates), and [Documents](https://linear.app/docs/project-documents#create-document-templates) to move faster with repeating tasks
* Assign custom [labels](https://linear.app/docs/labels) to categorize Issues, like bugs
* Set [Estimates](https://linear.app/docs/estimates) to describe the complexity or size of an Issue
* [Project statuses](https://linear.app/docs/project-status), to report on progress with larger pieces of work, and how you use [updates](https://linear.app/docs/initiative-and-project-updates) to keep the broader team informed
* Configure [status updates](https://linear.app/docs/github#issue-status-updates) to linked issues when updates are made to PRs

### **Set up Issue Triage**

We built [Triage](https://linear.app/docs/triage) to help teams manage unexpected work – urgent bugs, idea from across the organization, customer feature requests, and scope creep.

Enabling Triage will configure a separate inbox for reviewing issues created by users who aren’t part of a certain team in Linear, or by external integrations (like GitHub, Slack, and Intercom), before accepting them to that team's backlog.

**Triage helps you:**

* **Manage feature requests:** by connecting with Slack and your customer support tool (Zendesk, Intercom, Front) to turn product feedback into issues within Linear
* **Track bugs:** by enabling anyone in your organization (including non-Linear users) to log bugs directly in Linear through Slack and email

**Level-up features available on other plans**:

* [Triage responsibility](https://linear.app/docs/triage#triage-responsibility) [Business or Enterprise] enables you to link your on-call scheduled to automatically assign a triage owner
* [SLAs](https://linear.app/docs/sla) [Business or Enterprise] — service level agreements — to set guidance for when time-sensitive issues should be completed

---

## Migrating to Linear

Once you’ve got your teams set up in Linear, it’s time to start bringing over work from your other tools. Whether you’ve chosen to adopt Linear as your primary issue tracking and project management tool, or you’re integrating it alongside existing tools, data imports and synchronization are essential.

**Importing**

* Use the [Importer](https://linear.app/docs/import-issues) to pull in-flight issues into Linear and map them to appropriate teams. Linear offers native importers for GitHub Issues, Jira, Asana, Shortcut, and Trello.
* Alternatively, you can import a CSV with issue data

**Syncing**

* Sync issues with [Jira](https://linear.app/docs/jira) and [GitHub](https://linear.app/docs/github#github-issues-sync) while trialing or transitioning to Linear to keep projects up to date across tools

> [!NOTE]
> Follow our detailed [migration guide](https://linear.app/switch) for step-by-step instructions.

---

## Building & Planning

Most startups plan in short phases, focusing on what can be shipped in the coming weeks. Features are prioritized based on customer feedback and market opportunity, and delivered iteratively.

The tools you use should promote a bias for action and help you move with urgency.

### **Start with Issues**

For small teams, we recommend starting by creating Issues immediately, rather than over planning work with Projects and Initiatives. You can use those features later.

Issues are the atomic unit in Linear. They represent a specific piece of work, such as a task or bug, that has a clear output and might take anywhere from a few minutes to an hour or a day.

We've designed them to be zero-friction. Issues take seconds to create, which counterintuitively means your team will log additional bug reports and share ideas more frequently while spending _less_ time in the tool.

Each issue has [configurable properties](https://linear.app/docs/issue-properties):

* Categorized using labels
* Linked by relationships, such as _blocking_, _related_, or _duplicate_
* Assigned a due date and priority score
* Estimated in magnitude

You can create [recurring issues](https://linear.app/docs/creating-issues#create-recurring-issues) to automate your repeated tasks on a cadence of your choosing.

> [!NOTE]
> **Top tip**: You can create [sub-issues ](https://linear.app/docs/parent-and-sub-issues)when a set of work is too large to be a single issue but too small to be a project. Sub-issues also ideal for splitting up work shared across teammates. When you add a sub-issue to another issue, the other issue becomes its "parent."

↳ Doc: [Learn more about Issues](https://linear.app/docs/creating-issues)

### Here's an example workflow using issues:

* Begin by creating all potential and known work as Issues, even larger pieces of work that feel like Projects
* Use [Estimates](https://linear.app/docs/estimates), such as XL labels or custom sizing, to flag issues that might evolve into Projects
* Add known scope items as sub-issues
* Create a single [View](https://linear.app/docs/custom-views) that shows all Issues within the Team. You can filter out sub-issues, and only show parent issues in your view's display setting

This gives you a consolidated view of all the work happening across your startup.

### **Using Projects for planning**

When work kicks off, and you start to better understand the magnitude of it, you can easily convert an Issue into a Project by pressing cmd + K, and typing “convert to Project”.

Projects are designed for larger pieces of work that span multiple weeks or months. Projects are **optional** for small teams – they become useful when you start to plan in quarterly cycles, have multiple teams that need to collaborate, or when Issues start to snowball into larger tasks.

Examples of Projects:

* ENG / New Feature Launch
* ENG / Mobile App MVP
* Marketing / Customer Story Launch

### Managing a Project

Each Project should have a lead, responsible for maintaining momentum, ensuring accountability, and preventing work from falling through the cracks. Project Leads don’t have to be team leads — they can be anyone best suited for the project, whether they have direct ownership or are closest to the work.

* Use the [Project Overview](https://linear.app/docs/project-overview) to define your scope and align on the key objectives
* [Project Documents](https://linear.app/docs/project-documents) provide you with a space to go deeper and capture additional details
* Set [Project milestones](https://linear.app/docs/project-milestones) for longer projects with distinct stages (Alpha, Beta, GA)
* Keep everyone up to speed with [Project Updates](https://linear.app/docs/project-updates)
* Build [custom views](https://linear.app/docs/custom-views) to have clear visibility into Project work and progress

> [!NOTE]
> **Top tip:** Even if you're not at the stage where you're planning in advance, you can use Projects as a container for your thoughts, open questions, documents, and early designs relating to an aspect of your product or company.

---

## Understanding progress

### Updates

Projects include an [Updates](https://linear.app/docs/project-updates) feature. Leads will receive reminders from Linear to provide updates at regular intervals. These updates, along with progress tracking (On track, At risk, Off track), can be configured to post in Slack with bi-directional comment syncing — enabling you to keep the broader group informed.

![Project updates](https://webassets.linear.app/images/ornj730p/production/e29e93134992c6ab6ef12509ad49c95b20cea06c-3312x1732.tif?q=95&auto=format&dpr=2)

As Projects progress, they move through [statuses](https://linear.app/docs/project-status) that you can configure at the workspace level.

![Project statuses](https://webassets.linear.app/images/ornj730p/production/42b6cd5957a5374626fbbd7106bf0833e28280f6-3312x1820.tif?q=95&auto=format&dpr=2)

Built-in [Project Graphs](https://linear.app/docs/project-graph) help you understand the progress your team is making towards completion, and offers estimates for when you'll finish.

![Project graphs](https://webassets.linear.app/images/ornj730p/production/1583151e675c8ebcd8b2fd926362a15f4f407ea7-2880x1928.tif?q=95&auto=format&dpr=2)

### Go deeper with custom views

[Custom views](https://linear.app/docs/custom-views) enable you to create filtered views of issues or projects that you can save and share with others in your workspace. They can be private, available to everyone, or visible per team. They are particularly useful to see issues across multiple teams, projects, or a single label, like `label:bug`.

Views at the project level enable you to visualize progress in timelines, by progress, or status (n Track, At Risk, Off Track).

![Project timeline](https://webassets.linear.app/images/ornj730p/production/6a5478c3bc2de4eae7b848954548c9ddb2b0f53c-4460x2868.png?q=95&auto=format&dpr=2)

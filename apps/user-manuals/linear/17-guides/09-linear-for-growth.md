# How to use Linear for Growth

Linear is best paired with our philosophy on how teams should work, [The Linear Method](https://linear.app/method). We are building the Linear to support the core elements of the software development lifecycle: Planning and Building exceptional products.

![Header image](https://webassets.linear.app/images/ornj730p/production/69a3f5213c42e4aecc07639ed6e58c5a762202f0-2160x1326.png?q=95&auto=format&dpr=2)

Designed for larger companies, this guide walks your though how to set up your Linear workspace, and make the most of Linear's features.

---

## Setting up your workspace

### Migrate your data into Linear

Whether you’ve chosen to adopt Linear as your primary issue tracking and project management tool, or you’re integrating it alongside existing tools, ensuring smooth transfer of data and maintaining synchronization is essential.

The first step is to create your workspace to prepare for the data migration.

Use one of our native [import tools](https://linear.app/docs/import-issues) to pull in-flight issues into Linear and map them to appropriate teams. Linear offers native importers for GitHub Issues, Jira, Asana, and Shortcut. Alternatively, you can import a CSV with issue data using our [CLI Importer](https://linear.app/docs/import-issues#other).

> [!NOTE]
> During your import from [Jira](https://linear.app/docs/jira) or [GitHub](https://linear.app/docs/github#github-issues-sync), you have the option to syncing while trialing or transitioning to Linear to keep projects up to date across tools.

Follow our detailed [migration guide](https://linear.app/switch/migration-guide) for step-by-step instructions.

### Set up integrations

* [GitHub](https://linear.app/docs/github) or [GitLab](https://linear.app/integrations/gitlab): automate status updates and review PRs in Linear.
* [Slack](https://linear.app/docs/slack): allows your Linear team to create issues from Slack and share project updates.
* [Linear Asks](https://linear.app/features/asks): enable your non-Linear members to create Issues in Linear from Slack—from workplace requests, to bug reports, feature ideas and IT tickets.
* [Figma](https://linear.app/integrations/figma): link issues directly from Figma, and embed your designs
* [Zendesk](https://linear.app/docs/zendesk), [Intercom](https://linear.app/docs/intercom), or [Front](https://linear.app/docs/front): create issues from support tickets

> [!NOTE]
> Top tip: [Here's how we use integrations at Linear in our Customer Experience Team](https://linear.app/blog/how-we-think-about-customer-experience-at-linear)

↳ [See all integrations](https://linear.app/integrations)

### **Set up Teams**

The most common Team set up for larger organizations is to mimic your org chart. Top-level Teams are typically established by function—such as Engineering, Design, and Marketing—and [Sub-teams](https://linear.app/docs/sub-teams) are used to reflect specialized teams under those, like backend or frontend development, or a team working on a specific feature.

Admins can pre-load your Team structure in Settings, and invite members to the workspace via a unique link, email, or bulk CSV upload.

> [!NOTE]
> Top tip: [Share this with your team once added to help them spin up on Linear](https://linear.app/docs/joining-your-team-on-linear)

↳ Doc: [Learn more about Teams](https://linear.app/docs/teams)

### **Configure team workflows**

While standardized workflows in Linear enhance scalability and consistency across your organization, we understand that each team needs a certain level of autonomy to succeed.

* [Statuses](https://linear.app/docs/configuring-workflows) that your Issues will move through
* Templates for [Issues](https://linear.app/docs/issue-templates), [Projects](https://linear.app/docs/project-templates), and [Documents](https://linear.app/docs/project-documents#create-document-templates) to standardize processes
* Custom [labels](https://linear.app/docs/labels) to categorize specific Issues. Labels can also be created at the workspace level for common Issues, like bugs
* [Estimates](https://linear.app/docs/estimates) to describe the complexity or size of an Issue
* Schedules for sprint-like structures called [Cycles](https://linear.app/docs/use-cycles)
* Updates to your PR/MRs can [automate your Linear issue statuses](https://linear.app/docs/github#issue-status-updates)

---

## Planning

Mid-sized companies often plan in quarterly cycles based on annual strategic themes, balancing new feature development with platform upgrades across multiple product teams, each with its own roadmap.

We've built Linear to enhance coordination through automations, maintain visibility with reporting features that don't make the life of your engineers difficult, and standardize core processes for scale, whilst enabling team autonomy.

### **Using Initiatives**

Use [Initiatives](https://linear.app/docs/initiatives) to plan and manage strategic streams of work that span multiple Projects and longer timelines, such as major launches, product goals, or company-wide objectives like OKRs.

Typically set top down, leaders use initiatives to translate company strategy into visible progress. Initiatives set the overall direction, whilst managers and team members coordinate the underlying work via Projects.

Use [Initiative updates](https://linear.app/changelog/2025-02-13-initiative-updates) to report on progress and summarize work across multiple Projects. They enable leaders in your organization to quickly assess the health of major company priorities and leave feedback without getting lost in the details.

Initiative examples:

* ENG / Launch Enterprise Offering
* ENG / Mobile App v2
* GTM / Build /customers page

↳ Video: [Introducing Initiatives](https://webassets.linear.app/files/ornj730p/production/35a964cc743ad90074d1b33ff766c0adfec0622b.mp4)

### **Using Projects**

Organize and deliver meaningful work—such as launching new features or redesigning core product experiences—by using projects. Typically, projects are identified and initiated during a quarterly planning process.

Projects serve as a container for all related documents, customer discovery notes, and designs, allowing you to keep everything organized in one place.

* Use [Project documents](https://linear.app/docs/project-documents) to draft your specs and align on scope, which then lives side-by-side with the engineering work bringing it to life
* Set [Project milestones](https://linear.app/docs/project-milestones) for longer projects with distinct stages, such as a new feature launch that includes Alpha, Beta, and GA phases
* Use [Project updates](https://linear.app/docs/project-updates) to keep stakeholders informed on the latest with a project

Examples of Projects:

* ENG / New Feature Launch
* ENG / Mobile App MVP
* Marketing / Customer Story Launch

For each project, we recommend appointing a single lead responsible for drafting the specification, populating issues after scoping, inviting relevant team members, and driving the project forward.

At the workspace-level, establish organization-wide [project statuses](https://linear.app/docs/project-status) for a clear and uniformed understanding of a project's progress across the organization.

---

## Building

### **Using Issues**

Issues are the currency of work in Linear. You can use them to:

* Log bugs and track customer requests from support channels (Zendesk, Intercom), Slack channels, or by forwarding an email to Linear
* Set yourself to-dos
* Add an idea to your backlog
* Automate recurring tasks with [recurring Issues](https://linear.app/docs/creating-issues#create-recurring-issues)

Create [Labels](https://linear.app/docs/labels) at both the workspace and team level to categorize Issues, and establish relationships between Issues such as blocking, related, and duplicate using [Issue Relations](https://linear.app/docs/issue-relations).

> [!NOTE]
> Top tip: You can create [sub-issues ](https://linear.app/docs/parent-and-sub-issues)when a set of work is too large to be a single issue but too small to be a project. Sub-issues also ideal for splitting up work shared across teammates. When you add a sub-issue to another issue, the other issue becomes its "parent".

↳ Doc: [Learn more about Issues](https://linear.app/docs/creating-issues)

### Manage feature requests and bugs with Triage

[Triage](https://linear.app/docs/triage) is a dedicated inbox for managing unplanned work—urgent bugs, customer feature requests, and scope creep—before it enters your team’s main workflow. New Issues from support tickets, bug reports, or cross-team requests land here first, where they can be evaluated, prioritized, or declined without disrupting your team’s focus.

Make it sustainable by setting up [Triage responsibility](https://linear.app/docs/triage#triage-responsibility)— define who handles incoming requests, either through manual rotation or by connecting to your PagerDuty schedules.

#### Manage feature requests

* Connect Linear with Slack and your support tool (Zendesk, Intercom, or Front) to turn product feedback and feature requests into Issues within Linear
* [Customer Requests](https://linear.app/customer-requests) create unique customer identifiers in Linear, so you can track the feedback given by your most influential customers

#### Track bugs

* Anyone in your organization, including non-Linear users, can identify and log bugs directly in Linear through Slack, Linear Asks, email, or other forms of integrations (e.g. Zapier).
* Use [Issue Labels](https://linear.app/docs/labels) to track bugs, and [Views](https://linear.app/docs/custom-views) to see all of them across your company

[Use SLAs](https://linear.app/docs/sla) (Enterprise Plan only) — service level agreements — to set guidance for when time-sensitive issues should be completed.

↳ Blog: [Planning for unplanned work](https://linear.app/blog/planning-for-unplanned-work)

### Working in Cycles

If you’re accustomed to working in sprints, [Cycles](https://linear.app/docs/use-cycles) offer a similar time-boxed structure but with automation at their core. They repeat automatically, roll unfinished work forward, and help you to build a clear picture of your [team’s true capacity](https://linear.app/docs/use-cycles#cycle-capacity) without introducing planning overhead.

---

## Reporting

### Custom Views

[Custom Views](https://linear.app/docs/custom-views) are views of all Issues filtered by any dimension available in Linear. Custom Views are particularly useful to see issues across multiple teams, projects, or a single label, like `label:bug`. They can be private, available to everyone, or visible per team. Once you create a view that you want to access frequently, favorite it for later use.

### Insights

Turn your Linear data into actionable analytics to understand your team's performance.

[Insights](https://linear.app/docs/insights) come attached to every View in Linear, turning the data into visual reports that highlight trends, bottlenecks, and opportunities across your workspace.

Use them to:

* Track resource allocation across Projects
* Measure bug resolution speed and trends
* Evaluate estimation accuracy
* Retro cycle times to improve predictability
* Identify bottlenecks and blocking dependencies

↳ Video: [Reporting and Analytics ](https://docs.google.com/document/d/1R9WKiSkxc-UI-uLQnFZkba1mXKijauHdk_wayPFCfww/edit?tab=t.0)_(only if we can make a small cut of the Insights section)_

### Initiative & Project updates

Keep the team aligned with structured progress reports that include health indicators (On track, At risk, Off track) and text descriptions.

[Initiative updates](https://linear.app/docs/initiative-and-project-updates) help leaders monitor strategic streams of work across multiple projects, making it simple to track progress towards company-wide objectives.

[Project updates](https://linear.app/docs/initiative-and-project-updates) focus on execution details, where project leads can report on completed work, upcoming priorities, flag blockers and share milestone progress.

Both update types can be configured to post in Slack with bi-directional comment syncing. Set reminders to ensure consistent updates and create dedicated channels for better visibility.

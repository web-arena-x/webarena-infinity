# How to use Linear: Large & scaling companies

Linear is designed to support the core elements of the software development lifecycle: Planning and building exceptional products. For rapidly scaling companies, or those already larger in size, Linear helps you to maintain visibility into product progress and increase product building velocity amidst growing complexity.

**This guide**

* **is tailored for:** admins and leaders at larger companies, like later stage startups and enterprises, or those on Linear's Enterprise plan
* **and covers:** how to set up your Linear workspace, and make the most of Linear's features

> [!NOTE]
> Not an admin? Jump straight to [Planning & Building in Linear](https://linear.app/docs/how-to-use-linear-large-scaling-companies#planning).

## Setting up your workspace

As a workspace admin at a larger organization, establishing effective governance and structure in your Linear workspace is essential for smooth operations. This section outlines key best practices for configuring your workspace to meet enterprise requirements around security, access controls, team organization, and integration management.

### Workspace access management

#### SAML & SCIM integration

For secure, streamlined user management at enterprise scale:

* Connect your Identity Provider (Azure AD, Okta) using [SAML](https://linear.app/docs/saml-and-access-control) for Single Sign-On, enhancing security while simplifying the login experience
* Enable [SCIM](https://linear.app/docs/scim) for automated user provisioning/deprovisioning, ensuring access controls remain in sync with your HR systems
* Consider implementing group attribute statements through your Identity Provider for automatic team membership where available

#### User roles and permissions

Linear offers three permission levels to balance access with security:

* **Admins**: Full control over workspace settings, team configurations, integrations, and billing
* **Members**: Access to all public content with ability to create and modify issues, but limited from workplace settings
* **Guests**: Access restricted to only the specific teams they're invited to join; ideal for contractors or external collaborators

> [!NOTE]
> **Best Practice**: For most enterprise deployments, designate only a small group of IT/Operations personnel as workspace Admins, with the majority of employees as Members. Use Guest accounts for external collaborators who should have limited visibility.

↳ Doc: [Learn more about member roles](https://linear.app/docs/members-roles#roles)

### Team access controls

Effectively manage visibility across a large organization:

* **Public Teams**: Use for most cross-functional teams to encourage transparency and collaboration. Anyone in your workspace can join public teams, giving them full access to that team's content
* **Private Teams**: Create private teams for sensitive work that should remain confidential and can only be accessed by selected users

> [!NOTE]
> **Important**: Linear permissions work at the team level - there are no private issues or projects. If information needs to be restricted, it must be contained within a private team.

↳ Doc: [Learn more about Teams](https://linear.app/docs/teams)

> [!NOTE]
> Top tip: [Share this with your team once added to help them spin up on Linear](https://linear.app/docs/joining-your-team-on-linear)

---

## Integration management

### Key integrations to use

Install these integrations to get the most out of Linear:

* [GitHub](https://linear.app/integrations/github) & [GitLab](https://linear.app/integrations/gitlab): to automate status updates and review PRs in Linear
* [Slack](https://linear.app/docs/slack): create issues from Slack and share progress updates
* [Zendesk](https://linear.app/docs/zendesk), [Intercom](https://linear.app/docs/intercom), or [Front](https://linear.app/docs/front): create issues from support tickets
* PagerDuty or [incident.io](https://linear.app/integrations/incident-io): link on-call schedules to determine [Triage responsibility](https://linear.app/docs/triage#triage-responsibility)

↳ [See all integrations](https://linear.app/integrations)

> [!NOTE]
> Not seeing what you need? [The Linear API](https://developers.linear.app/docs) allows you to connect your existing tools and workflows with Linear, making it easy to create custom automation for your team. Built on GraphQL, the API gives you access to all Linear features, so you can create, update, and manage issues programmatically.

### Set up Issue Triage

[Triage](https://linear.app/docs/triage) is a shared inbox that captures incoming new issues such as bug reports, feature requests, and other unplanned work. Triage is enabled at the team level and acts as a first checkpoint to ensure that every issue is properly assigned and prioritized before it is added to the team’s workflow.

This centralized intake mechanism allows everyone in your organization to quickly create new issues without needing to worry about where they belong in your Linear workspace — particularly helpful for customer-facing teams such as Support or Sales who frequently report bugs or feature requests from users.

Integrations with tools such as Slack, Intercom, or Zendesk (where unplanned work typically first surfaces) can be configured to automatically route new issues directly to the most relevant triage queue.

Larger teams can enhance Triage with additional workflows:

* Configure [triage responsibility](https://linear.app/docs/triage#triage-responsibility) rotations by linking your on-call schedule to automatically assign a triage owner, who is responsible for reviewing issues that are added to the triage queue
* [Use SLAs](https://linear.app/docs/sla) — service level agreements — to set guidance for when time-sensitive issues should be completed
* Enable [Linear Asks](https://linear.app/docs/linear-asks) to streamline workplace requests from Slack

> [!NOTE]
> Looking for inspiration? [Here's a rundown of how we use Triage at Linear](https://linear.app/blog/planning-for-unplanned-work)

### Set up Linear Asks

[Asks](https://linear.app/docs/linear-asks) lets everyone in your Slack workspace turn requests such as bug reports, questions, and IT needs into actionable issues in Linear. Teams can submit requests directly from Slack and automatically send them to the relevant team in Linear. Useful for tracking bugs, logging customer feedback, or simply making a request to another team at your company — such as a request for data, or design mock ups for a marketing campaign.

↳ [Configure Linear Asks](https://linear.app/docs/linear-asks)

> [!NOTE]
> **Important:** Beyond these core integrations, your team can [request additional third-party apps](https://linear.app/docs/third-party-application-approvals). As an admin, you get to control which applications can access your Linear workspace, and set up a review process for integration requests to evaluate security and data access implications.

---

## Workspace structure

### Organizing teams

A [Team](https://linear.app/docs/teams) in Linear shares issues and projects and follows the same workflows, cycles, and triage processes. Users can be members of multiple teams for visibility, but will typically do most of their work out of 1-2 primary teams.

Teams can be structured into a hierarchy using parent and [sub-teams](https://linear.app/docs/sub-teams). Multiple sub-teams can be nested under a parent. This relationship enables you to create a hierarchy of teams within Linear, so that it's easier to understand and manage work across different levels.

![Sub-teams](https://webassets.linear.app/images/ornj730p/production/533d9155ce1ddbfc57cd0bc273537c5445675781-1148x467.png?q=95&auto=format&dpr=2)

### Configurable workflows

While standardized workflows in Linear enhance scalability and consistency across your organization, we understand that each team needs a certain level of autonomy to succeed.

**At the workspace level, admins can control:** | **While members can customize their team settings:** --- | ---
* [Statuses](https://linear.app/docs/project-status) to show the progress of each project
* [Updates](https://linear.app/docs/initiative-and-project-updates) for Initiatives and Projects
* Workspace templates for [Issues](https://linear.app/docs/issue-templates), [Projects](https://linear.app/docs/project-templates) and [Documents](https://linear.app/docs/project-documents#create-document-templates) | * [Statuses](https://linear.app/docs/configuring-workflows) that your Issues will move through
* Team templates for [Issues](https://linear.app/docs/issue-templates), [Projects](https://linear.app/docs/project-templates) and [Documents](https://linear.app/docs/project-documents#create-document-templates) for more specific requirements
* Custom [labels](https://linear.app/docs/labels) to categorize specific Issues. Labels can also be created at the workspace level for common Issues, like bugs
* [Estimates](https://linear.app/docs/estimates) to describe the complexity or size of an Issue
* Schedules for sprint-like structures called [Cycles](https://linear.app/docs/use-cycles)
* Configure [status updates](https://linear.app/docs/github#issue-status-updates) to linked issues when updates are made to PRs
These help with visibility across the organization by ensuring that all inputs feeding up to leadership use the same framework. | This flexibility allowed teams to work in ways that suited their unique needs while still fitting into the broader company structure.

---

## Migrating to Linear

Once you’ve got your teams set up in Linear, it’s time to start bringing over work from your other tools. Whether you’ve chosen to adopt Linear as your primary issue tracking and project management tool, or you’re integrating it alongside existing tools, data imports and synchronization are essential.

**Importing**

* Use the [Importer](https://linear.app/docs/import-issues) to pull in-flight issues into Linear and map them to appropriate teams. Linear offers native importers for GitHub Issues, Jira, Asana, Shortcut, and Trello
* Alternatively, you can import a CSV with issue data

**Syncing**

* Sync issues with [Jira](https://linear.app/docs/jira) and [GitHub](https://linear.app/docs/github#github-issues-sync) while trialing or transitioning to Linear to keep projects up to date across tools

---

## Planning

Linear brings planning and building together into one tool, eliminating the disconnect between strategy and execution. By keeping plans and progress in sync, teams maintain clear visibility while spending less time updating status reports and more time delivering value.

Linear offers several objects to track higher-level strategic goals (Initiatives), deliverables that roll up to them (Projects), and important progress stages (Milestones).

### **Using Initiatives, Projects, and Milestones**

![Initiatives](https://webassets.linear.app/images/ornj730p/production/2680d360daf1b22b15ed8b1eab84342eb35b9b61-3256x1394.tif?q=95&auto=format&dpr=2)

#### Initiatives

[**Initiatives**](https://linear.app/docs/initiatives): Designed to plan and manage strategic streams of work that span multiple Projects and longer timelines, such as major launches, product goals, or company-wide objectives. Typically set top-down, leaders use Initiatives to translate company strategy into visible progress by providing a single place for observing relevant Project timelines and updates.

_Examples:_

* _ENG / Launch Enterprise Offering_
* _ENG / Mobile App v2_
* _GTM / Grow Linear's customer base_

#### Projects

**[Projects](https://linear.app/docs/projects):** Enable leads and managers to coordinate work that underpins a company Initiative. They have a clear outcome or completion date, often encompass work from multiple people or teams, and last for several weeks to months.

_Examples:_

* _ENG / New Feature Launch_
* _ENG / Mobile App MVP_
* _Marketing / Customer Story Launch_

#### Milestones

**[Project Milestones](https://linear.app/docs/project-milestones):** Represent functional goals and deadlines within Projects that the team aims to achieve throughout its lifespan. Issues will be grouped by Milestone within a Project.

_Example_

* _Phases of each project; ex. Brainstorm, Design, Build, QA, Released._

### Assign a lead

Each Project and Initiative should have a lead, responsible for maintaining momentum, ensuring accountability, and preventing work from falling through the cracks. Project Leads don’t have to be team leads — they can be anyone best suited for the project.

### Draft the specification

Initiative and [Project Overview](https://linear.app/docs/project-overview) pages act as container for all the related information - documents, customer discovery notes, and designs.

![Project overview](https://webassets.linear.app/images/ornj730p/production/d9970576bed3615e3124981bbb85a0a80e2aa1b7-1832x1784.png?q=95&auto=format&dpr=2)

You can create [Documents](https://linear.app/docs/project-documents) at the Initiative and Project level. They can be used for tracking meeting notes, drafting PRDs, or expanding on certain aspects of the project.

## Building

### **Using Issues**

Issues are the atomic unit in Linear. They represent a specific piece of work, such as a task or bug, that has a clear output and might take anywhere from a few minutes to an hour or a day.

We've designed them to be zero-friction. Issues take seconds to create, which counterintuitively means your team will log additional bug reports and share ideas more frequently while spending _less_ time in the tool.

Each issue has [configurable properties](https://linear.app/docs/issue-properties):

* Categorized using labels
* Linked by relationships, such as _blocking_, _related_, or _duplicate_
* Assigned a due date and priority score
* Estimated in magnitude

You can create [recurring issues](https://linear.app/docs/creating-issues#create-recurring-issues) to automate your repeated tasks on a cadence of your choosing.

> [!NOTE]
> **Top tip:** You can create [sub-issues ](https://linear.app/docs/parent-and-sub-issues)when a set of work is too large to be a single issue but too small to be a project. Sub-issues also ideal for splitting up work shared across teammates. When you add a sub-issue to another issue, the other issue becomes its "parent."

↳ Doc: [Learn more about Issues](https://linear.app/docs/creating-issues)

### Working in Cycles

If you’re accustomed to working in sprints, [Cycles](https://linear.app/docs/use-cycles) offer a similar time-boxed structure but with automation at their core. They repeat automatically, roll unfinished work forward, and help you to build a clear picture of your [team’s true capacity](https://linear.app/docs/use-cycles#cycle-capacity) without introducing planning overhead.

---

## Understanding progress

### Updates

Both Projects and Initiatives include an [Updates](https://linear.app/docs/project-updates) feature. Leads will receive reminders from Linear to provide updates at regular intervals. These updates, along with progress tracking (On track, At risk, Off track), can be configured to post in Slack with bi-directional comment syncing — enabling you to keep the broader organization informed.

![Updates schedule](https://webassets.linear.app/images/ornj730p/production/e29e93134992c6ab6ef12509ad49c95b20cea06c-3312x1732.tif?q=95&auto=format&dpr=2)

As Projects progress, they move through [statuses](https://linear.app/docs/project-status) that you can configure at the workspace level.

![Project statuses](https://webassets.linear.app/images/ornj730p/production/42b6cd5957a5374626fbbd7106bf0833e28280f6-3312x1820.tif?q=95&auto=format&dpr=2)

Built-in [Project Graphs](https://linear.app/docs/project-graph) help you understand the progress your team is making towards completion, and offers estimates for when you'll finish.

![Project graph](https://webassets.linear.app/images/ornj730p/production/1583151e675c8ebcd8b2fd926362a15f4f407ea7-2880x1928.tif?q=95&auto=format&dpr=2)

### Go deeper with custom views and Insights

[Custom views](https://linear.app/docs/custom-views) enable you to create filtered views of issues or projects that you can save and share with others in your workspace. They can be private, available to everyone, or visible per team. They are particularly useful to see issues across multiple teams, projects, or a single label, like `label:bug`.

Views at the project level enable you to visualize progress in timelines, by progress, or status (n Track, At Risk, Off Track).

![Project timeline](https://webassets.linear.app/images/ornj730p/production/6a5478c3bc2de4eae7b848954548c9ddb2b0f53c-4460x2868.png?q=95&auto=format&dpr=2)

### Insights

[Insights](https://linear.app/docs/insights) come attached to every view in Linear, turning the data into visual reports that highlight trends, bottlenecks, and opportunities across your workspace.

Use them to:

* Track resource allocation across Projects
* Measure bug resolution speed and trends
* Evaluate estimation accuracy
* Retro cycle times to improve predictability
* Identify bottlenecks and blocking dependencies

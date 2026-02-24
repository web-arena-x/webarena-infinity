# Making the most of Linear

Welcome to Linear!

![Making the most of Linear](https://webassets.linear.app/images/ornj730p/production/69a3f5213c42e4aecc07639ed6e58c5a762202f0-2160x1326.png?q=95&auto=format&dpr=2)

This guide is designed to introduce you to the essential features of Linear and how best to use them within your software development lifecycle. Linear supports various agile methodologies but works best with [The Linear Method](https://linear.app/method), our philosophy on team workflows. In this guide, we will walk you through the four key phases of the development lifecycle within Linear: **Discover, Plan, Build**, and **Insights**.

## Discover

**Integrations with customer support platforms [Zendesk](https://linear.app/docs/zendesk), [Intercom](https://linear.app/docs/intercom), and [Front](https://linear.app/docs/front)** support and streamline the flow of customer requests between your ticketing tools and issue tracking.

**We offer a robust [Slack integration](https://linear.app/docs/slack)** and **Slack** **external request tooling,** [**Asks**](https://linear.app/docs/asks) (_Business and Enterprise Plan_), designed for managing your workspace requests coming from teams such as IT, HR, and Ops. Built by Linear and integrated with Slack, it streamlines your help desk workflows so that it’s easier than ever to submit, track, and manage requests.

All integrations designed to intake issues from other systems support [**issue templates**](https://linear.app/docs/issue-templates) and detection of **related issues within Linear.**

## Plan

### Initiatives, Projects, Milestones

#### Initiatives

**Initiatives** Each initiative represents a goal or objective an organization aims to achieve and to monitor their progress. This enables high-level planning across multiple projects and long timelines.

Company level objective, ex. “Meet customers where they are”, “Enterprise Readiness.”

**See our demo video on Initiatives [here](https://www.youtube.com/watch?v=FlDVDvzCmn0).**

#### Projects

**Projects** define larger pieces of work that have a clear outcome or completion date, such as launching a new feature.

Projects can be team specific or cross team; ex. “v2.0 Mobile App”, “SSO implementation” with assigned Start and Target dates.

#### Milestones

**Milestones** represent functional goals the team aims to achieve throughout a project’s lifespan.

Phases of each project; ex. Brainstorm, Design, Build, QA, Released.

**Project Templates**

[Project templates](https://linear.app/docs/project-templates) enable your team to predefine issues and milestones each time a new project is created. This keeps the team on the same page and moving all projects towards the same goals.

**Project Updates**

Use [Project Updates](https://linear.app/docs/project-updates) to keep stakeholders informed on the latest with a project. Project updates include a concise overview of project progress since the last update. Project Leads receive reminders for updates at a timed interval. Those updates and associated progress against the project can be configured for sharing in a Slack channel, introducing organization-wide visibility into what’s happening in Linear.

**Custom Project Views**

If you’d like to represent your team’s work in Projects in aggregate, you can build customized project views. You’d commonly use project views to see all projects planned for this quarter, or this half, or to represent all the projects your team is working on.

## Build

### Issues

[**Issues** are a collaboration interface](https://linear.app/method/write-issues-not-user-stories), where teams track and converse around work.

Use [**SLAs**](https://linear.app/docs/sla) (_Enterprise Plan_)—service level agreements—to set guidance for when time-sensitive issues should be completed, and give your team more tools to ensure important issues stay top of mind.

**Modeling issue relationships**

For [related issues](https://linear.app/docs/issue-relations#add-relationships), you can reference issues in Linear in comments and link them directly so that whenever that issue is picked up, or if a conversation ensues, all of the context going into that issue is captured in the issue history.

* _For duplicates_, Linear supports marking an issue as a Duplicate.
* _For blockers,_ Linear supports “Blocked by” and “Blocking” status for issues.

### Triage

Use [Triage](https://linear.app/docs/triage) to bring issues in from other teams. This offers a chance to review, update, and prioritize issues before they are added to the team's workflow. This feature is enhanced through the function of [Triage responsibility](https://linear.app/docs/triage#triage-responsibility) to bring your on-call rotation in from third-party sources, or configure responsibility for new issues directly in the app.

Visit our [blog article](https://linear.app/blog/planning-for-unplanned-work) to get into a little more depth about the Triage feature.

### **Customizing Linear for your organization**

#### Custom Views

[Custom Views](https://linear.app/docs/custom-views) are views of all issues filtered by any dimension available in Linear. Custom Views are particularly useful to see issues across multiple teams, projects, or a single label, like `label:bug`. They can be private, available to everyone, or visible per team. Once you create a view that you want to access frequently, favorite it for later use.

#### Working in Cycles

If your team plans work and executes within a set period of time, you’ll want to [use cycles](https://linear.app/docs/use-cycles) to track how much work is happening during those periods. Using cycles enables lightweight tracking of work being done, broken down by project and label via [cycle graphs](https://linear.app/docs/cycle-graph), and helps your team [predict capacity](https://linear.app/docs/use-cycles#cycle-capacity) using historical data. Keep one or two future cycles open for planning and visibility into what’s coming next.

#### **When to use Projects versus Parent/Sub Issues**

Projects in Linear offer features like progress tracking, target dates, Project Updates, and now Milestones, to break down the Project’s features into phases. We plan to continue investing in Initiatives and Projects, and will add even more functionality in the future.

We find that teams are using parent/sub issue relationships to model relationships between issues, and at times, to track larger groups of work that might not represent an entire planned Project.

In general, we recommend using Projects to track work on a Roadmap rather than the parent/sub issue relationship, since there tends to be a lot less visibility into the relationship that’s modeled in parent/sub issues.

> [!NOTE]
> As a best practice, we advise teams to leverage parent/sub issues to track smaller tasks with a logical grouping, and make sure that all parent and sub issues eventually roll up to a project.

#### **Automations**

[GitHub integration](https://linear.app/docs/github) supports linking commits, branches, and pull requests to Linear issues, automating your development workflow with Linear and speeding up communication between developers and the rest of the team.

#### Integrations

The Linear team offers in-house built [integrations](https://linear.app/settings/integrations) as well as a range of [third-party integrations](https://linear.app/integrations). Popular integrations include Zapier, where you can create customized workflows that are not currently supported natively in the app.

## Insights

[Insights](https://linear.app/docs/insights) (_Business or Enterprise plan_) is Linear’s built in reporting mechanism where you can find more information on what’s happening within your Linear workspace. Insights provides mechanisms for understanding both count based and duration based measures of issues. You can visualize those measures by dimensions like prioritization, label usage, or assignment.

A more simpler option is using our Google Sheets integration, which populations a [Google Sheet](https://linear.app/docs/google-sheets) with your issue data so you can run functions, queries, pivot tables, and more.

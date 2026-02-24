# Concepts

Gain a basic understanding of Linear's design so you can set up your workspace and navigate efficiently.

![Linear interface showing active issues page](https://webassets.linear.app/images/ornj730p/production/a6643535918840dfdc1e41e4515ef1fdde3fb59d-2820x1352.png?q=95&auto=format&dpr=2)

## Basic concepts

### Workspace

A Linear workspace is the container for all issues, teams and other concepts relating to an individual company (Vast.craft in the image above). As a user, you can have accounts on one or many workspaces and can switch between these accounts using the dropdown menu in the top left-hand corner of the application. Workspaces each have a unique URL in the style linear.app/example. When you log into Linear, you're logging into a specific workspace.

### Teams

A workspace has one or many teams within it. Teams typically represent groups of people who work together frequently, though in some cases you may choose to structure teams as parts of a product. Teams contain issues, and can have team-specific projects (though projects can also be shared between teams.)

Teams have their own settings available to configure features like Cycles, Triage, and Workflows so you can tailor each team to best fit how work gets done. Each team also contains an archive, which keeps a record of issues that are not being actively kept in your backlog (archive rules can be defined in team settings.)

### Issues

The most basic concept in Linear is the issue. Most other concepts in Linear are either associated with issues, or function to group issues together. 

An issue represents a task described in plain language. Each issue must belong to a single Linear team, has an identifier constructed of its team ID and number, like "ENG-123".

Issues are required to have a title and status – all other properties and relations are optional. This makes it quick to create issues and cuts down on unnecessary work (see [_Write Issues Not User Stories_](https://linear.app/method/write-issues-not-user-stories)).

We support basic issue properties such as priority, estimate, label, due date, and assignee. You can create relations between issues to mark issues as blocked or blocking or create sub-issues. 

You can create issues from anywhere in the app. Try it - open any page in the app and type `C`.

#### Workflows

As you work on and complete issues, they'll move through workflows; a group of ordered issue statuses defined per-team. These are the statuses that you'll see group issues on list views and show up as column headers on boards. We create a default workflow for you that you can further customize in Settings.

You can update issue statuses manually to reflect the current progress on that task. Where possible however, we recommend using integrations or automations to update issue status to avoid the need to "manage tickets".

For example, our GitHub and GitLab integrations move issues to _In Progress_ when you copy the git branch name and continues to update the status as the PR is drafted, opened, reviewed, and merged. Cycle automations move issues to and from the backlog and you can set issues to close and archive on their own so lists stay relevant.

> [!NOTE]
> **Special Statuses**  
> 
> 
> * **Backlog** is a status category in Linear. Each team has its own backlog and teams can add additional backlog statuses to group issues down further.  
> 
> * **Triage** is an optional status in Linear that makes it possible to review issues before accepting them and moving them to your team's backlog or cycles.

## Organizing issues

### Projects

Projects group issues towards a specific, time-bound deliverable, like launching a new feature. Projects have their own pages in Linear that display all issues related to a project, project details, and graphs that show progress and project completion date ranges. Projects can be shared across multiple teams and organized under Initiatives or Project views.

#### Milestones

Milestones are a concept used to further organize issues inside an individual project. For each project, define milestones in a way that represent meaningful stages of completion for that project, and assign issues in the project to those milestones.

You can filter by milestones in a project, and easily see how close to completion an individual milestone is at a given time based on the issues belonging to that milestone.

### Cycles

Cycles are similar to sprints and prioritize a set of issues during a specific time period. Cycles are automated and repeating; you'll set a start date and duration for cycles, which will then repeat every _N_ weeks_._ They specifically do not end in a release. Issues not completed during a cycle roll over to the next cycle and we display basic statistics around estimated workload and percentage completion. 

Cycles do not necessarily have a thematic grouping like Projects, and recur automatically according to a schedule, where Projects are intentionally curated.

### Issue Views

Views group issues according to a set of filters. Some issue views come standard like a team's _Backlog, All,_ or _Active_ issues, and you can define views based on any filter available in Linear. Because they're based on filters, views are dynamic -- when an issue meets the filter set defining the view they'll appear, when they no longer meet those criteria the issue will leave the view. Views can be constructed to be visible to only you, a particular team or your whole workspace.

* Access views to see all issues under a label, assigned to a user, or part of a particular cycle or project.
* My Issues is a curated set of views that shows you your assigned issues with the most relevant ones first, issues you've created, and ones you're subscribed to.

To build custom views, use filters on an existing view and then create a custom view from those parameters. You can also go to Views in the sidebar and create a custom view from scratch.

## Organizing Projects

### Project Views

Project views are accessible from the sidebar under a team. Projects will appear in those categories based on the status of the project. You can also view projects at the workspace level to get an overview of all projects within your organization.

As with issue views, Project Views are dynamic: when a project meets the filter criteria of the view it will appear there, when it no longer meets the criteria it will leave the view. Project views represent the actual state of projects in your workspace.

### Initiatives

Initiatives organize your projects and showcase the goals your company is working towards alongside their progress. Each Initiative contains a manually curated list of projects and Initiatives are presented within a single Initiatives view at the workspace level. This enables high-level planning across multiple projects and long timelines.  


Leadership and managers can use the top-level Initiatives view in their Linear workspace for a quick overview of ongoing goals, objectives, and their progress. 

## **Taking actions**

Whenever you do something in Linear that changes an issue, project, or another piece of data, you're taking an action.

### How it works

We've designed Linear so that you can take actions in multiple ways: using buttons, keyboard shortcuts, contextual menus, or by searching for the action in the command line. This makes it easy to figure out how to do anything in the app and build muscle memory since you're always following the same patterns. 

For example, let's say you want to apply the label _bug_ to an issue. You can follow any of these steps to do it:

* Open the issue and click the apply label button 
* Right-click on the issue from the board or list view and use the contextual menu 
* Use the keyboard shortcut `L` 
* Open the command menu `Cmd/Ctrl` `K` then search `label`.

To do anything else to an issue - add an estimate, set priority, update status, set the assignee, add it to a project - you follow pretty much the same steps. To do anything to a project from the initiative or project view, you also take similar steps.  

### Bulk actions

It's easy to update multiple issues at a time in Linear. You can move issues across teams, to and from cycles and projects, apply labels, and change status to tens or hundreds of issues at once. `Cmd/Ctrl` `A` will select all issues on a view and then you can take the action using any of the aforementioned methods. 

An `Undo` action (`Cmd/Ctrl` `Z`) reverses most actions. 

### Keyboard shortcuts

Your keyboard is the fastest method for using Linear. Even if you don't use keyboard shortcuts normally, we recommend learning ones for common actions such as creating an issue. These are the most helpful to learn:

`C` to create an issue in any view  
`Cmd/Ctrl` `K` to open the command menu  
`x` to select  
`Shift` `Up/Down` or `Shift` `Click` to select multiple  
`Esc` to go back or clear a list selection

Shortcuts cannot be remapped in Linear at this time, though we may consider adding custom shortcuts in the future.

![Gif showing keyboard shortcuts panel](https://webassets.linear.app/images/ornj730p/production/0b7cb2241179e14f43cdccd33387a8d9df8713c6-1200x813.gif?q=95&auto=format&dpr=2)

### Quick Navigation

Shortcuts follow patterns so that you learn them quickly. Navigate between views with `G`then `_`shortcuts: `G` then `I` to go to the Inbox, ``G`` then ``V`` to the current cycle, and `G` then `B` to the backlog. 

### Easy access

`O` then `_` shortcuts launch menus to then open items on a list. `O` then `F` opens favorites, `O `then `P` opens projects, and `O `then `C` opens cycles.

See the full list of shortcuts by pressing ``?``.

### Command menu

The command menu lets you search and take any actions applicable to your view or selection.

Launch the command menu with `Cmd` `K` on macOS or `Ctrl` `K` on Windows or Linux. 

Command menu actions are contextually dependent. For example, if you are looking at cycles and open the command menu, the command menu will first display commands that are related to cycles.

### Mouse

Of course, you can also navigate and take actions with your mouse. We have buttons, menus, and dropdowns throughout the app. Right-clicking on issues in lists or boards or projects on the timeline will bring up contextual menus.

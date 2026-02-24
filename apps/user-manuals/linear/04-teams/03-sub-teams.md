# Sub-teams

Group sub-teams underneath a parent team. Feature settings configured in the parent team drive alignment throughout the group.

> [!NOTE]
> Available to workspaces on our [Business](https://linear.app/pricing) and [Enterprise](https://linear.app/pricing) plans.

![Shows a mobile parent team with nested ios and android teams in Linear's sidebar](https://webassets.linear.app/images/ornj730p/production/8f60bea54b24eabdcf5877bba111161c744ef805-1072x749.png?q=95&auto=format&dpr=2)

## Overview

Sub-teams allow you to reflect your organization's structure in Linear, making it easier to understand and manage work across different levels of your company. Create new sub-teams to organize work into specialized units as your organization scales while keeping existing workflows standard within the group.

Concepts like cycles and labels set in a parent team are inherited by its sub-teams, allowing sub-teams to operate well both as individual units and as a unified whole.

## Basics

### Update an existing team to a sub-team

Go to Settings > Teams > Team hierarchy and select another existing team as its parent. Taking this action requires admin permissions. To protect the privacy of private teams, a private parent team may have only private sub-teams.

![Shows selecting a parent team under Team settings > Team hierarchy](https://webassets.linear.app/images/ornj730p/production/c954ed27ec8cbb0f86a1cf8308feda3938447985-2104x1009.png?q=95&auto=format&dpr=2)

### Create a new sub-team

When creating a new team, optionally designate it as a sub-team at creation. To protect the privacy of private teams, a private parent team may have only private sub-teams.

![Selecting team hierarchy when creating a new team](https://webassets.linear.app/images/ornj730p/production/560c41f14b0a6a1a18aa982097c82d3cbd7fe67c-1866x1448.png?q=95&auto=format&dpr=2)

### Configure a sub-team 

Once you've created a sub-team, a wizard will take you through any conflicts that need to be resolved. Common tasks include normalizing statuses between parent and sub-teams and resolving duplicate label conflicts. 

After configuring a sub-team, check its settings to customize features unique to that team (GitHub PR automations, for instance) to ensure they meet the sub-team's needs.

### Private parent and sub-teams

If a parent team is private, its sub-teams must also be private. If a parent team is public, its sub-teams may be public or private.

As with all private teams in Linear, a user can see private team-specific data only when they belong to the private team themselves.

As an example, given a private parent team A with private sub-teams B and C, a user belonging to A and C cannot see issues belonging to B, even if those issues are in a project or view shared with teams A and C. If there is a project shared between teams B and C, this user would only see issues belonging to team C in the project.

### Un-nesting a sub-team

Navigate to the sub-team's settings and click **Remove from parent...** under the "Team hierarchy" section. Once removed, you can expect:

* Labels, issue status, cycles, and members will no longer be inherited by the sub-team. We have a warning about this when you start to un-nest the team. Broadly speaking, inherited items that are not currently in use will be permanently removed, while anything actively used will be converted into independent copies so issues remain fully intact.
* Specifically, any inherited labels or templates that weren't used in the old sub-team are not carried over. Those that are used become standalone versions for that team.

## Parent and sub-team settings

### Parent team feature settings inherited by sub-teams

Certain settings from a parent team are enforced throughout all sub-teams. 

Feature | Inheritance by sub-teams
--- | ---
Membership | Members in a sub-team must also be members of the parent team. Guests are the exception to this and may belong to a sub-team but not its parent.
Status | Optionally, sub-teams can elect to inherit statuses from their parent team.
Cycles | If a parent team has a cycles schedule defined, all sub-teams will inherit the same schedule. If the parent has no schedule then sub-teams may define their own. When merging a sub-team cycle schedule with a parent's, past cycles remain untouched. The current cycle on the subteam will close, and upcoming cycles of the sub-team update to the closest parent cycles.
Estimates | Optionally, sub-teams can elect to inherit estimation settings from their parent team.

### Parent team feature settings accessible to sub-teams

Sub-teams benefit from other features used in the parent team, and retain the flexibility to create similar entities scoped to the sub-team.

Feature | Use in sub-team
--- | ---
Labels	 | Issues in a sub-team can use labels scoped to the sub-team, its parent team, or the workspace.
Templates	 | Issues in a sub-team can use a template scoped to the sub-team, its parent team, or the workspace.
Views	 | Sub-teams can have dedicated views. Issues in sub-teams are accessible in the views stored in their parent teams.

### Independent feature settings in sub-teams

Other features in sub-teams have no relation to the parent team and should be customized to meet the needs of the sub-team specifically. These include:

* Team timezone
* Recurring issues
* GitHub/GitLab automations

### Notification settings for sub-teams

* **Public sub-teams inherit Slack notifications from their parent team by default.**  
If the parent team has Slack notifications enabled, newly created issues in its public sub-teams will also post to the same Slack channel.
* **Sub-teams can have their own Slack notifications.**  
You can configure notifications on a per–sub-team basis, including sending updates to a different Slack channel. These notifications can run alongside the parent team’s notifications.
* **Private sub-teams do not inherit notifications.**  
Private sub-teams must have their own Slack notification settings enabled in order to send notifications to Slack.

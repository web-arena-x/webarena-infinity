# Private teams

Create private teams for issues that should only be accessed by certain workspace members.

> [!NOTE]
> Available to workspaces on our [Business](https://linear.app/pricing) and [Enterprise](https://linear.app/pricing) plans.

![Linear app showing a private team called Private Team.](https://webassets.linear.app/images/ornj730p/production/7c81aa05636cdf517bf18dd134a24077ce4e1f7a-1310x1064.png?q=95&auto=format&dpr=2)

## Overview

> [!NOTE]
> If you want a team to be public to all but a particular set of users, consider using the [Guest](https://linear.app/docs/members-roles#guest) role instead of making the team private.

This feature is available on Linear's Business and Enterprise [plans](https://linear.app/pricing). Anyone in the workspace can create a new private team. Only workspace owners, admins, and team owners can change visibility of an existing team.

Private teams are helpful in cases where:

* Work is sensitive and should be limited to only some team members (e.g. HR, customer data, founders or exec team).
* You want a personal team to keep track of issues.

## Visibility

**Private team:** Workspace admins can see all private teams in settings under [Settings > Administration > Teams](https://linear.app/settings/teams), update team settings, or join a private team by adding themselves as a member. If an admin attempts to join a team, they will receive a pop-up warning before confirming.

![Pop-up when an admin attempts to join a private team](https://webassets.linear.app/images/ornj730p/production/1fb4d5a858c6cbd4313e4b17c057bab9c325610f-1014x960.png?q=95&auto=format&dpr=2)

**Issues:** Those who are not a member of the private team will not be able to see issues associated with the team. You cannot @ mention a member in an issue in the private team if they are not already a member of the private team. See specific exceptions under _Share issues from a private team._  
  
**Projects created under public teams:** Projects created under public teams can also be shared with private teams. Only private team members will be able to see that the project has been associated with their team. Similarly, project issues related to the private team will only be visible to members of that team.   
  
If all public teams are removed from the project, it will become private and only visible to members of the private team from then on. 

**Projects created under private teams:** Projects created under private teams are visible to the private team members only. If the project is shared with a public team later on, the project will become visible to others. The name of the private team or issues from that team do not become visible to non-members.

**Initiatives:** Members of a private team can see its projects on the associated initiatives but those projects won't be visible to others.

## Configure

When creating teams from workspace settings, toggle the option **Make team private**.

!["Make team private" option when creating a team](https://webassets.linear.app/images/ornj730p/production/acb8f03aac5717df21fd3465d2a4c8f124cac9ef-1378x226.png?q=95&auto=format&dpr=2)

To make an existing team private or vice versa, go to your team's settings (right-click on the team from your sidebar) and then _Access and permissions > Change team visibility._ 

Any assignees that are not members of the private team will be removed and any subscribers to issues in the newly private team will be unsubscribed.

!["Change team visibility" section in Team settings.](https://webassets.linear.app/images/ornj730p/production/c9db20ba59b05ea9adada48c845e717ce600ef6a-1462x418.png?q=95&auto=format&dpr=2)

## Private team members

The person who creates a private team or converts an existing team to private becomes the default owner of the private team. 

Owners of a private team can go to _Members_ (from the team's settings page) to invite other workspace members to the team or promote an existing team member to team owner (admins can search for the team from _Settings > Administration > Teams_ and then select the three dot menu to access this page). 

Members of a private team can leave the team on their own, but they won't be able to re-join the team without an explicit invite.



## Share issues from a private team

> [!NOTE]
> This feature is available on Enterprise plans

Share an issue on a private team through the ⌘/Ctrl + K menu, or by selecting the _Share_ action in an issue's overflow menu. When an issue is shared, a banner at the top of the issue indicates whom it's shared with. Any team members can share or stop sharing an issue in that team.

This can be useful for cases where a user requires access to a particular issue, but not the wider team. Consider a private Security team sharing a vulnerability with specific developers—or an HR team that needs a manager to fulfill a sensitive task.

### Managing shared issues

When you share a team's issue with another user, they can view the issue and any of its sub-issues on the same team, sub-issues of those sub-issues, and so on. If an issue has sub-issues on a different team, it is not sharable. 

Users you share with can also leave comments, and change basic properties like assignee, status, priority or label. They cannot view projects associated with that issue or share the issue with others. 

When an issue is shared with you, it appears in _My issues_ under the _Shared_ tab, and you’ll be notified in your Inbox. You can view and update the issue and any of its sub-issue tree, but cannot view projects or cycles associated with that issue or share the issue with others.

## Exports

When exporting issues from the workspace using our Export tool, admins can choose to include issues from any private team.

![Option to include private teams in an export.](https://webassets.linear.app/images/ornj730p/production/db2c52ae1cbf88d897d62d65ac4a88da316e7f72-1426x544.png?q=95&auto=format&dpr=2)

## API Security Considerations

If your workspace has set up custom integrations or apps or is working with third party integrations, please consider their behavior and who has access to their output when adding private team data to Linear issues.

The API, webhooks, and integrations such as Zapier can expose a user's private team and issue titles. It's possible to access private issue data with the API if you are using a personal API key of a user that has access to private teams. Webhooks can also expose data from private teams as webhooks for private teams can be set up by team owners and workspace admins.

## Integrations

Some existing integrations have limitations to account for private data, while others will have more complete access to all workspace contents.

GitHub and GitLab | Private issues will be posted as linkbacks on PRs or MRs with the issue ID and link only
--- | ---
Google Sheets | Issue data from private teams is not accessible
Intercom | You cannot create or link issues in private teams
Sentry | You cannot create or link issues in private teams
Zapier | See our note above on API and webhooks
Zendesk | You cannot create or link issues in private teams
Front | If you have access to a private team, you can create and link to issues in that private team.
Airbyte | Information from all public and private teams will be loaded in Airbyte

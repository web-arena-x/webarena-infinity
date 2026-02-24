# Members and roles

Linear provides several role types to help you control access and permissions across your workspace. Each role gives team members the right level of access—from full administrative control to limited guest visibility.

## Overview

Administrative roles can manage workspace members and their from [Settings > Administration > Members](https://linear.app/settings/members). This page lists all active and suspended members and allows filtering by role or status (Pending invites, Suspended, or users who have left the workspace).

> [!NOTE]
> On Enterprise plans with [SCIM](https://linear.app/docs/scim) enabled, some or all member management will be accomplished through your IdP instead of the Members settings page.

## Managing user roles

### Changing a member's role

To update a user’s role:

1. Go to _Settings > Administration > Members_ page
2. Hover over a member’s row
3. Click the **overflow menu (⋯)**
4. Select the **Change role...**

### Suspend a member

Administrative roles can suspend a member from the workspace:

1. Go to [Settings > Administration > Members](https://linear.app/settings/members)
2. Hover over a member’s row
3. Click on the **overflow menu (⋯)**
4. Select **Suspend user...**

Suspended users lose all access immediately and are removed from your next billing cycle. They remain visible in the members list for historical purposes—for example, when viewing issues they created or were assigned to.

To view issue activity for a suspended user, visit their profile page at:  
`linear.app/<workspace-name>/profiles/<username>`

Admins can access this link from the user’s avatar or by filtering the Members page for **Suspended** users.

### Viewing workspace admins

Any member who needs to quickly identify workspace administrators can:

* Open Command menu `Cmd/Ctrl` `K` and select **View workspace admins**
* Navigate directly to [linear.app/settings/view-admins](https://linear.app/settings/view-admins)

---

## Role types

### Workspace owner

> [!NOTE]
> The workspace owner role is only available on Enterprise plans

Workspace owners have full administrative control, including access to the most sensitive settings such as billing, security, audit log, workspace exports, and approvals and team access management for OAuth applications. Admins in these workspaces, by contrast, have more limited permissions—ideal for routine workspace management.

In workspaces that need more flexibility, workspace owners can configure which roles can perform certain workspace-level actions via [_Settings > Administration > Security_](https://linear.app/settings/security) under the "Workspace restrictions" section.

**SCIM-managed workspaces**

Enterprise workspaces with brand new SCIM setups should create a `linear-owners` group to manage workspace owners, in addition to any other role groups described [here](https://linear.app/docs/scim#provisioning-roles). 

If you are upgrading an existing workspace that uses SCIM to the Enterprise plan, please look at [this article](https://linear.app/docs/changes-to-user-roles-when-upgrading-to-enterprise) to understand what actions you need to take.

---

### Admin

Admins have elevated permissions to manage routine workspace operations. This role is well-suited for managers, team leads, and operations-focused members.

**Free plan behavior**  
All workspace members become admins automatically

**Basic and Business plan behavior**  
The user who upgrades the workspace is granted the admin role

**Enterprise plan behavior**  
Admins will have limited permissions

---

### Team owner

> [!NOTE]
> Available on Business and Enterprise plans

Delegated control over how individual teams are run, without routing every change through workspace owners or admins.

**Configure team owners**

Workspace admins/owners or team owners may:

1. Go to _Team settings > Access and permissions_ and adjust settings to be restrictive to team owners only
2. Navigate to _Team settings > Members_ to promote members to team owners

There is no limit to the number of team owners a team can have, and teams are not required to have a team owner.

**Who are team owners?**

* _Workspace admins and owners_ are automatically team owners for all teams they can access. For any newly created team, the creator becomes a team owner by default
* Any team member can be promoted to team owner by an existing team owner or a workspace admin/owner
* Team owners in the parent team are team owners in the sub-teams
* Guests cannot be team owners

**Team owner only operations**

Certain critical actions are restricted to team owners only:

* Deleting a team
* Making a team private
* Changing a team's parent

**Configurable permissions**

![Team permissions](https://webassets.linear.app/images/ornj730p/production/2dfa78eee5af719095be345826537353c6d8f27b-1414x748.png?q=95&auto=format&dpr=2)

From _Team settings > Access and permissions_, team owners can choose whether to allow all members or only team owners to manage the following:

* **Issue Label Management** - Control who can create and edit team issue labels.
* **Template Management** - Control who can create and edit team templates.
* **Team Settings Management** - Control who can manage workflow statuses, cycles, triage rules, agent guidance, and other team settings.
* **Member Management** - Control who can add new users to the team. Note: Only team owners can add guest users, regardless of this setting.

> [!NOTE]
> Permission settings are not inherited from parent team to sub-team.

**Team access**

From _Team settings > Access and permissions_, team owners can also choose to restrict how members can join your team. By default, any member of your workspace can join a non-private team. Team owners now have the option to restrict access to only members they add or invite.

![Team access](https://webassets.linear.app/images/ornj730p/production/10c484efbd8dc5bfd8906dbf176ee9bf046a75e9-1368x496.png?q=95&auto=format&dpr=2)

---

### Member

Members can collaborate across teams they have access to and use all standard workspace features. They **cannot access** workspace-level administration pages

---

### Guest

> [!NOTE]
> Guest accounts are only available on Business and Enterprise plans, and are billed as regular members.

Guest accounts grant restricted access to specified teams—ideal for contractors, clients, or cross-company collaborators.

**Guests can**

* Access issues, projects, and documents for the teams they are explicitly added to
* Take the same actions as Members within those teams

**Guests cannot**

* View workspace-wide features such as workspace views, customer requests, or initiatives
* Access settings beyond their own **Account** tab

**Sharing projects with guests**

If a project spans multiple teams:

* Guests will only see issues belonging to the teams they’re part of
* They will still see the project shell, but only with their allowed team’s issues visible

**Integration security**

Integrations enabled for the workspace will be accessible to guest users, which could potentially allow them to access Linear data from teams outside those they're invited to join. To prevent data leakage:

* For Linear-built integrations (GitHub, GitLab, Figma, Sentry, Intercom, Zapier, Airbyte): Ensure guest users don't have access to your accounts on those services
* For integrations requiring email authentication (Slack, Discord, Front, Zendesk): These should automatically limit access to only issues and data in invited teams
* For third-party integrations: review access individually or contact the integration provider in the [Integrations directory](https://linear.app/integrations).

## FAQ

<details>
<summary>What permission will a user get if they are in both admin and owner groups in SCIM?</summary>
If a user is in two groups, they will get the permission of the most recent group that was pushed.
</details>

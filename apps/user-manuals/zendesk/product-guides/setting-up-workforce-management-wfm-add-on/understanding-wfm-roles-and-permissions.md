# Understanding WFM roles and permissions

Source: https://support.zendesk.com/hc/en-us/articles/6443374440090-Understanding-WFM-roles-and-permissions

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Understand workforce management roles and permissions to control access to features and data. Use standard roles like Admin and Agent or create custom roles to match your organization’s structure. Assign permissions for tasks like scheduling, reporting, and time-off management, and define scopes to limit access to specific teams and locations. This setup ensures users have the necessary access without overexposure.

Zendesk Workforce management (WFM) roles and permissions ensure that agents and
admins have access to the WFM features they need to use.

Your account includes standard, predefined roles that all Zendesk users are
initially assigned to. You can also create your own custom WFM roles to reflect your
organization's structure and access management system.

This article contains the following topics:

- [Overview of WFM roles and
  permissions](#topic_bzz_rzb_1bc)
- [Standard WFM roles](#topic_ngj_b1c_1bc)
- [Custom WFM roles](#topic_sw4_m1c_1bc)
- [WFM permissions](#topic_zcx_t1c_1bc)

Related articles

- [Creating custom WFM roles and assigning users](https://support.zendesk.com/hc/en-us/articles/6443314455834)
- [Managing WFM roles and permissions](https://support.zendesk.com/hc/en-us/articles/7037879703322)

## Overview of WFM roles and permissions

WFM roles and permissions allow you to manage who can do what in your account.
They help your organization run smoothly by making sure everyone has the access they
need.

There are two kinds of roles:

- **Standard roles** are predefined and can’t be deleted. All users in your Zendesk
  account are assigned to a standard role initially depending on what their role is in
  Zendesk.
- **Custom roles** are defined by admins who determine which parts of your WFM
  account users in these roles can access. This includes who can see which teams,
  locations, and workstreams.

When you assign someone to a role, they inherit the permissions and scopes
associated with the role. Note that users can be assigned to only one role at a time.

Both standard and custom roles have the same structure, which include:

- **Permissions** – Allows users to access certain areas of your WFM account, such as
  scheduling, reporting, or admin settings. Permissions keep your account secure and ensure
  that users have access only to what they need.
- **Scopes** – Determines the teams, locations, and workstreams that users have access
  to in their role. Setting the scope for a role allows admins to give users permission for
  certain features, without sharing information about all teams, locations, and
  workstreams.
- **Agents** – The users assigned to the role.

## Standard WFM roles

Your WFM account has two standard, predefined roles: Admin and Agent. By default, Zendesk
admins are automatically assigned to the WFM admin role. The rest of your Zendesk team
members are assigned to the WFM agent role.

In addition to the standard roles, you can create [custom roles](#topic_sw4_m1c_1bc) that reflect your organization’s structure and reassign
users to those roles.

### Admin role

The standard WFM admin role can’t be edited, except to be renamed, or
deleted.

WFM admins have [permissions](#topic_zcx_t1c_1bc) for all features, can manage which users are assigned to each role,
and their scope includes access to information about all teams, locations, and
workstreams.

Your account must always have at least one user assigned to the default WFM
admin role. For example, you may want your system administrator to be assigned to this
role so that they have full access to all features and resources in the system.

### Agent role

The standard WFM agent role can’t be deleted.

By default, the standard WFM agent role gives permission for agents to access
only the [Schedule](https://support.zendesk.com/hc/en-us/articles/6443374353434) in Zendesk Support. Admins can edit this
role to give permission to access more features though.

The scope for users assigned to the standard WFM agent role includes access to
information about their own teams, locations, and workstreams.

## Custom WFM roles

Custom WFM roles are roles admins create that reflect your organization’s structure. Create
custom roles to allow or restrict access and specify different permissions for your agents,
team leads, admins, managers, or other roles.

Common examples of roles you may want to create include:

- Manager
- Supervisor
- Team lead

See [Creating custom WFM roles and assigning users](https://support.zendesk.com/hc/en-us/articles/6443314455834).

## WFM permissions

WFM permissions are configured for each role. By configuring permissions for a role, you’re
defining whether users assigned to a role have access to certain WFM features.

Note: When you
configure permissions for a role, keep in mind that they are limited to the role’s
scope.

WFM permissions are segmented by the general feature area and include the following:

| Permissions | Description |
| --- | --- |
| Forecast and scheduling: | |
| - Forecast | Access the Forecast page and make changes to forecasts, including recalculating or regenerating. |
| - Schedule | Access the Schedule page and generate, publish, edit, delete and import schedules. |
| - Time off management | View, approve, deny, and reopen time off requests. |
| Reporting: | |
| - Custom reports | View, edit, create, export, and delete custom reports. |
| - System reports | View, duplicate, and export system reports. |
| - Scheduled reports | View, create, edit and delete scheduled reports. |
| - Dashboards | View, edit, create, and delete dashboards, including editing dashboard widgets. |
| - Agent activity | Access the Agent activity page and edit and delete activities. |
| - Agent attendance | Access the Agent attendance page. |
| Admin: | |
| - Organization structure | View and edit the account’s organization structure, which includes locations, workstreams, teams, and time off reasons. |
| - Automations | View, create, edit, and delete automations. |
| - Integrations | View and edit integrations by changing their parameters, including turning them on and off. |
| - Settings | Access and edit account settings. |
| Agent: | |
| - Agent schedule | Access the Agent schedule, request time off, create and manage shift trade requests. |
| - Team schedule | Access the Team schedule tab to see team schedules, time off and shift trade requests. |
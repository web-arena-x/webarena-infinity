# Getting started with Zendesk WFM: Admin guide

Source: https://support.zendesk.com/hc/en-us/articles/6514632760730-Getting-started-with-Zendesk-WFM-Admin-guide

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

This guide helps you set up Workforce Management (WFM) for effective workforce planning and volume forecasting. It covers planning your implementation, installing the feature, setting up your organization structure, managing user roles and access, creating general tasks, and configuring timezones for 24/7 support. You'll learn to define roles, manage schedules, and track time-off, ensuring streamlined operations and efficient resource allocation.

This guide is recommended for anyone who is responsible for workforce management (WFM) planning and volume forecasting, as well as the initial installation and organizational set-up of Zendesk WFM. Common roles include WFM planner, forecaster, admin, or manager.

Typically, planners take on an admin role in Zendesk WFM by setting up the system, importing Zendesk agents, and configuring basic settings.

This article contains the following sections:

- [Planning for your implementation](#topic_t5h_vdy_c1c)
- [Installing Zendesk WFM](#topic_zhp_j3y_c1c)
- [Setting up your organization structure](#topic_l4n_wmd_d1c)
- [Managing users and access](#topic_r51_xxd_d1c)
- [Creating general tasks for non-working tickets](#topic_okc_cc2_d1c)
- [Setting up timezones for 24/7 support](#topic_nll_qc2_d1c)

## Planning your implementation

Prior to setting up Zendesk WFM, you and your team should identify requirements and align on ownership of different workforce management workstreams. Some common considerations are outlined here.

Administrative planning and oversight:

- Zendesk WFM configuration and governance, including roles and permissions
- Forecasting, scheduling, reporting, and alignment around time-off reasons
- Organizational enablement and change management

Functional ownership and feature administration:

- Forecast and schedule generation and time-off management
- Daily schedule or intraday management
- Real-time monitoring and report analysis

For more information about the technical requirements for installation, see [Planning staffing with forecast and schedule](https://support.zendesk.com/hc/en-us/sections/6249100323098).

### Establish your initial forecast of ticket volume

The past six months of ticket data is brought over upon installation and you can generate a forecast. However, even before you install Zendesk WFM, you can establish a reliable estimate of ticket volume with just a month’s worth of ticket data. This pre-work helps you determine workstream needs and shift assignments for your installation.

For more information on setting up forecasts, see [Planning staffing with forecast and schedule](https://support.zendesk.com/hc/en-us/sections/6249100323098).

### Define roles and permissions

Granting access to agents and other admins is one of the first things you’ll do in Zendesk WFM. Organizations assign responsibilities for WFM in different ways and with different titles. Consider the following:

- **Admins**: Do you need additional admins to grant access as your workforce expands or contracts? Do you need help generating forecasts, schedules or setting up dashboards?
- **Managers**: Will all managers schedule and monitor day-to-day activity, or will you divide those responsibilities? Do you need someone to focus on intraday scheduling?
- **Agents**: Do you need to give some agents monitoring or team lead responsibilities?

You can also create Zendesk WFM roles so that you can distribute the work of managing your workforce as outlined above.

For more information, see [About agent permissions](https://support.zendesk.com/hc/en-us/articles/6443374440090).

## Installing Zendesk WFM

To activate Zendesk WFM, see [Buying Zendesk workforce engagement management add-ons (Zendesk WFM, Zendesk QA, and WEM bundle)](https://support.zendesk.com/hc/en-us/articles/6851584037146) or [contact our sales team.](https://www.zendesk.com/service/workforce-management/)

The Zendesk WFM icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_logo_icon.png)) appears in two places in your Zendesk Support account:

- The top menu bar where agents start and end their day
- The left sidebar where agents access their schedule and time-off requests.

### What you'll see after connection

When you connect your Zendesk instance to Zendesk WFM, you first land on the [Agent activity page](https://support.zendesk.com/hc/en-us/articles/6443347506970) in Zendesk WFM. You can view details about all team members in your WFM account by accessing the [User management page](https://support.zendesk.com/hc/en-us/articles/7052274669338).

The following data about your WFM team members is available:

- Name
- Email
- Group(s) membership in Zendesk
- Account status (active or inactive)

All agents, including Zendesk light agents, initially have the same permissions.

### What agents see after installation

Agents interact with Zendesk WFM minimally in their Zendesk ticketing interface — in the left sidebar where they’ll access their [schedules](https://support.zendesk.com/hc/en-us/articles/6443374353434) and in the navigation bar to [clock in or out of general tasks or ticketing work](https://support.zendesk.com/hc/en-us/articles/6443354661402).

## Setting up your organization structure

To configure Zendesk WFM, start by setting up your organizational structure.

Your organization structure contains the following pages:

- [Locations](#topic_axr_m4d_d1c)
- [Workstreams](#topic_ovl_qqd_d1c)
- [Team](#topic_ryg_x5d_d1c)
- [Time off reasons](#topic_qwn_qwd_d1c)

### Locations

Within locations, you create shifts and decide where and when work gets done. Group agents by geographic location or office designation and define operational rules for work hours. Shifts can be automatic, where your forecast determines shift start time, or fixed, the more common selection, where managers determine when shifts start and what occurs during those shifts.

A pre-configured location displays by default and includes the location name, hours, and shift requirements. You can add, edit, or delete locations from the admin panel.

For more information about adding shifts, different types of shifts, and shift intraday variants, see [Setting up locations and shifts in Zendesk WFM](https://support.zendesk.com/hc/en-us/articles/6443345205402).

### Workstreams

Workstreams segment work by organizing your team's tasks around Zendesk channels and other properties. Workstreams are a foundational component of WFM because they determine forecasts and daily schedules.

You can think of workstreams as ticket queues. By default, Zendesk WFM creates Tickets, Chat, and Voice workstreams to get you started. You can edit these workstreams and create others as well.

When you create a workstream:

- First, configure the **Settings**. This includes the workstream name, description, and color for visual identification in your forecast and team’s calendar.
- Next, define **Conditions** to select criteria for automatically assigning tickets to the workstream. Workstream conditions work similarly to the conditions in Zendesk business rules and determine which tickets go into the workstream.
- Finally, assign workstreams to your agents by group, team, or location.

Note: If you want to assign agents by team, return to this section after you've created your teams in the next step of the Organization structure set-up.

Workstreams can also be combined. For example, if you have a workstream for Tier 1 customers and one for Chat tickets, you could create a single workstream that assigns all Tier 1 chats and emails to one team for consistency.

For more information about creating, configuring, and combining workstreams, see [About Zendesk WFM workstreams](https://support.zendesk.com/hc/en-us/articles/6443314489242).

### Teams

Teams are groups of agents that report to the same manager. WFM teams are different from Zendesk groups, which tend to be defined around ticket or customer type.

Note: Agents and managers may be on more than one team, but teams can have only one manager.

For more information about how to create a team, see [Setting up teams in Zendesk WFM](https://support.zendesk.com/hc/en-us/articles/6443329411994).

### Time off reasons

For tracking time and forecasting capacity, you’ll need to understand when and why your agents take time off. You can add time off reasons for agents to select, such as a holiday or parental leave. There are two types of time-off reasons — planned and unplanned.

Tip: In your planning with other teams, you may want to map out time-off types and align them to other functions in your organization before creating time off reasons.

For more information about categorizing time off, see [Creating time off reasons for agents](https://support.zendesk.com/hc/en-us/articles/6443329403034).

## Managing users and access

You can define roles and permissions to suit your organization’s needs.

In Zendesk WFM, you’ll set up and manage agent roles and permissions in three places:

- At installation, you can allow or restrict access in a way that reflects your organization's structure and access management system.

  [Restrict access](https://support.zendesk.com/hc/en-us/articles/4409155972378#topic_xyf_wmw_qfb) to Zendesk WFM so that only agents in the groups or roles you list have access. For example, you can allow only a subset of agents, such as admins or a specific Zendesk group, to use the app. It's recommended to give all agents access though.
- From the [Agent Permissions page](https://support.zendesk.com/hc/en-us/articles/4408843830938-), click an individual agent’s profile to review their permissions. You can also change the agent's role here.
- On the Roles and permissions page, [create custom WFM roles](https://support.zendesk.com/hc/en-us/articles/6443314455834) to give agents modified permissions.

  Note: Zendesk light agents can use Zendesk WFM if you assign them a Zendesk WFM role but it will consume a full Zendesk WFM license.

### Roles

Create custom WFM roles that reflect the unique positions on your team, such as administrator, manager, team lead, or agent (of different types). You can create new roles as well as edit the existing, default roles.

- **Admins**: Depending on the size of your organization, you’ll need to determine whether you’ll have one or multiple admins. Grant admin access carefully and establish clear rules to follow.
- **Managers**: In Zendesk WFM, managers manage teams of agents. You may want to grant managers admin access so that they have the ability to view agent status up close, create schedules, and track reporting.
- **Agents**: You’ll decide whether all of your agents can use Zendesk WFM or just a subset. You'll also determine whether to define any special agent roles.

Tip: As you create new roles for different team members, you can return to Agent Permissions to re-assign agents to their new roles.

For more information about WFM roles, see [Creating custom WFM roles and assigning users](https://support.zendesk.com/hc/en-us/articles/6443314455834).

## Creating general tasks for non-ticketing work

General tasks are activities that happen outside of Zendesk, such as breaks, meetings, 1:1s, or training sessions. In Zendesk WFM, you or a manager can set up general tasks. Together with time spent on tickets, these tasks define your staffing forecast and appear in both your agent activity timeline and your historical reports.

For more information about general tasks, see [Creating Zendesk WFM general tasks](https://support.zendesk.com/hc/en-us/articles/6443329426330).

## Setting up timezones for 24/7 support

Choose the correct timezone and work week calendar in order for your shifts to align with your team’s availability, especially if you’ll leverage the auto-scheduling tool. Automations also key off of the set time.

For more information, see [Managing timezones in your Zendesk WFM account](https://support.zendesk.com/hc/en-us/articles/6443314319258).

If you’ll also have a role in creating schedules, review the [Getting started with Zendesk WFM: Manager guide](https://support.zendesk.com/hc/en-us/articles/6514633060634).
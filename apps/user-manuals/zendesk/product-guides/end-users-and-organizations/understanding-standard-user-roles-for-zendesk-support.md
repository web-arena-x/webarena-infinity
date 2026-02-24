# Understanding standard user roles for Zendesk Support

Source: https://support.zendesk.com/hc/en-us/articles/4408883763866-Understanding-standard-user-roles-for-Zendesk-Support

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

This article explains standard user roles, including end users, agents, admins, and account owners. End users submit and track tickets, while agents handle support requests. Admins manage settings and workflows, and the account owner oversees billing and account changes. Understanding these roles helps you assign appropriate permissions and responsibilities, ensuring efficient support operations and a streamlined ticket workflow.

Zendesk Support provides several standard user roles designed to meet common user needs and responsibilities. These roles give users predefined access and capabilities.

Each user's role is defined when they are added, although you may change a user's role as needed. When users sign in, they are only shown the parts of Zendesk Support that they are allowed to see and use.

This article describes the standard user roles in Zendesk Support. Depending on your plan, other roles may be available on your account, as described in [About team member product roles and access](https://support.zendesk.com/hc/en-us/articles/4408832171034).

Enterprise plans don't use a standard agent role. Instead, admins [define custom agent roles](https://support.zendesk.com/hc/en-us/articles/4408882153882).

This article contains the following sections:

- [End users, or customers](#topic_hlt_cbp_cc)
- [Agents, administrators, account owner (team members)](#topic_nqx_cbp_cc)
- [Agents](#topic_ibd_fdq_cc)
- [Administrators](#topic_evb_dbp_cc)
- [Account owner](#topic_fjb_ffq_cc)
- [User references in business rules](#topic_cwu_hbp_cc)

## End users, or customers

End users are also sometimes referred to as customers. These are the people who generate support requests from any of the available support channels. End users don't have access to any of the administrator and agent features of Zendesk Support. They can only submit and track tickets and communicate with agents publicly, which means that their ticket comments can never be private.

How your end users interact with Zendesk depends first on the support channels you've made available to them and then by how you've defined public access. You can provide either open or closed support. Open support in Zendesk means that anyone can submit tickets. Closed support in Zendesk means the opposite. For example, you might use closed support for an internal support operation within a corporation.

In a closed Zendesk, you add the end users. In an open Zendesk, you can either add users yourself or end users can add themselves by submitting tickets. If end users can add themselves, you can either require them to register or not. In a closed Zendesk, all end users must be registered.

You can also control if and how your end users access your help center.
This is the end user's view and includes the Submit Request page, the Knowledge Base, the Community (if available), and a view of their tickets. For more information on how end users can access Zendesk Support, see [Understanding options for end-user access and sign-in](https://support.zendesk.com/hc/en-us/articles/4408887573274).

However, if your end users aren't registered, they don't have access to that view of tickets (they must be signed in). For these end users, all communication with the support team is through email. For more information, see [Turning off ticket management in your help center to allow email-only support](https://support.zendesk.com/hc/en-us/articles/4408888722842-Setting-up-to-provide-email-only-support).

You also have the option of adding your end users to an organization, which is a collection of users (both end users and team members)
that can be used in many ways throughout your ticket workflow. For more information, see [About organizations and groups](https://support.zendesk.com/hc/en-us/articles/4408886146842).

## Agents, administrators, account owner (team members)

The people who resolve support requests play different roles in setting up and managing your ticket workflow. Agents, admins, and the account owner are all *team members*.

Other Zendesk products might have a dependency on Support user roles. For information about user roles in Chat, see [Understanding default roles in Zendesk Chat](../chat-basics/understanding-default-roles-in-zendesk-chat.md) and for Knowledge, see [Understanding Knowledge user roles and privileges](https://support.zendesk.com/hc/en-us/articles/4408827842458-Understanding-Guide-roles-and-setting-permissions).

### Agents

Note: Enterprise plans don't use a standard agent role. Instead, admins [define custom agent roles](https://support.zendesk.com/hc/en-us/articles/4408882153882).

Agents are the bulk of the support staff. They are assigned tickets and interact with customers as needed to resolve support issues. The agent's role and privileges are defined by admins and may include the following:

- May be added to more than one group (must be added to at least one)
- Add, edit, and delete end-user profiles. Agents cannot create or edit other agent or administrator profiles, and may not have permission to edit all properties in an end- user's profile.

 Agents can edit end users only if they have access to all tickets (see [About agent privileges and ticket access](https://support.zendesk.com/hc/en-us/articles/4408886939930-Adding-agents-and-administrators#topic_3zw_yl2_yg)).
- Add public or private comments or both to tickets
- Create and edit their own macros
- Create and edit their own views
- Can view reports. Only agents with access to all tickets in your Zendesk account will be able to view reports.
- Moderate and manage articles in the help center
- Access tickets in one of the following ways:
 - All tickets in your Zendesk account.
    Agents must have access to all tickets if you want them to be able to assign tickets to other groups.
 - Only tickets assigned to the group or groups to which they belong. Restricting an agent's permissions prevents them from making certain edits to users, including adding notes to user profiles.
 - Only tickets received from the organization to which they belong
 - Only tickets that they are assigned to

 The agent's groups and ticket access are [configured in the agent's profile](https://support.zendesk.com/hc/en-us/articles/4408886939930#topic_3zw_yl2_yg).

Admins can add new agents either manually one at a time or as a bulk import operation (you can set the user role in the CSV data file used in a bulk import). Agents can be promoted to the administrator role by an administrator.

Agents can be restricted to tickets within their [organizations and groups](https://support.zendesk.com/hc/en-us/articles/4408886146842). All agents must belong to at least one [group](https://support.zendesk.com/hc/en-us/articles/4408894175130). Agents and end users can both belong to [organizations](https://support.zendesk.com/hc/en-us/articles/4408882246298).
Agents with restricted ticket access (that is, access set to anything other than **All tickets**) can't create or edit end users.

Notwithstanding ticket access restrictions, CC'ing an agent on any ticket lets the agent receive email notifications of all public and private updates to the ticket. For example, suppose an agent is only allowed to see tickets in the L2 group. After the agent is CC'ed on a ticket in the L3 group, the agent gets email notifications of all public or private updates to the ticket even though she's not authorized to see L3 tickets.

### Administrators

Admins are agents with additional privileges to manage and customize your Zendesk. Admins can be assigned tickets like agents but they may also do the following:

- Access all tickets (not just the tickets they are assigned to)
- Access, create, and edit business rules (automations, macros, SLA service targets, triggers, views)
- Access and edit targets
- Install and configure apps
- Create reports
- Edit all reports
- Access and manage settings (account, security, channels, ticket fields, and so on)
- Add, manage, and delete end users, agents, and admins
- Promote agents to the admin role
- Create groups and organizations
- Assume an end user's identity
- Create custom agent roles (Enterprise plan only)
- Access and manage settings for voice

Admins on Enterprise plans can assign some of these permissions to agents by using custom roles. For more information and a list of permissions you can assign, see [Creating custom roles and assigning agents](https://support.zendesk.com/hc/en-us/articles/4408882153882).

Administrators are responsible for designing and implementing the ticket workflow. They add customers, agents, and other administrators; define the business rules (automations, triggers, views, etc.); and customize and extend Zendesk Support. Where an agent's primary function is to interact with customers and resolve support requests, administrators may do that as well as set up and manage the workflow.

Administrators can do all of the actions that agents can do.

### Account owner

The account owner is a type of administrator. The account name is associated with this person's name, usually the person who created the account. There can only be one account owner; however, account ownership can be reassigned by the account owner to another administrator if needed. The account owner has access to areas of Zendesk that other administrators do not. Examples:

- Subscription changes
- Billing and payment management
- Account changes

Only the account owner can update their account owner profile.
Other admins cannot do this.
For a full list of unique permissions associated with the account owner, see [Understanding account owner permissions](https://support.zendesk.com/hc/en-us/articles/4408846746778).

## User references in business rules

Business rules need to refer to some types of users in more abstract ways to define conditions and actions; therefore, you'll see references to *requester*, *submitter*, *assignee*, *current user*, and *non-restricted agent*.

### Requester

Requester refers to the person who is asking for support through a ticket.
By default, the requester of a ticket is the submitter, but the requester can be changed.
Requester is used in macros, views, automations, triggers, and reports to refer to the person that the support request is intended to help.

### Submitter

The ticket submitter is either the user who submitted the request or the agent that opened the ticket on behalf of the requester. By default, the submitter of a ticket is the requester, but the requester can be changed (the submitter cannot be).

### Assignee

Assignee is the agent assigned to a ticket. Assignee is used in macros, views, automations, triggers, and reports to refer to or set the assigned agent.

### Current user

In triggers, **(current user)** is the last person who updated the ticket. The **(current user)** changes each time someone different updates the ticket. The update can be made by any agent or end user with access to the ticket.

In views, **(current user)** is the agent who is currently viewing that view. This enables one view to show relevant tickets to each agent, without having to create a specific view for each individual agent (see [Creating views to manage ticket workflow](https://support.zendesk.com/hc/en-us/articles/4408888828570-Using-views-to-manage-ticket-workflow)).

### Non-restricted agent

A non-restricted agent is an agent who has access to all tickets. In other words, they have not been restricted to only the group or groups to which they belong, the organization they belong to, or to the tickets they have been assigned to. The ability to refer to these agents may be useful when creating triggers.
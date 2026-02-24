# About team member product roles and access

Source: https://support.zendesk.com/hc/en-us/articles/4408832171034-About-team-member-product-roles-and-access

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Explore team member roles and access settings to manage roles like Support, Knowledge, AI agents, Analytics, Voice, Chat, and QA. Customize roles to control permissions and access levels for admins, agents, and contributors. This centralizes role management, enhancing team efficiency and ensuring the right access for each team member. Check related articles for more on setting roles and editing profiles.

The Zendesk Admin Center provides a central location for setting a team member’s roles and access across multiple Zendesk product areas. A *team member* is anyone you add to a Zendesk account who is not an end user. Team members are also called *staff*, *admins*, and *agents*.

This article includes the following sections:

- [Support roles](#topic_pzw_3bs_qmb)
- [Knowledge roles](#topic_hct_wgt_qmb)
- [AI agents - Advanced roles](#topic_thq_lnf_dgc)
- [Analytics roles](#topic_mdb_g15_qmb)
- [Voice roles](#topic_a54_zlt_qmb)
- [Chat roles (live chat and messaging)](#topic_zys_xht_qmb)
- [Zendesk QA roles](#topic_nym_tzt_pgc)

**Related articles**

- [Setting roles and access in Zendesk Admin Center](https://support.zendesk.com/hc/en-us/articles/4408824375450)
- [Editing team member user profiles in Zendesk Admin Center](https://support.zendesk.com/hc/en-us/articles/4408832485914)

## Support roles

The following table shows the Support roles available in Admin Center. For more information, see [Understanding standard user roles for Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408883763866) and [Creating custom roles and assigning agents](https://support.zendesk.com/hc/en-us/articles/4408882153882).

| Role | Description |
| --- | --- |
| Admin | Can manage all Support settings except billing and can also manage Talk settings, regardless of their Talk role. |
| Agent (Team, Growth, Professional) | Can view and update tickets. Admins can control which tickets each agent can view and update. |
| Custom roles (Enterprise and Enterprise Plus) | Admins can define their own agent roles. Role settings control which tickets an agent can view and update. |
| Contributor (Chat Phase 4 only) | Can provide limited support by viewing and adding private comments to tickets in their groups. Contributors don't occupy an agent seat in Support unless they are manually upgraded to an agent role. If you have a Chat-only Phase 4 account, and later create an integrated Support account, existing chat agents will be added to your Support account as contributors. For more information, see [Creating agents and departments](https://support.zendesk.com/hc/en-us/articles/4408894143898-Creating-agents-and-departments) in the Zendesk Chat Help Center. |
| Legacy agent | This is a transitory role on Enterprise plans that includes all agents who have yet to be assigned to a role. For all these agents, we are maintaining the permissions they previously had on the plan you upgraded from. Also, you cannot assign agents to this transitory role. Lastly, this role disappears after all its members have been assigned to other roles. |
| Light agent | Light agent is a limited agent role. Light agents can be CC'd on tickets, can view tickets, and can add private comments to tickets within their groups. They cannot be assigned to or edit tickets. Light agents can be given permission to view reports or they can be restricted from viewing any reports. They cannot create or edit a report. The number of light agents you can add depends on your plan. See [Understanding light agent permissions](https://support.zendesk.com/hc/en-us/articles/4408846501402). You must have a Suite Growth plan or above, or a Light agents or Collaboration [add-on](https://support.zendesk.com/hc/en-us/articles/4408834152730), to have light agents. |

## Knowledge roles

The following table shows the Knowledge roles available in Admin Center. For more information, see [Understanding Knowledge roles and privileges](https://support.zendesk.com/hc/en-us/articles/4408827842458).

| Role | Description |
| --- | --- |
| Admin | Can manage all settings and permissions in Knowledge admin. |
| Agent | Can create, edit, and publish articles (if enabled by an admin). This role does not consume a seat when used in conjunction with the Light agent seat. However, it does consume an extra seat when used in conjunction with the Contributor seat. |
| Viewer | Can view and comment on published articles. (The team member will have the same permissions and access as an end user.) This role does not consume a seat when used in conjunction with a free Support seat such as Contributor or Light agent. |

## AI agents - Advanced roles

Within the AI agents - Advanced add-on, there are three user roles:

- **Client admin**: Can view, add, and edit all AI agents and users within an organization.
- **Client editor**: Can view and edit all AI agents within an organization.
- **Client user**: Can view and edit specified AI agents within an organization.

For instructions on creating users, see [Adding agents and admins and setting ticket access](https://support.zendesk.com/hc/en-us/articles/4408886939930). For information on controlling users’ access to specific AI agents within the add-on, see [Managing user access to advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756929562).

Tip: If you need to delete an AI agent or create a new organization, [contact Zendesk customer support](https://support.zendesk.com/hc/en-us/articles/4408843597850).

The table below lists the specific access levels for each role.

| | | | |
| --- | --- | --- | --- |
| **Access** | **Role** | | |
| **Client user** | **Client editor** | **Client admin** |
| **Features** | | | |
| Analytics | ✔️ | ✔️ | ✔️ |
| Training center | ✔️ | ✔️ | ✔️ |
| Content | ✔️ | ✔️ | ✔️ |
| Dialogue builder | ✔️ | ✔️ | ✔️ |
| Conversation logs | ✔️ | ✔️ | ✔️ |
| AI | ✔️ | ✔️ | ✔️ |
| **Settings** | | | |
| AI agent settings | - | - | ✔️ |
| CRM integration | - | - | ✔️ |
| Generative replies | - | - | ✔️ |
| Entities | ✔️ | ✔️ | ✔️ |
| Actions | View only | ✔️ | ✔️ |
| **AI agent access management** | | | |
| Browse user list | - | - | ✔️ |
| [Manage user access to advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756929562) | - | - | ✔️ |
| Edit AI agents | ✔️ (specified only) | ✔️ (all) | ✔️ (all) |
| **Exporting data** | | | |
| Conversation logs | ✔️ | ✔️ | ✔️ |
| Intents and training data | ✔️ | ✔️ | ✔️ |
| Translations | - | - | ✔️ |
| **AI agent and organization management** | | | |
| Create AI agents | - | - | ✔️ |
| Delete AI agents | - | - | - |
| Manage organization | - | - | ✔️ |
| Create new organization | - | - | - |

## Analytics roles

The following table shows the Analytics roles available in Admin Center. For more information, see [Giving agents access to Explore](https://support.zendesk.com/hc/en-us/articles/4408836002970).

| Role | Description |
| --- | --- |
| Admin | Can manage all settings and permissions in Explore. |
| Editor | Can create and manage dashboards, queries, and datasets. |
| Viewer | Can access shared dashboards. |
| The Explore Viewer role does not consume a seat when used in conjunction with a free Support seat such as Contributor or Light agent. If an agent has a custom role and the role has the **Manage channels and extensions** permission enabled, Support and Talk agents can make changes to Talk settings. | |

## Voice roles

The following table shows the Voice roles available in Admin Center. For more information, see [Giving agents access to Talk](https://support.zendesk.com/hc/en-us/articles/4408882966170).

Note: Support Admins can also manage Voice settings, regardless of their Voice role.

| Role | Description |
| --- | --- |
| Admin | Can manage all Talk settings but cannot make or receive calls. Does not require a Talk seat. |
| Team lead | A Talk admin who can also make or receive calls. |
| Agent | Can make or receive calls. |
| The Talk Admin role does not consume a seat when used in conjunction with a free Support seat such as Contributor or Light agent. | |

## Chat roles (live chat and messaging)

Chat roles are required for users working with live chat or messaging conversations. The following table shows the Chat roles available in Admin Center.

For more information on roles for messaging, see [Giving agents access to messaging channels](https://support.zendesk.com/hc/en-us/articles/6073485578010).

For more information on roles for live chat, see [Understanding default roles in Zendesk Chat](https://support.zendesk.com/hc/en-us/articles/4408882929946) and [Creating custom Chat roles and assigning users](https://support.zendesk.com/hc/en-us/articles/4408893917338).

| Role | Description |
| --- | --- |
| Admin | Can manage all Chat or messaging settings and provide chat or messaging support. |
| Agent | Can serve chats or messaging conversations, and provide chat or messaging support. |
| Agent (limited) | Can serve social messaging conversations and live chats only. |
| Custom roles (Enterprise) | Admins can define their own Chat roles. |

## Zendesk QA roles

The following table shows the Zendesk QA roles available in Admin Center. For more information, see [Understanding roles and permissions in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7043760141978).

Zendesk QA permissions apply to the [default workspace](https://support.zendesk.com/hc/en-us/articles/7043669430426#topic_wsw_cly_ydc) only. Additional [workspace permissions](https://support.zendesk.com/hc/en-us/articles/9203020826266) can be added on the Zendesk QA side.

| Role | Description |
| --- | --- |
| Admin | Can see everything and manage all settings. |
| Agent | Can view their own conversations, reply to feedback, and view their customer reviews. They have workspace-specific permissions and can view and edit data within their assigned workspaces only. They also have access to their own dashboard and can perform self-reviews, if enabled. |
| Reviewer | Can view all reviews but cannot edit workspace settings. Can perform peer reviews. |
| Workspace lead | Can view everything in the workspace and manage quizzes, assignments, groups, disputes, and calibration sessions. Cannot edit other workspace settings or scorecards. |
| Workspace manager | Can view all reviews and manage all workspace settings. |
| Connected user | Connected users don't have access to Zendesk QA. Their conversations are available for review, but these agents are unaware that they're being reviewed. |
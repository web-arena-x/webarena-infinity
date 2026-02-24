# Understanding roles and permissions in Zendesk QA

Source: https://support.zendesk.com/hc/en-us/articles/7043760141978-Understanding-roles-and-permissions-in-Zendesk-QA

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Understand roles and permissions to manage team access and security. Admins can set roles in Admin Center, while workspace permissions allow flexibility across different workspaces. Assign roles like Manager, Lead, Reviewer, or Agent to control access to features such as calibration, coaching, quizzes, disputes, and dashboards. Tailor permissions to fit your team's needs and streamline operations without compromising security.

Zendesk Admin Center provides a central location for setting team members’ roles and product access in Zendesk Quality assurance (QA). A team member is anyone you add to a Zendesk account who is not an end user. Additional workspace permissions can be added on the Zendesk QA side.

Ensuring that team members have the appropriate access levels maintains efficiency and security within your team.

This article contains the following topics:

- [About roles and permissions in Zendesk QA](#topic_kcp_yv1_cbc)
- [Workspace permissions](#topic_dzc_fgq_q2c)
- [Permissions by feature](#topic_ph4_bkq_42c)

Related articles:

- [Setting roles and access in Zendesk Admin Center](https://support.zendesk.com/hc/en-us/articles/4408824375450)
- [Managing users and workspaces in Zendesk QA](https://support.zendesk.com/hc/en-us/articles/7043760162074)

## About roles and permissions in Zendesk QA

Zendesk admins can update the following [Zendesk QA role permissions in Admin Center](https://support.zendesk.com/hc/en-us/articles/4408832171034#topic_nym_tzt_pgc):

- Admin
- Agent
- Reviewer
- Workspace lead
- Workspace manager
- Connected user

See [Setting roles and access in Zendesk Admin Center](https://support.zendesk.com/hc/en-us/articles/4408824375450).

Zendesk QA role permissions apply only to the [default workspace](https://support.zendesk.com/hc/en-us/articles/7043669430426#topic_wsw_cly_ydc), and users cannot be removed from the default workspace. Additional [workspace permissions](https://support.zendesk.com/hc/en-us/articles/9203020826266) can be added on the Zendesk QA side.

## Workspace permissions

Workspace permissions apply only within a specific workspace. Team members can have different permissions in different workspaces.

The following workspace permissions can be assigned:

| | |
| --- | --- |
| **Workspace permission** | **Description** |
| **Manager** | Can view all reviews and manage all workspace settings. |
| **Lead** | Can view everything in the workspace and manage quizzes, assignments, groups, disputes, and calibration sessions. Cannot edit other workspace settings or scorecards. |
| **Reviewer** | Can view all reviews but cannot edit workspace settings. Can perform peer reviews. |
| **Agent** | Can view their own conversations, reply to feedback, and view their customer satisfaction (CSAT) ratings. They have access to their own dashboard and can perform self-reviews, if enabled. |

## Permissions by feature

Different features in Zendesk QA have specific permissions associated with them:

| | | |
| --- | --- | --- |
| **Feature** | **Role** | **Permissions** |
| Calibration | - Admin, workspace manager, and lead | - Can create calibration sessions |
| - Reviewer | - Can participate in calibration sessions |
| Coaching | - Admin - Workspace manager, lead, and reviewer | - Can create new coaching sessions |
| - All members | - Can access coaching sessions |
| Dashboards | - Admin | - Can view all data from all workspaces |
| - Reviewer | - Can view all data where they are reviewers |
| - Agent | - Can only view their own workspaces’ data |
| Disputes | - Agents | - Reviewees (most commonly agents) can create disputes, depending on   workspace settings |
| - Workspace manager and lead | - Disputes can be escalated to a workspace manager or lead |
| - Reviewer | - Disputes can be sent to the initial reviewer |
| - Admin, workspace manager, and lead | - Can create disputes |
| Groups | - Admin | - Can create, edit, and delete groups |
| - Workspace manager and lead | - Can create, edit, and delete groups for their workspaces |
| Pins | - All users | - Can add pins |
| Quizzes | - Admin | - Can create new quizzes - Can access, change, delete, or publish quiz drafts - Can delete or archive all quizzes |
| - Workspace manager and lead | - Can create new quizzes |
| - All members in the workspace where the quiz was created | - Can access quizzes |
| Reviews | - All roles | - Can see reviews they received - Can edit and delete their own self-reviews   Agents can review the conversations where they're the assignee when the [Self-reviews workspace setting](https://support.zendesk.com/hc/en-us/articles/7043668704026) is enabled. |
| - Admin, workspace manager, lead, and reviewer | - Can see reviews of others - Can review any conversation   The reviewer role can't see reviews of others when the [Unbiased grading workspace setting](https://support.zendesk.com/hc/en-us/articles/7043668704026) is enabled |
| - Admin, workspace manager, and lead | Can edit and delete reviews done by others |
| Scorecards | - Admin | - Can create, edit, and delete scorecards, categories, and root   causes |
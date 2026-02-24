# Adding agents and admins and setting ticket access

Source: https://support.zendesk.com/hc/en-us/articles/4408886939930-Adding-agents-and-admins-and-setting-ticket-access

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Add agents and admins to manage customer support by manually entering details, bulk importing, or using the API. Customize user roles, ticket access, and privileges to fit your team's needs. Define user options like email, role, and language, and set agent permissions for ticket access and comments. Ensure you have available seats before adding new team members.

You can add team members (agents and admins) manually, through a bulk import of users, or
through the Zendesk API. You must be an admin to add team members.

This article covers the following topics:

- [Adding an agent or admin](#topic_h43_2k2_yg)
- [About the user options](#topic_kjp_mze_dc)
- [About agent privileges and ticket
  access](#topic_3zw_yl2_yg)

To add users in a bulk import, see [Bulk importing users](https://support.zendesk.com/hc/en-us/articles/4408893496218). To add users with the API, see [Zendesk Developer Tools: Introduction](https://developer.zendesk.com/documentation/developer-tools/).

Tip: To learn more about adding users and defining their roles, see the [Zendesk Support for Admins](https://training.zendesk.com/series/zendesk-admins/vilt-zendesk-support-for-admins-i) training course.

Related articles:

- [About the Team members page](https://support.zendesk.com/hc/en-us/articles/4408843830938)
- [Restricting agent ticket access by brand](https://support.zendesk.com/hc/en-us/articles/7584022494874)

## Adding an agent or admin

Admins can add any type of user (end users, agents, and other admins).

The account owner can also add agent seats to your subscription. The
account owner is included as an agent seat in your subscription.

Before you add a team member, you can check the **Seats remaining**
section of the Team members page to find out whether you have any available seats. If you don’t
have any seats left, you won’t be able to add the agent or admin.

**To add an agent or admin**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.

   The Team members page opens.
2. Click **Create team member**.
3. Enter the team member’s **Name** and **Email**, then click **Next**.
4. In the **Assign role** section, select the user’s Support role from the
   **Support** drop-down list, then click **Next**.

   You set only the Support role
   now. You can set other roles later.

   If the team member is an AI agents -
   Advanced user only and should not consume a Zendesk seat, select
   **Contributor**.
5. If the team member you're adding isn't an admin and your account has multiple brands,
   you may be prompted to select brands for the team member, depending on your [brand settings](https://support.zendesk.com/hc/en-us/articles/7584022494874#topic_yb2_whp_ngc). Select the brands that the team
   member should have access to. This [restricts the agent](https://support.zendesk.com/hc/en-us/articles/7584022494874) from accessing tickets in other
   brands.
6. Click **Save**.

   The new user is saved. If the **Also send a welcome
   email when a new user is created by an agent or administrator** option [is selected](https://support.zendesk.com/hc/en-us/articles/4408824350746#topic_vcv_xqj_v1b), the new user receives a welcome
   email and link to sign in.
7. (Optional) Click the new team member, who initially appears at the
   top of the list, to access their profile and assign any [additional roles](https://support.zendesk.com/hc/en-us/articles/4408824375450#topic_ppd_dky_lkb).

After you add the new team member, you can [open their Support profile](https://support.zendesk.com/hc/en-us/articles/4408822762650) to set [user options](#topic_kjp_mze_dc) and [agent permissions](#topic_3zw_yl2_yg). On
Enterprise plans, agent permissions are not set in the profile, but are determined by the
agent’s [custom role](https://support.zendesk.com/hc/en-us/articles/4408882153882).

## About user options

The following table describes the options that can be set for a new user.

| Profile data | Description |
| --- | --- |
| Name | User's name. |
| Email | Email address used for all email communications with the user. Team members can have more than one email address but one will be their primary email. |
| Role | Defines the user's function and access level in your Zendesk Support. There are two user types: End user and Staff Member. Customers are assigned the role *end user*. Staff members can be assigned a variety of roles, such as *agent* or *administrator*. On Enterprise plans, you can create custom roles for agents. Roles and product access are [managed in Admin Center](https://support.zendesk.com/hc/en-us/articles/4408824375450). Only admins can change a user's role. For information about user roles, see [Understanding Zendesk Support user roles](https://support.zendesk.com/hc/en-us/articles/4408883763866). For information about custom roles, see [Creating custom roles and assigning agents](https://support.zendesk.com/hc/en-us/articles/4408882153882-Using-custom-agent-roles-Enterprise-). |
| Contacts | Other contact information for the user, such as Phone, X (formerly Twitter) handle, Facebook page, and Google account. |
| Phone | Personal telephone number for the user. |
| Alias (Professional and Enterprise) | Alternative name for a team member to use on all communications with customers (also called end users) instead of their real name. If this field blank is blank, the team member's real name is used in email communications. |
| Signature | Closing line added to an agent's email notifications. |
| Tags | List of tags that will automatically be added to new tickets created by this user. Separate tags with a space. Tags are added to new tickets only, not updated tickets. This is an optional feature, and you may not have enabled user tagging. For more information about user tags, see [Adding tags to users and organizations](https://support.zendesk.com/hc/en-us/articles/4408881573658). |
| Organization | A collection of users (typically customers, but can include team members) created by an admin. On the Team plan, users can belong to only one organization. On Professional and Enterprise, users can belong to multiple organizations, up to 300. A user does not have to belong to any organization, however. For more information, see [About organizations and groups](https://support.zendesk.com/hc/en-us/articles/4408886146842). |
| Language | Language the user will view your Zendesk Support in. This setting affects this user only. |
| Time zone | Local time zone for the user; used to time stamp tickets. This setting affects this user only. |
| Details | Additional details about the user. Address, for example. Details are visible to other team members but not customers. |
| Notes | Additional notes about the user. Notes are visible to other team members but not customers. |

## About agent privileges and ticket access

When you add agents you need to define their privileges (groups they will be assigned to,
their access to tickets, if they can make both public and private comments, and their forums
access). These privileges are described in the following table.

Note: On Enterprise plans, you set the agent's groups in the agent's profile, but you do
*not* set agent permissions and ticket access in the agent's profile. Agent
permissions and access (except for groups) are determined by the [agent's custom role](https://support.zendesk.com/hc/en-us/articles/4408882153882).

| Privileges | Description |
| --- | --- |
| Brand membership | Defines the brands in which the user can view, search, and access tickets. Depending on your [configuration](https://support.zendesk.com/hc/en-us/articles/7584022494874#topic_yb2_whp_ngc), team members may be added to brands automatically when they are created, but you can modify their brand membership as needed.  A team member’s role can further refine their access. For example, a team member’s role might limit them to only tickets in their groups.  For more information about brand membership, see [Restricting agent ticket access by brand](https://support.zendesk.com/hc/en-us/articles/7584022494874). |
| Groups | List of groups the agent belongs to. Agents must belong to at least one group. Click the group name to edit the groups for the agent. For information about groups, see [Creating groups](https://support.zendesk.com/hc/en-us/articles/4408894175130#topic_wyj_dse_bc). |
| Access | Define the agent's access to tickets as one of the following:  - All tickets - Tickets in agent's groups - Tickets in agent's org - Assigned tickets only If you select to restrict the agent to an   organization, you must also set the agent's organization (on the **Add   user** page). See [Restricting agents to   an organization](https://support.zendesk.com/hc/en-us/articles/4408846640410#topic_ebz_dtn_bc).  Notwithstanding ticket access   restrictions, CC'ing an agent on any ticket lets the agent receive email   notifications of all public and private updates to the   ticket.  Agents must have **All tickets** access to create or edit   end users. However, agents with any ticket access level can create users   when setting the ticket requester to a new user.  Note: On Enterprise plans, you do not set ticket access in agent profiles.   Agent permissions are determined by the agent's custom role (see [Creating custom roles and assigning   agents](https://support.zendesk.com/hc/en-us/articles/4408882153882)). |
| Comments | Determine the type of comments an agent can make on tickets.  - **Notes and replies** enables the agent to add both internal notes and   public replies to tickets. - **Notes only** enables the agent to add only internal notes to   tickets. |
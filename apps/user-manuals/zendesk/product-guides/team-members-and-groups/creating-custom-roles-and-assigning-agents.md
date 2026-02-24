# Creating custom roles and assigning agents

Source: https://support.zendesk.com/hc/en-us/articles/4408882153882-Creating-custom-roles-and-assigning-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

Verified AI summary ◀▼

On Enterprise plans, you can create custom agent roles to match your team's unique workflow. Use predefined roles or create new ones, assigning agents to roles that define their permissions and access. Customize roles with specific permissions for tickets, people, channels, and more. Note that agents can't modify their own roles or admin roles.

On Enterprise plans, you can define your own agent roles and assign agents to those roles. This allows you to define agent roles that suit your own organizational structure and workflow. Several predefined system custom roles are provided to help you get started.

Admins and agents in custom roles with permission can create and assign custom roles.
However, agents can't modify their own role assignments or permissions or manage admin roles.

This article contains the following topics:

- [Understanding system custom agent roles in Zendesk Support](#topic_clf_k5q_qk)
- [Creating custom agent roles](#topic_cxn_hig_bd)
- [Assigning agents to custom roles](#topic_cbu_mmg_bd)

## Understanding system custom agent roles in Zendesk Support

There are a few predefined standard custom agent roles that reflect typical customer support roles. These are called *system* custom roles. These roles can be used as-is, or you can [create additional custom agent roles](#topic_cxn_hig_bd) by cloning them.

Table 1. Default agent roles

| Role | Description |
| --- | --- |
| Advisor | Advisors manage the workflow and configure your Zendesk. They create or manage shared automations, macros, triggers, and views. They also set up the service level agreements, channels, and extensions. Advisors don't solve tickets, they can only create tickets on behalf of end users and make private comments. |
| Staff | A Staff agent's primary role is to solve tickets. They can create tickets on behalf of an end user, edit tickets within their groups, view reports, and add or edit personal views and macros. |
| Team lead | Team leads have greater access to your Zendesk than staff agents. They can read and edit all tickets, moderate forums, create tickets on behalf of an end user, and create and edit end users, groups, and organizations. |

## Creating custom agent roles

You can create your own agent roles or base a new role on a [system custom agent role](#topic_clf_k5q_qk) that's predefined for you. You can either edit or clone most existing non-admin roles, or create a new role from scratch. You can create a maximum of 197 custom roles for your account. Each of your custom roles must have a unique name that isn’t too similar to the names of existing roles, such as *Admin* or *Administrator*.

**To create a new role**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Roles**.
2. Click **Create role**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/roles_add4.png)

   Alternatively, you can copy an existing role for your new role. Hover over the row of the role you want to clone, then click the options icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_options_icon.png)) and select **Clone**.
3. Enter a unique **Name** and **Description** for the role.

   The name must not be too similar to the name of existing roles, such as *Admin* or *Administrator*.
4. Define and create the agent role as described in [Permissions that agents with custom roles can have](#topic_tep_mig_bd).
5. When you've finished defining the new role, click **Save**.

### Permissions that agents with custom roles can have

When creating custom agent roles, you choose from an extensive list of permissions that define what agents can do.

| Permissions | Description |
| --- | --- |
| Tickets | You can define an agent's access to tickets, the types of comments they can make, and their editing permissions. An agent may access tickets that aren't suspended in one of the following ways:   - **Assigned to them** - **Requested by end users in their organizations**: Access   tickets created by end users only within their organizations.   Agents can still see what organizations are available within   their account, but they won't have access to any tickets   assigned to those organizations unless they are a member. Newly   created end users will automatically be assigned to the agent's   organization. If your account has multiple organizations, the   end user is assigned to the agent's default organization. - **Within their groups** - **Within their groups and all public groups**: Enable agents   to access and assign tickets within their groups, all public   groups, and tickets that haven't been assigned to a group. - **All, including those in private groups**: Access to all   tickets, including tickets in private groups they don't belong   to.   Notwithstanding ticket access restrictions, cc'ing an agent (including a Light Agent) on any ticket lets the agent receive email notifications of all public and private updates to the ticket. An agent may assign tickets to brands in the following ways: - **Only assign tickets to brands they belong to**: Assign   tickets only within their [brand   memberships](https://support.zendesk.com/hc/en-us/articles/7584022494874). - **Assign tickets to any brand**: Assign tickets to brands   they don't belong to. An agent may assign tickets to groups in the following ways: - **Only assign tickets to groups they belong to and public   groups** - **Assign tickets to any group**: Assign tickets to   private groups they don't belong to. An agent may manage [suspended tickets](https://support.zendesk.com/hc/en-us/articles/4408893392922) in one of the following ways: - **Not allowed**: Can't access the suspended tickets   view. - **Recover or delete**: Recover or delete suspended   tickets and export the list of suspended tickets. Interacting with tickets:   - **Edit ticket properties**: Be assigned to tickets and edit   properties. - **Edit ticket tags**: Add and remove tags on tickets. Agents   without this can still set custom fields. Agents without this   can't add tags with macros on existing tickets, but they can add   tags with macros upon ticket creation. - **Redact ticket content**: Permanently remove sensitive   ticket attachments and text in comments and side   conversations. - **Manage malicious attachments**: Manage access to   attachments with [detected malware](https://support.zendesk.com/hc/en-us/articles/4483794022170). - **Merge tickets**: Merge two tickets. - **Delete tickets**: Delete tickets and recover them. Can also   mark a ticket as spam if they have permission to delete the end   user.   - **View deleted tickets**: Access the deleted tickets     view, recover deleted tickets, and delete tickets     permanently.   Agents can add ticket comments in one of the following ways:   - **Private comments only** - **Public and private comments**   Additional ticket settings: - **View satisfaction prediction for tickets**: View the   predicted satisfaction ratings for tickets. Agents without   this permission can still see the satisfaction prediction in   views they can access. - **Manage ticket fields**: Create, modify, and delete   ticket fields using the Ticket fields page in Admin Center.   Agents can't take these actions through the API. - **Manage ticket forms**: Create, modify, and delete   ticket forms. |
| [Custom objects](https://support.zendesk.com/hc/en-us/articles/5914453843994) | You can define an agent's access to each custom object in your account. By default, agents don't have access to custom objects. They can be granted any combination of the following permissions for each custom object. - **View** - **Edit** - **Add** - **Delete**   Permission to **View** is automatically selected if you select any other type of permission for an object. |
| People | You can define an agent's access to users and user profiles. An agent may view and edit individual end user profiles in one of the following ways:   - **View only**: View end user profiles, but can't create new   end users. - **Add, edit, and assume profiles in organizations they belong   to**: Newly-created end users will automatically be   assigned to the agent's organization. If your account has   multiple organizations, the end user is assigned to the agent's   default organization. - **Add, edit, and assume profiles for any end user**:   Newly-created end users won't have an organization associated   with them. - **Add, edit, delete, and assume profiles for any end user**:   Newly-created end users won't have an organization associated   with them.   Permissions to edit end users enables the agent to verify end users. Only admins can change an end user's role. Managing custom agent roles: - **Create, edit, and delete roles**: Create and modify all   roles other than their own. Does not give permission to   assign roles to other agents. Viewing and managing customer lists with the Customer List add-on (for accounts created prior to September 9, 2020):   - **View only** - **Add and edit personal lists** - **Add and edit personal and groups lists** - **Add and edit personal, group, and global customer   lists**   Managing groups:   - **Add and remove team members from groups**: Manage team   members assigned to groups. - **Manage groups**: Create, edit, and delete groups.   Managing organizations:   - **Add, update, and delete organizations**: Add, update, and   delete organizations. Gives access to edit field values on the   organization. - **Manage organization fields**: Gives access to the Admin   Center pages for setting up custom organization fields.   Other user-related permissions: - **Manage user fields**: Create, modify, and delete custom   fields for user profiles for end users. (Only admins can   manage user fields for agents or other admins.) - **View customer lists**: Access the [Customers page](https://support.zendesk.com/hc/en-us/articles/4408828129946).   When this permission is deselected for agents, they can   still utilize auto-complete to access end-user information,   including name, email address, phone number, and   organization. - **Change agent status:** Change agent status from the   live reporting dashboard. This setting is available when   [omnichannel   routing](https://support.zendesk.com/hc/en-us/articles/5866925319962) is turned on. |
| Channels | Depending on the channels and admin permissions that have been enabled for your account, agents may also be allowed to do any of the following: - **Manage channels and extensions**: Manage channels   including email, social messaging apps, and other modes of   communication. Extensions include targets, webhooks, and   integrations. Note: Depending on   your admin permissions, some channels may not appear in   the menu. - **Manage Facebook pages**: Add Facebook pages that create   tickets from Facebook wall posts. - **Access saved X Corp searches**: Access   tweets from the X saved search   stream. - **Access Chat requests**: Access chats from end   users. - **Answer and place phone calls**: Answer calls from and   place calls to end users. |
| Agent workflow | The Agent workflow section includes access and editing permissions for views, macros, and dynamic content. Views are predefined conditions for a collection of tickets. Agents may access views in one of the following ways:   - **Play views only** - **See views only** - **Add and edit personal views** - **Add and edit personal and group views** - **Add and edit personal, group, and global views**   Additional views settings: - **Limit number of views**: Limits agents to the previous   default amount of views, which is a maximum of 12 shared   views and 8 personal views. Otherwise, agents will have   access to the default amount of views, which is 100 shared   views and 10 personal views. - **Access view filtering**: Allows agents to view and use   views filtering. This permission gives you more control over   the agent experience. - **CSV Export**: Allows agents to export CSV files, which   contain an entry for each ticket in the view, along with its   associated ticket information. Macros apply predefined actions to a ticket. Agents may do the following with macros:   - **Apply only**: Can apply macros, but can't add or edit   them. - **Add and edit personal macros** - **Add and edit personal and group macros** - **Add and edit personal, group, and global macros**   An agent can only update the groups on a macro if they are a member of every group. Additional agent workflow settings: - **Access dynamic content**: View, add, and edit dynamic   content. - **Manage contextual workspaces**: View, add, and edit   contextual workspaces. - **Contribute to side conversations**: Reply to or start   new side conversations with third parties or other agents   outside the ticket flow. Without this, agents can only view   side conversations. This option is only available if your   Zendesk plan includes side conversations (see [Using side conversations   in tickets](https://support.zendesk.com/hc/en-us/articles/4408844206746)). - **Create approval requests**: Create and withdraw   approval requests. This only pertains to creating and   managing approval requests, not actually responding to them.   No permissions are required to be an approver. |
| Business rules | You can decide if agents can manage business rules. - **Automations**: View, add, edit, and delete   automations. - **Skills**: View, add, edit, and delete skills. - **Service level agreements (SLAs)**: View, add, edit, and   delete SLAs. - **Triggers**: View, add, edit, and delete triggers. Does   not apply to [Slack ticket   triggers](https://support.zendesk.com/hc/en-us/articles/4963959597594). Agents can still view individual   triggers without this   permission. - **Business rules analysis**: Can access business rules   analysis. |
| Security and privacy | You can give agents security and privacy permissions. **[Manage deletion schedules](https://support.zendesk.com/hc/en-us/articles/8301879320474)** permissions include:   - **Not allowed** - **View only**: View deletion schedules only. - **Create, edit, and delete**: Can create, edit, and delete   deletion schedules.   **[Data masking](https://support.zendesk.com/hc/en-us/articles/9368104312602)** permissions (ADPP add-on): Hides end user personally identifiable information (PII) from the role. Log permissions include: - **[View audit   logs](https://support.zendesk.com/hc/en-us/articles/4408828001434)**: View the audit log to track changes   to your account. - **[View access   logs](https://support.zendesk.com/hc/en-us/articles/6066010357530)** (ADPP add-on): View the access log   to track what data has been accessed in your account. |
| Help center (if enabled) | You can give agents help center permissions. - **Manage Knowledge**: Access the help center as an admin   to manage articles, themes, and setting. When this option is selected, agents in this role have Knowledge admin permissions. When this option is not selected, agents in this role have Knowledge viewer permissions. For more information, see [Understanding Knowledge roles](https://support.zendesk.com/hc/en-us/articles/4408827842458#topic_gmm_j1c_qk). When this setting is *not* selected, it does not necessarily mean that agents can't add and edit articles and posts. Permission to add and edit articles is determined by user management permissions set on each article (see [Setting agent editing and publishing permissions on articles](https://support.zendesk.com/hc/en-us/articles/4408834435738)). Permission to add and edit posts is set at the topic level and applies to all posts in the topic (see [Allowing agents to add or edit posts in community topics](https://support.zendesk.com/hc/en-us/articles/4408821305498)). |
| Analytics (if Explore is enabled) | If Explore is enabled, you can configure the level of access that agents have to analytics. **Explore permissions** - **No access**: Cannot access Explore. - **View dashboards**: Can view dashboards shared with   them. - **Manage reports and dashboards**: Can create, edit, and   delete reports and dashboards. - **Manage reports, dashboards, and datasets**: Can manage   administrative settings and permissions for Explore. For additional details, see [Giving users access to Explore](https://support.zendesk.com/hc/en-us/articles/4408836002970). **Reports permissions** (in Support): - **No access**: Cannot access reports. - **View only**: Can only view reports. - **View, add, and edit**: Has full admin permissions. **View Talk dashboard**   - View details about calls on the [dashboard](https://support.zendesk.com/hc/en-us/articles/4408883025690). |

### Permissions that agents with custom roles can't have

There are some permissions that are available to admins that you can't assign to agents with custom roles. For example:

- Create or edit other agent or admin profiles
- Install apps
- Change a user's role
- Bulk import orgs or users
- Delete call recordings from tickets
- [Assume](https://support.zendesk.com/hc/en-us/articles/4408894200474)
 other agents
- Edit subscriptions (including trials)
- Generate and manage API tokens

For more information about agent and admin permissions, see [Understanding Zendesk Support user roles](https://support.zendesk.com/hc/en-us/articles/4408883763866).

## Assigning agents to custom roles

You can assign agents to a custom role from the role's settings or [from the agent's profile](https://support.zendesk.com/hc/en-us/articles/4408824375450).

**To add agents to a custom role**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Roles**.
2. On the role you want to add agents to, click the options icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) and select **Edit**.![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/roles_custom_edit.png)

   A detailed view of the custom role's settings is displayed. A list of team members in this role is visible in a panel on the right.
3. Click the **Actions** menu, then **Assign role**.

   The **Assign role** window is displayed.
4. In the **Select team members** field, select a team member from the list or search for a team member’s name and select it from the search results.

   To add additional team members, search again and select another team member.

   To remove an agent from the **Select team members** field, click the **x** next to their name.
5. Click **Assign role**.

   An updated list of agents in the role is displayed on the role settings page.
# Creating agents and departments in Chat

Source: https://support.zendesk.com/hc/en-us/articles/4408894143898-Creating-agents-and-departments-in-Chat

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

You need to create an account for each support agent who will be responding to chats. Depending on the size of your organization, you may want to organize these agents into departments, such as Billing or Shipments, to more efficiently direct visitors to an agent who can help them.

Note that the number of available agents and departments depends on your plan type.

This article includes the following topics:

- [Creating and updating agents](#topic_ozh_wyk_4fb)
- [Creating and updating department](#topic_mfr_wyk_4fb)

## Creating and updating agents

Each Chat agent needs a dedicated account in order to respond to chats. Each account, in turn, is assigned a role (default or custom) that grants the agent certain permissions. For information on roles, see [Understanding default roles in Zendesk Chat](https://support.zendesk.com/hc/en-us/articles/4408882929946) and [Creating custom roles and assigning users](https://support.zendesk.com/hc/en-us/articles/4408893917338).

Chat-specific settings can be edited on the **Edit Agent** page in the Chat dashboard. The procedures in this section assume you are starting from your Chat dashboard.

Global settings, such as an agent’s name, password, role, or enablement status are managed from the agent’s Admin Center profile. See [Adding agents and admins for more information](https://support.zendesk.com/hc/en-us/articles/4408886939930).

**To add an agent**

1. Go to your dashboard and select **Settings > Agents**.
2. Click **Add Agent**.
3. Enter the requested details:
   - **Name**: The agent’s name.
   - **Email**: The email address the agent uses to log into the dashboard.
   - **Role**: The role assigned to the agent.
4. Click **Add and configure** to create and enable the agent and continue configuring their profile. Or, click **Add** to create and enable the agent but configure their profile at another time

Administrators can update an agent’s profile and settings if needed. Note that the instructions here are for administrators editing *another* individual’s profile, not their own. To edit your own profile (whether you are an agent or administrator), see [Editing your personal settings in Zendesk Chat](https://support.zendesk.com/hc/en-us/articles/4408885997082-Editing-your-personal-settings-in-Zendesk-Chat).

**To edit an agent's profile information**

1. Go to your dashboard and select **Settings > Agents**.
2. Click the entry for the agent you want to update. This opens their Edit agent page. The settings at the top of the page is editable in Admin Center, while the remaining items are editable in the Chat dashboard.

   The following agent settings are managed in Admin Center. Click **Edit profile** to [update them in Admin Center](https://support.zendesk.com/hc/en-us/articles/4408886939930).

   - **Agent Status**: Indicates the agent's current status. If the checkbox is marked, the agent is Enabled.
   - **Name**: The agent’s name.
   - **Email**: The email address the agent uses to log into the dashboard. This field allows an admin to set who will be the assignee of the tickets created from chats of that user. If blank, the tickets will have no assignee. Make this update in your Chat dashboard **Settings > Agents** page.
   - **Role**: The role assigned to the agent.
   - **Profile**: Opens the agent’s profile in Admin Center.

   The agent settings at the bottom of the page are managed from the Chat dashboard.

   - **Display Name**: The name you want displayed when the agent is chatting with a visitor.
   - **Chat Limit**: The number of chats the agent can take simultaneously. If this setting is grayed out, chat limits are disabled. See [Configuring chat limits](setting-up-notification-routing-for-live-chat.md#topic_dlr_wt1_q5) for more information on enabling limits.
   - **Zendesk Support Email**: The Support email address that tickets created from this chat are assigned to.
   - **Skills**: The agent’s capabilities. See [Routing chats based on agent skills](routing-chats-based-on-agent-skills.md) for information.
3. When your changes are complete, click **Save Changes**. If you have other updates, see the procedures below.

## Adding and updating departments

Departments are collections of agents with a specifc coverage area or expertise. You can use departments in Zendesk Chat to filter chat requests to specific groups of agents. For example, you might want of your billing and payment questions to go to your Billing department, while troubleshooting questions should go to the Tech Support department.

Departments can be used to [automatically route chats](https://support.zendesk.com/hc/en-us/articles/4408881953434) to the right agents, or to specify which [pre-chat form](https://support.zendesk.com/hc/en-us/articles/4408882974234) should be presented to an end user requesting assistance.

Adding a department to your Chat account allows you to create and configure it. However, to use a department as described above the department must also be enabled.

**To add a department**

1. Go to your dashboard and select **Settings > Departments**.
2. Click **Add Department**.
3. Configure the following settings:

   - **Department Status**: Use the checkbox to enable or disable the department. Enabling the department allows you to include it in other areas, such as pre-chat forms or chat triggers.
   - **Name**: Give the department a name that makes it easily identifiable.
   - **Description (optional)**: Add a more detailed description of the department and its purpose.
   - **Department agents**: Click agent names to add them to the department.
4. Click **Create Department**.

**To edit a department**

1. Go to your dashboard and select **Settings > Departments**.
2. Click on the Department you wanted to edit.
3. Make the necessary changes, then click **Save changes**.
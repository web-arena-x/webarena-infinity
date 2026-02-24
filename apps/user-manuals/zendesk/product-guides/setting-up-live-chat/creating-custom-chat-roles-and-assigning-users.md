# Creating custom Chat roles and assigning users

Source: https://support.zendesk.com/hc/en-us/articles/4408893917338-Creating-custom-Chat-roles-and-assigning-users

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Enterprise |

You can create your own custom chat roles and assign those roles to any agent. Custom roles enable you to define agents' responsibilities, so they align with your organizational structure and workflow.

Custom roles are used in conjunction with default roles. For information about Chat default roles, see [Understanding default roles in Zendesk Chat](https://support.zendesk.com/hc/en-us/articles/4408882929946).

This article cover the following topics:

- [Understanding the predefined Chat roles](#topic_apr_rvc_k1b)
- [Creating custom roles](#topic_atq_tvc_k1b)
- [Assigning custom roles to agents](#topic_dh3_bwc_k1b)
- [Assigning shortcut roles](#topic_hxr_5pp_p2b)

## Understanding the predefined Chat roles

Zendesk Chat offers four predefined roles: owner, administrator, agent, and agent (limited). Each role is permitted access to different Chat features and functionalities. The owner and administrator roles are not customizable. You can customize the agent role permissions, but these settings will be applied to every user with the agent role. If you would like to assign different sets of permissions for individual agents, you will need to use custom roles (see [Creating custom roles](#topic_atq_tvc_k1b)).

For details on adding agents in Zendesk Chat, see [Creating agents and departments](https://support.zendesk.com/hc/en-us/articles/4408894143898).

Below is an overview of the available predefined roles. For more information on the predefined Chat roles, see [Understanding and managing roles in Zendesk Chat](https://support.zendesk.com/hc/en-us/articles/4408882929946-Understanding-and-managing-roles-in-Zendesk-Chathttps://support.zendesk.com/hc/en-us/articles/4408882929946-Understanding-and-managing-roles-in-Zendesk-Chat).

Table 1. Predefined agent roles

   | Name | Description |
| --- | --- |
| Owner | By default, the owner is the person who created the Chat account, but you can [change the account owner](https://support.zendesk.com/hc/en-us/articles/4408824174490) at any time. In addition to agent and administrator privileges, the account owner can upgrade or downgrade the account's plan, change billing information, access invoices, and cancel the account on the Chat account management page. You cannot modify permissions for the owner role. |
| Administrator | Administrators have access to of all the same privileges as regular agents (see [Chat role permissions](#topic_c1c_vvc_k1b)). They can also edit settings in **Widget** and **Account**, manage agents, triggers, and departments, and delete chats from History. You cannot modify permissions for the Administrator role. |
| Agent | Agents have restricted feature access. The owner and administrators can set their privileges in **Settings** > **Roles** > **Agent** (see [Chat role permissions](#topic_c1c_vvc_k1b)). While the agent role privileges can be modified, any settings you edit on the predefined agent role will be applied to all users assigned the agent role. If you would like to give individual agents different privileges, you will need to use custom roles. |
| Agent (limited) | Agents with this limited role can serve social messaging conversations and chats in the [Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930). This role is available only when the Zendesk Agent Workspace is enabled and the Social messaging add-on is activated on the account. |

## Creating custom roles

To apply unique permissions to different sets of agents, you will need to create custom roles. Custom roles can help you focus agents' workflow and align their privileges with their support responsibilities.

Note: Custom roles are included in your number of allowed agents.

**To create a new custom role**

1. From the dashboard, select **Settings**>**Roles**.
2. Next to the Search box, click the **Add Role** button.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_role_agent_list.png)
3. Enter a name and description for the new role.
4. Select the different permissions for the user role. See [Chat role permissions](#topic_c1c_vvc_k1b) below for descriptions of each permission.
5. Click **Create Role**.

You can edit the role any time by selecting it from **Settings** > **Roles**. See [Assigning custom roles to agents](#topic_dh3_bwc_k1b) for information on changing an agent's role.

### Chat role permissions

When creating custom user roles, you can choose from a list of permissions to define what agents can do.

Table 2.

   | Permissions | Options |
| --- | --- |
| Visitor List and Visualization | - **Visitors Seen**: Agents can view one of the following types of visitors:   - All visitors   - Department   - Personally serving - **Proactive Chatting**: Agents can view chats in one of the following ways:   - **Initiate and view chats**: Allows agents the ability to see visitors and manually select and prioritize certain visitors from the visitor's list. When this is enabled agents can serve chats over their specified limits   - **View chats**: Allows agents the ability to see all active chats in the visitor's list.   - **Personal chats only**: Allows agents to see only chats assigned to them. |
| Visitor Information | - **User Information**: Agents can edit visitor name, email, and phone. - **Notes**: Agents can edit notes. |
| History | - **View Past Chats**: Agents can view one of the following types of past chats:   - All chats   - Department   - Personal   - None - **Edit Chat Tags**: Agents can add/remove tags for past chats in History. |
| Visitor Banning | **Manage Visitor Bans**: Agents can temporarily ban visitors via browser cookies while in a chat or manage more permanent bans by IP. |
| Analytics | **Analytics and Email Reports**: Agents can access Analytics and Email Reports under personal settings. |
| Monitor | **View Monitor**: Agents can view real-time metrics on Monitor across the whole account. |
| Agent Management | **Departments**: Agents can edit department details and add or remove agents from a department. **Agent Chat Limits**: Agents can set chat limits for gents if agent limits are enabled. |
| Shortcuts | **Manage Shortcuts**: Agents can add, edit, and delete shortcuts that can be used by anyone while chatting with visitors. |

## Assigning roles to agents

You can assign a role to an agent by editing their profile, or you can assign a role to multiple agents at the same time. Agents with the disabled status will not be enabled by changing their role.

**To change the role of a single agent**

1. From the dashboard, select **Settings** > **Agents**.
2. Select the agent you would like to edit the role of. You will be redirected to the agent's user profile.
3. Click the **Role** field at the bottom of the profile and select a role.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Select_individual_user_role_profile.png)
4. Click the **Save Changes** button.

The agent role will be updated.

**To change the role of more than one agent**

1. From the dashboard, select **Settings**>**Agents**.
2. Select the checkbox next to the names of the agents you want to update.
3. Click the **Actions** button above the agents list, then select **Set Role**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Set_Role_Multiple_Agents.png)
4. Select a role from the **Roles** drop-down list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Reassign_Agent_Role.png)
5. Click **Set**.

The agents will be updated with the new role.

## Assigning shortcut roles

At the bottom of the role details page, There are four permission levels for agents and administrators working with shortcuts:

- **All shortcuts**: Can add and edit personal, department, and global shortcuts.
- **Department**: Can add and edit personal and department shortcuts.
- **Personal**: Can add and edit personal shortcuts.
- **None**: Unable to add or edit any shortcuts.

![](https://lh4.googleusercontent.com/QgUKxx3-ItP9dro6gc9RrMh7gvmteqOxxy-vYqC8TGbVMY2mo1ODfWkDROtzekrsO4vCl3qKj3n8PtlDNaBH2GgflAvuo-9pu8apPkCIjU53IVdoLWpOQvbR1emBl2G9k4jVzZk7)

For more information on shortcuts, see [Inserting common phrases with shortcuts](../live-chat-agent-guide/inserting-common-phrases-with-shortcuts.md).
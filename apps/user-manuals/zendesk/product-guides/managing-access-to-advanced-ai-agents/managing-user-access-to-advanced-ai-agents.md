# Managing user access to advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357756929562-Managing-user-access-to-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Access to the AI agents - Advanced add-on is controlled in Admin Center, where an admin must first create an account for a user and assign them an appropriate user role.

Users with the client admin role can then control which specific AI agents an individual user can access. How this AI agent access is controlled depends on whether the user is a client user, client editor, or another client admin.

This article contains the following topics:

- [Managing access to the AI agents - Advanced add-on](#topic_wn2_gbq_qhc)
- [Managing AI agent access for client users](#topic_ftl_54d_mgc)
- [Managing AI agent access for client editors and client admins](#topic_fzh_w4d_mgc)

Related articles:

- [Accessing the AI agents - Advanced add-on](https://support.zendesk.com/hc/en-us/articles/8357756913178)

## Managing access to the AI agents - Advanced add-on

Access to the AI agents - Advanced add-on is controlled in Admin Center. By default, the Zendesk account owner is the only user with access to the add-on and has an AI agents role of Client admin.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_managing_access_account_owner.png)

No other Zendesk admins have access to the add-on by default.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_managing_access_admin_default.png)

The account owner must first [grant other admins access](https://support.zendesk.com/hc/en-us/articles/4408824375450#topic_yvc_rky_lkb) to the add-on, and then [change their AI agents role](https://support.zendesk.com/hc/en-us/articles/4408824375450#topic_ppd_dky_lkb) as needed. For more information about permissions for each role, see [AI agents - Advanced roles](https://support.zendesk.com/hc/en-us/articles/4408832171034#topic_thq_lnf_dgc).

After that, any admin can then [create accounts for other users](https://support.zendesk.com/hc/en-us/articles/4408886939930#topic_h43_2k2_yg) and assign them to the appropriate AI agents role.

## Managing AI agent access for client users

Client admins can control which AI agents can be accessed by client users.

**To manage AI agent access for client users**

1. In AI agents - Advanced, in the left sidebar, select **Organization management** > **User access**.

   The Users page appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_user_access_list.png)
2. Hover over the user you want to manage AI agent access for and click the Edit icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/pencil_icon.png)).

   The Edit user pane opens. All fields except AI agents are read-only.
3. Click **Select AI agents**.
4. Select the AI agents that the user should be able to access.

   You can select more than one. You can also start typing to filter the results of the drop-down list.

   When you select an AI agent, it’s added above the AI agents field. You can click the X next to an AI agent to remove the user’s access to it.
5. Click **Save**.

## Managing AI agent access for client editors and client admins

By default, client editors and client admins have access to all AI agents. However, a client admin can [contact Zendesk customer support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to request that Zendesk restrict the AI agents that another client admin has access to.

When this happens:

- Client admins with restricted AI agent access can give other users access only to the AI agents they themselves have access to.
- If a client admin with restricted AI agent access is downgraded to a client editor or client user, they continue to have the same restricted AI agent access.

Note: Currently, client editors’ access to AI agents cannot be restricted.
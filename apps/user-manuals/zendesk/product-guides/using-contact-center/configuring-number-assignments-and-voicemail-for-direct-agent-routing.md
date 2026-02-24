# Configuring number assignments and voicemail for direct agent routing

Source: https://support.zendesk.com/hc/en-us/articles/10255377209498-Configuring-number-assignments-and-voicemail-for-direct-agent-routing

---

Direct agent routing gives customers and partners a fast path to the right person, reduces time in shared queues, and makes ownership crystal clear. You can use it to offer VIP access to specialists, streamline internal and partner calls, and capture after-hours messages with voicemail for timely followups.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Direct agent routing gives customers and partners a fast path to the right person, reduces time in shared queues, and makes ownership crystal clear. You can use it to offer VIP access to specialists, streamline internal and partner calls, and capture after-hours messages with voicemail for timely followups.

To achieve this, admins configure back office number assignments for agents. Back office number assignments can be either direct phone numbers know as direct inward dialing (DID) or internal extensions. Additionally, you can choose whether to offer voicemail for back office numbers.

This article contains the following topics:

- [Setting up a direct number for an agent](#topic_assign_direct_number_agent)
- [Setting up an extension for an agent](#topic_assign_extension_agent)

Related articles:

- [Configuring user-based voicemail](https://support.zendesk.com/hc/en-us/articles/10255333454490#topic_user_based_voicemail)

## Setting up a direct number for an agent

When setting up a dedicated phone number for an agent using DID, you can choose whether to offer voicemail and a custom message on that number.

**To assign a direct number to an agent**

1. In [Contact Center](https://support.zendesk.com/hc/en-us/articles/9696121449114), click **Admin Settings**.
2. Click the settings icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_cogs_icon.png)) in the sidebar.
3. Click the **Backoffice** tab at the top.
4. Click **New DID Configuration**.
5. In the new DID configuration, select the **Agent** this phone number will route calls to.

   This is the DID owner.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_backoffice_did_add.png)
6. Enter the dedicated **Phone number** for this agent.
7. (Optional) Select **Enable voicemail** to offer voicemail for this number when the agent is unavailable.
8. (Optional) Select **Use custom message** to play a custom voicemail message for this number when the agent is unavailable.
9. (Optional) Under **Voicemail language**, select the language to use for the voicemail prompt.
10. (Optional) Enter the custom **Voicemail message** to play to callers.
11. (Optional) Select **Enable call recording** to record calls to this number.
12. Click **Create configuration**.

## Setting up an extension for an agent

When setting up an internal extension for an agent, you can control whether callers can leave voicemail on that extension and, if so, configure voicemail settings such as language and custom prompt options.

**To assign an extension to an agent**

1. In [Contact Center](https://support.zendesk.com/hc/en-us/articles/9696121449114), click **Admin Settings**.
2. Click the settings icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_cogs_icon.png)) in the sidebar.
3. Click the **Backoffice** tab at the top.
4. Click **New Extension Configuration**.
5. In the new extension configuration, select the **Agent** this extension will route to.

   This is the extension owner.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_backoffice_extension_add.png)
6. Enter the dedicated **Extension** number for this agent (for example, 1001 or 2001).
7. (Optional) Select **Enable voicemail** to offer voicemail for this number when the agent is unavailable.
8. (Optional) Select **Use custom message** to play a custom voicemail message for this number when the agent is unavailable.
9. (Optional) Under **Voicemail language**, select the language to use for the voicemail prompt.
10. (Optional) Enter the custom **Voicemail message** to play to callers.
11. (Optional) Select **Enable call recording** to record calls to this number.
12. Click **Create configuration**.
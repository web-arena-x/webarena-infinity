# Activating focus mode for voice and chat in the Zendesk Agent Workspace

Source: https://support.zendesk.com/hc/en-us/articles/4408835750042-Activating-focus-mode-for-voice-and-chat-in-the-Zendesk-Agent-Workspace

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article describes how to activate and deactivate focus mode in the Zendesk Agent
workspace. Focus mode enables admins to set conditional routing based on agent activity for
voice and chat.

This article includes the following sections:

- [About focus mode](#topic_oht_2cs_n4b)
- [Activating and deactivating focus mode](#topic_bx4_fcs_n4b)

Note: To configure focus mode for omnichannel routing, see [Managing your omnichannel routing configuration](https://support.zendesk.com/hc/en-us/articles/4828787357210).

## About focus mode

When activated with the [Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930), *focus mode* allows agents to be
online for both voice and chat conversations but only serves the agent one channel at a
time. For example, if an agent is on a call, they will not be offered chats until the call
and call wrap-up has ended. If an agent is responding to a chat or handling multiple chats
(up to the maximum chat limit), then no calls are offered to the agent until all their chats
have ended.

By default, agents can get calls and chats at the same time.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_focus_mode_default.png)

When focus mode is activated, an agent working on chats will not receive calls until their
chats have ended.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_focus_mode_chat.png)

When focus mode is activated, an agent taking a call will not be offered chats until their
call and call wrap-up has ended.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_focus_mode_talk.png)

Focus mode is excluded for direct call and chat transfers between agents. Agents can
transfer a call to another agent who is actively engaged in a chat. Similarly, agents can
transfer a chat to another agent who is actively working on a call.

Within the Agent Workspace, focus mode is available only for customers using Zendesk voice
and chat. It is not supported for [Talk Partner Edition](https://support.zendesk.com/hc/en-us/articles/4408819751194), Zendesk messaging, or web and social
messaging channels. However, when [using focus mode with omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4828787357210), it is available for
Zendesk voice, chat, and messaging (including web and social messaging channels).

## Activating and deactivating focus mode

The Agent Workspace focus mode setting is visible for all the accounts that have the
Zendesk Agent Workspace activated, but aren’t using [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514).

Focus mode is off by default. If you activate focus mode, then later [deactivate](https://support.zendesk.com/hc/en-us/articles/4581758611866) the Zendesk Agent Workspace, focus mode is deactivated
automatically.

Note: If you've activated omnichannel routing, you must manage your focus mode settings in the
[omnichannel routing configuration](https://support.zendesk.com/hc/en-us/articles/4828787357210#topic_ymt_btp_m5b).

**To activate focus mode**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Agent interface**.
2. In the **Focus Mode** section, select **Enable focus mode for live
   channels**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_focus_mode_sm.png)
3. **Save** your changes.

**To disable focus mode**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Agent interface**.
2. In the **Focus Mode** section, deselect **Enable focus mode for live
   channels**.
3. **Save** your changes.
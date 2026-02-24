# Turning on automatic conversation acceptance for agents

Source: https://support.zendesk.com/hc/en-us/articles/6009407849754-Turning-on-automatic-conversation-acceptance-for-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Admins can configure messaging and live chat conversation routing so agents are
served new, incoming messaging and live chat requests without needing to click the
Conversations or Accept buttons. Automating this part of the agent’s process can
significantly boost efficiency, ensuring optimal use of available agent
capacity.

Auto-accept is available for messaging and live chat users. If you're using standard
routing for messaging and live chat conversations, auto-accept is activated and managed
in the Chat dashboard. However, if you are using omnichannel routing, your configuration
options are managed in Admin Center.

Note: Turning on auto-accept may remove chat
acceptance data from [Chat analytics](../reporting-for-for-live-chat/monitoring-chat-activity-with-analytics.md) and activity
monitor.

For information on automatic conversation acceptance for agents, see [Automatically accepting live chat and messaging conversations in
the Agent Workspace](https://support.zendesk.com/hc/en-us/articles/6442469463194).

This article covers the following topics:

- [About the auto-accept feature](#topic_rdc_5yy_fzb)
- [Turning on auto-accept for messaging and live chat](#topic_jpb_qzy_fzb)
- [Turning on auto-accept for messaging users with omnichannel routing](#topic_e5g_qzy_fzb)

## About the auto-accept feature

Auto-accept is available for messaging and live chat customers on all plans with
accounts that meet the following requirements:

- Agent Workspace is activated. See [Activating and deactivating the Zendesk
  Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4581758611866).
- Assigned routing is activated. Hybrid mode can be activated if
  needed. See [Setting up notification routing for
  messaging](https://support.zendesk.com/hc/en-us/articles/5020833543450).

The following limitations currently apply to the auto-accept
functionality:

- It is not compatible with the [Broadcast mode](https://support.zendesk.com/hc/en-us/articles/4408836490138#topic_nzf_pdb_pmb) of routing.
- Reassignment capability is not supported.

## Turning on auto-accept for messaging and live chat

The auto-accept option for messaging and live chat users is managed in the
Chat dashboard.

Note that if Hybrid mode is activated for notification routing, the agent experience
will be impacted. See [Configuring hybrid assignment mode](https://support.zendesk.com/hc/en-us/articles/4408836490138#topic_wyd_vy1_q5).

**To turn on auto-accept for messaging and live chat users**

1. In your Chat dashboard, select **Settings > Routing**.
2. Click the **Settings** tab, and make sure **Assigned**
   is selected for chat routing. Auto-accept options are only displayed if
   Assigned is selected.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/auto-accept-messaging.png)
3. In the Auto-accept section, select **On**.
4. Click **Save changes** at the bottom of the page.

## Turning on auto-accept for messaging users with omnichannel routing

If you have activated omnichannel routing, auto-accept is managed in Admin
Center as part of the omnichannel configuration. Note that even with omnichannel
routing activated, currently the auto-accept feature only works with messaging
conversations.

Auto-accept functionality is not compatible with reassignment timing, which
must be turned off before activation.

**To turn on auto-accept for omnichannel users**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)**Objects and rules**
   in the sidebar, then select **Omnichannel routing > Routing
   configuration**.
2. On the Routing Configuration page, click **Edit** next to the
   configuration you are using.
3. In Messaging routing section, select the following options:
   - **Wait until an agent accepts**.
   - **Auto-accept for an agent**.
4. Click **Save** at the bottom of the page.
# Configuring and using call monitoring and barging in Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9790996719770-Configuring-and-using-call-monitoring-and-barging-in-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Enable call monitoring and barging to let agents listen in on ongoing voice contacts and join if necessary. Configure these features in Amazon Connect, ensuring both Contact Center and Amazon Connect are open. Monitoring is discreet, while barging alerts the agent. This setup helps manage calls effectively and provides support when needed.

You can give agents permission to monitor another agent's ongoing contact and
join, or *barge* in, it if needed. These options are supported on voice contacts
only.

You configure monitor and barge in Amazon Connect. Agents must have both
Contact Center and Amazon Connect open to use monitor and barge.

This article contains the following topics:

- [Configuring monitoring and barging](#topic_f4c_5c3_wgc)
- [Monitoring an agent's contact](#topic_lhp_1d3_wgc)
- [Barging in on a contact](#topic_mkk_cd3_wgc)

## Configuring monitoring and barging

You can turn on monitoring and barging so that agents can monitor another agent's
contact and barge in, if needed..

**To configure monitoring and barging**

1. In Contact Center, click the Settings icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_settings_icon.png)), then click **Workflows**.
2. Find the relevant workflow, then click **Edit workflow**.
3. Configure the **Notes** and **Resolution Codes**, as shown.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cont_cent_barge.png)

## Monitoring an agent's contact

If monitoring and barging is turned on, an agent can monitor another agent's ongoing
contact. The agent being monitored is not aware that they are being monitored.

**To monitor a contact**

1. In Amazon Connect, select **Analytics and optimization** >
   **Real-time Metrics** > **Agents** to open the Real-time Metrics.
2. Find the agent you want to monitor.
3. Click the **Eye** icon next to the Voice channel for the
   agent.
4. Select Zendesk for Contact Center, where you will monitor the
   agent.

## Barging in on a contact

An agent who is in monitoring mode can barge in to join the ongoing contact, if
needed. When you barge in on a contact, the agent knows that you have joined.

**To barge into a contact**

- Click
  **Monitoring**.

You are now in barge mode.
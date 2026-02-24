# Monitoring calls with the live calls dashboard

Source: https://support.zendesk.com/hc/en-us/articles/4408885902490-Monitoring-calls-with-the-live-calls-dashboard

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Talk Professional or Enterprise |

Using the live calls dashboard, team managers can see at-a-glance all ongoing calls, listen in on agent conversations, and join calls when agents need support or escalation.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/live_dashboard.png)

This article contains the following topics:

- [Understanding live calls dashboard permissions](#topic_ecz_tx5_lcc)
- [Viewing the live calls dashboard and monitoring calls](#topic_ekm_45r_xjb)
- [Auditing call monitoring activity](#topic_l35_45r_xjb)

## Understanding live calls dashboard permissions

To give agents access to the live calls dashboard, you'll need to understand the following permissions:

### Who can view the live calls dashboard?

To access the live calls dashboard, an agent must have the following permissions:

- A user account of the type staff member
- A Talk role of admin or team lead

### Who can listen in on and join calls?

To listen in on calls, your agents must have the following permissions:

- A user account of the type staff member
- A Talk agent role of team lead (admins cannot listen in on calls)
- On Enteprise plans, an agent must be a member of a [custom role](https://support.zendesk.com/hc/en-us/articles/4408832292506) with the permission to manage channels and extensions. Users with only the view Zendesk Talk dashboard permission cannot monitor calls.

For more information about configuring permissions, see [Giving agents access to Talk](https://support.zendesk.com/hc/en-us/articles/4408882966170).

## Viewing the live calls dashboard and monitoring calls

The live calls dashboard contains the following information for each live call:

- The agent on the call
- The group the agent belongs to
- The call type (inbound or outbound)
- The caller number
- The ticket related to the call
- The call duration

Use the procedure below to learn how to open the live calls dashboard and monitor calls.

Note: When you monitor calls, ensure that your custom greetings provide adequate notice in accordance with your state or country's telephone recording laws.

**To view the live calls dashboard and monitor calls**

1. From any Zendesk product, open the product tray and click **Voice**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/product_tray_v2.png)
2. In the new tab that opens, click the live calls icon in the sidebar.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/live_calls_dashboard.png)

   The dashboard opens. You can filter the dashboard by agent or group name using the search field in the upper right.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_monitor_filter.png)
3. In addition to viewing live call information, the dashboard enables you to take the following actions:
   - **Listen into a call:** To monitor a call without notifying the agent or caller, click **Listen**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/callmonitoring_listen.png)

     Note: If a call shows a status of **IN MONITORING**, it means that another administrator is already listening to the call. Only one user can listen to a call at a time.
   - **Join an existing call (barge):** Click **Barge** to join the call. The agent and caller will both hear a beep notifying them a third party has joined.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/callmonitoring_barge.png)

     Click **End barge** to leave and return to listening in to the call.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/callmonitoring_endbarge.png)

     Note: Only one agent can barge into a call at a time.
     The original agent must remain on the call; if they disconnect, the call will end.
   - **Stop listening in:** Click **Leave call** to stop listening to the call.

Note: You can continue to listen to and barge into calls even if they have been transferred to an external number.

## Auditing call monitoring activity

You can export a comma-separated values (CSV) file containing an audit report of call monitoring activity.

**To the call monitoring activity report**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. Click the **Usage charges** tab.
3. Click the **Export CSV** button, then select Export Monitoring CSV.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_export_monitoring.png)

The report will be emailed to the address associated with your user account.
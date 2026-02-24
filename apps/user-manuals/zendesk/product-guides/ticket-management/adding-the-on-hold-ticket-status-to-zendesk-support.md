# Adding the On-hold ticket status to Zendesk Support

Source: https://support.zendesk.com/hc/en-us/articles/4408889282458-Adding-the-On-hold-ticket-status-to-Zendesk-Support

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > Objects and rules > Tickets > Fields

The On-hold status is optional and only available if you activate it for the Support ticket interface. On-hold is an internal ticket status for tickets that require input or resolution from a third party. On-hold status is visible to agents only, not end users. For end users, tickets that are set to On-hold are always displayed as Open.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/onhold_lotus.png)

On-hold gives you another level so that you can more accurately track who currently has responsibility for a ticket. For example, imagine that your company produces a product that includes components from partners and other suppliers. If you have tickets that require their input, and for which the assigned agent can do nothing but wait, setting the ticket to On-hold provides a way for distinguishing between tickets that are the responsibility of agents and those that are waiting for a third party.

If you track your agents' performance, using the On-hold status allows you to filter out all On-hold tickets from performance tracking. You can also use the On-hold status to create a workflow for tickets that require input or a resolution from a third party. On Support Professional and Enterprise you have an additional reporting metric called **On-hold time in hours**.

This article contains the following sections:

- [Activating and deactivating the On-hold status](#topic_kdz_5qn_b3)
- [Activating the On-hold status category for custom ticket statuses](#topic_zqr_jfz_kxb)
- [Using the On-hold status in views and SLAs](#topic_k1x_pb4_b3)
- [Using the On-hold status in your reports](#topic_xbh_gxn_b3)
- [How the On-hold status works with ticket sharing](#topic_3d3_yzn_b3)

## Activating and deactivating the On-hold status

Admins can add the On-hold status to the Support ticket interface. The On-hold status is deactivated by default.

**To activate or deactivate the On-hold status**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Tickets > Fields**.
2. Beside the **Status** field, click the options menu, then select **Edit**.

   Note: If custom ticket statuses were activated without the On-hold status having been activated previously, the Status field doesn't appear in the list. See [Activating the On-hold status category for custom ticket statuses](#topic_zqr_jfz_kxb).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/status_field_edit.png)
3. Under Field Values, select **Enable On-hold status**.

   If you are disabling this option, deselect **Enable On-hold status**.
4. Click **Update field**.

The On-hold status is added to the list of ticket statuses between Pending and Solved. On-hold status is visible to agents only, not end users. For end users, tickets that are set to On-hold are always displayed as Open in the Help Center customer portal.

**Community Tip!** Check out this tip to see how to [set reminders for On-hold tickets](https://support.zendesk.com/hc/en-us/articles/4910920686618-How-can-I-create-reminders-on-tickets-that-are-on-hold-).

## Activating the On-hold status category for custom ticket statuses

If you've [activated custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306) without the On-hold status having been activated previously, you can activate it from the Ticket statuses page.

**To activate or deactivate the On-hold status category**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Tickets > Ticket statuses**.
2. Click the **Options menu**(![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_menu_icon_verticle_sm.png)), then select **Status category settings**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cts_sort_statuses.png)
3. Select **Activate On-hold ticket status category**.

   If you are deactivating this option, deselect **Activate On-hold ticket status category**.
4. Click **Save**.

## Using the On-hold status in views and SLAs

You create new views, or edit existing views, to track tickets that are On-hold. You can select On-hold as the value of the **Status** condition and also use the **Hours since on hold** condition.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/onhold_view.png)

The On-hold status is added to the Status condition between Pending and Solved. This means that the condition statement **Status less than On-hold** will return tickets that are Pending, Open, or New and **Status greater than On-hold** will return tickets that are set to Solved or Closed.

The **Hours since on hold** condition allows you to specify the hours that have passed since the ticket's status was set to On-hold.

## Using the On-hold status in your reports

On Support Professional and Enterprise, you can use the On-hold status in a number of different ways using Explore:

- The metric **On-hold tickets** in the Tickets dataset displays the number of tickets that are currently on-hold.
- The metric **On-hold time** displays the total time (in minutes or hours) that a ticket was in the on-hold status.
- The metric **On-hold time - Business hours** displays the total time (in minutes or hours) that a ticket was in the on-hold status taking into account any business hour you've configured.

On-hold time is also included as a value in the **Ticket status** attribute. You can use the **Ticket status** attribute to break down a metric by each status. On the Zendesk Support pre-built Explore dashboard, Ticket status is used in a number of the reports on the **Unsolved tickets** tab.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/current_backlog_ticket_status_graph.png)

When you add the On-hold status, it will also affect the **Requester wait time in hours** and **Current backlog** metrics. The metrics will include the On-hold state in their calculations.

**Note:** The **Agent wait time in hours** metric is not affected by the On-hold status. This metric is still defined as the cumulative time a ticket has been in a Pending state (awaiting a response from the requester).

See [Metrics and attributes for Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408827693594).

## How the On-hold status works with ticket sharing

The On-hold status only affects ticket sharing agreements that use **Make public & private comments; sync status**. Because On-hold is an optional status in Zendesk Support, these ticket sharing agreements treat On-hold as Open.

For example, if a shared ticket is set to On-hold by the sending account, the ticket is displayed as Open in the receiving account. This occurs even if the receiving account has the On-hold status activated. All other statuses will sync normally.
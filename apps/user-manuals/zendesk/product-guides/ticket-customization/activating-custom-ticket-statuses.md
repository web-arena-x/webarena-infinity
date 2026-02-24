# Activating custom ticket statuses

Source: https://support.zendesk.com/hc/en-us/articles/4412575841306-Activating-custom-ticket-statuses

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center > Objects and rules > Tickets >
Ticket statuses

If your Zendesk account was created after Jan 17, 2023, then custom ticket statuses are activated by default and you can begin creating new ticket statuses right away.

Zendesk supports a set of standard ticket statuses that are used to help you manage your ticket workflows. Activate custom ticket statuses to create additional, more-specific ticket statuses.

Make sure you understand how activating custom ticket statuses affects other features in your account, such as your business rules and the agent experience.

This article includes these sections:

- [Activating and deactivating custom ticket statuses](#topic_g2k_t4g_vrb)
- [Understanding how custom ticket statuses impact your account](#topic_hmv_5kl_dwb)
- [Understanding how custom ticket statuses impact the agent experience](#topic_ip1_fll_dwb)

Related articles:

- [Creating custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575861018)
- [About form ticket statuses](https://support.zendesk.com/hc/en-us/articles/7755811560346)

## Activating and deactivating custom ticket statuses

You must be an admin to activate or deactivate custom ticket statuses.

**To activate custom ticket statuses**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Ticket statuses**.
2. Click **Custom ticket statuses** to expand it.
3. Select **Allow custom ticket statuses**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cst_enable2.png)

   You may want to review your triggers, automations, macros, and views based on standard ticket statuses and make sure you’re happy with how they were automatically updated.

   Note: When custom ticket statuses are activated, [keyboard shortcuts](https://support.zendesk.com/hc/en-us/articles/4408832849946) will not work when you are creating a new ticket. After a ticket is created, however, you can use keyboard shortcuts again.

   Now, you're ready to create custom ticket statuses (see [Creating custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575861018)).

**To deactivate custom ticket statuses**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Custom ticket statuses** to expand it.
3. Deselect **Allow custom ticket statuses**.
4. Click **Save**.
5. Review your triggers, automations, macros, and views based on ticket statuses.

   You may need to make some adjustments. For example, any instances of the Status category and Ticket status condition in your triggers will be automatically converted to the Status condition.

## Understanding how custom ticket statuses impact your account

Zendesk supports a set of standard ticket statuses which are used to help you manage your ticket workflows. These standard ticket statuses are used in your default triggers and other automations that are based on status changes in a ticket.

When you activate custom ticket statuses, the existing standard ticket statuses — New, Open, Pending, On-hold (if [activated](https://support.zendesk.com/hc/en-us/articles/4408889282458)), Solved, and Closed — become status categories.

A status category is a logical group of similar ticket statuses; it includes at least one default ticket status and can contain multiple ticket statuses.

Status categories, and the initial default ticket statuses inside of each status category, are named after the standard ticket statuses. The example below shows your initial default ticket statuses organized into their respective status categories:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cst_initial_defaults.png)

Note: If your account was created on or after February 13, 2024, an additional ticket status, **In Progress**, is included in the Open status category. This status is included as an example of a custom ticket status but it can still be applied to tickets, edited, or deactivated like other ticket statuses. See [Managing ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575941402).

Custom ticket statuses are created within these status categories. For example, you could create a custom ticket status in the Open category that describe why a ticket is open, such as Open - New customer or Open - Existing customer:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cst_open_customer_example.png)

You can [change the default ticket status of a status category,](managing-ticket-statuses.md#topic_zgh_dbh_vrb) if needed. Every ticket status, including both standard and custom ticket statuses, belongs to a status category. You can’t create or edit status categories, and you can’t move ticket statuses from one status category to another.

The status category you use to create a new ticket status controls the state of the ticket and is dependent on the [system ticket rules](https://support.zendesk.com/hc/en-us/articles/4408894213018).
All ticket statuses, including both standard and custom statuses, are dependent on these rules.

When you activate or deactivate custom ticket statuses, the status of your tickets are automatically updated based on status categories.
For example, if you created a custom ticket status called Open Investigating in the Open status category, assigned it to several tickets, but then deactivated custom ticket statuses, the status of all those tickets is changed to Open.

Finally, it’s important to note that [AI agent tickets](https://support.zendesk.com/hc/en-us/articles/9204149016346) can’t have custom ticket statuses.

### How custom ticket statuses impact existing business rules

When you activate custom ticket statuses, the ticket status conditions and actions in your existing triggers, automations, macros, and views are automatically updated from Ticket: Status to Ticket: Status Category. The Ticket:
Status Category condition and action uses the default ticket status of the status category, where applicable.

In the example below, the default automation "Close ticket 4 days after status is set to solved", contains the condition "Ticket: Hours since solved" and action "Ticket: Status Closed":

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cst_default_automation_before.png)

After you activate custom ticket statuses, the automation is updated to the condition "Ticket: Hours since status category solved" and action "Ticket: Status category closed":

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cst_default_automation_after.png)

It's recommended to review your existing triggers and other business rules after activating custom ticket statuses. Edit the "Ticket: Status Category" condition or action to "Ticket: Ticket status" as needed.

## Understanding how custom ticket statuses impact the agent experience

When you activate custom ticket statuses, you and your agents will see a variety of changes to other features, including:

- Selecting a status from the status picker in the ticket interface
- The appearance of ticket statuses in views
- Searching for tickets based on ticket statuses
- Tickets in the "Closed" state retain the solved status (see [About closed tickets solved with a custom ticket status](https://support.zendesk.com/hc/en-us/articles/8263915942938#topic_zlx_pyk_fdc))
- Tickets in the “Closed” state appear in search results if your search terms are included in their subject line or comments. See [Searching Zendesk Support data](https://support.zendesk.com/hc/en-us/articles/4408894221594#topic_xh1_kdy_wr).
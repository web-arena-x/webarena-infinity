# Creating custom ticket statuses

Source: https://support.zendesk.com/hc/en-us/articles/4412575861018-Creating-custom-ticket-statuses

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

Zendesk supports a set of [standard ticket statuses](https://support.zendesk.com/hc/en-us/articles/8263915942938#topic_lqf_myk_fdc) that are used to help you manage your ticket workflows. Admins can create custom ticket statuses to indicate a more meaningful ticket status to your business and end users.

You can use [custom ticket status attributes in your reporting](https://support.zendesk.com/hc/en-us/articles/4408827693594#topic_jnb_4hq_4y) and [associate specific statuses to your ticket forms](https://support.zendesk.com/hc/en-us/articles/7755811560346).

Note: If your account was created before Jan 17, 2023, you might need to [activate custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306).

This article includes these sections:

- [Creating a custom ticket status](#topic_jqm_g1h_vrb)
- [Configuration options for custom ticket statuses](#topic_otl_drg_vrb)

Related articles:

- [Viewing your ticket statuses](https://support.zendesk.com/hc/en-us/articles/4892092747162)
- [Managing ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575941402)

## Creating a custom ticket status

Admins can create custom ticket statuses.

If you've just activated custom ticket statuses, then you may need to refresh Admin Center to see the Ticket statuses page.

**To create a custom ticket status**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Ticket statuses**.
2. Click **Create ticket status**.
3. Configure **the basics** for your new status.

   For information about the options that appear on this page, see [Configuration options for ticket statuses](#topic_otl_drg_vrb).
4. Click **Next**.
5. Add the status to one or more ticket forms:
   - To add the status to all of your ticket forms, select **All forms**.
   - Choose one or more ticket forms from the **Select where to add this ticket status** drop-down.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cts_create_form_stepper.png)

   Learn more about [adding ticket statuses to your forms](https://support.zendesk.com/hc/en-us/articles/7755811560346).
6. Click **Create ticket status**.

   For information about making changes to a ticket status after you saved it, see [Editing ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575941402).

   After you create custom ticket statuses and begin using them, you can view reporting information in Explore. See [Metrics and attributes for Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408827693594#topic_jnb_4hq_4y). Also see [Explore recipe: Reporting on custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/6487691412762) and [Explore recipe: Creating KPIs for tickets by status](https://support.zendesk.com/hc/en-us/articles/4628409464474) to learn more about reporting for custom ticket statuses.

## Configuration options for custom ticket statuses

You can configure these options when you create or edit a ticket status:

| Options | Description |
| --- | --- |
| Category | Specifies which status category (New, Open, Pending, On hold, Solved) the ticket status is assigned to. You cannot assign a ticket status to the New or [Closed](https://support.zendesk.com/hc/en-us/articles/4408883475354) status categories. Category is editable only when you’re creating a new ticket status. Make sure you assign the new ticket status to the correct status category. Once you save your changes, you can’t move it to a different status category. Note: The **On hold** status category only appears if the [On-hold status](https://support.zendesk.com/hc/en-us/articles/4408889282458) is activated. |
| Name (agent view) | Specifies the name of the ticket status that agents see. There’s a 48 characters limit for ticket status names. Ticket status names that are 35 characters or longer are truncated. For example, on the **Submit** button, in the status picker, on ticket tabs, and in the **Status** column of a view. To translate the custom ticket status name to different languages, you can enter a [dynamic content placeholder](https://support.zendesk.com/hc/en-us/articles/4408882999066). For example, `{{dc.custom_ticket_status_pending_review}}`. |
| Description (agent view) | Description that agents see for the ticket status. |
| Show end users a different view | Select this option if you want end users to see a different name or description. Otherwise, agents and end users will see the same name and description. |
| Name (end user view) | Specifies the name of the ticket status that only end users see. Available only when **Show end users a different view** is selected. |
| Description (end user view) | Description of the ticket status name that end users see. Available only when **Show end users a different view** is selected. |
| Set as active | Activates the ticket status. See [Activating and deactivating a ticket status](https://support.zendesk.com/hc/en-us/articles/4412575941402#topic_qbl_32h_vrb). |
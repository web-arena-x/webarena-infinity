# About form ticket statuses

Source: https://support.zendesk.com/hc/en-us/articles/7755811560346-About-form-ticket-statuses

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

Location: Admin Center > Objects and rules > Tickets >
Ticket statuses

Zendesk offers a set of standard ticket statuses to help you manage your ticket workflows. When [custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306) are activated, you can create additional ticket statuses that are more meaningful to your business and end users.

With form ticket statuses, you can define which ticket statuses should appear in certain ticket forms. Associating ticket statuses to forms allows you to only show ticket statuses that are relevant to the ticket an agent is working on. This results in a shorter list of ticket statuses in the status picker for agents to choose from and can help them select the appropriate status more quickly.

This article includes the following sections:

- [Understanding form ticket statuses](#topic_vbd_gqx_vcc)
- [Associating ticket statuses to forms](#topic_erq_nqx_vcc)
- [Managing form ticket statuses](#topic_k54_ddy_vcc)

Related articles:

- [Activating custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306)
- [Creating multiple ticket forms](https://support.zendesk.com/hc/en-us/articles/4408846520858)

## Understanding form ticket statuses

Form ticket statuses are the standard and custom statuses you associate with your ticket forms.

Associating ticket statuses to forms allows you to only show ticket statuses that are relevant to the ticket an agent is working on. For example, say you have a ticket form for Customer Returns and an internal ticket form for Agent Onboarding. You can create custom ticket statuses that are relevant to each form, such as Refund issued or Training in process. By associating statuses to relevant forms, agents can quickly find the appropriate status.

### About the agent experience with form ticket statuses

Agents can select the appropriate status from the status picker in the Zendesk Agent Workspace. When agents switch the form applied to a ticket, the status picker updates the statuses associated with the form. Agents benefit from form ticket statuses because they can quickly find the status relevant to a ticket and don’t have to scroll through a long list of statuses.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/form_status_agent_interface.png)

## Associating ticket statuses to forms

Your default ticket statuses – initially, New, Open, Pending, On-hold (if activated), and Solved – are automatically associated with every form. If you’ve [changed your default ticket status names](https://support.zendesk.com/hc/en-us/articles/4412575941402#topic_zgh_dbh_vrb), then those statuses appear on your forms.

Define which custom ticket statuses should appear on ticket forms so that only relevant statuses are displayed. You can also associate ticket statuses to one or more forms when you [create a new ticket status](https://support.zendesk.com/hc/en-us/articles/4412575861018).

**To associate ticket statuses to a form**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Ticket statuses**.

   A list of your active ticket statuses appears on the All Ticket Statuses tab. If you haven’t created any custom ticket statuses yet, see [Creating custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575861018).

   Tip: To view your default statuses, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) at the top of the table and select **Default**.
2. Click the **Ticket statuses by form** tab.

   A list of your forms displays.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/form_ticket_status_tab.png)
3. Click the name of the form you want to associate ticket statuses with.
4. Click the arrow next to each status category and select the statuses you want to associate with the form.

   Note: Both active and inactive statuses appear. You can select only active statuses. See [Activating and deactivating a ticket status](https://support.zendesk.com/hc/en-us/articles/4412575941402#topic_qbl_32h_vrb).

   As you add statuses to the form, the status picker **Preview** updates.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/form_ticket_status_select.png)
5. Continue to add or remove statuses, then click **Save**.

   The number of statuses associated with the form update on the Ticket statuses by form tab and in the status picker in the agent interface.
   Learn more about [the agent experience with form ticket statuses](#topic_ysc_kqx_vcc).

## Managing form ticket statuses

On the Ticket statuses by form tab, you can [edit which ticket statuses appear on your forms](#topic_erq_nqx_vcc), view the number of standard and custom ticket statuses associated with each form, view which brands are assigned to the forms, search for forms, and filter forms by active status and brands.

### Searching and filtering forms

Search for and filter forms on the Ticket statuses by form tab to help quickly find the form whose statuses you want to manage.

**To search and filter your forms**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Ticket statuses**.
2. Click the **Ticket statuses by form** tab.
3. Take one of the following actions:
   - To search for a specific form, enter a term in the search box.
   - To filter forms by active status or brands, click **Filter**.

     Select **Active** or **Inactive** in the Form status menu, or click the **Forms associated with brands** menu and select the brands you want to filter by.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/from_ticket_status_filter_brand.png)

     See [Activating and deactivating ticket forms](https://support.zendesk.com/hc/en-us/articles/4408836460698) and [Assigning brands to a ticket form](../ticket-management/creating-and-applying-branded-ticket-forms.md#topic_nhh_gys_5wb) to make changes to your forms.

     Click **Apply filters**.
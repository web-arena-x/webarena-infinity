# Using ticket view in Salesforce

Source: https://support.zendesk.com/hc/en-us/articles/4408828317082-Using-ticket-view-in-Salesforce

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

The ticket view feature in the Zendesk for Salesforce integration queries Zendesk Support in real-time, and displays a list of tickets within your Salesforce Account, Contact, Lead, and Opportunity pages. It also enables users to view, create, and edit Support tickets. When using ticket view, Zendesk ticket data is not stored in Salesforce.

This article contains the following topics:

- [Limitations](#topic_gg2_3pw_rjb)
- [Viewing tickets in Salesforce](#topic_t1y_pzq_pjb)
- [Filtering and sorting tickets in ticket view](#topic_iw5_xzq_pjb)
- [Adding Zendesk credentials to create and edit tickets](#topic_nd4_c1r_pjb)
- [Creating and editing tickets in Salesforce](#topic_xkm_r1r_pjb)

Related articles:

- [Salesforce integration resources](https://support.zendesk.com/hc/en-us/articles/4408827957274)

## Limitations

The ticket view feature has the following limitations:

- Attachments and ticket macros are not supported
- Tickets with a requester who does not belong to an organization is only displayed on the Salesforce Contact page, if the email address of the Salesforce contact matches the Zendesk user
- When editing tickets, multi-select picklist fields are not shown or supported.
- Conditional fields aren't conditional within ticket view. Ticket view shows all fields within the selected ticket form.

## Viewing tickets in Salesforce

The ticket view feature in Salesforce shows Zendesk Support tickets. To use the ticket view, make sure you have set it up as described in [Setting up a Zendesk ticket view in Salesforce](https://support.zendesk.com/hc/en-us/articles/4408834115738). There are two interfaces when viewing tickets in Salesforce:

- **Ticket list view**: The ticket list view shows a lists all tickets for the Account, Contact, Opportunity, or Lead page.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Salesforce_ticket_view.png)
- **Detailed ticket view**: When you select a ticket, the detailed ticket view shows all the fields and comment history of the selected ticket. To edit a ticket, see [Creating and editing tickets in Salesforce](#topic_xkm_r1r_pjb).

## Filtering and sorting tickets in ticket view

The ticket view in Salesforce allows you to specify default settings for sorting and filtering of tickets. By default, all unclosed tickets are shown and sorted in descending priority.

The default filtering and sorting is set by clicking the **Filter List** icon in the upper right of the ticket view. You can select and deselect any values in the Priority, Status, and Type filter categories to filter tickets.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Salesforce_filter_tickets.png)

## Adding Zendesk credentials to create and edit tickets

To create or update tickets in Salesforce, a Salesforce user must be authenticated by adding their Zendesk agent account credentials to the ticket view personal settings. Light agents can also be linked.

Note: When linking to a Light Agent, the agent can edit all aspects of a ticket. However, once the ticket is submitted, an error is returned due to their restricted Support permissions.

**To add Zendesk credentials to personal settings**

1. In Salesforce, click on the app launcher icon in the upper left, and select an Account, Contacts, Leads, or Opportunities page.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Salesforce_pages.png)
2. Navigate to the ticket view in your Salesforce Account, Contacts, Leads, or Opportunities page.
3. Click the cog icon ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_cog.png) in the upper right of the ticket view to open **Personal settings**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Salesforce_link_agent_1.png)
4. Under **Zendesk Agent**, click **Link Zendesk Agent**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_link_agent_2.png)
5. Enter your Zendesk credentials and allowed permissions. If you are already logged in, you are automatically authenticated and redirected back to Salesforce. You can now create and edit tickets in ticket view.

## Creating and editing tickets in Salesforce

Tickets can be created and edited in ticket view within your Salesforce Accounts, Opportunities, Contacts, and Leads pages. You can also add internal and public comments to existing tickets. However, attachments cannot be added to tickets.

**To create a ticket**

1. In Salesforce, click on the App Launcher icon in the upper left, and select an Account, Contacts, Leads, or Opportunities page.
2. In your ticket view in your Salesforce page, click **New ticket**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Salesforce_create_ticket.png)
3. Enter details in the new ticket form. The fields are similar to the ticket interface in Zendesk Support:
   - **Requester**: The name of the person making the request. It is a contact in the Salesforce account.
   - **Assignee**: The user in Support who is assigned to resolve the ticket.
   - **Form**: The [ticket form](https://support.zendesk.com/hc/en-us/articles/4408846520858-Creating-ticket-forms-to-support-multiple-request-types-Professional-add-on-and-Enterprise-) to support the request type.
   - **Type**: The request type.
   - **Priority**: The priority to resolve the request.
   - **Subject**: The ticket subject
   - **Public reply / internal reply:** Customer or agent comments

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Salesforce_new_ticket_form.png)
4. Click **Submit as**. The ticket appears in your ticket view in Salesforce and in your ticket editor in Zendesk Support.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Salesforce_ticket_view_edit.png) 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Salesforce_zendesk_tickets.png)

Note: It can take up to a few minutes for created or updated tickets to be indexed and appear in your ticket view.

**To edit a ticket**

1. In Salesforce, click on the App Launcher icon in the upper left, and select an Account, Contacts, Leads, or Opportunities page.
2. In your ticket view, double click on the ticket. The ticket window opens.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Salesforce_ticket_view_edit.png)
3. Click the pencil icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_pencil_icon.png)) in the ticket fields to edit the ticket.
4. Click **Submit As** to save changes.

Next, you can continue with [Configuring data sync from Salesforce to Zendesk](https://support.zendesk.com/hc/en-us/articles/4408828539290--Configuring-data-sync-from-Salesforce-to-Zendesk).
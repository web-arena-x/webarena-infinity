# Working with the Zendesk Sell app in Support

Source: https://support.zendesk.com/hc/en-us/articles/4408831980314-Working-with-the-Zendesk-Sell-app-in-Support

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

You must have Sell and Support to use this integration.

If you have installed the Zendesk Sell app in Support, you can view the contact information for Zendesk Sell leads and contacts on tickets and end-user pages in Support (see [About integrating Sell and Support for an overview of customer communication in your company](https://support.zendesk.com/hc/en-us/articles/4408833438746)).

The Sell app in Zendesk Support provides greater visibility between the two systems and helps support agents understand more about the requester.

This article covers the following topics:

- [Viewing customer information](#topic_azx_nnm_wnb)
- [Notifying Sales about current Sell leads and contacts](#topic_myh_pnm_wnb)
- [Creating a lead in Sell from Zendesk Support](#topic_vsd_qnm_wnb)
- [Resolving common issues that occur when setting up the Sell app in Support](#topic_ms2_prv_w4b)

Related articles:

- [Setting up the Zendesk Sell-Support integration](https://support.zendesk.com/hc/en-us/articles/4408828146586)
- [Setting up the Zendesk Sell-Chat integration](https://support.zendesk.com/hc/en-us/articles/4408831757210)

## Viewing customer information

The Sell app in Zendesk Support allows your support agents to see specific Sell information related to a Support ticket requester. This gives your support agents useful context before they reach out to provide service for the customer. The app uses the requester's email address or phone number to pull in relevant information from Sell including:

- Information about the last point of contact
- Links to their website or X (formerly Twitter), Facebook, or LinkedIn pages
- Sell owner
- Type of record in Sell (e.g. Lead or Contact - for both the person and the company)
- Status of the record (if applicable)
- Related deals (if applicable)
- Email
- Phone numbers (work and mobile)
- Address
- Description of the Sell lead or contact
- Custom fields values

You can also configure what type of information will be displayed in the Sell app in Support, and in what order that information is displayed (see [Customizing the data fields displayed by the Zendesk Sell for Support app](https://support.zendesk.com/hc/en-us/articles/4408821766938)).

Note: To find a matching object in Sell, the Sell app searches through the first 50 email addresses and phone numbers of the requester.

## Notifying Sales about current Sell leads and contacts

Click **Send note to sales** in the Zendesk Sell app for Support to notify the sales team about existing leads or contacts that have been contacting Support. This will add a note to the lead or contact in Sell. The note is then sent to Sell and the lead or contact owner will receive a notification.

![Sell-Support send note to sales support](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_support_send_note_to_sales_support.png)

## Creating a lead in Sell from Zendesk Support

If want to connect a requester from an incoming ticket with someone from your sales team, you can create a lead in Sell.

1. In the Zendesk Sell app in Zendesk Support, click **Create lead**.

   This option only becomes available if no lead or contact is found in Sell.

   ![Sell-Support create lead](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_create_lead_support.png)
2. (Optional) Add a note and click **Create**.

   The lead with the requester name is created in Sell. The requester's email address, phone number, X (formerly Twitter), Facebook and organization name are added to the lead's contact information in Sell.

The lead status, owner, and source are set according to how it is [set up in the Zendesk Sell-Support integration](https://support.zendesk.com/hc/en-us/articles/4408828146586). Depending on your combination of settings, during the lead creation process, an agent may be asked to choose a distribution or specify a sales rep that the lead will be assigned to.

![Sell-Support Assign to field](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_support_assign_suggested.png)

The note is supplemented with the name of the agent who created the lead, and a link to the ticket that will appear in the new lead's Activity Feed in Sell. The Support ticket is also updated with a comment that the lead was passed on to Sell.

![Sell leads and open tickets](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_support_app_leads_and_open_tickets.png)

## Resolving common issues that occur when setting up the Sell app in Support

If an agent cannot see the lead or contact data in the Sell app, or they cannot create leads, then it means the Sell administrator has not configured the app to allow these actions. To allow agents to see the information in the Sell app, a Zendesk Sell administrator must grant them access (see [Setting up your Zendesk Sell-Support integration](https://support.zendesk.com/hc/en-us/articles/4408828146586)).

![Zendesk Sell app in Support](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_zendesk_sell_app_in_support.png)
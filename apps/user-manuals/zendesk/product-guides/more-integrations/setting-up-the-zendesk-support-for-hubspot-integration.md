# Setting up the Zendesk Support for HubSpot integration

Source: https://support.zendesk.com/hc/en-us/articles/4408884090650-Setting-up-the-Zendesk-Support-for-HubSpot-integration

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

The HubSpot integration allows HubSpot users to receive Zendesk ticket events and chat transcripts in the HubSpot's contact timeline.

This integration is available to all HubSpot subscriptions.

This article covers the following topics:

- [Functionality overview](#zd_hs_fo)
- [Installing and configuring the integration](#h_186fe4c5-2bb3-4f8a-92a1-607df6659a3d)
- [Deleting the integration](#topic_delete)
- [Frequently asked questions](#faq)

## Functionality overview

The Zendesk for HubSpot integration enables you to view Zendesk ticket information in the timeline section of a customer's profile page in HubSpot.

Three types of tickets that can be displayed are:

- New tickets created
- Solved tickets
- Solved tickets with CSAT rating

The following ticket information that can be displayed include:

- Title and ticket status
- The whole ticket conversation
- Link to the ticket to Zendesk
- CSAT (Only for solved tickets with CSAT rating)
- Group and Assignee that responded to the ticket
- Tags that have been assigned to the ticket

## Installing and configuring the integration

1. Visit <https://hubspot.zendesk-integrations.com/zendesk>.
2. Enter your Zendesk subdomain. For example,  *z3nianhelp*.
3. Authorize the Zendesk app.
4. Allow access to the HubSpot app.
5. Authorize Zendesk to use your data.
6. Go to your HubSpot account and click **Contacts**.
7. Click any contact, then select the **Activities** tab.
8. Click **Filter activity**.
9. Select the Integrations > Zendesk checkbox. 

   ![Screenshot_1_-_Example_of_filtering_for_Zendesk_activities.jpg](https://support.zendesk.com/hc/article_attachments/7856558174106)

Three triggers and one webhook are automatically created after connecting your Zendesk account to HubSpot. These ensure that the tickets are sent to your HubSpot when they are created, solved, or rated.

The following triggers are set up:

- [Hubspot Integration] - Ticket Created
- [Hubspot Integration] - Ticket Solved
- [Hubspot Integration] - Ticket CSAT Rating Submitted

The webhook is:

- HubSpot Integration

You can disable the triggers if you’d like to turn off the integration.

**Important**: Do not test the HubSpot webhook created by the integration in Admin Center, as this will trigger an API call with an invalid JSON and disconnect the integration. Test the integration instead.

**Note**: If your tickets from HubSpot submissions are automatically becoming suspended tickets, see [Tickets created from my custom ticket form are being suspended](https://support.zendesk.com/hc/en-us/articles/4408881830298).

## Deleting the integration

Go to <https://hubspot.zendesk-integrations.com/account>, enter your Zendesk subdomain and click delete.

See [this HubSpot knowledge base article](https://protect-us.mimecast.com/s/_ymqCo2AAGCX20205c23-5k?domain=knowledge.hubspot.com) for the steps to delete the Zendesk app from your Hubspot account.

## Frequently asked questions

### Can I sync Support tickets to the Company timeline or the Deal view?

Currently, you can only display tickets in the contact timeline.

### I can’t set up the integration. I am redirected to an “Application Error” page.

Contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) if you are getting this error. This error happens sporadically and we can get it back up within 24 hours.

### I can’t see the tickets events in my HubSpot account.

Confirm that you reach the setup complete page for Zendesk.

Make sure you are using the latest version of HubSpot CRM. Consult with a HubSpot specialist in case you need help upgrading to the latest version.

Make sure that the Zendesk checkbox is ticked in the “Filter timeline…” drop down list.

### I want to filter out tickets that will go to my HubSpot account.

Go to your Zendesk triggers and find the three triggers created, as described above. These triggers are responsible for sending ticket events to HubSpot. You can edit the conditions of the triggers to filter in/out tickets going to your HubSpot account. The actual JSON payload (ticket information) cannot be modified.

### I only see the group and assignee in Solved ticket events in HubSpot

The initial version of the integration doesn’t display ticket information for solved tickets. In the meantime, click on the ticket link to view the ticket information inside Zendesk.

### I would like to set up the integration for Zendesk Chat

You can add the Chat widget to your Hubspot pages so your customers can chat to your agents. This requires adding the widget script into your HTML source pages. For more information, see [Adding the Chat widget to your website](https://support.zendesk.com/hc/en-us/articles/4408881932698).

### I want to modify the ticket information that appears in HubSpot

You can't customize the ticket information that appears in HubSpot.

### I want to have my contacts in HubSpot appear in Zendesk

The Zendesk Support for HubSpot integration is one-way with information flowing from Zendesk to HubSpot. In order to create the users from HubSpot in Zendesk, you'll need to use the Support API.  For more information, see the [Support API documentation](https://developer.zendesk.com/api-reference/ticketing/introduction/).

### How are users created in HubSpot?

At this time, only the user's email address is synced from Zendesk. First and last name are not synced.
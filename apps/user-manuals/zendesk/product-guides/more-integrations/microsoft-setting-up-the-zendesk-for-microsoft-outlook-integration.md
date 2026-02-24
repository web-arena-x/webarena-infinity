# Microsoft: Setting up the Zendesk for Microsoft Outlook Integration 

Source: https://support.zendesk.com/hc/en-us/articles/4408886020634-Microsoft-Setting-up-the-Zendesk-for-Microsoft-Outlook-Integration

---

The Outlook integration allows Outlook users with or without a Zendesk account to copy email contents to a new ticket in Zendesk without leaving the Outlook application.

This article covers the following topics:

- [Requirements for setting up the integration](#topic_req)
- [Installing and configuring the integration](#topic_install)
- [Deleting the integration](#topic_delete)
- [Frequently asked questions](#topic_faq)

## Requirements for setting up the integration

The integration setup should be done in the Exchange Center admin by the administrator of your Microsoft organization to ensure that any tickets created are sent to the correct Zendesk subdomain for your organization. Additionally, to set up the integration, you must:

- Have Microsoft 365
- Have permissions to install Outlook add-ins
- Be a Zendesk administrator
- \*If you are using an on-premise exchange server, please consult with Microsoft support to configure the server to ensure that the add-in will work

## Installing and configuring the integration

Before you can use the Outlook integration, you must perform the following tasks:

- Install the Zendesk add-in to Outlook
- Configure the Zendesk add-in
- Set up the integration

**To install the Zendesk add-in**

1. Open Outlook, then click **Add apps** in the app finder. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/outlook_integration_add_apps.png)
2. Type **Zendesk** to search for the **Zendesk Support for Outlook** app.
3. Click the app name, then click **Add**. The app is now added to your account.

**To configure the Zendesk add-in**

1. In Outlook, click the **View** menu, then select **View settings** > **Email** > **Customize actions**.
2. Select the **Zendesk Support** check box. The Zendesk Support icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/outlook_integration_icon.png)) is added to the email toolbar.
3. Select an email to open it, then click the Zendesk Support icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/outlook_integration_icon.png)) in the toolbar.
4. In the Zendesk Support side panel that appears, create a ticket by selecting the **Type**, **Priority**, **Status** and then clicking **Create ticket**.

You should see an error message with a link to set up the integration.

**To set up the integration**

1. In the error message described above, click the **Set up now** link. You are redirected to the integration setup page.
2. Enter your Zendesk subdomain, click the check box to agree to the terms and conditions, then click **Authorize**.
3. Complete the setup and return to Outlook.
4. Close the add-in and reopen it again.
5. Complete the ticket information in the right pane, then click **Create ticket**.   
   You receive a confirmation message that the ticket was successfully created in Zendesk.

## Deleting the integration

Go to <https://integrations.zendesk.com/integrations/outlook/uninstall>, enter your Zendesk subdomain, and click delete.

## Frequently Asked Questions

### I successfully completed the integration setup, but it still shows "Set Up Now" in the add-in window.

Close the add-in window by clicking on the add-in and reopen it by clicking it again. This will refresh the add-in and enable you to create a ticket successfully.

### The add-in is integrated with the wrong Zendesk subdomain. How can I change it?

Go to <https://integrations.zendesk.com/integrations/outlook/uninstall>, enter your Zendesk subdomain, and click delete. Once deleted, you can set up the integration again with the new subdomain.

### When I click "View in Zendesk" I’m asked to log in, but I don’t have credentials. How can I view the ticket in Zendesk?

Only employees in your organization with a Zendesk account can view tickets inside Zendesk. Request a Zendesk account from your organization’s Zendesk admin to view the ticket inside Zendesk.

### Why aren't images from my email visible in the Zendesk ticket?

This integration copies body text from your email message into the Zendesk ticket. Inline images do not copy over. However, if you have images attached to your email, they are copied as attachments to the Zendesk ticket.

### How many Zendesk accounts can be connected to Outlook?

There is a 1:1 limitation for this integration.

### If I have CCs on my email in Outlook, are they added to the Zendesk ticket?

CCs are not supported. The integration does not add CCs from the Outlook email to the Zendesk ticket.

### Can I change the ticket fields that appear in the Zendesk add-in?

You cannot change or add ticket fields to the Zendesk add-in.

### Can I integrate my Zendesk Sell contacts with Microsoft Exchange?

No, contacts do not sync between Zendesk Sell and Microsoft Exchange. We recommend using external software such as Zapier to integrate Sell and Office 365. To learn more about Zapier, see [Using Zapier with Sell](https://support.zendesk.com/hc/en-us/articles/4408837805210).
# Installing and using the Clone Ticket app

Source: https://support.zendesk.com/hc/en-us/articles/4408881594010-Installing-and-using-the-Clone-Ticket-app

---

The [Clone Ticket app](https://www.zendesk.com/apps/support/clone-ticket/) integrates with Zendesk Support and enables agents to clone a ticket multiple times in batches. You can select a specific ticket and clone as many copies as set by an administrator.

The app maintains all ticket metadata and allows the configuration of tickets after they are cloned. The cloned tickets contain the source ticket information such as contact details, status, type, and the initial question or comment. An internal comment is added showing the date, time, and source ticket number.

![](https://support.zendesk.com/hc/article_attachments/7856386153882)

This article includes the following topics:

- [Limitations](#h_01JMFJZV3SA06D9ZJWCREJSX7H)
- [Installing the app](#h_cc5354a3-b593-4464-b380-5ce8c556dbd7)
- [Using the app](#h_a01f8f7d-066b-43df-b557-1eed7dcc5598)

## Limitations

- Cloned messaging tickets aren't linked to an active conversation. Therefore, you can't respond to the requester of the cloned ticket or end the messaging session from the cloned ticket. [Switch to a different channel](../../agent-guide/ticket-basics/composing-messages-in-the-zendesk-agent-workspace.md#topic_gtw_j1h_rmb) to contact the requester.

## Installing the app

The app is installed from the Zendesk Marketplace.

**To install the app**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Apps and integrations** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)) in the sidebar, then select **Apps > Zendesk Support apps**.
2. Click **Marketplace** at the top of the page and then enter "Clone ticket" in the Marketplace search bar.
3. Double-click the **Clone Ticket** app icon, then click **Install**.
4. Select the account to install the app, then click **Install**.
5. In the **Installation** section, enter a name for the Clone Ticket app.
6. In the **Creation Limit** setting, set the max number of tickets that can be cloned at one time. This cannot be set to zero.
7. In **Tags for cloned tickets**, add any tags that you would like to apply to cloned tickets.
8. You can select **Allow agents to automatically open cloned tickets**, and the cloned tickets can be opened immediately.
9. Enable group and role restrictions if required.
10. Click **Install**.

## Using the app

When a ticket is opened, the app is available to clone the ticket in the ticket sidebar.

Note: If you clone a closed ticket, an error message displays, but tickets are created with a closed status.

**To clone the ticket**

1. Display the Clone Ticket app on the ticket page by clicking the **Apps** button on the upper-right side of the page.
2. In the Clone Ticket app, click **Create clones of this ticket.**![](https://support.zendesk.com/hc/article_attachments/7856386152218)
3. Enter the number of times to clone a ticket and click **Create.** You can choose whether to open the tickets automatically after creation.![](https://support.zendesk.com/hc/article_attachments/7856363717402)
4. Re-enter the number of times to clone a ticket as confirmation, and click **Confirm.**![](https://support.zendesk.com/hc/article_attachments/7856386152474)  
   A confirmation message displays the number of cloned tickets created.![](https://support.zendesk.com/hc/article_attachments/7856386153242)
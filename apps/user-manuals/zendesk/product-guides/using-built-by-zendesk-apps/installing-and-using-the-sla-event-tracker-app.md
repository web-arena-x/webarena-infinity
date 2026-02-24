# Installing and using the SLA Event Tracker app

Source: https://support.zendesk.com/hc/en-us/articles/4409148550554-Installing-and-using-the-SLA-Event-Tracker-app

---

The [SLA Event Tracker App](https://www.zendesk.com/apps/support/sla-event-tracker/) provides a quick and easy interface that displays Service Level Agreement (SLA) data about the ticket in Zendesk Support. The app provides an agent with a quick view of a ticket's progress against any applicable SLAs. This allows users to see when SLA metrics have been applied, fulfilled, or breached.

This article contains the following topics:

- [Installation](#h_cc5354a3-b593-4464-b380-5ce8c556dbd7)
- [Using the App](#h_a01f8f7d-066b-43df-b557-1eed7dcc5598)

## Installation

1. Go to the [SLA Event Tracker](https://www.zendesk.com/marketplace/apps/support/223192/sla-event-tracker/) page on the Zendesk Marketplace.
2. Click **Install**.
3. Select the account to install the app, then click **Install**.
4. In the Installation section, enter a name for the SLA Event Tracker app, and enable group and role restrictions if required.   
   These configuration options are also available after installation by navigating to Admin Center > Apps and integrations > Zendesk Support apps and clicking on the app.
5. Click **Install.**

## Using the app

After opening a ticket that has an SLA applied, you will see information similar to the following in the ticket app sidebar, as it applies to the SLA for your specific ticket:

![](https://support.zendesk.com/hc/article_attachments/4409149684890)

The app displays a future breach date if the target is active and hasn't yet breached. If the target is fulfilled before the breach date, the breach date is removed, the status changes to **fulfilled**, and the metric breach displays **no current breach** in green.

If the ticket doesn't have a SLA assigned, then you will see the following notification:

![](https://support.zendesk.com/hc/article_attachments/4409156646298)

The app also include links to common questions and instructions on how SLAs work in Zendesk Support. The **About SLA** and **Troubleshoot** buttons take you to helpful articles within our knowledge base, and the **Glossary** button shows you the various terms associated with SLAs and their definitions.
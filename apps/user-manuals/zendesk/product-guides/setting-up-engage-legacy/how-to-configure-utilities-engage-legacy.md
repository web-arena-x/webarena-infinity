# How to Configure Utilities (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731466438938-How-to-Configure-Utilities-Engage-Legacy

---

## Create a Utility

1. Navigate to the **Settings** menu and select the **Utilities** tab
2. To create a new Utility click the **New Utility** button
3. Choose the relevant **Utility Type**
4. Complete the **New Utility** form
5. Click on the **Save Utility** button

### Ensuring your iFrame Embed is functional

When configuring an iFrame Embed Utility, it is important to use the Preview functionality to determine whether or not the Utility will work for your Agents.

Ensure the 3rd party application is iFrame-able. Not all websites allow the use of iFrames.

The preview section at the bottom of the page will help you to determine whether or not your configuration is functional.

As an example, a non-functional iFrame Embed Utility will appear as below:

![](https://support.zendesk.com/hc/article_attachments/9731449953050)

### Personalization Tokens

To access various pieces of information about the current contact within a Utility, you can utilize Engage Personalization Tokens in the IFrame Url.

As an example, if you are embedding a delivery tracking application, you can include the order ID Personalization Token within the iFrame URL to take the Agent straight to the specified order. The Order ID may be based on data collected in the Contact Flow or in the Customer Profile.

The iframe url would look something like this: **https://mytrackingapp.com/{{contact.order\_id}}** or **https://mytrackingapp.com?orderId={{contact.order\_id}}**

## Add a Utility to a Workflow

After creating a Utility, Admins can integrate it into specific workflows. Utilities can be added to existing workflows or new custom workflows created. Multiple Utilities can be added to a workflow, and they will appear as a dropdown list if there are too many to display.

To limit a Utility to a specific queue(s), you will need to configure it in a Custom Workflow

1. Within the **Settings** menu, navigate to the **Workflows** tab
2. Select an existing workflow to edit, or create a new custom workflow
3. Scroll down to **Interface Settings** section
4. Select where you would like the Utility tab to appear in a contact, *Main Panel* or *Side Panel*
5. Click on the **Add new** button
6. Select the desired Utility from the drop-down list of Utilities you have created
7. Select the visibility, i.e. choose when the Utility tab should appear for Agents. The options are *During an active call/chat* and *During ACW,* both can be selected.
8. Click on the **Save** button

‍

‍
# Why didn't I receive an email notification from a submittal? - Procore

Source: https://support.procore.com/faq/why-didnt-i-receive-an-email-notification-from-a-submittal

---

## Background

Procore lets admin users configure notification preferences for the Submittals tool in many different ways. If these settings are not set properly or are changed without notice, users may find themselves looking for an email that was never delivered. This article will help you determine the cause of the missing notification.

## Answer

If a submittal notification is not delivered, one of the following scenarios may have occurred.

- **Create & Send Emails was not clicked when creating the submittal.**
 - When a submittal is created, if 'Create' is clicked instead of 'Create & Send Emails', email notifications will NOT be sent to workflow members or other users on the submittal.  
    ![create-and-send-submittals.png](https://support.procore.com/@api/deki/files/321689/create-and-send-submittals.png?revision=1)
 - If the 'Create' button is used when creating a submittal instead of the 'Create & Send Emails', the 'Send Date' field in the submittal's workflow will appear blank.
- **The email notification matrix in the Submittals configure settings was set incorrectly *before*the email triggering event took place.**
 - This is a leading cause of missed email notifications. For example, users in a submittal's distribution group will not receive an email if the 'Distribution Group' box is not selected in the notifications matrix for the specific event that triggered the notification. In this example, being in the distribution group does not always guarantee an email notification. See [Who receives an email when a submittal is created or updated?](https://support.procore.com/faq/who-receives-an-email-when-a-submittal-is-created-or-updated "Who receives an email when a submittal is created or updated?")
 - Changing the email matrix settings *after*the missed notification will NOT cause emails to be sent retroactively. This means that if you update the settings to include a certain role in the notifications for a triggering event after that event has taken place, no emails will be delivered. See [Configure Settings: Submittals Tool](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/configure-settings-submittals-tool "Configure Settings: Submittals Tool").
- **The email was sent from Procore but was never delivered to the recipient.**
 - Admin users can leverage the **Outbound Emails Report**in the project's Reports tool to determine if a submittal notification was sent from the project. If the email does not appear in the report, it is likely that the project was not set to send the particular email at the time of the triggering event.
 - If the email appears in the Outbound Emails Report and was also not delivered to its recipient, contact Procore Customer Support.
- **The notification preferences in your Directory entry are set to 'Not at All'.**
 - A Directory tool admin will need to check if this setting is configured properly.
 - This setting is often toggled to 'Not at All' when users go on vacation or are out of the office for an extended period of time. Turning it back to 'via Email' can easily be forgotten when the user returns.

## See Also

- [Who receives an email when a submittal is created or updated?](https://support.procore.com/faq/who-receives-an-email-when-a-submittal-is-created-or-updated "Who receives an email when a submittal is created or updated?")
- [Configure Settings: Submittals Tool](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/configure-settings-submittals-tool "Configure Settings: Submittals Tool")
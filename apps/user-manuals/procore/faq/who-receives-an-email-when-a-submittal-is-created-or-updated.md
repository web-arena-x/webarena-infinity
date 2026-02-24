# Who receives an email when a submittal is created or updated? - Procore

Source: https://support.procore.com/faq/who-receives-an-email-when-a-submittal-is-created-or-updated

---

## Answer

Users in the first step of a submittal's workflow will receive 'Action Required' emails from Procore if **Create & Send Emails** is clicked when the submittal is created. If the Submittal is created *without*using the **Create & Send Emails**button, emails will not be delivered according to the email configuration settings.

When the users in each step of a submittal's workflow have completed their required action (or if **Update & Send Emails** is clicked if the submittal is updated), users in the next step of the workflow will receive 'Action Required' emails.

In Procore, 'Action Required' emails cannot be turned ON or OFF (see [Why can't I turn OFF the 'Action Required' emails sent from the Submittals tool?](https://support.procore.com/faq/why-cant-i-turn-off-the-action-required-emails-from-the-submittals-tool "Why can't I turn OFF the 'Action Required' emails sent from the Submittals tool?")).  However, users with 'Admin' level permission can configure settings for other email notifications on the Project level Submittals tool.

### Default Email Settings

The illustration below shows the default email settings for submittal items in Submittals tool. A user with 'Admin' level permissions on the project's Submittals tool can change these settings. See [Configure Settings: Submittals Tool](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/configure-settings-submittals-tool "Configure Settings: Submittals Tool").

*Note:* These email settings do not apply when sending and resending submittals in submittal packages. See [Emails for Submittal Packages](#Emails_for_Submittal_Packages "Who receives an email when a submittal is created or updated?") below. 
 
![submittals-submittal-emails.png](https://support.procore.com/@api/deki/files/142060/submittals-submittal-emails.png?revision=1) 
 
To learn more about the different roles in the columns of the 'Submittal Emails' table, see the following articles:

- [What is the 'Submittal Manager' role?](https://support.procore.com/faq/what-is-the-submittal-manager-role "What is the 'Submittal Manager' role?")
- [Add a Submitter and Approvers to the Submittal Workflow](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/add-submitter-and-approvers-to-the-submittal-workflow "Add a Submitter and Approvers to the Submittal Workflow")
- [Forward a Submittal for Review](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/forward-a-submittal-for-review "Forward a Submittal for Review")
- [What is the difference between a distribution group and distribution list in Procore?](https://support.procore.com/faq/what-is-the-difference-between-a-distribution-group-and-a-distribution-list "What is the difference between a distribution group and distribution list in Procore?")

### Emails for Submittal Packages

Emails sent when users send or resend submittals in submittal packages for review do not follow the default email settings for individual submittal items.

When users send or resend submittals in submittal packages for review, the system sends emails with the following subject lines:

- 'Action Required For Submittals in Package'. This email is sent to members of the first step of the submittal workflow to alert the Ball in Court person that a response is required.
- 'Submittals Sent For Review in Package'. This email is sent to each submittal's manager and distribution list members.

## See Also

- [Configure Advanced Settings: Submittals](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/configure-settings-submittals-tool "Configure Advanced Settings: Submittals Tool")
- [Why can't I turn OFF the 'Action Required' emails sent from the Submittals tool?](https://support.procore.com/faq/why-cant-i-turn-off-the-action-required-emails-from-the-submittals-tool "Why can't I turn OFF the 'Action Required' emails sent from the Submittals tool?")

## 

If you would like to learn more about Procore's submittals management software and how it can help your business, please visit our [construction submittals software product page ![icon-external-link.png](https://support.procore.com/@api/deki/files/186764/icon-external-link.png?revision=2&size=bestfit&width=14&height=14)](https://www.procore.com/project-management/submittals "https://www.procore.com/project-management/submittals").
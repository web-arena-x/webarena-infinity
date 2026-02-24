# Outbound Email Setup (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731475290394-Outbound-Email-Setup-Engage-Legacy

---

Outbound email for Engage has been specifically designed to address the needs of agents when communicating with customers outside of current contacts. This includes the ability to add attachments, use snippets, reply to existing threads, manage customer profiles more efficiently, and use generative AI via Engage’s Smart Tools, to assist our customer service personnel in writing outgoing emails more effectively.

Local Measure Engage provides full outbound email capabilities to proactively engage with customers over email.

##### **Key** **Benefits Include**:

- Ability for agents to start new email contacts with an easy-to-use interface.
- Standardised approach by using Utilities.
- Attachments and snippets support for outbound emails.
- Capability to reply to existing threads, maintaining context for the customer.
- Integration of customer profile lookup or creation during the email composition process.
- Ability to send from multiple mailboxes.
- It enables the configuration of friendly reply addresses.
- Users have the ability to establish a predefined signature for each Utility, which will take precedence over the signature used in the Workflow.
- Give customer support representatives access to generative AI's email composition capabilities by using Engage’s Smart Tools.

##### Prerequisites

- Amazon Simple Email Services (SES) being configured correctly
- New Slate email editor

Please be aware that access to this feature requires the use of the new email UI. If you have any questions or need clarification, please contact your Key Accounts Manager.

### Implementation Steps

Setting up the outbound email functionality follows the same basic configuration as creating any Utility type in Engage. Outbound emails are triggered via a Utility, therefore making it easy to use as all agents are currently using Utilities for various tasks.   
‍The steps to configure and outbound email utility type is as follows:

1. Navigate to the Setting page by clicking on the setting icon.
2. Select the “Utilities” tab from the top menu.
3. Click “New Utility”.
4. Select the "Outbound Email" utility type.
5. Capture the relevant fields and click the “Create Utility” button. To ensure the Outbound Email Utility is save correctly, navigate to Utilities listing page and scroll for the Utility name you just created.
6. To include multiple email boxes, input each individual email address separated by a comma (comma-separated) or by inserting a space and pressing the enter key.
7. In order to create a outbound email default signature which can be linked to one or multiple FROM email addresses, users can define custom token fields for the "FROM address," enabling the email sender's address to be dynamically populated. The custom token field is {{Utility.FromEmail}}. 
   The outbound email default signature is set in the Utility and will overwrite the default workflow signature.
8. Click on "Workflows" to add the new "Outbound Email" utility to the agent workflow.
9. Click the “Edit workflow” button to add the new outbound email utility to the panel of your choosing.

Hint, add it to the center and right panel to ensure it works for both.

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731499447066)

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731462866074)

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731499501210)

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731462964378)

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731466838298)

‍
# Configure Advanced Settings: T&M Tickets

Source: https://v2.support.procore.com/product-manuals/tm-tickets-project/tutorials/configure-advanced-settings-tm-tickets

---

## Background

Before your team starts using the T&M Tickets tool, you'll want to configure the tool's advanced settings. You can add one or more Procore users to the tool's default distribution list. You can also specify which user(s) or groups receive automatic email notifications from Procore when specific actions are completed in the tool.

## Things to Consider

- [Required User Permissions](/product-manuals/tm-tickets-project/permissions)

## Prerequisites

- Add the T&M Tickets tool to Project Tools. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).
- For a Procore user to appear as a selection in the Default Distribution group's 'Select a Person' drop-down list, complete the steps in [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory) or [Bulk Add Users and Companies to a Project Directory](/product-manuals/directory-project/tutorials/bulk-add-users-and-companies-to-a-project-directory).

## Steps

- Configure T&M Settings

  - Create a Default Distribution Group
  - Configure T&M Emails
- Configure the Change Events Export Options

### Configure the T&M Settings

Using the controls in the T&M Settings tab, you can create a default distribution group and configure emails for the T&M Tickets tool.

#### Create a Default Distribution Group

To create an email distribution group for the T&M Tickets tool, follow these steps:

1. Navigate to the **T&M Tickets** tool.
2. Click the **Configure Settings**  icon.
3. Under the **T&M Settings** tab, scroll to the **Default Distribution** section.
4. Select one or more project users from the **Select a Person** drop-down list.

   ##### Â Notes

   - For a Procore user to appear as a selection in the 'Select a Person' drop-down list, a user with the appropriate permissions must complete the steps in [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory) or [Bulk Add Users and Companies to a Project Directory](/product-manuals/directory-project/tutorials/bulk-add-users-and-companies-to-a-project-directory).

- Continue with Configure T&M Emails.

#### Configure T&M Emails

To choose the actions that will send emails to distribution group members, follow these steps:

1. Under the **T&M Settings** tab, scroll to the **T&M Emails** section.
2. Mark one or more role checkboxes to specify which notifications to send to users and distribution group members upon completion of each action in the list:  
   *Note*: You can click the 'Reset to default' link to enable notifications for all actions.

   - **Actions**:

     - **T&M Ticket Created**. Procore sends an email notification when a new T&M Ticket is added or created. Updates to existing tickets will not trigger an email notification. See [Create a T&M Ticket](/process-guides/project-equipment-user-guide/create-a-tm-ticket-web).
     - **Signed by Company:** Procore sends an email notification when a company signee submits a signature. See [Sign a T&M Ticket](/product-manuals/tm-tickets-project/tutorials/sign-a-tm-ticket).
     - **T&M Ticket Signed By Customer**. Procore sends an email notification when a customer signee submits their signature. See [Sign a T&M Ticket](/product-manuals/tm-tickets-project/tutorials/sign-a-tm-ticket).
     - **Closed:** Procore sends an email notification when a T&M ticket has been closed.   
       *Note*: When a customer signee submits a signature, Procore always sends the customer signee a copy of their signed ticket for their records. This email cannot be turned OFF using the 'T&M Ticket Signed by Customer Setting' check box.
   - **Recipients**:

     - **Creator**. Sends an email notification to the Procore user who created the T&M ticket.
     - **Company Signee**. Sends an email notification to the email address associated with the user designated as the Company Signee on the ticket..
     - **Custom Signee**. Sends an email notification to the email address associated with the user designated as the Company Signee on the ticket.
     - **Distribution Group**. Sends a notification to all of the Procore users who have been added to the 'Default Distribution' group.
   - **Status**:

     - **In Progress**: Indicates a new T&M Ticket has been created.
     - **Ready For Review**: Indicates a T&M Ticket has been signed by a company and is ready for review.
     - **Field Verified**: Indicates a T&M Ticket has been signed by a customer.
     - **Closed**: Indicates a T&M Ticket has been closed.
3. Click **Update**.

### Configure the Change Events Export Options

1. Click the **Change Events Export Options** tab.

   ##### Â Note

   This tab is only visible and available when the Change Events tool is active on the project. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools) and [Can I enable the Change Events tool on my existing project?](/faq-can-i-enable-the-change-events-tool-on-my-project)

- Under the **Summarize Labor Line Items** section, choose one of the **Group Labor Totals** options:

  ##### Â Note

  - An asterisk (\*) below indicates Procore's default setting.
  - To preview each summarization option, hover your mouse cursor over the tooltip next to each option button.
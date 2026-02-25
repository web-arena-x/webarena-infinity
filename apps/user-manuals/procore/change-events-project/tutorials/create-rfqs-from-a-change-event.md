# Create RFQs from a Change Event

Source: https://v2.support.procore.com/product-manuals/change-events-project/tutorials/create-rfqs-from-a-change-event

---

## Background

After creating a change event on a project, you can then create an RFQ for that change event. In Procore, an RFQ is a request to a collaborator to submit a price quote for the goods, services, and tasks associated with the requirements of the change event. After creating an RFQ from a change event as described in the steps below, your team has two options:

- You can invite your collaborators to enter their own responses and quotes into your Procore project. To do this, follow the steps in [Assign and Send an RFQ to a Collaborator](/product-manuals/change-events-project/tutorials/assign-and-send-an-rfq-to-a-collaborator). Next, provide your collaborator with the instructions to [Submit a Quote as a Collaborator](/product-manuals/change-events-project/tutorials/submit-a-quote-as-a-collaborator). 
   OR
- If you do NOT want your collaborators to enter their own responses and quotes, you can manage the submission process outside of Procore. Then you can enter the response and quote on behalf of your collaborator. For instructions, see [Respond to an RFQ on Behalf of a Collaborator](/product-manuals/change-events-project/tutorials/respond-to-an-rfq-on-behalf-of-a-collaborator).

## Things to Consider

- **Required User Permissions:** To create or edit an RFQ from a change event:

 - 'Admin' level permissions on the project's Change Events tool. 
     AND
 - 'Admin' level permissions on the project's Commitments tool.
- **Requirements:**

 - For a collaborator's name to appear as a selection in the **Assignee** drop-down list on an RFQ:

    - The collaborator's company must have a company record in the Project Directory. See [Add a Company to the Project Directory](/process-guides/set-up-a-project-directory/create-companies).
    - The collaborator must have an active Procore user account in the Project Directory. See [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory).
    - The collaborator's user account must be granted 'Standard' level permissions on the project's Commitments tool. See [Change a User's Permissions in the Project Directory](/product-manuals/directory-project/tutorials/change-a-users-permissions-in-the-project-directory).
    - The collaborator must be listed as an employee of the 'Contract Company' on the commitment and a member of the 'Private' drop-down list on the commitment. See [Create a Purchase Order](/product-manuals/commitments-project/tutorials/create-a-purchase-order) or [Create a Subcontract](/product-manuals/commitments-project/tutorials/create-a-subcontract).

## Prerequisites

- Add the Change Events tool to the Project Tools menu. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).
- Complete the steps in [Create a Commitment](https://support.procore.com/products/online/user-guide/project-level/commitments/tutorials/create-a-commitment) to enable the RFQs feature in the Change Events tool.
- Complete the steps in [Create](/product-manuals/change-events-project/tutorials/create-a-change-event) [a Change Event](/product-manuals/change-events-project/tutorials/create-a-change-event).

## Steps

1. Navigate to the project's **Change Events** tool.
2. Under the **CE Number - Title** tab, mark the checkbox that corresponds to the desired change event.
3. Click **Send Requests for Quote.**
4. Verify the information that is automatically populated by Procore:

   - **Title**. Procore automatically populates this field with the change event number and description. You can change the title as you want.
   - **Due Date**. Procore automatically sets the due date for seven (7) working days out. You can change the date as you want.

     ##### Â Note

     - To learn how to change the default setting default due date setting, see [Configure Settings: Commitments](/product-manuals/commitments-project/tutorials/configure-advanced-settings-commitments) and [Set Project Working Days](/product-manuals/admin-project/tutorials/set-project-working-days).

- **Request Details**. Procore enters the change event number, title, and description by default. You can replace or enter a new message that will be sent to the 'Recipients' named in the 'Commitment Select' table.
- Complete the following fields:

 - **Distribution**. Select any users that you want Procore to notify when a reply to an RFQ is submitted by a 'Recipient' named in the Commitment Select table. You can chose a distribution group and any Procore users who have been added to the project's Directory tool.

    ##### Â Notes

    - The Distribution list is intended to notify members of your company's internal project team. It is not intended to be used to notify your external subcontractors, vendors, and so on.
    - To set up a distribution group, see [Configure Settings: Commitments](/product-manuals/commitments-project/tutorials/configure-advanced-settings-commitments).
    - The creator of the RFQ will automatically receive notifications from Procore.

- **Attachments**. Attach any related items to the RFQ from Procore or from your computer.
- Under the **Commitment Select** section, some information is automatically populated for you. Confirm this information:

 - **RFQ Scope Description**. Confirm that the RFQ scope description automatically entered by Procore is as you want it. You can update this entry as needed.
 - **Contract Company**. Confirm that the correct company name appears in the drop-down list. The company name is the 'Contract Company' associated with the change event line item. The 'Contract Company' also determines the recipients you can select in the 'Recipients' list.
 - **Contract Number**. Confirm that the correct contract number is selected.
 - **Recipients**. Confirm the recipient named in the drop-down list. This user is the 'Assignee' on the RFQ.

    ##### Â Note

    If there are no designated 'Recipients' available in the list, Procore will allow you to save the RFW details. However, the RFQ cannot be sent by email without a valid 'Recipient.' To learn how to assign and RFQ to a collaborator, see [Assign and Send an RFQ to a Collaborator](/product-manuals/change-events-project/tutorials/assign-and-send-an-rfq-to-a-collaborator).
# Create a Prime Contract Change Order

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/create-a-prime-contract-change-order

---

## Background

Use the steps below when you need to create a prime contract change order.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Prime Contracts tool.
- **Additional Information:**

  - If you are using an account where is the Procore + DocuSignÂ© integration enabled, see [DocuSignÂ©](https://support.procore.com/integrations/docusign).
  - If the [Change Events](https://support.procore.com/products/online/user-guide/project-level/change-events) tool is active in Project Tools, you must complete the steps in [Create a Change Event](/product-manuals/change-events-project/tutorials/create-a-change-event). Then follow the steps in [Create a Prime Contract Change Order from a Change Event](/product-manuals/change-events-project/tutorials/create-a-prime-contract-change-order-from-a-change-event) instead of the Steps below.
- For companies using the  ERP Integrations tool: **Show/Hide**

  - Not all ERP integrations support the sync of change orders. For those that do, additional requirements, limitations, and considerations vary depending on the ERP system your company's account is integrated with. See [Things to Know About your ERP Integration](https://support.procore.com/products/online/user-guide/company-level/erp-integrations/things-to-know-about-your-erp-integration) for details.

## Prerequisites

- [Create](/product-manuals/prime-contracts-project/tutorials/create-prime-contracts) [Prime Contracts](/product-manuals/prime-contracts-project/tutorials/create-prime-contracts)

## Steps

1. Navigate to the project's **Prime Contracts** tool.
2. Locate the prime contract to work with. Then click its **Number** link.
3. Click **Create Prime Contract CO**.
4. Complete the following fields:

   - **Sign with DocuSignÂ®**If you have enabled the Procore + DocuSignÂ® integration (see [Enable or Disable the DocuSignÂ® Integration on a Procore Project](/product-manuals/admin-project/tutorials/enable-or-disable-the-docusign-integration-on-a-procore-project)), a checkmark appears in this box by default. If you do NOT want to collect signatures with DocuSignÂ®, remove the mark.

     Sign with DocuSign

     ##### Â Tip

     **How do you collect signatures with DocuSign?** After the data entry for the item is complete, Procore recommends changing the item's status to 'Out for Signature' before clicking the **Complete with DocuSign** button to launch the DocuSignÂ® application. If you have not previously signed in, you will be prompted to [Log In to DocuSignÂ®](/product-manuals/docusign/tutorials/log-in-to-docusign). Once you are signed in, you can prepare the DocuSign\_Â®\_ envelope for signatures. After the signature process is complete, Procore automatically changes the status of the item to 'Approved' and marks the item as 'Executed'. To learn more, see [DocuSignÂ®](/product-manuals/docusign/).

- **#**Accept the default number, enter a new number, or create a custom numbering scheme for this change order and future ones.

  Number

  ##### Â Notes

  - Procore automatically assigns the item a new number in sequential order. For example; 001, 002, 003, and so on.
  - To use a custom numbering scheme, enter any set of alphanumeric characters. Procore automatically assigns new numbers in sequential order using your custom scheme.

- **Date** **Created**Shows the date and time the change order was created in Procore. You cannot change this date.

  Date Created - Change Order
- **Revision.** If you revise a change order later, you can enter the revision number here.

  Revision
- **Created By**Procore automatically populates this field with the name of the user who created the change order.

  Created By - Change Order
- **Title**Enter a descriptive name here.

  Title
- **Status**Select the current status of the change order. Procore automatically places the change order in the 'Draft' status. To learn more, see [What are the default statuses for change orders in Procore?](/faq-what-are-the-default-statuses-for-change-orders-in-procore)

  Status
- **Private**Mark this checkbox if you want the item to be private. This means it is only visible to users with 'Admin' level permissions on the contract (or funding).

  Private
- **Due Date**Select a due date to indicate the date by which the 'Designated Reviewer' must approve or reject the change order.

  Due Date
- **Invoiced Date**Select the date when the change order was invoiced.

  Invoiced Date
- **Designated** **Reviewer**

  Select the Procore user at your organization who is responsible for approving or rejecting the change order. To appear as a selection in this list, the designated reviewer's Procore user account must be added to the Project Directory and have 'Standard' level permissions or higher to the contract or funding tool. See [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory).

  Designated Reviewer

  ##### Â Tip

  **Are you the 'Designated Reviewer' on a change order?** To learn how to submit an approve or reject response, see [Approve or Reject a Change Order](/product-manuals/change-orders-project/tutorials/approve-or-reject-a-change-order).
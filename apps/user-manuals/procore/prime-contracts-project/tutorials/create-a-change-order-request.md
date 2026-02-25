# Create a Change Order Request for a Prime Contract

Source: https://v2.support.procore.com/product-manuals/prime-contracts-project/tutorials/create-a-change-order-request

---

## Background

A Change Order Request (COR) provides you with the ability to create a package that contains one (1) or more Potential Change Orders (PCOs) to use as a formal request to the project's owner. When creating a COR, it is a common practice to group PCOs that share the same scope of work into a single COR. This helps to organize your change orders into logical groups, which can streamline the review and approval process for the project owner.

##### Â Important

A COR requires that your project's Prime Contracts tool is configured to use the three (3) tier change order setting. 1- and 2- tier change order configurations do NOT support the use of CORs. See [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's **Prime Contracts** tool.

## Prerequisites

- The project's prime contract must be in the 'Approved' state.

## Steps

1. Navigate to the project's **Prime Contracts** tool.
2. Locate the prime contract to work with. Then click its **Number** link.
3. Click **Create CO Request**.  
   *Note*: This button is only available if your project's prime contract is in the '**Approved'** status.
4. Complete the following:

   - **Number**. This field is automatically prefilled based on the number of other CORs that have been created. By default, the number will automatically increment by one. However, you can manually enter a different number, if desired. (*Note*: If you manually enter a number, the next COR that's created will automatically increment by one, based upon this specified value.)
   - **Date Created**. Displays the date and time that the COR was created. You cannot change this value.
   - **Revision**. This field displays the COR's revision number. When a COR is first created, its revision number is zero (0). Depending on the feedback you receive from the reviewer/approver, a COR may have multiple revisions.
   - **Created By**. Displays the name of the user who created the COR. You cannot change this name.
   - **Title**. Enter a title that describes the COR.
   - **Status**. Select the current state of the COR.

     1. **Approved**. The COR has been approved. Costs are reflected as 'Approved Changes' in the budget.
     2. **Draft**. The COR still needs to be modified before it can be submitted for review. Costs are not reflected in the budget.
     3. **Pending - In Review**. The COR is currently being reviewed by an approver. Costs are reflected as 'Pending Changes' in the budget.
     4. **Pending - Revised**. The COR has been modified since its initial submission. Costs are reflected as 'Pending Changes' in the budget.
     5. **Pending - Pricing**. The COR is pending and is currently out for pricing. Costs are reflected as 'Pending Changes' in the budget.
     6. **Pending - Not Pricing**. The COR is pending and is not actively being priced. Costs are reflected as 'Pending Changes' in the budget.
     7. **Pending - Proceeding**. The COR is still pending and the work is being completed. Costs are reflected as 'Pending Changes' in the budget.
     8. **Pending - Not Proceeding**. The COR is pending and the work is not currently taking place. Costs are reflected as 'Pending Changes' in the budget.
     9. **Rejected**. The COR was rejected. Costs are not reflected in the budget.
     10. **No Charge**. The COR will be performed at no charge. Costs are not reflected in the budget.  
         *Note*: These statuses reflect the budget in the ways listed above for the Procore Standard Budget View. To create or modify views, see [Set up a New Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project).
   - **Prime Contract Change Order**. (For 3-tier change orders only) If desired, you can add the COR to a PCCO. You can either select an existing PCCO from the drop-down menu or create a new PCCO where the COR will automatically be added to it.
   - **Private**. Mark this checkbox if you want the COR to be private and only visible to users with 'Admin' permissions on the Prime Contract tab.
   - **Description**. Enter a more detailed description of the COR.
   - **Schedule Impact**. If known, you can provide an estimate of the number of additional days that would potentially be added to the current project schedule if the COR were approved.
   - **Potential Change Order**. Select which PCOs to include in the COR.
   - **Attachments**. Select and attach any relevant documents.
5. Click **Create**.

##### Â Note

If you want to email the COR to the project owner or another user for review, click **Create & Email**. This action opens a new page where you can select the recipients for the email. The recipients can then email a reply to the message to approve the change order.
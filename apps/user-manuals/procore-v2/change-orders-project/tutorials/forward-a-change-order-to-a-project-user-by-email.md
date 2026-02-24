# Forward a Change Order to a Project User by Email

Source: https://v2.support.procore.com/product-manuals/change-orders-project/tutorials/forward-a-change-order-to-a-project-user-by-email

---

## Background

The Change Orders tool includes a built-in email function that lets you forward a [Commitment Change Order](/glossary-of-terms) or [Prime Contract Change Order](/glossary-of-terms) to any user in the Project Directory. You can also use the steps below to forward a change order to its 'Designated Reviewer.' This notifies that person that the change order is awaiting their approve or reject response.

## Things to Consider

- **Required User Permissions:**

 - 'Standard' level permissions or higher on the project's Change Orders tool.
- **Additional Information:**

 - All recipients must have a Procore user account with a valid email address. See [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory).
 - Recipients who have been granted the appropriate permissions can click the **View Online** link to view the most current update of the change order in the Procore web application.

## Prerequisites

- [Create a Commitment Change Order](/process-guides/materials-user-guide-with-financials/create-a-change-order-cco) 
   OR
- [Create a Prime Contract Change Order](/product-manuals/prime-contracts-project/tutorials/create-a-prime-contract-change-order)

## Steps

1. Navigate to the project's **Change Orders** tool.
2. Click the **Prime Contracts** or **Commitments** tab.
3. Locate the change order that you want to forward.
4. Click the **View** button.
5. Click the **Email** button.
6. Complete following fields:

   - **To** Enter the name of the Procore user to whom you want to forward the change order.

     ##### Â Important

     - To notify the person named as the 'Designated Reviewer' on a CCO or PCCO that the item is ready to be approved (or rejected), you must add that person's name in the 'To' field. This will send that person a message.

- **CC** Enter in the name of any users to copy on the email.
- **Private** Mark this check box to to ensure only users with 'Admin' permissions or those in the email distribution list can view the email.
- **Subject** The subject field will automatically populate with the name of the change order you are email forwarding, but you can manually edit this field as necessary.
- **Attachments** Attach any relevant documents or files.
- **Message** Enter in a message in the text field.
- Click **Send**.   
   Procore forwards the email to the selected users. The subject line of the email is: FW: 'FW: Prime Contract Change Order: PCCO #: Title' or 'FW: Commitment Change Order: CCO#:'
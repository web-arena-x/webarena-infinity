# Approve or Reject Commitment Change Orders

Source: https://v2.support.procore.com/product-manuals/change-orders-project/tutorials/approve-or-reject-commitment-change-orders

---

## Background

A *Commitment Change Order* (CCO) details a change in costs that affects the original [commitment](/glossary-of-terms). When you create a [change order](/glossary-of-terms), you can assign another project user as its 'Designated Reviewer'. You can only assign one (1) Procore user as a 'Designated Reviewer' per commitment. Before a reviewer can submit an 'Approve' or 'Reject' response, the change order must be in the *Pending - In Review* status.

## Things to Consider

- **Required User Permissions:**

 - *To approve or reject a commitment change order*, 'Standard' level permissions or higher on the project's Commitments and Change Orders tool, and added as the 'Designated Reviewer' on the change order.

    ##### Â Tips

    - **How do you assign a 'Designated Reviewer' to a change order?** For instructions, see [Create a Commitment Change Order](/process-guides/materials-user-guide-with-financials/create-a-change-order-cco) or [Edit a Change Order](/product-manuals/change-orders-project/tutorials/edit-a-change-order).
    - **How do you view a commitment change order that has been marked 'Private'?** You must be granted 'Standard' level permissions on the project's Commitments tool and added as a member of the 'Private' drop-down list on the commitment. See [Create a Commitment](https://support.procore.com/products/online/user-guide/project-level/commitments/tutorials/create-a-commitment).

- **Additional Information:**

 - Only one (1) user can be assigned as the 'Designated Reviewer' on the change order.
 - The 'Designated Reviewer' must submit an *Approve* or *Reject* response in Procore.
 - The 'Designated Reviewer' cannot submit a response to the change order from the Procore email notification.
- **Limitations:**

 - The 'Designated Reviewer' field is only available on downstream change orders for a commitment. This fields is NOT available on an upstream [potential change order](/glossary-of-terms).

## Prerequisites

- Place the change order into the *Pending - In Review* or *Pending - Revised* status. See [Create a Commitment Change Order](/process-guides/materials-user-guide-with-financials/create-a-change-order-cco)

## Steps

1. Open the change order requiring your response. Here are ways for a 'Designated Reviewer' to find it:

   - Locate the email message with the subject line: 'FW: Commitment Change Order: CCO#: Title.' Then the **View Online** link in the email notification to view the change order in Procore.

     ##### Â Notes

     - To receive an email notification, it must be forwarded to you by a project user. See [Forward a Change Order to a Project User by Email](/product-manuals/change-orders-project/tutorials/forward-a-change-order-to-a-project-user-by-email).
     - If you are NOT logged into Procore when you click the **View Online** link, Procore prompts you to log in. See [How to Log in to Procore Web (app.procore.com)](/product-manuals/directory-company/tutorials/log-in-to-procore-web).

- Navigate to the project's **Home** page and click the change order's link in the '**My Open Items**' area. See [About the Project Home Page](/product-manuals/home-project/tutorials/about-the-project-home-page).
- Navigate to the project's **Commitments** tool. Locate the commitment contract in the table and click the **Number** link to open it. Then click the contract's **Change Orders** tab. Locate the change order and click **View**. See [View Change Orders](/product-manuals/change-orders-project/tutorials/view-change-orders).
- Navigate to the project's **Change Orders** tool. In the **Commitments** tab, locate the change order and click **View**. See [View Change Orders](/product-manuals/change-orders-project/tutorials/view-change-orders).
- Review the change order.
- When you are ready to submit an 'Approve' or 'Reject' response, scroll to the **Reviewer's Response** box.
- Choose from these options:

 - To approve the change order, enter any approval comments. Then click **Approve this CCO**.

    ##### Â In Beta

    **Note to users participating in the 'Subcontractor Estimated Completion' limited release beta program.** When a user places a change order in the 'Approved' status and it includes a value in 'Schedule Impact' field of the change order, Procore automatically updates the 'Estimated Completion Date' field in the commitment contract by the number of days entered.
# Approve or Reject Funding Change Orders

Source: https://v2.support.procore.com/product-manuals/change-orders-project/tutorials/approve-or-reject-funding-change-orders

---

## Background

A *change order* details a modification that changes the scope of work or pricing of a contract. When you create a change order, you can assign another project user as the 'Designated Reviewer' for that change order. Only one (1) Procore user can be assigned as the 'Designated Reviewer' on a change order. In addition, before the reviewer can submit an 'Approve' or 'Reject' response, the change order must be placed into the *Pending - In Review* or *Pending - Revised* status.

## Things to Consider

- **Required User Permissions:**

 - \_To approve or reject a FCO, '\_Standard' level permissions or higher on the project's Change Orders tool and added as the 'Designated Reviewer' on the change order.
 - *To view a FCO in the Change Orders tool*, 'Read Only' or 'Standard' level permissions on the project's Funding tool and added as a member of the 'Private' list on the funding.
- **Additional Information:**

 - Only one (1) project user can be named as the 'Designated Reviewer' field on a FCO.
 - A 'Designated Reviewer' can only submit a 'Reviewer's Response' when the FCO is in the '*Pending - In Review*' state.
 - FCOs must be reviewed in the Procore web application. Reviewers are NOT permitted to submit responses via email.

##### Â Notes

- For customers using Procore's Resource Tracking and Project Financials tools, production quantities and hours entered on your project's change orders automatically updates data in these Procore features, when change orders are placed in the 'Approved' status:

 - The Procore Labor Productivity Cost budget view.
 - The Field Production Report. See [Which data columns are in a Field Production Report?](/faq-which-data-columns-are-in-a-field-production-report)

## Prerequisites

- Place the FCO into the *Pending - In Review* or *Pending - Revised* status. See [Create a Funding Change Order](https://support.procore.com/products/online/user-guide/project-level/funding/tutorials/create-a-funding-change-order).

## Steps

1. Open the FCO requiring your response. Here are ways for a 'Designated Reviewer' to find it:

   - Locate the email message with the subject line: 'FW: Funding Change Order: FCO #: Title.' Then click the **View Online** link in the email notification to view the FCO in Procore.

     ##### Â Notes

     - To receive the email notification, it must be forwarded to you. For instructions, see [Forward a Change Order to a Project User by Email](/product-manuals/change-orders-project/tutorials/forward-a-change-order-to-a-project-user-by-email).
     - If you are NOT logged into Procore when you click the **View Online** line, you will be prompted to enter your login credentials.

- Navigate to the project's **Home** page and click the FCO's link in the **My Open Items** area. See [About the Project Home Page](/product-manuals/home-project/tutorials/about-the-project-home-page).
- Navigate to the project's **Funding** tool. Locate the funding and click its **Number** link to open it. Then click its **Change Orders** tab. Locate the FCO and click **View**. See [View Fundings](https://support.procore.com/products/online/user-guide/project-level/funding/tutorials/view-fundings).
- Navigate to the **Change Orders** tool. In the **Funding** tab, locate the FCO and click **View**. See [View Change Orders](/product-manuals/change-orders-project/tutorials/view-change-orders).
- Review the FCO.
- When you are ready to submit an approve or reject response, scroll to the 'Reviewer's Response' box.
- Choose from the following options:

 - To approve the FCO, enter any approval comments. Then click the **Approve this FCO** button.
 - To reject the FCO, enter an explanation about the rejection. Then click the **Reject this FCO** button.

##### Â Notes

After you click the approve or reject button detailed above, Procore does the following:

- Sends an email notification about your response to the creator of the FCO.
- Automatically adds the name of the 'Designated Reviewer' to the 'Reviewer' field on the approved or rejected FCO.
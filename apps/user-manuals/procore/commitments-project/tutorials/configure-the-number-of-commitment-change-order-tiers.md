# Configure the Number of Commitment Change Order Tiers

Source: https://v2.support.procore.com/product-manuals/commitments-project/tutorials/configure-the-number-of-commitment-change-order-tiers

---

## Background

When setting up a project's Commitments tool, most Procore clients choose to implement a 1- or 2-tier configuration setting. This setting:

- Determines how many steps are required to manage change orders for your project's commitments. To learn more, see [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)
- Must always be configured before your project team starts creating change orders. You are NOT permitted to change this setting after your team creates a change order.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Commitments tool.
- **Additional Information:**

 - To learn about the supported change order tiers in Procore, see [What are the different change order tier settings in Project Financials?](/faq-what-are-the-different-change-order-tier-settings-in-project-financials)

##### Â Important

- Your change order tier setting MUST be configured in Procore before you create the first change order on the project.
- If you do NOT specify a setting, the default setting on the tool is the 1-tier configuration.
- It is strongly recommended that you do NOT change this setting after you have created commitment change orders on your project.
- If your team is considering changing this setting during the course of the project, please be aware of the following before making a setting change:

 - You can increase the number of change order tiers from two (2) tiers to (3) tiers at any time.
 - You cannot decrease the number of change order tiers unless you first delete ALL of your project's existing change orders.
- If you choose the two (2) or three (3) tier change order configuration setting, you have an option to allow your collaborators to create their own potential change orders. Both tier settings utilize PCOs. You must also enable the 'Allow Standard Level Users to Create PCOs' checkbox. To learn more, see [Allow Collaborators to Submit Field-Initiated Change Orders (Beta)](/product-manuals/commitments-project/tutorials/allow-collaborators-to-submit-field-initiated-change-orders).

## Prerequisites

- Add the Commitments tool to the project. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).

## Workflow

Depending on the configuration you choose, your users will follow the workflow detailed below to manage changes for your project's commitments.

## Steps

1. Navigate to the project's **Commitments** tool.
2. Click **Configure Settings** .
3. Select one of these options from the **Number of Commitment Change Order Tiers** drop-down list:

   ##### Â Note

   If you choose the two (2) or three (3) tier change order configuration setting, you have an option to allow your collaborators to create their own potential change orders. Both tier settings utilize potential change orders. You must also enable the 'Allow Standard Level Users to Create PCOs' checkbox. To learn more, see [Allow Collaborators to Submit Field-Initiated Change Orders (Beta)](/product-manuals/commitments-project/tutorials/allow-collaborators-to-submit-field-initiated-change-orders).

- **One (1) Tier Change Orders**This is Procore's default configuration setting. With this setting, users create a commitment change order when there is a change to a purchase order or subcontract. Then, users submit the commitment change order to the appropriate users to review and approve.
- **Two (2)-Tier Change Orders**With this setting your project users follow these steps:

 - Create one (1) or more commitment potential change orders
 - Create a commitment change and then group the potential change orders into it. Then, users submit the commitment change orders to the appropriate users to review and approve.
 - **Three (3)-Tier Change Orders**
 - With this setting, your users follow these steps:

    - Create one (1) or more commitment potential change order(s).
    - Add the potential change orders individually or group them into a change order request. Then, users submit the change order request to the appropriate users to review and approve.
    - After approval, create a commitment change order and group all of the change order requests into it. Then, users submit the commitment change order to the appropriate users to review and approve.

      ##### Â Important

      **The three (3) tier setting is NOT a common setting to implement in a Procore project**. You should only apply the three (3)-tier change order setting to a Procore project when your billing process requires you to group all approved change orders for the month into a single, combined change order for final signature. Because this is an uncommon requirement, most Procore customers choose to implement the one (1) or two (2) tier change order setting.
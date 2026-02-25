# Create a Bid Package from an Estimate

Source: https://v2.support.procore.com/product-manuals/estimating-project/tutorials/create-a-bid-package-from-an-estimate

---

##### Â In Beta

This is feature is currently in open beta for our Procore customers. See [User Guide Bidding And Estimating Integration](/process-guides/user-guide-bidding-and-estimating-integration/) for more information.

## Background

The Bidding and Estimating Integration allows you to create bid packages directly from an estimate. By connecting the two experiences, users no longer need to recreate estimates in the Bidding tool. This allows you to send out accurate bid invitations more quickly, saving time in a competitive market. After a bid is awarded, you can update your estimate to reflect the awarded contract(s) with a single click. See [User Guide Bidding And Estimating Integration](/process-guides/user-guide-bidding-and-estimating-integration/).

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Estimating tool.

    AND
 - 'Admin' level permissions on the project's Bidding tool.
- **Additional Information:**

 - You can create multiple bid packages from the project's estimating tool.
 - Each estimate creates one bid package.
 - A separate bid form is created for each group within an estimate.

## Steps

1. Navigate to the project's **Estimating** tool.
2. Click the **Estimating** tab.
3. Select your Cost Item groups:

   - **To include everything:** Click **Actions** and select **Create Bid Package**.
   - **To include specific cost groups:** Mark the checkboxes next to the desired Cost Item groups.

     - Click **Bidding**, and select **Create Bid Package**.
4. On the **How do you want to map your estimate data to the bid package?** window, choose how to structure your bid form:

   - **Create a bid form for each top level group in the estimate**
   - **Create a single bid form with sections corresponding to each estimate group**
5. Review and update the Bid Package information. 
   *Note:* If you're creating multiple bid packages, you may want to update the name of your bid package to reflect the specific estimate.
6. Click **Create Bid Package**.
7. Your Bid Forms will appear on the left to preview what is being created. The following fields are editable:

   - Items
   - Description
   - Response Field Types

     - Unit & Quantity
     - Amount
     - Include / Exclude
8. Click **Create Bid Forms**.

##### Â Note

For the beta:

- You can create a bid package for multiple estimates.
- Each estimate creates it's own bid package.
- Within the bid package, a bid form is automatically created for each group in your estimate. Each bid form includes all line items within the group.
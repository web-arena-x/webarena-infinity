# Create a Purchase Order from a Change Event

Source: https://v2.support.procore.com/product-manuals/change-events-project/tutorials/create-a-purchase-order-from-a-change-event

---

## Background

If a change event leads to a need to create a new purchase order, you can create one directly from a change event line item using the steps below.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Change Events and Commitments tool.
- **For companies using the** **ERP Integrations tool:** Prerequisites, requirements, limitations, and considerations might apply depending on the ERP system your Procore account is integrated with.

## Prerequisites

- Add the Change Events tool to the project. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).

## Steps

1. Navigate to the project's **Change Events** tool.
2. Select the change event line items you want to create a purchase order for.
3. From the **Bulk Actions** drop-down menu, select **Create a Purchase Order** contract.
4. Enter general information about the purchase order.

   - **#**: Enter or validate the unique identifier for the purchase order. If you are creating the first purchase order on a project, Procore automatically assigns it a number (for example, PO-01-001). Subsequent purchase orders are automatically assigned the next sequential number (for example, PO-01-002).
   - **Bill To**: Enter information about the company responsible for paying the invoice. The subcontracting company will use this information to send its invoice to the correct company and address. 
     *Note*: This field will auto-populate with the data entered in the most recently created purchase order.
   - **Ship To**: Enter the address where the materials should be delivered. In some cases, you may want to specify a different location than the actual job site. 
     *Note*: This field will auto-populate with the data entered in the most recently created purchase order.
   - **Contract Company**: Select the vendor/company who will provide the purchased materials (e.g., American Construction Co.). This vendor/company must exist in the Project Directory. See [Add a Company to the Project Directory](/process-guides/set-up-a-project-directory/create-companies) (*Note*: For companies using the ERP Integrations tool with Sage 300 CRE, synced vendor/company data will have "(Sage)" appended to their names).
   - **Title**: This field is automatically filled with the name of the correlated change event, but you have the ability to adjust to your liking.
   - **Status**: Specify the status of the commitment. (Default: Draft) Purchase Orders with the status set to Draft, or Closed will not be reflected on the budget. Purchase Orders with the status Processing, Submitted, Partially Received, and Received will be listed in the Pending Cost column. Purchase Orders with the status Approved will be listed in the Committed Cost column on the Budget.
   - **Private**: Specify who can view the Purchase Order. By default, the Purchase Order is private and only visible to users with 'Admin' level permissions on the Commitments tool. You can allow non-Admin level users to view the purchase order, if desired. Additionally, you can allow selected non-Admin users to have read-only access to the to individual line items under the SOV tab.
   - **Payment Terms**: Specify relevant payment conditions, if applicable.
   - **Assigned To**: Select the person from the vendor/company who is responsible for the fulfillment of the purchase order.
   - **Deliver Date**: Specify the date when the purchased goods are to be delivered to the location specified in the "Ship To" field.
   - **Ship Via**: Specify how the materials will be shipped. (for example, freight, FedEx, and so on.)
   - **Default Retainage**: Specify the percent of payment retainage that will be withheld (for example, 10).
   - **Executed**: Specify whether or not the materials have been delivered. Alternatively, you can use this checkbox to denote that the purchase order was fully signed and executed.
   - **Description**: This field is automatically filled with the name and description of the correlated change event, but you have the ability to adjust to your liking.
   - **Attachments**: Attach any related materials such as pricing quotes, receipts, signed purchase orders, etc. You may attach files that have been uploaded to your project or drag and drop files from your local computer.
5. Click **Create.** The Schedule of Values will be created from the change event line items.
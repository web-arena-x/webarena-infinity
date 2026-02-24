# Create a Purchase Order (Android)

Source: https://v2.support.procore.com/product-manuals/commitments-android/tutorials/create-a-purchase-order-android

---

## Background

A purchase order typically represents a contractual agreement issued by a buyer to a seller, indicating types, quantities, and agreed prices for products or services.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Commitments tool. 
    OR
 - 'Read Only' or 'Standard' level permissions on the project's Commitments tool with the ['Create Purchase Order' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
- **Additional Information:**

 - You can configure what items are created with the **quick create** icon, see [Configure Quick Create Settings](/product-manuals/project-overview-screen-ios/tutorials/configure-quick-create-settings-ios).
 - This action can be performed offline. Tasks performed offline sync with Procore once a network connection is reestablished.

## Prerequisites

- [Configure Settings: Commitments](/product-manuals/commitments-project/tutorials/configure-advanced-settings-commitments)

## Steps

1. Open the **Procore** app on an Android mobile device and select a project. 
   *Note:* This loads the Tools screen for the project.
2. Tap the **quick create** icon and select **Purchase Order**. 
   OR Tap the **Commitments** tool, then tap the **create** icon.
3. Tap into the following fields to add the desired information:

   - **Title:** Provide a descriptive name for the commitment.
   - **#:** Enter or validate the unique identifier for the commitment. If you are creating the first commitment of a project, Procore will automatically number the commitment (for example, PO-01-001). Subsequent commitments will automatically be prefilled with the next sequential number based on the format of the first commitment (for example, PO-01-002).
   - **Status:** Specify the status of the commitment. (Default: 'Draft') Purchase Orders with the status set to 'Draft,' or 'Closed' will not be reflected on the budget. Purchase Orders with the status Processing, Submitted, Partially Received, and Received will be listed in the Pending Cost column. Purchase Orders with the status Approved will be listed in the Committed Cost column on the on the Budget.
   - **Private:** The commitment will be private by default. Tap the toggle to OFF remove the privacy setting.
   - **Executed:** This setting is OFF by default. Tap the toggle to ON to signify that the commitment has been executed.
   - **Contract Company:** Select the vendor/company who will provide the purchased materials (for example, American Construction Co.). This vendor/company must exist in Procore's Project Directory.
   - **Bill To:** Enter information about the company responsible for paying the invoice. The subcontracting company will use this information to send its invoice to the correct company and address.
   - **Ship To:** Enter the address where the materials should be delivered. In some cases you may want to specify a different location than the actual job site.
   - **Default Retainage:** Specify the percent of payment retainage that will be withheld (for example, 10).
   - **Description:** Provide additional information, as necessary.
   - **Delivery Date:** Specify the date when the purchased goods are to be delivered to the location specified in the "Ship To" field.
   - **Payment Terms:** Specify relevant payment conditions, if applicable.
   - **Ship Via:** Enter the shipping/transport method for materials (for example, freight, FedEx, etc.).
   - **Attachments:** Attach any related materials such as pricing quotes, receipts, signed purchase orders, etc. You may attach files that have been uploaded to your project or drag and drop files from your local computer.
4. Tap **Create**.
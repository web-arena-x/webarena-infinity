# Create a Purchase Order (iOS)

Source: https://v2.support.procore.com/product-manuals/commitments-ios/tutorials/create-a-purchase-order-ios

---

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Commitments tool. 
    OR
 - 'Read Only' or 'Standard' level permissions on the project's Commitments tool with the ['Create Purchase Order Contract' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
- **Additional Information:**

 - To configure what items are created with the **quick create** icon, see [Configure Quick Create Settings](/product-manuals/project-overview-screen-ios/tutorials/configure-quick-create-settings-ios).
 - This action can be performed in offline mode. Tasks performed in offline mode will sync with Procore once a network connection is reestablished.

## Prerequisites

- [Configure Advanced Settings: Commitments](/product-manuals/commitments-project/tutorials/configure-advanced-settings-commitments)

## Steps

1. Open the **Procore** app on an iOS mobile device and select a project. 
   *Note:* This loads the Tools screen for the project.
2. Tap the **quick create** icon and select **Purchase Order**. 
   OR Tap the **Commitments** tool and tap the **create** icon.
3. Enter the following information:

   - **Title:** Provide a descriptive name for the commitment.
   - **Status:** Specify the status of the commitment. (Default: Draft) Purchase Orders with the status set to Draft, or Closed will not be reflected on the budget. Purchase Orders with the status Processing, Submitted, Partially Received, and Received will be listed in the Pending Cost column. Purchase Orders with the status Approved will be listed in the Committed Cost column on the Budget.
   - **Private:** Slide the toggle to the ON position to mark the purchase order as 'Private'.
   - **Executed:** Slide the toggle to the ON position to indicate that the purchase order has been executed.
   - **Contract Company:** Select the vendor/company who will provide the purchased materials (for example, American Construction Co.). This vendor/company must exist in Procore's Project Directory. See [Add a Company to the Project Directory](/process-guides/set-up-a-project-directory/create-companies).
   - **Bill To:** Enter information about the company responsible for paying the invoice. The subcontracting company will use this information to send its invoice to the correct company and address.
   - **Ship to:** Enter the address where the materials should be delivered. In some cases you may want to specify a different location than the actual job site.
   - **Default Retainage:** Specify the percent of payment retainage that will be withheld (for example, 10).
   - **Description:** Provide additional information, as necessary.
   - **Delivery Date:** Specify the date when the purchased goods are to be delivered to the location specified in the 'Ship To' field.
   - **Payment Terms:** Specify relevant payment conditions, if applicable.
   - **Ship Via:** Enter the shipping/transport method for materials (for example, freight, FedEx, etc.).
   - **Add Attachment:** Tap this link to add any relevant files or photos.
4. Tap **Save**.
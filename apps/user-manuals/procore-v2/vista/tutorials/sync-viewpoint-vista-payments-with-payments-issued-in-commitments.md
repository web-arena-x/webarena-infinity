# Sync ViewpointÂ® Vistaâ¢ Payments with Payments Issued in Commitments

Source: https://v2.support.procore.com/product-manuals/vista/tutorials/sync-viewpoint-vista-payments-with-payments-issued-in-commitments

---

## Background

If your company has enabled the ERP Integrations tool and configured it to work with VistaÂ®, your project's accountants can enter bill payments in VistaÂ® against bills synced from Procore and then export those payments into Procore. This feature automatically imports the specified VistaÂ® payments into the Payments Issued tab for subcontracts and purchase orders in the Commitments tool.

## Things to Consider

- **Required User Permission**:

  - To view payments made against subcontractor invoice, 'Read-Only' level permission or higher on the project's Commitments tool.
  - To change the configuration settings in the ERP Integrations tool, 'Admin' level permission on the ERP Integrations tool.
- **Requirements**:

  - The ERP Integrations tool must be configured for VistaÂ®.
  - The Commitments tool must be active on the desired project(s).
  - The Invoice Tool must be active. to turn on Subcontract Invoice Export for the integration.
  - The Payments Issued tab must also be enabled in the project's Commitments tool.
- **Prerequisites**:

  - The subcontractor invoice for which a payment is being made must first be exported to VistaÂ®.
- **Supported Items**:  
   The sync process supports the following payments:

  - Check and Credit Card payments in VistaÂ®.
  - Full and partial payments in VistaÂ®.
  - Changes made to a payment after it is synced. For example, voiding a check.
- **Limitations**:

  - Invoices that were created in Procore and sent to VistaÂ® as AP Unapproved invoices are out of scope.
  - There are no special considerations being made for retainage payments as part of this feature.
  - Voided payments in VistaÂ®:

    - When voiding payments in VistaÂ® you will be presented with a check box called âRecord CM Reference as Void - number cannot be reusedâ. When NOT checking this box, instead of updating the payment header as âVoidedâ, VistaÂ® will delete the payment (check number) from the database. **If the above box is not checked one of the following actions must be taken to void this payment in Procore**:
    - to request that they unlink the payment from the ERP. Once the payment is unlinked, the user can delete the payment record from Procore.
    - Manually create an additional an payment record in Procore with a negative amount to cancel out the original amount, and a note stating âVOIDEDâ. Please note that this is **not an update** to the original payment, but rather an **additional payment record**.
- **Additional Information**:

  - Users cannot edit synced payments in Procore.
  - Synced payments deleted in VistaÂ® are not deleted automatically from Procore. To delete a synced payment, . Include details such as project number, commitment number, and invoice number, as well as details about the specific payment.

## Steps

### 1. Wait for the Scheduled Payment Sync

The hourly sync schedule will import your VistaÂ® subcontract invoice payments for subcontractor invoices that have already been synced with Procore.

1. Ensure that these prerequisites have been completed:

   - Complete the steps in [Export Subcontractor Invoices from Procore to ERP](/product-manuals/erp-integrations-company/tutorials/export-subcontractor-invoices-from-procore-to-erp).
2. After the next scheduled sync, follow these steps to verify that your bill payments have synced with the project's corresponding commitment:

   1. Navigate to the project's **Commitments** tool.
   2. Locate the desired commitment and click **View**.
   3. Verify that the value in the **Invoice #** matches the bill number in VistaÂ®.
   4. Click the **Payments Issued** tab. A GREEN icon indicates that the bill payment has successfully been synced.
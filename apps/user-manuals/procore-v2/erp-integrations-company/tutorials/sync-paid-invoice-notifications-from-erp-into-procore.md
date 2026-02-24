# Sync Paid Invoice Notifications from ERP into Procore

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/sync-paid-invoice-notifications-from-erp-into-procore

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

If your company has enabled the ERP Integrations tool and configured it to work with your ERP system, your project's accountants can enter payments in your ERP system against payables synced from Procore and then export those payments into Procore. This feature automatically imports the specified payments from your ERP system into the Payments Issued tab for commitments in the Commitments tool.

## Things to Consider

- **Required User Permission**:

 - To perform an on-demand sync with the ERP Integrations tool, 'Admin' level permission on the project's ERP Integrations tool.
 - To view payments made against subcontractor invoice, 'Read-Only' level permission or higher on the project's Commitments tool.
 - To change the configuration settings in the ERP Integrations tool, 'Admin' level permission on the ERP Integrations tool.
- **Requirements**:

 - The ERP Integrations tool must be configured for your ERP system.
 - The Export Subcontractor Invoices feature must be enabled.
 - The Commitments tool must be active on the desired project(s). [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).
 - The Payments Issued tab must also be enabled in the project's Commitments tool. See [Enable the Payments Issued Tab](/product-manuals/commitments-project/tutorials/enable-the-payments-issued-tab-on-a-commitment).
- **Prerequisites**:

 - The subcontractor invoice for which a payment is being made must first be exported to your ERP system. See [Export Subcontractor Invoices from Procore to ERP](/product-manuals/erp-integrations-company/tutorials/export-subcontractor-invoices-from-procore-to-erp).
 - The invoice payment(s) that you want to sync must be entered in your ERP system.
- **Additional Information**:

 - Users cannot edit synced payments in Procore.
 - Users can add or edit attachments in Procore.
 - User can add or edit the Payment number in Procore.
- **Supported Items,** **as well as additional requirements, limitations, or considerations might apply depending on the ERP system your company is integrated with.**

## Steps

### Perform an On-Demand Payment Sync

If you have 'Admin' level permission on the ERP Integrations tool or if your company has designated you as one of its 

In Procore, an *Accounting Approver* is an individual with the authority to accept and reject Procore data for export to an integrated ERP system. Accounting approvers can unlink several item types, such as commitments, commitment change orders, prime contract change orders, and subcontractor invoices, that have been synced between Procore and an integrated ERP system. See [Which ERP Integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

Accounting Approver, an *on-demand sync* lets you import bill payments made in your ERP system immediately.

1. Ensure that these prerequisites have been completed:

   - Complete the steps in [Export Subcontractor Invoices from Procore to ERP](/product-manuals/erp-integrations-company/tutorials/export-subcontractor-invoices-from-procore-to-erp).
   - Pay the bills that you want to sync in your ERP system.   
     *Note*: The sync process supports both full and partial payments in your ERP system.
2. Navigate to the **ERP Integrations** tool.
3. Click **Subcontractor Invoices**.
4. Click **Sync Payments for Synced Invoices**.
5. After the next scheduled sync, follow these steps to verify that your bill payments have synced with the project's corresponding commitment:

   1. Navigate to the project's **Commitments** tool.
   2. Click **View** next to the commitment.
   3. Verify that the value in the **Invoice #** matches the number in your ERP system.
   4. Click the **Payments Issued** tab. A GREEN icon indicates that the bill payment has successfully been synced. 
      *Note*: To learn about ERP icon color codes, see [What do the ERP icons mean?](/faq-what-do-the-erp-icons-mean)
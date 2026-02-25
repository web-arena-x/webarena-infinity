# Import a ViewpointÂ® Vistaâ¢ Vendor Record to Procore

Source: https://v2.support.procore.com/product-manuals/vista/tutorials/import-a-vendor-record-to-procore

---

## Background

When Procore is connected to VistaÂ®, you will need to make sure that the existing 'active' vendor records in VistaÂ® are linked to their corresponding company records in Procore. See [Link ERP Companies to Procore Companies](/product-manuals/erp-integrations-company/tutorials/link-erp-companies-to-procore-companies).

After existing records are linked, you'll need to add any remaining vendor records that only exist in VistaÂ® to Procore. You can import those vendor records from VistaÂ® using the steps below. If new vendor records are created in VistaÂ® in the future, and a corresponding record is not created directly in the Procore Directory tool, you'll need to repeat these steps to add them to Procore.

## Things to Consider

- **Required User Permission**:

  - 'Admin' level permission on the company's Directory tool.
- **Prerequisites**:

  - ***Important!*** Before using the steps below, always check the Company Directory to confirm that matching company record does NOT already exist in Procore. If you do not perform this check, you might end up with duplicate or unlinked company entries. See [Consolidate and Link ERP Companies to Procore Companies](/product-manuals/erp-integrations-company/tutorials/consolodate-and-link-erp-companies-to-procore-companies).
- **Additional Information**:

  - Vendor records in VistaÂ® must be marked 'Active' in order for them to appear on the 'Ready to Import' page. Vendor records marked 'Inactive' will NOT be imported.
  - New vendor records imported into Procore as new company records will automatically inherit the corresponding VistaÂ® Vendor ID.

## Steps

1. Navigate to the company's **ERP Integrations** tool.
2. Click the **Vendors** tab.
3. Under **Filters**, click **Ready to Import**.
4. Choose from these options:

   - If you want to add the new vendor record in VistaÂ® as a new company record in Procore, click **Add to Procore**. Then continue with the next step.
   - If you want to link an existing vendor record in VistaÂ® to an existing company record in Procore, see [Link ERP Companies to Procore Companies](/product-manuals/erp-integrations-company/tutorials/link-erp-companies-to-procore-companies).
5. Repeat the above step for each vendor in the list.   
    When the Integration by Procore imports the VistaÂ® vendor record into Procore, the record's company and insurance information is also imported.
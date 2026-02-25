# Export a PCCO with Multiple PCOs as Individual PCIs to CMiC

Source: https://v2.support.procore.com/product-manuals/cmic/tutorials/export-a-pcco-with-multiple-pcos-as-individual-pcis-to-cmic

---

## Background

During a construction project, you will often create prime contract change orders. When a PCCO has multiple linked PCOs in Procore, you may need to export these as individual PCIs to CMiC. Follow the steps below to export a Procore PCCO with multiple PCOs as separate PCIs in CMiC.

## Things to Consider

- **Required User Permissions:**

 - *To enable the âCreate Multiple PCIsâ setting,* 'Admin' level permissions on the project's Admin tool.
 - *To submit a request to enable the feature in your company's Procore account,* you must be your company's Procore Administrator or the CMiC integration contact on your company's Procore account.
- **Requirements:**

 - Your company's Procore Administrator must submit a request to your company's Procore point of contact to enable this feature on the backend of Procore.
 - A user with 'Admin' permission on the project's Admin tool must enable the capability to create multiple PCIs as described in the steps below.
- **Additional Information:**

 - Not all ERP Integrations support the creation of multiple PCIs.

## Steps

1. Navigate to the project's **Admin** tool.
2. Under 'Project Settings', click **General**.
3. Scroll to 'Advanced'.
4. Mark the checkbox to **Create Multiple PCIs**.
5. Click **Update**.
6. Complete the steps in [Export a PCCO to ERP](/product-manuals/erp-integrations-company/tutorials/export-a-pcco-to-erp).
# Import a Prime Contract from an Integrated ERP System into Procore

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/import-a-prime-contract-from-an-integrated-erp-system-into-procore

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

Some ERP integrations allow you to import a prime contract from your integrated ERP system into the Prime Contracts tool in a Procore project. After your contract is successfully imported, you can then continue to modify and update it in Procore. If someone in your organization changes the prime contract in your ERP system, you will need to manually sync and re-import your prime contract into Procore.

## Things to Consider

- **Required User Permission**:

 - 'Standard' level permission or higher on the ERP Integrations tool.
- **Prerequisites**:

 - The Prime Contracts tool must be active on the project in Procore.
 - Create a prime contract in your ERP system. Refer to your ERP system's documentation for instructions.
- **Additional Information**:

 - If you update the Prime Contract in your ERP system after it is imported, you will need to re-import the contract to see those changes in Procore. See [Re-import a Prime Contract into Procore from your Integrated ERP System](/product-manuals/erp-integrations-company/tutorials/reimport-a-prime-contract-from-an-integrated-erp-system-into-procore).

## Steps

1. Navigate to the Company level **ERP Integrations** tool.
2. Click the **Prime Contracts** tab.
3. Click the **Ready to Import** option in the right sidebar.
4. Locate the desired project's prime contract in the **ERP Prime Contracts Ready to be Imported** list.
5. If unit-based Prime Contracts are enabled in your ERP integration settings, you can choose to designate your prime contract as either **Unit-based** or **Amount-based** before importing.

   ##### Â Note

   - The default setting for this feature is 'Off'. If the setting is not enabled, the column will be read-only and will default to 'Amount'.
   - This change to your prime contract allows you to track units in Procore. However, these units will not sync back to your ERP system through downstream prime contract change orders at this time.
   - This does not send or retrieve unit detail to or from the ERP system. This change only allows you to track units on a Prime Contract in Procore once it is imported.

- Click **Add to Procore**.   
   A message in GREEN text confirms when your prime contract has been added to Procore.
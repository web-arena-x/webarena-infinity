# Re-import a Prime Contract from an Integrated ERP System into Procore

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/reimport-a-prime-contract-from-an-integrated-erp-system-into-procore

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

Some ERP integrations allow you to import a prime contract from your integrated ERP system into the Prime Contracts tool in a Procore project. After your contract is successfully imported, you can then continue to modify and update it in Procore. If someone in your organization changes the prime contract in your ERP system, you will need to manually sync and re-import your prime contract into Procore.

## Things to Consider

- **Required User Permission**:

 - 'Admin' level permission on the ERP Integrations tool. 
    AND
 - 'Admin' level permission on the Project level Prime Contracts tool.
- **Prerequisites**:

 - The Company level ERP Integrations tool has been configured to work with your company's Procore account.
 - The Prime Contract that you want to sync with Procore has been updated in your integrated ERP system. For example, you've added one or more line item(s) or changed existing line item(s).
- **Additional Information**: 
 You will not be able to re-import a Prime Contract when:

 - The Prime Contract is in an unapproved state.
 - The Prime Contract does not belong to a synced job.
 - The Prime Contract has inadvertently been added to two projects in your company's Procore account.

## Steps

1. Navigate to the Company level **ERP Integrations** tool.
2. Click the **Prime Contracts** tab.
3. Click the **Synced** option in the right sidebar.
4. Locate the desired project's budget in the **ERP Prime Contracts Ready to be Imported** list.
5. Click **Re-Import**.   
   *Note*: If this button is grayed out and unavailable, there is no updated information in the Prime Contract to import.
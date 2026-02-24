# Unlink or Reset PCCOs Synced with ERP

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/unlink-pccos-synced-with-erp

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

When a PCCO in Procore is synced with your ERP system, a link is created between the records in each system. Sometimes, you might need to edit or delete a PCCO that has already been synced. To be able to modify or delete a synced PCCO, you must first unlink or reset it. The option to unlink or reset depends on the ERP integration you have.

## Things to Consider

- **Required User Permissions**:

 - You need all the following:

    - 'Admin' on the project's Prime Contracts tool.
    - 'Standard' or 'Admin' on the ERP Integrations tool.
    - The person's account must be granted the 'Can Push to Accounting' privilege in the Company Directory. To request to enable this privilege, submit a request to your Procore point of contact. This must be enabled for you by Procore.
- **For most integrations, deletion of the item in the ERP system is a prerequisite for unlinking.** Prerequisites, requirements, and limitations vary depending on which ERP system your account is integrated with.

## Steps

1. Navigate to the company's **ERP Integrations** tool.
2. Click **Prime Contract** **Change Orders**.
3. Locate the desired PCCO under **Change Orders - Successfully Synced with ERP.**
4. Depending on your ERP system, you will see the option to **Unlink** or **Reset** the PCCO.

   - **Unlink** -This will verify the Change Order no longer exists in your ERP system before unlinking the record.
   - **Reset** - This will immediately un-sync the Change Order. You must manually remove the record from your ERP system before it can be re-sent.
5. Click **Unlink** or **Reset**. 
   *Note:* All edits and deletions will be reflected in the audit log within the Change History tab.
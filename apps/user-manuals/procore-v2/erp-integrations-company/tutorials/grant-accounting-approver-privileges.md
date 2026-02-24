# Grant Accounting Approver Privileges

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/grant-accounting-approver-privileges

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

An 

In Procore, an *Accounting Approver* is an individual with the authority to accept and reject Procore data for export to an integrated ERP system. Accounting approvers can unlink several item types, such as commitments, commitment change orders, prime contract change orders, and subcontractor invoices, that have been synced between Procore and an integrated ERP system. See [Which ERP Integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

Accounting Approver is a user with the ability to accept or reject items for export to an integrated ERP system. As an accounting approver who also has Admin level permissions on the Company level Directory tool, you can assign these privileges to another user in Procore by editing their user record in the Company level Directory.

Privileges to export and import items to an integrated ERP system can be assigned for each individual type of item, with a few exceptions. However, it's important to note that any user with Admin level permissions to the Company level Directory AND the 'Can push to accounting' privilege can assign themselves and other users the ability to export and import all types of items.

## Things to Consider

- **Required User Permissions**:

 - You need both:

    - 'Admin' level permissions on the Company level Directory tool
    - 'Can push to accounting' enabled on the user's Directory profile.
- Any user with 'Admin' level permissions on the Company level Directory tool AND the 'Can push to accounting' privilege can assign themselves and other users the ability to export and import all types of items. Granular control of export or import capabilities on an item type basis can only be managed for users with 'Standard' level permissions or lower on the Directory tool, though the option is presented for all user types.

## Steps

1. Navigate to the Company level **Directory** tool.
2. Locate the user record to modify.
3. Click **Edit**.
4. Scroll to the **ERP Permissions** section.
5. Mark the checkbox next to 'Can push to accounting'. 
   *Note:* If the user record being modified has 'Standard' level or lower permissions to the Directory tool, mark the checkboxes next to the items you want to give them the explicit ability to import or export from your ERP system.
6. Mark or un-mark the checkbox for 'Subscribe to ERP digest emails'. 
   *Note:* It is recommended you leave the checkbox marked for all accounting approvers. The ERP Digest Email provides accounting approvers with a daily summary email that alerts the approver that data from Procore tools are awaiting an accept or reject response from the approver.
7. Click **Save.**
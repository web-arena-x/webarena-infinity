# Resend a Rejected Company to ERP Integrations for Accounting Acceptance

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/resend-a-rejected-company-to-erp-integrations-for-accounting-acceptance

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

If you previously sent a company record to the ERP Integrations tool and it was rejected by your company's designated accounting approver, the accountant will typically include a reason when performing the rejection. The rejected company is then removed from the ERP Integrations tool. After correcting the company issue(s), use the steps below to re-send the company to the ERP Integrations tool for acceptance by the accounting approver. After acceptance, the system will export the company to the integrated ERP system.

## Things to Consider

- **Required User Permission**:

 - 'Admin' level permissions on the company's Directory tool.
- **Additional Information**:

 - When entering data in the 'Name' field in the 'General' tab, be aware that your ERP imposes a maximum limit of 30 characters on the 'Name' field.

## Steps

1. Navigate to the company's **Directory** tool.
2. Locate the company record that you want to export.
3. Click **Edit**.
4. Review the record. 
   *Note*: If you want to make any changes, it is recommended that you modify and save them before sending the company record to the ERP Integrations tool for acceptance for export by an accounting approver.
5. Click **+Re-send to ERP**. 
   *Notes*:

   - If the **Send to ERP** (or **Re-send to ERP**) button is grayed out and unavailable, hover your cursor over the **question mark** icon to learn why. Typically, its because the project's ERP data has not yet been synced or because the item does not meet the minimum requirements.
   - If the **Retrieve from ERP** button appears, the data has already been sent to the ERP Integrations tool.

The system re-sends the company record to the ERP Integrations tool for acceptance. Once accepted by an accounting approver, the system exports the company from Procore and then adds it as a company record in the integrated ERP system.
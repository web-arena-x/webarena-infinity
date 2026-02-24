# Configure Cost Code Preferences for ERP

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/configure-cost-code-preferences-for-erp

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Things to Consider

- **Required User Permission**:

 - 'Admin' level permission to the company's Admin tool.

## Steps

1. Navigate to the company's **Admin** tool.
2. Under **Company Settings**, click **Work Breakdown Structure**.
3. Under **Segments**, click **Cost Code**
4. In the **Standard Cost Code segments** page, click the desired option:

   - **ERP Standard Cost Codes**

     - Click the Settings Gear Check the box labeled **Available for use on new projects**. This setting allows new Procore projects to use your ERP Standard Cost Code segments.
       *Notes*:

       - If you will be integrating one (1) or more projects with your ERP system, you should always enable this option.
       - If you want to review the codes on the list, click **Edit** to open the ERP Standard Cost Codes page.
       - If a cost code has been deactivated, you cannot add it to a project unless you reactivate it first. See [Reactivate Segment Items](/process-guides/company-administration-work-breakdown-structure-guide/reactivate-segment-items) and [Deactivate Segment Items](/process-guides/company-administration-work-breakdown-structure-guide/deactivate-segment-items).
       - After reviewing the codes, you can click **Cost Codes** under **Company Settings** in the right pane to return to the Standard Cost Code segments page.
   - **Standard Cost Codes List**

     - Click the Settings Gear Check the box labeled **Available for use on new projects** if one (1) or more projects in Procore will NOT be synced with your ERP system.
       *Notes:*

       - Projects using the 'Standard' Cost code list CANNOT be integrated with your ERP system.
5. Click **Update**.
# Retrieve a Company from ERP Integrations Before Acceptance

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/retrieve-a-company-from-erp-integrations-before-acceptance

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

After a company record in the Directory tool is sent to the ERP Integrations tool for acceptance by an accounting approver, the system locks the record and you are NOT permitted to modify it in Procore, until it is either:

- Accepted for export to the integrated ERP system by your company's designated accounting approver.   
   OR
- Rejected by the accounting approver.

However, if you recently sent a company to the ERP Integrations tool and realize you need to quickly correct some data, you can use the steps below to retrieve the company from the ERP Integrations tool. You can only perform these retrieval steps if the accounting approver has not yet approved the company for export.

## Things to Consider

- **Required User Permission**:

 - 'Admin' level permission on the Directory tool. (Required)
 - 'Admin' level permission on the ERP Integrations tool. (Optional)
- **Additional Information**:

 - You can only retrieve a company that was sent to the company's ERP Integrations tool when it has not yet be accepted or rejected by an accounting approver.
 - If you successfully retrieve a company from the ERP Integrations tool, it is placed into an editable state in the Directory tool.

## Steps

1. Navigate to the company's **Directory** tool.
2. Click **Companies**.   
   *Note*: If your company has enabled the ERP Integrations tool for use with an 

   In Procore, the term *integrated ERP System*, is used to refer to *Enterprise Resource Planning (ERP)* software applications that can be configured to exchange data between Procore and a supported application using the Company level ERP Integrations tool. See [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

   Integrated ERP System, color-coded icons and ribbons appear in relevant areas of Procore. This visually highlights your system's ERP integration data, to help you quickly identify its current state. To learn more, see [What do the ERP icons mean?](/faq-what-do-the-erp-icons-mean)
3. Click **Edit** next to the company record.
4. Click **Retrieve from ERP**.   
   This removes the record from the Ready to Export list in the company's ERP Integrations tool.
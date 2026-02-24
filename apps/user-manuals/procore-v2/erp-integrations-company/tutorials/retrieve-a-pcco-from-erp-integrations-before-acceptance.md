# Retrieve a PCCO from ERP Integrations Before Acceptance

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/retrieve-a-pcco-from-erp-integrations-before-acceptance

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

After a PCCO is sent to the ERP Integrations tool for acceptance by an accounting approver, the system locks the PCCO. You will only be able to to modify it in Procore, after:

- The PCCO was accepted for export to the integrated ERP system by your company's designated accounting approver and has been synced with the integrated ERP system. 
   OR
- The PCCO was rejected by the accounting approver.

However, if you recently sent a PCCO to the ERP Integrations tool and realize you need to quickly correct some data, you can use the steps below to retrieve the commitment from the ERP Integrations tool. You can only perform these retrieval steps if the accounting approver has not yet approved the PCCO for export.

## Things to Consider

- **Required User Permission**:

 - 'Admin' permission on the project's Prime Contracts tool.
- **Additional Information**:

 - You can only retrieve a PCCO that was sent to the company's ERP Integrations tool if it has not yet be accepted or rejected by an accounting approver
 - If you successfully retrieve a budget from the ERP Integrations tool, you will be able to modify it using the Change Orders tab of the project's Prime Contracts tool.

## Steps

1. Navigate to the Prime Contract in the project's **Prime Contracts** tool.
2. Click the **Change Orders** tab.
3. Click **View** next to the PCCO you want to retrieve.
4. Click **Retrieve from ERP**. 
   *Notes*:

   - If the button is grayed out and unavailable, you can hover the cursor over the tooltip (?) icon to view the reason it's not available.
   - The system changes the color of the ERP icon to YELLOW. See [What do the ERP icons mean?](/faq-what-do-the-erp-icons-mean)
   - The system removes the PCCO from the ERP Integrations tool.
# Retrieve a Sub Job from ERP Integrations Before Acceptance

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/retrieve-a-sub-job-from-erp-integrations-before-acceptance

---

## Background

After a Sub Job is sent to the ERP Integrations tool for acceptance by an accounting approver, the system locks the Sub Job and you are NOT permitted to modify it in Procore, until it is either:

- Accepted for export to the integrated ERP system by your company's designated accounting approver.   
 *Note*: It must also be successfully synced with the integrated ERP system.
- OR Rejected by the accounting approver.

However, if you recently sent a commitment to the ERP Integrations tool and realize you need to quickly correct some data, you can use the steps below to retrieve the commitment from the ERP Integrations tool. However, you can only perform these retrieval steps if the accounting approver has not yet responded to the Sub Job (e.g., submitted an accept or reject response).

## Things to Consider

- **Required User Permission**:

 - 'Admin' level permission on the Project level Admin tool.
- **Prerequisites**:

 - Sub Jobs can only be retrieved from the ERP Integrations tool if it has NOT yet been accepted for export by an accounting approver.
- **Additional Information**:

 - After a Sub Job is successfully retrieved, it can be updated in the Project level Admin tool and then resent to ERP Integrations.

## Steps

1. Navigate to the Project level Admin tool tool. 
    This reveals the Sub Job page.
2. Under **Project Settings**, click **Sub Jobs**.   
    This reveals the Sub Jobs page.
3. Located the desired Sub Job in the list. Then click **View**.   
    This opens the Sub Job in view mode.
4. Click **Retrieve from ERP**   
      
   *Note*: If the button is grayed out and unavailable, you can hover the cursor over the tooltip (?) icon to view the reason its not available. 
    The system retrieves the Sub Job from the Company level ERP Integrations tool so you can make changes in the Project level Admin tool.

## Next Steps

- [Resend a Rejected Sub Job to ERP Integrations for Accounting Acceptance](/product-manuals/erp-integrations-company/tutorials/resend-a-rejected-sub-job-to-erp-integrations-for-accounting-acceptance).
# Resend a Rejected Sub Job to ERP Integrations for Accounting Acceptance

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/resend-a-rejected-sub-job-to-erp-integrations-for-accounting-acceptance

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

If you previously sent a Sub Job to the ERP Integrations tool and it was rejected by your company's designated accounting approver, the accountant will typically include a reason when performing the rejection. The rejected Sub Job is then removed from the ERP Integrations tool. After correcting the Sub Job issue(s), use the steps below to re-send the Sub Job to the ERP Integrations tool for acceptance by the accounting approver. After acceptance, the system will export the Sub Job to the integrated ERP system.

## Things to Consider

- **Required User Permissions**:

 - 'Admin' on the project's Admin tool.
- **Additional Information**:

 - The maximum character length for a Sub Job ID is 30 characters.
 - If you are unsure about what Sub Jobs are synced, you can [View a List of Synced Sub Jobs](/product-manuals/erp-integrations-company/tutorials/view-a-list-of-synced-sub-jobs).

## Steps

1. Navigate to the Project level **Admin** tool. 
    This reveals the Admin page.
2. Under **Project Settings**, click **Sub Jobs**. 
    This reveals the Sub Jobs page.
3. Locate the desired Sub Job in the list.
4. If you want to change the name of a Sub Job, double-click the desired Sub Job in the list. Then type a new name over the existing one.
5. Then click **View**.
6. If the Sub Job is in the 'Approved' status, click **Resend to ERP**. 
      
      
      
   *Note*: If this button is grayed out and unavailable, it is most likely because the Sub Job has not been approved. Hover your mouse cursor over the tooltip for more information.   
    The system sends the Sub Job to the Company level ERP Integrations tool and the icon at the top of the page changes to BLUE. See [What do the ERP icons mean?](/faq-what-do-the-erp-icons-mean)
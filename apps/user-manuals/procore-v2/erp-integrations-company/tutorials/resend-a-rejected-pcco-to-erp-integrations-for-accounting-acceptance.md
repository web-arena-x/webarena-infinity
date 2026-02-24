# Resend a Rejected PCCO to ERP Integrations for Accounting Acceptance

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/resend-a-rejected-pcco-to-erp-integrations-for-accounting-acceptance

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

If you previously sent a PCCO to the ERP Integrations tool and it was rejected by your company's designated accounting approver, the accountant will typically include a reason when performing the rejection. The rejected PCCO is then removed from the ERP Integrations tool and is also unlocked in the project's Prime Contracts tool so the issue can be corrected. After correcting the PCCO issue(s), use the steps below to re-send the PCCO to the ERP Integrations tool for acceptance by the accounting approver. After acceptance, the system will export the PCCO to the integrated ERP system.

## Things to Consider

- **Required User Permission**:

 - 'Admin' level permission on the Project level Prime Contract Tool.
- **Additional Information**:

 - The Prime Contract Change Order (PCCO) must have an 'Approved' status.
 - The Date field on a change order is required.

## Steps

1. Navigate to the Project level **Prime Contracts** tool.
2. Click the **Change Orders** tab.
3. Locate the desired PCCO in the list.
4. Choose from these options:

   - If the PCCO is in the *Approved* status, click **View**.   
        
      OR
   - If the PCCO is in any other status, click **Edit**. Then change the status to *Approved* and click **Save** at the bottom on the page. 
     *Note*: You must have 'Admin' level permission on the Prime Contract tool or be a 'Designated Approver' on the PCCO to change the status of a PCCO to *Approved*.
5. If the PCCO is in the 'Approved' status, click **Resend to ERP**. 
   *Note*: If this button is grayed out and unavailable, it is most likely because the PCCO has not been approved. Hover your mouse cursor over the tooltip for more information.   
      
      
      
    The system sends the PCCO to the Company level ERP Integrations tool and the icon at the top of the page changes to BLUE. See [What do the ERP icons mean?](/faq-what-do-the-erp-icons-mean)
# Export a Sub Job to Sage 300 CREÂ®

Source: https://v2.support.procore.com/product-manuals/sage-300-cre/tutorials/export-a-sub-job-to-sage-300-cre

---

## Background

If you want to export sub jobs to Sage 300 CREÂ®, you first need to create them in your Procore project.

After a sub job is created, an 

In Procore, an *Accounting Approver* is an individual with the authority to accept and reject Procore data for export to an integrated ERP system. Accounting approvers can unlink several item types, such as commitments, commitment change orders, prime contract change orders, and subcontractor invoices, that have been synced between Procore and an integrated ERP system. See [Which ERP Integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

Accounting Approver can export it to your ERP system.

## Things to Consider

- **Required User Permissions**:

  - 'Standard' or 'Admin' level permission on the ERP Integrations tool.  
     AND
  - The person performing the export must be granted the 'Can Push to Accounting' privilege in the Company Directory. To request to enable this privilege, submit a request to your Procore point of contact. This must be enabled for you by Procore.
- **Prerequisites**:

  - Ensure that the Sub Jobs feature has been enabled in Procore. See [Enable Sub Jobs](/process-guides/company-administration-work-breakdown-structure-guide/enable-sub-jobs-for-projects).

## Steps

To export a Sub Job to Sage 300 CREÂ®, complete these tasks:

1. [Add 'Sub Job' Segment Items to a Procore Project](/product-manuals/admin-project/tutorials/add-sub-job-segment-items-to-a-procore-project)
2. [Send a Sub Job to ERP Integrations for Accounting Acceptance](/product-manuals/erp-integrations-company/tutorials/send-a-sub-job-to-erp-integrations-for-accounting-acceptance)
3. [Accept or Reject a Sub Job for Export to ERP](/product-manuals/erp-integrations-company/tutorials/accept-or-reject-a-sub-job-for-export-to-erp)  
   *Notes*:

   - If the accounting approver accepts the Sub Job, the system exports it to Sage 300 CREÂ®.
   - If the accounting approver rejects the Sub Job, you can edit it as needed and then resend it for approval. See [Edit Sub Jobs on a Project](/process-guides/project-administration-work-breakdown-structure-guide/edit-sub-jobs-on-a-project).
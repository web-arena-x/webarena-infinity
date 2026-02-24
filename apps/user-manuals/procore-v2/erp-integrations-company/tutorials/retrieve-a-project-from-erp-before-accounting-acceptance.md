# Retrieve a Project from ERP Before Accounting Acceptance

Source: https://v2.support.procore.com/product-manuals/erp-integrations-company/tutorials/retrieve-a-project-from-erp-before-accounting-acceptance

---

##### ERP DOCUMENTATION

**Each Procore-built ERP integration offers its own unique feature set.** Your integration might not support the action described on this page.

To learn about your integration and its supported features, see [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

## Background

After a user sends a Procore project to the ERP Integrations tool for accounting acceptance, the integrated project information (e.g., 'Project Name' and 'Address') is no longer editable. This is because accepted data must be synced with your third-party ERP system. However, if you send a project to ERP and then notice a mistake that needs to be corrected, you may have time to retrieve the project to make any necessary changes. You can retrieve data only if your project changes have not yet been accepted or rejected by an 

In Procore, an *Accounting Approver* is an individual with the authority to accept and reject Procore data for export to an integrated ERP system. Accounting approvers can unlink several item types, such as commitments, commitment change orders, prime contract change orders, and subcontractor invoices, that have been synced between Procore and an integrated ERP system. See [Which ERP Integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

Accounting Approver.

## Things to Consider

- **Required User Permissions**:

 - 'Admin' level permission on the project's Admin tool.
- **Prerequisites**:

 - The project must have been previously sent to the ERP Integrations tool for accounting acceptance.

## Steps

1. Navigate to the project's **Admin** tool. 
    *Note*: When a Procore project has been integrated with an ERP system a green ERP label appears next to the General Project Information page.
2. Click **Retrieve from ERP**. 
    *Note*: If the project has not been accepted by an accountant, the system retrieves the project from the ERP Integrations tool and returns it to an editable state.   
   ***Important!*** After your changes are complete, you must resend the project to the ERP Integrations tool.
# Sync Cost Codes from Yardi VoyagerÂ®  to Procore

Source: https://v2.support.procore.com/product-manuals/yardi-voyager/tutorials/sync-cost-codes-from-yardi-voyager-to-procore

---

## Background

To sync cost codes via the Yardi integration, you must first create a budget in **Yardi**, where the line items can be set at $0 if final values are pending. You will then import these cost codes into Procore to serve as the project's financial foundation. The imported cost codes are **project-specific** and unique to each individual Procore project.

## Things to Consider

- **Required Permissions**:

  - **ERP Integrations Tool**

    - 'Standard' or 'Admin' permissions on the company's ERP Integrations tool.  
      AND
    - The person's account must be granted the 'Can Push to Accounting' privilege in the Company Directory. See [Grant Accounting Approver Privileges](/product-manuals/erp-integrations-company/tutorials/grant-accounting-approver-privileges).
  - **Project Admin tool**

    - âAdmin' user permissions on the projectâs Admin tool.
- **Additional Information**:

  - The cost code(s) in Yardi do not have a cost type. However, a cost type is required for every cost code in Procore.
  - Cost Types must be set in Yardi and cannot be specified on the Cost Code Cost Type Assignment page in the Procore project Admin tool
  - Cost codes are project specific.
  - GL account information is configured in Yardi.
  - The Yardi integration supports a maximum of five Cost Code tiers.

## Prerequisites

- The project must be synced with Yardi.

  - [Send a Procore Project to ERP for Accounting Acceptance](/product-manuals/erp-integrations-company/tutorials/send-a-procore-project-to-erp-integrations-for-accounting-acceptance).
- A budget must be created on the project in Yardi.

## Steps

#### ERP Integrations Tool

1. Navigate to the company level **ERP Integrations** tool.
2. Click **Job Costs**.
3. Under Select a Job, select your project in the drop down menu.
4. Click **Sync Job Costs for Selected Job**.

#### Project Admin Tool

1. Navigate to the project level **Admin** tool.
2. Under Project Settings, click **Work Breakdown Structure**.
3. Under Segments, click **Cost Code**.
4. Click **Refresh Cost Codes**.

##### Note

Allow up to five minutes for the cost codes to fully process and appear in Procore.
# VistaÂ®

Source: https://v2.support.procore.com/product-manuals/vista/enhancements-for-the-new-vista-integration

---

Table of Contents

## Enhancements for the new VistaÂ® Integration

### Overview

The new Procore-built VistaÂ® connector, powered by Trimble's App Xchange platform, provides several benefits over the legacy VistaÂ® connector.

### Features

- **Sync Companies with International Addresses.** Import, export, and link companies with international (non-US) addresses between Procore and VistaÂ®.
- **Delete SOV** **Line Items from Synced Prime Contracts in VistaÂ®.** Delete SOV line items from a synced prime contract in VistaÂ® and re-importthe updated contract to Procore.
- **Sync Select VistaÂ® Cost Types to Procore.** Import specific VistaÂ® cost types to Procore.
- **Delete Synced VistaÂ® Cost Types.** Delete synced VistaÂ® cost types from Procore after they have been removed in Vista.
- **Delete JC Original Estimates & Synced Cost Type Assignments.** Remove unused JC Original Estimates from VistaÂ®, and delete the relevant cost type assignments from your project's cost code list.
- **Hide Payroll Units & Hours.** Hide units and hours on payroll direct cost transactions, displaying only the total cost amount.
- **Exclude** **Vendors by VistaÂ® Fields.** Exclude vendors in VistaÂ® based on specific VistaÂ® database fields.
- **Archived Items Counts & Status.** Migration from the legacy VistaÂ® integration does not retain archived counts of items in Procore. While previously synced data remains synced, archived items (including vendors, jobs, and contracts) will be listed for import in Procore.
- **Cost Code Formatting.** Migration to the new VistaÂ® integration removes leading dots and whitespace from synced VistaÂ® cost codes in Procore.
- **Link VistaÂ® Projects to Existing Procore Projects.** Link projects in VistaÂ® to existing projects in Procore.

### Detailed Data Mapping

| PROCORE | Exports data from Procore to VistaÂ® | Imports data from VistaÂ® to Procore | VistaÂ® | Notes |
| --- | --- | --- | --- | --- |
| **PROJECTS** |  |  | **JC JOBS** | - Link projects in VistaÂ® to existing projects in Procore. |
| **COMPANIES** |  |  | **AP VENDORS** | - Import, export, and link companies with international (non-US) addresses between Procore and VistaÂ®. - Exclude vendors in VistaÂ® based on specific VistaÂ® database fields. *Note:* To enable this feature, reach out to your Procore point of contact. |
| **COST CODES** **COST TYPES** |  |  | **JOB PHASES  JOB COST TYPES** | - Import specific VistaÂ® cost types to Procore.  *Note:* This feature is only available during the implementation of the new VistaÂ® integration. - Delete synced VistaÂ® cost types from Procore after they have been removed in VistaÂ®. |
| **BUDGETS** |  |  | **JC ORIGINAL ESTIMATES** | - Remove unused JC Original Estimates from VistaÂ®, and delete the relevant cost type assignments from your project's cost code list. |
| **DIRECT COSTS** |  |  | **JTD COST DETAIL** | - Hide units and hours on payroll direct cost transactions, displaying only the total cost amount. *Note:* To enable this feature, reach out to your Procore point of contact. |
| **PRIME CONTRACT** |  |  | **JC CONTRACTS** | - Delete SOV line items from synced prime contracts in VistaÂ® and re-importthe updated contracts to Procore. |

##### Note

For details on the remaining data synced between Procore and VistaÂ®, see [Vista - Detailed Data Mapping](/product-manuals/vista/detailed-data-mapping).

### Things to Know

| Procore Item or Setting | Considerations, Limitations, and Requirements |
| --- | --- |
| **Configuration Settings & Sync Schedule** | - **Syncing**    - Migration from the legacy VistaÂ® integration does not retain archived counts of items. While previously synced data remains synced, archived items such as vendors, jobs, and contracts will reappear as available for import in the **ERP Integrations** tool.  *Note:* Total counts of archived itemsmay vary from the legacy integration due to the deletion of items in VistaÂ®.   - You can export multiple items in bulk from Procore to VistaÂ®. *Note:* For details on the items supported for export by the Vista integration, see [VistaÂ® - Detailed Data Mapping](/product-manuals/vista/detailed-data-mapping). |
| **Projects** | - **Syncing**    - You can link VistaÂ® projects to existing Procore projects using the **ERP Integrations** tool. See [Link ERP Projects to Existing Procore Projects](/product-manuals/erp-integrations-company/tutorials/link-erp-projects-to-procore-projects). |
| **Companies** | - **Syncing**    - You can import, export, and link companies with international (non-US) addresses in the **Companies** tab of the **ERP Integrations** tool.   - You can exclude vendors in VistaÂ® based on specific VistaÂ® fields. For example, the 'udSyncYN' field in Vista can be used to exclude certain vendors from being imported to Procore.Â Only vendors synced after you enable this feature will be filtered.  *Note:* To enable this feature, reach out to your Procore point of contact. |
| **Prime Contracts** | - **Syncing:**    - You can delete SOV line items from synced prime contracts in VistaÂ® and re-importthe updated contracts in the **ERP Integrations** tool. See [Re-import a Prime Contract from an Integrated ERP System into Procore](/product-manuals/erp-integrations-company/tutorials/reimport-a-prime-contract-from-an-integrated-erp-system-into-procore). |
| **Direct Costs (Transaction Detail)** | - **Additional Information**    - You can hide units and hours on payroll line items in the **Direct Costs** tool, displaying only the **Amount**. Only new payroll transactions synced after you enable this feature will have the units and hours hidden.  *Note:* To enable this feature, reach out to your Procore point of contact. |
| **Company Level Work Breakdown Structure (WBS)** | - **Syncing:**    - You can select which VistaÂ® cost types are imported into the VistaÂ®Cost Types list. *Note:* This feature is only available during the implementation of the new VistaÂ® integration.   - You can delete synced VistaÂ® cost types on the **VistaÂ® Cost Types** page in the company level **Admin** tool if they have already been deleted in VistaÂ®. - **Additional Information:**    - During the migration to the new VistaÂ® integration, leading periods and whitespace are automatically removed from synced VistaÂ® cost codes in the VistaÂ® Standard Cost Codes list. |
| **Budget** | - **Additional Information**:    - You can delete unused JC Original Estimates in VistaÂ®, and then remove the corresponding cost type assignments from the synced VistaÂ® project's cost code list. See [Delete Cost Type Assignments from a Synced ERP Project Cost Code List](/product-manuals/erp-integrations-company/tutorials/delete-cost-type-assignments-from-a-synced-erp-project-cost-code-list). |

##### Note

For details on the remaining things to know about the VistaÂ® connector, see [Vista - Things to Know](/product-manuals/vista/things-to-know).
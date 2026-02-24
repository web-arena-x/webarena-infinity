# Jobpac

Source: https://v2.support.procore.com/product-manuals/jobpac/things-to-know

---

Table of Contents

## Things to Know

### Background

Each of Procore's available ERP connectors perform the basic function of syncing data between the ERP system and Procore, usually in the same way as other connectors. However, each connector has a unique set of items it can sync, and the way those items are synced will vary based on how that ERP system and its corresponding integration are built to function.

Jobpacâ¢, like all ERP integrations, has some key considerations, limitations, and things to know about how each Procore object is synced. Those considerations, limitations, and things to know are outlined in the table below according to tool or item being synced.

### Things to know about the Jobpacâ¢ Connector

| Procore Item or Setting | Considerations, Limitations, and Requirements |
| --- | --- |
| Configuration Settings & Sync Schedule | - In order to connect Procore and Jobpac, you must have the following information:    - The server you are hosted on, environment, application, encryption key, Jobpac User ID and Password and Work ID. |
| **Work Breakdown Structure (WBS)** | - The WBS codes are created in Jobpac and imported to Procore. - Project specific cost codes are not supported and must exist on the standard cost code list. |
| Cost Codes | - A Jobpacâ¢ cost code cannot be both a header and a cost centre. - Project-specific cost codes are NOT supported with the Procore + Jobpacâ¢ integration. Your company will have one (1) cost code list for use with all Jobpacâ¢ integrated projects. - 'Cost Centre' in Jobpacâ¢ refers to 'Cost Code + Cost Type' in Procore. |
| Sub Jobs | - The sub job feature is NOT supported with the Procore + Jobpacâ¢ integration. Sub jobs are disabled in Procore for Jobpacâ¢ integrated projects. |
| Projects | - This integration was designed for use only on new construction jobs/projects. Projects that are in-progress or created before connection of the integration cannot be synced. Professional Services for assistance with integrating in-progress/pre-existing project records may be available for an additional fee. - A separate Jobpacâ¢ organization for each project is NOT supported. For each Procore company account, the integration is designed to support one (1) Jobpacâ¢ organization per connector. - Project must be created in Jobpac and imported to Procore. - Projects that are in-progress or created before connection of the integration cannot be synced. Professional Services may be available for assistance with integrating in-progress/pre-existing project records for an additional fee. - 'Job' in Jobpacâ¢ refers to 'Project' in Procore. |
| Companies | - Creditors are created in Jobpac and imported to Procore. For those that already exist in Procore, you can link the existing record. - 'Creditor' in Jobpacâ¢ refer to 'Company' in Procore. |
| **BUDGET** | - Budgets are created in Jobpac and imported to Procore, but is limited to a two tier level. |
| Commitments | - Commitments are created in Procore and exported to Jobpac. - To sync a commitment, all a Schedule of Values (SOV) line items must be tied to a cost codes and categories from your ERP-synced lists of Standard Cost Codes and Cost Types. |
| Commitment Change Orders (CCO) | - You must nominate a 1 type variation as mapped in Jobpac when exporting a Commitment Change Order. - The company account must be integrated with Jobpac. - The Change Orders and Commitments tool must be an active tab on the project. |
| Subcontractor Invoices | - The Subcontractor Invoices are created in Procore and exported to Jobpac. |
| Direct Costs | - Any expenses, labour will come from Jobpac and automatically update Procore to the associated cost code and cost type. |
| Prime Contracts | - Head Contracts are created in Procore and exported to Jobpac. Claims are exported from Procore into Jobpac; however, receipt of payment must be manually done in both systems. - Within your ERP Integration settings, ERP Admins can enable the ability to designate your prime contract as either Unit-based or Amount-based before importing to Procore. |
| Prime Contract Change Orders (Pcco) | **Syncing** You must nominate a 2 type variation as mapped in Jobpac when exporting a Head Contract Variation. **Note** You can view the 'Quantity', 'Unit of Measure (UOM)', and 'Unit Cost' fields without any values for line items in PCCOs. Currently, these fields cannot be edited because the Procore + Jobpac integration does not support this capability. |
| Timecards, Timesheets, Head Contract Invoices, and Payments | - Data from these Procore tools and items do NOT sync with Jobpacâ¢ |
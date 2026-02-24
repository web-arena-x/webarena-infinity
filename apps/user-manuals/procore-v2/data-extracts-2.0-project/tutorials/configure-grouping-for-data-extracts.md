# Configure Grouping for Data Extracts

Source: https://v2.support.procore.com/product-manuals/data-extracts-2.0-project/tutorials/configure-grouping-for-data-extracts

---

### Background

In the Data Extracts 2.0 tool, you can configure the grouping of data for various Procore tools when creating and editing extracts. This enables you to categorize the data into sub-folders within the extract based on your selected grouping options. For example, you may want to group all your inspection items by location.

### Things to Consider

- [Required User Permissions](/product-manuals/data-extracts-2.0-project/permissions)
- **Additional Information:**

 - If an item does not have a grouping option (e.g., you select 'Location' as the grouping option for the Inspections tool, but an Inspection item has a blank location field), that item will be included in a folder labeled 'Ungrouped' within your extract.
 - Grouping options are not available for the following Procore tools:

    - Change Events
    - Change Orders
    - Directory
    - Models
    - Prime Contracts

### Manage Grouping

You can group data by clicking the **Group By** button in the project level Data Extracts 2.0 tool.

1. In the Procore tool, click the **Group By** button to see the available grouping options for a Procore tool.
2. You can apply one or more grouping options to your tool's data. 
   The data is grouped based on the grouping options, and the grouped data is only visible in the extracted file.

#### Grouping Options by Tool

| Procore Tool | Grouping Option(s) |
| --- | --- |
| Action Plans | Location, Type |
| Bidding | Status |
| Correspondence | Location, Type |
| Daily Log | Created Month |
| Documents | Folder |
| Drawings | Set Name, Discipline |
| Emails | Created Month |
| Forms | Template Name |
| Incidents | Incident Month, Recordable |
| Inspections | Location, Type, Trade, and Template Name |
| Meetings | Series |
| Observations | Location, Type, Trade, and Created Month |
| Photos | Year/Month Taken, Album |
| Prime Contract Invoices | Contract, Status |
| Punch List | Location, Type, Trade, and Created Month |
| Purchase Orders | Company |
| RFI | Location, RFI Stage, and Responsible Contractor |
| Specifications | Division |
| Subcontractor Invoices | Billing Period, Company, and Status |
| Subcontracts | Company |
| Submittals | Spec Section, Location, and Type |
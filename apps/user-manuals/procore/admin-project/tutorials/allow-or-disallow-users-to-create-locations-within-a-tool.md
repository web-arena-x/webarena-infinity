# Allow or Disallow Users to Create Locations within a Tool

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/allow-or-disallow-users-to-create-locations-within-a-tool

---

## Background

Locations are typically created in the Location Manager in the project's Admin tool. Admins can choose to limit location creation to the Location Manager, or allow users to add new locations in other tools, based on a setting in the Location Manager tool.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' on the project's Admin tool.
- **Additional Information:**

 - These settings are only available if your original locations were created manually or imported.
 - If your locations hierarchy was [generated from drawings](/product-manuals/admin-project/tutorials/generate-locations-from-drawings), locations can only be added in the Drawings or Admin tools. See [Add Locations to a Project](/product-manuals/admin-project/tutorials/add-multi-tiered-locations-to-a-project).
 - This list details the Procore tools and tasks that include a 'Locations' drop-down list that interacts with the project Locations Manager in the project's Admin tool:

    | Procore Tool | To create a location, see this tutorial... |
    | --- | --- |
    | **Action Plans** | - [Create an Action Plan](/product-manuals/action-plans-project/tutorials/create-an-action-plan) |
    | **Commitments** | - [Create RFQs](/product-manuals/change-events-project/tutorials/create-rfqs-from-a-change-event) - [Create a Commitment Change Order](/product-manuals/commitments-project/tutorials/create-a-commitment-change-order-cco) |
    | **Correspondence** | - [Create a Correspondence Item](/product-manuals/correspondence-project/tutorials/create-a-correspondence-item) |
    | **Custom Tools** | (custom) |
    | **Daily Log** | - [Create a Daily Log Item](/product-manuals/daily-log-project/tutorials/create-daily-log-items) - [Create Equipment Log Entries](/product-manuals/daily-log-project/tutorials/create-equipment-entries) - [Create Inspection Log Entries](/product-manuals/daily-log-project/tutorials/create-inspection-entries) - [Create Notes Log Entries](/product-manuals/daily-log-project/tutorials/create-note-entries) - [Create Manpower Log Entries](/product-manuals/daily-log-project/tutorials/create-manpower-entries) - [Create Quantity Log Entries](/product-manuals/daily-log-project/tutorials/create-quantity-entries) |
    | **Funding** | - [Create a Potential Change Order for a Funding](/product-manuals/funding-project/tutorials/create-funding-change-orders) |
    | **Incidents** | - [Create an Incident](/product-manuals/incidents-project/tutorials/create-an-incident) |
    | **Inspections** | - [Create an Inspection](/product-manuals/inspections-project/tutorials/create-an-inspection) |
    | **Observations** | - [Create an Observation](/product-manuals/observations-project/tutorials/create-an-observation) |
    | **Photos** | - [Add Locations to a Project](/product-manuals/admin-project/tutorials/add-multi-tiered-locations-to-a-project) |
    | **Prime Contracts / Funding / Client Contracts** [What tool names and terms are different in Procore for general contractors, owners, and specialty contractors?](/faq-what-tool-names-and-terms-are-different-in-procore-for-general-contractors-owners-and-specialty-contractors) | - [Create a Potential Change Order for a Prime Contract](/product-manuals/prime-contracts-project/tutorials/create-a-potential-change-order-for-a-prime-contract) |
    | **Punch List** | - [Create a Punch List Item](/product-manuals/punch-list-project/tutorials/create-a-punch-list-item) |
    | **RFIs** | - [Create an RFI](/product-manuals/rfi-project/tutorials/create-an-rfi) |
    | **Submittals** | - [Create a Submittal](/product-manuals/submittals-project/tutorials/create-a-submittal) - [Perform Bulk Actions on Submittals](/product-manuals/submittals-project/tutorials/perform-bulk-actions-on-submittals) |
    | **Timesheets** | - [Create a Timesheet](/product-manuals/timesheets-project/tutorials/create-a-timesheet) |

## Steps

1. Navigate to the project's **Admin** tool.
2. In the 'Project Settings' menu, click **Locations**.
3. Under 'Location Settings', select or clear the **Only Allow Locations to be Created in the Location Manager Above** box:

   - **To allow users to create locations from other Procore tools**, remove the mark from the checkbox.   
     OR
   - **To restrict users from creating locations from other Procore tools**, mark the checkbox. This means that users with 'Admin' level permission on the project's Admin tool must use the Location Manager to create locations. 
     *Note:* Any change to this setting is saved automatically.

## Next Steps

1. [Add a Multi-tiered Location to an Item](/product-manuals/admin-project/tutorials/add-a-multi-tiered-location-to-an-item)
2. [Edit Multi-tiered locations](/product-manuals/admin-project/tutorials/edit-multi-tiered-locations)
3. [Filter by multi-tiered locations](/faq-how-do-i-filter-items-by-multi-tiered-locations)
# Add a Multi-Tiered Location to an Item - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/add-a-multi-tiered-location-to-an-item

---

## Objective

To add a multi-tiered location to an item within the create or edit page of an item (e.g. submittal, RFI, change order, etc.).

## Background

If your Project Administrator has enabled this functionality on the project, you may be able to add multi-tiered locations "on the fly." This means that when adding a location to an item, you will be able to create a new one from within the item's edit or create page to add to the master list of project locations.

## Things to Consider

- **Required User Permissions:**
  - Varies by tool and by task. Check the User Permissions Matrix to see what permissions you need to create or edit items on the supported tools.  
    *Note:* Users with the appropriate permission can also add a location using the Project level Admin tool. See [Add Tiered Locations to a Project](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/add-multi-tiered-locations-to-a-project "Add Tiered Locations to a Project").
- **Supported Procore Tools**:
  - This list details the Procore tools and tasks that include a 'Locations' drop-down list that interacts with the project Admin tool's Locations Manager:

    | Procore Tool | To create a location, see this tutorial... |
    | --- | --- |
    | **Action Plans** | - [Create an Action Plan](https://support.procore.com/products/online/user-guide/project-level/action-plans/tutorials/create-an-action-plan "Create an Action Plan") |
    | **Client Contracts**1 | - [Create a Potential Change Order for a Client Contract](https://support.procore.com/products/online/user-guide/project-level/client-contracts/tutorials/create-a-potential-change-order-for-a-client-contract "Create a Potential Change Order for a Client Contract") |
    | **Commitments** | - **[Create RFQs](https://support.procore.com/products/online/user-guide/project-level/change-events/tutorials/create-rfqs-from-a-change-event "Create RFQs")** - [Create a Commitment Change Order](https://support.procore.com/products/online/user-guide/project-level/commitments/tutorials/create-a-commitment-change-order-cco "Create a Commitment Change Order") |
    | **Correspondence** | - **[Create a Correspondence Item](https://support.procore.com/products/online/user-guide/project-level/correspondence/tutorials/create-a-correspondence-item "Create a Correspondence Item")** |
    | **Custom Tools** | (custom) |
    | **Daily Log** | - [Create a Daily Log Item](https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/create-daily-log-items "Add a Daily Log Item") - [Create Equipment Log Entries](https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/create-equipment-entries "Add Equipment Log Entries") - [Create Inspection Log Entries](https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/create-inspection-entries "Add Inspection Log Entries") - [Create Notes Log Entries](https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/create-note-entries "Add Notes Log Entries") - [Create Manpower Log Entries](https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/create-manpower-entries "Add Manpower Log Entries") - [Create Quality Log Entries](https://support.procore.com/products/online/user-guide/project-level/daily-log/tutorials/create-equipment-entries "Add Equipment Log Entries") |
    | **Funding**2 | - [Create a Potential Change Order for a Funding](https://support.procore.com/products/online/user-guide/project-level/funding/tutorials/create-a-potential-change-order-for-a-funding "Create a Potential Change Order for a Funding") |
    | **Incidents** | - [Create an Incident](https://support.procore.com/products/online/user-guide/project-level/incidents/tutorials/create-an-incident "Create an Incident") |
    | **Inspections** | - [Create a Project Level Inspection](https://support.procore.com/products/online/user-guide/project-level/inspections/tutorials/create-a-project-level-inspection "Create a Project Level Inspection") |
    | **Observations** | - [Create an Observation](https://support.procore.com/products/online/user-guide/project-level/observations/tutorials/create-an-observation "Create an Observation") |
    | **Photos** | - [Add Tiered Locations to a Project](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/add-multi-tiered-locations-to-a-project "Add Tiered Locations to a Project") |
    | **Prime Contracts** | - [Create a Potential Change Order for a Prime Contract](https://support.procore.com/products/online/user-guide/project-level/prime-contracts/tutorials/create-a-potential-change-order-for-a-prime-contract "Create a Potential Change Order for a Prime Contract") |
    | **Punch List** | - [Create a Punch List Item](https://support.procore.com/products/online/user-guide/project-level/punch-list/tutorials/create-a-punch-list-item "Create a Punch List Item") |
    | **RFIs** | - [Create an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/create-an-rfi "Create an RFI") |
    | **Submittals** | - [Create a Submittal](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/create-a-submittal "Create a Submittal") - [Perform Bulk Actions on Submittals](https://support.procore.com/products/online/user-guide/project-level/submittals/tutorials/perform-bulk-actions-on-submittals "Perform Bulk Actions on Submittals") |
    | **Timesheets** | - **[Create a Timesheet](https://support.procore.com/products/online/user-guide/project-level/timesheets/tutorials/create-a-timesheet "Create a Timesheet")** |

    1 **The Client Contracts tool is only available to Procore users in the United States who have implemented the Procore for Specialty Contractors point-of-view dictionary. See*[What tool names and terms are different in Procore for general contractors, owners, and specialty contractors?](https://support.procore.com/faq/what-tool-names-and-terms-are-different-in-procore-for-general-contractors-owners-and-specialty-contractors "What tool names and terms are different in Procore for general contractors, owners, and specialty contractors?")*

    2**The Funding tool is only available to Procore users in the United States who have implemented the Procore for Owners point-of-view dictionary. See* [What tool names and terms are different in Procore for general contractors, owners, and specialty contractors?](https://support.procore.com/faq/what-tool-names-and-terms-are-different-in-procore-for-general-contractors-owners-and-specialty-contractors "What tool names and terms are different in Procore for general contractors, owners, and specialty contractors?")*
- **Additional Information**:
  - Even if you have permissions to edit or create an item in the above list, your project manager may have turned off the ability to add new locations on the fly. If this is the case, you will not see the orange "Add New Location" button when you go to add a location.
  - A location can have a virtually unlimited number of tiers.
  - Duplicate location names are not permitted.
  - Locations are created on a per-project basis.

## Steps

1. Navigate to one of the supported tools.  
   *Note:* See [Things to Consider](#Things_to_Consider "How do I add a multi-tiered location to an item?") above for a list of tools that support creating new locations.
2. Click the **Edit** button next to the item you wish to add a multi-tiered location to or create a new item on that tool. (*Note:* Instructions on how to create and edit are available by searching for "Create a \_\_\_\_" or "Edit a \_\_\_\_" in the search bar at the top of this page.)
3. Select the drop-down menu next to "Location."
4. Use the type-ahead search bar to find the location you wish to add to the item, or add a new location.  
     
   ![select a multi tier location.png](https://support.procore.com/@api/deki/files/4278/select-a-multi-tier-location.png?revision=2&size=bestfit&width=437&height=262)

#### Add a New Location

You can add a brand new multi-tiered location, or you can add a new sub location to an existing multi-tiered location.

##### Add a new multi-tiered location

1. Type in the name of your first tier location. (*Note:* See [What are multi-tiered locations?](https://support.procore.com/faq/what-are-multi-tiered-locations "What are multi-tiered locations?") The first tier location will be the parent location to your sub locations, and should be the most broad. For example, in the list in the image above, we could add "Floor 3".)
2. If the 1st tier location already exists, you will be prompted to add the existing location; if the location doesn't exist, click **+ Add [location name**].
3. Type the name of your second tier location. (*Note:* The second tier locations will be a sub location to the first tier location, and it should refer to a location inside of the 1st tier. For example, you could add "Room 301" to "Floor 3").
4. Click **+Add [location name]** the green checkmark.  
     
   ![add-a-new-location-to-an-item.png](https://support.procore.com/@api/deki/files/4279/add-a-new-location-to-an-item.png?revision=2&size=bestfit&width=500)
5. Add as many sub locations as needed to apply to the location of the item. (*Note:* It is recommended that you follow the best practices for adding locations that your company has set up.)  
     
   At any point in this process, you may delete a tier and all of its sub tiers by hovering your mouse over the breadcrumbs and clicking the X to delete the location and all of its sub locations. If the location or sub location already existed in Procore before opening this multi-tier location picker, it will not delete it permanently).
6. Click **Create** when you're done adding the multi-tiered location to the item. (*Note:* The item will automatically be placed in the location field of the item).
7. Click **Update** or **Create** at the bottom of the page to save the location to the project.

##### Add a new tier to an existing location

![type-ahead.png](https://support.procore.com/@api/deki/files/4281/type-ahead.png?revision=1&size=bestfit&width=500)

1. Select the first tier location you wish to add a sub location to or use the type-ahead menu to find the first tier location you would like to add a sub location to.
2. Follow the location tier path in a similar way until you reach the tier you wish to add a new sub location to.
3. Type the name of your sub location.
4. Click **+Add [location name]** the green checkmark.
5. Click **Create** when you're done adding the multi-tiered location to the item. (*Note:* The Create button will not be selectable unless you create a new sub location. Once you click Create, the new location will automatically be placed in the location field of the item).
6. Click **Update** or **Create** at the bottom of the page to save the location to the project.

## Next Steps

- [Filter by Multi-tiered Locations](https://support.procore.com/faq/how-do-i-filter-items-by-multi-tiered-locations "How do I filter by multi-tiered locations?")

## See Also

- [Add Multi-tiered Locations](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/add-multi-tiered-locations-to-a-project "(add links/screenshots) Add Multi-tiered Locations")
- [Edit Multi-tiered Locations](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/edit-multi-tiered-locations "Edit Multi-tiered Locations")
# Delete Tiered Locations from a Project

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/delete-multi-tiered-locations

---

## Background

Locations give you the ability to link different Procore items (RFIs, Submittals, and more) to specific locations on a job site. This helps project team members to identify the exact location on a job site where a defect was observed, where materials are to be installed, or where a project change order occurred.

## Things to Consider

- **Required User Permissions:**

 - You need one of the following:

    - 'Admin' level permission on the project's Admin tool.
    - 'Read Only' or 'Standard' level permissions on the project's Admin tool with the ['Manage Locations' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permission template.
- **Additional Information:**

 - When you delete a location, the selected location and any of its sub-locations are permanently removed.

## Steps

Take the following steps based on how your locations hierarchy was created and which tool you are using:

- Manually Created or Imported (Admin Tool)
- Generated from Drawings (Admin Tool)
- Generated from Drawings (Drawings Tool)

### Delete Manually Created or Imported Locations

1. Navigate to the Project level **Admin** tool.
2. In the 'Project Settings' menu, click **Locations**.
3. Locate the desired tier.
4. Click the vertical ellipsis (â®) and choose **Delete**. 
    As shown in the example below, the system removes the selected location (e.g., *Level Four*) and all of its sub-locations (e.g., *East* and *West*).
5. At the 'Delete Warning' message, click **Confirm**.   
    The system removes the location and any sub-locations. It also disassociates any items in Procore that have been assigned to that location and its sub-locations.

### Delete Locations Generated from Drawings from the Admin Tool

##### Â Limited Release

This experience is available in **Australia, Canada, Ireland, United Kingdom, United States,** and **New Zealand**.

1. Navigate to the Project level **Admin** tool.
2. Under the 'Project Settings' menu, click **Locations**.
3. Click **Edit Location Hierarchy**.
4. Select **Skip Drawings and Edit** to edit existing locations.
5. Click the **vertical ellipsis** next to a location. Click **Delete**, then take one of the following actions:

   - Select **Delete Boundary** to delete the boundary, but maintain the location name and data.
   - Select **Delete a Location**. Then click **Delete** to confirm. 
     *Note:* Deleting a location is permanent and cannot be recovered. Deleting a location also deletes all of its sub locations and disassociates any items, such as RFIs and submittals.

### Delete Locations Generated from Drawings from the Drawings Tool

##### Â Limited Release

This experience is available in **Australia, Canada, Ireland, United Kingdom, United States,** and **New Zealand**.

1. Navigate to the **Drawings** tool.
2. Click **Locations** and select **Edit Locations,** then **Quick Edit.**
3. Click the **vertical ellipsis** next to a location. Click **Delete**, then take one of the following actions:

   - Select **Delete Boundary** to delete the boundary, but maintain the location name and data.
   - Select **Delete a Location**. Then click **Delete** to confirm. 
     *Note:* Deleting a location is permanent and cannot be recovered. Deleting a location also deletes all of its sub locations and unassociates any items, such as RFIs and submittals.
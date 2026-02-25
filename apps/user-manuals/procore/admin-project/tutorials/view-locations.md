# View Locations

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/view-locations

---

## Background

Once you've generated your locations hierarchy from drawings, you can view them using the Locations feature. The Locations feature allows you to edit locations themselves, boundaries for locations overlaid on drawings, and also view a heat map to see how many items in Procore are associated to each location. The Locations feature is accessible from both the Project level Admin tool, and the Drawings tool.

## Things to Consider

- **Required User Permissions**:

 - To view published locations:

    - 'Read Only' or higher level permissions on the project's Admin tool.
 - To view draft locations, you need one of the following:

    - 'Admin' level permissions on the project's Admin tool
    - 'Read Only' or 'Standard' level permissions with the 'Manage Locations' granular permission enabled on the project Admin tool. See [Grant Granular Permissions in a Permission Template](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template).
 - To view a heat map of items associated to locations, you need one of the following:

    - Admin' level permissions on the project's Admin tool
    - 'Read Only' or 'Standard' level permissions with the 'Manage Locations' granular permission enabled on the project Admin tool. See [Grant Granular Permissions in a Permission Template](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template).
- **Additional Information**:

 - Users will not be able to see items associated to a location if they don't have permission to view that item in its source tool.

## Steps

Take the following steps based on how your locations were created and which tool you are using:

- Manually Created or Imported (Admin Tool)
- Generated from Drawings (Admin Tool)
- Generated from Drawings (Drawings Tool)

### View Manually Created Locations from the Admin Tool

1. Navigate to the Project level **Admin** tool.
2. Click **Locations**.
3. View your location hierarchy. 
   ***Tip:*** You can also view items associated to locations, such as RFIs, submittals, and punch items. See [View Item Locations](/product-manuals/admin-project/tutorials/view-item-locations).

### View Generated Locations from the Admin Tool

##### Â Limited Release

This experience is available in **Australia, Canada, Ireland, United Kingdom, United States,** and **New Zealand**.

1. Navigate to the Project level **Admin** tool.
2. Click **Locations**.
3. Click **View Location Status**.
4. View your location hierarchy.
5. Take additional steps if you generated your locations from drawings (available in the **United States** and **Canada**):

   - To view locations in a tree structure instead of in a list view next to their associated drawings, select **Tree View**.
   - Click a **location** from the list to view the associated drawing, location boundaries, and heat map.
   - Click **Location Items**, to see items associated with the location. See [View Item Locations](/product-manuals/admin-project/tutorials/view-item-locations).
   - To view or hide boundaries and pins, move the **toggles** ON or OFF.

### View Generated Locations from the Drawings Tool

##### Â Limited Release

This experience is available in **Australia, Canada, Ireland, United Kingdom, United States,** and **New Zealand**.

1. Navigate to the Project level **Drawings** tool.
2. Click **View** **Locations**.
3. If you generated locations from drawings, click **View Locations**.
4. Take additional steps if you generated your locations from drawings (available in the **United States** and **Canada**):

   - To view locations in a tree structure instead of in a list view next to their associated drawings, select **Tree View**.
   - Click a **location** from the list to view the associated drawing, location boundaries, and heat map.
   - Click **Location Items**, to see items associated with the location. See [View Item Locations](/product-manuals/admin-project/tutorials/view-item-locations).
   - To view or hide boundaries and pins, move the **toggles** ON or OFF.
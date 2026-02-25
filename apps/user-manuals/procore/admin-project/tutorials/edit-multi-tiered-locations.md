# Edit Tiered Locations

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/edit-multi-tiered-locations

---

## Background

Locations give you the ability to link different Procore items (RFIs, Submittals, and more) to specific locations on a job site. This helps project team members to identify the exact location(s) on a job site where a defect was observed, where materials are to be installed, or where a project change order occurred.

You can edit locations as needed.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permission on the project's Admin tool. 
     OR
 - 'Read Only' or 'Standard' level permissions on the project's Admin tool with the ['Manage Locations' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permission template.
- **Limitations:** ***Important!*** Any changes to the locations in your project are updated in every place that references that location. For example, if your project has an existing single-tier location called âEast Wing Menâs Bathroomâ and you want to rename the first tier âEast Wingâ and create a second-tier within the East Wing named, âMenâs Bathroom,â any items in Procore that had been tied to the single-tier location will be automatically set to use the new "East Wing" first-tier location. If you want your items to point to the second tier location, you will need to manually edit that information in one of the supported tools. For a list of supported tools, see [What are multi-tiered locations?](/faq-what-are-multi-tiered-locations)

## Steps

Take the following steps based on how your locations hierarchy was created and which tool you are using:

- Manually Created or Imported (Admin Tool)
- Generated from Drawings (Admin Tool)
- Generated from Drawings (Drawings Tool)

### Edit Manually Created or Imported Locations

1. Navigate to the project's **Admin** tool.
2. Under 'Project Settings' in the right pane, click **Locations**.
3. Locate the location or tier that you want to edit.
4. If you want to use the search feature, highlight the location or tier that you want to search within. Then start typing the location or tier name to find the desired match.
5. Click the icon with the vertical dots and then choose **Edit** from the shortcut menu.
6. Type over the existing entry to change the location name.
7. Click the green checkmark. 
    This saves your changes automatically, so you can navigate away from the page when done editing.

### Edit Locations Generated from Drawings from the Admin Tool

##### Â Limited Release

This experience is available in **Australia, Canada, Ireland, United Kingdom, United States,** and **New Zealand**.

1. Navigate to the Project level **Admin** tool.
2. Under the 'Project Settings' menu, click **Locations**.
3. Click **Edit Location Hierarchy**.
4. Select **Skip Drawings and Edit** to edit existing locations.
5. Select a location from the list to view the associated drawing, location boundaries, and heat map.
6. To edit the name, click the **vertical ellipsis** next to a location. Select **Edit**, then click **Edit Name**.

   1. Click **Location Name.**
   2. Enter the name of the location.
   3. Click the **checkmark** to confirm.
7. To edit the boundary, click the **location name** on the list OR the **boundary** on the map. 
   *Note:* This puts you in edit mode.

   1. Click and hold the **dots** at the corners of the location's shape. Move the dots to change the boundary using a drag and drop operation.
   2. Double click, click outside the boundary, or press ENTER to save the location's boundary.
8. To move locations using a drag and drop operation, click the **Tree View.**

   1. Click the **select** icon.
   2. Click the **location** you want to move. 
       OR To select multiple locations, click and drag your cursor over the locations, or press and hold the **Shift** key and click the desired **locations**.
   3. Drag and drop the selected locations over the new parent location.

### Edit Locations Generated from Drawings from the Drawings Tool

##### Â Limited Release

This experience is available in **Australia, Canada, Ireland, United Kingdom, United States,** and **New Zealand**.

1. Navigate to the **Drawings** tool.
2. Click **Locations** and select **Edit Locations,** then **Quick Edit.**
3. Select a location from the list to view the associated drawing, location boundaries, and heat map.
4. To edit the name, click the **vertical ellipsis** next to a location. Select **Edit**, then click **Edit Name**.

   1. Click **Location Name.**
   2. Enter the name of the location.
   3. Click the **checkmark** to confirm.
5. To edit the boundary, click the **location name** on the list OR the **boundary** on the map. 
   *Note:* This puts you in edit mode.

   1. Click and hold the **dots** at the corners of the location's shape. Move the dots to change the boundary using a drag and drop operation.
   2. Double click, click outside the boundary, or press ENTER to save the location's boundary.
6. To move locations using a drag and drop operation, click the **Tree View.**

   1. Click the **select** icon.
   2. Click the **location** you want to move. 
       OR To select multiple locations, click and drag your cursor over the locations, or press and hold the **Shift** key and click the desired **locations**.
   3. Drag and drop the selected locations over the new parent location.
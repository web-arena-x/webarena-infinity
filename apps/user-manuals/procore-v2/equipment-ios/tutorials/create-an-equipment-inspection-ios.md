# Create an Equipment Inspection (iOS)

Source: https://v2.support.procore.com/product-manuals/equipment-ios/tutorials/create-an-equipment-inspection-ios

---

## Things to Consider

- [Required User Permissions](/product-manuals/equipment-ios/permissions)
- QR Codes must be scanned with QR reader for the Equipment tool in the Procore mobile app.
- You must give the Procore app permission to access the camera on your mobile device.

## Prerequisites

- To create an inspection for equipment, you must first configure the following settings:

 - The Equipment tool must be enabled for your project. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).
 - Equipment records must be added to your project. See [Add or Remove Equipment from Projects](/process-guides/project-equipment-user-guide/add-from-company-web).
 - Equipment must be enabled on your configurable fieldset for inspections. See [Edit Configurable Fieldsets](/product-manuals/admin-company/tutorials/edit-configurable-fieldsets).
 - If using Inspection Templates, [Create a Company Level Inspection Template](/product-manuals/inspections-company/tutorials/create-a-company-level-inspection-template) or [Add Inspection Templates to Your Project](/process-guides/company-equipment-setup-guide/assign-company-templates-to-projects).

## Steps

You can create an inspection from the following places:

- Equipment Tool
- Inspections tool

### Create an Inspection from the Equipment Tool

1. Navigate to the **Equipment** tool using the Procore app on an iOS mobile device.
2. Tap the equipment record. 
   OR Tap the **QR code** icon. Then point your camera toward the QR code to open the equipment details page.
3. Click the **horizontal ellipsis** and select **Create Inspection**.
4. Tap the template you want to use for the inspection. 
   *Note:* Inspection templates are created by users with 'Admin' permissions to the Company level Inspections tool. If none appear here, contact an Inspections Admin user to have them [Create a Company Level Inspection Template](/product-manuals/inspections-company/tutorials/create-a-company-level-inspection-template) or [Add Inspection Templates to Your Project](/product-manuals/inspections-project/tutorials/add-company-level-inspection-templates-to-your-project).
5. Tap into the following fields to add the appropriate information:

   - **Status**: Select the status of the inspection. New inspections are in 'Open' status by default. 
     *Note:* An inspection's status should be set to 'open' when someone begins performing the inspection. It should remain open until there are no more deficient items on the inspection. At this point, you should change the status to 'closed' to indicate that no further action is needed.
   - **Add Attachments**:

     - **Camera** **:** Tap to open your device's camera and take a photo to add to the inspection.
     - **Photos:** Tap to select an image from your device's photo library or Procore Photos. After you select the photos, click **Add** or **Done**.
     - **Files:** Tap to select a saved file from your device's files.
   - **Trade**: Select a trade related to your inspection. 
     *Note:* If you do not have trades added to your company, the 'Trade' field will appear as an empty field. You will need to add these to the Company level Admin tool before you can fill this field out. See [Add or Delete Trades](/product-manuals/admin-company/tutorials/add-a-custom-trade).
   - **Inspection Date**: Select the date the inspection is taking place.
   - **Due Date**: Select the date the inspection needs to be completed by.
   - **Assignees**: Select one or more assignees that will be responsible for the inspection. âââ
   - **Location**: Select a location associated with the inspection. 
     *Note:* You can also scan a location's QR code to enter a location:

     1. Tap the **QR code** icon in the upper right on the **Locations** menu.
     2. Point the camera of your device to the QR code automatically scan your location and add it to the inspection.
   - **Responsible Contractor**: Select the company that performed the work to be inspected. 
     *Notes:*

     - If you selected a point of contact before this, you will only be able to choose from the contractor that point of contact is associated with.
     - If no contracting companies exist in the project's Directory, you will not be able to select a 'Point of Contact'.
   - **Point of Contact**: Select a person to be the point of contact for the inspection. If you selected a 'Responsible Contractor' before this, you will only be able to choose a contact who is associated with that company. 
     *Note:* Only users with 'Standard' level permissions or above on the Observation tool may be listed as the Inspection's 'Point of Contact'.
   - **Specification Section**: Select a specification section to associate with the inspection.
   - **Private.** Move the toggle to the **ON** or **OFF** position. Private inspections are only visible to the 'Point of Contact', 'Assignee(s)', members added to the inspection's distribution list, and 'Admin' level users on the project's Inspections tool.
   - **Description**: Enter a description of the inspection.
6. Tap **Create**.

### Create an Inspection from the Inspections Tool

1. Open the **Procore** app on an iOS mobile device and select a project. 
   *Note:* This loads the Tools screen for the project.
2. Tap the **quick create** icon and select **Inspection**. 
   OR Tap the **Inspections** tool and tap the **create** icon.
3. Tap the template you want to use for the inspection. 
   *Note:* Inspection templates are created by users with 'Admin' permissions to the Company level Inspections tool. If none appear here, contact an Inspections Admin user to have them [Create a Company Level Inspection Template](/product-manuals/inspections-company/tutorials/create-a-company-level-inspection-template) or [Add Inspection Templates to Your Project](/process-guides/company-equipment-setup-guide/assign-company-templates-to-projects).
4. Tap into the following fields to add the appropriate information:

   - **Status**: Select the status of the inspection. New inspections are in 'Open' status by default. 
     *Note:* An inspection's status should be set to 'open' when someone begins performing the inspection. It should remain open until there are no more deficient items on the inspection. At this point, you should change the status to 'closed' to indicate that no further action is needed.
   - **Add Attachments**:

     - **Camera** **:** Tap to open your device's camera and take a photo to add to the inspection.
     - **Photos:** Tap to select an image from your device's photo library or Procore Photos. After you select the photos, click **Add** or **Done**.
     - **Files:** Tap to select a saved file from your device's files.
   - **Trade**: Select a trade related to your inspection. 
     *Note:* If you do not have trades added to your company, the 'Trade' field will appear as an empty field. You will need to add these to the Company level Admin tool before you can fill this field out. See [Add or Delete Trades](/product-manuals/admin-company/tutorials/add-a-custom-trade).
   - **Inspection Date**: Select the date the inspection is taking place.
   - **Due Date**: Select the date the inspection needs to be completed by.
   - **Assignees**: Select one or more assignees that will be responsible for the inspection. âââ
   - **Location**: Select a location associated with the inspection. 
     *Note:* You can also scan a location's QR code to enter a location:

     1. Tap the **QR code** icon in the upper right on the **Locations** menu.
     2. Point the camera of your device to the QR code to automatically scan your location and add it to the inspection.
   - **Responsible Contractor**: Select the company that performed the work to be inspected. 
     *Notes:*

     - If you selected a point of contact before this, you will only be able to choose from the contractor that point of contact is associated with.
     - If no contracting companies exist in the project's Directory, you will not be able to select a 'Point of Contact'.
   - **Point of Contact**: Select a person to be the point of contact for the inspection. If you selected a 'Responsible Contractor' before this, you will only be able to choose a contact who is associated with that company. 
     *Note:* Only users with 'Standard' level permissions or above on the Observation tool may be listed as the Inspection's 'Point of Contact'.
   - **Specification Section**: Select a specification section to associate with the inspection.
   - **Private.** Move the toggle to the **ON** or **OFF** position. Private inspections are only visible to the 'Point of Contact', 'Assignee(s)', members added to the inspection's distribution list, and 'Admin' level users on the project's Inspections tool.
   - **Description**: Enter a description of the inspection.
5. Tap **Create**.

##### Â Tip

1. Click **Fix Errors** to navigate to the first empty required field (if the required fields are empty or blank).
2. Click **Next Field** or **Previous Field** to view other empty fields. Once all required fields are filled, you are able to create or save the form.

## Next Steps

- [Perform an Inspection (iOS)](/process-guides/project-equipment-user-guide/perform-inspection-ios)
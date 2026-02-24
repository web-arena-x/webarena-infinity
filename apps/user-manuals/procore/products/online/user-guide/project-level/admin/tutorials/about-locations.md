# About Locations - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/about-locations

---

Table of Contents

**Table of Contents**

- [Overview](https://support.procore.com/#)
- [Considerations](https://support.procore.com/#)
- [Details](https://support.procore.com/#)
- [Common Questions](https://support.procore.com/#)
- [More](https://support.procore.com/#)

## Overview

Locations give you the ability to link different Procore items (e.g., RFIs, Submittals, and more) to specific locations on a job site. This helps project team members to identify the exact location(s) on a job site where a defect was observed, where materials are to be installed, or where a project change order occurred.

Historically, you could manually create or import your locations. These options are still available. A new enhanced Locations experience is designed to leverage the latest AI technology to automatically [generate a locations hierarchy](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/generate-locations-from-drawings "Generate Locations From Drawings") based on your project's architectural drawings.

You can view locations in the Locations screen throughout the life of your project to easily see and access items associated with each location. Locations are accessible through the Project level Admin and Drawings tools.

![locations-screen.png](https://support.procore.com/@api/deki/files/483318/locations-screen.png?revision=1)

## Considerations

- Locations must be published to be visible to users with 'Read Only' or 'Standard' level permissions. Draft locations are only visible to users with 'Admin' level permissions.
- You can add new locations, or edit existing locations, at any point during the project lifecycle.

## Details

With Locations, you can take the following actions:

- [Generate locations hierarchy from drawings](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/about-locations/details#generate_a_list_of_locations_from_architectural_drawings "Locations: Details")
- [Import locations](#Import_Locations-217634 "Locations: Details")
- [Manually create locations](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/about-locations/details#Manually_Create_Locations "Locations: Details")
- [Generate and print QR codes for locations](#Generate_and_print_QR_codes_for_locations-217634 "Locations: Details")
- [View a heat map of items associated with locations](#View_a_heat_Map_of_Items_Associated_with_Locations-217634 "Locations: Details")
- [View all items related to a location](#View_all_Items_Related_to_a_location-217634 "Locations: Details")

#### generate a locations Hierarchy from architectural drawings

With the new Locations experience, you can use your Architectural plans in Procore to automatically generate your locations hierarchy. Select which drawings to use to create your hierarchy of locations, review the locations, and modify them if needed. Each location shows a boundary around the location's area on your drawing. See [Generate Locations Hierarchy From Drawings](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/generate-locations-from-drawings "Generate Locations Hierarchy From Drawings").

#### Manually Create Locations Hierarchy

Manually create your locations hierarchy and set preferences for your users to create locations from other tools in Procore.

See [Manually Create Locations Hierarchy](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/manually-create-tiered-locations "Manually Create Tiered Locations")and [Allow or Disallow Users to Create Locations within a Tool](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/allow-or-disallow-users-to-create-locations-within-a-tool "Allow or Disallow Users to Create Locations within a Tool").

![add-third-tier.jpg](https://support.procore.com/@api/deki/files/18822/add-third-tier.jpg?revision=2&size=bestfit&width=800&height=457)

#### Import Locations

Import locations from other systems outside of Procore. You can import locations in the following ways:

- [Import Locations Using the Procore Plug-In for Revit®](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/import-locations-using-the-procore-plug-in-for-revit "Import Locations Using the Procore Plug-In for Revit®")
- [Perform a Multi-tiered Locations Import (Procore Imports)](https://support.procore.com/products/procore-imports/project-admin/tutorials/import-locations-into-your-project-level-admin-tool-procore-imports "Import Locations into your Project Level Admin Tool (Procore Imports)")
- [Request a Multi-tiered Locations Import](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/request-a-multi-tiered-locations-import "Request a Multi-tiered Locations Import")

#### Generate and print QR codes for locations

Generate and print location QR codes and post them at each location at your job site. Users in the field can scan the QR code using the Procore Mobile App to either filter by the location identified in the QR code or create an item in Procore with that location linked. See [Generate and Print QR Codes for Locations](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/generate-and-print-qr-codes-for-locations "Generate and Print QR Codes for Locations"), [Scan a QR Code to View an Item (iOS)](https://support.procore.com/procore-mobile-ios/user-guide/camera-ios/tutorials/scan-a-qr-code-with-the-procore-camera-to-view-an-item-ios "Scan a QR Code to View an Item (iOS)"), and [Scan a QR Code to View an Item (Android)](https://support.procore.com/procore-mobile-android/user-guide/camera-android/tutorials/scan-a-qr-code-with-the-procore-camera-to-view-an-item-android "Scan a QR Code to View an Item (Android)")

#### View a heat Map of Items Associated with Locations

*Note:* The heat map is only available for locations [generated from drawings](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/about-locations/details#generate_a_list_of_locations_from_architectural_drawings "Locations: Details").

When you generate locations from drawings, you can view a heat map of items associated to locations. This heat map helps you see which areas have higher activity relating to RFIs, Submittals, and more. A darker color indicates a higher number of total items linked to that location.

![locations-heat-map.png](https://support.procore.com/@api/deki/files/483311/locations-heat-map.png?revision=1&size=bestfit&width=505)

#### View all Items Related to a location

When viewing your location hierarchy, you can click a location to view a list of all items associated with that location. See [View Item Locations](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/view-item-locations "View Item Locations").

![location-items.png](https://support.procore.com/@api/deki/files/483314/location-items.png?revision=1&size=bestfit&height=350)

## Common Questions

#### How Are Locations Generated from Architectural Drawings?

The Locations feature leverages Procore's Optical Character Recognition (OCR) and Machine Learning (ML) technology to scan your project's architectural drawings. It identifies which locations should be populated in your locations list, and automatically creates the list for you based on the architectural drawings you select for use during location generation.

Once the list is created, you can review it and make any adjustments to locations and their boundaries as needed. You can add, edit, and create new locations throughout the lifecycle of your project.

#### can i add new locations after Creating the initial list?

Yes. You can edit existing locations, or add new locations, at any time.

#### Can I update Drawing Generated locations when new drawing revisions are published?

Yes. Each drawing can only have one revision selected for use with locations. Selecting a different revision of a drawing that has already been used to extract locations will replace the existing drawing with the selected revision and update the related locations.

#### does the new locations feature work on a project that already has a locations list?

Yes. At this time, all projects with or without an existing locations list can automatically leverage some of the new features for locations.

#### When Can I see the Heat map?

You can see a heat map when viewing locations from the project's Admin or Drawings tool. The heat map is only available if locations  were [generated by drawings](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/generate-locations-from-drawings "Generate Locations From Drawings").

## More

### Create Locations

- [Generate Locations Hierarchy From Drawings](generate-locations-from-drawings.md)
- [Download the Procore Plugin to Import Locations from Revit®](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/download-the-procore-plug-in-to-import-locations-from-revit "Download the Procore Plugin to Import Locations from Revit®")
- [Import Locations Using the Procore Plug-In for Revit®](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/import-locations-using-the-procore-plug-in-for-revit "Import Locations Using the Procore Plug-In for Revit®")
- [Manually Create Locations Hierarchy](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/manually-create-tiered-locations "Manually Create Tiered Locations")
- [Perform a Multi-tiered Locations Import (Procore Imports)](https://support.procore.com/products/procore-imports/project-admin/tutorials/import-locations-into-your-project-level-admin-tool-procore-imports "Import Locations into your Project Level Admin Tool (Procore Imports)")
- [Request a Multi-tiered Locations Import](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/request-a-multi-tiered-locations-import "Request a Multi-tiered Locations Import")

### Manage Locations

- [Add Tiered Locations to a Project](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/add-multi-tiered-locations-to-a-project "Add Tiered Locations to a Project")
- [Allow or Disallow Users to Create Locations within a Tool](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/allow-or-disallow-users-to-create-locations-within-a-tool "Allow or Disallow Users to Create Locations within a Tool")
- [Assign an Office Location to a Project](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/assign-an-office-location-to-a-project "Assign an Office Location to a Project")
- [Delete Tiered Locations from a Project](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/delete-multi-tiered-locations "Delete Tiered Locations from a Project")
- [Edit Tiered Locations](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/edit-multi-tiered-locations "Edit Tiered Locations")
- [Export Locations](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/export-locations "Export Locations")
- [Generate and Print QR Codes for Locations](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/generate-and-print-qr-codes-for-locations "Generate and Print QR Codes for Locations")
- [View Item Locations](https://support.procore.com/products/online/user-guide/project-level/admin/tutorials/view-item-locations "View Item Locations")
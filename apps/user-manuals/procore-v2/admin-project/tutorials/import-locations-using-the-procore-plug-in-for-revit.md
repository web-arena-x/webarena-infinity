# Import Locations Using the Procore Plugin for RevitÂ®

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/import-locations-using-the-procore-plug-in-for-revit

---

## Background

In general, your locations hierarchy can be [generated from drawings](/product-manuals/admin-project/tutorials/generate-locations-from-drawings), [created manually in the project's Admin tool](/product-manuals/admin-project/tutorials/manually-create-tiered-locations) or filled out on an Excel file to be imported by our Support team or your Procore point of contact . See [Request a Multi-tiered Locations Import](/product-manuals/admin-project/tutorials/request-a-multi-tiered-locations-import).

If you use RevitÂ® and already have locations established for your models, you can import these locations directly to your project by using the Procore plugin for RevitÂ®. Importing locations through the plugin allows you to quickly and easily add locations to your project at any time.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Project level Admin tool.
- **Additional Information**:

 - The import will only add locations to the project, and not replace any existing locations. If you need to edit locations, see [Edit Tiered Locations](/product-manuals/admin-project/tutorials/edit-multi-tiered-locations).

## Prerequisites

- You must have RevitÂ® installed on your computer. Versions 2017-2023 are currently supported. 
 *Note*: Any versions that are not installed on your computer will not appear as options in the Procore plugin manager.
- The Procore plugin manager must be installed on your Windows computer, which can then be used to install the RevitÂ® plugin. You can download the plugin from the project's Admin tool or Coordination Issues tool. See [Download the Procore Plugin for RevitÂ®](/product-manuals/admin-project/tutorials/download-the-procore-plug-in-to-import-locations-from-revit).
- ***Important!*** The setting that allows or disallows locations to only be created from the Location Manager in the Admin tool needs to be disabled in order to import locations from RevitÂ®. To manage this setting, navigate to the Locations page of the project's Admin tool and unmark the checkbox under Location Settings. See [Allow or Disallow Users to Create Locations within a Tool](/product-manuals/admin-project/tutorials/allow-or-disallow-users-to-create-locations-within-a-tool). 
 *Note*: Turning this setting off will allow users to create locations from within other tools on the project.

## Steps

*Note*: If you have already installed the plugin for RevitÂ® through the Procore plugin application, open RevitÂ® on your computer and start at step 5.

1. Open the Procore plugin manager on your computer.
2. Expand the RevitÂ® section.
3. Click **Install** next to the version of RevitÂ® you want to add the plugin to. 
   *Note*: The text on the button will change to "Installed".
4. Open RevitÂ® on your computer. 
   *Note*: A message will appear on your PC explaining "The publisher of this add-in could not be verified." You will have the following options:

   - **Always Load** (*recommended*): The plugin will always be loaded.
   - **Load Once**: The plugin will only be loaded once.
   - **Do Not Load**: The plugin will not be loaded, and you will not be able to import locations to Procore through Revit.
5. Open the model you want to import locations from.
6. Click the **Procore** tab.
7. Click **Export Locations.**
8. Select the company and project you want to add locations to. 
   *Note*: If you don't have the required permissions to add locations to the project, an error message will appear in the footer.
9. Review the levels and rooms summary shown in the plugin, then click **Next**.
10. Click **Publish** and wait for the operation to complete. This may take a few minutes. 
    *Note*: If duplicate locations are found, an error message will appear. Click **Cancel** to cancel the import, or click **Yes, Continue** to publish the rest of the locations.
11. If the operation fails, click **Retry**. 
     OR If the operation succeeds, click **Done**.
    *Note*: Procore will open to the Locations page, and the locations will automatically appear in the list of locations.
12. In RevitÂ®, click the **X** on the Procore tab to exit out of the operation.
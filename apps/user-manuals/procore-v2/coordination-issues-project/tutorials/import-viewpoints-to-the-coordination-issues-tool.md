# Import Viewpoints to the Coordination Issues Tool

Source: https://v2.support.procore.com/product-manuals/coordination-issues-project/tutorials/import-viewpoints-to-the-coordination-issues-tool

---

## Background

Importing viewpoints from NavisworksÂ® to Procore helps your teams transition from using a viewpoints workflow to using the Procore Coordination Issues tool and plugin. Imported viewpoints will be created as issues in the Coordination Issues tool so they can be tracked and managed in Procore.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the project's Coordination Issues tool.
- **Additional Information:**

 - Information from a viewpoint is carried over to the issue created from the import:

    - The title of the viewpoint becomes the Title of the coordination issue.
    - Any comments on the viewpoint are carried over to the Description field of the issue.
    - Any markups on the viewpoint, excluding Cloud markups, are also included on the issue.
 - To prevent duplication or redundant issues from being imported, a folder that has already been imported from through the plugin will not be available as an option to select for another import.

## Steps

1. Open the NavisworksÂ® application on your computer.
2. Click the **Procore** tab to open the Procore plugin.
3. Open the model you want to import viewpoints from.
4. In the plugin, click the **ellipsis** icon to open the drop-down menu.
5. Click **Import from Viewpoints**. *Note:* All folders and viewpoints will be shown in the 'Convert Viewpoints to Issues' window.
6. Mark the checkbox next to a viewpoint to select a single viewpoint, or the checkbox next to a folder containing multiple viewpoints. *Note:* Click **Select All** to import all viewpoints.
7. Select the following fields from the drop-down menus: *Note* *:* Fields with an asterisk \* are required.

   - **Status**\*

     - **Open**: Select to create new issues that require action.
     - **Closed**: Select to create historical issues that have already been resolved.
   - **Assignee**
   - **Location**
8. Click **Create**. *Note:* All viewpoints will be created as issues in the project.
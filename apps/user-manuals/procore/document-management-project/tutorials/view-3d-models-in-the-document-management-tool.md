# View 3D Models in the Document Management Tool

Source: https://v2.support.procore.com/product-manuals/document-management-project/tutorials/view-3d-models-in-the-document-management-tool

---

##### Regional availability

The Document Management tool is available in select countries. It is not yet available for Procore accounts in the U.S. To learn more, please reach out to your Procore point of contact.

## Background

Contractors without access to 3D model applications, such as AutodeskÂ® RevitÂ® files, can now view 3D models directly in Procore's Document Management tool. All project users can quickly access and view 3D models without switching between applications or Procore tools.

## Things to Consider

- **Required User Permissions:**

 - 'Standard' or 'Admin' level permissions to the project's Document Management tool. 
    *Notes:*

    - Users can only view documents that they have access to through a permission group. See [How do permissions work in the Document Management tool?](/faq-how-do-permissions-work-in-the-document-management-tool)
    - Users with 'Admin' level permissions to the Document Management tool can view all files that have been added to the 'Uploads' tab. Users with 'Standard' permission can only view the files that they have uploaded.
- **Additional Information**:

 - This feature does *not* require the [Procore BIM](/product-manuals/procore-bim-plugins/) product. Any project user with permissions to the 3D model files in the Document Management tool can view and download them, though accounts with Procore BIM have automatic processing of 3D models which can reduce user wait times.
 - This feature works on the Document Management tool's web application but *not* on mobile in the Document Management tool at this time.
 - The Procore generated model will be the entire model. It will *not* respect any hidden items or section boxes.
 - RevitÂ® models import the Default 3D view (designated as {3D} in the Project Browser in RevitÂ®). If this view does not exist, it will be created automatically.
 - NavisworksÂ® models import the latest save view as the default view.
 - The following file types are currently supported in the 3D model viewer in the Document Management tool: 
    *Note:* The latest modeling software versions are typically supported 6 months after their initial release. Support for additional file types will be added in the future.

    - RevitÂ® (.rvt) 2017-2024
    - NavisworksÂ® (.nwd, .nwc) 2017-2025
    - Industry Foundation Class (.ifc):
    - IFC2x3 (ISO/PAS 16739:2005)
    - IFC4 (ISO 16739-1:2018)
    - 3D DWG (.dwg)
    - 3D DWF (.dwf/.dwfx)
    - Other file types (see [list](/product-manuals/document-management-project/tutorials/upload-documents-to-the-document-management-tool)) can be uploaded to the Document management tool but the tool does not currently support viewing them.

## Prerequisites

- 3D model files must be [uploaded](/product-manuals/document-management-project/tutorials/upload-documents-to-the-document-management-tool), with [completed file information](/product-manuals/document-management-project/tutorials/complete-information-for-documents-in-the-document-management-tool), and then [submitted](/product-manuals/document-management-project/tutorials/submit-documents-in-the-document-management-tool) in the Document Management tool.

## Steps

1. Navigate to the project's **Document Management** tool.
2. Click on the **Documents** tab. 
   *Note:* You can also access 3D models from the **Uploads** tab. A green checkmark in the 'File' column of the 'Uploads' tab means that the file is already processed and ready for viewing.
3. Click the file name of the 3D model you want to view. If needed, learn how to search for files in the Document Management tool.
4. Click **Process File** if prompted. Since Procore accounts withProcore BIM (Models tool) automatically process 3D model files upon upload, they do not have this step.   
   *Note:* While a file is processing, a "Loading Model" window appears with a progress bar. The processing time depends on the size of the model.
5. With the model open, use the following tools to navigate and examine the model. Or view [Keyboard Interactions](/process-guides/user-guide-publish-and-manage-models-from-the-documents-tool/view-models) to learn keyboard shortcuts for all the same actions. 
      
    Click or scroll to view details on each feature.

   - Home
   - Default
   - Fly
   - Orbit
   - Objects: Search Object Names
   - Objects: Show or Hide Objects
   - Properties
   - Measure
   - Section Box
   - X-Ray Mode
   - Settings
   - Keyboard Interactions

#### Home

Click **Home** to quickly return to the Home viewpoint for the model. You can also use a keyboard shortcut: **CTRL+0** (Windows) or **CMD+0** (Mac).

#### Default

Click **Default** (or press **V** on your keyboard) to navigate the model using the default camera view.

- **Left-click + drag**: Click the left mouse button and drag the cursor up or down across the screen to rotate the camera.
- **Scroll**: Press the scroll button on your mouse and scroll up or down to move the camera forward or backward.
- **Middle-click + drag**: Press the middle click button on your mouse to move the camera perpendicularly. 
 *Tip!* You can perform a similar action by pressing and holding the space bar on your keyboard and clicking the left mouse button at the same time.
- **Right-click**: Click the right mouse button to select an object and access the following options from the drop-down menu:

 - Click **Hide Object** to hide the selected object from the view.
 - Click **Hide Similar** to hide all objects with the same name as the selected object.
 - Click **Select Similar** to highlight all objects with the same name as the selected object.
 - Click **Isolate** to isolate the selected object and hide all other objects.
 - Click **Isolate in X-Ray Mode** to show the selected object while simplifying the rest of the model.
 - Click **Isolate in Section Box** to isolate the selected object in a 'section box' and hide all other objects.
 - Click **View Properties** to view properties for the selected object.
 - Click **Zoom to Selection** to zoom to the bounding box of the selected object.

#### Fly

Click **Fly** (or press **F** on your keyboard) to navigate the model from the camera view at varying velocities.*Note:* The velocity of the camera movement will increase or decrease depending on how far you move the cursor on your mouse.

- **Left-click + drag up or down**: Click the left mouse button and drag the cursor up or down to move the camera into or away from the model.
- **Left-click + drag left or right**: Click the left mouse button and drag the cursor left or right to rotate the camera clockwise or counterclockwise.
- **Scroll**: Press the scroll button on your mouse and scroll to rotate the camera up or down.
- **Middle-click + drag**: Press the middle click button on your mouse to move the camera perpendicularly. 
 *Tip!* You can perform a similar action by pressing and holding the space bar on your keyboard and clicking the left mouse button at the same time.
- **Right-click**: Click the right mouse button to select an object and access the following options from the drop-down menu: 
   Note: To exit

 - Click **Hide Object** to hide the selected object from the view.
 - Click **Hide Similar** to hide objects with the same name.
 - Click **Select Similar** to highlight all objects with the same name as the selected object.
 - Click **Isolate** to isolate the selected object and hide all other objects.
 - Click **Isolate in X-Ray Mode** to show the selected object while simplifying the rest of the model.
 - Click **Isolate in Section Box** to isolate the selected object in a 'section box' and hide all other objects.
 - Click **View Properties** to view properties for the selected object.
 - Click **Zoom to Selection** to zoom to the bounding box of the selected object.

#### Orbit

Click **Orbit** (or press **O** on your keyboard) to rotate the camera from a fixed point.

- **Left-click on an object**: Click on an object with the left mouse button and drag the cursor left or right to rotate the camera around the click point.
- **Left-click on an empty space**: Click the left mouse button on an empty space to rotate the camera around the center of the model.
- **Middle-click + drag**: Press the middle click button on your mouse to move the camera perpendicularly around an object. 
 *Tip!* You can perform a similar action by pressing and holding the space bar on your keyboard and clicking the left mouse button at the same time.
- **Right-click**: Click the right mouse button to select an object and access the following options from the drop-down menu:

 - Click **Hide Object** to hide the selected object from the view.
 - Click **Hide Similar** to hide objects with the same name.
 - Click **Select Similar** to highlight all objects with the same name as the selected object.
 - Click **Isolate** to isolate the selected object in the view.
 - Click **Isolate in X-Ray Mode** to show the selected object while simplifying the rest of the model.
 - Click **Isolate in Section Box** to isolate the selected object in a 'section box' and hide all other objects.
 - Click **View Properties** to view properties for the selected object.
 - Click **Zoom to Selection** to zoom to the bounding box of the selected object.

#### Objects: search object names

You can search for a specific object name to automatically apply it as a filter to see all results for the object in the model. All objects beneath the filtered object are automatically included, but you can choose to hide or show objects as necessary.

1. Click **Objects** to open the Model Objects window. You can also use a keyboard shortcut: **ALT+O** (Windows) or **OPTION+O** (Mac).
2. Enter an object name in the search bar and submit your search by pressing ENTER or RETURN on your keyboard or clicking the **magnifying glass** icon. The number of results is shown in the search bar, with the object names highlighted in the object tree. 
   *Note:* Results are only shown after you submit the search.
3. Click the expand /collapse arrow to view or hide objects underneath a level, and click the **show** or **hide** icons as necessary to change what shows in the model. See the [Objects: Show or Hide Objects](/process-guides/user-guide-publish-and-manage-models-from-the-documents-tool/view-models) section below for more information.

#### Objects: show or hide objects

1. Click **Objects** to open the Model Objects window. You can also use a keyboard shortcut: **ALT+O** (Windows) or **OPTION+O** (Mac).
2. The following options are available: 
   *Note:* indicates an object is shown and indicates an object is hidden.

   - Click the arrows to expand or collapse levels of the object tree.
   - Mark the checkboxes for objects that you want to perform actions on. Click the **Object Actions** menu to access the following options:

     - **Hide Object**: Hide any selected objects from the view.
     - **Isolate**: **I**solate any selected objects from the view.
     - **Isolate in X-Ray Mode**: Show the selected object while simplifying the rest of the model.
     - **Isolate in Section Box :** Isolate the selected object in a 'section box' and hide all other objects.
     - **Zoom to Selection**: Zoom to the bounding box of any selected objects in the view.
   - If you want to show all objects on the model again, click **Unhide** in the bottom menu.

####
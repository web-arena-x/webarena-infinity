# Getting Started Guide: 2D Views in the Models Tool

Source: https://v2.support.procore.com/product-manuals/models-project/tutorials/getting-started-guide-2d-views-in-the-models-tool

---

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Models tool.
- **Additional Information**:

  - The 2D Views feature is only available on the Procore app for iOS devices.

## Prerequisites

- The Models tool must be active on the project.
- You must have access to the following AutodeskÂ® programs: NavisworksÂ® (Manage or Simulate) and RevitÂ®.

## Steps

Follow the steps below to use the 2D Views feature for the first time:

1. Download or Update the Procore App on an iOS Device
2. Download the Procore Plugin on a Computer
3. Publish a Model to Procore
4. Export Grids from Revit

### Step 1: Download or Update the Procore App on an iOS Device

1. If the Procore app is not already on your iOS device, you will need to download it from the App Store.
2. Open the **Procore** app.
3. Confirm that your app version is 2021.0412 or later.

   - To see what version you are currently using, tap **Settings** and scroll to the bottom. The version number is shown under your Procore email address, next to 'Procore for iOS'.
   - If you need to update the app, go to the App Store on your device to initiate the update. See [Update the Procore iOS App](/process-guides/getting-started-procore-app-ios/update-the-procore-ios-app).

### Step 2: Download the Procore Plugin on a Computer

See the full [Download the Procore Plugin for the Models Tool](/product-manuals/models-project/tutorials/download-the-procore-plugin-for-the-models-tool) tutorial, or click below to view the steps.

**Show** **/Hide Steps**

1. [Download](https://procore-vdc.s3.amazonaws.com/ProcoreVdcSetup.exe)the plugin application to your Windows computer. *Note:* You can also download the plugin directly from the Models tool in Procore by clicking **Download Plugin**.
2. Click the downloaded .exe application file to begin setting up the plugin.
3. Allow Procore to make changes to your device. *Note:* You will need Administrator rights to your computer.
4. Log into Procore with your Procore credentials.
5. Click **Install** next to the version you want to download. *Note:* The year of your NavisworksÂ® application and the Procore plugin should be the same.
6. Open the NavisworksÂ® application on your computer. A Procore tab will be viewable in NavisworksÂ®.

### Step 3: Publish a Model to Procore

See the full [Publish a Model to Procore](/product-manuals/models-project/tutorials/publish-a-model-to-procore) tutorial, or click below to view the video and steps:

**Show** **/Hide Video and Steps**

Follow the steps below to publish a model to Procore.

- Step 1: Launch the Procore Plugin in NavisworksÂ®
- Step 2: Select the Publish Action
- Step 3: Enter Model Information
- Step 4: Configure Viewpoints
- Step 5: Add a 2D Sheet
- Step 6: Map the 2D Sheet to the Model

### Step 1: Launch the Procore Plugin in NavisworksÂ®

1. In NavisworksÂ®, click the **Procore** tab to open the plugin ribbon.
2. Click **Publish** to open the Models window.

### Step 2: Select the Publish Action

In the Models window, choose one of the following options:

- **To publish a new model,** click **New Model**.
- **To publish a new version of an existing model**, hover over the model in the list and click **Publish Version**.

### Step 3: Enter Model Information

Enter information about the model as follows:

1. **Choose the appropriate option**:

   - **For a new model,** enter the name that will be displayed in Procore in the **Model Name** field.
   - **For an existing model,** keep the existing name.
2. **Select the Status of the model from the drop-down list**:

   - **Coordination.** For reference only. Not approved for construction.
   - **Construction.** Fully coordinated and approved for field installation and layout.
   - **As-Built.** Updated to reflect final, field-verified conditions.

### Step 4: Configure Viewpoints

#### Set the Home Viewpoint

The *Home Viewpoint* is the model's default starting view and thumbnail image. For best results and easy navigation, choose a clear, general overview of the project.

1. **Set the initial viewpoint**:

   1. In the viewer, navigate the model to your desired starting position.
   2. Click **Add**.
   3. Click **Save** to confirm.
2. ***Optional:*** **Update an existing viewpoint**:

   1. Navigate the model to the new position.
   2. Click **Edit**.
   3. Click **Save** to apply the changes.

#### Add Saved NavisworksÂ® Views (Optional)

You can upload specific viewpoints to make them available in Procore.

1. **Add a saved view:**

   1. Click **Add**.
   2. Mark the checkbox next to each view you want to upload.
   3. Click **Add** to confirm your selections.
2. ***Optional:*** **Remove a saved view:**

   1. Click the **delete (x)** icon next to the viewpoint.

### Step 5: Add a 2D Sheet

Use these steps to link a 2D drawing sheet to your 3D model by setting its location and elevation.

1. **Select the drawing sheet**:

   1. In the **2D Sheets** section, click **Add**.
   2. If your project uses drawing areas, you must first select an area from the **Drawing Area** drop-down list.
   3. Select your drawing from the **Drawing** drop-down list.
2. **Set the sheet's elevation**. This sets the vertical position of the sheet within the model:

   1. **To use an existing level**, select a predefined level from the **Level** drop-down list.
   2. **To set by model selection**, click directly on an element in the 3D model. The elevation will be calculated automatically based on the point you clicked.
   3. **To create a new leve**l, click **Create New** and enter the details for the new level.
3. **Proceed to the next step**:

   - After setting the elevation, click **Next**.
   - Now, you must map the sheet to the model. See Step 6: Map the 2D Sheet to the Model.

     ##### Â Important

     Before adding another 2D sheet, you must complete the mapping process for the current sheet and then repeat these steps.

### Step 6: Map the 2D Sheet to the Model

This step aligns the 2D drawing with the 3D model by asking you to select two common reference points on each.

1. **Select reference points on the 2D sheet**:

   1. Click **Start** to begin.
   2. Select two opposing reference points on the 2D drawing. The points will be labeled 'A' and 'B'.
   3. To re-select your points at any time, click **Clear**.
   4. When you are satisfied with your points, click **Done**.

      ##### Â Tip

      For the best accuracy, choose grid line intersections that are located within the main project footprint.

- **Select matching points on the 3D model**:  
   Now, you will select the same two points on the 3D model.

  1. Click **Start** to begin selecting points on the model.
  2. Select the same two reference points on the 3D model that correspond to points 'A' and 'B' from the drawing.
  3. Click **Save** to confirm the points.

     ##### Â Important

     The reference points selected in the 3D model must exist on the Z-axis (vertical plane). You cannot choose points on a flat floor or a 2D object. For precision, Procore recommends turning the NavisworksÂ® grid ON by selecting **View > Show Grid**.

#### Step 5: Publish the Model

Before finalizing the model, decide whether to process it using Procore's cloud servers (recommended) or your local computer.

##### Â Important

Use Section Boxes in NavisworksÂ® to publish specific areas or views of your model. See [Add a Section Box to a Model](/product-manuals/models-project/tutorials/add-a-section-box-to-a-model-in-navisworks). Section Planes are not supported and can't be published to Procore.

1. **Choose your publishing method**:

   1. **Cloud Publishing** (Default & Recommended)

      - **How**: Leave the **Publish Locally** checkbox cleared.
      - **Description**: This is the fastest method. Procore's servers do the heavy lifting, which frees up your computer. You can monitor the progress on the **Uploads** tab in the Procore BIM plugin.
   2. **Local Publishing**

      - **How**: Mark the **Publish** **Locally** checkbox.
      - **Description**: This option is significantly slower. Procore recommends using it when publishing a locked model file or when troubleshooting issues with the NavisworksÂ® Appearance Profiler.
2. **Finalize and view**:

   1. When ready, click **Publish**.
   2. After the model has successfully processed, a confirmation message will appear. Click **Done**.
   3. View your model in the Models tool on the Procore web or mobile app. See [View a Model (Web)](/process-guides/user-guide-publish-and-manage-models-from-the-documents-tool/view-models), [(iOS)](/product-manuals/models-ios/tutorials/view-models-ios), or [(Android)](/product-manuals/models-android/tutorials/view-models-android).
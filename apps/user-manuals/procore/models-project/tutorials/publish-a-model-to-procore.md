# Publish a NavisworksÂ® Model to Procore with the Procore BIM Plugin

Source: https://v2.support.procore.com/product-manuals/models-project/tutorials/publish-a-model-to-procore

---

## Background

Coordinated models are often stuck in the office, accessible only to BIM teams on desktop computers. Publishing models to a Procore project connects office staff with field personnel. This gives field teams mobile access to the models, helping them reduce installation errors and boost productivity.

##### Â Tip

You can also [publish models from the Documents tool](/process-guides/user-guide-publish-and-manage-models-from-the-documents-tool/publish-models).

## Things to Consider

- **Required User Permissions**: You need both:

  - **Models (Project)**: 'Admin' permissions
  - **Drawings (Project)**: 'Read Only' permissions higher (required to add and map 2D drawings)
- **Additional Information**:

  - **File Format**: You can only publish .NWD or .NWF files from NavisworksÂ®.
  - **File Size**: Model files uploaded via the Procore BIM Plugin must not exceed 5GB.

## Prerequisites

- Ensure you've installed the following on a WindowsÂ® computer:

  - AutodeskÂ® NavisworksÂ®
  - Procore BIM Plugin
- Apply a 'Section Box' to your model before publishing. NavisworksÂ® Section Planes are not supported for publishing because they lack the defined boundary required by Procore.

## Steps

### Set Up the Model Information and Preferences

1. Open your model in NavisworksÂ®.
2. Click the **Procore** tab to use the Procore BIM Plugin.
3. Click **Publish** to open the Models window.
4. In the Models window, choose one option:

   - **Publish a new model**: Click **New Model**.
   - **Publish new version of an existing model:** Hover over the model in the list and click **Publish Version**.
5. Enter information about the model as follows:

   - **For a new model:** Enter the **Model Name**.
   - **For an existing model**: Keep the existing name.
6. Select the model's **Status** from the list:

   - **Coordination**: For reference only. Not approved for construction.
   - **Construction**: Fully coordinated and approved for field installation and layout.
   - **As-Built**: Updated to reflect final, field-verified conditions.
7. Select the **Automatic Revisions** box to automatically publish a new revision when a new version is updated.
8. Set your 2D mapping:

   - **Map Drawings**: Click **Next**. This is a required step.
   - **Publish**: Click **Save Changes**.

### Set the Viewpoints

1. Set the **Home Viewpoint**. This is the model's default starting view and thumbnail image. For best results and easy navigation, choose a clear, general overview of the project.
2. Set the initial viewpoint:

   1. In the viewer, navigate the model to your desired starting position.
   2. Click **Add**.
   3. Click **Save** to confirm.
3. *Optional:* Update an existing viewpoint:

   1. Navigate the model to the new position.
   2. Click **Edit**.
   3. Click **Save** to apply the changes.
4. *Optional:* Add or remove any saved views from NavisworksÂ® to make them available in Procore:

   1. **Add a saved view:**

      1. Click **Add**.
      2. Mark the checkbox next to each view you want to upload.
      3. Click **Add** to confirm your selections.
   2. ***Optional:*** **Remove a saved view:**

      1. Click the **delete (x)** icon next to the viewpoint.

### Add and Map a 2D Sheet

1. Add a 2D Sheet:

   1. On the **Map Drawings to Model** screen, make a selection from the dropdown menu for each of the following required fields:

      - **Level.** Select a location level from the drop-down menu.
      - **Drawing Area.** Select a drawing area from the drop-down menu.
      - **Drawings.** Select the relevant drawing(s).
2. Click **Next.**
3. Map the 2D Sheet to the Model to align aligns the 2D drawing with the 3D model with reference points.

   1. Select reference points on the 3D model:

      1. Click **Map Model** to begin.
      2. Select two reference points on the 3D model. The points will be labeled 'A' and 'B'.
      3. To clear the selected points, click **Reset All**.
      4. When satisfied with the points, click **Save**.
   2. Select matching points on the 2D drawing(s):

      1. Click **Map Drawings** to begin selecting points on the drawing(s).
      2. Select the same two reference points on the 2D drawing that correspond to points 'A' and 'B' from the model.

         - The rest of the selected drawings will be automatically mapped   
           *Note:* Reference points are saved automatically, but reviewing the drawing turns the checkmark blue.
      3. To clear your selected points, click **Reset All**.
      4. To clear the selected points on one drawing, select the drawing and click **Reset Mapping**.
      5. Click **Save** to confirm the points.
   3. Click **Done Mapping** when finished.
   4. Click **Save Changes**.

#### Publish the Model

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
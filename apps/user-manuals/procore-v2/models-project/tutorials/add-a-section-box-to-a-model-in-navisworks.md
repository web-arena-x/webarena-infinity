# Add a Section Box to a Model in NavisworksÂ®

Source: https://v2.support.procore.com/product-manuals/models-project/tutorials/add-a-section-box-to-a-model-in-navisworks

---

## Background

Procore recommends applying a 'Section Box' to your NavisworksÂ® model prior to publishing. Unlike a NavisworksÂ® 'Section Plane', a 'Section Box' provides a defined boundary that allows Procore to calculate the camera view center, optimizing web performance on mobile devices. This action is important because it helps to prevent rendering issues, especially on models using a 'Shared' or 'World' coordinate system.

## Things to Consider

- [Required User Permissions](/product-manuals/models-project/permissions)

## Prerequisites

- Ensure you've installed the following on a WindowsÂ® computer:

  - AutodeskÂ® NavisworksÂ®
  - Procore BIM Plugin
- Apply a 'Section Box' to your model before publishing. NavisworksÂ® Section Planes are not published to Procore.

## Steps

#### Configure the Section Box in NavisworksÂ®

1. Open your model in NavisworksÂ®.
2. Click the **Viewpoint** tab and select **Enable Sectioning**.
3. Click **Mode** and select **Box**.
4. Define the box's boundaries using one of these methods:

   - **Manual Adjustment**: Use the **Scale**, **Move**, and **Rotate** tools to manually fit the box around the specific portion of the model you want to publish.
   - **Fit Selection**: Select an item (or multiple items) in the Selection Tree (i.e., Architectural or Structure models are usually good options). Click the **Fit Selection** button to automatically snap the box to that specific geometry.
5. Save the section box:

   1. Right-click and select **Save Viewpoint**.
   2. Name it as you want.

#### Link to Home View & Publish to Procore

Once the Section Box is configured on your model, do the following:

1. In the Procore BIM Plugin while setting the **Home View**:

   1. If setting up a new view, click **Add**.
   2. If updating an existing model version, click **Edit**.
2. Click **Save** to link the Section Box to the Home View.
3. Ensure the following:

   - All the required model information fields are complete.
   - The Section Box is visible.
4. Continue with [Publish a Model to Procore](/product-manuals/models-project/tutorials/publish-a-model-to-procore).
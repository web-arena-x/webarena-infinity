# Create or Link Coordination Issues on a Drawing (iOS)

Source: https://v2.support.procore.com/product-manuals/drawings-ios/tutorials/create-or-link-coordination-issues-on-a-drawing-ios

---

## Background

When adding markups to a drawing in a project's Drawings tool, you can choose to link to existing coordination issues, or create new ones. Coordination issues can be added directly to pin markups, or linked to other markup types such as Cloud, Text, and Arrow.

## Things to Consider

- **Required User Permissions:**

 - *To add markups to the Personal layer:*

    - 'Read Only' or higher permissions on the project's Drawings tool.
 - *To publish markups to the Published layer:*

    - 'Standard' or 'Admin' permissions on the project's Drawings tool. See [What is the difference between personal and published markups?](/faq-what-is-the-difference-between-personal-and-published-drawing-markups)
 - *To create new coordination issues on a drawing:*

    - 'Standard' or 'Admin' permissions on the project's Coordination Issues AND Drawings tools.
- **Additional Information:**

 - In order to link a coordination issue to a drawing, the Coordination Issues tool must be enabled for the company's account and active on the project. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).   
    *Note:* The Coordination Issues tool is part of Procore's [Design Coordination](https://www.procore.com/project-management/coordination-issues) product. Please reach out to your Procore point of contact for additional information.
 - After publishing a new coordination issue markup on a drawing, a snapshot of the area of the drawing is added to the coordination issue, and the drawing is added to the 'Links' section of the coordination issue. This allows users to easily reference the original drawing when viewing the coordination issue from the Coordination Issues tool.

## Steps

1. Open the **Procore** app on an iOS mobile device.
2. Tap the project's **Drawings** tool.
3. Locate and open the drawing you want to add a coordination issue to.   
    You can create or link coordination issues from multiple markup types. See the steps below:

#### To create or link coordination issues on pin markups:

1. In the markup toolbar, tap the **Pin** markup tool and select **Issue**.
2. Tap the area of the drawing you want to pin a coordination issue to.
3. Choose whether you want to link to an existing coordination issue or create a new one:

   - **To link to an existing coordination issue:**

     1. Tap **Link Existing**.
     2. Tap the issue you want to link to. To search or filter for coordination issues, see [Search for and Filter Coordination Issues (iOS)](/product-manuals/coordination-issues-ios/tutorials/search-for-and-filter-coordination-issues-ios). 
        *Note:* The coordination issue is automatically added to the drawing.
   - **To create a new coordination issue:**

     1. Tap **New Coordination Issue**.
     2. Enter the necessary information for the coordination issue. See [Create Coordination Issues (iOS)](/product-manuals/models-ios/tutorials/create-coordination-issues-from-a-model-ios).
     3. Tap **Create & Publish**. 
        *Note:* The coordination issue is automatically added. If you are working in offline mode, the new coordination issue will be labeled as 'New Item' on the drawing until the issue is uploaded and a number is assigned.
4. If you want others to be able to see the coordination issue markup on the drawing, select the markup and tap **Publish**. See [Publish Personal Drawing Markups (iOS)](/product-manuals/drawings-ios/tutorials/publish-personal-drawing-markups-ios).

#### To create or link coordination issues on other markups:

1. Tap the markup tool that you want to use for your markup. See [Mark Up a Drawing (iOS)](/product-manuals/drawings-ios/tutorials/mark-up-a-drawing-ios).
2. Add your markup to the relevant area of the drawing.
3. Tap **Link** and select **Link a Coordination Issue**.
4. Choose whether you want to link to an existing coordination issue or create a new one:

   - **To link to an existing coordination issue:**

     - Tap the issue you want to link to.
   - **To create a new coordination issue:**

     1. Tap the **create** icon.
     2. Enter the necessary information for the coordination issue. See [Create Coordination Issues (iOS)](/product-manuals/models-ios/tutorials/create-coordination-issues-from-a-model-ios).
     3. Click **Create**.
5. If you want others to be able to see the coordination issue markup on the drawing, select the markup and tap **Publish**. See [Publish Personal Drawing Markups (iOS)](/product-manuals/drawings-ios/tutorials/publish-personal-drawing-markups-ios).
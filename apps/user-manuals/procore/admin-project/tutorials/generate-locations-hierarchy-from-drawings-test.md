# Generate Locations Hierarchy from Drawings Test

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/generate-locations-hierarchy-from-drawings-test

---

## Background

Often, a list of locations for a project is tiered. Tiered locations give users the ability to link different Procore objects (e.g., RFIs, Submittals, and more) to specific locations on a job site. This helps project team members to pinpoint the exact location(s) on a job site where a defect was observed, where equipment will be installed, or where a project change order occurred.

##### Examples

Let's say your project includes the construction of a parking lot. You might use a location structure like this:

Parking Lot A > Ground Floor > EastParking Lot A > Ground Floor > WestParking Lot A > Level Two > EastParking Lot A > Level Two > West

Procore's Locations feature allows you to automatically generate this list from your project's architectural drawings.

## Before you Begin

- [Required User Permissions](/product-manuals/admin-project/permissions)
- **Additional Information**:

 - If you initially manually created your locations in the Admin tool, you would need to delete them to instead generate your locations from Drawings.
 - You can only generate locations from drawings where the drawing discipline is set to 'Architectural'. See [Configure Default Drawing Disciplines](/product-manuals/drawings-project/tutorials/configure-default-drawing-disciplines)
 - The colors next to the locations indicate the confidence level in creating the location from the drawing. Green indicates the highest level of confidence.
 - Tiers are named based on the following information:

    - Tier 0 is the name of the project.
    - Tier 1 is the drawing name.
    - Tier 2 is the location on the drawing.
- **Limitations**

 - This feature does not currently support projects that have a single drawing sheet that represents multiple floors on the project. If a project has typical floors, do NOT generate locations from drawings.

## Steps

- [Generate from the Admin Tool](#:~:text=navigate to the projectâs admin tool)
- Generate from the Drawings Tool

### Generate Drawings Hierarchy from the Admin Tool

1. Navigate to the project's **Admin** tool.
2. Under the 'Project Settings' menu, click **Locations.**
3. Click **Create Location Hierarchy**.
4. Select the drawings you want to use to create your list of locations.
5. Click **Submit for Extraction**. 
   A tile appears in the side menu panel to show the progress of your location extraction.
6. If prompted, click **Review Drawings.** *Note:* This feature was built to extract locations for Architectural floor plans. If you want to create locations for Architectural drawings without a floor plan, keep the checkbox marked for the drawing, and Procore will generate a placeholder parent location for you to manually manage locations and boundaries.

   1. Clear the checkbox for drawings you wish to NOT extract locations.
   2. Click **Continue Location Extraction**.
7. Once processing is complete, click **Review Locations.**

   Locations are listed alongside an image of the associated drawing.
8. Optional: Modify the boundaries if needed.

   1. by clicking the **vertical ellipsis**.
   2. Click **Edit**, and select **Boundary**.
   3. Click and drag the points around the boundary to reconfigure it.
9. After review, click **Save as Draft** or **Publish Locations.**

### Generate Drawings Hierarchy from the Drawings Tool

1. Navigate to the project's
2. **Drawings** tool.
3. Click **Create Locations**.
4. Select the drawings you want to use to create your list of locations.
5. Click **Submit for Extraction**. 
   A tile appears in the side menu panel to show the progress of your location extraction.
6. If prompted, click **Review Drawings.** *Note:* This feature was built to extract locations for Architectural floor plans. If you want to create locations for Architectural drawings without a floor plan, keep the checkbox marked for the drawing, and Procore will generate a placeholder parent location for you to manually manage locations and boundaries.

   1. Clear the checkbox for drawings you wish to NOT extract locations.
   2. Click **Continue Location Extraction**.
7. Once processing is complete, click **Review Locations.** Locations are listed alongside an image of the associated drawing.
8. Optional: Modify the boundaries if needed.

   1. Click the **vertical ellipsis.**
   2. Click **Edit**, and select **Boundary**.
   3. Click and drag the points around the boundary to reconfigure it.
9. After review, click **Save as Draft** or **Publish Locations**.
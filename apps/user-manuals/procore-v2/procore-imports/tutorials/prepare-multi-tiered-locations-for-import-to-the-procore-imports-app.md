# Prepare Multi-Tiered Locations for Import to the Procore Imports App

Source: https://v2.support.procore.com/product-manuals/procore-imports/tutorials/prepare-multi-tiered-locations-for-import-to-the-procore-imports-app

---

## Background

You can use the Procore Imports App to self-import your multi-tiered locations in bulk to your project's Admin tool. This will add up to six-tiered locations to your project in Procore. If you need to add more tiers, they can be created manually. For additional information, see [What are multi-tiered locations?](/faq-what-are-multi-tiered-locations)

## Things to Consider

- **Required User Permission**:

  - 'Admin' level permission on the project's Admin tool.  
    *Note*: Granular Permissions are not supported in the Procore Imports application.
- **Additional Information:**

  - Procore's multi-tiered locations feature does not integrate with any location-related custom segment segments that you create for [Work Breakdown Structure](https://support.procore.com/products/online/work-breakdown-structure).

## Steps

- Download the Multi-Tiered Locations Import Template
- Format the Multi-Tiered Locations Import Template

#### Download the Multi-Tiered Locations Import Template

- Download the Locations Import Template: [import-locations.xlsx](https://procore-imports-templates.s3.amazonaws.com/import%5Ftemplate%5Flocations.xlsx)

#### Format the Multi-Tiered Locations Import Template

1. See the considerations below for filling out the template.

   - Make sure you begin with the first tier, then add the first tier with the second tier, and then add the first tier with the second tier and the third tier, etc.
   - Make sure there are no blank rows.
   - Check for special/hidden characters. Many users will copy/paste their information from Microsoft Word into Excel. The interpretation of the symbols listed below are different between the two applications and will cause import errors. It's important to correct any incorrect symbols before importing. Hidden characters can be found and corrected (in most cases) by copying all data, pasting the text into Notepad, and then copying from Notepad and pasting it into the .xlsx or CSV. Be sure to note the correct placement of the information.

     - , (comma)
     - - (dash)
     - / (dash)
     - 1/2 (forward slash)
     - " (double quote)
     - ' (single quote)
     - ` (grave accent)
     - ***Important***: Do not include ">" in any one tier's location title (e.g. "Floor>1" or "Floor 1>bathroom"). These tiers will be translated as tier separator and will cause the import to fail.
2. Complete the import template.

   - You must work from largest to smallest when creating your locations. Start with the first tier location (example "Building 1") and then add each sub-location until each tier is written out (e.g. "Floor 1, Unit 101, Master Bedroom"). See the image below of the recommended order.

## Next Steps

- [Import Locations into your Project Level Admin Tool (Procore Imports)](/product-manuals/procore-imports/tutorials/import-locations-into-your-project-level-admin-tool-procore-imports)
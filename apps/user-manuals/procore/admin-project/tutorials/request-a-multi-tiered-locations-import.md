# Request a Multi-tiered Locations Import

Source: https://v2.support.procore.com/product-manuals/admin-project/tutorials/request-a-multi-tiered-locations-import

---

***IMPORTANT!*** In order to protect the integrity of your companyâs data, Procore Employees are restricted from modifying the data that clients submit in all Procore Import Templates. This restriction applies to all data modifications, including correcting typographical errors. If Procore determines that errors are present in any Procore Import Template that you submit to Procore, it will be returned to you for correction. **Please note that the import process may take up to 72 hours to process.**

## Background

At the beginning of a project, you can perform your own or request your locations hierarchy be bulk-added to the Admin tool of your project. This will add as many multi-tiered locations to your project as you need without having to manually add each location and sub-location in Procore.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Project level Admin tool.
- **Additional Information:**

 - There is no way to undo this import. Please carefully review your data before submitting your import request to Procore.
 - Imports can only be used to add locations. Your import will not edit or delete existing locations in your project.   
    *Note:* Once your locations have been successfully imported into Procore, you can make modifications to a location in the Procore application. See [Edit Tiered Locations](/product-manuals/admin-project/tutorials/edit-multi-tiered-locations).
 - Any duplicates on your import will be ignored.
 - You can expedite the import process by performing your own location import using the Procore Imports app. See [Import Locations into your Project Level Admin Tool (Procore Imports)](/product-manuals/procore-imports/tutorials/import-locations-into-your-project-level-admin-tool-procore-imports) for more information.

## Steps

1. Download the import template: [import-locations.xlsx](https://procore-imports-templates.s3.amazonaws.com/import%5Ftemplate%5Flocations.xlsx). 
   *Note*: You can also download the template from the Project level Admin tool's Locations page under Project Settings in the Procore web application.
2. Complete the import template.

   - You must work from largest to smallest when creating your locations. Start with the first tier location (for example, "Building 1") and then add each sub-location until each tier is written out (for example, "Floor 1, Unit 101, Master Bedroom"). See the image below of the recommended order.
3. See the below considerations when filling out the template.

   - Make sure you begin with the first tier, then add the first tier with the second tier, and then add the first tier with the second tier and the third tier, etc.
   - Make sure there are no blank rows.
   - Make sure no additional empty columns were added. More tiers columns can be added with headers, but no columns can be completely blank to the right or left.
   - Check for special/hidden characters. Many users will copy/paste their information from Microsoft Word into Excel. The interpretation of the symbols listed below are different between the two applications and will cause import errors. It's important to correct any incorrect symbols before importing. Hidden characters can be found and corrected (in most cases) by copying all data, pasting the text into Notepad, and then copying from Notepad and pasting it into the .xlsx. Be sure to note the correct placement of the information.

     - , (comma)
     - - (dash)
     - / (dash)
     - 1/2 (forward slash)
     - " (double quote)
     - ' (single quote)
     - ` (grave accent)
     - ***Important***: Do not include ">" in any one tier's location title (for example, "Floor>1" or "Floor 1>bathroom"). These tiers will be translated as tier separator and will cause the import to fail.
4. After you fill out the import template according to the considerations above, send your import file to your Procore point of contact or [imports@procore.com](mailto:imports@procore.com). When that person is done reviewing, they will contact you to have you verify that everything is to your liking.

## Next Steps

- [Edit Multi-tiered Locations](/product-manuals/admin-project/tutorials/edit-multi-tiered-locations)
# Import Coordination Issues from a BCF File

Source: https://v2.support.procore.com/product-manuals/coordination-issues-project/tutorials/import-coordination-issues-from-a-bcf-file

---

## Background

If you have BCF files containing coordination issues, you can import them all at once to the Coordination Issues tool so you don't have to create them manually.

## Things to Consider

- **Required User Permissions:**

 - 'Standard' or 'Admin' level permissions on the project's Coordination Issues tool.

## Prerequisites

- To import issues, you must export a BCF file (.bcf) from our source software tool.
- Before starting an import, read [How can I prevent BCF import errors when using the Coordination Issues tool?](/faq-how-can-i-prevent-import-errors-when-using-the-coordination-issues-tool)

## Steps

1. Navigate to the project's **Coordination Issues** tool on [app.procore.com](http://app.procore.com/).
2. At the top of the page, click **Import**.
3. Select the BCF file from your computer that you want to import issues from.
4. If the project uses the Models tool, you can choose to associate the issues with a specific model. Otherwise, click **Skip**. 
   *Note:* Associating issues with a model will allow you to quickly open the issue in Procore's model viewer directly from a coordination issue (explained further in Step 6).
5. An 'Import in Progress' banner shows at the top of the page, and you'll receive an email when all issues have finished importing.
6. To view the issues that were created from the import, add the **Created From** filter to the list and select the BCF file that you imported. See [Search for and Filter Coordination Issues](/process-guides/getting-started-guide-documents-plugin-for-autodesk/search-and-filter-coordination-issues).

   - Click on an issue to view its details in the side panel.
   - If an issue was associated with a model during import, you can hover over the model image and click **View** to open the issue in Procore's model viewer.
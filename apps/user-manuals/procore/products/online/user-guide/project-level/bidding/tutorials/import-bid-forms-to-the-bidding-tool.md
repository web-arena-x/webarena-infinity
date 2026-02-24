# Import Bid Forms to the Bidding Tool - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/import-bid-forms-to-the-bidding-tool

---

##### Note

The content below describes functionality that is part of the new *Bid Management Enhanced Experience*. See [About Bid Management Enhanced Experience](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/about-bid-management-enhanced-experience "About Bid Management Enhanced Experience").

## Objective

To create bid forms from a CSV file import.

## Background

In addition to [creating a bid form](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/create-a-bid-form "Create a Bid Form") in the Bidding tool, you can also download a CSV template to fill out and import the information. With a CSV import, you can create multiple bid forms at once.

## Things to Consider

- **Required User Permissions:**
 - 'Admin' level permissions on the project's Bidding tool.
- **Additional Information**:
 - You can import and create multiple bid forms at a time from the same CSV file.
 - The following requirements exist for the template:
    - The Bid Form Name must be filled out for each line item. Bid form names cannot be duplicated.
    - A line item can only have a Cost Code or Subject filled out, not both.
    - Cost codes must match the cost codes in the project.
 - If you edit the CSV template in a text editor and need to separate values, use either commas or semicolons. Most CSV files use commas by default.
 - The bid form will not import if errors are detected, and a banner will list details of what prevented the import. After you correct the issues and save the template file on your computer, you can upload again.

## Prerequisites

- [Create a Bid Package](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/create-a-bid-package "Create a Bid Package")

## Steps

1. Navigate to the project's **Bidding** tool.
2. Open a bid package.
3. If there are no bid forms in the bid package yet, click **Create Bid Form** on the Bidding tab.  
   OR If at least one bid form exists, click **View Bid Forms** and then click **Create Bid Form**.
4. On the **Create Bid Form** menu, select **From CSV**.
5. Click **Download CSV Template** and select one of the following options:
   - **Blank Template**: The template file will be blank except for column headers.
   - **Template with Cost Codes**: The template will contain column headers and line items for every cost code in the project.
6. Open the CSV file on your computer and fill out the template as necessary: 
   *Note:* The only required column is Bid Form Name, since there could be times when you want to create new bid forms without line items. If you want to add line items, fill out the other columns listed below.    
   ![bid-template.png](https://support.procore.com/@api/deki/files/535857/bid-template.png?revision=1&size=bestfit&width=1100)
   - **Bid Form Name**: Enter the name of a bid form you want to create.
   - **Item Type**: Enter 'Base Bid' or 'Alternates' to specify which section a line item should be listed under.
   - **Section**: Enter the name of the section.
   - **Cost Code**: If the line item has a cost code associated with it, enter the cost code (example: 03-100 - Concrete). Otherwise, leave this blank and go to the Subject column. Cost codes must match the cost codes that exist in the project.
   - **Subject**: If the line item doesn't need a cost code, enter a subject for the line item (example: Concrete Refinishing). If it does need a cost code, leave this blank and go to the Cost Code column.
   - **Description**: Enter a description of the line item.
   - **Response Field Type**: Enter a response type (Amount, Include/Exclude, or Unit & Quantity) for each line item.  
     *Note:*
     - All three response types can be used for Base Bid items, but 'Include/Exclude' is not allowed for Alternates.
     - When entering values, the spacing must match the example text in the Response Field Type column header. For example:
       - 'Unit & Quantity' instead of 'Unit&Quantity'
       - 'Include/Exclude' instead of 'Include / Exclude'
7. When you are finished filling out the template, save the CSV file and return to the 'Create Bid Forms from CSV' window in Procore.
8. Under 'Select CSV Delimiter', select the type of character that you used to separate values in the template: 
   *Note:* This only applies if you edited the CSV file in a text editor.
   - **Comma** (,)
   - **Semicolon** (;)
9. In the 'CSV File' section, click **Upload File**, or drag and drop the file over.
10. When you are ready to import the file, click **Create**.
    - If the import is successful, the bid form(s) will be created automatically in the Bidding tool.
    - If errors are detected, a banner will appear with details of what prevented the import. After you correct the issues and save the template file on your computer, you can upload again.

## See Also

- [Create a Bid Form](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/create-a-bid-form "Create a Bid Form")
- [Preview a Bid Form](https://support.procore.com/products/online/user-guide/project-level/bidding/tutorials/preview-a-bid-form "Preview a Bid Form")
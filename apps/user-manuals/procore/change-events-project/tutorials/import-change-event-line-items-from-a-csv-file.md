# Import Change Event Line Items from a CSV File

Source: https://v2.support.procore.com/product-manuals/change-events-project/tutorials/import-change-event-line-items-from-a-csv-file

---

## Background

To save time from manually adding line items to a change event, you can download a CSV file from your project, add your line items to that file, and then import it into Procore.

## Things to Consider

- **Required User Permissions:**

 - 'Standard' level permission or higher on the project's Change Events tool.

## Steps

- Download the Schedule of Values CSV Template
- Add Line Items to the CSV Template
- Upload the Completed CSV Template to Procore

#### Download the Schedule of Values CSV Template

1. Create a new change event or edit an existing change event.
2. Click **Import Line Items from CSV** at the bottom of the 'Line Items' card.
3. Click **Download Blank CSV Template**.

After completing the steps above, continue with Add Line Items to the CSV Template.

#### Add Line Items to the CSV Template

1. Open the CSV template that you downloaded.   
   *Note:* The Sub Job, Cost Code, and Cost Type fields will be pre-populated with the budget code segments that are currently in use on your project. These fields are *required*.
2. Complete the following fields on the import template for each line you want to import: 
   *Note:* Only lines with amounts entered into at least one of the following columns will be imported.

   - **Description.** Enter a description for the line item(s).
   - **Vendor.** Enter the name of the company associated with the line item as it is entered in the project's Directory.
   - **Contract.** Enter the contract number and title. 
     *Note:* The required format for this field is "#'Contract Number': 'Contract Title'". For example, a contract with a number of 'SC--001' and a title of 'Test Contract' is entered as "#SC--001: Test Contract".
   - **Revenue Quantity.** Enter the unit quantity for the Revenue line item(s).
   - **Revenue Unit Cost.** Enter the unit quantity for the line item(s).
   - **Revenue ROM.** Enter the Revenue ROM amount for the line item(s).
   - **Quantity.** Enter the unit quantity for the line item(s).
   - **Unit of Measure.** Enter the unit of measure (UOM) for the line item(s) (Case Sensitive).
   - **Unit Cost.** Enter the unit cost value for the line item(s).

After completing the steps above, continue with Import the Completed CSV Template to Procore.

#### Import the Completed CSV Template to Procore

1. Click **Import Line Items from CSV**.
2. Click **Upload File** and select your completed template or drag and drop the file into the 'Drag & Drop' box. 
   *Note:* If there are any errors in the template a banner will appear preventing you from importing. To review the errors, click **Show Errors** and make the necessary corrections to the template.
3. Click **Import**.   
   *Note:* Clicking 'Import' will complete the creation process for the change event. The change event line items' revenue ROM setting will be applied based on the scope that is chosen for the change event before importing.
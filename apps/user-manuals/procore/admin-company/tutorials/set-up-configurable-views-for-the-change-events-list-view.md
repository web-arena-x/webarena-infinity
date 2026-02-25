# Set up Configurable Views for the Change Events Line Items View

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/set-up-configurable-views-for-the-change-events-list-view

---

## Background

The default views in the Change Events tool list view are 'Classic Detail', 'Classic Summary', 'Complete View', 'Owner's View' and 'Scope View'. Each view consists of a different arrangement and grouping of columns designed to present the data in the tool in a specific way. A *configurable view* is created and configured by Procore users when the desired column arrangement for the Change Events tool is not met by the existing default views. Creating configurable views allows users to customize the list view of the Change Events tool with the columns of their choice and save the view so it can be standardized across Procore projects.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information:**

 - Newly created views are automatically applied to all projects.
 - Newly created views are set to 'Hidden' until they are published. See Change the Status of a Configurable Change Events View.
 - Custom Fields are NOT supported by configurable views.

## Steps

### Create a New View

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click **Change Management**.
3. Click the **Configurable Views** tab.
4. Click **Create View**. 
   *Note: To edit an existing view, click the title of the view in on the Configurable Views page.*
5. Enter a name and description for the view.
6. *Optional:* Select a project from your company to preview the new view with up to 25 rows of data.
7. *Optional:* Choose an existing view to use as a template for creating the new view. The new view will automatically be populated with the columns from the selected existing view.
8. Click **Configure View** to begin configuring the new view.
9. Click the configuration icon to view the list of available columns to add to the view.
10. Toggle the switches on to include a column in the view.

### Configure Columns

Click the 'Table Settings' icon to open the menu for row height and column configurations.

- **Row Height**:

 - Choose between small, medium, and large row height for the change events list view.
- **Configure Columns:**

 - Use the toggle switch to determine which columns will be displayed or hidden from the change events list-view.
 - Clicking **Reset To Default** will set all columns to display.

Click and drag column titles to move their position in the table to the left or right.

Click the vertical ellipsis when hovering over a column header/title to open additional column settings:

- Group By
- Pin Column

 - Pin Left
 - Pin Right
- Autosize This Column
- Autosize All Columns
- Reset Columns

### View Line Items

The Line Items card on an individual change event lets you perform different viewing and editing functions. To learn about your options, see [(Beta) View the Change Events Line Items View](/product-manuals/change-events-project/tutorials/view-the-change-events-line-items-view).

#### Change Event Data Columns

##### Change Event General Information - **Number** Shows the change event number that was assigned at creation. Number - **Title** Shows the title of the change event. Title - **CE Number - Title** The change event number and title combined. CE Number - Title - **Status** Show the current status of the change event. To learn about Procore's default statuses, see [What are the default statuses for change events in Procore?](/faq-what-are-the-default-statuses-for-change-events-in-procore) Status - **Scope** Shows the following scope options: *In Scope*, *Out of Scope*, or *TBD*. See [What are the default scope options for change events in Procore?](/faq-what-are-the-default-scope-options-for-change-events-in-procore) Scope - **Type** Shows the type associated with the change event: *TBD*, *Allowance*, *Contingency*, *Owner Change*, or *Transfer* to indicate the type of cost you are preparing for. See [Set the Default Change Management Configurations](/product-manuals/admin-company/tutorials/set-the-default-change-management-configurations). Type - **Change Reason** Shows the reason associated with the change. See [Set the Default Change Management Configurations](/product-manuals/admin-company/tutorials/set-the-default-change-management-configurations). Change Reason - **Origin** Shows a link to the item in a Procore project tool from which the change event originated. See [Which Procore tools can I use to create a change event?](/faq-which-procore-tools-can-i-use-to-create-a-change-event) Origin - **Date Created** The date the change event was created. Date Created - **Created By** The name of the user who created the change event. Created By

##### Change Event Detail - **Item Type** Shows the type associated with the line item: *Line Item, or Markup.* Item Type - **Budget Code** Select a budget code or click **Create Budget Code**. See [What is a budget code in Procore's WBS?](/faq-what-is-a-budget-code-in-procores-wbs) Budget Codes - **Description** Enter a description for the line item. Description - **Vendor**. Select the vendor's company name from the drop-down menu. See [Add a Company to the Project Directory](/process-guides/set-up-a-project-directory/create-companies). Vendor - **Contract** Select the impacted purchase order or subcontract from the drop-down menu. See [Create a Purchase Order](/product-manuals/commitments-project/tutorials/create-a-purchase-order) or [Create a Subcontract](/product-manuals/commitments-project/tutorials/create-a-subcontract). Contract - **Unit of Measure** The unit of measure selected for the change event line item. See [Which units of measure are included on Procore's master list?](/faq-which-units-of-measure-are-included-in-procores-master-list) Unit of Measure

##### Production - **Unit of Measure** The unit of measure selected for the measurable amount of work installed on the project that is associated with the change event line item. Unit of Measure - **Quantity** The number of the chosen units of measure associated with the measurable amount of work installed on the project that is associated with the change event line item. Quantity

##### Revenue - **Quantity** The number of the chosen units of measure associated with the revenue of the change event line item. Quantity - **Unit Cost** The value assigned to each unit associated with the revenue of change event line item. Unit Cost - **Revenue ROM** The rough order of magnitude (ROM) is the preliminary revenue value assigned to the change event line item. Revenue ROM - **Prime/Prime PCO** The value of the prime change order SOV line item connected to the change event line item. Prime/Prime PCO - **Prime PCO Title** The title of the change order or potential change order connected to the change event line item. Prime PCO Title - **Latest Price** The most up to date value associated with the revenue of the change event line item. Latest Price

##### Cost - **Quantity** The number of the chosen units of measure associated with the cost of the line item. Quantity - **Unit Cost** The value assigned to each unit associated with the cost change event line item. Unit Cost - **Cost ROM** The rough order of magnitude (ROM) is the preliminary cost value assigned to the change event line item. Cost ROM - **Request for Quote** The value of a returned RFQ associated with the change event line item. Request for Quote - **RFQ Title** The title of an RFQ associated with the change event line item. RFQ Title - **Commitment/Commitment CO/PCO** The value of the commitment or commitment change order SOV line item connected to the change event line item. Commitment/Commitment CO/PCO - **Commitment Title** The title of the of the contract or change order connected to the change event line item. Commitment Title - **Latest Cost** The most up to date value associated with the cost of the change event line item. Latest Cost - **Over/Under** The difference between the 'Latest Price' and the 'Latest Cost'. Over/Under

##### Budget - **Quantity** The number of the chosen units of measure associated with the budget of the change event line item. Quantity - **Unit Cost** The value assigned to each unit associated with the budget of the change event line item. Unit Cost - **Budget ROM** The rough order of magnitude (ROM) is the preliminary value assigned to a budget change connected to the change event line item. Budget ROM - **Budget Change** The value of the budget change connected to the change event line item. Budget Change - **Latest Budget Impact** The most up to date value for the budget impact of the change event line item. The value will match the Budget ROM column or the Budget Change column if there is a value. Latest Budget Impact

### Filter and Sort the Line Items View

#### Filtering

Click the **Filters** at the top of the change events table.

Select from the following filters:

- Status
- Scope
- Type
- Change Reason

#### Sorting

Click the title of a column to change its sorting behavior.*Example: Change the sorting order of the 'Status' column so Open Change events are listed first.*

### Grouping Columns

Column grouping allows you to better organize the Change Events line items table, especially when it comes to evaluating financial risk in your project. Specify which columns you would like to group and items within that group will roll-up underneath.

To group columns, click the **Select Group** selector at the top of the change events table and select the columns you want to group together.

If more than one grouping is selected, they can be rearranged within the 'Group By' Selector by clicking and dragging them into the preferred order. A grouping can be deleted by clicking the 'x' on the right side of the group.

Groupings can be reset by clicking **Reset** at the bottom of the selector.

### Change the Status of a Configurable Change Events View

The status of individual configurable views can be toggled between **Published** and **Hidden**. Published views are available for use on their assigned projects and hidden views are not available for use. The hidden status is useful for when a configurable view is in creation but not ready to be implemented.

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click **Change Management**.
3. Click the **Configurable Views** tab.
4. Click the **Status** column in the row of the view being changed.

### Duplicate or Delete a View

Configurable views can be duplicated to make building a new view easier. Duplicating a view creates a new view that is an exact copy of the existing view. Deleting a view removes the view permanently.*Note: Deleted views are* ***NOT*** *recoverable. Procore's default views cannot be deleted.*

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings', click **Change Management**.
3. Click the **Configurable Views** tab.
4. Click the ellipsis icon in the row of the view being changed.
5. Click **Duplicate** or **Delete**.
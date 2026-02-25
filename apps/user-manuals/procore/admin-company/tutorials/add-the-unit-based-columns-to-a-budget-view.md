# Add the Unit-Based Columns to a Procore Budget View

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/add-the-unit-based-columns-to-a-budget-view

---

## Background

The following source columns can be added to non-ERP Standard Budget views, enabling their use in **calculated columns:**

- **Standard Budget Columns** Before you can track productivity on your budget, you must first set up three columns on the budget view that you want to use:

 - Unit Cost
 - Budgeted Production 

    In Procore, a *Unit of Measure (UOM)* can be created to express these quantities for use with Procore's Financial Management tools: time, amount, length, area, volume, or mass. For example, hours, each, square foot.

    Unit of Measure
 - Budget Unit Qty
- **Source Columns**

 - Change Event Unit Qty (which can be used as filters for Rough Order of Magnitude (ROM) and Revenue ROM)
 - Direct Costs Unit Qty
 - Prime Unit Qty
 - Timecard Entry Hours
- For more information about creating calculated columns, see [Set Up a New Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project).

## Things to Consider

- **Required User Permissions:**

 - 'Admin' on the company's Admin tool.
- **For companies using the ERP Integrations tool**:

 - If you add the unit-based columns to the Procore ERP Direct Cost Budget or any ERP-integrated views, keep in mind that syncing the unit-based columns is NOT currently supported by Procore's 

    In Procore, the term *integrated ERP System*, is used to refer to *Enterprise Resource Planning (ERP)* software applications that can be configured to exchange data between Procore and a supported application using the Company level ERP Integrations tool. See [Which ERP integrations are supported by Procore?](/faq-which-erp-integrations-are-supported-by-procore)

    Integrated ERP System.

## Prerequisites

- Create the budget view that you want to add the column to. See [Set up a New Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project).

## Steps

1. Navigate to the company's **Admin** tool.
2. Under **Tool Settings**, click **Budget**.
3. Click **Set Up New Budget View**.
4. Under **Standard Views**, select any non-ERP view in the list.
5. Click **Create**.
6. Click **Configure Columns**.
7. Under the **Standard** columns list, place a checkmark next to the *Budget Unit Cost*, *Budget UOM*, and *Budget Unit Qty*.
8. Choose one of these options to create a **Source** column:

   - Click **Create Source Column**.   
      OR
   - Click **Create** at the top right and choose **Source** from the drop-down menu.
9. Complete this data entry:

   - **Column Name**. Type a name for your new column.
   - **Column Source**. Select a *Unit Quantity* column from the drop-down list. For a list of fields, see Background above.
10. Configure options for the column you selected by marking the check boxes for the column.
11. Click **Create**.
12. Click the **X** button to close the window when you are done working with it. The new column will now appear on your budget view, and it will also be available to create calculated columns in reports.
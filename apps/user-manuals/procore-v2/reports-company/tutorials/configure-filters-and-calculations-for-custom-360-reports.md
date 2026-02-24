# Configure Filters & Calculations for Custom 360 Reports with Visuals and Dashboards (Beta)

Source: https://v2.support.procore.com/product-manuals/reports-company/tutorials/configure-filters-and-calculations-for-custom-360-reports

---

##### In Beta

This content is for Procore users participating in the 360 Reporting tool's Visuals and Dashboards Beta Program.

## Background

When creating a 360 Report with visuals and dashboards. Once you've selected a visual type and data set, the next step is to configure it to present your data. This tutorial provides detailed instructions for customizing each available visual types, from tabular reports to scorecards. Follow the steps for your chosen visual type to define data sources, apply filters, add calculations, and customize the display to fit your needs.

## Things to Consider

- **Required User Permissions**:

  - [How do 360 Reporting permissions work?](/faq-how-do-360-reporting-permissions-work)

## Steps

#### Load Data Manually for Better Performance

By default, **Load Data Manually** is **on** to improve performance with large data sets.

- **When ON (Default):** Users click a button to load the report data when they are ready. This feature is ON by default to improve performance with large data sets.
- **When OFF:** If you prefer data to load automatically, move the toggle to the left to turn this feature OFF.

    

#### Add Filters and Conditions

Pinpoint the exact information needed by applying one or more filters to the report.

1. Click the **Filters** tab.
2. Select a filter from the **Add Filters** box.
3. Apply a condition to the filter:

       
   - **Matches** or **Does not match**
   - **Contains text** or **Does not contain text**
   - **Starts with** or **Ends with**
4. Add additional features as needed.

#### Set Up a Basic Calculation

Create a new field in the report by performing simple math on the existing data.

1. Click **+Create New Calculation**.
2. Add a **Name** and **Description** for the basic calculation.
3. Select **Basic Calculation** from the Calculation Builder.
4. **Describe the calculation:**

   1. Type a name for the calculation in the **Add a Name** box.
   2. Add its purpose in the **Description** box.
5. **Build the equation**: Click the **Reset** button at any time to start over.

   1. In the **Column Type** list, select **Basic Calculation**.
   2. Select a field.
   3. Select an operator (like + or -).
   4. Select the second field.
6. **Format the result**:

   - Choose a **Format** (e.g., # Number, $ Currency, or % Percent).
   - Set the number of **Decimal Places**.
   - *Optional:* Choose the **Decimal Places**.
7. Turn the **Rounding** toggle ON to round numeric results.
8. Click **Save**.

#### Set Up a Date Variance Calculation

Calculate the difference between two date fields.

1. Click **Create New Calculation**.
2. Add a **Name** and **Description** for the basic calculation.
3. In the **Column Type** list, select **Date Variance**.
4. **Build the equation**:

       
   1. Select the first date column.
   2. Select an operator (e.g., **-(subtract)**).
   3. Select the second date column.
5. Click **Save**.
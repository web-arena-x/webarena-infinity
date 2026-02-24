# Add the Columns for the 'Budget Changes' Feature to a Budget View

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/add-the-columns-for-the-budget-changes-feature-to-a-budget-view

---

##### Â Phased Release

The [new Budget Changes feature](/process-guides/about-budget-changes/) is designed to replace the existing budget modifications feature. Once you migrate to Budget Changes, you will no longer have access to the budget modifications feature. If you have any questions before your company starts the migration, contact your Procore point of contact. To learn more about the timeline for migration, see: [Common Questions](/process-guides/about-budget-changes/common-questions).

## Background

Procore's 'Budget Changes' functionality provides project managers with greater control and insight into changes that impact your budget. Whether it's an increase, decrease, or net zero (0) budget change, this feature eliminates the need to create a separate budget line item in Procore. It also allows you to reflect the true cost and revenue of your change on a project's budget.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information:**

 - To learn more about budget changes in Procore, see [Create Budget Changes](/process-guides/resource-tracking-and-project-financials-setup-guide/record-changes-on-an-internal-budget-change).

## Prerequisites

- Add the Budget and Change Events tool to the project. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).
- Configure the 'Budget ROM' column settings in the Change Events tool. See [Configure Settings: Change Events](/product-manuals/change-events-project/tutorials/configure-advanced-settings-change-events).

## Steps

- Step 1: Add or Modify a Budget View
- Step 2: Add the Source Columns for the Budget Changes Feature
- Step 3: Modify the Calculated Columns for the Budget Changes Feature
- Step 4: Preview the Budget View
- Step 5: Assign the Budget View to Your Projects

### Step 1: Add or Modify a Budget View

When adding the columns detailed in this article, you have these choices:

- You can create a new budget view and add the recommended columns. See [Set Up a New Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project).
- You can edit an existing budget view and add the recommended columns. See [Edit an Existing Budget View](/product-manuals/admin-company/tutorials/edit-an-existing-budget-view).
- You can set up a budget view to use with Procore custom reports and add the recommended columns. See [Set Up a Budget View for Custom Reporting](/product-manuals/admin-company/tutorials/set-up-a-budget-view-for-custom-reporting).

After choosing the preferred option for your budget view, add all of the recommended columns using the steps detailed below.

##### Example

For the next steps, we created a new budget view based on the [Procore Standard Budget](/product-manuals/budget-project/tutorials/about-the-procore-standard-budget-view) view, which is at the top of the list under 'Standard Views'.

We also named our new view 'Budget Changes'. However, you can name your budget view as you want. When you are ready to continue, click the **Configure Columns** button. Then proceed by adding the recommended source and calculated columns.

### Step 2: Add the Source Columns for the Budget Changes Feature

You will begin by adding the recommended source columns as follows:

- Add the 'Budget ROM' Source Column
- Add the 'Budget Changes' Source Column

#### Add the 'Budget ROM' Source Column

In the 'Configure Columns' window, follow these steps to add a new source column named 'Budget ROM'. This column allows your team to forecast the potential impact that a change may have on your budget. Depending on the 'Budget ROM' settings in the Configure Settings page of the Change Events tool, you can configure this column to reflect the [Rough Order of Magnitude](/glossary-of-terms) value in your budget as *Cost* or *Revenue*. To learn more, see [Configure Settings: Change Events](/product-manuals/change-events-project/tutorials/configure-advanced-settings-change-events) and [What is the 'Budget ROM' column in Procore's Budget tool?](/faq-what-is-the-budget-rom-column-in-procores-budget-tool)

| Steps from the Configure Columns window in the Company Admin toolâ¦ | Settings |
| --- | --- |
| 1. Choose one of these options:     - Click **Create Source Column** in the center of the window.   OR    - Click the **Create** button and choose **Source** from the drop-down list. 2. In the **Column Name** field, type: Budget ROM 3. From the **Column Source** drop-down list, select *Change Events*. 4. Mark the **Budget ROM (Rough Order of Magnitude)** checkbox.    Â Note In the following steps, the Procore-recommended settings for the checkboxes to select are marked with an asterisk (\*). However, you can tailor your settings to suit your environment. - Under **Budget Changes**, mark the desired checkboxes:    - **With Budget Change** This option includes budget change amounts in the 'Budget ROM' column.   - **Without Budget Change \***   This option excludes budget change amounts from the 'Budget ROM' column. - Under Scope, mark all of the desired checkboxes:    - *In Scope \**   - *Out of Scope \**   - *TBD \**   - *No Scope Associated \** - Under **Change Event Status**, mark all of the desired checkboxes:    - *Open \**   - *Closed* \*   - *Pending \**   - *Void* - Click **Save**. Procore adds the new column to the **Source** list on the left. | |

#### Add the 'Budget Changes' Source Column

In the 'Configure Columns' window, follow these steps to add a new source column named 'Budget Changes'.

| Steps from the Configure Columns window in the Company Admin toolâ¦ | Settings |
| --- | --- |
| 1. Choose one of these options:     - Click **Create Source Column** in the center of the window.   OR    - Click the **Create** button and choose **Source** from the drop-down list. 2. In the **Column Name** field, type: Budget Changes 3. From the **Column Source** drop-down list, select *Budget Changes*. 4. Mark the **Budget Change Adjustments** check box. A *Budget Change Adjustment* represents a formal change to your budget.    Â Note In the following steps, the Procore-recommended settings for the checkboxes to select are marked with an asterisk (\*). However, you can tailor your settings to suit your environment. - Under **Scope**, mark all of the desired checkboxes:    - *In Scope \**   - *Out of Scope \**   - *TBD \**   - *No Scope Associated \** - Under **Status**, mark all of the desired checkboxes:    - *Draft* \*   - *Under Review* \*   - *Approved* \*   - *Void* - Click **Save**.   This adds the new column to the **Source** list on the left. | |

### Step 3: Modify the Calculated Columns for the Budget Changes Feature

Next, you will modify the existing calculated columns (or add new ones) to include the new source columns in the calculated columns formulas.

- Add or Modify the 'Revised Budget' Calculated Column
- Add the 'Projected Cost Budget' Calculated Column

#### Add or Modify the 'Revised Budget' Calculated Column

In the 'Configure Columns' window, follow these steps to modify the existing 'Revised Budget' column for the budget changes feature. Adding this column allows your project team to see the impact of the change on your budget.

| Steps from the Configure Columns window in the Company Admin toolâ¦ | Settings |
| --- | --- |
| 1. Choose one of these options:     - Click **Create Calculated Column** in the center of the window.   OR    - Click the **Create** button and choose **Calculated** from the drop-down list. 2. Under 'Calculated' on the left, highlight the **Revised Budget** column to reveal the 'Show Formula' section. 3. Click **Edit**. 4. In the **Column Name** field, choose from the options:     - Keep the existing column name: Revised Budget OR    - Create a new column name: Revised Budget (+Changes) 5. In the **Format** drop-down list, make sure *Currency* is selected. 6. Keep *Original Budget Amount* selected in the top drop-down list. 7. Click the **Remove** links. 8. Select these calculation settings as shown in the drop-down lists:     - *Original Budget Amount*    - *Plus (+) sign*    - *Pending Budget Changes* 9. Optional. Keep the mark in the **Allow Subtotals and Grand Totals** check box. 10. Depending on your choice in step 4 above: - Click **Update**. This updates the formula for the calculated column in the budget view.   OR - Click **Save as New**. This adds a new calculated column to the budget view. | |

#### Add the 'Projected Cost Budget' Calculated Column

In the 'Configure Columns' window, follow these steps to add a calculated column named 'Project Cost Budget'. Adding this column allows you to include budget changes so your team can track the projected cost to completion on the project's Budget tool.

| Steps from the Configure Columns window in the Company Admin toolâ¦ | Settings |
| --- | --- |
| 1. Choose one of these options:     - Click **Create Calculated Column** in the center of the window.   OR    - Click the **Create** button and choose **Calculated** from the drop-down list. 2. Under 'Calculated' on the left, highlight the **Revised Budget** column to reveal the 'Show Formula' section. 3. Click **Edit**. 4. In the **Column Name** field, type: Projected Cost Budget 5. In the **Format** drop-down list, make sure *Currency* is selected. 6. Keep *Original Budget Amount* selected in the top drop-down list. 7. Click the **Remove** links. 8. Select these calculation settings as shown in the drop-down lists:     - *Original Budget Amount*    - *Plus (+) sign*    - *Budget ROM*    - *Plus (+) sign*    - *Pending Budget Changes* 9. Optional. Keep the mark in the **Allow Subtotals and Grand Totals** check box. 10. Depending on your choice in step 4 above: - Click **Update**. This updates the formula for the calculated column in the budget view.   OR - Click **Save as New**. This adds a new calculated column to the budget view. | |

### Step 4: Preview the Budget View

Next, you can preview your new columns in the 'Column Configuration' area and by selecting different projects in the 'Preview with Project' drop-down list. The new columns appear on the right side of the budget. Finally, you can assign the budget view to one or more Procore projects in your company's account using the options in the 'Assign to Projects' drop-down list.

##### Example

Below is an example of the new columns that you can add to a Procore budget view, after it has been assigned to a project.
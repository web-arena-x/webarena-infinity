# Add Cost ROM, RFQ & Non-Commitment Cost Source Columns to a Budget View

Source: https://v2.support.procore.com/product-manuals/change-events-project/tutorials/add-cost-rom-rfq-and-non-commitment-source-columns-to-a-budget-view

---

## Background

If your company has opted to use the Change Events tool on a project, you can use the steps below to add one or more of the data columns associated with the Change Events tool to your project's budget view.

The Change Events data columns include:

- **Cost ROM**. Short for Cost Rough Order of Magnitude. This column shows the Cost ROM estimate for a change event.
- **RFQ**. Short for Request for Quote. This column shows the RFQ number.
- **NCC**. Short for Non-Commitment Cost. This column shows the value of a cost that is NOT included as a line item on a purchase order or subcontract.

 ##### Â Note

 If you also want to include the 'Revenue ROM' column in a budget view, see [Add the Change Events Columns to a Budget View](/product-manuals/change-events-project/tutorials/add-the-change-events-columns-to-a-budget-view-including-revenue-rom).

## Things to Consider

- **Required User Permissions:**

 - 'Admin' level permissions on the Company level Admin tool.
- **Additional Information:**

 - To learn more about non-commitment costs in Procore, see [How do I track non-commitment costs on a change event?](/faq-how-do-i-track-non-commitment-costs-on-a-change-event)
 - If you also want to include the 'Revenue ROM' column in a budget view, see [Add the Change Events Columns to a Budget View](/product-manuals/change-events-project/tutorials/add-the-change-events-columns-to-a-budget-view-including-revenue-rom).

## Prerequisites

- Add the Budget and Change Events tool to the project. See [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).

## Steps

- Step 1: [Choose a Budget View](#step-1-choose-a-budget-view)
- Step 2: [Add the Recommended Columns](#step-2-add-the-recommended-columns)

## Step 1: Choose a Budget View

When adding the columns detailed in this article, you have these choices:

- You can create a new budget view and add the recommended columns. See [Set Up a New Budget View](/process-guides/project-equipment-user-guide/assign-the-budget-view-to-a-procore-project).
- You can edit an existing budget view and add the recommended columns. See [Edit an Existing Budget View](/product-manuals/admin-company/tutorials/edit-an-existing-budget-view).
- You can set up a budget view to use with Procore custom reports and add the recommended columns. See [Set Up a Budget View for Custom Reporting](/product-manuals/admin-company/tutorials/set-up-a-budget-view-for-custom-reporting).

After choosing the preferred option for your budget view, add all of the recommended columns using the steps detailed below.

## Step 2: Add the Recommended Columns

#### Add a Cost ROM Column

This adds a source column named 'Cost ROM' which shows a 

*Rough Order of Magnitude (ROM)* is a rough numerical cost estimate that is used in the construction industry to gain a rough idea of the cost(s) to complete a project. ROM estimates are typically provided by a knowledgeable, high-level expert during the initiation/beginning phases of a project when there is still a high level of uncertainty about the project. ROM estimates are understood to have a lower level of accuracy than a definitive/conclusive estimate. Procore also provides an option for tracking potential revenue for change events using a Revenue ROM option that lets you use the latest cost amounts when changes are out of scope.

Rough Order of Magnitude estimate for change events. The value that appears in this column on a budget line item is not yet associated with a 

In Procore, a *Commitment Change Order (CCO)* details a potential change that will affect the original costs and/or timeline of a *purchase order* or *subcontract*.

Commitment Change Order, an 

A *Request for Quote (RFQ)* is a business process where a client requests a price quote from a *collaborator*, such as a *subcontractor*, vendor, or another supplier. The collaborator reviews the client's RFQ requirements and then responds by providing a written price quote. In Procore, RFQs are created after a *change event* occurs and helps the client to avoid incurring unexpected and costly alterations or substitutions.

Request for Quote, or a 

In Procore, a Non-Commitment Cost (NCC) is a cost that is NOT included on the line items of a purchase order or subcontract. The cost is also an amount that is different from a cost submitted on a Potential Change Order (PCO).

Non-Commitment Cost.

| Steps from the Configure Columns window in the Company Admin toolâ¦ | Settings |
| --- | --- |
| 1. Click **Create Source Column**. 2. Under **New Source Column**, do the following:     - **Column Name**. Enter the name: Cost ROM    - **Column Source**. Select *Change Events*. 3. Mark the **ROM (Rough Order of Magnitude)** checkbox to apply these filters:     - Under **Prime PCO**, remove all of the marks from these checkboxes.    - Under **RFQ or Commitment Cost**, mark the **Without Cost** checkbox only.    Â Note This ensures that the source column includes only items that do not have associated costs, which excludes amounts from:       - Request for Quotes (RFQs)      - 2-tier Commitment Potential Change Orders (Commitment PCOs)      - 1-tier Commitment Change Orders (CCOs) - Under **Non-Commitment Cost**, mark the **Without Cost** checkbox only.    Â Note This ensures that the source column includes only amounts with commitment costs and excludes Non-Commitment Costs (NCCs). - Under **Scope**, mark these checkboxes only:    - In Scope   - TBD - Under **Change Event Status**, mark these boxes only:    - Open   - Closed   - Pending    Â Note - When filtering the columns data by change event status, any statuses not considered 'Void' are selected by default.     - If your company created custom statuses, those will NOT be shown by name. However, any custom status considered 'Open', 'Closed', and 'Pending' are also selected by default.     - To learn more about custom statuses, see [Set the Default Change Management Configurations](/product-manuals/admin-company/tutorials/set-the-default-change-management-configurations). - Click **Create**. | |

#### Add a Cost RFQ Column

This adds a source column named 'Cost RFQ' which shows costs associated with RFQs. The value that appears in this column on a budget line item is not yet associated with a 

In Procore, a *Commitment Change Order (CCO)* details a potential change that will affect the original costs and/or timeline of a *purchase order* or *subcontract*.

Commitment Change Order or a 

In Procore, a Non-Commitment Cost (NCC) is a cost that is NOT included on the line items of a purchase order or subcontract. The cost is also an amount that is different from a cost submitted on a Potential Change Order (PCO).

Non-Commitment Cost.

| Steps from the Configure Columns window in the Company Admin toolâ¦ | Settings |
| --- | --- |
| 1. Click **Create Source Column**. 2. Under **New Source Column**, do the following:     - **Column Name**. Enter the name: Cost RFQ    - **Column Source**. Select *Change Events*. 3. Mark the **RFQ (Request for Quote)** checkbox to apply these filters:     - Under **Prime PCO**, remove all of the marks from these checkboxes.    - Under **RFQ or Commitment Cost**, mark the **Without Cost** checkbox only.    Â Note This ensures that the source column only includes values that do not have costs. This setting excludes amounts from:       - 2-tier Commitment Potential Change Orders (Commitment PCOs)      - 3-tier Commitment Potential Change Orders (Commitment PCOs)      - 1-tier Commitment Change Orders (CCOs) - Under **Non-Commitment Cost**, mark the **Without Cost** checkbox only.    Â Note This ensures that the source column includes only amounts with commitment costs and excludes Non-Commitment Costs (NCCs). - Under **Scope**, mark these checkboxes only:    - In Scope   - TBD - Under **Change Event Status**, mark these boxes only:    - Open   - Closed   - Pending    Â Note - When filtering the columns data by change event status, any statuses not considered 'Void' are selected by default.     - If your company created custom statuses, those will NOT be shown by name. However, any custom status considered 'Open', 'Closed', and 'Pending' are also selected by default.     - To learn more about custom statuses, see [Set the Default Change Management Configurations](/product-manuals/admin-company/tutorials/set-the-default-change-management-configurations). - Under **RFQ Status**, remove all of the marks from these checkboxes. - Click **Create**. | |

#### Add a Non-Commitment Cost Column

This adds a source column named 'Non-Commitment Cost' column. The value that appears in this column on a budget line item represents a 

In Procore, a Non-Commitment Cost (NCC) is a cost that is NOT included on the line items of a purchase order or subcontract. The cost is also an amount that is different from a cost submitted on a Potential Change Order (PCO).

Non-Commitment Cost.

##### Â Important

If you plan to use the 'Non-Commitment Cost' column in the calculation for the 'Projected Cost' column (or for a 'Forecast' column), it is important to choose one (1) of the following options to ensure the calculation is NOT double-counted when related direct costs impact your budget:

- *Optional:* Update the 'Cost RFQ' column to exclude 'Closed' change event statuses. Then instruct users who create relevant direct costs to also change the appropriate change event's status to 'Closed.' This will exclude the Non-Commitment Cost from the column's value.   
   OR
- *Optional:* When users create relevant direct costs, instruct your users to delete the 'Non-Commitment Cost' from the appropriate change event.   
   OR
- *Optional:* Do NOT create direct costs for the 'Non-Commitment Costs' being tracked in your budget.

| Steps from the Configure Columns window in the Company Admin toolâ¦ | Settings |
| --- | --- |
| 1. Click **Create Source Column**. 2. Under **New Source Column**, do the following:     - **Column Name**. Enter the name: NCC    - **Column Source**. Select *Change Events*. 3. Select the **RFQ (Request for Quote)** checkbox to apply these filters:     - Under **Prime PCO**, remove all of the marks from these checkboxes.    - Under **Scope**, mark these checkboxes only:       - In Scope      - TBD    - Under **Change Event Status**, mark these boxes only:       - Open      - Closed      - Pending    Â Note - When filtering the columns data by change event status, any statuses not considered 'Void' are selected by default.        - If your company created custom statuses, those will NOT be shown by name. However, any custom status considered 'Open', 'Closed', and 'Pending' are also selected by default.        - To learn more about custom statuses, see [Set the Default Change Management Configurations](/product-manuals/admin-company/tutorials/set-the-default-change-management-configurations). - Under **Non-Commitment Costs**, mark the **Without Costs** checkbox. - Click **Create**. | |

#### Update Pending Cost Changes Column

The Procore Standard Budget View includes a 'Pending Cost Changes' source column. Use the steps below to update that column.

| Steps from the Configure Columns window in the Company Admin toolâ¦ | Settings |
| --- | --- |
| 1. Under **Source,** highlight the 'Pending Cost Changes' column. 2. Click **Edit**. 3. Ensure the **Column Source** is set to **Commitments**. 4. Under **Subcontracts**, mark the **Draft** checkbox and remove the marks from all other checkboxes. 5. Under **Purchase Order Contracts**, mark the **Draft** checkbox and remove the marks from all other checkboxes. 6. Under **Change Orders**, mark the **Draft** checkbox and remove the marks from all other checkboxes. 7. Click **Update**. | |

#### Update the Projected Costs Column

The Procore Standard Budget View includes a 'Projected Cost ' calculated column. Use the steps below to update that column.

| Steps from the Configure Columns window in the Company Admin toolâ¦ | Settings |
| --- | --- |
| 1. Under **Calculated,** highlight the 'Projected Costs' column. 2. Click **Edit**. 3. Configure the calculation's drop-down lists as follows:     - Select the 'Cost ROM' column.    - Select the plus (+) sign.    - Select the 'Cost RFQ' column.    - Select the plus (+) sign.    - Select the 'NCC' column. 4. Click **Update**. | |
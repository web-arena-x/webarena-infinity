# Compare Bids in Portfolio Financials

Source: https://v2.support.procore.com/product-manuals/portfolio-financials/tutorials/compare-bids-in-portfolio-financials

---

##### Â Legacy

This information is intended for accounts with [Portfolio Financials](/product-manuals/portfolio-financials/) product in Procore. Please reach out to your Procore point of contact  for more information.

## Background

With the Bid Comparison feature in Portfolio Financials, you can compare received bids side-by-side and evaluate their data to make informed decisions about your bids. Since all submitted bids in a Bid Room would have used the same bid form, the bids are already leveled on the page.

## Things to Consider

- **Required User Permissions**:

  - 'Limited' access to the project or higher.  
    *Note:* Users with 'Limited' access must be on the Bid Room Team for the project.
- **Additional Information**:

  - ***Important!*** If your organization has the 'Sealed Bidding' feature enabled by Procore and you are running a sealed bid process, the 'Compare Bids' button will not be available until the bids are unlocked.

## Steps

1. Navigate to the **Bid Room** you want to compare bids in.
2. Click **Manage Bids**.
3. Click **Compare Bids**.
4. Follow steps for the following:

   - Bid Comparison Page Overview

     - View Bidder Comments on Line Items
   - Select Bids to Compare
   - Select Comparison Tools

     - Enable or Disable a Tool
     - Adjustments
     - Price Per Square Foot (Price/ftÂ²)
     - Show Outliers
     - Merge or Unmerge Alternates
     - Budget (Compare a Bid Against a Budget)
     - Average Bid
     - Synthetic Low Bid
   - Export Bid Data

### Bid Comparison Page Overview

The following options are available in this mode (refer to each number in the image above):

*Total value of bid.*

*Bid form completion percentage.*

*Date the bid was received.*

*Bid revisions (if applicable).*

*Number of requested bid form fields completed.*

*Price per square footage (Price/ftÂ²) breakdown for a line item.*

***Comparing Bids*** *drop-down menu to select and display which bids are visible.*

***Tools*** *drop-down menu to select which comparison tools are currently enabled or disabled.*

***Export*** *drop-down menu to export the current view.*

#### View Bidder Comments on Line Items

Bidders have the ability to leave comments on individual line items in their bids to provide additional information or context.*Note*: If there is a comment on a line item, there will be a **speech bubble** icon on a cell.

**To view comments on a line item**:

- Click the **speech bubble** icon in a cell.

---

### Select Bids to Compare

When you enter the bid comparison page, all of the most recent bids submitted by your vendors appear as columns by default. You can show or hide these columns as needed from the Comparing Bids menu. This tool can also be used to make previously submitted versions of a bid visible so that you can compare the most recent bid to its past iterations if needed. You can also view one bid individually.

#### **To show or hide bids as columns**:

1. Click the **Comparing Bids** drop-down menu.
2. Choose which bids you want to compare:

   - Mark the checkboxes next to bids you want to display as columns.
   - Clear the checkboxes for the bids you do not want to display as columns.  
        
     *Note*: If there are any bid revisions, a **down arrow** icon is shown to the right of a bid (shown above). Click the **down arrow** to expand the revisions and mark the checkboxes next to them if you want to display them as columns.
3. Click **Done**.

---

### Select Comparison Tools

The **Tools** drop-down menu contains a number of tools to help you evaluate your bids.

#### Enable or Disable a Tool

1. Click the **Tools** drop-down menu.
2. Mark the checkbox next to a tool to enable it for your comparison.  
    OR  
    Clear the checkbox next to a tool to disable it.

See the sections below for details on the following bid comparison tools and actions:

- Adjustments
- Price Per Square Foot (Price/ftÂ²)
- Show Outliers
- Merge or Unmerge Alternates
- Budget (Compare a Bid Against a Budget)
- Average Bid
- Synthetic Low Bid

---

#### Adjustments

The Adjustments tool is enabled by default, and allows you to manually manipulate the value of cells in your bids. For example, this function can be useful if you want to evaluate what a bid might look like with the price of a line item reduced.

*Notes*:

- Any adjustments you make will modify the total bid value so that you can see how your adjustments affect the overall bid.
- Manipulating the data in the cells DOES NOT modify the actual bids. In addition, the vendor is NOT notified that you are adjusting the values.

#### Make Adjustments to a Cell

**To adjust the value of a cell:**

1. Make sure **Adjustments** is selected in the **Tools** drop-down menu.
2. Click into a cell.
3. Enter a new value for the cell.
4. Press ENTER or RETURN on your keyboard.  
   *Note*: The original value of the cell appears immediately to the left of the adjusted value in grey text. Adjusted values appear in blue text.

**To remove an adjustment on a cell:**

1. Make sure the Adjustments tool is enabled.
2. Click into a cell.
3. Delete the contents of that cell.
4. Press ENTER or RETURN on your keyboard.

###### Add and Manage Notes for a Cell

You can add a note on individual cells to provide additional information. For example, you might want to add a comment on a cell that you have adjusted so that your team knows why the value was changed. Notes are visible to all members of the Bid Room Team, and are NOT visible to bidders.

*Note*: A cell with a note on it is indicated by a triangle  in the top-right corner of the cell, as shown below.

**To add a note to a cell**:

1. Hover your mouse over the cell you want to add a note to.
2. Click the **plus**  icon in the corner of the cell.
3. Enter your note into the text box.
4. Click out of the text box to save the note.

**To edit a note on a cell**:

1. Hover over the cell you want to edit the note for.
2. Click the **triangle**  icon in the corner of the cell.
3. Edit the note in the text box.
4. Click out of the text box to save your note.

**To remove a note from a cell**:

1. Hover over the cell you want to remove a note from.
2. Click the **triangle**  icon in the corner of the cell.
3. Delete the contents of the note in the box that appears.
4. Click outside of that box to save your changes.

---

#### Price Per Square Foot (Price/ftÂ²)

Price per square foot breakdown is enabled by default. Each cell will have its price per square foot broken down by the square footage value that was entered on the Trade Setup page.

**To edit the Square Footage value for a breakdown**:

1. Make sure **Price/ftÂ²** is selected in the **Tools** drop-down menu.
2. Click **Edit** next to Price/ftÂ².
3. Enter a new square footage value.
4. Click **Save**.

---

#### Show Outliers

Outliers are cells whose values vary significantly (higher or lower) from the same item across all bids, or vary significantly from other values in the same bid.

*Note*: As you make adjustments to cells, more outliers might appear or disappear to reflect the adjustments you make. The sensitivity for outliers can be adjusted from the **Tools** drop-down menu as explained below.

##### Â Note

Cells highlighted in YELLOW indicate outliers. In addition, if you increase the sensitivity for outliers in the **Tools** menu, the color of existing outliers will turn a deeper shade of yellow.

**To adjust the sensitivity for outliers**:

1. Click the **Tools** drop-down menu.
2. Adjust the outlier sensitivity slider.

---

#### Merge or Unmerge Alternates

By default, pricing for alternates does NOT factor into the total bid value. Instead, you must enable them to have their price factored in:

**To include an alternate in the total bid value**:

1. Scroll to the Alternates section.
2. Mark the checkbox next to an alternate to add it into the total bid value.

**To merge alternates into one line item**:

1. Make sure **Activate Merges** is enabled in the **Tools** drop-down menu.
2. Scroll down to the Alternates section.
3. Click the **Tools** drop-down menu and select **Merge Alternates**.
4. Mark the checkboxes to the alternates you want to merge.
5. Click **Merge** to merge the alternates.
6. Click **Finish** to finalize the merge.  
   *Note*: Merged alternates are indicated by a **merge**  icon.

**To unmerge alternates**:

1. Scroll down to the Alternates section.
2. Click the **merge**  icon.
3. Click **Unmerge**.

---

#### Budget (Compare a Bid Against a Budget)

If you have a budget for each individual line item in your bid, you can compare your bids to those individual budgets.*Note*: Budget values on this page are not pulled in from the project page and must be entered manually.

***Step 1:*** **Enable Budget Comparison**:

1. Click the **Tools** drop-down menu.
2. Mark the checkbox next to **Budget**.
3. Click **Apply**.   
   *Note*: After enabled, you can enter a budget amount into the budget column that appears.

***Step 2:*** **Enter a Budget Value in the Budget Column**:

1. Click on a cell that says 'Enter Budget' in the column.
2. Type a value for that budget.
3. Press ENTER or RETURN on your keyboard.

***Optional*****: Edit or Remove a Budget Value:**

- **To edit a budget value:**

  1. Click on a cell in the budget column.
  2. Adjust the value of the cell.
  3. Press ENTER or RETURN on your keyboard.
- **To remove a budget value:**

  1. Click on a cell in the budget column.
  2. Remove the contents of the cell.
  3. Press ENTER or RETURN on your keyboard.

---

#### Average Bid

You can generate an average bid to show what the average cost of each line item from each bid is.

**To enable or disable the Average bid view**:

1. Click the **Tools** drop-down menu.
2. Mark the checkbox next to **Average** to enable the average bid column.  
    OR  
    Clear the checkbox to disable the column.
3. Click **Apply**.

---

#### Synthetic Low Bid

You can generate an synthetic low bid to show a bid comprised of the lowest values from all of the bids. This is used to provide a sense of what the lowest possible cost for the bid might be.

**To enable or disable the Synthetic Low bid view**:

1. Click the **Tools** drop-down menu.
2. Mark the checkbox next to **Synthetic Low** to enable the synthetic low bid column.  
    OR  
    Clear the checkbox to disable the column.
3. Click **Apply**.

---

### Export Bid Data

All of the data on the bid comparison page can be exported to an XLS or PDF file.

##### Â Important

When exporting, the export captures the CURRENT view of the bid comparison page. All adjustments, notes, view, columns, and merges will appear in your exported report.
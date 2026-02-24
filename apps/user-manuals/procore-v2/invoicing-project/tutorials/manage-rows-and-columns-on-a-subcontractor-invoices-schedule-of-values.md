# Manage Rows and Columns on a Subcontractor Invoice's Schedule of Values

Source: https://v2.support.procore.com/product-manuals/invoicing-project/tutorials/manage-rows-and-columns-on-a-subcontractor-invoices-schedule-of-values

---

##### Using Owner or Specialty Contractor Terminology?

Procore can be configured to use terminology specific to General Contractors, Owners, or Specialty Contractors. Learn [how to apply the dictionary options.](/faq-what-tool-names-and-terms-are-different-in-procore-for-general-contractors-owners-and-specialty-contractors)

- To learn the differences: **Show/Hide**

 - This table shows the differences in tool names (**bold**) and terms across the point-of-view dictionaries for Project Financials.

    | **General Contractors English (United States) - Default** | **Owners** ***English (Owner Terminology V2)*** | **Specialty Contractors** ***English (Specialty Contractor Terminology)*** |
    | --- | --- | --- |
    | **Invoicing** | ***Invoicing*** | ***Progress Billings*** |
    | Owner | *Funding* | *Owner* |
    | Owner/Client | *Owner/Client* | *GC/Client* |
    | Prime Contract Change Order | *Funding Change Order* | *Client Contract Change Order* |
    | **Prime Contracts** | ***Funding*** | ***Client Contracts*** |
    | Revenue | *Funding* | *Revenue* |
    | Subcontract | *Contract* | *Subcontract* |
    | Subcontractor | *Contractor* | *Subcontractor* |
    | Subcontractor Schedule of Values (SSOV) | *Contractor Schedule of Values (CSOV)* | *Subcontractor Schedule of Values (SSOV)* |

    ##### About These Dictionaries

    - **Default Setting:** The 'General Contractor' dictionary is enabled by default for all accounts.
    - **Availability:** These alternate dictionaries in *italics* are available in US English only.

    ##### How to Switch Your Dictionary

    To change your company's terminology to the Owner or Specialty Contractor dictionary, contact your company's 

    A *Procore Administrator* is a user who has 'Admin' level permissions on all of the Company level Tools in Procore. Granting a user âAdminâ level permissions in the Company level Directory tool automatically assigns that user âAdminâ permissions on all Company level tools. Also called a *Company Administrator*.

    ProcoreÂ Administrator. They will work with your Procore Point of Contact to make the change.

## Background

If you want to show, hide, group, sort, or size the columns in the 'Schedule of Values' table in the project's Commitments tool, there are a variety of operations you can use to organize the line items on your invoices.

## Things to Consider

- [Required User Permissions](/product-manuals/invoicing-project/permissions)

## Prerequisites

- [Create a Subcontractor Invoice](/process-guides/invoice-administrator-guide/create-subcontractor-invoices)

## Steps

- Group by Menu
- Bulk Edit a Schedule of Values
- [Manage Table Settings](/product-manuals/commitments-project/tutorials/manage-rows-and-columns-in-the-commitments-tool)

 - [Row Height](/product-manuals/commitments-project/tutorials/manage-rows-and-columns-in-the-commitments-tool)
 - [Configure Columns](/product-manuals/commitments-project/tutorials/manage-rows-and-columns-in-the-commitments-tool)
- [Manage Columns](/product-manuals/commitments-project/tutorials/manage-rows-and-columns-in-the-commitments-tool)

 - [Adjust Column Width](/product-manuals/commitments-project/tutorials/manage-rows-and-columns-in-the-commitments-tool)
 - [Arrange Columns](/product-manuals/commitments-project/tutorials/manage-rows-and-columns-in-the-commitments-tool)
 - [Sort Columns](/product-manuals/commitments-project/tutorials/manage-rows-and-columns-in-the-commitments-tool)
- [Overflow Menu](/product-manuals/commitments-project/tutorials/manage-rows-and-columns-in-the-commitments-tool)

 - Group by Column
 - [Pin Column](/product-manuals/commitments-project/tutorials/manage-rows-and-columns-in-the-commitments-tool)
 - [Autosize this Column](/product-manuals/commitments-project/tutorials/manage-rows-and-columns-in-the-commitments-tool)
 - [Autosize All Columns](/product-manuals/commitments-project/tutorials/manage-rows-and-columns-in-the-commitments-tool)
 - [Reset Columns](/product-manuals/commitments-project/tutorials/manage-rows-and-columns-in-the-commitments-tool)

### Group by Menu

A **Group by** menu is available when viewing and editing a invoice's Schedule of Values. With these options, you can choose how the system groups your line items in the Schedule of Values. By default, the *Commitment Lines and Change Orders* option is selected\_.\_ You can add and remove any additional options as desired.

##### Â Tip

**How do I show/hide columns that I've selected as grouping options?** When you add an option to the Group By menu, Procore automatically adds the column to the right side of the table, unless that column is already configured to show in the Schedule of Values. To show or hide columns, apply the ON/OFF controls described in .

To organize your Schedule of Values data, you can click the grab bar on the left side of each option (see 1 and 2 below) and drag the option into the desired position to modify the hierarchy of item groupings in the SOV table. To remove any options from the invoice, click the close (x) icon next to a single option or simply click **Reset**.

When applying the menu options, its important to note that the groupings in the Schedule of Values do NOT impact the layout of the invoice's PDF export files. Any settings you apply to one contract's invoice, do not change the settings on another contract's invoices. However, any options you set do remain in effect between user sessions on the selected contract's invoices.

### Bulk Edit a Schedule of Values

You can bulk edit the percentage values to apply to selected line items on a subcontractor invoice's Schedule of Values. To open the Edit panel, select the line items and then click the Pencil icon. The fields in the Edit panel are available when you update the latest invoice for a commitment. The bulk editing options detailed in the table below are only available when an invoice is in the *Draft* or *Revise & Resubmit* status. Any options you set will remain in effect between user sessions on the commitment contract's invoices.

The first step is to select one (1) or multiple line items using the options illustrated above. The following table describes your options in more detail.

| **What do you want to select?** | **Steps** | **Example** |
| --- | --- | --- |
| All line items in the Schedule of Values | Mark the **Item Number** checkbox at the top of the Schedule of Values. | |
| All line items in a group | Mark the check box(es) at the top of the desired group(s) in the Schedule of Values table. | |
| One or multiple line items | Mark the check box(es) that correspond to individual line item(s) in the Schedule of Values. | |

The next step is to click the pencil icon at the top of **Schedule of Values** to open the **Edit** panel on the right.

The final step is to edit one (1) or all of the values in the fields described in this table:

| **Field Name in the Edit Panel** | **To edit the selected line items...** | **To apply your edits...** | **Learn More** |
| --- | --- | --- | --- |
| **Work Completed This Period (%)** | Type a percentage value to bill for work complete. | After updating the field(s) the **Edit** panel, click the **Apply** button. | [Create a Subcontractor Invoice](/process-guides/invoice-administrator-guide/create-subcontractor-invoices) |
| **Total Completed & Stored to Date (%)** | Type a percentage value to bill for work complete. | | |
| **Work Retainage This Period (%)** | Type a percentage value to set work retainage. | [Set or Release Retainage on a Subcontractor Invoice](/product-manuals/invoicing-project/tutorials/set-or-release-retainage-on-a-subcontractor-invoice) | |
| **Retainage Released (%)** | Type a percentage value to release retainage. | | |
| **Materials Retainage (%)** | Type a percentage value to set materials retainage. | | |

### Manage Table Settings

You can adjust row height and show/hide columns using the Table Settings options in the Schedule of Values. First, click the **Table Settings** icon on the top-right side of the SOV table. This reveals the Table Settings pane on the right side of the web page. To close the Table Settings pane, click the 'x' in the top-right corner.

#### Row Height

Under **Row Height**, choose the *Small*, *Medium*, or *Large* option button. Procore's default setting is *Medium*.

#### Configure Columns

To choose the columns to show and hide, click the **Table Settings** icon on the top-right side of the contracts table. This reveals the Table Settings pane on the right side of the web page. Under the **Configure Columns** area, move the toggle to the right to turn the column display ON. Procore's default setting is to show all available columns.

##### Â Notes

- The blank line at the top of the 'Configure Columns' list is used to turn the 'Grand Totals' on the SOV table ON and OFF.
- By default, all of the available columns on an invoice are turned ON.
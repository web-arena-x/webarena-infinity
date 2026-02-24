# About Group Row Billing on Owner Invoices

Source: https://v2.support.procore.com/product-manuals/invoicing-project/tutorials/about-group-row-billing-on-owner-invoices

---

##### Â In Beta

This page details the modernized owner invoice experience.

## Overview

On the [Schedule of Values](/glossary-of-terms) of an [owner invoice](/glossary-of-terms), you can use the 'Group Row Billing' features to update line items when you want to quickly:

- **Bill for a fixed dollar ($) amount and distribute it among the line items in a group**. You have the option to proportionally distribute that amount among the group's line items.
- **Bill original Schedule of Values and Budget Change amounts as one line item.** Instead of editing line items and associated budget changes one by one, you can group the line items to update all of the line items in a group.

## Considerations

To update a group's line items, you can enter values in these fields on the **Group** or **Subtotal** row of an owner invoice's Schedule of Values

- **Work Completed This Period ($)**
- **Work Completed This Period (%)**
- **Total Completed & Stored Materials Total to Date (%)**

## Details

### Billing 'Work Completed: This Period ($)'

#### Billing Up to the Group's 'Scheduled Value'

When you want to bill up to the group's **Scheduled Value** amount, input a fixed amount in the **Work Completed: This Period ($)** field found on a group's **Subtotal** row. Procore proportionally distributes that fixed amount to each line item. Procore determines the proportion to distribute to each line item using the proportions from the **Balance to Finish** column.

##### Example

In this example, a user wants to distribute $100,000 among the line items in the group. Before data entry, the following was true:

- **Line Item 2.1.1** was 90% of the group's **Scheduled Value**.
- **Line Item 2.1.2** was 10% of the group's **Scheduled Value**.
- The group's **Balance to Finish** was $250,000.00. This is the **Scheduled Value** ($250,000) minus the **From Previous Application ($)** ($0.00) amount.

To distribute 50% of the **Balance to Finish** ($100,000.00) among the group's line items:

1. Enter 100,000.00 in the **Work Completed: This Period ($)** field on the group's **Subtotal** row.
2. Procore distributes the **$100,000.00** amount as follows:

   - **Line Item 2.1.1** is allocated **90.00%** of that amount, which is **$90,000.00** in **This Period ($)**.
   - **Line item 2.1.2** is allocated **10.00%** of that amount, which is **$10,000.00** in **This Period ($)**.
3. Procore updates the **Total Completed & Stored Materials** columns as follows:

   - **Total to Date ($)** is now **$90,000.00**, which is **40.00%** of the line item's **Scheduled Value**.
   - **Total to Date (%)** is now **$10,000.00**, which is **40.00%** of the line item's **Scheduled Value**.
   - **Balance to Finish** is now **$100,000.00.**

After data entry, the SOV looks like this:

---

#### Billing When Some Line Items are Fully Billed

When one or more line item's in a group previously billed for 100% of their **Schedule Value**, input a fixed ($) amount in the **Work Completed: This Period ($)** field found on the group's **Subtotal** row. Procore proportionally distributes that amount to the remaining line items. Procore determines the proportion to distribute to each line item using the proportions from the **Balance to Finish** column.

##### Example

In this example, the user also wants to distribute $100,000 among the line items in the group. However, before data entry, the following was true:

- **Line Item 3.2** was previously billed to 100% of its **Scheduled Value**.
- The group's **Balance to Finish** was $200,000.00, which is the **Scheduled Value** ($1,100,000.00) minus the **Work Completed: From Previous Application** ($900,000.00).

To bill for 50% of the group's **Balance to Finish** ($100,000.00)**:**

1. Enter 100,000.00 in the **Work Completed: This Period ($)** on the group's **Subtotal** row.
2. Procore distributes the **$100,000.00** amount to the remaining line items as follows:

   - **Line item 3.1** is allocated **$50,000.00** of that amount **This Period ($)**, which is **50.00%** of its **Scheduled Value**.
   - **Line item 3.2** is allocated **$0.00** of that amount **This Period ($)**, which is **0.00%** of its **Scheduled Value**.
   - **Line item 3.3** is allocated **$12,500.00** of that amount **This Period ($)**, which is **50.00%** of its **Scheduled Value**.
   - **Line item 3.4** is allocated **$2,500.00** of that amount **This Period ($)**, which is **50.00%** of its **Scheduled Value**.
   - **Line item 3.5** is allocated **$35,000.00** of that amount **This Period ($)**, which is **50.00%** of its **Scheduled Value**.
3. Procore updates the individual line items in the **Total Completed & Stored Materials** fields. It also updates the group's **Subtotal** row as follows:

   - **Total to Date ($)** is now **$1,000,000.00**, which is **90.91%** of the group's **Scheduled Value**.
   - **Total to Date (%)** is now **$90.91%** of the group's **Scheduled Value**.
   - **Balance to Finish** is now **$100,000.**

After data entry, the Schedule of Values looks like this:
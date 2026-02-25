# Amount Based Data Entry

Source: https://v2.support.procore.com/product-manuals/invoicing-project/tutorials/amount-based-data-entry

---

Review this example to learn how to bill for stored materials on invoices when a contract is configured to use the 'Amount-Based' accounting method.

##### Data entry on the first Amount-BasedÂ invoice

For the contract's first invoice, the value in the **New Materials Stored** column is always set to $0.00 by default. Since the subcontractor received materials on-site during this billing period, the invoice contact enters $2,000.00 in the **New Materials Stored** column (see 1). This represents the currency amount of the materials received. Once input, Procore automatically updates these values on the line item (see 2):

- **Total Completed & Stored to Date (%)**. Procore converts the entry to a percentage value (16%) to show total progress.
- **Materials Presently Stored**. Procore updates this column with the amount in the **New Materials Stored** column ($2,000.00).
- **Total Completed & Stored Date ($)**. Procore adds the $2,000.00 entry to this column (see 2). *Note:* This column shows the cumulative total of the values in the **Work Completed This Period**, **New Materials Stored**, and **Materials Presently Stored** column.
- **Balance to Finish**. This column is only visible to invoice administrator(s). Procore takes the **Scheduled Value** amount and subtracts the **New Materials Stored** amount to calculate the balance to finish). *Note:* In subsequent invoices, this column shows the cumulative decline from the contracted amount for the line item.

##### Data entry on the SecondÂ Amount-Based invoice

For the next billing period, the invoice contact prepares their second invoice. In all new invoices, the **New Materials** **Stored** column is always set to $0.00 by default (see 1). However, Procore automatically moves the value from the **New Materials Stored** column on the previous invoice to the **Previous Materials Stored** column on the current invoice (see 1 to 2). Before making additional data entry, note that the highlighted values (see 3) match the first invoice (above).

Next, perform some additional data entry on the line item.

For this entry, the subcontractor received an additional $2,500.00 in new materials that are now stored on the job site (or in a storage facility). The invoice contact enters $2,500.00 in the **New Materials Stored** column (see 1). After the entry, Procore automatically updates these values (see 2).

- **Total Completed & Stored to Date (%)**. Procore updates this value from 16% to 36%.
- **Materials Presently Stored**. Procore updates this value from $2,000.00 to $4,500.00.
- **Total Completed & Stored to Date ($)**. Procore updates this value from $2,000.00 to $4,500.00.
- **Balance to Finish**. Procore subtracts the sum of the 'New Materials Stored' value and the 'Previous Material Stored' amount from the 'Scheduled Value' amount. This shows the cumulative decline of the contracted amount.   
 *Note:* The **Work Completed from Previous Application (%)** value remains unchanged (see 3).

Next, half of the new materials stored on the first invoice were installed on the job site during the current billing period. To address this, the invoice contact takes $1,000.00 from the **Previous Materials Stored** column (see 1) and moves that $1,000.00 to the **Work Completed this Period** column (see 2).

##### 

After you change the entry in the **Previous Materials Stored** column, the system the system focus jumps to the **Work Retainage This Period ($)** column. This occurs if the invoice administrator enables the retainage setting on the commitment. To keep to the purpose of billing for stored materials, retainage data entry is not included in this example. However, documentation about retainage is available:

- To learn how to enable retainage on a commitment, see [Enable Retainage on a Purchase Order or Subcontract](/product-manuals/commitments-project/tutorials/enable-retainage-on-a-purchase-order-or-subcontract).
- To learn how to set and release retainage on an invoice, see [Set or Release Retainage on a Subcontractor Invoice](/product-manuals/invoicing-project/tutorials/set-or-release-retainage-on-a-subcontractor-invoice).

After moving the **Previous Materials Stored** amount to the **Work Completed This Period** column, Procore considers the entries to calculate these values:

- **Total Completed & Stored to Date (%)**. Procore keeps the value at 36%.
- **Materials Presently Stored**. Procore keeps the value at $3,500.00.
- **Total Completed & Stored to Date ($)**. Procore keeps the value at $4,500.00.
- **Balance to Finish**. Procore subtracts the sum of the 'New Materials Stored' value and the 'Previous Material Stored' amount from the 'Scheduled Value' amount. This shows the cumulative decline of the contracted amount.   
 *Note:* The **Work Completed from Previous Application (%)** value remains unchanged.
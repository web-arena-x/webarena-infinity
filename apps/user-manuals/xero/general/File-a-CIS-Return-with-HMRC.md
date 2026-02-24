# File a CIS return

Source: https://central.xero.com/s/article/File-a-CIS-Return-with-HMRC

---

## Overview

- Run the monthly return to show CIS deductions payable to HMRC in a tax period.
- Check details of all the transactions included in your return before you submit.
- File your return with HMRC from Xero, or manually file it with HMRC and mark it as submitted.

What you need to know

### HMRC requirements

HMRC requires contractors to file their CIS monthly return by the 19th of every month. Returns are filed for the tax period from the 6th of the previous month to the 5th of the current month. You don’t have to file a return in months where no CIS payments are made, but you must tell HMRC that there are no payments for the month by filing a nil return in Xero.

Only labour payments are subject to CIS deductions. CIS materials payments aren’t subject to deduction but must still be reported with the labour payments on the monthly return.

Any returns you file through HMRC’s portal only show in their portal, they don’t show in Xero. Returns you file through Xero show in Xero but don’t show in your HMRC portal.

### How it works in Xero

You need the advisor or standard + reports user role to access the CIS returns, reports, or verify subcontractors.

Once [CIS is enabled in your organisation](Enable-CIS-in-your-organisation.md), you can:

- Run and export the monthly return to submit it through HMRC’s portal
- Mark the return as submitted in Xero
- See the detail of each transaction included in the return, filter by subcontractor and search for specific transactions
- Download payment and deduction statements to manually send to your subcontractors

If [CIS Contractor](/s/article/Construction-Industry-Scheme-CIS-in-Xero) is added to your subscription, you can also:

- Run the monthly return and submit it to HMRC from Xero
- Bulk email payment and deduction statements to your subcontractors directly from Xero
- Verify your subcontractor’s deduction rate from Xero

It’s also important to understand that:

- Xero displays monthly returns either from the date you enable CIS or the date of the earliest CIS payment you subsequently record in Xero.
- The data displayed on the return is live. Any changes you make to CIS transactions, or to subcontractor details show on the return you see in Xero, even after you’ve filed it or marked it as submitted. We recommend you export a copy of the original return you file.
- Foreign currency transactions are converted and displayed in GBP. Amounts submitted to HMRC are truncated to the nearest pound (£).
- The return only includes information from bills paid or credit notes refunded in the period. Part paid bills and credit notes are included on a pro rata basis.
- Prepayments and overpayments aren't included. You can't select CIS account codes for these types of transactions because they might include work that's not subject to deduction.

### CIS columns explained

You'll see slightly different column headings depending on which Xero report you use. Below are explanations for some of the most important columns.

| Column name | Description |
| --- | --- |
| **Payments (Incl. VAT)** or **Total payment (inc. VAT)** | The total, including VAT, of all items paid to the subcontractor in the tax period, where the bill or credit note contains a CIS labour cost. Bills or credit notes that contain the CIS Materials account code but don't include a CIS labour cost aren't included. This total isn't required for the HMRC return. |
| **VAT** or **Total VAT** | The total VAT element of all payments made to subcontractors or credit notes applied to bills in the tax period. This isn't required for the HMRC return. |
| **Payments (Excl. VAT)** or **Total payments (excl. VAT)** | The total, excluding VAT, of all items paid to the subcontractor in the tax period, where the bill or credit note contains a CIS labour cost. Bills or credit notes that contain the CIS Materials account code but don't include a CIS labour cost aren't included. This total is required for the HMRC return. |
| **Cost of materials** | The total of all items coded to the CIS Materials account code on bills or credit notes that contain a CIS labour cost and were paid to the subcontractor in the tax period. CIS materials items that aren’t part of a bill or credit note that includes the CIS Labour account code aren’t included in this figure. |
| **Non-CIS** | Any line item that isn’t CIS labour or CIS materials, on a bill or credit note that includes labour or materials. These items aren't included in the liable to deduction amount and aren’t required for the HMRC return. |
| **Liable to Deduction** or **Labour** | The Payments (excl VAT) figure, less the Cost of Materials and any other non-CIS items on the bill or credit note. The Liable to Deduction figure represents the portion of all bills and credit notes paid in the tax period that are subject to a CIS deduction, which is then calculated according to the subcontractor’s CIS Rate. This isn't required for the HMRC return. |
| **Amount Withheld** or **CIS amount** | The total CIS deduction due for the subcontractor in the tax period, calculated by deducting the percentage amount specified in the CIS Rate field for the subcontractor from the Liable to Deduction amount. |

If the **Amount Withheld** or **CIS amount** column doesn’t display the percentage of the liable to deduction total you expect to see, it might be because the subcontractor’s CIS rate changed during the tax period.

Run and file your monthly return from Xero

If CIS Contractor is part of your subscription, you can file your return from within Xero.

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **CIS Contractor (Monthly Return, Online Filing and Statements)** report. You can use the search field in the top right corner.
3. Select the period of the return you want to file.
4. (Optional) Check the **UTR**(Unique Tax Reference) and **SVN**(Subcontractor Verification Number) details are correct. Click **Edit** to update them.
5. (Optional) To check the details of the return, select the **Transactions by subcontractor** tab. Filter by subcontractor, group by invoice or click on the transaction line to view the bill. You can also change the date range, export the data or preview and download the statements your subcontractors will receive.
6. Confirm the amounts reported are correct, then click **Submit to HMRC**.
7. Read through the HMRC declaration, then click **Confirm and continue**.
8. Enter your HMRC Gateway User ID and Password, then click **Connect to HMRC**.
9. It may take a few minutes for HMRC to process your return. Once you've connected to HMRC:

   - If your submission is in a queue with the HMRC, click **OK, got it**.
   - If your submission has failed, click **Close** and try submitting your return again.

   If you get a credentials error when trying to connect, check some [common causes](HMRC-credentials-error-when-filing-CIS-returns-online.md).
10. Refresh your screen in Xero to see the status of your return. You might need to do this several times if your return is in a queue at HMRC.

    - If your submission is successful, click **View confirmation** to see details of the submission and the IRmark. HMRC recommend you keep a record of this receipt.
    - If your submission has failed, click **Resubmit to HMRC** to try again.

      Sometimes failed submissions are due to an incorrect UTR. If you see a banner at the top of your return, click through to your [financial settings](Enable-CIS-in-your-organisation.md) and check that the UTRis entered correctly. Once you've updated your UTR, try filing your return again.

Once you've successfully filed your return, [email payment and deduction statements](CIS-Payment-and-Deduction-Statements.md) to your subcontractors.

Warning

The email HMRC sends to confirm their servers have received your return isn't confirmation of a successful submission. Check the status of your return in Xero.

### Resubmit a previously filed return

If you make changes that impact a CIS Return you've already submitted, resubmit the updated return to HMRC to overwrite the previous return. HMRC won't penalise you for resubmitted returns.

1. Open the return you want to resubmit.
2. Click **Resubmit to HMRC**, then click **Confirm and continue**.
3. Enter your HMRC Gateway credentials, then click **Connect to HMRC**.

Run your monthly return to submit outside of Xero

If you don't have CIS Contractor as part of your subscription, export your monthly return and submit it via the HMRC portal.

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **CIS Monthly Return**. You can use the search field in the top right corner.
3. Select a **Date range**.
4. Click **Update** to view your report.

You can [customise your report](Select-contents-and-display-order-in-a-new-report.md) to show the information you want:

- Choose which **Columns** appear on your report – such as amount withheld, NI number, VAT.
- Change the report layout by **Grouping/Summarising** the details.
- Add a **Filter** to refine the report results, then click **Apply**.
- Click **More** to show or hide **Decimals**.

You can also add, edit or delete a footer in the return.

To add or edit a footer:

1. Click **Insert content,** then select **Footer**.
2. To edit an existing footer, click **Edit** next to the text.
3. Inside the footer, enter the note you want to add to the return and choose your formatting options.
4. Click **Done**.

To delete a footer:

1. Next to the footer, click the menu icon , then select **Delete**.
2. Click **Delete** to confirm.

Once you’ve completed the return:

1. Click **Update** to refresh the return following any changes.
2. Confirm the amounts are correct.
3. Click **Export** and select the [file type](Export-or-print-a-report.md).
4. Manually [file the return with HMRC](https://www.gov.uk/what-you-must-do-as-a-cis-contractor/file-your-monthly-returns) (HMRC website).

To mark the return as submitted:

1. Find and open the **CIS Contractor (Monthly Return, Online Filing and Statements).** You can use the search field in the top right corner.
2. Click **Mark as submitted**.
3. Click **Got it** to go back to the return.

## What's next?

Send [payment and deduction statements](CIS-Payment-and-Deduction-Statements.md) to your subcontractors.
# The VAT201 return

Source: https://central.xero.com/s/article/The-VAT-201-return

---

## Overview

- Run the VAT201 return to meet your South African Revenue Service (SARS) requirements.
- Keep track of VAT201 returns and their due dates from one location in Xero.

What you need to know

### How it works

The VAT201 return is available to organisations on the cashbook pricing plan or above.

The return is based on how your tax rates are mapped. You can change the fields your tax rates are mapped to if needed. The Transactions by field number report is part of the VAT201 return and lists the individual transactions included for the period.

Xero displays the different tax lines on the return for you to review and use when you submit your return with SARS.

Any changes made to VAT201 returns display in the **History** section at the bottom of the return. You can also view the changes in the [History and notes report](View-a-history-and-notes-summary-for-transactions-and-user-activity.md).

### Late claims

Late claims are transactions you enter for a past period after the VAT return was finalised. Late claims can also arise if you edit, void or delete transactions that were included in a previous VAT period.

The VAT201 return automatically includes late claims from the date you start to use the return.

Transactions dated earlier than your Xero conversion date, and any changes you make to them after your conversion date, aren't included as late claims.

Before you start

### Complete your tax details

Before running your first VAT201 return, check you’ve completed your tax details to access the returns.

- [Set your tax basis](Select-or-update-your-tax-settings.md) to accrual.The return isn’t available to organisations where the tax basis is set to cash.
- [Set your tax period](https://central.xero.com/s/article/Set-up-your-organisation-s-financial-details-SA) to monthly, bi-monthly, quarterly, half-yearly or annually, depending on your organisation.
- Enter your [10 digit VAT registration number](/s/article/Set-up-your-organisation-s-financial-details-SA).
- Xero automatically pulls the default tax rates through to the correct lines on the VAT201 return. You need to [map tax rates](Map-tax-rates-to-the-VAT-201-return.md) you've added or customised to the correct fields on the return. This ensures that transactions you've applied the custom rate to are included correctly in the return.

### Select the VAT201 return start date

Select a VAT201 return start date to set the period of your first VAT201 return in Xero.

You need to complete your VAT details in the Financial Settings before you can select a start date.

To select or change the start date:

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **VAT201 Report**. You can use the search field in the top right corner.
3. Under **Start returns from**, either:

   - Click **Select date**, then select the period of your first VAT201 return in Xero.
   - Click your current start date, then select the new period of your first VAT201 return in Xero.
4. Click **Save**, then click **Save** again.

Xero suggests return periods based on your organisation's [conversion date](Setting-your-conversion-date.md) and filing frequency. If the start date you want isn't listed or you've joined Xero part way through the current tax period, file outside of Xero and start at the next filing period.

You can change the VAT201 start date before you finalise your first VAT201 return. To change the start date of a finalised return, you need to revert it to a draft status first.

How Xero populates fields in the return

### What you need to know

Xero calculates the return lines based on the mapped tax rates you apply to transactions for the return period. If transactions don’t map to the correct fields in your VAT return, check the mapping and make any changes as required.

To comply with SARS’ requirements, Xero rounds some fields on the return’s **Summary** tab to the nearest whole number. When these fields are used to calculate another field on the return, Xero uses the rounded value in the calculation.

The **Transactions by field number** tab displays the unrounded amounts for each field, based on the transactions entered in Xero.

### Fields in the VAT201 return explained

The table below shows how the VAT201 return fields are calculated and whether they’re rounded to the nearest whole number.

| Field number | Tax rate mapping | Rounded |
| --- | --- | --- |
| **Field 1** | Total VAT inclusive amount of sales with the Standard Rate Sales tax rate | ✔ |
| **Field 1A** | Total VAT inclusive amount of sales with the Standard Rate Sales - Capital Goods tax rate | ✔ |
| **Field 2** | Total amount of sales with the Zero Rate (Excluding Goods Exported) tax rate | ✔ |
| **Field 2A** | Total amount of sales with the Zero Rate (Only Exported Goods) tax rate | ✔ |
| **Field 3** | Total amount of sales with the Exempt and Non-Supplies tax rate | ✔ |
| **Field 4** | 15% VAT calculated from **Field 1** | X |
| **Field 4A** | 15% VAT calculated from **Field 1A** | X |
| **Field 5** | Total VAT exclusive amount of sales with the Accommodation exceeding 28 days tax rate | ✔ |
| **Field 6** | 60% of **Field 5** | ✔ |
| **Field 7** | Total VAT exclusive amount of sales with the Accommodation under 28 days tax rate | ✔ |
| **Field 8** | Sum of **Fields** **6** and **7** | X |
| **Field 9** | VAT calculated from **Field 8** | X |
| **Field 10** | Total VAT inclusive amount of sales with the tax rates:   - Change in Use Sales - Export of Second-hand Goods | ✔ |
| **Field 11** | 15% VAT calculated from **Field 10** | X |
| **Field 12** | Total VAT amount of sales with the tax rates:   - Old 14% Standard Rate Sales - Old 14% Standard Rate Sales - Capital Goods - Old 14% Change in use and Export of Second-hand Goods - Other Sales | X |
| **Field 13** | Sum of **Fields 4, 4A, 9, 11** and **12** | X |
| **Field 14** | Total VAT amount of supplies with the Standard Rate Purchases - Capital Goods tax rate | X |
| **Field 14A** | Total VAT amount of supplies with the Capital Goods Imported tax rate | X |
| **Field 15** | Total VAT amount of supplies with the Standard Rate Purchases tax rate | X |
| **Field 15A** | Total VAT amount of supplies with the Goods and Services Imported tax rate | X |
| **Field 16** | Total VAT amount of supplies with the Change in Use Purchases | X |
| **Field 17** | Total VAT amount of supplies with the Bad Debt tax rate | X |
| **Field 18** | Total VAT amount of supplies with these tax rates:   - Old 14% Standard Rate Purchases - Old 14% Standard Rate Purchases - Capital Goods - Old 14% Change in Use - Other Purchases | X |
| **Field 19** | Sum of **Fields 14**, **14A**, **15**, **15A**, **16**, **17** and **18** | X |
| **Field 20** | Difference between **Field 13** and **19** | X |

Tax rates excluded from the return:

- Exempt Purchases
- Zero Rated Purchases
- No VAT

Finalise the VAT201 return

### What you need to know

Xero's VAT201 return displays the fields required for your VAT201 summary, so you can review the field totals of your return. The **Transactions by field number** tab acts as an audit report for your VAT201 return.

### Run the return

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **VAT201 Report**. You can use the search field in the top right corner.
3. You see a list of returns displayed for the organisation. Each return has its status, date and amount you owe or owed to you showing against it. The returns are listed from oldest to newest.
4. Select the return from the list.

### Review the VAT return

To view the individual transactions that make up your return, select the **Transactions by field number** tab at the top of the return. This tab lists all the organisation’s transactions for the return period. The transactions are displayed in groups based on the field number they’re mapped to, so you can easily check your return.

Alternatively, click a specific line of the VAT201 return to view the transactions that are mapped to it.

You can also review any transactions not included in the return under **Unclaimable VAT** in the **Transactions by field number** tab.

To export a list of the transactions that make up the return, click **Export** at the top of the return, then select **Excel** or **PDF**. To choose what to include, click **Export**, then select **More options**.

If you’re not ready to finalise the return yet, click **Save as draft** at the bottom of the return.

### Finalise the VAT201 return

Once you've reviewed the return and made any changes to the underlying transactions, click **Finalise** to save a final copy of your return.

Once you finalise your first return:

- Any changes or additional transactions entered for the period won’t be included in the return. These are included as late claims in the next period instead.
- Finalise all subsequent returns in sequential order, ie from oldest to most recent.
- Xero automatically locks any previous returns and moves them under **Completed**.

To prevent further changes and close the period, [set a lock date](Set-up-and-work-with-lock-dates.md).

To make adjustments to a finalised VAT201 return in Xero, click **Revert as Draft** within the relevant return, then run it again.

Once the return is filed, it shows under the **Completed** section.

Warning

If you revert a finalised return back to a draft state, it will impact late claims made from the date the return was first finalised.

## What's next?

Once you've finalised your return, [file with SARS](File-a-VAT201-return-with-SARS.md).
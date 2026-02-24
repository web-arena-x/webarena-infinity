# Add, import and post manual journals

Source: https://central.xero.com/s/article/Add-import-and-post-manual-journals

---

## Overview

- Create a single manual journal or import multiple draft journals at once, then post them to the general ledger.
- You need the advisor or standard + reports user role to add and post manual journals or download the manual journal template and import journals.

How it works

Only users with the advisor or standard + reports user role can add and post manual journals, or download the manual journal template and import journals. Read only users can only [view manual journals](View-edit-or-copy-a-manual-journal.md).

You can create a single manual journal, then save it as a draft or post it straight to the general ledger. Alternatively, use the CSV template to create:

- A single draft manual journal, using the same date and narration for each line that you enter
- Multiple draft journals, using a new narration and/or a different date for each separate journal you want to create

When using a spreadsheet editor, such as Microsoft Excel, you can import up to 300 lines in one template file. Once the file has been imported to Xero, you can add more lines to the manual journals.

If you have recurring entries, you can [set up a repeating journal](Set-up-a-repeating-journal.md) to automate the process.

If your pricing plan includes multicurrency, you can only add manual journals in your base currency.

Tip

You can try out manual journals in the [Xero demo company](Use-the-demo-company.md). It has most of the features of an actual Xero organisation so you can explore Xero without entering your own data.

Add and post manual journals

### Add a single manual journal

Add a single manual journal, then save it as a draft or post it straight to the general ledger:

1. In the **Reportin****g** menu, select **All re****ports**.
2. Find and open the **Journal Report**. You can use the search field in the top right corner.
3. Click **Add new journal**, then enter the journal details in the relevant fields. [This short video](https://learning.central.xero.com/student/path/2665/activity/3935?/page/655775960d0fa3ccc5138ca2#/page/655775960d0fa3ccc5138ca2) shows you how to speed up data entry using Xero's inbuilt calculator.
4. Click **Save as draft**, or click the arrow next to **Save as draft**, then select **Save & add another** to save the journal without posting it to the general ledger. Alternatively, click **Post** or click the arrow next to **Post**, then select **Post & add another** to post the journal to the general ledger.

   If you post and add another journal, the date of the posted journal is used for the new journal.

### Post multiple manual journals

Post multiple draft journals to the general ledger at the same time:

1. In the **Reportin****g** menu, select **All re****ports**.
2. Find and open the **Journal Report**. You can use the search field in the top right corner.
3. Click **Go to manual journals**, then select the **Draft** tab.
4. Select the checkbox for each journal you want to post.
5. Click **Post**, then click **OK**.

Import multiple manual journals

Warning

Don't change any of the column headings in the template file, as this causes the import to fail.

Create the manual journal template file, then import it into Xero:

1. In the **Reportin****g** menu, select **All re****ports**.
2. Find and open the **Journal Report**. You can use the search field in the top right corner.
3. Click **Go to manual journals**, then click **Import**.
4. Click **Download template file**.
5. Enter the journal details into the template.

   If you leave both the date and narration cells blank, Xero treats that row as belonging to the same journal as the row above it.
6. Save the file with .csv as the file extension. For example, 2019Journals.csv.
7. In Xero, return to the **Import Manual Journal** screen, click **Browse**, then select the file.
8. Click **Import**, review the message, then click **Complete Import**.

Journal fields explained

| Journal field | Import template field | Description |
| --- | --- | --- |
| **Narration** | Narration | This field is mandatory. Enter a title to help you search for the journal. This field displays in the manual journal list and the [Journal report](Journal-report.md). When importing journals, enter the **Narration**value for the first row of the journal, then leave it blank for each row you want to import as lines in the same journal. |
| **Default narration to journal line description** | | Select the checkbox to copy the journal's narration into each line item description. |
| **Show journal on cash basis report** | | Select the checkbox if you want the journal to display on cash based reports, such as the [Statement of Cash Flows](Statement-of-Cash-Flows-New.md) and payments basis GST Return. |
| **Date** | Date | This field is mandatory. Select the date to post the journal to the general ledger (effective date). The date format needs to be either dd mmm yyyy or dd/mm/yyyy. For example, 30 Jun 2019 or 30/06/2019. When importing journals, enter the **Date** value for the first row of the journal, then leave it blank for each row you want to import as lines in the same journal. |
| **Auto Reversing Date** | | This field is optional. Select a future date on new or draft journals to reverse the journal automatically on the selected date. |
| **Amounts are** | | This field is mandatory. By default it shows as **No Tax**.   - Select **Tax Exclusive** to add the tax to each line item amount. - Select **Tax Inclusive** to include the tax with each line item amount.   The journal shows as tax exclusive when it's saved or posted. |
| **Description** | Description | This field is optional. Enter a description for each line item. If you selected default narration for the description, click in each description field for it to populate. |
| **Account** | AccountCode | Select the account code for each line item. Some [system accounts](Locked-and-system-accounts-in-your-chart-of-accounts.md) can't be selected in a manual journal. When importing, just enter the account code, don't include the account name. For example, 200. |
| **Tax Rate** | TaxRate | This field is mandatory to post a journal. When you create a journal in Xero, the tax rate for each line item defaults to the tax rate assigned to the account in your chart of accounts. The tax amount shown in the journal total depends on your selection in the **Amounts are** field. When importing journals, enter the full tax rate name as it appears in your tax settings in Xero. For example, '15% GST on Expenses'. You can import a template file with no tax rate entered, but you need to add this before you can post the journal in Xero. You can't edit the tax rate if **No Tax** is selected in the **Amounts are** field. Select **Tax Exclusive** or **Tax Inclusive** to change the tax rate. |
| **Tracking** | TrackingName[X] and TrackingOption[X] | This field is optional. If [tracking](Set-up-tracking-categories.md) is set up in your organisation, select the relevant tracking option for each line item, or select **Add new tracking option** to add another tracking option to the tracking category. If tracking is only used on one side of the journal (debit or credit), Xero creates a balance entry using the [Tracking Transfers system account](Locked-and-system-accounts-in-your-chart-of-accounts.md). When importing, enter the tracking category name and tracking category option as it appears in Xero. You need to enter both columns to import tracking information. If you don’t have a second tracking category, leave **TrackingName2** and **TrackingOption2** columns blank. |
| **Debit and credit amounts** | Amount | This field is mandatory. Enter the debit or credit amount for each line item. When you enter the account code for the second and any subsequent line items, Xero automatically enters the credit or debit journal balance, and adds the tax amount to the GST account when you post the journal. When importing, enter debits amounts as positives and credits as negative numbers. The total debits must equal the total credits before you can post the journal. You can use the [inbuilt calculator](Tips-and-shortcuts.md) to work out your debit and credit amounts. |
| **Add a new line** | | Click **Add a new line** to add a new line item to the journal. Click the delete icon beside the line item to delete it. |

## What's next?

[View or edit the details of the journals](View-edit-or-copy-a-manual-journal.md) you've just created.
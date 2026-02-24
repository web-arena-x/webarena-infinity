# Manually enter data for a document

Source: https://central.xero.com/s/article/Manually-enter-data-for-a-document

---

## Overview

- If Hubdoc didn't extract all the data you need for a document, you can manually enter it.
- You can also edit the data Hubdoc has extracted and change the tax amount calculated.

## Enter data manually

When a new document appears in your organisation, Hubdoc extracts the **Date**, **Total** **Amount** and **Supplier**, and if available the **Due Date** and **Invoice / Ref #**.

You might need to enter data manually if:

- Data has been extracted, but you need to edit it
- Hubdoc has failed to extract any data
- You need to manually adjust the tax rate for a document
- The amount uses a comma rather than a full stop and it hasn't been extracted correctly

To manually enter data for a document:

1. [Find and open the document](/s/article/Search-for-documents-in-Hubdoc?userregion=true).
2. To the right of the document, click **Edit Document** to open the data toolbar.
3. For each [document field](About-data-extraction-in-Hubdoc.md), enter the relevant data.

Tip

Edit the document’s line items and apply untracked inventory items you’ve set up in Xero when you [manually publish the document](Publish-Hubdoc-documents-to-Xero.md).

## Change the tax amount calculated

If selecting a single tax rate doesn’t result in the correct tax amount for the document, or a document has multiple tax rates that apply, you can manually adjust the tax calculated using the extracted amount calculator. You can use the tool to generate multiple line items for the document and select a tax rate for each line.

To have the **Tax Rate** fields available, you need to select **Publish tax data** in the Xero section of the [integration settings](Connect-Hubdoc-to-Xero.md#Setdefaulttaxrates).

To use the calculator tool:

1. [Find and open the document](/s/article/Search-for-documents-in-Hubdoc?userregion=true), then click **Edit Document** to open the data toolbar.
2. Under **Tax Rate**, select **Extracted Amount**.
3. In the **Tax Amount** field, enter the actual tax paid as per the document.
4. Select the tax rate that applies to the taxable and un-taxable amounts.
5. Under **Account**, select the chart of account code to apply to the taxable and un-taxable amounts.
6. Click **Generate Line Items** to see the tax amount calculations. Due to rounding, the line items calculated may differ from the document – you can adjust the amounts in the **Edit Line Items** dialog box.

   Alternatively, click **Or enter manually** to enter the line items yourself.

   You can click and drag the **Edit Line Items** dialog box around your screen so it’s easier to see the relevant areas of the document.
7. (Optional) If the document has more than two tax codes, click **Add a new line** to create additional lines.
8. Click **Save & Close** in the **Edit Line Items** dialog box to make changes to the edit data toolbar.

## What's next?

Once all the data is extracted and entered, [publish the document to Xero](Publish-Hubdoc-documents-to-Xero.md).
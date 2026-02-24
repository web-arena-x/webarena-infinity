# Extract bank statement data in Hubdoc

Source: https://central.xero.com/s/article/About-bank-statement-extraction-in-Hubdoc

---

## Overview

- Convert a PDF bank statement to a CSV file of transactions which you can import to Xero or QuickBooks Online.

What you need to know

### How it works

Use Hubdoc to extract the transactions from your scanned or downloaded PDF bank statement and convert the data to a CSV file. Then import the CSV file to Xero or QuickBooks Online to reconcile your transactions.

Hubdoc can extract data from debit or credit statements:

- Debit statements – Hubdoc will extract the date, description and amount for each transaction
- Credit statements – Hubdoc will extract the posted date, transaction date, description and transaction amount

Sometimes there can be an error extracting a transaction. This can occur if totals don’t match, no opening or closing date could be extracted, or data couldn’t be extracted for another reason.

When selected, the checkbox **Highlight extracted transactions on bank statement** highlights the transactions that were extracted from the statement, to help you review and fix errors faster. If an extraction error occurs, you only need to review the non-highlighted transactions.

### Statement requirements

To upload and export your bank statement data, your file must:

- Be a PDF with a maximum height and width of 40 inches, or 2880 points
- Contain all pages of the statement, with a maximum of 100 pages per PDF
- Be 35MB or less
- Have a minimum resolution of 200 DPI
- Only contain one statement
- Be written in English
- Be a debit or credit statement
- Be scanned straight; crooked or slanted scans can result in an error

###

Extract bank statement data

Warning

While you can upload a statement from any bank, we can’t guarantee the accuracy of extracted data from non-supported banks. See below for a list of supported banks.

1. [Upload your bank statement to Hubdoc](Upload-or-email-documents-into-Hubdoc.md).
2. Once uploaded, [find and open the statement](/s/article/Search-for-documents-in-Hubdoc?userregion=true) in Hubdoc.
3. In the transaction details, under **Document Type**, select **Statement**.
4. Under **File Format**, select your preferred file format for the exported data.
5. Click **Generate CSV**.
6. Once Hubdoc has processed your statement, click **Download**. Your transactions will download as a CSV file to your device.

If an error message shows, there may be a problem or missing transactions in your CSV file. Select the checkbox **Highlight extracted transactions on bank statement**. Successfully extracted transactions will be highlighted in the document viewer, allowing you to easily identify any missing transactions.

Note that Hubdoc might create multiple CSV files to meet the import requirements of the selected file format. For example, the import limit for Xero is 1,000 transactions per CSV file. If you select Xero CSV as your file format and your statement has more than 1,000 transactions, Hubdoc will export your data to a zip folder containing multiple CSV files.

If you notice an issue with your CSV data, you can [report it](Resolve-issues-with-bank-statement-extraction-in-Hubdoc.md).

Supported banks

Hubdoc can extract data from selected statement types from supported banks. This means the data extraction has been validated and high quality results are likely.

If your bank isn’t supported, you can still upload a statement, however we can’t guarantee the accuracy of the extracted data. Please carefully review the CSV before uploading it to your accounting software.

You can also request to add the bank as a supported bank by raising it as an idea in [Xero Product Ideas](https://productideas.xero.com/forums/940636-for-accountants-bookkeepers?category_id=418573), our website where you can share and support ideas for change.

The following banks are supported:

| **United States** |
| --- |
| Ally Bank Amarillo National Bank America First Credit Union Ameris AMEX Apple Card Atlantic Capital Axos Bank Bank of America Bank of Hawaii Bank of Nevada Bank of the West Bank Ozk BankUnited Banner Bank Barclays BBVA Best Buy Credit Card Bluevine BMO Harris Bank Boeing Employees Credit Union Byline Bank Capital One Centennial Bank Chase Bank Citibank Citizens Bank City National Bank Columbia Bank Comerica Bank Commerce Bank Community Banks of Colorado Consumers Credit Union Credit One Bank Discover Bank East West Bank Eastern Bank  Enterprise Bank F&M Bank Fidelity Bank Fifth Third Bank First Citizens Bank First Fed First Financial Bank First Horizon Bank | First Internet Bank First Interstate Bank First Merchants Bank First Midwest Bank First National Bank First National Bank of Omaha First National Bank of Tennessee First Premier Bank First Republic Bank First Service Bank FirstBank Financial Corporation Flagstar Bank Frost Bank GM Rewards Card Horizon Bank HSBC Huntington National Bank Interior Savings Investors Bank Island Savings jetBlue KeyBank Live Oak Bank Lloyds Bank M&T Bank Mechanics Bank Mercury Bank Montecito Bank & Trust Mountain America Credit Union Navy Federal Credit Union Nelson & District Credit Union New Republic Bank Northern Trust Novo Old National Bank One Bank of Tennessee Origin Bank Park National Bank Paypal PlainsCapital Bank PNC Bank Prairie Community Bank Premier Bank Prospera Credit Union Prosperity Bank RedWood Credit Union | Regions Bank Relay Financial Renasant Bank Rogers Bank Sam's Club Credit Card San Luis Valley Federal Bank Sandy Spring Bank Seacoast National Bank Security Service Federal Credit Union Security State Bank & Trust ServisFirst Bank Silicon Valley Bank SmartBank South State SouthStar Bank Spokane Teachers Credit Union Square Financial Services Sterling National Bank SunTrust (Truist) Synchrony Bank Synergy Credit Union Synovus TD Bank Towne Bank Truist Trustmark National Bank Umpqua Bank Union Bank United Bank United Community United Federal Credit Union USAA Federal Savings Bank U.S. Bank U.S. Century Bank Valley National Bank VyStar Credit Union WA Federal Bank Walmart Rewards Washington Trust Bank Webster Bank Wells Fargo WesBanco Bank Woodforest National Bank Zions Bancorp |

| **Canada** |
| --- |
| Affinity Credit Union Alterna Savings ATB BMO Bulkley Valley Credit Union Canadian Tire Bank Canadian Western Bank CIBC Coastal Community Credit Union Connect First Credit Union East Coast Credit Union Kootenay Savings Credit Union | MBNZ National Bank of Canada PC Financial RBC Express Revelstoke Credit Union Royal Bank of Canada Salmon Arm Savings & Credit Union Scotia Bank Servus Credit Union TD Canada Bank Trust Valley First |

## What's next?

Now you’ve extracted the transactions from your statement, [import the CSV file to Xero](Import-a-CSV-bank-statement.md) or [QuickBooks Online](https://quickbooks.intuit.com/learn-support/en-us/help-article/import-transactions/manually-upload-transactions-quickbooks-online/L0rE9OXBz_US_en_US) (QuickBooks Online website) to reconcile them.
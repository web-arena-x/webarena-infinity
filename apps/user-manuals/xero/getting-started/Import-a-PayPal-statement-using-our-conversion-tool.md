# Import a multicurrency PayPal statement

Source: https://central.xero.com/s/article/Import-a-PayPal-statement-using-our-conversion-tool

---

## Overview

- Use our conversion tool to import multicurrency PayPal transactions into Xero.
- The tool is a Microsoft Excel macro that summarises PayPal fees into a single line and sorts transactions by currency.

**1** Download the Paypal manual import conversion tool

1. Click [conversion tool](https://xero.my.salesforce.com/sfc/p/o0000000biwC/a/1N000000UbqM/AtgaCaSCjMy0smHv3mXGGF4l2aX1.lyJyyP0k0zoxf8) (ZIP, 45KB), then click **Download** above.
2. Go to your downloads folder on your computer, right click on the **PayPal manual import conversion tool.zip** folder and extract the contents.
3. In Microsoft Excel, open the CSV file you downloaded from PayPal, then copy the whole sheet (including the column headers).
4. Open the conversion tool, then paste the copied sheet into the **PayPalExtract** tab.
5. Select the **Instructions** tab, then **Click here**.
6. PC users – the macro will automatically save the CSV file on your desktop.

   Mac users – Choose the location where you'd like the file to be saved, select **Comma Separated Values(CSV)** as the format, then click **Save**. If you're importing multiple currencies, you'll need to save the file for each currency separately.

**2** Import your transactions into Xero

1. In the **Accounting** menu, select **Bank accounts**.
2. Find the PayPal account that you want to import the PayPal transactions into, click the menu icon , then select **Import a Statement**.
3. In **File to upload**, drag and drop the CSV file or click **Select file** and choose the CSV file from your computer, then click **Next**. Make sure you select the file with the correct currency for this account.
4. If prompted, assign the columns in your import file to the matching bank statement fields in Xero as follows:

   - **Date** to **Transaction Date**
   - **Time** to **No field**
   - **Name** to **Payee**
   - **Type** to **Description**
   - **Gross** to **Transaction Amount**
   - **Transaction ID** to **Reference**.
5. If prompted, select the date format used in your CSV file, then click **Next**.
6. Review the imported transactions and clear the checkbox next to any transaction you don't want to import.
7. Click **Complete import**.

## What's next?

After you import statement lines from PayPal into Xero, [reconcile your bank account](Reconcile-your-bank-account.md).
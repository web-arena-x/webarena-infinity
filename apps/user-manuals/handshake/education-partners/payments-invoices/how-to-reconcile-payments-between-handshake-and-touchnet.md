# How to Reconcile Payments Between Handshake and TouchNet

Source: https://support.joinhandshake.com/hc/en-us/articles/360012301013-How-to-Reconcile-Payments-Between-Handshake-and-TouchNet

---

If your school uses TouchNet, please review the instructions below on how you can use the External ID to link and reconcile payment reports.

### 1. Download the invoice report

You'll need to first download an invoice report from Handshake. For step by step instructions, please refer to [How to Download Invoice Reports](https://support.joinhandshake.com/hc/en-us/articles/218693718).

When generating the invoice report, enter the information specified below:

- **Start Date** - *specify the earliest date the registration was created (not the date the payment was processed)*
- **End Date** - *specify the latest date the registration was created (not the date the payment was processed)*
- **Employer name** - *leave blank*
- **Payment Status** - **paid**
- **Chargeable Type** - **Registration**

### 2. Format the invoice report

1. Open the downloaded invoice report.

2. Highlight column P.

3. Click on "Data" tab.

4. Select the "Text to Columns" option.  
![](/attachments/token/5S5jmPzyiatpSEjlm90VytqVG/?name=inline-625687985.png)

5. Click "Next".

6. Select "Comma' under the "Delimiters" section.

7. Click "Next".

8. Select "Finish".

9. Copy and paste "Charge Sessions IDs" to the newly created columns.

10. Add a new column the right of each one of the "Charge Session IDs" columns and name it "TouchNet Payment Amount".  
![](/attachments/token/f1pQ4FzDNPvzAfeoRxjyOBDq0/?name=inline800936196.png)

### 3. Merge TouchNet and invoice reports

1. Open newly formatted Invoice Report.

2. Open report from TouchNet.

3. Copy contents from TouchNet report into Invoice report after the last column of the report.

4. Click on the first "TouchNet Payment Amount column".

5. Enter in your vlookup formula to pull in the information from the TouchNet report into the "TouchNet Payments Amount" column.
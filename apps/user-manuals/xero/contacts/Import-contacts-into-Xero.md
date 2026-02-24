# Import new contacts into Xero

Source: https://central.xero.com/s/article/Import-contacts-into-Xero

---

## Overview

- To import multiple contacts to Xero, you need to first download the CSV template file from Xero, then format and save the data.

Warning

You can't delete imported contacts but you can archive them. We recommend that you test the import file in the [demo company](Use-the-demo-company.md#Web) first.

**1** Download CSV template file from Xero

1. In the **Contacts** menu, select **All contacts**.
2. At the top right corner of the screen, click the menu icon , then select **Import**.
3. Click **Download template**.

**2** Prepare and save data in the file

Open the file downloaded from Xero and enter your contacts' details. The primary contact's name must be entered, any other information is optional.

If you can, use English or the basic Roman alphabet so you can search for your contact throughout Xero.

To import your contacts as smoothly as possible:

- Make sure the data you enter goes in the correct column.
- Check that columns with character limits haven't been exceeded.
- You need to have the admin user permission to import bank account details.
- Email addresses need to be formatted correctly, eg email@domain.com.
- Split up the file if you're importing more than 1,000 contacts.

### (Optional) Format additional information

Update the formatting for any other information you're introducing.

| Column | Description | Format or entry details |
| --- | --- | --- |
| PhoneNumber | Contact's phone number | Use spaces to separate country code, area code and the number. |
| BankAccountNumber | Supplier's bank account for batch payments | Enter the full bank account number. We recommend using hyphens when formatting the number - this avoids Excel converting it to a scientific format because it's longer than 11 digits. |
| AccountsReceivableTaxCodeName | Default tax rate for invoices | Enter the exact [tax rate name](Add-or-edit-tax-rates.md). |
| AccountsPayableTaxCodeName | Default tax rate for bills | Enter the exact [tax rate name](Add-or-edit-tax-rates.md). |
| Website | Contact's website | Include http:// |
| Discount | Default sales discount % | Enter a number up to 2 decimal places. |
| DueDateBillDay | Default bill payment term (due date or days after) | Enter up to 2 numbers for the day of the month, or up to 3 numbers for days after. Also enter **DueDateBillTerm**. |
| DueDateBillTerm | Default bill payment term | Enter **Current Month** or **Following Month** or **Days After** or **Days After End of Month**. Also enter **DueDateBillDay**. |
| DueDateSalesDay | Default invoice payment term (due date or days after) | Enter up to 2 numbers for the day of the month, or up to 3 numbers for days after. Also enter **DueDateSalesTerm**. |
| DueDateSalesTerm | Default invoice payment term | Enter **Current Month** or **Following Month** or **Days After** or **Days After End of Month**. Also enter **DueDateSalesDay**. |
| SalesAccount | Default account for sales transactions | Enter just the [code from your chart of accounts](Components-of-an-account-in-your-chart-of-accounts.md). |
| PurchasesAccount | Default account for purchase transactions | Enter just the [code from your chart of accounts](Components-of-an-account-in-your-chart-of-accounts.md). |
| BrandingTheme | Default invoice template for invoices and other documents you send | Enter the name of an invoice template you've added. |
| DefaultTaxBills | Default tax treatment for purchase transactions | Enter **Inclusive** or **Exclusive** or **No Tax**. |
| DefaultTaxSales | Default tax treatment for sales transactions | Enter **Inclusive** or **Exclusive** or **No Tax**. |
| Person[x]FirstName, Person[x]LastName, Person[x]Email Person[x]IncludeInEmail | Additional people to contact | Enter details for each additional person you want to include in a contact record. To include them in emails, enter **Yes** in **IncludeInEmail**. You can only add additional people if the primary person's email address has been added. |
| TrackingName1 TrackingName2 | Add a tracking category | Enter the exact [tracking category name](Set-up-tracking-categories.md). If you’re importing tracking categories, these need to be set up in Xero first. **TrackingName** is the name of the category, for example ‘Region’. |
| SalesTrackingOption1 PurchasesTrackingOption1 SalesTrackingOption2 PurchasesTrackingOption2 | Add a tracking option | Enter the exact tracking category options. **SalesTrackingOption** and **PurchasesTrackingOption** relate to the options within the category, such as ‘North’ or ‘South’. |

### Character limits

Some columns in the import file have a limit on the number of characters you can enter. Exceeding this limit could cause an error during the import process.

| Column | Character limit |
| --- | --- |
| DDINumber: Area | 10 characters |
| BankAccountParticulars, BankAccountCode, BankAccountReference | 12 characters |
| DDINumber: Country | 20 characters |
| AccountName, POPostalCode, SAPostalCode, POCountry, SACountry, TaxNumber, CompanyNumber, BankAccountName, BankAccountNumber | 50 characters |
| Website | 200 characters |
| ContactName, FirstName, LastName, Person#FirstName, Person#LastName, POAttentionTo, SAAttentionTo, POCity, SACity, PORegion, SARegion | 255 characters |
| EmailAddress Person#Email, POAddressLine#, SAAddressLine# | 500 characters |

**3** Import your file into Xero

1. In the **Contacts** menu, select **All contacts**.
2. At the top right corner of the screen, click the menu icon , then select **Import**.
3. Drag and drop your file or, Click **Select file** and select your saved file.
4. Under **On importing an existing contact, empty fields will**, select **Be ignored**.
5. Click **Next**.
6. Review the information you're importing, then click **Complete Import**.

You can [update an individual contact's details](Edit-a-contact.md) after you've imported them.

Imported contacts are automatically categorised into the **All** contact group when first created. Once you've entered an invoice, bill or credit note transaction for a contact, Xero will automatically assign them into the **Customers** or **Suppliers** contact group. It's not possible to manually move contacts between the default groups, but you can [create a new contact group](Manage-contact-groups.md).

## What's next?

If you need to make changes to the information of several contacts, you can [update multiple contacts’ details](/s/article/Update-or-edit-multiple-contacts?userregion=true) in bulk.
# Creating a CSV file to import leads, contacts, or deals in Sell

Source: https://support.zendesk.com/hc/en-us/articles/4408838742682-Creating-a-CSV-file-to-import-leads-contacts-or-deals-in-Sell

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

You can import your contacts, leads, and deals into Zendesk Sell using a CSV file, helping you to quickly import deal information in bulk. If you are updating existing deals in bulk, see [Importing leads, contacts, and deals using a csv file](https://support.zendesk.com/hc/en-us/articles/4408845638298).

Note: You can import most field types. However, there are some fields that you cannot import (see [Field types that are unsupported for import](https://support.zendesk.com/hc/en-us/articles/4408836276890/#topic_gxd_55x_nrb)).

This article covers the following topics:

- [Preparing your CSV file](#topic_ft1_wl1_5mb)
- [Sample CSV template](#topic_orc_2n1_5mb)

Related articles:

- [Importing leads and contacts using a CSV file](https://support.zendesk.com/hc/en-us/articles/4408845638298)
- [Importing deals using a CSV file](https://support.zendesk.com/hc/en-us/articles/4408845246746)
- [Bulk updating using a CSV file](https://support.zendesk.com/hc/en-us/articles/4408836276890)

## Preparing your CSV file

When you create a list of customers to import, you'll probably generate this list from a user management system, using a CSV export facility. If you need to create the list from scratch you can use a program such as Microsoft Excel or OpenOffice.org Calc.

**To prepare your file, ensure the following**

- The file you are uploading is formatted correctly for a successful upload.
- Checkbox custom fields contain values that are "0" or "1" (which equate to No/Yes).
- Each of your CSV columns contains a header in the first row. This helps you identify the data you're mapping during the import.
- Data that you are not importing for a field, is not listed in the header row.
- The CSV file is properly formatted and saved using UTF-8 or UTF-16 character encoding, to ensure it properly handles all symbols (for example: — , “, č, ć, ł).
- There are no line breaks in your data because line breaks in the header row cause issues in the import process.
- The file size of your import is reasonable: Do not exceed 3,000 contacts per import. For example, if you have 5,000 contacts in your CSV file, consider dividing it into two imports. There is no limit on the number of contacts you can upload, or the number of CSV files that you import.
- If you want to assign a lead or contact to a user in your account, then you must include a column in your file labeled *Owner* that you will match to the *Owner* field in Sell. Owner indicates which user in your account owns a particular lead or contact.
- If you are importing deals, and associate each deal with a contact, then the contact can be either a singular contact (person) or a company contact.
 - If your deal is associated with a contact that is a person, then the contact must have a last name. If you are importing your contact's full name, the contact's name should be separated into two columns - first name and last name.
 - If your deal's contact is already in your Sell account, Zendesk will merge your existing contact with the one in your CSV file and send you an email summary of your merged data.
 - Each deal has a deal name and associated deal contact. If one or more of your deals do not have a stage listed, it will be placed in your initial pipeline stage by default.
 - During import, do not assign deals to a user in your account. The imported data is assigned to the person who imports it. You can reassign the data once the import is complete.
- If you add a company name to your contact, two contact records will be created in your Sell Contacts list - one for the person and one for the company. For this reason, importing a company name with your contact is optional.
- If you are importing deals - add a *Deal Added* column in your spreadsheet if you want to back-date Deal creation dates. This column is mapped to the *Date Added* field of your deals. If you don't include a Date Added column in your CSV, the date the deal was created will default to the day that your import is completed. Keep the following guidelines in mind when creating your Date Added column:
 - If your account uses the American date format with a 12hr time format, Sell will only match the date when it is written as MM/DD/YYYY.
 - If your account uses a European date format with a 24hr time format, Sell will only match the date when it is written as DD/MM/YYYY.

 The following table lists examples of fields that you can include in the file.

Table 1. User import data

   | Field | Description |
| --- | --- |
| first name | Customer's first name. Attention: When importing leads, if a first name is provided, then a last name must also be included. |
| last name | Customer's last name, (surname). **Last Name or Company Name required for importing new Leads**. **Last Name required for Contacts.** |
| name | Customer's full name - can be automatically split into first/last name during the import process. **Note:** Zendesk Sell categorizes contacts as Person Contacts (Employees) and Company Contacts. The First Name and Last Name fields need to be included in each imported file - so Zendesk knows how to name your contacts. Sell also provides the option to import First Name and Last Name separately during the import mapping process. Company contacts do not need a first and last name, only a name under a Company Name field. |
| mobile number | Mobile phone number for the Lead/Contact. |
| work number | Work phone number for the Lead/Contact. |
| email address | Customer's full email address, (for example: user@mycompany.com). You can give customers more than one email address with additional email fields. |
| company name | **Last Name or Company Name required for importing new Leads**. Customer's company name. **Note:** If you want to associate contacts with a company, include a separate column in your file that includes Company Name. Upon importing, Sell will match Person Contacts to Company Contacts, so that your Person Contacts appear as Employees when viewing the Companies in Sell. If you import Person Contacts without mapping a Company Name, these Person Contacts will be imported without an associated Company Contact. |
| title | Customer's job title. |
| source (Lead) | Channel from which the lead or deal was created (see [Tracking lead.and deal sources](https://support.zendesk.com/hc/en-us/articles/4408839415834)) This is a drop-down field, if an existing Source does not exist that matches your imported data, it can automatically be added to your existing list of Sources, and the mapping can be edited to modify the content to an existing Source if preferred. |
| industry | Customer's Industry to allow you to categorize and filter leads and contacts. This is a drop-down field, if an existing Industry does not exist that matches your imported data, it can automatically be added to your existing list of industries, and the mapping can be edited to modify the content to an existing industry if preferred. |
| notes | Notes relating to the customer. You can add notes to the lead, contact, or deal card as notes or by adding another field, (such as: Description). |
| street (address) | Customer's street address. **Note:** When importing an address to a Contact, we suggest dividing the specific details of the address into multiple columns in your CSV file. This will allow you to sort or filter by these fields in Sell. You will want to make sure the following fields are separated into their own columns in your file before importing: street address, city, region/state, zip/postal code, and country. |
| city | Customer's city. |
| postal code or zip code | Customer's postal or zip code. |
| state/region | Customer's state or region. |
| country | Customer's country. (Drop down field) |
| company address | Address for Customer's Company. **Note:** If you’re importing different addresses for Person Contacts and Company Contacts, you'll need to create separate columns in your file that include Person Address columns and Company Address columns. Person Address columns you’ll want to include are person address (street address), person city, person region/state, person country, whereas Company Address columns should include company street, company city, company region/state, etc. |
| tags | Specific tags added to lead, contact, or deal to help categorize customers and quickly filter in Smart Lists and reports (see [Using tags on leads, contacts, and deals](https://support.zendesk.com/hc/en-us/articles/4408838233882)). Separate each tag with a comma. |
| owner | Sell user who owns the lead, contact, or deal. |
| website | Customer's website. |
| skype | An embedded link to Customer's Skype account. |
| facebook | An embedded link to Customer's Facebook account. |
| twitter | An embedded link to Customer's X (formerly Twitter) account. |
| linkedin | An embedded link to Customer's LinkedIn account. |
| fax | Customer's fax number. |
| description | To add a description to the Customer's profile. |
| custom field | Custom fields can be matched to existing custom fields (or created during import). The following custom fields are supported:   - Single Line Text - Paragraph - Number - Dropdown - Date - Multiselect - Email - Phone - Address - URL - Checkbox (with values of "0" or "1") |

The following suggestions will also help you keep your import under control.

- There is no limit to how many records you can import at a time. However, it is good practice to split a large CSV data file into smaller files when importing. This ensures the import doesn't take too long and you can also check to see if each file is importing correctly. Start with a 20k file, then if everything's all right, increase the file size to 30-50k for the subsequent files.
- Ensure that there are no line breaks in your header row, or the import will not import successfully.

### Sample CSV template

If you do not already have a CSV file, or you want to start from scratch, you can use the Zendesk CSV template to populate your deals using a program such as Excel. [Download sample CSV](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/deals-and-contacts-import-template-1.csv)
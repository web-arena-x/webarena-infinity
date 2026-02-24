# Update the Company or User Import Template

Source: https://v2.support.procore.com/product-manuals/directory-company/tutorials/update-the-company-or-user-import-template

---

##### IMPORTANT!

In order to protect the integrity of your companyâs data, Procore Employees are restricted from modifying the data that clients submit in all Procore Import Templates. This restriction applies to all data modifications, including correcting typographical errors. If Procore determines that errors are present in any Procore Import Template that you submit to Procore, it will be returned to you for correction. **Please note that the import process may take up to 72 hours to process.**

## Background

You can import vendor or user records to the Company or Project level Directory tool by using Procore Imports or by submitting a request to Procore. When importing users to Procore, you can choose to have them imported at the Company or Project level. If you decide to import users to a project, those records will automatically be added to Procore's Company Directory.

## Things to Consider

- **Required User Permissions**

 - *To update the import template:* None. This task is performed in Microsoft Excel.
- **General Import Requirements**

 - For general considerations about updating an import template, see [How do I prepare my data for import into Procore?](/product-manuals/procore-imports/tutorials/prepare-your-data-for-import-into-procore)
 - The XLSX file must be formatted as a table.
 - The first line of the table must include the header.
 - The import process will fail if you change the column headers in any way, including adding, removing, reordering, or modifying the values.
 - There is no limit to the number of rows you can import. However, an entire row cannot be blank.
 - Procore interprets a blank value as a 'No' entry.
- **Company Import Template Requirements**

 - **Required Row Data**

    - Each row requires a value in the **Name** column in order to create the company record. Other values in the same row can be blank.
    - Each row in the table corresponds to an individual vendor.
 - **Required Column Data**

    - If your company account has enabled the Company level ERP Integrations tool, your template is set up to automatically add one of these column headers: Sage 300 CREÂ® Cost Codes, QuickBooksÂ® Cost Codes, or timberline\_vendor\_id (this field is included only for customers with the legacy Sage Timberline Office (STO) integration).
- **User Import Template Requirements**

 - **Required Row Data:**

    - Each row in the table corresponds to an individual user.
    - Each row in the table corresponds to a contact record (a.k.a., a user).
    - At a minimum, each record requires a value for the contact's **First Name**, **Last Name**, **Email Address**, and **Permission Template**.

## Prerequisites

- Learn about the import process. See [Request Company and People Imports](/process-guides/request-company-and-people-imports/).
- Complete the steps in [Download the Company or User Import Template](/process-guides/request-company-and-people-imports/download-import-template).
- Set up your company's Work Breakdown Structure. See [Create Your Company's Default Work Breakdown Structure](/product-manuals/admin-company/tutorials/create-your-companys-default-work-breakdown-structure).

## Steps

- Update the Company Import Template
- Update the User Import Template

### Update the Company Import Template

1. Download the User Import Template from the Procore web application. See [Download the Company or User Import Template](/process-guides/request-company-and-people-imports/download-import-template).
2. Open the XLSX template in Microsoft Excel.
3. Complete the data entry as follows: 
   *Note:* An asterisk (\*) denotes a required field.

   - **\*Name:** Enter the vendor/company name exactly as you want it to appear in the Directory tool. Company names are case- and punctuation-sensitive. If your company has enabled the Company level ERP Integrations tool, be aware that your entry is synced with an integrated ERP system that imposes character limits on imported project names. For details, see [What is the maximum character length for a 'Company Name' in the Directory tool?](/faq-what-is-the-maximum-character-length-for-a-company-name-in-the-directory-tool) ***Important!*** To avoid creating a duplicate entry when importing entries to a Directory with existing records:

     - If your company is importing data using the ID column (instead of the Name column), Procore will overwrite any existing data for that vendor in the Directory.
     - If you have existing data in the Directory, enter the name exactly as it appears in the Directory.
   - **Entity Type:** Select ABN ([Australian Business Number](/glossary-of-terms)) or EIN ([Employer Identification Number](/glossary-of-terms)) from the drop-down list. Then enter the entity's identification number in the **Entity Id** field.
   - **Entity Id:** If you select an option from the **Entity Type** list, you must enter the appropriate number here. See [Australian Business Number](/glossary-of-terms) or [Employer Identification Number](/glossary-of-terms).
   - **Address:** Enter the street or mailing address for the vendor/company.
   - **City:** Enter the full city name (e.g., San Diego, Seattle, Westchester).
   - **State:** Enter the two-letter state or territory abbreviation (e.g., CA, WA, NY). See [U.S. State Abbreviations](https://about.usps.com/who-we-are/postal-history/state-abbreviations.pdf).
   - **Zip:** Enter the company's Zip code. 
     *Tip!* If a Zip code contains a leading zero (e.g., 92129, 98122, 10503), there is a known issue in Microsoft Excel related to displaying numbers. See the Microsoft Office web site for details: [Displaying Numbers as Postal Codes](https://support.office.com/en-us/article/Display-numbers-as-postal-codes-61b55c9f-6fe3-4e54-96ca-9e85c38a5a1d).
   - **Country:** Enter the full country name of the company's address (e.g., United States or Canada).
   - **Business Phone:** Enter the vendor's/company's business telephone number using the [NANP](/glossary-of-terms) number format (e.g., 805-555-0100). Do not use SPACES or parentheses as delineators.
   - **Fax Number:** Enter the vendor's/company's business facsimile number using the [NANP](/glossary-of-terms) number format (e.g., 805-555-0101). Do not use SPACES or parentheses as delineators.
   - **Company Email Address:** Enter one (1) full email address for the vendor/company. Typically, this is a general business email address (e.g., [info@example.com](mailto:info@example.com)). This field does not support the entry of multiple email addresses.
   - **Primary Contact Email Address:** Enter one (1) full email address for the primary contact at the vendor/company. Typically, this is a person's email address (e.g., [jsmith@example.com](mailto:jsmith@example.com)). This field does not support the entry of multiple email addresses.   
     ***Important!*** The **primary\_contact** must be an email address and the user associated with the email address must have a record in the Directory tool.
   - **Default Bid Invitee Email Address:** Enter the email address for the default bid invitee for that company. If there are multiple invitees, use the pipe symbol (|) as a separator and include a single SPACE on either side of the pipe symbol (e.g., [jsmith@example.com](mailto:jsmith@example.com) | [mjones@example.com](mailto:mjones@example.com)).
   - **DBA Name:** Enter the company's Doing Business As name.
   - **Website:** Enter the vendor's/company's website.
   - **Trades:** Enter the vendor/company trade (e.g., Concrete or Masonry). If there are multiple trades, use the pipe symbol (|) as a separator and include a single SPACE on either side of the pipe symbol (e.g., Concrete | Masonry). 
     *Notes:*

     - To type the pipe symbol (|), hold down your keyboard's SHIFT key and then press the backslash (\) key. On most US English keyboards, the backslash key is directly above ENTER or RETURN. However, your keyboard may be different.
     - Trades let you filter records in the Project Directory. See [Add or Delete Trades](/product-manuals/admin-company/tutorials/add-a-custom-trade).
     - They and also let you quickly create bid lists with Procore's Bidding tool. See [Export a Bid Package's Bid List to a PDF or CSV](/product-manuals/bidding-project/tutorials/export-a-bid-packages-bid-list))
   - **Business Type Considerations** *Note:* If local, federal, or state regulations restrict your organization from the collection of this data, you must leave this cell blank.

     - **Authorized Bidder:** Enter 'Yes' to indicate if the vendor is authorized to bid on all your company projects (if you are importing at the Company level) or a specific project (if you are importing at the Project level)
     - **Union Member:** Enter 'Yes' to indicate if the company is a member of a union.
     - **Prevailing Wage:** Enter 'Yes' to indicate if the company is subject to general prevailing wage determinations.
     - **Small Business:** Enter 'Yes' to indicate if the company is certified by the U.S. Small Business Administration as a Small Business Enterprise.
     - **African American Business:** Enter 'Yes' to indicate if the company is certified by the U.S. Small Business Administration as a Minority Owned Business (e.g., African American Business Enterprise).
     - **Asian American Business:** Enter 'Yes' to indicate that the company is certified by the U.S. Small Business Administration as a Minority Owned Business (e.g., Asian American Business Enterprise).
     - **Hispanic Business:** Enter 'Yes' to indicate if the company is certified by the U.S. Small Business Administration as a Minority Owned Business (e.g., Hispanic Business Enterprise).
     - **Native American Business:** Enter 'Yes' to indicate if the company is certified by the U.S. Small Business Administration as a Minority Owned Business (e.g., Native American Business Enterprise).
     - **Woman's Business:** Enter 'Yes' to indicate if the company is certified by the U.S. Small Business Administration as a Minority Owned Business (e.g., Women Owned Business Enterprise).
     - **Disadvantaged Business:** Enter 'Yes' to indicate if the company is certified by the U.S. Small Business Administration as a Minority Owned Business (e.g., Disadvantaged Business Enterprise).
     - **Historically Underutilized Business:** Enter 'Yes' to indicate if the company is certified by the U.S. Small Business Administration as a Minority Owned Business (e.g., Historically Underutilized Business Enterprise).
     - **Minority Business Enterprise:** Enter 'Yes' to indicate if the company is certified by the U.S. Small Business Administration as a Minority Owned Business Enterprise.
     - **Service-Disabled Veteran-Owned Small Business:** Enter 'Yes' to indicate that the company is certified by the U.S. Small Business Administration as a Minority Owned Business (e.g., Service-Disabled Veteran-Owned Small Business).
     - **8a Business Enterprise:** Enter 'Yes' to indicate that the company is certified by the U.S. Small Business Administration as a Minority Owned Business (e.g., Socially- or Economically- Disadvantaged Business under the 8(a) program).
     - **Affirmative Action**: Enter 'Yes' to indicate that the company is subject to affirmative action when bidding.
     - **Certified Business Enterprise:** Enter 'Yes' to indicate that the company registered with the Department of Small and Local Business Developmentâs (DSLBDâs) Certified Business Enterprise ([CBE](/glossary-of-terms)) Program.
   - **Prequalified:** Enter 'Yes' to indicate that the company is on the relevant Prequalified Contractors Listing for the state in which it will be doing business.
   - **License Number:** Enter the company's state contractors license.
   - **Tags Keywords:** Enter any keyword tags for the vendor here. Separate entries with a comma (,). You can enter up to 255 characters in this field.
   - **Cost Codes:** 

     Enter one or more cost codes. Use a dash (-) to separate each tiered segment item on the 'Cost Code' segment and a pipe (|) symbol to separate each individual cost code entry. Always include a SPACE on either side of the pipe (|) symbol.

     *Notes:*In Procore's [WBS](https://support.procore.com/products/online/work-breakdown-structure), the 'Cost Code' segment is a [tiered segment](/faq-what-is-the-difference-between-a-flat-and-tiered-segment-in-procores-wbs) in your [budget code structure](/faq-what-is-a-budget-code-structure-in-procores-wbs). In the import template, tiers within a segment must be delimited by a dash (-). Depending on your company's specific budget code structure, your cost code entries may be different than these examples:

     - If your company or project level 'Cost Code' segment has two (2) tiers, the first tier might represent a Division number (01) in the CSI MasterFormat. The second tier includes nested segment items with the 'Division', which are considered cost codes in the MasterFormat (000, 002, 010, and so on). Using this example, your cost code entry in the import template would look like: 01-000
     - If your 'Cost Code' segment has three (3) tiers, the first tier might represent the Division number (01) in the CSI MasterFormat, the second tier is a sub division (10), and the third tier is the cost code (010), so your cost code entry would look like: 01-10-010
     - If you want to enter multiple cost codes to associate with the company, separate each code with the pipe (|) symbol and be sure to include a single SPACE on either side of the pipe (|) symbol. For example: 01-000| 01-002| 01-010 **or** 01-10-000 | 01-10-002 | 01-10-010

     To learn more about Procore's default 'Cost Code' segment, see [What are Procore's default cost codes?](/faq-what-are-procores-default-cost-codes) and [Work Breakdown Structure](https://support.procore.com/products/online/work-breakdown-structure).

     Cost Codes: Import Template Entry
   - **ERP Integrations Cost Code List**

     - **Select Integration/None:** Select this option if your company has NOT enabled the ERP Integrations tool.   
       *Note:* You will also select this option if you are using the Procore + ViewpointÂ® SpectrumÂ® or Procore + Integration by Ryvit. These integrations do NOT currently allow you to import cost codes (i.e., phase codes in Integration by Ryvit with a vendor record.
     - **Sage 300 CRE:** Select this option if you are using the Procore + Sage 300 CREÂ® and want to associate cost codes with a specific vendor record. See [Sage 300 CREÂ®](https://support.procore.com/products/online/user-guide/company-level/erp-integrations/sage-300-cre).
     - **QuickBooks:** Select this option if you are using the Procore + QuickBooksÂ® and want to associate your QuickBooks costs codes with a specific vendor. See [QuickBooksÂ®](https://support.procore.com/products/online/user-guide/company-level/erp-integrations/quickbooks).
     - **timberline\_vendor\_id:** Select this option if you are using the legacy version of the Procore + Sage Timberline Office (STO) integration. This is NOT common and is also NOT related to the current Procore + Sage 300 CREÂ® integration. 
       *Note*: Although it not commonly used, you can also add import data to this column if you are storing the Timberline Vendor ID (a.k.a., Accounting Vendor ID) in your vendor records.
     - If your company has enabled the Company level ERP Integrations tool for a supported ERP system, this column heading corresponds to your specific ERP system. To change the column heading, click the **Instructions** tab. Then scroll to the 'To Complete This Template' section. Then, next to step 2, select one of these options:
4. **Id:** This field is for a vendor's pre-designated Procore unique ID that will only populate when you export the vendors list from your Directory.
5. Save your updates by clicking **File**, then **Save**.
6. When your data entry is complete, continue with [Send a Company or User Import Template to Procore](/process-guides/request-company-and-people-imports/submit-completed-template).

### Update the User Import Template

1. Download the User Import Template from the Procore web application. See [Download the Company or User Import Template](/process-guides/request-company-and-people-imports/download-import-template).
2. Open the XLSX template in Microsoft Excel.
3. Complete the data entry as follows: 
   *Notes:*

   - An asterisk (\*) denotes a required field.
   - If you are pulling your user source data from a different spreadsheet, you MUST always separate the user's first and last name into separate cells. To learn how to do this before adding the data to the template, visit this article on the Microsoft Office Support site for assistance: [Split Text Into Different Cells](https://support.office.com/en-us/article/Split-text-into-different-cells-30b14928-5550-41f5-97ca-7a3e9c363ed7)
   - When you begin your data entry, the template's built-in data validation highlights the required cells with errors (i.e., missing data entry) in light RED until there are no detectable errors.

     - **\*First Name:** Enter the user's first name exactly as you want it to appear in the Directory tool (e.g., John). 
       ***Important!*** First names are case and punctuation sensitive.
     - **\*Last Name:** Enter the user's surname exactly as you want it to appear in the Directory tool (e.g., Smith). 
       ***Important!*** Last names are case and punctuation sensitive.
     - **\*Email Address:** Enter the user's full email address (e.g., [jsmith@example.com](mailto:jsmith@example.com)) 
       ***Important!*** The email address must be unique to each individual. It is also used as the [unique identifier](/glossary-of-terms) for the user's profile.
     - **\*Permission Template:** Enter the name of the project permissions template that will be applied to each user record. You must enter the name exactly as it appears in Procore.
     - **Company:** Enter the vendor/company name exactly as you want it to appear in the Directory tool. Company names are case- and punctuation-sensitive in Procore. 
       ***Important!*** If the vendor/company already exists in the Directory tool, enter the name exactly as it appears in the Directory to avoid creating a duplicate. See [Add a Company to the Company Directory](/product-manuals/directory-company/tutorials/add-a-company-to-the-company-directory).
     - **Is Employee**: If the user is an employee of your company, select **Yes** from the list box. If the user is affiliated with a subcontractor, supplier, or vendor, select **No** from the list box.
     - **Employee Id:** If you selected **Yes** in the **Is Employee** field, you have the option of entering an employee ID. If you selected **No** in the **Is Employee** field, leave this field blank *Note*: If you attempt to enter an **Employee ID** without selecting Yes in the **Is Employee** field, the data validation in the worksheet will highlight the error in light RED.
     - **Job Title:** Enter the user's professional title exactly as you want it to appear in the Directory tool. You can enter up to 255 alphanumeric characters.
     - **Address:** Enter the user's address (e.g., company or mailing address) exactly as you want it to appear in the Directory tool.
     - **City:** Enter the full city name for the user's address (e.g., La Jolla).
     - **State:** Enter the two-letter state or territory abbreviation (e.g., CA). See [U.S. State Abbreviations](https://about.usps.com/who-we-are/postal-history/state-abbreviations.pdf). If you enter a state abbreviation, you will be required to enter a **Country Name**.
     - **Zip:** Enter the ZIP or postal code. 
       ***Tip!*** If Microsoft Excel cuts off the leading zeros in the code, right-click the cell (or cell range) and choose 'Format Cells' from the shortcut menu. Next, under 'Number,' click 'Special.' Then apply the 'Zip Code' or 'Zip Code + 4' format. For more details, visit the Microsoft Office web site for instructions: [Displaying Numbers as Postal Codes](https://support.office.com/en-us/article/Display-numbers-as-postal-codes-61b55c9f-6fe3-4e54-96ca-9e85c38a5a1d).
     - **Country:** Spell out the full country name. 
       ***Important!*** Do NOT use abbreviations (e.g., United States or Canada). You MUST always spell out the full country name.
     - **Business Phone:** Enter the user's business telephone number using the number format (e.g., 805-555-0100). How you enter the phone number here determines how it will appear in Procore.
     - **Business Phone Extension:** Enter the user's business telephone number's extension.
     - **Fax Number:** Enter the user's business facsimile number using the number format (e.g., 805-555-0106). How you enter the phone number here determines how it will appear in Procore.
     - **Mobile Phone:** Enter the user's mobile telephone number using the number format (e.g., 805-555-0107). How you enter the phone number here determines how it will appear in Procore.
     - **Notes:** Add up to 255 alphanumeric characters.   
       *Note*: The notes you enter here populate the 'Tags / Keywords' field on the person's profile. Users can later search the notes field for matches using different Procore tools.
     - **Work Classification:** Enter the user's work classification. To learn which Procore tools interact with classifications, see [Which Procore tools support 'Classifications'?](/faq-which-procore-tools-support-classifications)
     - **Company Permissions Template:** Enter the name of the company permissions template that will be applied to each user record. You must enter the name exactly as it appears in Procore. See [Create a Company Permissions Template](/product-manuals/permissions-company/tutorials/create-a-company-permissions-template).
4. Save your updates by clicking **File**, then **Save**.
5. When your data entry is complete, continue with [Send a Company or User Import Template to Procore](/process-guides/request-company-and-people-imports/submit-completed-template).
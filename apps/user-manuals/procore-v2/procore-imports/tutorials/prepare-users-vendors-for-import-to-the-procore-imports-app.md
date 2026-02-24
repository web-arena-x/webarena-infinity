# Prepare Project Users & Vendors for Import to the Procore Imports App

Source: https://v2.support.procore.com/product-manuals/procore-imports/tutorials/prepare-users-vendors-for-import-to-the-procore-imports-app

---

## Background

You can use the Procore Imports App to self-import either a list of users or vendors into your company's or project's Directory tool. This will add as many contacts to your project as you need without having to manually add each contact in Procore.

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the Company Directory.  
    *Note*: Granular Permissions are not supported in the Procore Imports application.

## Steps

- Download the Users or Vendors Import Template
- Format the Users Import Template
- Format the Vendors Import Template

#### Download the Users or Vendors Import Template

1. Choose from the following options:

   - **Download the Users Import Template:** [import-users.xlsx](https://procore-imports-templates.s3.us-east-1.amazonaws.com/import%5Ftemplate%5Fusers%5Fv3.xlsx)  
     *Note:* In Procore, a "user" is an individual person who will be logging into Procore, such as your employee or an employee of another company who will be accessing your project.
   - **Download the Vendors Import Template:** [import-vendors.xlsx](https://procore-imports-templates.s3.amazonaws.com/import%5Ftemplate%5Fvendors.xlsx)  
     *Note:* In Procore, a "vendor" is another company or entity that your company interacts with during a project.

#### Format the Users Import Template

1. See below considerations when filling out the template.

   - **Required Row Data**:

     - Each row in the table corresponds to an individual user.
     - Each row in the table corresponds to a contact record (a.k.a., a user). At a minimum, each record requires a value for the contact's **First Name**, **Last Name**, **Email Address**, and **Permission Template**. The column headings for the required fields have a RED background. All other columns and cells in a single row may be left blank.
     - ***Important!*** There is no limit to the number of rows you can import. However, rows cannot be blank.
   - **Required Column Data**:  
      The first line of the table must include the header, which defines the fields in the Excel table and your company's contact database in Procore.

     - The import process will fail if you modify values in column headers.
     - The import process will fail if you insert new columns, move columns, or remove columns from the template.
     - The import process will fail if you change the column header order in the template.
2. Complete the import template.  
   *Notes:*

   - An asterisk (\*) denotes a required field.
   - If you are pulling your user source data from a different spreadsheet, you MUST always separate the user's first and last name into separate cells. To learn how to do this before adding the data to the template, visit this article on the Microsoft Office Support site for assistance: [Split Text Into Different Cells](https://support.office.com/en-us/article/Split-text-into-different-cells-30b14928-5550-41f5-97ca-7a3e9c363ed7).

     - **\*First Name:** Enter the user's first name exactly as you want it to appear in the Directory tool (e.g., John).  
       ***Important!*** First names are case- and punctuation-sensitive.
     - **\*Last Name:** Enter the user's surname exactly as you want it to appear in the Directory tool (e.g., Smith).  
       ***Important!*** Last names are case- and punctuation-sensitive.
     - **\*Email Address:** Enter the user's full email address (e.g., [jsmith@example.com](mailto:jsmith@example.com))  
       ***Important!*** The email address must be unique to each individual. It is also used as the [unique identifier](/glossary-of-terms) for the user's profile.
     - **\*Permission Template:** Enter the name of the project permissions template that will be applied to each user record. You must enter the name exactly as it appears in Procore.
     - **Company:** Enter the vendor/company name exactly as you want it to appear in the Directory tool. Company names are case- and punctuation-sensitive in Procore.   
       ***Important!*** If the vendor/company already exists in the Directory tool, enter the name exactly as it appears in the Directory to avoid creating a duplicate. See [Add a Company to the Company Directory](/product-manuals/directory-company/tutorials/add-a-company-to-the-company-directory).
     - **Is Employee**: If the user is an employee of your company, select **Yes** from the list box. If the user is affiliated with a subcontractor, supplier, or vendor, select **No** from the list box.
     - **Employee Id:** If you selected **Yes** in the **Is Employee** field, you have the option of entering an employee ID. If you selected **No** in the **Is Employee** field, leave this field blank.   
       *Note*: If you attempt to enter an **Employee Id** without selecting Yes in the **Is Employee** field, the data validation in the worksheet will highlight the error in light RED.
     - **Job Title:** Enter the user's professional title exactly as you want it to appear in the Directory tool. You can enter up to 255 alphanumeric characters.
     - **Address:** Enter the user's address (e.g., company or mailing address) exactly as you want it to appear in the Directory tool.
     - **City:** Enter the full city name for the user's address (e.g., La Jolla).\* **State:** Enter the two-letter state or territory abbreviation (e.g., CA). See [U.S. State Abbreviations](https://about.usps.com/who-we-are/postal-history/state-abbreviations.pdf). If you enter a state abbreviation, you will be required to enter a **Country Name**.
     - **Zip:** Enter the ZIP or postal code.  
       ***Tip!*** If Microsoft Excel cuts off the leading zeros in the code, right-click the cell (or cell range) and choose 'Format Cells' from the shortcut menu. Next, under 'Number,' click 'Special.' Then apply the 'Zip Code' or 'Zip Code + 4' format. For more details, visit the Microsoft Office web site for instructions: [Displaying Numbers as Postal Codes](https://support.office.com/en-us/article/Display-numbers-as-postal-codes-61b55c9f-6fe3-4e54-96ca-9e85c38a5a1d).
     - **Country:** Spell out the full country name.  
       ***Important!*** Do NOT use abbreviations (e.g., United States or Canada). You MUST always spell out the full country name.
     - **Business Phone:** Enter the user's business telephone number using the [NANP](/glossary-of-terms) number format (e.g., 805-555-0100). How you enter the phone number here determines how it will appear in Procore.\* **Business Phone Extension:** Enter the user's business telephone number's extension.
     - **Fax Number:** Enter the user's business facsimile number using the [NANP](/glossary-of-terms) number format (e.g., 805-555-0106). How you enter the phone number here determines how it will appear in Procore.
     - **Mobile Phone:** Enter the user's mobile telephone number using the [NANP](/glossary-of-terms) number format (e.g., 805-555-0107). How you enter the phone number here determines how it will appear in Procore.
     - **Notes:** Add up to 255 alphanumeric characters.   
       *Note*: The notes you enter here populate the 'Tags / Keywords' field on the person's profile. Users can later search the notes field for matches using different Procore tools: [Search and Filter the Company Directory](/product-manuals/directory-company/tutorials/search-and-filter-the-company-directory), [Search and Filter the Project Directory](/product-manuals/directory-project/tutorials/search-and-filter-the-project-directory), and [Search for and Invite Bidders](/product-manuals/bidding-project/tutorials/search-for-and-invite-bidders).
     - **Work Classification:** Enter the user's work classification. Your entry must match the 'Classifications' list in the Company Admin tool (see [Add a Classification](/product-manuals/admin-company/tutorials/add-a-classification)). Classifications also interact with the Project level Timesheets tool. See [Enable Classifications on a Project](/product-manuals/admin-project/tutorials/enable-classifications-on-a-project).
     - **Company Permissions Template:** Enter the name of the company permissions template that will be applied to each user record. You must enter the name exactly as it appears in Procore. See [Create a Company Permissions Template](/product-manuals/permissions-company/tutorials/create-a-company-permissions-template).
3. Respond to Data Validation Alerts  
    If your data entry does NOT meet Procore's import criteria, the invalid cell will be highlighted in red.

#### Format the Vendors Import Template

1. See below for considerations when filling out the template.

   - **Required Row Data**:  
     ***Important!*** There is no limit to the number of rows you can import. However, rows cannot be blank.

     - Each row requires a value in the **Name** column in order to create the company record. Other values in the same row can be blank.
     - Each row in the table corresponds to an individual vendor.
     - The import process will fail if you change the column header order in the template.
     - The import process will fail if you insert new columns, move columns, or remove columns from the template.
     - The import process will fail if you modify values in column headers.
   - **Required Column Data**:

     - The first line of the table must include the *header*, which defines the fields in the Excel table and your company's vendor database in Procore.
     - The import process will fail if you modify values in column headers.
     - The import process will fail if you insert new columns, move columns, or remove columns from the template.
     - The import process will fail if you change the column header order in the template.
2. Complete the import template.  
   *Note:* An asterisk (\*) denotes a required field.

   - **\*Name:** Enter the vendor/company name exactly as you want it to appear in the Directory tool. Company names are case- and punctuation-sensitive. If your company has enabled the Company level ERP Integrations tool, be aware that your entry is synced with an integrated ERP system that imposes character limits on imported project names. For details, see [What is the maximum character length for a 'Company Name' in the Directory tool?](/faq-what-is-the-maximum-character-length-for-a-company-name-in-the-directory-tool)  
     ***Important!*** To avoid creating a duplicate entry when importing entries to a Directory with existing records:

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
   - **Business Phone:** Enter the vendor's/company's business telephone number using the [NANP](/glossary-of-terms) number format (for example, 805-555-0100). Do not use SPACES or parentheses as delineators.
   - **Fax Number:** Enter the vendor's/company's business facsimile number using the [NANP](/glossary-of-terms) number format (for example, 805-555-0101). Do not use SPACES or parentheses as delineators.
   - **Company Email Address:** Enter one (1) full email address for the vendor/company. Typically, this is a general business email address (for example, [info@example.com](mailto:info@example.com)). This field does not support the entry of multiple email addresses.
   - **Primary Contact Email Address:** Enter one (1) full email address for the primary contact at the vendor/company. Typically, this is a person's email address (e.g., [jsmith@example.com](mailto:jsmith@example.com)). This field does not support the entry of multiple email addresses.   
     ***Important!*** The **primary\_contact** must be an email address and the user associated with the email address must have a record in the Directory tool.
   - **Default Bid Invitee Email Address:** Enter the email address for the default bid invitee for that company. If there are multiple invitees, use the pipe symbol (|) as a separator and include a single SPACE on either side of the pipe symbol (e.g., [jsmith@example.com](mailto:jsmith@example.com) | [mjones@example.com](mailto:mjones@example.com)).
   - **DBA Name:** Enter the company's Doing Business As name.
   - **Website:** Enter the vendor's/company's website.
   - **Trades:** Enter the vendor/company trade (e.g., Concrete or Masonry). If there are multiple trades, use the pipe symbol (|) as a separator and include a single SPACE on either side of the pipe symbol (e.g., Concrete | Masonry).  
     *Notes:*

     - To type the pipe symbol (|), hold down your keyboard's SHIFT key and then press the backslash (\) key. On most US English keyboards, the backslash key is directly above ENTER or RETURN. However, your keyboard may be different.
     - Trades let you filter records in the Project Directory. See [Add or Delete Trades](/product-manuals/admin-company/tutorials/add-a-custom-trade). They and also let you quickly create bid lists with Procore's Bidding tool. See [Export a Bid Package's Bid List to a PDF or CSV](/product-manuals/bidding-project/tutorials/export-a-bid-packages-bid-list)).
   - **Business Type Considerations**:  
     *Note*: If local, federal, or state regulations restrict your organization from the collection of this data, you must leave this cell blank.

     - **Authorized Bidder:** Select 'Yes' to indicate if the vendor is authorized to bid on all your company projects (if you are importing at the Company level) or a specific project (if you are importing at the Project level). Select 'No' to indicate the vendor is not an authorized bidder.
     - **Union Member:** Select 'Yes' or 'No' to indicate if the vendor is a member of a union.
     - **Prevailing Wage:** Select 'Yes' to denote that the company is subject to general prevailing wage determinations. Select 'No' to indicate the company is not subject to these determinations.
     - **Small Business:** Select 'Yes' to denote that the company is certified by the U.S. Small Business Administration as a Small Business Enterprise. Select 'No' to indicate the company is not certified as a small business. Procore interprets a blank value as a 'No' entry.
     - **African American Business:** Select 'Yes' to denote that the company is certified by the U.S. Small Business Administration as a Minority Owned Business (e.g., African American Business Enterprise). Select 'No' to denote that the company is not certified. Procore interprets a blank value as a 'No' entry.
     - **Asian American Business:** Select 'Yes' to denote that the company is certified by the U.S. Small Business Administration as a Minority Owned Business (e.g., Asian American Business Enterprise). Select 'No' to denote that the company is not certified. Procore interprets a blank value as a 'No' entry.
     - **Hispanic Business:** Select 'Yes' to denote that the company is certified by the U.S. Small Business Administration as a Minority Owned Business (e.g., Hispanic Business Enterprise). Select 'No' to denote that the company is not certified. Procore interprets a blank value as a 'No' entry.
     - **Native American Business:** Select 'Yes' to denote that the company is certified by the U.S. Small Business Administration as a Minority Owned Business (e.g., Native American Business Enterprise). Select 'No' to denote that the company is not certified. Procore interprets a blank value as a 'No' entry.
     - **Woman's Business:** Select 'Yes' to denote that the company is certified by the U.S. Small Business Administration as a Minority Owned Business (e.g., Women Owned Business Enterprise). Select 'No' to denote that the company is not certified. Procore interprets a blank value as a 'No' entry.
     - **Disadvantaged Business:** Select 'Yes' to denote that the company is certified by the U.S. Small Business Administration as a Minority Owned Business (e.g., Disadvantaged Business Enterprise). Select 'No' to denote that the company is not certified. Procore interprets a blank value as a 'No' entry.
     - **Historically Underutilized Business:** Select 'Yes' to denote that the company is certified by the U.S. Small Business Administration as a Minority Owned Business (e.g., Historically Underutilized Business Enterprise). Select 'No' to denote that the company is not certified. Procore interprets a blank value as a 'No' entry.
     - **Minority Business Enterprise:** Select 'Yes' to denote that the company is certified by the U.S. Small Business Administration as a Minority Owned Business Enterprise. Select 'No' to denote that the company is not certified. Procore interprets a blank value as a 'No' entry.
     - **Service-Disabled Veteran-Owned Small Business:** Select 'Yes' to denote that the company is certified by the U.S. Small Business Administration as a Minority Owned Business (e.g., Service-Disabled Veteran-Owned Small Business). Select 'No' to denote that the company is not certified. Procore interprets a blank value as a 'No' entry.
     - **8a Business Enterprise:** Select 'Yes' to denote that the company is certified by the U.S. Small Business Administration as a Minority Owned Business (e.g., Socially- or Economically- Disadvantaged Business under the 8(a) program). Select 'No' to denote that the company is not certified. Procore interprets a blank value as a 'No' entry.
     - **Affirmative Action**.: Select 'Yes' to denote that the company is subject to affirmative action when bidding. Select 'No' to indicate the vendor is not subject to affirmative action. Procore interprets a blank value as a 'No' entry.
     - **Certified Business Enterprise:** Select 'Yes' to denote that the company registered with the Department of Small and Local Business Developmentâs (DSLBDâs) Certified Business Enterprise ([CBE](/glossary-of-terms)) Program. Select 'No' to indicate the company is not a district-based (i.e., Washington D.C.) business.
     - **Prequalified:** Select 'Yes' if the contractor is on the relevant Prequalified Contractors Listing for the state in which it will be doing business. Select 'No' if the contractor is not on the listing. Procore interprets a blank value as a 'No' entry.
     - **License Number:** Enter the company's state contractors license.\* **Tags Keywords:** Enter any keyword tags for the vendor here. Separate entries with a comma (,). You can enter up to 255 characters in this field.
   - **Cost Codes:** 

     Enter one or more cost codes. Use a dash (-) to separate each tiered segment item on the 'Cost Code' segment and a pipe (|) symbol to separate each individual cost code entry. Always include a SPACE on either side of the pipe (|) symbol.

     *Notes:*In Procore's [WBS](https://support.procore.com/products/online/work-breakdown-structure), the 'Cost Code' segment is a [tiered segment](/faq-what-is-the-difference-between-a-flat-and-tiered-segment-in-procores-wbs) in your [budget code structure](/faq-what-is-a-budget-code-structure-in-procores-wbs). In the import template, tiers within a segment must be delimited by a dash (-). Depending on your company's specific budget code structure, your cost code entries may be different than these examples:

     - If your company or project level 'Cost Code' segment has two (2) tiers, the first tier might represent a Division number (01) in the CSI MasterFormat. The second tier includes nested segment items with the 'Division', which are considered cost codes in the MasterFormat (000, 002, 010, and so on). Using this example, your cost code entry in the import template would look like: 01-000
     - If your 'Cost Code' segment has three (3) tiers, the first tier might represent the Division number (01) in the CSI MasterFormat, the second tier is a sub division (10), and the third tier is the cost code (010), so your cost code entry would look like: 01-10-010
     - If you want to enter multiple cost codes to associate with the company, separate each code with the pipe (|) symbol and be sure to include a single SPACE on either side of the pipe (|) symbol. For example: 01-000| 01-002| 01-010 **or** 01-10-000 | 01-10-002 | 01-10-010

     To learn more about Procore's default 'Cost Code' segment, see [What are Procore's default cost codes?](/faq-what-are-procores-default-cost-codes) and [Work Breakdown Structure](https://support.procore.com/products/online/work-breakdown-structure).

     Cost Codes: Import Template Entry
   - **Id:** This field is for a vendor's pre-designated Procore unique ID that will only populate when you export the vendors list from your Directory.

## Next Steps

- [Import Users & Vendors into your Project Level Directory Tool (Procore Imports)](/product-manuals/procore-imports/tutorials/import-users-vendors-into-your-project-level-directory-tool-procore-imports)  
   OR
- [Update Users & Vendors in your Project Level Directory Tool (Procore Imports)](/product-manuals/procore-imports/tutorials/update-users-vendors-in-your-project-level-directory-tool-procore-imports)
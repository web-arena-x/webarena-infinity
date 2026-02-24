# Prepare Contacts for Import to the Procore Imports App

Source: https://v2.support.procore.com/product-manuals/procore-imports/tutorials/prepare-contacts-for-import-to-the-procore-imports-app

---

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the Project level Directory tool.  
    *Note:* Granular permissions are not supported in the Procore Imports application.

## Steps

- Download the Contacts Import Template
- Format the Contacts Import Template

### Download the Contacts Import Template

1. **Download the Contacts Import Template:** [import-contacts.xlsx](https://procore-imports-templates.s3.us-east-1.amazonaws.com/import%5Ftemplate%5Fcontacts.xlsx)  
   *Note:* In Procore, a contact is a person whose name may be required as part of a data entry value, but does not have a user account to log in to Procore. See [What is a 'contact' in Procore and which project tools support the concept?](/faq-what-is-a-contact-in-procore-and-which-project-tools-support-the-concept)

### Format the Contacts Import Template

1. Review the following considerations:

   - **Required Row Data:**

     - Each row in the spreadsheet corresponds to an individual contact.
     - At minimum, each record requires a value for the contact's **First Name** and **Last Name**. The column headings for required fields have a RED background. All other columns and cells in a single row may be left blank.
     - ***Important!*** There is no limit to the number of contacts you can import. However, rows cannot be blank.
   - **Required Column Data:**  
      The first row of the table must include the Procore default headers.

     - The import process will fail if you modify the text or the order of the table column headers.\* The import process will fail if you add, move, or remove any columns in the table.
2. Complete the import template.

   ##### Â Note

   - An asterisk (\*) below denotes a required field.
   - The contact's first and last names must be entered in their own separate cells.

- **\*First Name:** Enter the contact's first name exactly as you want it to appear in Procore.  
  ***Important!*** First names are case- and punctuation-sensitive.
- **\*Last Name:** Enter the contact's last name exactly as you want it to appear in Procore.  
  ***Important!*** Last names are case- and punctuation-sensitive.
- **Is Employee:**\* If the contact is an employee of your company, select **Yes**.  
   OR\* If the contact is not an employee of your company, select **No**.
- **Employee Id:** If you selected **Yes** for the **Is Employee** column, you can enter an employee ID for the contact under this column. Enter the employee ID exactly as you want it to appear in Procore.
- **Work Classification:** Enter the contact's work classification.

  ##### Â Notes

  - Classification entries must exactly match a classification in the Company Admin tool. See [Add a Classification](/product-manuals/admin-company/tutorials/add-a-classification).
  - To view a contact's work classification in the Timesheets or T&M Tickets tool after the import, the imported classification must be enabled on the project. See [Enable Classifications on a Project](/product-manuals/admin-project/tutorials/enable-classifications-on-a-project).
  - To learn more about classifications, see [Which Procore tools support 'Classifications'](/faq-which-procore-tools-support-classifications)
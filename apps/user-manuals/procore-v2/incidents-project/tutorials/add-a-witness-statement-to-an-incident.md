# Add a Witness Statement to an Incident

Source: https://v2.support.procore.com/product-manuals/incidents-project/tutorials/add-a-witness-statement-to-an-incident

---

## Background

When incidents occur, collecting statements from witnesses is common practice. A *witness statement* is taken as part of the incident investigation process and is used to better understand what happened, why it happened, and how similar incidents can be prevented in the future.

## Things to Consider

- **Required User Permissions:**

 - *To add a witness statement:* 'Standard' level permissions or higher on the projectâs Incidents tool.
 - *To add a contact in the 'Witness Name' field* (see [What is a 'contact' in Procore and which project tools support the concept?](/faq-what-is-a-contact-in-procore-and-which-project-tools-support-the-concept)):

    - 'Standard' level permissions or higher on the project's Incidents tool.
    - 'Read Only' or 'Standard' level permissions on the project's Directory tool with the ['Create Contacts' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permission template. Consider the following:

      - Users who have been granted the 'Create Contacts' granular permission can:

        - Add a new contact when the person does NOT already exist in the Company or Project Directory.
        - View existing contacts as a drop-down selection for all projects in the company's Procore account.
      - Users who have NOT been granted the 'Create Contacts' granular permission do NOT have sufficient permission to add contacts. However, they do have sufficient permission to view contacts added by others on the project and to select an existing contact when adding a record.

## Prerequisites

- [Create an Incident](/product-manuals/incidents-project/tutorials/create-an-incident)

## Steps

1. Navigate to the project's **Incidents** tool.
2. Click the **Incidents** tab.
3. Click **View** next to the incident you want to add a witness statement to.
4. Scroll to 'Witness Statements'.
5. Click **Add Witness Statement**.
6. Add the following information in the 'New Witness Statement' side panel.

   - **Name**. Select the witness's name from the list. Consider the following:

     - If the person's name exists in the Project Directory, a match will appear as you type. See [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory). 
       OR
     - If the person's name does NOT exist in the Project Directory, type the person's name and click **Create Person**. In the window that appears, enter this information:

       - **First Name**. Enter the person's first name.
       - **Last Name**. Enter the person's last name. This is a required field.
       - **Employee ID**. Enter the person's Employee ID if available.
       - **Is Employee of [Company Name]**. Mark this checkbox if the person is an employee of the company noted.
       - Click **Create**. 
         This action creates a contact. To learn more, see [What is a 'contact' in Procore and which project tools support the concept?](/faq-what-is-a-contact-in-procore-and-which-project-tools-support-the-concept)
   - **Date Received**. Select the date of the witness statement from the drop-down calendar.
   - **Statement**. Type the witness statement in this box.
   - **Attachments**. Click **Attach Files** or use a drag-and-drop-operation to upload a file with the statement or any supplemental information related to the statement.

     ##### Â Tip

     Users can add audio recordings of the witness stating their account of the incident using one of the Procore mobile applications. See [Add a Witness Statement to an Incident (iOS)](/product-manuals/incidents-ios/tutorials/add-a-witness-statement-to-an-incident-ios) and [Add a Witness Statement to an Incident (Android)](/product-manuals/incidents-android/tutorials/add-a-witness-statement-to-an-incident-android).

- Click **Create**.
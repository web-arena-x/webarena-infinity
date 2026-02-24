# Add a Witness Statement to an Incident (iOS)

Source: https://v2.support.procore.com/product-manuals/incidents-ios/tutorials/add-a-witness-statement-to-an-incident-ios

---

## Background

When incidents occur, collecting statements from witnesses is common practice. A *witness statement* is taken as part of the incident investigation process and is used to better understand what happened, why it happened, and how similar incidents can be prevented in the future.

## Things to Consider

- **Required User Permissions:**

 - *To add a witness statement:* 'Standard' level permissions or higher on the projectâs Incidents tool.
 - *To add a contact in the 'Witness Name' field* (see [What is a 'contact' in Procore and which project tools support the concept?](/faq-what-is-a-contact-in-procore-and-which-project-tools-support-the-concept)):

    - 'Standard' level permissions or higher on the project's Incidents tool.
    - 'Read Only' or 'Standard' level permissions on the project's Directory tool with the ['Create Contacts' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permission template. *Notes:*

      - Users who have been granted the 'Create Contacts' granular permission can:

        - Add a new contact when the person does NOT already exist in the Company or Project Directory.
        - View existing contacts as a drop-down selection for all projects in the company's Procore account.
      - Users who have NOT been granted the 'Create Contacts' granular permission do NOT have sufficient permission to add contacts. However, they do have sufficient permission to view contacts added by others on the project and to select an existing contact when adding a record.

## Prerequisites

- [Create an Incident (iOS)](/product-manuals/incidents-ios/tutorials/create-incidents-ios)

## Steps

1. Navigate to the **Incidents** tool using the Procore app on an iOS mobile device.
2. Tap the incident you want to add a witness statement to.
3. Under Witness Statements, tap **Add**.
4. Fill out the following fields as appropriate: 
   *Note:* An asterisk (\*) denotes a required field.

   - **Witness\*:**

     - Select a witness name from the list.   
       OR
     - To add a witness who does not already exist in the project's Directory:

       - Tap **Add New Item**.
       - Fill out the following:

         - **First Name\*:** Enter the witness's first name.
         - **Last Name\*:** Enter the witness's last name.
         - **Employee ID:** If the witness is an employee, enter the employee ID.
         - **Employee of [Company Name]:** Tap the toggle to the ON position if the witness is an employee of your company.
       - Tap **Add**.
     - **Date Received:** Select the date of the witness statement.
     - **Statement:** Enter the witness statement or comment in this box.
5. *Optional:* To add relevant files, photos, or an audio recording of the witness statement, tap one of the following options:

   1. **Camera:** Take a photo with your mobile device's camera and add it to the incident.
   2. **Attachments:** Choose a photo or file from your mobile device and add it to the incident.
   3. **Add a Recording:** Take an audio recording of the witness stating their account of the incident. 
      *Note:* The maximum recording time is 10 minutes.
6. Tap **Save**.
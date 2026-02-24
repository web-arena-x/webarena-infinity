# Add a Near Miss Record to an Incident

Source: https://v2.support.procore.com/product-manuals/incidents-project/tutorials/add-a-near-miss-record-to-an-incident

---

## Background

When you create an incident in Procore, you can add one or more near miss records to capture important safety details. In the construction industry, properly documenting near misses helps to correct potential problems and can help to reduce injury accidents in the future. Examples of a *Near Miss* include tripping over extension cords, minor falls that do not result in injury, and more.

## Things to Consider

- **Required User Permissions:**

 - *To add a record:*

    - 'Standard' level permissions or higher on the projectâs Incidents tool.
 - *To add a contact in the 'Person Affected' field. S*ee [What is a 'contact' in Procore and which project tools support the concept?](/faq-what-is-a-contact-in-procore-and-which-project-tools-support-the-concept) and consider these permissions:

    - 'Standard' level permissions or higher on the project's Incidents tool.
    - 'Read Only' or 'Standard' level permissions on the project's Directory tool with the ['Create Contacts' granular permission](/product-manuals/permissions-company/tutorials/edit-a-project-permissions-template) enabled on your permission template.

      - Users who have been granted the 'Create Contacts' granular permission can:

        - Add a new contact when the person does NOT already exist in the Company or Project Directory.
        - View existing contacts as a drop-down selection for all projects in the company's Procore account.
      - Users who have NOT been granted the 'Create Contacts' granular permission do NOT have sufficient permission to add contacts. However, they do have sufficient permission to view contacts added by others on the project and to select an existing contact when adding a record.
- **Additional Information:**

 - Custom options can be created for certain fields in a record. See [Add Custom Options for Incident Fields](/product-manuals/admin-company/tutorials/add-custom-options-for-incident-fields). 
    *Note:* These field options for incidents are managed in the Company level Admin tool and can only be created by users with 'Admin' permissions on the Company Admin tool.

## Prerequisites

- [Create an Incident](/product-manuals/incidents-project/tutorials/create-an-incident)

## Steps

1. Navigate to the project's **Incidents** tool.
2. Click the **Incidents** tab.
3. Click **View** next to the incident you want to add a near miss record to.
4. Scroll to 'Incident Records'.
5. Click **Add Record** and select **Near Miss** in the drop-down menu.
6. Add the following information, as applicable, in the 'New Near Miss Record' side panel:

   - **Company Affected**. Select the company of the person that was involved from the near miss. See [Add a Company to the Project Directory](/process-guides/set-up-a-project-directory/create-companies).
   - **Person Affected**. Enter the name of the person involved in the near miss. *Notes:*

     - If the person's name exists in the Project Directory, a match will appear as you type. See [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory).
     - If the person's name does NOT exist in the Project Directory, add them:

       1. Type the person's name and click **Create Person**.
       2. Enter their information.
       3. Click **Create** to create a contact. See [What is a 'contact' in Procore and which project tools support the concept?](/faq-what-is-a-contact-in-procore-and-which-project-tools-support-the-concept)
   - **Work Activity**. Select the activity the person was doing when the near miss occurred.
   - **Equipment**. Select the equipment involved in the near miss. 
     *Note:* This list is pulled from the Project level equipment tool. See [Add Equipment](/product-manuals/equipment-project/tutorials/add-equipment-to-projects-in-the-project-equipment-tool).
   - **Source of Harm**. Select the source of harm that affected the person (e.g., Chemical, Explosion, Vehicle, and so on).
   - **Description**. Enter any additional information relevant to the near miss record.
7. Click **Create**.
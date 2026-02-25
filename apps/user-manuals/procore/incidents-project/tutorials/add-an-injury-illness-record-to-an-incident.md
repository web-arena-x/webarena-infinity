# Add an Injury/Illness Record to an Incident

Source: https://v2.support.procore.com/product-manuals/incidents-project/tutorials/add-an-injury-illness-record-to-an-incident

---

## Background

When you create an incident in Procore, you can add one or more incident records to capture details. When an injury or illness occurs on a project, use the steps below to capture important information about the incident.

## Things to Consider

- **Required User Permissions:**

 - *To add a record:*

    - Standard' level permissions or higher on the project's Incidents tool.
 - *To add a contact in the 'Person Affected' field* (see [What is a 'contact' in Procore and which project tools support the concept?](/faq-what-is-a-contact-in-procore-and-which-project-tools-support-the-concept)):

    - 'Standard' level permissions or higher on the project's Incidents tool.
    - Read Only' or 'Standard' level permissions on the Project level Directory tool with the ['Create Contacts' granular permission](/product-manuals/permissions-company/tutorials/edit-a-project-permissions-template) enabled on your permission template. 
      *Notes:*

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
3. Click **View** next to the incident you want to add an injury/illness record to.
4. Scroll to 'Incident Records'.
5. Click **Add Record** and select **Injury/Illness** in the drop-down menu.
6. Add the following information, as applicable, in the 'New Injury/Illness Record' side panel:

   - In the 'General Information' section:

     - **Filing Type**. Select the filing type the person chose to use (e.g., Record Only, Refused Care, First Aid, Medically Treated, Restricted Work, Lost Time, and Fatality).
     - **Recordable**. Click the toggle to the ON position if this injury or illness is legally classified as a recordable incident by a regulatory agency or governing body.
     - **Company Affected**. Select the company of the person who was involved in the injury or illness. See [Add a Company to the Project Directory](/process-guides/set-up-a-project-directory/create-companies).
     - **Description**. Enter any additional information relevant to the injury/illness record.
     - **Person Affected**. Select the name of the person involved in the injury or illness.   
       *Notes*:

       - If the person's name exists in the Project Directory, a match will appear as you type. See [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory).
       - If the person's name does NOT exist in the Project Directory, add them.

         1. Enter the person's name and click **Create Person**.
         2. Enter their information
         3. Click **Create** to add the contact. To learn more, see [What is a 'contact' in Procore and which project tools support the concept?](/faq-what-is-a-contact-in-procore-and-which-project-tools-support-the-concept)
   - In the 'Source of Harm' section:

     - **Work Activity**. Select the activity the person was doing when the incident occurred.
     - **Equipment**. Select the equipment involved in the incident. 
       *Note:* This list is pulled from the Project level equipment tool. See [Add Equipment](/product-manuals/equipment-project/tutorials/add-equipment-to-projects-in-the-project-equipment-tool).
     - **Source of Harm**. Select the source of harm to the person (e.g., material, electrical, chemical).
   - In the 'Injury/Illness Details' section:

     - **Injury/Illness**. Select the injury or illness that the person sustained from the incident.
     - **Body Parts Affected.** Use the body diagram or dropdown menu to select one or more body parts affected by the injury or illness sustained in the incident.
     - **Work Days Absent**. Enter the number of workdays the person was absent from work because of injuries or illnesses sustained in the incident.
     - **Work Days Restricted**. Enter the number of workdays the person was restricted from work because of injuries or illnesses sustained in the incident.
     - **Work Days Transferred**. Enter the number of workdays the person was transferred to another role on the job site because of injuries or illnesses sustained in the incident.
     - **Date Returned to Work**. Enter the date the person returned to work.
     - **Date of Death**. Enter the date that the person died because of the incident.
   - In the 'Treatment Details' section:

     - **Treatment Provider**. Enter the name of the treatment provider who treated the person's injuries or illnesses.
     - **Treatment Facility**. Enter the name of the facility that the person was sent to for treatment.
     - **Treatment Facility Address**. Enter the address of the facility that the person who was sent to for treatment.
     - **Treated in ER**. Click the toggle to the ON position if the person affected was treated in the Emergency Room.
     - **Hospitalized Overnight**. Click the toggle to the ON position if the person affected stayed in the hospital overnight.
7. Click **Create**.
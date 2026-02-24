# Add a Record to an Incident (Android)

Source: https://v2.support.procore.com/product-manuals/incidents-android/tutorials/add-a-record-to-an-incident-android

---

## Things to Consider

- **Required User Permissions:**

 - *To add a record:* 'Standard' level permissions or higher on the project's Incidents tool.
 - *To add a contact in the 'Person Affected' field* (see [What is a 'contact' in Procore and which project tools support the concept?](/faq-what-is-a-contact-in-procore-and-which-project-tools-support-the-concept)):

    - 'Standard' level permissions or higher on the project's Incidents tool.
    - 'Read Only' or 'Standard' level permissions on the Project level Directory tool with the ['Create Contacts' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permission template. *Notes:*

      - Users who have been granted the 'Create Contacts' granular permission can:

        - Add a new contact when the person does NOT already exist in the Company or Project Directory.
        - View existing contacts as a drop-down selection for all projects in the company's Procore account.
      - Users who have NOT been granted the 'Create Contacts' granular permission do NOT have sufficient permission to add contacts. However, they do have sufficient permission to view contacts added by others on the project and to select an existing contact when adding a record.
- **Additional Information:**

 - Custom options can be created for certain fields in a record. See [Add Custom Options for Incident Fields](/product-manuals/admin-company/tutorials/add-custom-options-for-incident-fields). 
    *Note:* These field options for incidents are managed in the Company level Admin tool and can only be created by users with 'Admin' permissions on the Company Admin tool.

## Prerequisites

- A record can only be added to an incident after the incident has been created in Procore. See [Create an Incident (Android)](/product-manuals/incidents-android/tutorials/create-incidents-android).

## Steps

1. Navigate to the **Incidents** tool on an Android mobile device.
2. Tap the incident you want to add a record to.
3. Across from 'Records', tap **Add**.
4. Select the type of record you want to add to the incident.

   - Environmental
   - Injury/Illness
   - Near Miss
   - Property Damage

### Environmental

1. Fill out the following fields as appropriate:

   - **Company Affected:** Select the company that was involved in the incident.
   - **Work Activity:** Select the activity that the company was involved in when the incident occurred.
   - **Equipment:** Select the equipment involved in the incident. 
     *Note:* This list is pulled from the Project level equipment tool. See [Add Equipment to a Project (Android)](/product-manuals/equipment-android/tutorials/add-equipment-to-a-project-android).
   - **Type:** Select the type of environmental incident that occurred.
   - **Quantity:**

     1. If relevant, enter a quantity incident in the Quantity field.
     2. Select the type of units for the quantity in the Units field.
   - **Estimated Cost Impact:** Enter the estimated cost impact of the incident.
2. Tap **Save**.

### Injury/Illness

1. Fill out the following fields as appropriate:

   - **Company Affected:** Select the company of the person who was involved in the injury or illness.
   - **Person Affected:**

     - Select from the list the name of the person involved in the injury or illness.
     - Add a person who does not already exist in the project's Directory:

       1. Tap the **add** icon.
       2. Fill out the information.
       3. Tap **Add**.
   - **Work Activity:** Select the activity the person was doing when the incident occurred.
   - **Equipment:** Select the equipment involved in the incident. 
     *Note:* This list is pulled from the Project level equipment tool. See [Add Equipment to a Project (Android)](/product-manuals/equipment-android/tutorials/add-equipment-to-a-project-android).
   - **Source of Harm:** Select the source of harm to the person (e.g., material, electrical, chemical).
   - **Injury/Illness:** Select the injury or illness that the person sustained from the incident.
   - **Body Parts Affected:** Use the body diagram or dropdown menu to select one or more body parts affected by the injury or illness sustained in the incident.
   - **Filing Type:** Select the filing type the person chose to use (e.g., Record Only, Refused Care, First Aid, Medically Treated, Restricted Work, Lost Time, and Fatality).
   - **Recordable:** If this injury or illness is legally classified as a recordable incident by a regulatory agency or governing body, tap the toggle to the ON position.
2. Tap **Save**.

### Near Miss

1. Fill out the following fields as appropriate:

   - **Company Affected:** Select the company of the person who was involved in the near miss.
   - **Person Affected:**

     - Select from the list the name of the person involved in the injury or illness.
     - Add a person who does not already exist in the project's Directory:

       1. Tap the **add** icon.
       2. Fill out the information.
       3. Tap **Add**.
   - **Work Activity:** Select the activity the person was doing when the incident occurred.
   - **Equipment:** Select the equipment involved in the incident. 
     *Note:* This list is pulled from the Project level equipment tool. See [Add Equipment to a Project (Android)](/product-manuals/equipment-android/tutorials/add-equipment-to-a-project-android).
   - **Source of Harm:** Select the source of harm to the person.
2. Tap **Save**.

### Property Damage

1. Fill out the following fields as appropriate:

   - **Company Affected:** Select the company of the person who was involved in the property damage.
   - **Work Activity:** Select the activity the person was doing when the property damage occurred.
   - **Equipment:** Select the equipment involved in property damage. 
     *Note:* This list is pulled from the Project level equipment tool. See [Add Equipment to a Project (Android)](/product-manuals/equipment-android/tutorials/add-equipment-to-a-project-android).
   - **Responsible Company:** Select a responsible company.
   - **Estimated Cost Impact:** Enter the estimated cost impact of the property damage.
2. Tap **Save**.
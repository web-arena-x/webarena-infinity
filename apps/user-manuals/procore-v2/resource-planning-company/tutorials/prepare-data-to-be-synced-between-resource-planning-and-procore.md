# Prepare Data to be Synced Between Resource Planning and Procore

Source: https://v2.support.procore.com/product-manuals/resource-planning-company/tutorials/prepare-data-to-be-synced-between-resource-planning-and-procore

---

## Background

When setting up Resource Planning, customers first need to choose how you want to add information to Resource Planning. See [What Integrations are available for Resource Planning](/faq-what-integrations-are-available-for-resource-planning). After you select how to get information into Resource Planning, you can choose to sync people and project data so that information is kept in sync in Resource Planning and other Procore tools:

- People listed in the **People Lis**t sync one-way from Resource Planning to the **Company Directory** in Procore.
- Projects sync one-way between the **Project List** in Resource Planning and the **Portfolio** tool in Procore.

People data updated in Resource Planning is synced at the time of a change, and typically updated in the Company Directory tool in less than one minute. For project data, if Resource Planning is your system of record, information updated in the Project List syncs immediately to the Portfolio tool. If the Portfolio tool is your system of record, data updated in the Portfolio tool currently syncs once every hour to the Project List in Resource Planning.

## Things to Consider

- [What people information is synced between Resource Planning and the Procore Company Directory?](/faq-what-people-information-is-synced-between-resource-planning-and-the-procore-company-directory)
- [What project information is synced between Resource Planning and Procore Projects?](/faq-what-project-information-is-synced-between-resource-planning-and-procore-projects)

## Steps

1. Work with your Procore account team to identify your system(s) of record where you will add and manage people and projects. See [What Integrations are available for Resource Planning?](/faq-resource-planning-and-procore-detailed-data-mapping)
2. Work with your Procore account team to identify if you want all people synced or if you only want users (people marked as 'Users' or 'Assignable Users' in Resource Planning) to be synced.
3. Identify if you have any people that currently exist in both Resource Planning and Procore's Directory and update their information so that their user records can be linked. âââââIf people exist in both systems, follow these steps so that the data can be linked between Resource Planning and Procore:

   ##### Â Note

   It is important that data is cleaned up beforehand, otherwise duplicate records may be created.

   If the below fields are not matching there is a high possibility that the sync will sever and will not be able to relink thus creating duplicate records.

   Inactive People are not synced in this initial set up. However, after this initial setup process is complete, records of inactivated people will sync between Resource Planning and Procore.

1. Review your people data fields between People List in Resource Planning and your Company Directory in Procore (Users and Contacts). The following fields must match between the People List and your Procore Company Directory prior to turning on the people sync:

   - First name
   - Last name
   - Email address
   - Employee ID
   - Mark the 'Is Employee' checkbox for users in the Procore Directory.
2. Ensure **users** in your Procore Company Directory that you want to mange in Resource Planning are 'Users' or 'Assignable Users' in your Resource Planning People List. If users are in the Company Directory, but not yet in the People List, follow these steps:

   1. Navigate to the **Company Directory.**
   2. Locate the user that needs to be added in Resource Planning and click **Edit**.
   3. Ensure the **Is Employee** checkbox is marked.
   4. Update the user's permission to have '**Read Only'** access or higher to the Resource Planning tool.
   5. Navigate to the Company level **Resource Planning** tool.
   6. Click **People** and select **People List**.
   7. Click **New**.
   8. Complete the form with the following information:

      - **First Name**. The person's first name.
      - **Last Name**. The person's last name.
      - **Email**. The person's email address.  
        *Note:* This must match the email address in the Company Directory.
      - **Type**. Select **User** or **Assignable User**.
      - **Permission.** Select the user's permission level.
      - **Group**. The person's group. See [Configure Groups for Resource Planning](/product-manuals/resource-planning-company/tutorials/configure-groups-for-resource-planning).
   9. Click **Save**.
3. Ensure **contacts** in your Procore Company Directory that you want to manage in Resource Planning are 'Assignable' people in your Resource Planning People List.  
   *Note:* Skip this step if you chose to only sync users.

   1. Navigate to the Company level **Resource Planning** tool.
   2. Click **People** and select **People List**.
   3. Click **New**.
   4. Complete the form with the following information:

      1. **First Name**. The person's first name.
      2. **Last Name**. The person's last name.
      3. **Employee ID**. The person's employee ID.  
         *Note:* This must match the employee ID in the Company Directory.
      4. **Type**. Select **Assignable**.
      5. **Group**. The person's group. See [Configure Groups for Resource Planning](/product-manuals/resource-planning-company/tutorials/configure-groups-for-resource-planning).
   5. Click **Save**.

- By default, projects are synced from Procore's Portfolio tool to Resource Planning. If you prefer project data to originate in Resource Planning, please discuss with your Procore point of contact.
- Follow steps to [Prepare Data for Import to the Resource Planning Tool](/product-manuals/resource-planning-company/tutorials/prepare-data-for-import-to-the-resource-planning-tool).
- Follow steps to [Import Resource Planning Data](/product-manuals/resource-planning-company/tutorials/import-resource-planning-data).
- Reach out to your Procore point of contact to initiate the data sync. This can be done via email or by emailing [support@procore.com](mailto:support@procore.com).
- Going forward, all new **projects** in your system of record will be kept in sync between Resource Planning and the Portfolio tool.
- Going forward, all **people** are kept in sync between Resource Planning and the Company Directory. See [Add People to Resource Planning](/product-manuals/resource-planning-company/tutorials/add-people-to-resource-planning).   
  *Note:* It is recommended to create new users in the Resource Planning tool for a more streamlined workflow.
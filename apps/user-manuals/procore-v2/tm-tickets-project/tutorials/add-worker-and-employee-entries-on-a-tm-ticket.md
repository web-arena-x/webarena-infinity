# Add Worker and Employee Entries on a T&M Ticket

Source: https://v2.support.procore.com/product-manuals/tm-tickets-project/tutorials/add-worker-and-employee-entries-on-a-tm-ticket

---

## Background

When creating or editing a T&M ticket, you can record the name of the worker, their classification, the time type, and the number of hours to complete the task as a line item in the 'Labor' section. If the worker you are looking for has not been added to the project as an available employee in the 'Employee' drop-down list, you can use the **+Add Worker** button to create a new worker or search to add an existing worker from a previous project.

*Note:* When a worker is added in Procrore, they will also be accessible in the both the [Crews](/product-manuals/crews-project/) and [Timesheets](/product-manuals/timesheets-company/) tools, and added as a contact in both the Project Directory and Company Directory.

## Things to Consider

- **Required User Permissions:**

  - 'Standard' level permissions or higher on the T&M Tickets tool.  
     AND
  - 'Read Only' or 'Standard' level permissions on the project's Directory tool with the ['Create Contacts' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled.  
     OR  
     'Admin' level permissions on the project's Directory tool.
- **Additional Information:**

  - The T&M Tickets tool does NOT allow you to create duplicate workers.
  - The workers added will be displayed in the Employee List on the Crews, Timesheets, and T&M Tickets tools.
  - Once a worker (contact) has been added to the Crews tool in one project, that person's First Name, Last Name, Employee ID, and Classification will auto-complete when a user begins to enter that name in crews or inside a T&M Tickets.
  - Contact records are added to the Project and Company level Directory tools in the 'Contacts' tab.
  - Contact records can be edited in the Project level Crews tool and in the Project and Company level Directory tools. See [Edit a Worker](/product-manuals/crews-project/tutorials/edit-a-worker), [Edit a Contact in the Project Directory](/product-manuals/directory-project/tutorials/edit-a-contact-in-the-project-directory), and [Edit a Contact in the Company Directory](/product-manuals/directory-company/tutorials/edit-a-contact-in-the-company-directory).

## Prerequisites

- ['Create Contacts' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template)

## Steps

1. Navigate to the project's **T&M Tickets** tool.
2. Locate the ticket that you want to work with.
3. Click the **+Create** button to create a new ticket or the Edit button to edit an existing ticket.
4. In the 'Labor' section, click the **Employee** drop-down list.
5. Scroll to the bottom of the drop-down list and click **Add Worker**.
6. Enter the following information:

   - Add a unique Employee ID for each worker (Recommended)
   - Enter a middle initial or name after the first name.
   - Enter the worker's full name.
   - **\*First Name:** Enter or Edit the worker's first name. If you have previously added workers, a list of potentially matching names will appear. You can select the correct match or type a full name.
   - **\*Last Name:** Enter or Edit the worker's last name. If you have previously added workers, a list of potentially matching names will appear. You can select the correct match or type a full name.
   - *Optional:* **Employee ID**. Edit the Employee ID for the worker in this list.
   - *Optional:* **Classification:** Edit the classification by selecting an option from the drop-down list. To learn which Procore tools interact with classifications, see [Which Procore tools support 'Classifications'?](/faq-which-procore-tools-support-classifications)

     ##### Â Note

     If you have two (2) or more workers with identical names, the Crews tool will NOT allow you to create duplicate worker entries. Filling out Employee ID or Classifications fields helps to identify the individual workers.

- Click **Add**. This adds a new worker to the project's Crews tool and also creates a contact record in the Project Directory tool.

## Next Step

- [Edit a Contact in the Company Directory](/product-manuals/directory-company/tutorials/edit-a-contact-in-the-company-directory).
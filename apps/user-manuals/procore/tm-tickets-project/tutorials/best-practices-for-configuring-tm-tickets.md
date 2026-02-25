# Best Practices for Configuring T&M Tickets

Source: https://v2.support.procore.com/product-manuals/tm-tickets-project/tutorials/best-practices-for-configuring-tm-tickets

---

With the T&M Tickets tool, you can ensure that everyone on your team is informed of the status of extra work without filling out paper tickets or tags.For instructions on how to add the T&M Tickets tool to your projects, see [Add and Remove Project Tools](/product-manuals/admin-project/tutorials/add-and-remove-project-tools).

###### 1. Start by configuring your Company level information so you can enable your users and ensure information is consistent across your projects.

|  |  |  |
| --- | --- | --- |
| Do you want to create a new [configurable fieldset](/faq-what-fieldset-configurations-are-recommended-for-configurable-fieldsets) and/or new [custom fields](/faq-what-are-custom-fields-and-which-procore-tools-support-them) to use with the T&M Tickets tool? | Have you set up Company Classifications and assigned them to your team so that they will automatically be assigned on Timesheets or a T&M ticket? | Have you decided which users should be able to create and manage T&M Tickets? |
| [Create New Configurable Fieldsets](/product-manuals/admin-company/tutorials/create-new-configurable-fieldsets) and [Create New Custom Fields](/product-manuals/admin-company/tutorials/create-new-custom-fields). | [Add a Classification](/product-manuals/admin-company/tutorials/add-a-classification), [Enable Classifications on a Project](/product-manuals/admin-project/tutorials/enable-classifications-on-a-project), and assign classifications to users or contacts when you [Edit a User Account in the Project Directory](/product-manuals/directory-project/tutorials/edit-a-user-account-in-the-project-directory) or [Edit a Worker](/product-manuals/crews-project/tutorials/edit-a-worker). | Follow the [Manage Users](/product-manuals/permissions-company/tutorials/edit-a-project-permissions-template) steps in [Edit a Project Permissions Template](/product-manuals/permissions-company/tutorials/edit-a-project-permissions-template). |
|  |  |  |

###### 2. Configure your project to make it easier for the team on-site to select Employees, Equipment, and Signees.

|  |  |  |
| --- | --- | --- |
| Have all employees and workers been added to the project? | Has all the equipment on the project that is currently on-site been set up? | Have you added who will verify tickets or who can authorize extra work? |
| [Add Workers to Crews](/product-manuals/crews-project/tutorials/add-a-worker) or [Add Employees to the Directory](/product-manuals/directory-project/tutorials/edit-a-user-account-in-the-project-directory). | [Add Equipment to Your Project](/process-guides/project-equipment-user-guide/add-from-company-web) using the Equipment tool. | [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory) with 'Read Only' level permissions or higher on the T&M Tickets tool. |
|  |  |  |
| 3. Streamline communication between your office, the field teams, and your customer. |  |  |
| Do you want notifications for when a T&M ticket is created or verified on-site by your customer so you can take action? |  |  |
| Select who should receive email notifications when T&M tickets are created or verified on-site by following the steps in [Configure Advanced Settings: T&M Tickets](/product-manuals/tm-tickets-project/tutorials/configure-advanced-settings-tm-tickets). |  |  |
|  |  |  |
| Need to get a better understanding of the status of T&M work across your projects? | Need to export Labor, Material, or Equipment information into a spreadsheet? | Need to download your T&M ticket for backup documentation? |
| [Create a 'T&M Ticket' Report](/product-manuals/reports-project/tutorials/create-a-project-single-tool-report) in the project's Reports tool and [Distribute a Snapshot of a Custom Project Report](/product-manuals/reports-project/tutorials/distribute-a-snapshot-of-a-custom-project-report). | Follow the steps in [Edit a Custom Company Report](/product-manuals/reports-company/tutorials/edit-a-company-single-tool-report) and [Export a Custom Company](/product-manuals/reports-company/tutorials/export-a-company-single-tool-report) [Report](/product-manuals/reports-company/tutorials/export-a-company-single-tool-report). | See [Export a T&M Ticket as a PDF](/product-manuals/tm-tickets-project/tutorials/export-a-tm-ticket-as-a-pdf) from the Procore web application or from your email. |

## SetÂ Up T&M Tickets

- Configure Permissions
- Set up a Labor Force
- Set up Equipment
- Configure Notifications
- Set up Reports

#### Configure Permissions

- To assign permissions to users for the T&M Tickets tool:

  - [Assign appropriate permissions to the user](/product-manuals/permissions-company/tutorials/edit-a-project-permissions-template) in the company's Permissions tool.

#### Set Up a Labor Force

- For users to appear in the T&M Tickets tool:

  - Add Employees on an individual project basis.

    - Go to the Directory, add or edit each employee's user profile and under 'Personal Information', scroll down to mark the checkbox that says 'Is Employee of [Company Name]?â. The employee will need to be added to each Project Directory that you want to track their time for. See [Edit a User Account in the Project Directory](/product-manuals/directory-project/tutorials/edit-a-user-account-in-the-project-directory) for more information.
    - Add a "worker" to the Crews tool. An email address is NOT required to create a "worker" nor do they need to be added to the Directory. See [Add a Worker](/product-manuals/crews-project/tutorials/add-a-worker) to learn more.
  - Select Employees from the Company Directory (only if the configuration "can be tracked on all projects" is marked).

    - Employees will be listed in the Timesheets tool for all projects if the 'Can Company Employees be Tracked on all Projects?' setting is enabled and they are an "Employee of the Company". See [Configure Advanced Settings: Company Level Timesheets](/product-manuals/timesheets-company/tutorials/configure-advanced-settings-company-level-timesheets).
  - Select a crew (a group of employees).

    - A crew must first be created in the Crews tool. For more information, see [Create a Crew](/product-manuals/crews-project/tutorials/create-a-crew).

#### Set Up Equipment

- To add equipment for use in the T&M Tickets tool:

  - [Add Equipment](/product-manuals/admin-project/tutorials/add-equipment) in the Project level Admin tool.
  - [Create Equipment from a T&M Ticket](/product-manuals/tm-tickets-project/tutorials/add-equipment-entries-on-a-tm-ticket) in the T&M Tickets tool.

#### Configure Notifications

- To configure notification settings for users:

  - [Configure T&M Ticket Admin settings](/product-manuals/tm-tickets-project/tutorials/configure-advanced-settings-tm-tickets) to designate who receives notifications about T&M tickets.

#### Set Up Reports

- To capture data about T&M tickets:

  - [Create a custom project report](/product-manuals/reports-project/tutorials/create-a-project-single-tool-report) to gain real-time insights.
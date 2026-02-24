# Overview of Custom Role Permissions

Source: https://help.clio.com/hc/en-us/articles/40062980685467-Overview-of-Custom-Role-Permissions

---

After creating a role, the available sections provide detailed options for controlling user access to various areas of Clio Manage. Since a custom role can result in slight differences in the user experience, you can review the information below to understand how these permissions can impact your access to information and workflows.

## Contacts management

Contact management permissions control a user's ability to view and manage contacts, as well as define what actions a user can perform with them.

- **Edit contacts:** Allows users to edit contact properties like type, name, contact information, address, tags, custom fields, employees, and billing preferences
- **Delete contacts**: Allows users to remove a single contact record from the system. A deleted contact can be recovered by the system administrator.

 **Note:** To enable Delete contacts permissions, first enable **Edit contacts** permission.
- **Create contacts:** Allows users to add a new contact, person, or company to their firm.

 **Note:** To enable Create contacts, first enable **Edit contacts**.
- **Export contacts**: Enables the exporting of the firm's contacts via a PDF or CSV file.
- **Bulk delete contacts:** Allow users to remove multiple contacts simultaneously.

 **Note:** To enable Bulk delete contacts, first enable **Delete contacts**.

## Matter management

Matter management permissions control user access to matters and all associated information, including documents, notes, communications, and activities. You can define which roles can view, edit, create, delete, and export matter-related information. This ensures data integrity and appropriate matter access for each user role. These permissions define what a user can do with matters.

- **Edit matter properties**: Allow users to edit properties for a single matter. Matter properties include:
 - Matter details
 - Matter permissions
 - Matter notifications
 - Blocking users
 - Related contacts
 - Custom fields
 - Billing preferences for the matter
 - Task list
 - Documents folder
 - Reports
 - Grants
 - Personal injury preferences
- **Bulk edit matters**: Allow users to edit multiple matters simultaneously. These actions include:
 - Update matter status
 - Update matter permissions
 - Update responsible attorney
 - Block and unblock users

**Note:** To enable Bulk edit matters, first enable **Edit matter properties**.

- **Delete matters**: Allow users to delete a single matter record from the system. The following content relating to this matter will be deleted:
 - Tasks
 - Notes
 - Clio for Co-Counsel access
 - Clio for Clients access
- The following content will no longer be associated with this matter:
 - Contacts
 - Calendar events
 - Activity entries
 - Bills
 - Documents
 - Communications
 - Grants

**Important:** Deleting a matter is a permanent action.

**Note:** To enable Delete matters, first enable **Edit matter properties.**

- **Bulk delete matters**: Allow users to delete multiple matters at the same time from the firm.

 **Important:** Deleting a matter action is permanent.

 **Note:** To enable Bulk Delete of matters, first enable Edit matter properties.
- **Create matters**: Allow users can create a new matter in the firm.
- **Export Matters**: Allow users to export matters in PDF or CSV format.
- **View matter timeline**: Allow users to see a chronological view of all activities and updates related to a specific matter. This includes actions like document uploads, time entries, and stage changes, located in the matter dashboard.
- **View restricted matters**: Views high-level info for matters the user cannot access.
- **View matter financials**: Allow users read-only access to the financial overview section on the matter dashboard. These include:
 - Work in progress balance
 - Outstanding balance
 - Matter trust funds balance
 - Matter budget (Billable and Non-billable)

## Timekeeping

Timekeeping permissions control a user's access to activities and expenses.

#### View Activities

- **View all activities**: Allow users to view all activities.
- **View activities from assigned matters:** Allow users to view all activities from matters they own or have access to.
- **View own activities:** Can view their own activities only.

## Financial management

Financial permissions control access to bills, transactions, and accounts. These permissions are critical for custom roles as they determine a user's access to financial subtabs (e.g., Transactions and Bills) within a matter or contact card. These permissions determine a user's access to financial actions and details of your firm's finances.

#### Bills and trust requests

- **View bills and trust requests:** Allow users to view the Bills section in the left navigation and the Bills tab in Matters and Contacts. Including view, quick view, download, copy links, and print.
- **Manage bills and trust requests:** Allow users to approve, edit, delete, send, submit bills, apply trust funds, accept online payments, record payments, and issue refunds.

 **Note:** To enable Manage bills and trust requests permissions, first enable **View bills and trust requests.**
- **Create bills and trust requests:** Allow users to create new bills, new trust requests, statements of accounts, legal aid bills, quick bills, and duplicate new requests.

 **Note:** To enable Create bills and trust requests, first enable **Manage bills and trust requests** and **View all activities.**

#### Accounts

Accounts permission allows users to see account information based on the following three levels:

- **View all account information:** Includes all accounts in the firm, account balances, and account properties. Enables access to accounts in the global navigation.

 **Note:** To enable Bulk edit matters, first enable **Edit matter properties.**
- **Limited view of account information:** Display account names and essential details for managing transactions and bills without displaying balances. Does not enable access to accounts in the global navigation.
- **Views no accounts:** Does not see any account information.

 **Note:** You will need to disable **Manage bills and trust requests** and **View transactions** to enable View no accounts.

#### Transactions

- **View transactions:** Allows users to see the **Transactions** tab within a Matter or Contact card. This permission is required for users to view trust account activity and retainer balances.

 **Note:** To enable **View transactions**, you will need to enable either **View all account information** or **Limited view of account information**.

## Firm settings

Firm settings permissions control a user's ability to view and manage your firm's administrative information. These permissions define what a user can do with firm-wide settings.

- **View account firm feed:** Allow users to view the firm feed via the firm's dashboard.
- **Manage roles:** Allow users to create, edit, archive, assign, and unassign roles to other firm users.
- **Manage users:** Allow users to invite, remove, and edit firm user information.
- **Manage custom fields:** Allow users to create, edit, delete, and convert contact and matter custom fields.

## Conflict check

Conflict check settings control a user's ability to initiate conflict checks and view the conflict check report. Learn about conflict checks [here](https://help.clio.com/hc/articles/35286010477979).

- **Create, view, and manage conflict checks:** Any potential conflict found that is associated with a matter to which a user does not have access will appear as a line item marked as hidden and will be inaccessible to the user.
- **View conflict check report, bypassing matter and contact visibility permissions:** By default, only administrators have the ability to view a conflict check report.

 **Important:** When applying this permission, a user will be able to view the full PDF report. The report includes information about all conflict check results, including details that the user may not normally have access to, as specified by the [matter permissions](https://help.clio.com/hc/articles/9286062516123-Matter-Permissions-and-Rates).
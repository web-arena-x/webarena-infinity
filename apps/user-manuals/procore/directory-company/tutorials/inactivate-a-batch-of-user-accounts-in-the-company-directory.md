# Deactivate User Accounts in the Company Directory

Source: https://v2.support.procore.com/product-manuals/directory-company/tutorials/inactivate-a-batch-of-user-accounts-in-the-company-directory

---

## Background

Maintain comprehensive project history and accurate recordkeeping by keeping all user information within your organization's Procore company account. While direct deletion isn't an option, you can easily deactivate a user's profile to prevent login access.

Before deactivating an account in the Company Level Directory, ensure a seamless transition by closing any pending assigned items or reassigning them to another user. Procore highly recommends completing these steps before deactivation for optimal results. For a helpful overview of a user's open assignments, 'Admin' level users can conveniently view the Assignment Report in the company's Reports tool.

Some considerations to take into account prior to deactivating a user are outlined in the example below.

##### Examples

If a user is associated with any open items on an active project, be sure to either close those items or reassign them to another user using the appropriate project tool in Procore. This should always be completed prior to deactivating a user in your organization's Company level Directory.Some best-practice considerations include, but are not limited to, the following:

- Is the user an 'Employee' who requires a final timecard entry in the 'Timecard Entry' area of the Daily Log? See [Create a Timecard Entry](/product-manuals/timecard-company/tutorials/create-a-timecard).
- Is the user designated in the 'Assignment' field on a meeting item? See [Edit a Meeting Item](/product-manuals/meetings-project/tutorials/edit-a-meeting-item).
- Is the user designated as 'Point of Contact' for a Responsible Contractor in an inspection? See [Edit a Project Level Inspection](/product-manuals/inspections-project/tutorials/edit-a-project-level-inspection).
- Is the user designated as an 'Assignee' on an observation? See [Edit an Observation](/product-manuals/observations-project/tutorials/edit-an-observation).
- Is the user designated in the 'Assigned To' field on a punch list item? See [Edit a Punch List Item](/product-manuals/punch-list-project/tutorials/edit-a-punch-list-item).
- Is the user an 'RFI Manager' or 'Assignee' on an RFI? See [Edit an RFI](/product-manuals/rfi-project/tutorials/edit-an-rfi).
- Is the user a 'Submittal Manager' or an 'Approver' on a submittal? See [Edit a Submittal](/product-manuals/submittals-project/tutorials/edit-a-submittal).

## Things to Consider

- [Required User Permissions](/product-manuals/directory-company/permissions)
- After a user is inactive, the following is true:

 - The user will not be able to access your company's account when they log in.
 - The user's name is removed from the selectable options in 'User' drop-down menus.
 - The user information remains in the Company level Directory and is archived in the Inactive Users view. A user with 'Admin' level permissions to the Directory can reactivate the user at any time.
 - All user activity is stored in Procore and open items remain in the state they were in at the time of deactivation.
 - The user no longer receives notifications for projects that they were a part of.

## Prerequisites

- Before you deactivate a user account in the company's Directory tool, it is recommended that a user with 'Admin' level permission close and/or reassign any open items that might be assigned to the user throughout Procore.

## Steps

1. Navigate to the Company level **Directory** tool.
2. Click **Users**.
3. Mark the checkbox next to one or more users you want to deactivate.
4. Click **Bulk Actions** and select **Inactivate**.
5. Review the list of users.
6. *Optional:* Click the X next to a user's name to remove them from the list.
7. Click **Inactivate**.
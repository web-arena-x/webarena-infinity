# Configure General Company Timesheets Settings

Source: https://v2.support.procore.com/product-manuals/timesheets-company/tutorials/configure-advanced-settings-company-level-timesheets

---

## Things to Consider

- [Required User Permissions](/product-manuals/timesheets-company/permissions)

## Prerequisites

- Your company must have Procore's Resource Management license and enable the included tools.

## Steps

1. Navigate to the company's **Timesheets** tool.
2. Click the **Configure Settings**  icon.
3. Click the **Configurations** tab.
4. Update the settings under the following sections:

   - **Shared Settings**  
     *Note:* These settings apply to Timecards, Timesheets, and Daily Log.

     - **Employee Tracking on Projects**

       1. Mark this checkbox to enable a employees and workers of your company to be automatically added to the employee list on all Resource Tracking tools for all projects.  
          *Note:* To add users as workers or employees, see [Add a Worker](/product-manuals/crews-project/tutorials/add-a-worker) and [How do I add someone as an employee of my company?](/product-manuals/directory-company/tutorials/add-someone-as-an-employee-of-your-company)
     - **Timecard Privacy**

       1. Mark the checkbox to make timecards private by default.

          ##### Â Notes

          - Private Timecards are only visibile to the creator of the timecard, the user the time is being tracked for, and admins of the Timesheets tool.
          - Enabling the setting will make all existing and future timecards across all project private.
          - This privacy setting only affects the visibility of timecards in the Timesheets tools. It does not change the privacy of timecards in the company level Timecard tool and the Daily Log Timecard module. See [What is a 'private' timecard and which timecards can be set to private?](/faq-what-is-a-private-timecard-and-which-timecards-can-be-set-to-private)

- **Timecard Rounding.** See [What is timecard rounding and how does it work in Procore?](/faq-what-is-timecard-rounding-and-how-does-it-work-in-procore)

  1. Mark the checkbox to enable rounding on timecards.
  2. Select the **time increment**.
  3. Select the **rounding direction**.
- **Timesheet Settings**

  - **Limit Available Cost Codes by Cost Type**.

    1. Mark the checkbox next to the cost types that you want to show to users in the Timesheets tool for labor and equipment. To add cost types, see [Add Company Cost Types](/product-manuals/admin-company/tutorials/add-company-cost-types).
  - **Default Cost Type for Timecards**  
    *Note:* If your company is using Procore's Project Financials, this configuration assigns the selected cost type to timecard entries for real-time visibility into labor costs in the budget tool.

    1. Select the default **cost type** to assign to your project's **labor** timecard entries.
    2. *Optional:* Mark the checkbox to **Apply to Existing Entries** to apply the default cost type to all existing timecard entries.
    3. Select the default **cost type** to assign to your project's **equipment** timecard entries.
    4. *Optional:* Mark the checkbox to **Apply to Existing Entries** to apply the default cost type to all existing timecard entries.

       ##### Â Important

       - Applying a new default cost type to existing timecards by clicking **Apply to existing timecards** is a one-time action and cannot be undone without contacting your Procore point of contact.
       - If your company is using Resource Tracking with Project Financials, you must assign a Default Cost Type to timecard entries before your project teams can work with the following budget views:

         - [Resource Tracking and Project Financials: Setup Guide](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/resource-tracking-and-project-financials-setup-guide)
         - [Set Up the Procore Labor Productivity Cost Budget View](/process-guides/resource-tracking-and-project-financials-setup-guide/preview-the-budget-view)

- If your company is integrated with an **ERP system** **Show/Hide Details**

  - **Default Cost Type for Timecards on Non-ERP Synced Projects.**

    1. Select the cost type to assign to timecard entries for non-ERP synced projects.

       - Click **Update** to apply the default cost type to any future timecard entries.
       - Click **Apply to Existing Timecards** to apply the default cost type to all existing timecard entries.
  - **Default Cost Type for Timecards on Synced Projects.**

    1. Select the cost type from your payroll system to assign to your project's timecard entries.

       - Click **Update** to apply the default cost type to any future timecard entries.
       - Click **Apply to Existing Timecards** to apply the default cost type to all existing timecard entries.
- **Custom Signature Text**. Enter the text you want to show in the Signature field when a user is signing their time entry.
- Click **Save**.
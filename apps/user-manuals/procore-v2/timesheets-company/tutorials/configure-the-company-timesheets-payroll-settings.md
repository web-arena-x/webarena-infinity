# Configure Payroll Settings for Timesheets

Source: https://v2.support.procore.com/product-manuals/timesheets-company/tutorials/configure-the-company-timesheets-payroll-settings

---

## Things to Consider

- [Required User Permissions](/product-manuals/timesheets-company/permissions)
- To add users to the email distribution list, they must be listed in your Company Directory.

## Prerequisites

- Your company must have Procore's Resource Management license and enable the included tools.

## Steps

1. Navigate to the company's **Timesheets** tool.
2. Click the **Configure Settings**  icon.
3. Click the **Payroll** tab.
4. Update the settings under the following sections:

   - **Payroll Settings**

     - Select your company's **Default Work Week**.
     - ##### Beta

       Company Administrators can [enable](/product-manuals/admin-company/tutorials/manage-features-with-procore-explore) the **Timesheets - Closing A Pay Period** beta in [Procore Explore](https://app.procore.com/earlyaccess/programs/closing_a_pay_period). ([US 2](https://us02.procore.com/earlyaccess/programs/closing_a_pay_period) **|** [UK](https://uk01.procore.com/earlyaccess/programs/closing_a_pay_period))

       - Select your company's **Pay Period Frequency**.
       - Click the **Email Distribution** field, then enter and select the names of the users to be notified when a time entry has been created for a closed pay period.
       - Enter the **Custom Message** an employee will be sent when they submit a timecard for a closed pay period.

- **Manage Time Types**

  1. Mark the checkbox next to the **time types** you want to show in the Timesheets tool.
  2. *Optional:* To add a new time type, enter the **Type** and **Abbreviation**, then click **Add**.
- **Payroll Export Settings**

  1. Select your supported payroll system to transfer entries from Company Timesheets.

     - **QuickBooksÂ® Desktop (2021 or before)**Select this option for all versions of QuickBooksÂ® Desktop when you also use **QuickBooksÂ® Time**. (This includes QuickBooksÂ® Desktop for 2022 and after when you also use QuickBooksÂ® Time.)

       1. Drag and drop the [Timer List IIF File you exported from QuickBooksÂ® Desktop](/product-manuals/timesheets-company/tutorials/export-timecard-entries-from-procore-to-import-into-quickbooks-software) 'Attach Files' area. This file provides the data tables Procore needs to export your time entries back to QuickBooksÂ® Desktop later.

          - ##### Â Important

            If the IIF file contains data, the Time Types and Employee Names in QuickBooksÂ® Desktop must exactly match the Time Types and User/Contact Names in Procore.

- **QuickbooksÂ® Desktop (2022 or after)**

  ##### Note

  - After selecting this option, you can attach the IIF file that you exported Procore's Company level Timesheets.
  - This option is intended for customers who upgraded to QuickBooksÂ® Desktop 2022 or after without purchasing QuickbooksÂ® Time.
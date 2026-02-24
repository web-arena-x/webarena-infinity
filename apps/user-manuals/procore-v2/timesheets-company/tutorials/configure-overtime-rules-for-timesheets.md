# Configure Overtime Rules for Timesheets

Source: https://v2.support.procore.com/product-manuals/timesheets-company/tutorials/configure-overtime-rules-for-timesheets

---

##### Â In Beta

This feature is currently in Beta.

## Background

You can configure overtime rules to automatically apply overtime and double time rates. Company rules are applied to all projects by default and apply to Timesheets, Timecards, My Time, and Daily Log Timecard entries. You can create project rule sets that override the company rules, and apply them to specific projects.

## Things to Consider

- [Required User Permissions](/product-manuals/timesheets-company/permissions)

## Steps

- Enable and Configure Company Overtime Rules
- Create Project Overtime Rules and Assign to Projects

### Enable Overtime Management and Configure Company Overtime Rules

1. Navigate to the company's **Timesheets** tool.
2. Click the **Configure Settings**  icon.
3. Click the **Overtime Management** tab.
4. Move the **toggle**  to the ON position to 'Enable Overtime Management'.
5. *Optional:* Move the **toggle**  to the ON position to 'Always automatically apply overtime rules when creating time entries'.  
   *Note:* If this toggle is off, users entering timesheets can select whether or not to apply overtime rules.
6. Configure Overtime Time Types

   ##### Â Important

   Time types should match your ERP or payroll system to streamline payment processing. See [Configure Payroll Settings](/product-manuals/timesheets-company/tutorials/configure-the-company-timesheets-payroll-settings).

1. Select the **time type** to apply to Regular Time.
2. Select the **time type** to apply to Overtime Time.
3. Select the **time type** to apply to Double Time.
4. Click **Next**.

- Create 'Company Overtime Rules' that are applied by default to all projects.  
  *Note:* Regular time is applied until employees exceed the thresholds you configure.

  - Mark the checkbox to **Apply Weekly Overtime Rules**.

    1. Enter the number of **hours in a week** after which overtime is applied.
  - Mark the checkbox to apply **Daily Overtime Rules**.

    1. Enter the number of **hours in a day** after which overtime is applied.
  - Mark the checkbox to apply **Daily Double Time Rules**.

    1. Enter the number of **hours in a day** after which double time is applied.
- Click **Enable**.

##### Â Note

After Overtime Rules have been enabled, you can make changes at any time by clicking **Edit** for the relevant section.
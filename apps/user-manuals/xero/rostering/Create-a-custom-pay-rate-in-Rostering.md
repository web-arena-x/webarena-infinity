# Create a custom pay rate in Rostering (BETA)

Source: https://central.xero.com/s/article/Create-a-custom-pay-rate-in-Rostering

---

## Overview

- Use the pay rate builder to create a custom pay rate.

Tip

Rostering and advanced timesheets is currently in closed beta and is restricted to a small number of users.

How it works

- Use the pay rate builder to edit an existing pay rate in Rostering and advanced timesheets to meet your requirements or create a new pay rate.
- You need [system administrator or advisor access](Access-levels-in-Rostering-explained.md) to create custom pay rates.
- Before you start, we recommend that you edit your business settings and [change the timesheet recalculation setting](Approve-or-unapprove-a-timesheet.md) to **All timesheets within the applicable range**.
- For more information on pay rule calculation types, including overtime rates, see [Deputy’s help centre](https://help.deputy.com/hc/en-au/sections/10067928388879-Pay-rule-calculation-types) (Deputy website).

View pay rates

To view your pay rates:

1. In the **Payroll** menu, select **Rostering and advanced timesheets**.
2. In the **Settings** menu, select **General settings**.
3. Select the **Pay** tab.
4. Click **View pay rates**.

To filter the pay rates by status, click the arrow icon next to the **Search** field, then select or clear the checkbox next to the relevant pay rate status.

Create a pay rate

Tip

Not all library pay rates are currently available to edit using the pay rate builder.

### Customise existing pay rate

Customise an existing pay rate to use a rate from the pay rate library with minor changes, such as adjusting the multiplier rate or adding pay rules. This creates a copy of the pay rate that you can adjust. The original pay rate remains unchanged.

1. In the **Payroll** menu, select **Rostering and advanced timesheets**.
2. In the **Settings** menu, select **General settings**.
3. Select the **Pay** tab, then click **View pay rates**.
4. Click **Create pay rate**.
5. Select **Customise existing pay rate**.
6. Select the type of employee and the existing pay rate you want to customise, then click **Create**.

### Start from scratch

Create a brand new pay rate with no preconfigured settings.

1. In the **Payroll** menu, select **Rostering and advanced timesheets**.
2. In the **Settings** menu, select **General settings**.
3. Select the **Pay** tab, then click **View pay rates**.
4. Click **Create pay rate**.
5. Select **Start from scratch**.
6. Under **Name of contract**, enter a name for the pay rate, then click **Create**.

### Duplicate pay rate

Duplicate a pay rate to copy and edit an existing pay rate.

1. In the **Payroll** menu, select **Rostering and advanced timesheets**.
2. In the **Settings** menu, select **General settings**.
3. Select the **Pay** tab, then click **View pay rates**.
4. Next to the pay rate you want to duplicate, click the options icon , then select **Duplicate**.
5. Under **Name of contract**, enter a name for the pay rate, then click **Duplicate** or **Duplicate and edit**.

Edit the pay rate general settings

The pay rate details are the key details that make up the pay rate.

1. In the **Pay rates** screen, click the options icon next to the pay rate, then select **View**.
2. Select the **General** tab.
3. Next to **Pay rate details**, click **Edit**.
4. Enter the name and select the employment type for the pay rate.
5. Next to **Start of the week day**, select the start time of a new day. This defaults to midnight.
6. Next to **Split time worked over the end of the day**, select **Yes** or **No**. When a shift crosses the end of a work day, hours can count towards that work day or the following day for overtime. Select **No** for hours to belong to the day the shift started.
7. Select the status of the pay rate. Only pay rates with an **Active** status can be assigned to employees.
8. Click **Save**.

Set the regular rate of pay

### Set a regular rate

The regular rate of pay is the rate paid to an employee when no other pay rules apply. Regular rates are used as a multiplier by other rates such as overtime.

To set a regular pay rate:

1. In the **Pay** **rates** screen, click the options icon next to the pay rate, then select **View**.
2. Select the **Regular pay** tab.
3. Next to **Regular rates**, click **Edit**.
4. Enter the name, regular rate, classification and export code for the pay rate.
5. Click **Save**.

### Set a junior rate

You can set junior rates for any junior employees. On the junior employee’s birthday, Rostering and advanced timesheets will automatically update the employee’s pay rate based on their age. If the employee has a higher rate set in their profile, Rostering and advanced timesheets won’t update the pay rate.

To set a junior pay rate:

1. In the **Pay rates** screen, click the options icon next to the pay rate, then select **View**.
2. Select the **Regular pay** tab.
3. Next to **Junior rates**, click **Edit**.
4. Select **% of regular rate** to set the rates as a percentage of the regular pay rate or select **per hour** to set the rates as a flat value per hour.
5. Enter the relevant rate for each age.
6. Click **Save**.

Add, edit or delete pay rules

### What you need to know

- A pay rule is a specific way an employee can be paid. For example, use a daily overtime rule to pay an employee overtime when they work more than eight ordinary hours in a day.
- Add a pay rule from a list of calculation types. Each calculation type has existing rules that dictate how pay rules are applied.
- Set the pay rate of a pay rule to determine how the pay rule is paid. Select **Multiple of regular rate** to pay the user’s pay rate multiplied by an amount (eg enter 1.5 to pay 1.5 times the user’s regular pay rate) or select **Flat rate** to pay a set amount per hour.
- For more information on pay rule calculation types, including overtime rates, see [Deputy’s help centre](https://help.deputy.com/hc/en-au/sections/10067928388879-Pay-rule-calculation-types) (Deputy website).

### Add a pay rule

1. In the **Pay rates** screen, click the options icon next to the pay rate, then select **View**.
2. Select the **Pay rules** tab.
3. Next to **Pay rules**, click **Add**.
4. Select the pay rule you want to add, then click **Add pay rule**.
5. Enter a name for the pay rule and adjust the settings of the pay rule as required.
6. Click **Save**.

### Edit a pay rule

1. In the **Pay rates** screen, click the options icon next to the pay rate, then select **View**.
2. Select the **Pay rules** tab.
3. Next to the pay rule you want to edit, click **Edit**.
4. Make your changes to the pay rule, then click **Save**.

### Delete a pay rule

1. In the **Pay rates** screen, click the options icon next to the pay rate, then select **View**.
2. Select the **Pay rules** tab.
3. Next to the pay rule you want to delete, click the options icon , then select **Delete**.
4. Click **Delete**.

### Change shared settings

Shared settings are pay rule settings that are shared between multiple pay rules. Adjust shared settings to set default rules.

1. In the **Pay rates** screen, click the options icon next to the pay rate, then select **View**.
2. Select the **Pay rules** tab.
3. Next to **Shared settings**, click **Edit**.
4. Update the settings as required, then click **Save**.

Change the pay rate rule priorities

Use the pay rate rule priority to set the order rates are applied when an employee’s pay is calculated. This priority is used when two rules conflict and both apply to an employee’s timesheet.

1. In the **Pay rates** screen, click the options icon next to the pay rate, then select **View**.
2. Select the **Rule Priorities** tab.
3. Next to **Rule priority**, click **Edit**.
4. Use the reorder icon to click and drag your pay rate rules into the desired order. The highest priority pay rule should be at the top of the list.
5. Click **Save**.

Hide a pay rate

If you don’t want a pay rate to be available to select for an employee, you can set the pay rate to Inactive or Draft. You can’t delete a pay rate.

1. In the **Pay rates** screen, click the options icon next to the pay rate, then select **View**.
2. Select the **General** tab.
3. Next to **Pay rate details**, click **Edit**.
4. Next to **Status**, select **Inactive** or **Draft**, then click **Save**.

## What's next?

Now you’ve created your new pay rate, you can [assign the pay rate](Set-an-employee-s-pay-rate-or-award.md) to your employees.
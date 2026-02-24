# Set up a repeating journal

Source: https://central.xero.com/s/article/Set-up-a-repeating-journal

---

## Overview

- Set up a repeating journal in Xero to automatically create journals in a weekly or monthly series, for a specified period.

## About repeating journals

Set up repeating journals to automate a series of recurring journal entries.

- Insert placeholders to populate dates that depend on when the repeating journal was generated.
- You can backdate repeating journals to the first day of your organisation's previous financial year.
- Repeating journals can be set to **Save as Draft** or **Post**. Repeating journals set to **Save as Draft** can be changed to **Post**. However, once a repeating journal has been set to **Post**, it can't be changed back to **Save as Draft**.
- You can edit repeating journals, but if you roll back the next journal date, Xero creates a new set of journals in addition to your existing ones.
- When you edit a repeating journal, changes take effect immediately. The next journal entry Xero creates will display and post the edited details. The History & Notes section will show that the journal has been edited, but it won’t show the details.
- You need the advisor or standard + reports user role to create repeating journals.

## Dates and frequency fields

| Field | Description |
| --- | --- |
| **First Journal Date** | The date you want Xero to start generating the journal. If the repeating journal is edited, this field will show as **Next Journal Date**. |
| **Repeat this journal every** | How often you want Xero to generate the journal. This can be a set number of weeks or months. If you choose a month-end date, Xero records the journals at the end of each month. For example, if you set up a repeating monthly journal starting 30 June, Xero records the next journal in the series at 31 July, not 30 July. |
| **End date** | The last date Xero should generate the journal. |
| **Save as Draft** or **Post** | If you need to make changes to the journal each time, or if it needs to be approved first, set the repeating journal to **Save as Draft**. If the journal will be the same each time it's recorded, set the repeating journal to **Post**. If repeating journals are set to **Post**, they can't be voided in bulk. Each repeating journal needs to be voided separately. |

## About placeholders

Placeholders are named markers where content will appear when a repeating journal is generated. The value of the placeholder will depend on the date of the repeating journal.

1. Click in the **Narration** or **Description** field to see the **Insert Placeholder** link.
2. Click **Insert Placeholder**, then select the placeholder option.

   - You can add or subtract within the placeholder to change the placeholder value. For example, [Month-1] will display the previous month to the repeating journal month.
   - You can have more than one placeholder in a field. For example, if a journal is generated in April, with a description of [Month] to [Month+1], the journal will show April to May in the Description field.
   - Click **Preview placeholders** to see how the placeholders will appear in the journals.

Week calculations follow the ISO 8601 standard. Week 1 starts on Monday and always includes the first Thursday of the new year. The last week of the year will be either 52 or 53.

## Create a repeating journal

Tip

If you have an existing manual journal that you'd like to convert into a repeating journal, open the journal, then in the **Journal Options** drop-down, select **Repeat**.

To create a new repeating journal:

1. In the **Reporting** menu, select **All reports**.
2. Find and open the **Journal Report**. You can use the search field in the top right corner.
3. Click **Go to manual journals** to get to the manual journals screen.
4. Click **New Repeating Journal**.
5. Enter the date and frequency information for the repeating journal.
6. Select **Save as Draft** or **Post**.
7. (Optional) Add placeholders to the **Narration** and **Description** fields.
8. Enter the [journal details](Add-import-and-post-manual-journals.md) into the relevant fields.
9. Click **Save**.

View all the repeating journals set up for your organisation from the **Repeating** tab on the manual journals screen.

## What's next?

[Reverse a manual journal](Void-archive-or-delete-multiple-journals.md) or [copy a manual journal](View-edit-or-copy-a-manual-journal.md).
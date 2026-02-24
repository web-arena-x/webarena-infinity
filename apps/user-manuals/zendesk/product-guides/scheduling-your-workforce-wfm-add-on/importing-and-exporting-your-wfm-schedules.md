# Importing and exporting your WFM schedules

Source: https://support.zendesk.com/hc/en-us/articles/6443377641754-Importing-and-exporting-your-WFM-schedules

---

You can import your existing schedules into Zendesk Workforce management (WFM). You can also export a CSV of your schedules.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

You can import your existing schedules into Zendesk Workforce management (WFM). You can also
export a CSV of your schedules.

This article contains the following topics:

- [About importing a
  schedule](#topic-1__section_bgx_jhb_1dc)
- [Importing a schedule](#topic-1__section_dgx_jhb_1dc)
- [Exporting a schedule](#topic-1__section_fgx_jhb_1dc)

## About importing a schedule

Note the following key information before you import a schedule:

- Time off that's imported isn't overwritten during the schedule import and can result in
  two or more layers of time off in the same period.
- All shifts are overwritten if they start on the same day UTC.
- If there are overlaps due to overnight shifts, the import doesn't delete the previous
  day's schedule but will create overlaps.
- When filling out the Import template, ensure that the agents' names and emails match
  exactly in Zendesk WFM. You may want to [export your list of agents](https://support.zendesk.com/hc/en-us/articles/7446311222042). Note that fields are case-sensitive.

## Importing a schedule

**To import a schedule**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_calendar.png)
   **Schedule** in the navigation bar, then select **Schedule**.
2. Click the **CSV** icon.
3. Select **Import schedule**.
4. Click **Schedule import template**.

   When you click this button, two template files
   can be downloaded:
   - The Schedule import template file, that contains an example of how your
     CSV should be formatted.
   - The Task field keys file, that contains the IDs of all your tasks:
     - Workstreams
     - [General tasks](https://support.zendesk.com/hc/en-us/articles/6443329426330) or [unified agent statuses](https://support.zendesk.com/hc/en-us/articles/10114746509978) (both listed as
       *generalTask*)
     - Time off reasons.
5. Upload your CSV file.
6. Click **Import schedule**.

## Exporting a schedule

**To export a schedule**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_calendar.png)
   **Schedule** in the navigation bar, then select **Schedule**.
2. Click the **CSV** icon.
3. Select **Export Schedule**.
4. Choose if you want to export the **Published schedule** or **Draft version**.
5. Select a **Date range**.
6. Click the **Agents** tab, then select the agents whose schedule you want to
   export.
7. Click **Export schedule**.

   The export is sent to your email when it's
   complete.

Note: If there's no schedule entered or the schedule is not published, the export downloads
without any data for the selected date range and users. Make sure that the date range
you're exporting has a draft version or schedule available.
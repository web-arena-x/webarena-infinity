# Scheduling dashboard deliveries

Source: https://support.zendesk.com/hc/en-us/articles/4408843602714-Scheduling-dashboard-deliveries

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

After you share a dashboard, you can notify users of updates by automatically emailing the latest version on a schedule you configure. In this article, you'll learn to email dashboards to other agents, admins, and groups. On Enterprise plans, you can also [email dashboards to end users](https://support.zendesk.com/hc/en-us/articles/4408835716378).

This article contains the following topics:

- [Scheduling a dashboard delivery](#topic_iwv_gvz_mhb)
- [Reviewing and modifying an existing scheduled delivery](#topic_byr_4h3_fvb)
- [Deleting a scheduled delivery](#topic_uw3_spn_nhb)

## Scheduling a dashboard delivery

Important: As of early 2025, Zendesk is transitioning customers to a new version of the dashboard builder. If you used the legacy dashboard builder to schedule an email delivery of a prebuilt or custom dashboard, you'll need to recreate the scheduled delivery in the new dashboard builder. See [Migrating legacy Explore dashboards to the new dashboard builder](https://support.zendesk.com/hc/en-us/articles/8096478451098).

After you [open a dashboard](https://support.zendesk.com/hc/en-us/articles/4408831997466), you can schedule a delivery to one or more groups. To create a schedule, you must have [permissions to edit the dashboard](https://support.zendesk.com/hc/en-us/articles/4408836002970).

**To schedule a dashboard delivery**

1. In an Explore dashboard that you have previously [shared](https://support.zendesk.com/hc/en-us/articles/4408827282714), click **Share** > **Schedule delivery**.

   On the **Scheduled deliveries** page, you'll see any delivery schedules you previously configured.
2. Click **Schedule delivery**.

   ![Explore dashboard delivery schedule](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_delivery_1.png)
3. On the **Schedule delivery** page, configure the following options:
   - **Frequency:** Use the drop-down lists to configure the time and recurrence for when each dashboard should be run.

     Note that the *scheduled* time isn’t exactly the same as the *delivery* time. The scheduled time of a dashboard is the point in time at which the dashboard’s reports are calculated using the data that's currently synced in Explore. Meaning, if you schedule a dashboard for 9 AM, recipients might not get the dashboard until sometime after 9 AM, but the reports they see when they do get the dashboard will reflect the data that existed in Explore as of 9 AM.

     For complex reports or large sets of data, it might take some time for the data to be calculated and sent before the dashboard reaches recipients.

     Note: If you're scheduling a dashboard that should return data for the entire previous day, make sure to schedule it for 2 AM or later. [Explore's data sync](https://support.zendesk.com/hc/en-us/articles/4408820703386) can take up to two hours to complete, so scheduling your delivery for 2 AM ensures that the previous day's data has fully synced before the dashboard is sent.
   - **Run for:** From the drop-down list, select for how long you want to share the dashboard. You can select up to 12 months in the future.

     The person who created the schedule and all Explore admins will receive two reminders when your schedule is nearing expiration: one week before and one day before the expiration date.
   - **Format:** Select one or more delivery formats. Choose from:
     - **CSV:** Sends each report as a comma-separated values (.csv) file. The .csv files for each tab are compressed as a .zip file.

       Note: Scheduled deliveries have an email attachment limit of 25 MB. To avoid hitting this limit when scheduling large dashboards, refrain from using both Image and PDF formats at the same time. If the size of the scheduled dashboard exports are larger than 25MB, the export will be sent in multiple emails. The emails will be marked sequentially in the subject with, for example, 1/3, 2/3, 3/3. If any single export is larger that 25MB, it will not be sent.
     - **Excel (formatted):** Sends the dashboard as an Excel (.xlsx) file for each tab.
     - **PNG:** Sends the dashboard as an image (.png) file for each tab.
     - **PDF:** Sends the dashboard as a single PDF (.pdf) file that includes all tabs.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_delivery_2.png)
4. **People or groups:** Choose the groups or users to send the dashboard to. You can begin typing a group or user name in the search box, and then select it once it's displayed in the list.

   If you're using Explore Enterprise and want to schedule dashboard deliveries to end users, you must first enable this for each user by adding the **explore** tag to their user profile. For details, see [Scheduling dashboard deliveries with end users](https://support.zendesk.com/hc/en-us/articles/4408835716378).

   You cannot schedule dashboards to users with [Limited viewer and Limited editor permissions](https://support.zendesk.com/hc/en-us/articles/4408836002970).
5. When you're finished, click **Save**.

The schedule you configured is displayed on the **Scheduled deliveries** page.

Recipients of scheduled deliveries are grouped by language and time zone, with one email sent to each group. For details, see [Why do Explore scheduled dashboard emails exclude some recipient addresses?](https://support.zendesk.com/hc/en-us/articles/7513074447258) If a scheduled delivery fails, a notification email is sent to the owner of the schedule only.

Recipients of the email will only see their own email address in the email "To" field. For security purposes, the names of other recipients are hidden.

Note: When an agent is downgraded, any scheduled deliveries they created are immediately deleted and are no longer available for review on this page. For more information, see [Downgrading and removing an agent](https://support.zendesk.com/hc/en-us/articles/4408888690842#topic_dx3_t23_m5b).

## Reviewing and modifying an existing scheduled delivery

From the dashboards library, you can review and modify scheduled deliveries. Admins can see all scheduled deliveries, but editors can see only their own scheduled deliveries.

**To modify a scheduled delivery**

1. In Explore, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.

   The **Schedules** column shows you the number of schedules a dashboard is included in.
2. Find the dashboard you want to review the schedule for and select it to open it.
3. Click **Schedule**.
4. On the **Scheduled deliveries** page, click the edit icon for the schedule you want to modify.

   ![Explore dashboard delivery schedule](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_delivery_1.png)
5. Make any changes to the delivery details or recipients as necessary. See [Scheduling a dashboard delivery](#topic_iwv_gvz_mhb) for help.
6. When you're done, click **Save**.

## Deleting a scheduled delivery

You can delete a delivery you previously configured from the **Scheduled delivery** page.

1. In Explore, click the **Dashboard** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) in the left sidebar.
2. Find the dashboard you want to delete the schedule for and click to open it.
3. In the dashboard, click **Share** > **Schedule delivery**.
4. In the **Scheduled deliveries** click the trashcan icon for the delivery you want to delete, then confirm the deletion.

The schedule is deleted and users will no longer receive emails.
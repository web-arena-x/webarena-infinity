# Setting up the Time Tracking app

Source: https://support.zendesk.com/hc/en-us/articles/4408828227098-Setting-up-the-Time-Tracking-app

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

Use the Time Tracking app to monitor how much time agents spend on tickets. Once you've set
up the app, see [Using
the Time Tracking app](https://support.zendesk.com/hc/en-us/articles/4408822487450) to learn how to use it.

If you're looking for help using Zendesk Explore to generate reports about your time
tracking, see [Time Tracking app: metrics you need to be
measuring](https://support.zendesk.com/hc/en-us/articles/4408825230490).

This article covers the following topics:

- [Important considerations](#topic_jk1_3tn_zzb)
- [Installing and configuring the Time Tracking app](#topic_edz_3ry_g4)
- [Understanding Time Tracking custom ticket fields](#topic_vdh_vs2_44)

## Important considerations

- When the installation is complete, the Time Tracking app automatically creates two
  custom ticket fields to store time: **Time spent last update** and **Total time
  spent**. These fields need to be added to your ticket forms. See [Understanding Time Tracking custom ticket
  fields](#topic_vdh_vs2_44).
- The **Time spent last update** and **Total time spent** fields are hidden from
  agents in roles with permission to use the app. If you use several apps, there might be a
  slight delay when loading the app in the Apps panel, briefly exposing these fields.
- The **Time spent last update** and **Total time spent** fields can be updated via
  the API. In very rare cases, agents have used this to modify time in these fields.
- When [managing tickets in bulk](https://support.zendesk.com/hc/en-us/articles/4408886890906), changes made to the
  **Time spent last update** and **Total time spent** fields in the bulk editor
  aren't recorded.
- If an agent quickly updates and submits a ticket (manually or via a macro) before the
  Time Tracking app can fully load in the Apps panel, it could result in time not being
  recorded.
- Agents can find ways to skip the app's loading process and its normal functions. There
  have been cases where agents have leveraged the limitations of the app to manipulate the
  times on tickets.
- The Time Tracking app doesn't work outside of a ticket in areas such as side
  conversations, the bulk ticket editor, and the Zendesk Support mobile app.
- If you uninstall the app, recorded time values on a ticket will no longer be visible in
  Zendesk Support, even if you reinstall the app.

## Installing and configuring the Time Tracking app

You can download and install the Time Tracking app from the [Zendesk
Marketplace](https://www.zendesk.com/apps/). With this app, you can track how much time agents spend working on
tickets. Light agents can't use this app.

**To install the Time Tracking app**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Apps > Channel
   apps**.
2. Click **Zendesk Marketplace**.
3. Find the **Time Tracking** app, then click the title.
4. On the app details page, click **Install**.
5. From the drop-down, choose the account you want to install the app to, then click
   **Install**.
6. On the app settings page, configure any settings you want, as described below. You can
   return to this settings page at any time by clicking **Apps** > **Manage** >
   **Time Tracking**:
   - **Title:** Displays the name of the app. You can edit this to be any name you
     want.
   - **Display timelogs to agents:** Determines if agents can see a log of time spent
     on that ticket so far, including the agent and status for each time interval.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/time-tracking-timelogs.png)
   - **Hide the app from agents:** Only displays the app to agents with the admin
     role. If the app is hidden, agents without the admin role cannot see or edit the
     timer.
   - **Auto pause:** Automatically pauses the timer when the agent navigates away from
     the ticket, such as by switching to another ticket tab. The timer resumes
     automatically when the agent navigates back to the ticket.

     Note: Auto pause will not
     occur when an agent's workstation is inactive or when they navigate to a different
     browser tab. This setting is specifically configured for switching between ticket
     tabs within Zendesk.
   - **Display timer controls:** Determines whether agents see the play and pause
     buttons next to the timer, allowing them to manually control when the timer starts and
     stops.
   - **Reset current time:** Determines whether agents can see the refresh button next
     to the timer, allowing them to start the timer over.
   - **Resume on changes:** When changes are made to any fields, the agent will be
     asked if the timer should be resumed.
   - **Edit time submission:** When you enable this setting, the window below appears
     when an agent submits a ticket. Agents can review and edit the time they spent on a
     ticket if, for example, they spent significant time discussing the issue with a
     colleague outside of Zendesk.

     With this feature enabled, agents are required to
     confirm their time in order to submit the ticket. They have 15 seconds from when the
     window opens to cancel.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/time-tracking-edit-time-submission.png)
   - **Simplified time submission:** Enables agents to edit and submit their time
     spent in minutes, rather than hours, minutes, and seconds. For example, with this
     setting enabled, an agent could enter "5" for five minutes. Without this setting
     enabled, the agent must enter it in the format "00:05:00". This setting only applies
     if you've also enabled the Edit time submission setting.
   - **Enable role restrictions:** Select which roles can use the Time Tracking app.
     The app will not appear and will not track time for roles you don't select if you have
     this setting enabled.

     Note: If you enable role restrictions, roles without access to
     the app will see the custom fields the app creates in their tickets. By design,
     roles with access to the app won't see the custom fields. For details, see [Understanding Time
     Tracking custom ticket fields](#topic_vdh_vs2_44__title_tcy_152_44).

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/time-tracker-enable-role-restrictions.png)
   - **Enable group restrictions:** Enables you to select which groups have access to
     the app.
   - **Block large time spent submissions:** Blocks submission of a ticket if an agent
     is trying to submit a ticket with a time spent value greater than two weeks.

   When you've finished configuring settings, click **Install**.
7. If your Zendesk plan includes multiple ticket forms, you must update all your forms to
   include two new custom ticket fields created by Time Tracking. For details, see [Understanding Time Tracking custom ticket fields](#topic_vdh_vs2_44).

## Understanding Time Tracking custom ticket fields

Installing Time Tracking automatically creates two custom ticket fields: **Time spent last
update** and **Total time spent**. To view the fields, in [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
**Objects and rules** in the sidebar, then select **Tickets > Fields**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/time-tracking-custom-fields.png)

By design, agents with access to the app won't see the custom fields on their tickets. If
you enable role restrictions, roles that *don't* have access to the app *will* see
the custom fields on their tickets.

If your Zendesk plan includes multiple ticket forms, you must manually move the new fields
to all your ticket forms. If you don't add the new fields to all your ticket forms, you will
receive an error message. See [Time Tracking app error message](https://support.zendesk.com/hc/en-us/articles/4411267942810).

**To add the custom fields to your ticket forms**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Forms**.
2. Click the name of a ticket form to open it.
3. Drag the **Time spent last update** and **Total time spent** fields from the list
   on the right onto your ticket form.

   For more information, see [Creating multiple ticket forms](https://support.zendesk.com/hc/en-us/articles/4408846520858).
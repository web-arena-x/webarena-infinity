# About Zendesk WFM workstreams

Source: https://support.zendesk.com/hc/en-us/articles/6443314489242-About-Zendesk-WFM-workstreams

---

Workstreams are part of your organization structure and serve as one of Zendesk Workforce Management’s (WFM) main building blocks. They're sets of tickets that agents work on and are similar to your regularZendesk channels, such as tickets, chats, and voice.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Workstreams help organize your team's workload by grouping tickets based on specific conditions, like email or regional calls. They inform forecasts and schedules, ensuring efficient resource allocation. You can create, edit, and delete workstreams, and even combine or prioritize them through the Early Access Program. This flexibility allows you to tailor workstreams to match your team's unique needs and priorities.

Workstreams are part of your organization structure and serve as one of Zendesk Workforce Management’s (WFM) main building blocks. They're sets of tickets that agents work on and are similar to your regular [Zendesk channels](https://support.zendesk.com/hc/en-us/articles/4408824097050), such as tickets, chats, and voice.

You define workstreams based on specific conditions to create custom channels or segmentations that reflect your team's work. For example, your team might respond to emails from a specific ticket form or take calls from a particular region.

Your forecasts are generated based on workstreams, which in turn inform your schedule.

This article contains the following sections:

- [Understanding workstreams](#topic_uhy_2jz_11c)
- [Creating workstreams](#topic_br5_tjz_11c)
- [Editing workstreams](#topic_qg3_rkz_11c)
- [Deleting workstreams](#topic_tg4_lsz_11c)
- [Creating combined workstreams (EAP](#topic_qbx_1tz_11c))
- [Prioritizing workstreams (EAP)](#topic_i1y_s5z_11c)

Related articles

- [Adding and removing users from multiple workstreams in bulk in Zendesk WFM](https://support.zendesk.com/hc/en-us/articles/9822760145818)

## Understanding workstreams

Workstreams capture tickets created after you [buy the Zendesk WFM add-on](https://support.zendesk.com/hc/en-us/articles/6851584037146).

Workstreams take into account each time a ticket enters a workstream, including changes made from one workstream to another.

When you run preview conditions on Workstreams, it shows how many tickets have entered a workstream over the past 30 days.

The workstream's preview match does not reflect unique tickets entering a workstream. Each time a ticket enters that workstream, it's counted, including when a ticket is [reopened](https://support.zendesk.com/hc/en-us/articles/8263915942938).

The [Forecast](https://support.zendesk.com/hc/en-us/articles/6443407875354) (where your [historical volume](https://support.zendesk.com/hc/en-us/articles/6443407875354#topic_ub5_whd_tzb) lives) is recalculated when you change workstream conditions.

The example below illustrates the workstream count:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_workstream_count_example.png)

Tickets created before you buy the WFM add-on aren't matched to workstreams in the agent activity page, but are counted towards the historical volume in the forecast.

If the matching criteria are met only in an update made after the ticket is set to Solved, the ticket fails to match the workstream.

## Creating workstreams

When you first add Zendesk WFM to your account, ticket, voice, and chat workstreams are created by default. You can also create additional workstreams.

You must be an [admin or user with permission](https://support.zendesk.com/hc/en-us/articles/6443374440090) to access the Workstreams page.

For the best results, don't exceed 50 workstreams or assign more than 5000 agents to a single workstream.

To add multiple users to workstreams at once, see [Adding and removing users from multiple workstreams in bulk in Zendesk WFM](https://support.zendesk.com/hc/en-us/articles/9822760145818).

When selecting workstream conditions, keep in mind that **Meet ALL of the following conditions** uses the *and* operator. This means that each condition in this section must be true for a ticket for the workstream to identify it. Conditions in the **Meet ANY of the following conditions** use the *or* operator. This means that at least one condition in this section must be true for a ticket to be calculated in the workstream.

**Workstream conditions logic**

| | | |
| --- | --- | --- |
| **Condition** | **Logic** | **Behavior** |
| **Meet ALL of the following conditions** | include | All specified values must be present. |
| don’t include | All specified values must be absent. |
| **Meet ANY of the following conditions** | include | At least one specified value must be present. |
| don’t include | At least one specified value must be absent. |

When a ticket doesn't meet the conditions of any workstreams, it’s labeled [No Workstream](workforce-management-glossary.md#NoWorkstreams) in black under your [Agent Activity](https://support.zendesk.com/hc/en-us/articles/6443347506970). The *No Workstream* status is also displayed in the [Agent Status](https://support.zendesk.com/hc/en-us/articles/6443331637018) and in your [Reports](https://support.zendesk.com/hc/en-us/articles/6443331692698).

If a ticket meets the conditions for two or more workstreams simultaneously it’s labeled [Multiple Workstreams](workforce-management-glossary.md#MultipleWorkstreams).

To troubleshoot issues with tickets marked as No Workstream that you believe meet a workstream condition, see [Why do I see some agent activity entries in black?](https://support.zendesk.com/hc/en-us/articles/6947927377818).

**To create workstreams**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **Organization structure**.
2. Click **Workstreams**.
3. Cick the plus sign (**+**) icon, then select **Workstream**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_org_structure_workstream_create.png)
4. Enter a **Workstream name**.
5. (Optional) Describe the purpose of the workstream.
6. Choose a color for the workstream or add a custom color by clicking the palette icon.
   The color you select is used in the forecast visualization.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_org_structure_workstreams_define_new.png)
7. Click the **Conditions** tab.
8. Choose a **Contact via** type.

   For example, tickets, chat or voice. You can define by type with more granularity for tickets and voice channels.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_workstreams_define_type.png)
9. Select additional conditions by choosing a specific group, tag, brand, or form that you use in Zendesk.
10. Click **Preview** to verify the conditions and that the workstream will show you the expected values.
11. Click the **Agents** tab and select which agents to assign to the workstream. You can filter the agents list by group, team, and location.

    Tip: Choose the team members that have the skill to perform the type of work you're specifying for the workstream. This doesn't affect the forecast calculations, but is used with the [automated schedule](https://support.zendesk.com/hc/en-us/articles/6443348256794).
12. Click **Save**.

## Editing workstreams

When you edit a workstream and change its conditions, the updates are visible on the ticket tracking only after a user updates the ticket.

**To edit a workstream**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **Organization structure**.
2. Click **Workstreams**.
3. Select the workstream you want to edit.
4. Make any changes, then click **Save**.

## Deleting workstreams

When you delete a workstream, your existing schedules that include the workstream are affected.

Note: Deleting a workstream is permanent and can't be undone.

**To delete a workstream**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **Organization structure**.
2. Click **Workstreams**.
3. Select the workstream you want to edit.
4. Click **Actions**, then select **Delete**.
5. Click **Delete workstream** to confirm. This action can't be undone.

## Creating combined workstreams (EAP)

Note: Combined workstreams are currently in an Early Access Program (EAP).
You can [sign up for the EAP here](https://docs.google.com/forms/d/e/1FAIpQLSeVCemGsDZCh084u_C7EVdw5qoI1eRfFXyOLJuw80fpmV6qIQ/viewform).

Combined workstreams allow admins and users with permission to schedule multiple workstreams at the same time and ensure [adherence](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_xwv_3n4_52c__in_adherence_time) is properly tracked, regardless of which workstream the agent is working in.

When generating schedules, the algorithm decides whether it's best to schedule a user for a single workstream or a combined workstream for that specific period to ensure the most efficient resource allocation.

You can also control how combined workstreams are used when generating schedules using the Scheduling settings. When the [Schedule combined workstreams option is activated](#topic_qbx_1tz_11c__activate_schedule_combined), the scheduling algorithm uses only combined workstreams when creating a schedule. It will consider any individual workstreams that are not part of any combined workstream afterwards.

General tasks and workstreams defined in your intraday variants are still scheduled as defined in your [location shifts](https://support.zendesk.com/hc/en-us/articles/6443345205402).

**To create combined workstreams**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **Organization structure**.
2. Click **Workstreams**.
3. Click the plus sign (**+**) icon, then select **Combined workstream.**
4. Enter a name for the combined workstream.
5. Select the **Workstreams** you want to combine.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_workstreams_combo_create.png)
6. (Optional) Describe the purpose of the combined workstream.
7. Choose a color for the workstream or add a custom color by clicking the palette icon.
   The color you select is used in the forecast visualization.
8. Click **Save**.

   The algorithm will now decide whether it’s best to schedule a user for a single workstream or a combined workstream.

   You can identify combined workstreams in the All workstreams panel by their icons.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_workstreams_sidebar_combo_icon.png)

To use only combined workstreams [activate the Schedule combined workstreams setting](#topic_qbx_1tz_11c__activate_schedule_combined). Instead of the default behavior where the algorithm decides whether it’s best to schedule a user for a single workstream or a combined workstream when creating a schedule, it will consider only combined workstreams and any individual workstreams that aren't part of any combined workstream afterward.

**To activate the Schedule combined workstreams setting**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **Organization structure**.
2. Click **Workstreams**.
3. Click the **Scheduling settings** icon ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_settings.png) next to All workstreams.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_scheduling+settings.png)
4. Select **Schedule combined workstreams**.
5. Click **Save**.

   The scheduling algorithm starts using only combined workstreams when creating a schedule. It will consider any individual workstreams that are not part of any combined workstream afterwards. Existing schedules are not affected by these changes.

## Prioritizing workstreams (EAP)

Note: Workstream prioritization is currently in an Early Access Program (EAP). You can [sign up for the EAP here](https://docs.google.com/forms/d/e/1FAIpQLSec7J9g91jmtJNtVKtRQKo2a5XA6ajQ68FSUWwEO4T3XU16sA/viewform).

You can prioritize your workstreams from highest to lowest. Prioritize workstreams whose channels or nature of work are most important to your business. For example, you may want to prioritize your Voice workstream first since phone calls can't wait like emails.

The algorithm will still schedule all workstreams based primarily on the forecast; however, priority adds a "bonus point" for a workstream to be selected by the algorithm.

Setting the priority matters only when the forecasted demand is similar between two workstreams or when the demand is fulfilled or really small. In these cases, priority helps in the decision making to schedule the higher priority workstream first until their forecasted demand is covered. Your other workstreams are then scheduled in sequence based on their priority level. However, if the lowest priority workstream has highest demand, it still gets scheduled before other workstreams.

**To prioritize workstreams**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **Organization structure**.
2. Click **Workstreams**.
3. Click the **Scheduling settings** icon ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_settings.png) next to All workstreams.
4. Select **Custom workstream priority**.
5. Click the dropdown menu next to a workstream and select a priority level.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/wfm_combined_workstreams.png)
6. Continue to set the priority for all of your workstreams, then click **Save**.
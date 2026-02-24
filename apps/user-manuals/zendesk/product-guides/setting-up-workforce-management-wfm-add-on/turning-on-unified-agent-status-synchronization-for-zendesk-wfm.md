# Turning on unified agent status synchronization for Zendesk WFM

Source: https://support.zendesk.com/hc/en-us/articles/10114746509978-Turning-on-unified-agent-status-synchronization-for-Zendesk-WFM

---

Unified agent statusesare part ofomnichannel routingand allows agents to control availability for email, voice, and messaging from a single menu in the Agent Workspace. With Zendesk Workforce Management (WFM) unified agent status synchronization, WFM synchronizes agent statuses and activity data directly from Zendesk’s omnichannel routing.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Enable unified agent status synchronization for Workforce Management to streamline agent availability across channels. This feature maps agent statuses to workstreams, enhancing real-time accuracy in adherence, utilization, and reporting. It replaces general tasks with unified statuses for better tracking and insights. Admins or those with permissions can easily activate or deactivate this synchronization to suit operational needs.

[Unified agent statuses](https://support.zendesk.com/hc/en-us/articles/5133523363226) are part of [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514) and allows agents to control availability for email, voice, and messaging from a single menu in the Agent Workspace. With Zendesk Workforce Management (WFM) unified agent status synchronization, WFM synchronizes agent statuses and activity data directly from Zendesk’s omnichannel routing.

Unified agent status synchronization with WFM allows admins and [users in custom roles with permissions](https://support.zendesk.com/hc/en-us/articles/6443314455834) to map agent statuses to specific workstreams. This eliminates the need for agents to update their availability in two systems and improves real-time accuracy in adherence, utilization, and reporting. You can calculate adherence and track activities using agent statuses configured in omnichannel routing instead of [general tasks](https://support.zendesk.com/hc/en-us/articles/7069811858586).

This article contains the following topics:

- [Considerations for turning on unified agent status synchronization for Zendesk WFM](#topic_kcp_yv1_cbc)
- [Turning on unified agent status synchronization for Zendesk WFM](#topic_u4m_l52_whc)
- [Turning off unified agent status synchronization for Zendesk WFM](#topic_egl_w52_whc)

Related articles

- [Mapping unified agent statuses in WFM](https://support.zendesk.com/hc/en-us/articles/10117789027610)
- [About unified agent statuses](https://support.zendesk.com/hc/en-us/articles/5133523363226)

## Considerations for turning on unified agent statuses synchronization for Zendesk WFM

Make sure you understand how synchronizing unified agent statuses with Zendesk WFM affects WFM features and metric calculations.

Specifically, when unified agent statuses are synchronized with WFM:

- Instead of [using the WFM time tracker](https://support.zendesk.com/hc/en-us/articles/6443354661402) agents should [set their unified agent statuses](https://support.zendesk.com/hc/en-us/articles/4410545721114#topic_xvw_ytp_m5b) in the Agent Workspace. At the end of their shift, they should log out of Zendesk Support or close their computer, unless an [end day automation](https://support.zendesk.com/hc/en-us/articles/6443374423066) is in place.

 When agents start working on a ticket, Zendesk WFM automatically starts tracking their time and attendance. However, if their day starts with a status that does not include working on tickets, they must still manually start their day by clicking **Start day** [using the WFM time tracker](https://support.zendesk.com/hc/en-us/articles/6443354661402).
- [General tasks](https://support.zendesk.com/hc/en-us/articles/7069811858586) become unavailable in WFM. However, historical general task data remains available.
- Instead of general tasks, WFM uses unified agent statuses for [adherence and occupancy calculations](https://support.zendesk.com/hc/en-us/articles/6443376913818), [real-time dashboards](https://support.zendesk.com/hc/en-us/articles/10115130172826), [agent activity reporting](https://support.zendesk.com/hc/en-us/articles/6443347506970#topic_css_zf5_ngc), and [public API](https://developer.zendesk.com/api-reference/wfm/introduction/) data streams. Adherence and occupancy data refreshes automatically every few minutes in near real time.
- You’ll need to update your [schedule](https://support.zendesk.com/hc/en-us/articles/6443365957274) and [shift settings](https://support.zendesk.com/hc/en-us/articles/6443345205402) to replace general tasks with unified agent statuses. If necessary, republish your schedule.
- When using unified agent statuses, adherence is calculated as:

 `scheduled activity vs. agent’s unified status + ticket activity`

 - [**In adherence**](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_xwv_3n4_52c__in_adherence_time): An agent is considered in adherence when their active unified agent status is mapped to a workstream they are scheduled to work on. For example, if an agent is scheduled for Workstream A and is either working on a Workstream A ticket or in a status mapped to Workstream A, the agent is considered in adherence. The agent is also considered in adherence if the agent is online but not working (idle time).
 - [**Out of adherence**](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_xwv_3n4_52c__out_of_adherence): If the agent is in a status not mapped to their scheduled workstream or working on the wrong ticket, the agent is considered out of adherence. The “Offline – sign out” status is also excluded from adherence.
- [Adherence rate](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_xwv_3n4_52c__adherence_rate) percentage is calculated as:

 `ratio of time in mapped activities vs. scheduled time`
- [Occupancy percentage](https://support.zendesk.com/hc/en-us/articles/6443376913818-WFM#topic_xwv_3n4_52c__occupancy_rate_ocr) is calculated as:

 `time spent in productive unified agent statuses / total paid time`
- [Utilization percentage](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_xwv_3n4_52c__utilization_ocr) is calculated as:

 `productive time / (total paid + idle time)`
- [Idle time](https://support.zendesk.com/hc/en-us/articles/5286614817562#topic_wwb_5l1_cwb) replaces [untracked time](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_xwv_3n4_52c__untracked_time). Idle time is the period when an agent is not working on a ticket while in a status of online, away, transfer only, or a [custom unified status](https://support.zendesk.com/hc/en-us/articles/4410525357594) using one of those three [standard statuses](https://support.zendesk.com/hc/en-us/articles/5133523363226#topic_vrd_ld1_4vb).
- The [Agent status page](https://support.zendesk.com/hc/en-us/articles/6443331637018) provides real-time visibility of who is online, offline, and idle. Data refreshes every 10 seconds, giving supervisors near real-time insights into:
 - Who is currently online or offline
 - Which workstream each agent is working on
 - How long agents remain in each status or activity
 - Whether they are adhering to their scheduled workstreams
- The [Agent activity page](https://support.zendesk.com/hc/en-us/articles/6443347506970) provides detailed, intraday visibility of what agents worked on and when.
- Only the following [automations](https://support.zendesk.com/hc/en-us/articles/6443314435610) are available when WFM is using unified agent statuses:
 - **Send Message**: Send in-app or Slack notifications to agents or supervisors.
 - **End Day automation**: Automatically end the agent’s day after a defined period of inactivity.
- Task creation, status switching, or time-tracking automations are not available under the unified agent status with Zendesk WFM synchronization. If needed, [create new WFM automations](https://support.zendesk.com/hc/en-us/articles/6443374423066) that use unified agent status data.
- If you use the [Zendesk time tracker Chrome extension](https://support.zendesk.com/hc/en-us/articles/6676772528026) to map external URLs to general tasks, you'll need to remap them to unified agent statuses.

## Turning on unified agent status synchronization for Zendesk WFM

When configured to synchronize unified agent status data, WFM exclusively uses that data instead of general tasks.

You must be an admin or have a [custom role with permission](https://support.zendesk.com/hc/en-us/articles/6443314455834) to activate unified agent status synchronization for Zendesk WFM.

**To turn on unified agent status synchronization for Zendesk WFM**

1. If you haven’t already, [set up and configure omnichannel routing in Admin Center](https://support.zendesk.com/hc/en-us/articles/5866925319962).
2. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **Account settings**.
3. On the **General** tab, scroll to Unified agent status synchronization and select **Agent status synchronization**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_unified_agent_status.png)
4. Click **Save**.
5. In the confirmation dialog, review and confirm that you understand the [main impacts of turning on the unified agent status synchronization with Zendesk WFM and your required actions](#topic_kcp_yv1_cbc).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_turn_on_unified_sync.png)
6. Click **Save and turn on**.

   Your changes are saved and may take up to five minutes to become visible.
7. [Map your WFM workstreams to unified agent statuses](https://support.zendesk.com/hc/en-us/articles/10117789027610) for adherence.

## Turning off unified agent status synchronization for Zendesk WFM

When unified agent status synchronization is turned off, WFM reverts to exclusively using general tasks data. Historical unified agent status data remains visible, but is not used for new activities.

[Untracked time](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_xwv_3n4_52c__untracked_time) replaces [idle time](https://support.zendesk.com/hc/en-us/articles/5286614817562#topic_wwb_5l1_cwb), and general tasks data is used for [adherence and occupancy calculations](https://support.zendesk.com/hc/en-us/articles/6443376913818), [real-time dashboards](https://support.zendesk.com/hc/en-us/articles/10115130172826), [agent activity reporting](https://support.zendesk.com/hc/en-us/articles/6443347506970), and [public API](https://developer.zendesk.com/api-reference/wfm/introduction/) data streams.

You must be an admin or have a [custom role with permission](https://support.zendesk.com/hc/en-us/articles/6443314455834) to turn off unified agent status synchronization for Zendesk WFM.

**To turn off unified agent status synchronization for Zendesk WFM**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **Account settings**.
2. On the **General** tab, scroll to Unified agent status synchronization,and deselect **Agent status synchronization**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_unified_agent_status.png)
3. Click **Save**.
4. In the confirmation dialog, review and confirm that you understand the main impacts of turning off the unified agent status synchronization for Zendesk WFM and your required actions.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/wfm_turn_off_unified_sync.png)
5. Click **Save and turn off**.

   Your changes are saved and may take up to five minutes to become visible.
6. Verify that your [general tasks](https://support.zendesk.com/hc/en-us/articles/6443329426330) are correctly set up.
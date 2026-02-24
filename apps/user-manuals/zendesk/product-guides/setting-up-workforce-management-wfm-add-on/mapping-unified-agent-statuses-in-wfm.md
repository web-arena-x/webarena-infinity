# Mapping unified agent statuses in WFM

Source: https://support.zendesk.com/hc/en-us/articles/10117789027610-Mapping-unified-agent-statuses-in-WFM

---

Synchronizingunified agent status for Zendesk WFMallows agents to set a single status and admins to calculate adherence and track activities based onunified agent statusdata. This approach simplifies workflows and improves reporting accuracy.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Mapping unified agent statuses in WFM allows you to streamline workflows by connecting workstreams to agent statuses. This setup aids in calculating schedule adherence and tracking activities. You can define statuses as paid or productive time, influencing occupancy rate calculations. Customize statuses for tasks like meetings or breaks to optimize agent time without manual updates, enhancing efficiency and reporting accuracy.

Note: The information in this article applies only when unified agent status synchronization is turned on for WFM. If you aren't using unified agent status data in WFM, see [Setting up general tasks for non-ticketing work](https://support.zendesk.com/hc/en-us/articles/6443329426330).

Synchronizing [unified agent status for Zendesk WFM](https://support.zendesk.com/hc/en-us/articles/10114746509978) allows agents to set a single status and admins to calculate adherence and track activities based on [unified agent status](https://support.zendesk.com/hc/en-us/articles/5133523363226) data. This approach simplifies workflows and improves reporting accuracy.

After turning on synchronization, you must map your WFM workstreams to your unified agent statuses. Connecting workstreams to the status ensures that the workstreams’ activities are also taken into consideration when calculating the agent’s schedule [adherence](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_xwv_3n4_52c__in_adherence_time).

Align with other stakeholders in your organization on which workstreams you want to map to agent statuses.

For example, select the workstreams for meetings or breaks if the agent will be away from Zendesk. Setting the workstreams associated with a status helps you optimize your agents' time by reducing the number of actions they need to perform. They won't need to update their status manually, which improves efficiency.

If necessary, review and [manage](https://support.zendesk.com/hc/en-us/articles/5133588225690) the unified agent statuses available to your agents.

Admins can also define whether the agent status is counted as [paid time](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_xwv_3n4_52c__paid_time) or [productive time](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_xwv_3n4_52c__productive_time).

If the status is counted as paid or productive time, it’s included when calculating the [occupancy rate](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_xwv_3n4_52c__occupancy_rate_ocr).

There are certain scenarios where you’ll want to define a status as productive time. For example, if an agent works on social media management outside of Zendesk, you can create a status for that type of work and track it as productive time.

Note that all productive time statuses are included in paid time.

However, not all unified statuses need to be defined as productive time.
Unproductive time is a standard part of customer support work. Activities and tasks such as attending training or meetings could be considered unproductive but still count as paid time.
While they’re necessary activities, they aren’t the core focus of an agent’s job. You may also want to define a “lunch” status as unpaid time.

****To map unified agent statuses in WFM****

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **Agent statuses mapping**.
2. Under **All statuses**, click the name of the status you want to map to WFM workstreams.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_unified_agent_statuses.png)
3. (Optional) Under **Occupancy settings**, click the **Log this status as paid time** toggle to include the status in paid time when calculating agents’ occupancy rates.
4. (Optional) When logging the status as paid time, click the **Log this status as productive time** toggle to include it as productive time when calculating agents’ occupancy rates.
5. Under **Schedule adherence customization** select the workstreams you want to map to the status.
6. Click **Save**.
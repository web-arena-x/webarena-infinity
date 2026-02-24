# Creating WFM automations to manage agent activity

Source: https://support.zendesk.com/hc/en-us/articles/6443374423066-Creating-WFM-automations-to-manage-agent-activity

---

Zendesk Workforce management (WFM) automations allow you to manage certain agent activities automatically, such as ending agents' days when they forget to clock out. You can create multiple automations in your account to manage and perform actions for different types of agent activity. When you create automations, they can apply to all agents in your account or to only specific agents or teams.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

With Workforce Management automations, you can automatically manage agent activities, like ending shifts when agents forget to clock out. Create automations for various agent activities, applying them to all or specific agents. Set triggers based on clock-in times or schedule adherence, and define actions like sending notifications. Note that having over 50 automations may affect performance.

Zendesk Workforce management (WFM) automations allow you to manage certain agent activities automatically, such as ending agents' days when they forget to clock out. You can create multiple automations in your account to manage and perform actions for different types of agent activity. When you create automations, they can apply to all agents in your account or to only specific agents or teams.

## Creating WFM automations

You must be a WFM admin or [have permission](https://support.zendesk.com/hc/en-us/articles/6443374440090) to create an automation. Make sure you understand how automations work before you start creating them. See [About WFM automations and how they work](https://support.zendesk.com/hc/en-us/articles/6443314435610).

**To create a WFM automation**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_admin_icon.png)
   **Settings** in the navigation bar, then select **Automations**.
2. Click **Create automation**.
3. Enter a unique **Automation name**.
4. Select a **Run event**.

   The default event is **Clocked into**, but it can be changed to **Early to** or **Late to**.

   The Clocked into event means that the automation will run after a specified duration since an agent clocks into a task or workstream.

   The Early and Late to events consider the agent’s adherence to their scheduled start and end times. The Early to event runs on a specified duration before an agent’s scheduled start or end time. The Late to event runs on a specified duration beyond an agent’s scheduled start or end time.
   To learn more, see [Structure of a WFM automation](https://support.zendesk.com/hc/en-us/articles/6443314435610#structure-of-wfm-automations).
5. (Optional) If you selected Clocked into, click the **Tasks** field and choose the [general tasks](https://support.zendesk.com/hc/en-us/articles/7069811858586), [agent statuses](https://support.zendesk.com/hc/en-us/articles/10114746509978), and [workstreams](https://support.zendesk.com/hc/en-us/articles/6443314489242) it applies to, or select **Any task** for all.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_automation_create.png)
6. (Optional) If you selected **Early to** or **Late to**, click the **Condition** field and choose between **End day** or **Start day**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_automation_early_late.png)
7. In the **Duration** field, specify the length of time the agent must be clocked into a task or workstream for the automation to run. The Early to event runs on the specified duration before an agent’s scheduled start or end time.
   The Late to event runs after a specified duration beyond an agent’s scheduled start or end time.
8. Select the **Actions to perform** from the predefined list. To learn more, see [Structure of a WFM automation](https://support.zendesk.com/hc/en-us/articles/6443314435610#structure-of-wfm-automations).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_auto_actions_eap.png)
9. (Optional) If you selected to shift a user to a general task, select the task from the **General task** menu that appears.

   Note: Changes in activity related to [general tasks](https://support.zendesk.com/hc/en-us/articles/6443329426330) run by automations do not affect your [agents' talk states](https://support.zendesk.com/hc/en-us/articles/4408829114138).
10. (Optional) If you select **Send Message**, choose who to send the message to.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_automations_notify_select_users.png)

    The users you select will receive a push notification in their [Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) in Zendesk Support.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_push_notification.png)
11. Click the **Agents** tab, then select which agents the automation applies to.
    You can apply the automation to all agents in your account or specify certain agents.
12. Click **Create automation**.

Note: Currently, there is no set limit on the number of automations that can be created. However, creating more than 50 automations may lead to performance issues.
# Real-time QA insights (EAP)

Source: https://support.zendesk.com/hc/en-us/articles/9745122485914-Real-time-QA-insights-EAP

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

| | |
| --- | --- |
| **Add-on** | Copilot |

Verified AI summary ◀▼

Real-time QA insights use AI to detect critical issues in live ticket conversations, helping you address privacy concerns, vulnerable or abusive customers, churn risks, and unresolved tickets. Insights appear in the Agent Workspace and Agent Home. You can control access with custom roles and automate workflows with triggers based on insights, enhancing your team's ability to resolve issues promptly and maintain service quality.

Real-time QA insights are currently in an early access program (EAP).
You can [sign up for the EAP here](https://docs.google.com/forms/d/e/1FAIpQLSdtyshFkjbV5L9E1avDSSqlm3uhotFMFX-UJA_ZfQBhxRvs2Q/viewform) if you have either the [QA or Copilot add-on](https://support.zendesk.com/hc/en-us/articles/4408834152730).

Real-time QA insights leverage AI to detect predefined concerns in live ticket conversations. For example, real-time QA insights can detect churn risks when users express extreme frustration or dissatisfaction. When insights are identified, potential critical issues are surfaced for your team members, helping them deliver better resolutions, prevent compliance violations, and route tickets to the appropriate groups promptly.

Real-time QA insights appear in the Agent Workspace and Agent Home. Admins can also set up triggers to automate workflows when specific insights are detected.

Getting started with Zendesk QA: Real-time QA (1:53)

This article contains the following topics:

- [Understanding real-time QA insights](#topic_lky_zs2_m2c)
- [Viewing real-time QA insights in the Agent Workspace](#topic_jqy_st2_m2c)
- [Viewing real-time QA insights in Agent Home](#topic_xgq_22y_sgc)
- [Creating or editing custom roles to grant access to QA insights](#topic_whd_x2y_sgc)
- [Creating business rules to leverage QA insights in automated workflows](#topic_xtm_2fy_sgc)

## Understanding real-time QA insights

Real-time QA insights leverage AI to detect predefined concerns in ticket conversations as they happen. These insights include:

- **Privacy**: Detected when a user raises a concern related to data or cybersecurity, such as unsolicited access notifications, suspended security flaws, account compromise, intellectual property violations, and requests related to personal data.

 Identifying privacy concerns in live ticket conversations can help team members identify suspicious activity alerts, flag sharing of confidential information, and prevent data breaches before they occur.
- **Vulnerability**: Detected when a user explicitly mentions experiencing financial distress, physical or mental health challenges, addiction issues, or situations that pose risks to their physical safety or well-being. This insight isn't detected in conversations initiated by an agent or when the initial message is automated or form-generated.

 Identifying users who may be considered vulnerable allows your team members to offer timely support, which can protect your users.
- **Abuse**: Detected when either a user is abusive towards an agent, or when a user reports abusive treatment by staff. Signs of abuse include the use of profanity, name-calling, offensive or disrespectful behaviour, discriminatory remarks, or any form of aggressive or repeated harassment.

 Identifying abusive users can help you address the behavior immediately to ensure a safe workplace for your team.
- **Churn risk**: Detected when a user expresses extreme frustration, disappointment, or dissatisfaction, especially when using capital letters or excessive punctuation. Statements about seeking alternatives or threatening to cancel a subscription, order, or account are also detected as churn risks.

 Identifying churn risks allows you to take immediate action to ensure retention.
- **Unresolved issue**: Detected when a user states they haven't received a solution or satisfactory response, mentions repeated contact with support, or reports that the problem continues to occur.

 Identifying unresolved tickets can help you prioritize unresolved issues to fix problems in a timely manner, prevent escalations, and improve service quality.

### Real-time QA insights EAP limitations

The following limitations apply to real-time QA insights during the EAP:

- Insights and their associated tags can't be edited or removed from tickets.
- Only open tickets are analyzed for QA insights.
- QA insight detection is currently text-only and is not yet available for call transcripts.

## Viewing real-time QA insights in the Agent Workspace

When real-time QA insights are enabled in your account, your open tickets are analyzed by AI on a per-message basis. Messages from end users are checked for all predefined insights, while agent messages are checked only for the "abuse" insight.

Admins and [team members in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can view QA insights in the Agent Workspace. To grant your team members access, see [Creating or editing custom roles to grant access to QA insights](#topic_whd_x2y_sgc).

**To access real-time QA insights in the Agent Workspace**

- In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), navigate to an open ticket with an ongoing conversation.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_realtime_insights_aw_eap.png)

 The insights detected in the ongoing conversation appear in the **QA insights** ticket field in the left panel. Tags associated with the insight appear in the **Tags** ticket field.

## Viewing real-time QA insights in Agent Home

In Agent Home, a QA insights widget displays all key insights surfaced from live, open tickets, giving visibility into critical issues.

Admins and [team members in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can view the QA insight widget in Agent Home. To great your team members access, see [Creating or editing custom roles to grant access to QA insights](#topic_whd_x2y_sgc).

[Agent Home must be activated](https://support.zendesk.com/hc/en-us/articles/9178190742554) in your account to view the QA insights widget.

**To access real-time QA insights in Agent Home**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the Home (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_dashboard.png)) icon in the sidebar.
2. In the **Realtime QA insights** widget on the right, view the number of live tickets with insights detected.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_insights_agent_home.png)

   If no insights are currently detected in your tickets, then the QA insights widget appears empty.
3. Click an insight's ticket count to filter and view all related tickets associated with the insight.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_insights_filter_view.png)

## Creating or editing custom roles to grant access to QA insights

By default, only admins automatically have access to view QA insights in the Agent Workspace and Agent Home. As an admin, you can control which team members have access by creating or editing custom roles with the QA insights permission, then assigning the appropriate team members to the roles.

Configuring access with permission-based roles helps ensure that sensitive insights are visible only to the right team members. For example, you may want to allow only your team leads to view QA insights.

**To create or edit a custom role and grant team members access to QA insights**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Roles**.
2. Click **Create role** to [create a new role](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cxn_hig_bd) or click an existing custom role to edit it.
3. Under **Permissions**, click **View QA insights**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_real_time_insights_permissions.png)

   This permission grants access to view QA insights in the Agent Workspace and Agent Home.
4. Click **Save**.
5. Assign your team members to the role. See [Assigning agents to custom roles](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_cbu_mmg_bd).

## Creating business rules to leverage QA insights in automated workflows

Automate your workflows when specific issues are detected by creating business rules based on QA insights. Since insights are added to tickets as fields and tags, this information can be used in [trigger](https://support.zendesk.com/hc/en-us/articles/4408822236058) and [automation](https://support.zendesk.com/hc/en-us/articles/4408832701850) condition statements.

The example below describes how to create a trigger that changes the priority of a ticket and assigns a specific team member to the ticket when the "vulnerable customer" insight is detected.

**To create a trigger based on QA insights**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click **Create trigger**.
3. Enter a **Trigger name** and select a **Trigger category**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_insights_trigger_name_example.png)
4. Click **Add condition** and enter the following:
   - **Ticket > Status category | Is | New**
   - **Ticket > QA insights | Includes | Vulnerable customer**
   - **Ticket > Agent replies | Less than | 1**

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_insights_trigger_example_conditions.png)
5. Click **Add action** and enter the following:
   - **Ticket > Assignee | Ticket > [Agent name]**
   - **Ticket > Priority | Urgent**

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/qa_insights_trigger_example_actions.png)
6. Click **Create trigger**.
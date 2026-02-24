# Dynamically adapting dashboard data based on viewer

Source: https://support.zendesk.com/hc/en-us/articles/5282695803290-Dynamically-adapting-dashboard-data-based-on-viewer

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

When you [create a dashboard](https://support.zendesk.com/hc/en-us/articles/4408830235930-Working-with-the-dashboard-builder-Beta-#h_01FG7AT96GRH809GXH9Q3F4E1S), you might want certain users to see some of the data without being able to see all of it. While you could create a separate filtered dashboard for each user, it’s much easier to accomplish this goal with dashboard restrictions.

For example, you can create a single dashboard to monitor agent productivity, and then use dashboard restrictions to ensure that each agent can see only their own metrics when they open the dashboard.

This article contains the following topics:

- [Creating a dashboard restriction](#topic_ptw_n3r_3wb)
- [Sharing a restricted dashboard with users](#topic_qdf_q3r_3wb)
- [Viewing a dashboard with a restriction](#topic_ymb_r3r_3wb)
- [List of dynamic attributes](#topic_lgx_r3r_3wb)

## Creating a dashboard restriction

The first step in determining what a dashboard viewer can see is creating a dashboard restriction. A dashboard restriction is a set of rules that determines what data—broken down by dataset, attribute, and attribute value—a user is allowed to view.

Customers on Professional plans can create a maximum of 10 dashboard restrictions. Customers on Enterprise plans can create a maximum of 500.

Tip: You can create a dashboard restriction from the dashboard sharing window too. See [Sharing a restricted dashboard with users](#topic_qdf_q3r_3wb).

**To create a dashboard restriction**

1. Open an existing dashboard for editing (it must have been created using the beta dashboard builder), or [create a new dashboard using the beta dashboard builder](https://support.zendesk.com/hc/en-us/articles/4408830235930-Working-with-the-dashboard-builder-Beta-#h_01FG7AT96GRH809GXH9Q3F4E1S).

   Tip: You can use the **Support agent productivity** template to quickly create a dashboard that’s designed to show a full picture of agent productivity over the last seven days.
2. Click the arrow next to the **Share** button and select **Manage data restrictions**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_dashboard_restrictions_share.png)
3. Click **Create restriction**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_dashboard_restrictions_create.png)
4. In the window that appears, fill out the following fields:
   - **Name**: Give your dashboard restriction a descriptive name.
   - **Dataset**: Select the dataset that you want to restrict data for.
   - **Filter**: Select the attribute that you want to restrict data for. For details, see [List of dynamic attributes](#topic_lgx_r3r_3wb).
   - **Values**: For the filter you selected above, select up to 20 values that will be visible to the dashboard viewer. Search for specific values by typing. For example, if you want the dashboard to show only tickets assigned to a specific agent, you could select a **Filter** of **Assignee name**, and a **Value** of the agent’s name.

     The **Based on viewer** option dynamically restricts a dashboard’s data based on the signed-in user. For example, if you select the **Assignee name** filter and the **Based on viewer** value, the dashboard will show only tickets where the signed-in user is the assignee.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_dashboard_restrictions_details.png)

     Note: Dashboard restrictions that use the **Based on viewer** setting can’t be [shared externally](https://support.zendesk.com/hc/en-us/articles/4408830235930#h_01HEJCJC0JWVEED6KYP8RH30K2).
5. If needed, click **Add filter** and select an additional set of **Dataset**, **Filter**, and **Values**. You can add up to five filters to restrict the dashboard to your desired level.

   You can remove a filter at any time by clicking **Remove filter** underneath the corresponding **Dataset/Filter/Values** set.
6. When you’re done, click **Create dashboard restriction**. The **Dashboard restrictions** window appears, showing you the restriction you just created along with any other restrictions that exist for this dashboard.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_dashboard_restrictions_existing.png)
7. Click **Done**.

Creating a dashboard restriction is the first step in controlling what dashboard viewers can see, but you need to share that dashboard restriction with the applicable users for it to have any effect.

## Sharing a restricted dashboard with users

After you’ve created at least one dashboard restriction, you need to share it with users. Sharing a dashboard restriction with a user invites them to view the restricted version of the dashboard, meaning they’ll be able to see only the data that you defined in the dashboard restriction you created above.

**To share a restricted dashboard with users**

1. Open an existing dashboard for editing (it must have been created using the beta dashboard builder), or [create a new dashboard using the beta dashboard builder](https://support.zendesk.com/hc/en-us/articles/4408830235930-Working-with-the-dashboard-builder-Beta-#h_01FG7AT96GRH809GXH9Q3F4E1S).
2. Click **Share**. The **Invite people** window appears.
3. In the **Add team members or groups** field, select the users you want to share the dashboard with. Search for specific users by typing.
4. In the **Access** field, select the dashboard restriction that defines which data the selected users should be able to see. If you don’t want to apply any dashboard restriction for the selected users, choose **All data**. The **People with access** pane shows you which users can already see the dashboard.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_dashboard_restrictions_invite.png)

   Tip: If none of the existing dashboard restrictions meet your needs, you can create a new one from this dropdown by clicking **Create dashboard restriction**.
5. (Optional) Clear the **Send email notification** checkbox if you don’t want to send an email notification to the invited users to view the dashboard. If you don’t send an email, users can still find the dashboard in the report library or by going to the dashboard’s URL.
6. Click **Invite people**.

## Viewing a dashboard with a restriction

When a user opens a dashboard that was created with the beta dashboard builder, they can see the name of the dashboard and the currently applied dashboard restriction at the top.

Users with access to multiple dashboard restrictions (like admins) can switch between the different restrictions, changing the data shown in the dashboard. Users with access to only a single restriction cannot change the selection.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_dashboard_restrictions_available_views.png)

**To view a dashboard with a restriction**

1. Open a dashboard that was created using the beta dashboard builder.
2. If you have access, select the dropdown next to the dashboard’s name to switch between different dashboard restrictions.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_dashboard_restriction_view.png)

## List of dynamic attributes

You can create a dashboard restriction with any historical dataset or attribute. However, the attributes listed in the table below are the only ones that dynamically change the dashboard’s data based on the viewer.

You cannot create dashboard restrictions for live data.

| Dataset | Corresponding attributes |
| --- | --- |
| Support - Tickets | - Ticket group - Ticket brand - Assignee name - Assignee ID - Assignee email - Assignee locale - Requester name - Requester ID - Requester email - Requester locale - Submitter name - Submitter ID - Submitter email - Submitter locale - Ticket organization name - Requester organization name - Ticket organization name - Unsorted - Requester organization name - Unsorted |
| Support - Updates history | - Update ticket group - Update ticket assignee - Update ticket assignee ID - Update ticket brand - Previous ticket group - Previous ticket brand - Previous ticket assignee - Previous ticket assignee ID - Ticket group - Ticket brand - Assignee name - Assignee ID - Assignee email - Assignee locale - Requester name - Requester ID - Requester email - Requester locale - Submitter name - Submitter ID - Submitter email - Submitter locale - Updater name - Updater agent name - Updater ID - Updater email - Updater locale - Ticket organization name - Requester organization name - Updater organization name - Ticket organization name - Unsorted - Requester organization name - Unsorted - Updater organization name - Unsorted |
| Support - SLAs | - Ticket group - Ticket brand - Assignee name - Assignee ID - Assignee email - Assignee locale - Requester name - Requester ID - Requester email - Requester locale - Submitter name - Submitter ID - Submitter email - Submitter locale - Ticket organization name - Requester organization name - Ticket organization name - Unsorted - Requester organization name - Unsorted |
| Support - Backlog history | - Group name - Assignee name - Brand |
| Voice - Calls | - Ticket group - Ticket brand - Ticket assignee - Ticket requester - Ticket organization - Call group - Call agent name - Call agent ID - Call agent email - Call agent locale - Leg agent name - Leg agent ID - Leg agent email - Leg agent locale - End-user name - End-user ID - End-user email - End-user locale - Organization name - Ticket organization - Unsorted - Organization name - Unsorted |
| Chat - Engagement | - Ticket group - Ticket brand - Ticket assignee - Ticket requester - Ticket organization - Agent name - Agent ID - Agent email - Agent locale - Ticket organization name - Unsorted |
| Chat - Messaging tickets | - Ticket group - Ticket brand - Assignee name - Assignee ID - Assignee email - Requester name - Requester ID - Requester email - Ticket organization name - Ticket organization name - Unsorted |
| Chat - Chat concurrency | - Agent name - Agent ID - Agent email - Agent locale |
| Chat - Messaging goal conversions | - Ticket group - Ticket brand - Ticket organization - Assignee name - Assignee ID - Assignee email - Requester name - Requester ID - Requester email - Ticket organization - Unsorted |
| Knowledge - Quick answers | - Search brand name - User name - User ID - User email |
| AI - Copilot suggestions | - Ticket group - Ticket brand - Ticket assignee - Ticket requester - Ticket organization - Agent name - Agent ID - Agent email - Agent locale - Ticket organization - Unsorted |
| AI - Copilot auto assist | - Ticket group - Ticket brand - Ticket assignee - Ticket requester - Ticket organization - Agent name - Agent ID - Agent email - Agent locale - Ticket organization - Unsorted |
| AI - Intelligent triage | - Ticket group - Ticket brand - Ticket assignee - Ticket requester - Ticket organization - Ticket organization - Unsorted |
| AI - Generative AI tools | - Ticket group - Ticket brand - Ticket assignee - Ticket requester - Ticket organization - Agent name - Agent ID - Agent email - Agent locale - Ticket organization - Unsorted |
| Omnichannel - Engagements | - Group name - Agent name - Agent ID - Agent email - Agent locale |
| Omnichannel - Custom queues | - Group name |
| Omnichannel - Agent state daily | - Group name - Agent name - Agent ID - Agent email - Agent locale |
| Omnichannel - Agent state | - Group name - Agent name - Agent ID - Agent email - Agent locale |
| Omnichannel - Agent productivity | - Group name - Agent name - Agent ID - Agent email - Agent locale |
| AI agents - Flow builder | - Brand |
| AI agents - Article recommendations (legacy) | - Answer brand - Ticket group - Ticket brand - Ticket assignee - Ticket requester - Ticket organization - User name - User ID - User email - User locale - Ticket organization - Unsorted |
| AI agents - Essential | - Conversation brand |
| Knowledge - Page efficiency | - Page brand - Page author name - Page author ID - Article author name - Article author ID |
| Knowledge - User session | - Session brand - Visitor name - Visitor ID - Visitor email |
| Knowledge - Community | - Brand name - Author name - Author ID |
| Knowledge - Search | - Search brand name |
| Knowledge - Team publishing | - Event article brand - Agent name - Agent ID - Agent email - Agent locale |
| Knowledge - Knowledge capture | - Knowledge Capture brand - Ticket group - Ticket brand - Ticket assignee - Ticket requester - Ticket organization - Agent name - Agent ID - Agent email - Agent locale - User name - User ID - User email - User locale - Ticket organization - Unsorted |
| Knowledge - Knowledge base | - Author name - Engagement brand - Article brand |
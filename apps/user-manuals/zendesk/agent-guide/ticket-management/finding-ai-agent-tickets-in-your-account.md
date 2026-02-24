# Finding AI agent tickets in your account

Source: https://support.zendesk.com/hc/en-us/articles/9966620612634-Finding-AI-agent-tickets-in-your-account

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

AI agent tickets are tickets for messaging conversations that were handled entirely by your [AI agent](https://support.zendesk.com/hc/en-us/articles/6970583409690) or [basic messaging response](../../product-guides/zendesk-messaging/configuring-messaging-responses-and-business-hours.md), meaning they haven’t yet been or never were escalated to a human agent. Agents and admins can view AI agent tickets in the Agent Workspace.

To prevent disruption, AI agent tickets aren’t included by default in lists, views, or searches that already existed when the [AI agents feature was turned on](https://support.zendesk.com/hc/en-us/articles/9204149016346#topic_myq_2r1_2gc). However, you can update existing lists, views, and searches (or create new ones) to include AI agent tickets as desired.

This article contains the following topics:

- [Searching for AI agent tickets in Agent Workspace](#topic_t4h_vt1_2gc)
- [Filtering views for AI agent tickets](#topic_ym4_151_2gc)
- [Creating or editing views to show AI agent tickets](#topic_tb2_zt1_2gc)
- [Searching for AI agent tickets in Support](#topic_anv_xt1_2gc)

Related article:

- [Understanding and viewing AI agent tickets for AI agent–only conversations](https://support.zendesk.com/hc/en-us/articles/9204149016346)

## Searching for AI agent tickets in Agent Workspace

From within Agent Workspace, you can search for tickets and narrow your results so that you see only AI agent tickets.

**To search for AI agent tickets in Agent Workspace**

1. [Perform an advanced search.](https://support.zendesk.com/hc/en-us/articles/4408835086106)
2. Select the **Tickets** filter.
3. Select **Support type**.
4. Select **AI agent**.

   Your search results are filtered to AI agent tickets only.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_ai_agent_tickets_searching_AW.png)

## Filtering views for AI agent tickets

You can filter the results of an existing view to show regular tickets and AI agent tickets, or AI agent tickets only. This works only if the view has been [created or updated to include AI agent tickets](#topic_tb2_zt1_2gc).

**To filter a view for AI agent tickets**

1. [Open a view.](https://support.zendesk.com/hc/en-us/articles/4408829483930#topic_1nl_ftm_vt)
2. Click **Filter**.
3. In **Support type**, select one of the following options:
   - **All** to show regular tickets and AI agent tickets.
   - **AI agent** to show AI agent tickets only.
4. Click **Apply filters**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_ai_agent_tickets_filtering_view.png)

## Creating or editing views to show AI agent tickets

You can create or edit views to include regular tickets and AI agent tickets, or AI agent tickets only. By default, views created before you [turned on the AI agent tickets feature](https://support.zendesk.com/hc/en-us/articles/9204149016346#topic_myq_2r1_2gc) do not include AI agent tickets.

Note: To prevent AI agent tickets from appearing in existing views by default, views created before this feature was rolled out to your account were automatically updated to include a condition of **Ticket** >
**Support type** | **Is** | **Agent**.

**To create or edit a view to show AI agent tickets**

1. [Create a new view](https://support.zendesk.com/hc/en-us/articles/4408888828570) or [edit an existing view](https://support.zendesk.com/hc/en-us/articles/4408832792986#topic_fzx_qyj_5b).
2. Under **Meet ALL of the following conditions**, add the following condition based on what you want your view to show:
   - For regular tickets and AI agent tickets: **Ticket > Support type** | **Is** | **All**
   - For AI agent tickets only: **Ticket > Support type** | **Is**
     | **AI agent**

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_ai_agent_tickets_creating_view.png)

## Searching for AI agent tickets in Support

On the Search page in Support, you can search for tickets and narrow your results so that you see only AI agent tickets.

**To search for AI agent tickets in Support**

1. [Perform a search.](https://support.zendesk.com/hc/en-us/articles/4408894221594#topic_htl_zbm_wf)
2. On the search results page, click **Filters**.
3. In **Support type**, select **AI agent**.

   Your search results are filtered to AI agent tickets only.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_ai_agent_tickets_searching_support.png)
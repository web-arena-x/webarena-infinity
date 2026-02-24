# Creating views for automatically triaged tickets

Source: https://support.zendesk.com/hc/en-us/articles/4662504732954-Creating-views-for-automatically-triaged-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Copilot |

If you [use intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538), you can create views
that take advantage of the intent, language, and sentiment values that are automatically
assigned to tickets.

For example, you might want to create a view for a specific type of intent,
such as billing, which you could then assign to your accounting or finance group. Or,
you might want to create separate views for different languages, which you could then
assign to groups of agents dedicated to specific language support. You could even create
a view for tickets where the requesters are particularly upset, sending those tickets to
a team trained to handle delicate situations.

This approach is typically most helpful for small organizations with relatively
few agents. For larger organizations with many agents, we recommend using omnichannel
routing, standalone skills-based routing, or triggers to route tickets based on
intelligent triage predictions. See [Choosing a routing method for automatically triaged
tickets](https://support.zendesk.com/hc/en-us/articles/4973607684506).

Views can also be used by supervisors and team leaders to see the health of
their teams’ ticket queues.

This article walks you through examples of how to set up views for intelligent
triage intents, languages, and sentiments, but feel free to customize the views however
makes sense for your business. For more information on creating views, see [Creating views to manage ticket workflow](https://support.zendesk.com/hc/en-us/articles/4408888828570).

This article contains the following topics:

- [Creating a view for all
  intents](#topic_yth_bz3_5tb)
- [Creating views for a specific
  intent](#topic_hfh_cz3_5tb)
- [Creating views for a specific
  language](#topic_ncj_dz3_5tb)
- [Creating views for specific sentiments](#topic_xgl_whh_hwb)

Note: When creating views in Admin Center, intelligent triage
prediction values are available only in English. However, intelligent triage is
capable of evaluating content in the languages listed [here](https://support.zendesk.com/hc/en-us/articles/4408821324826#h_01GYJ1PBVKD26QN3E8JNS3X3TX).

## Creating a view for all intents

You can create a view to show all of the tickets that intelligent triage
has assigned an intent to. This helps you get an at-a-glance view of what your
tickets are about.

**To create a view grouped by intent**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Views**.
2. Click **Add view**.
3. At the top of the page, enter a name for the view (such as **Tickets by
   intent**).
4. Enter a **Description** for your view.
5. Under **Tickets must meet all of these conditions to appear in the
   view**, add the condition:

   **Status** | **Less than** |
   **Solved**
6. Under **Formatting options**, choose the **Columns** you want to add
   to your view. It can be helpful to add **Intent** and **Language**.
7. Under **Group by**, select **Intent**, and then select
   **Descending**.
8. Under **Order by**, select the ticket field you want to order your view
   by (within each group), and the direction of the sort.
9. Click **Save**.

You now have a view that shows you all non-closed tickets grouped by intent.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_ml_automated_triage_view_all_intents.png)

## Creating views for a specific intent

You can create a view for a specific intent, like refund requests, and then assign
that view to the group of agents that are dedicated to that specialty.

A view like this also gives supervisors a quick way to see how tickets with a certain
intent (for example, frequent or sensitive topics) are being handled by their
teams.

**To create a view for a specific intent**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Views**.
2. Click **Add view**.
3. At the top of the page, enter a name for the view (such as **Unassigned
   refund request tickets**).
4. Enter a **Description** for your view.
5. (Optional) In the **Who has access** dropdown, select **Agents in
   specific groups**. In the **Choose which groups have access**
   dropdown, select the group responsible for refund requests.
6. Under **Tickets must meet all of these conditions to appear in the
   view**, add the following conditions:
   - **Assignee** | **Is** | **-**
   - **Status** | **Less than** | **Solved**
   - **Intent | Is | Billing::Refund::Refund request**

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_ml_automated_triage_view_specific_intent.png)

     If you’re creating a view with multiple intents, it’s
     easier to build a condition using **Tags** instead of
     **Intent**. For example, your third condition might look
     like this instead:

     **Tags** | **Contain at least one
     of the following** | *all tags that start with
     “intent\_\_billing”*
7. Under **Formatting options**, choose the **Columns** you want to add
   to your view. It can be helpful to add **Intent** and
   **Language**.
8. Under **Group by**, select the ticket field you want to group your view
   by, and the direction of the sort.
9. Under **Order by**, select the ticket field you want to order your view
   by, and the direction of the sort.
10. Click **Save**.

You now have a view that shows you all unassigned tickets that intelligent triage
determined to be refund requests. Your billing team can use this view to work new
tickets from customers who need help with refunds.

## Creating views for a specific language

You can create a view for a specific language, like Spanish, and then
assign that view to the group of agents who are trained to handle requests in that
language.

A view like this also gives supervisors a quick way to see how tickets for a certain
language are being handled by their teams.

**To create a view for a specific language**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Views**.
2. Click **Add view**.
3. At the top of the page, enter a name for the view (such as **Unassigned
   tickets for Spanish support**).
4. Enter a **Description** for your view.
5. (Optional) In the **Who has access** dropdown, select **Agents in
   specific groups**. In the **Choose which groups have access**
   dropdown, select the group responsible for Spanish-speaking support.
6. Under **Tickets must meet all of these conditions to appear in the
   view**, add the following conditions:
   - **Assignee** | **Is** | **-**
   - **Status** | **Less than** | **Solved**
   - **Language** | **Is** | **Spanish; Castilian**

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_ml_automated_triage_view_specific_language.png)
7. Under **Formatting options**, choose the **Columns** you want to add
   to your view. It can be helpful to add **Intent**.
8. Under **Group by**, select the ticket field you want to group your view
   by, and the direction of the sort.
9. Under **Order by**, select the ticket field you want to order your view
   by, and the direction of the sort.
10. Click **Save**.

You now have a view that shows you all unassigned tickets where the requester speaks
Spanish. Your Spanish-speaking support team can use this view to work new
tickets.

## Creating views for specific sentiments

You can create views for tickets based on specific sentiments (Negative and Very
negative, for example) for specially trained customer service teams.

A view like this also gives supervisors a quick way to see how tickets with specific
sentiments (especially unhappy customers) are being handled by their teams.

**To create a view for a specific sentiment**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Views**.
2. Click **Add view**.
3. At the top of the page, enter a name for the view (such as **Tickets with
   negative sentiment**).
4. Enter a **Description** for your view.
5. (Optional) In the **Who has access** dropdown, select **Agents in
   specific groups**. In the **Choose which groups have access**
   dropdown, select the group responsible for handling delicate
   situations.
6. Under **Tickets must meet all of these conditions to appear in the
   view**, add the following conditions:
   - **Assignee** | **Is** | **-**
   - **Status** | **Less than** | **Solved**
7. Under **Tickets can meet any of these conditions to appear in the view**,
   add the following conditions:
   - **Sentiment** | **Is** | **Negative**
   - **Sentiment** | **Is** | **Very negative**

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ml_intelligent_triage_views_sentiment.png)
8. Under **Formatting options**, choose the **Columns** you want to add
   to your view. It can be helpful to add **Intent**.
9. Under **Group by**, select the ticket field you want to group your view
   by, and the direction of the sort.
10. Under **Order by**, select the ticket field you want to order your view
    by, and the direction of the sort.
11. Click **Save**.

You now have a view that shows you all tickets where intelligent triage predicted the
customer sentiment was Negative or Very negative. Your customer service team can use
this view to work new tickets where careful communication may be required.
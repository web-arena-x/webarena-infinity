# Using standalone skills-based routing

Source: https://support.zendesk.com/hc/en-us/articles/4408883700122-Using-standalone-skills-based-routing

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

Skills-based routing enables admins to set up skills, which are attributes associated with individual agents and sets of ticket conditions. This article describes setting up skills based routing as a standalone solution.

This article contains the following topics:

- [About skills-based views](#topic_ygf_twf_2nb)
- [Creating views with skills-based conditions (recommended)](#topic_ifc_vwf_2nb)
- [Creating a skills-match view](#topic_cnx_pwf_2nb)
- [Converting an existing skills-match view](#topic_ldb_2dg_2nb)
- [Validating your skills-based views](#topic_hmr_lnv_vxb)

## Preparing to use standalone skills-based routing

The first several steps for setting up skills-based routing are the same whether you're using it as a standalone solution or as part of [omnichannel routing](https://support.zendesk.com/hc/en-us/articles/4409149119514).

- [Plan out your skills](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_x5d_cvs_5xb).
- [Create skills](https://support.zendesk.com/hc/en-us/articles/4408838892826).
- [Assign them to agents](https://support.zendesk.com/hc/en-us/articles/4408838892826#topic_w3m_th2_bbb).
- [Configure an automated way to assign skills to tickets](https://support.zendesk.com/hc/en-us/articles/5833458075930).

The last step for setting up skills based routing as a standalone solution is creating a single (or small number of) of views for agents to work from. A single broadly-defined view can be configured to show different matching tickets depending on who’s looking at it, but in some cases you may find it best to use more than one view.

## About skills-based views

A skills-based view is a view that displays only tickets with skill requirements that match the skills of the agent using the view. There are currently two types of skills-based views in Support:

- [Views with a skills-based condition (recommended)](#topic_uvt_tmw_vxb)
- [Skills-match views](#topic_u5x_5mw_vxb)

### Views with a skills-based condition (recommended)

You can create a skills-based view by adding a skills-based condition to a view. You can do this to as many views as you want. For more information, see [Creating views with skills-based conditions](#topic_ifc_vwf_2nb).

We recommend using this type of skills-based view because it offers several advantages compared to skills-match views. For example:

- You can filter all views by skills instead of just one.
- There’s no limit on the number of tickets assessed.
- There’s no limit on the number of tickets displayed in the view.
- The results of the view are paginated.

However, there are a few limitations to these views to consider:

- Closed tickets are not included in views with skills-based conditions.
- Tickets with no skills are excluded from the view.

### Skills-match views

You can create a skills-match view by applying a *skills filter* to a view. For more information, see [Creating a skills-match view](#topic_cnx_pwf_2nb).

Skills-match views have the following limitations:

- You can only have one skills-match view in Support, not multiple.
- If the ticket count in a skills-match view includes more than 3,000 tickets or a processing timeout occurs, all tickets will have the skills correctly applied, but some tickets may not appear in the view.
- Only the first 30 tickets in a skills-match view are displayed. The order is based on how your tickets are sorted. You can change the displayed tickets by changing the view’s sorting criteria.
- Tickets with no skills are also included in the skills-match view and are visible to all agents. The only tickets excluded from a skills-match view are tickets that have different skills than those specified in the filter.

### Limitations of views when using routing rules to add skills to tickets

The following limitations apply to all types of skills-based views if you're using routing rules to assign skills to tickets rather than triggers.

- Routing rules add skills to tickets only when tickets are created. This means if a ticket is updated so that it no longer meets a skill's conditions, the ticket will continue to appear in the view for the original skill match. To remove a ticket from a view when it no longer meets the skill's conditions, you can manually [remove the skill from the ticket](https://support.zendesk.com/hc/en-us/articles/5833458075930#topic_obh_qrt_5xb).
- Language skills are applied to a ticket based on the requester’s language, not the ticket's language.

## Creating views with skills-based conditions (recommended)

When an agent uses a view with a skills-based condition, they can see tickets with skill requirements that match their own skills or tickets with no associated skills.
You can't combine these conditions in a single view.

Keep in mind that views with skills-based conditions don't have any indicators for agents or admins that only tickets matching their skills are visible to them in the view. You can include something like "(skills)" or "(filtered)" in the view name if you want to make this clearer to agents using the view.

Note: Don't add a skills-match filter to views with skills-based conditions. This negatively affects the view's performance.

**To create a skills-based view using conditions**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Views**.
2. Click **Add view** or hover your cursor over the skill type you want to modify, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)), and select **Edit view** or **Clone view**.
3. In the **Conditions** section, click **Add Condition** under **Tickets must meet all of these conditions to appear in the view**.
4. Add the condition:
   - **Skills + Is + Current user skills**: You can add this type of condition to as many different views as you want. Tickets without skills are excluded from views with this condition.
   - **Skills + Is + No skills**: This condition can't be combined with the *Skill+Is+Current user skills* condition. Only tickets without skills are included in a view with this skills-based condition. Views with this condition don't include a count of tickets, and the user experience of browsing back and forward looks a little different from other views.
5. Click **Save**.
6. If the view is a [shared view](https://support.zendesk.com/hc/en-us/articles/4408888828570#topic_emv_1tp_tz), ensure it's visible to the right agents and then let the agents know that the view is a skills-based view.

## Creating a skills-match view

You can create a skills-match view by adding a skills filter to a [view](https://support.zendesk.com/hc/en-us/articles/4408888828570). However, you can have only one skills-match view in Support.
Tickets without skills are included in this view.

Note:

- If you need a skills-based view that includes tickets without skills, apply a skills filter to the view instead of a skills-based condition. Don’t add a skills filter and a skills-based condition to a single view.
- Only certain views are compatible with filtering. Incompatible views appear in the drop-down menu, but are dimmed and can't be selected.

**To create a skills-match column view**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Views**.
2. Click **Add view** or hover your cursor over the skill type you want to modify, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)), and select **Edit view** or **Clone view**.
3. On the view's page, under **Formatting** click **Add column** and select **Skill match**. All tickets in the view should have a checkmark in this column; if they don’t, go back and check your view conditions. Using the column on its own, without the skills match filter, on any view lets agents know which tickets match their skills without actually hiding the ones that don’t.
4. Make any other changes to the view and click **Save**.

**To create a skills-match filtered view**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Skills**.
2. Apply a skills filter to a view.
   - Under **Skills match view**, click **Choose view**, and use the dropdown menu to select the view you want to filter by skill. Then click **Save**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/skills_filter_dropdown.png)

### Using a skills-match filtered view

When a skills filter is applied to a view:

- On the **Views** page in Admin Center, the view appears with a filter icon.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_page_skills_filter.png)
- When an agent opens the view, they see only those tickets for which they match all required skills.
- When an agent uses [Play mode](https://support.zendesk.com/hc/en-us/articles/4408882039450#topic_avj_hfg_vt) with the view, only skills-matched tickets are displayed.

## Converting an existing skills-match view

If you have an existing skills-match view, you can convert it into a [view with a skills-based condition](#topic_ygf_twf_2nb) by cloning it and then adding a skills-based condition.

**To convert a skills-match view into a view with a skills-based condition**

1. Deactivate your skills-match view.

   In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Views**.
2. Hover your mouse over the view, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)), and select **Deactivate view**.
3. Hover your mouse over the deactivated view, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)), and select [**Clone view**](https://support.zendesk.com/hc/en-us/articles/4408888828570#topic_fjf_vev_ec).
4. Edit the cloned view to [add skills-based conditions](#topic_ifc_vwf_2nb).
5. Click **Save**.

   Note: When you clone a view, it becomes an active view as soon as you click **Save**, regardless of whether the parent view was active or inactive.

## Validating your skills-based views

To figure out the best way to define your skills-based views, you can start with a small test. Set up a view for yourself with a skills match column. Are you seeing the checkmarks where you expect them to be? Then add a skills match filter to that view. You shouldn't see any tickets without a checkmark.

Next, ask one or two agents to help you test the skills and view. When doing this, pick a view the agents use often, clone it, and add the skills column. Incorporate their feedback and then continue to expand the test by using the skills match filter rather than the column. This enables agents to use play or Guided Mode, which is probably easier for them.

Repeat this testing and validation process as needed to ensure the views are still meeting your needs.
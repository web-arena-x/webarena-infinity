# Searching triggers

Source: https://support.zendesk.com/hc/en-us/articles/4408838286106-Searching-triggers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center > Objects and rules > Business rules >
Triggers

Admins and [agents in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) to manage business rules can search for ticket triggers and object triggers and filter them based on a number of factors. You can define a simple filter based on a single criteria such as name, description, condition, or action, or you can create advanced filters based on multiple criteria. For more information on triggers, see [Triggers resources](https://support.zendesk.com/hc/en-us/articles/4408843730458).

This article contains the following sections:

- [Searching for triggers by name](#topic_vnl_zpy_tb)
- [Searching for triggers by description](#topic_sgf_3xz_xmb)
- [Searching for triggers by condition](#topic_hc4_wxz_xmb)
- [Searching for triggers by action](#topic_jyz_qzz_xmb)
- [Searching based on multiple filters](#topic_iyp_y11_ymb)
- [Viewing category tags in search results for ticket triggers](#topic_ezg_rvn_14b)

**Related topics**

- [About Zendesk triggers and how they work](https://support.zendesk.com/hc/en-us/articles/4408822236058)
- [Creating ticket triggers for automatic ticket updates and notifications](https://support.zendesk.com/hc/en-us/articles/4408886797466)
- [Creating object triggers to update records and send notifications](https://support.zendesk.com/hc/en-us/articles/7313293890970)

## Searching for triggers by name

If you know the name, or partial name, of the ticket or object trigger you want to view, you can enter it into the search at the top of the page.

**To search for triggers by name**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.The Triggers list appears.
2. Click the **Tickets** tab or **Objects** tab.
3. **Active** triggers are listed by default. If you’re searching for an inactive trigger, click **Filter**, select **Inactive**, and click **Apply filters**.

   Note: You must select either *active* or *inactive*. If you clear filters neither will be selected, and no trigger results can returned.
4. Enter the name or partial name of the trigger in the search field above the triggers list and press **Enter**.

   All triggers with a name that contains the search term appear in the list, along with the number of search results.

   You can also enter multiple search terms, separated by a space, to find names that contain all of the terms. For example, searching for **req cc** finds all names that include both the words **requester** and **CCs**.

## Searching for triggers by description

In some cases, it may be helpful to search by a trigger description. For example, you might search for descriptions that include the word *escalate* to find triggers that might change ticket priority.

**To search for triggers by description**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click the **Tickets** tab or **Objects** tab.
3. **Active** triggers are listed by default. If you’re searching for an inactive trigger, click **Filter**, select **Inactive**, and click **Apply filters**.

   Note: You must select either *active* or *inactive*. If you clear filters neither will be selected, and no trigger results can returned.
4. Enter a trigger description or the first few characters of a word in the description in the search field at the top of the triggers list and press **Enter**.

   All triggers with a description that contains the search term appear in the list, along with the number of search results.

   You can also enter multiple search terms, separated by a space, to find descriptions that contain all of the terms. For example, searching for **requester email** or **req email** finds all descriptions that include both the words **requester** and **email**.

## Searching for triggers by condition

Use filters to search for specific conditions within trigger definitions. For example, you could search for all triggers that run when the ticket status is solved.

**To search for triggers by condition**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click the **Tickets** tab or **Objects** tab.
3. **Active** triggers are listed by default. If you’re searching for an inactive trigger, click **Filter** and select **Inactive**.

   Note: You must select either *active* or *inactive*. If you clear filters neither will be selected, and no trigger results can returned.
4. Click **Filter**
5. In the **Filter by** panel, click **Add**.
6. Select **Conditions**, then select a **Category**, **Operator**, and **Value**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/triggers_search_condition_field_tm.png)

   To quickly find a condition, you can start typing the condition name in the field. For a full list of the available trigger conditions, see [Building trigger condition statements](https://support.zendesk.com/hc/en-us/articles/4408893545882#topic_i3y_fkz_1cb).
7. Click **Apply filters**.

   All triggers that contain the condition and values specified are returned, along with the number of search results.

## Searching for triggers by action

Use filters to search for specific actions within trigger definitions. For example, you could search for all triggers that send email to customers.

**To search for triggers by action**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click the **Tickets** tab or **Objects** tab.
3. **Active** triggers are listed by default. If you’re searching for an inactive trigger, click **Filter** and select **Inactive**.

   Note: You must select either *active* or *inactive*. If you clear filters neither will be selected, and no trigger results can returned.
4. Click **Filter**.
5. In the **Filter by** panel, click **Add**.
6. Select **Actions**, then select a **Category** and **Value**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/triggers_search_action_field_tm.png)

   See [Building trigger action statements](https://support.zendesk.com/hc/en-us/articles/4408893545882#topic_ncz_4kz_1cb) for a list of the available trigger actions. To quickly find an action, you can start typing the action name in the field.
7. Click **Apply filters**.

   All triggers that contain the action and values specified are returned, along with the number of search results.

## Searching based on multiple filters

You can also search for triggers based on multiple names, descriptions, conditions, or actions. Names and descriptions are entered in the search field, and conditions and actions are defined as filters. You can define up to two condition and action filters in addition to the status filter.

**To search based on multiple filters**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. Click the **Tickets** tab or **Objects** tab.
3. **Active** triggers are listed by default. If you’re searching for an inactive trigger, click **Filter** and select **Inactive**.

   Note: You must select either *active* or *inactive*. If you clear filters neither will be selected, and no trigger results can returned.
4. Enter your search term related to the name or description of the trigger.
5. Click **Filter**.
6. In the **Filter by** panel, click **Add** and define up to two filters based on [Conditions](#topic_hc4_wxz_xmb)
   or [Actions](#topic_jyz_qzz_xmb).
7. Click **Apply filters**.

   All triggers that meet your search critera are returned, along with the number of search results.

## Viewing category tags in search results for ticket triggers

Search results include a category tag to show which category each trigger in the results belongs to.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/triggers_search_category_tags_tm.png)
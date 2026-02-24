# Categorizing your views

Source: https://support.zendesk.com/hc/en-us/articles/8009260752794-Categorizing-your-views

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > Workspaces > Agent tools > Views

Views are a way to group tickets based on certain criteria. You can access your views list and open any view to see the tickets associated with that view. The views list includes up to 100 active standard and shared team views and up to 10 personal views.

Admins and [agents with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can categorize shared views to create a folder structure that reflects your organization and allows you to better monitor work across your teams. Admins and [agents with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can also categorize their personal views to quickly navigate their expanded views list.

This article covers the following topics:

- [Understanding views categorization](#topic_kqy_15d_tcc)
- [Creating view categories and subcategories](#topic_qjv_hvd_tcc)

Related articles:

- [Creating view to build customized list of tickets](https://support.zendesk.com/hc/en-us/articles/4408888828570)
- [Managing your views](https://support.zendesk.com/hc/en-us/articles/4408832792986)

## Understanding views categorization

Create views [categories](#topic_dj5_f5d_tcc) and [subcategories](#topic_yvf_h5d_tcc) from the Views page in Admin Center. When you create categories and subcategories for your views, you’re creating a folder structure in the Views panel in the Zendesk Agent Workspace. These folders are expandable and collapsible and can help you better navigate your views.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_categorized_agentworkspace.png)

Views can be categorized in a hierarchy of up to three levels under your Shared and Personal Views folders in the Agent Workspace.

### About categories

You can create a category by entering a double colon (**::**) in a view’s title field. For example:

`Tier 2::Returns`

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_categorize_category_create.png)

In the example above, the text preceding the double colon is a category; the text after the double colon is the view. In the Agent Workspace, the view (in this case, Returns) is nested under the category folder (Tier 2).

You can group multiple views under one category by entering the exact text and the double colon (::) syntax before the titles of each view you want to appear in the category. For example:

- Tier 2::Refunds
- Tier 2::Sales
- Tier 2::Recently solved

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_categories_multiple_views.png)

In the Agent Workspace, the views Recently solved, Refunds, Returns, and Sales are all nested under the Tier 2 category folder. The total number of tickets in the category is shown to the right of the category name.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_categorize_nested.png)

Note: The category text must match exactly if you want to nest multiple views under a category. If the text doesn’t match, a new category folder is created.

### About subcategories

Similar to categories, you can create view subcategories by using the double colon (::) syntax in a view’s title. A subcategory is the third level in a view folder hierarchy so you’ll enter the double colon twice in the view’s title. For example:

`Tier 2::Tier 2 - Escalated::Urgent`

In this example, the text after the first double colon (Tier 2 - Escalated) is the subcategory; the text after the second double colon (Urgent) is the view. In the Agent Workspace, the view is nested under the subcategory folder which is nested under the category folder (Tier 2).

Like categories, you can group multiple views under a subcategory by entering the exact text and the double colon (::) syntax before the titles of each view you want to appear in the category. For example:

- Tier 2::Tier 2 - Escalated::Pending
- Tier 2::Tier 2 - Escalated::Hold

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_categorize_nested_subcategories.png)

In the Agent Workspace, the Tier 2 - Escalated subcategory is nested under the Tier 2 category folder. The Tier 2 - Escalated subcategory views - Urgent, Pending, and Hold - are nested under the subcategory folder. The total number of tickets in the subcategory is shown to the right of its name.

Note: The category and subcategory text must match exactly if you want multiple views to nest under a category or subcategory. If the text doesn’t match, a new category or subcategory folder is created.

## Creating view categories and subcategories

Admins and [agents with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can create categories and subcategories for shared and personal views.

**To categorize views**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png) **Workspaces** in the sidebar, then select **Agent tools > Views**.
2. [Create a new view](https://support.zendesk.com/hc/en-us/articles/4408888828570) or [edit an existing view](managing-your-views.md#topic_fzx_qyj_5b).

   Alternatively, you can [clone a view](creating-views-to-build-customized-lists-of-tickets.md#topic_fjf_vev_ec).
3. In the view’s title field, do one of the following:
   - To create a category, enter the category name, followed by a double colon (::) and view name. For example, Tier 2::Returns.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_categorize_category_create.png)
   - To create a subcategory, enter the category name, followed by a double colon (::), subcategory name, another double colon (::), and the view name. For example, Tier 2::Tier 2 - Escalated::Urgent.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_categorize_create_subcategory.png)
4. Set the view's access, conditions, and grouping as needed (see [Creating views](https://support.zendesk.com/hc/en-us/articles/4408888828570)).
5. Click **Save**.

   You can continue to add views to the categories and subcategories you create. Note that the category and subcategory text (that is, the text before a double colon) must match exactly. See [Understanding views categorization](#topic_kqy_15d_tcc).
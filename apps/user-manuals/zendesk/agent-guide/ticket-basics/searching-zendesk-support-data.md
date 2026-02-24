# Searching Zendesk Support data

Source: https://support.zendesk.com/hc/en-us/articles/4408894221594-Searching-Zendesk-Support-data

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Use the search tool to find data like tickets, users, and articles. You can filter results by type, customize columns, and preview ticket details. Access recent searches and update multiple tickets at once. Share search URLs with team members for consistent queries. This feature streamlines finding and managing support data, enhancing your workflow.

In Zendesk Support, you can search for data, such as ticket properties, user properties, comments, tags, help center articles, and so on by using the search tool located in the top toolbar. You can also search [live chat and messaging conversations](https://support.zendesk.com/hc/en-us/articles/4408846801946).

Administrators can search everything and agents can search the tickets and users that they have permission to see. For example, if as an agent you are limited to only seeing tickets in the groups that you belong to, you will only be able to see those tickets in your search results.

This article covers the following topics:

- [Accessing the search tool](#topic_kvk_xyk_zs)
- [Using search](#topic_htl_zbm_wf)
- [Accessing your recent searches](#topic_mn4_xxj_f1c)
- [Reviewing your search results](#topic_rh2_mzh_xf)
- [Filtering your search results](#id_amc_5f5_xr)
- [Customizing columns in search results](#topic_ij2_mzm_yhc)
- [Previewing ticket details from search results](#topic_srp_jn3_yr)
- [Updating tickets in bulk from search results](#topic_p2h_235_xr)
- [Sharing search URLs](#topic_ur5_vxd_yfb)

## Accessing the search tool

There are a few ways you can get to the Support search tool.

**To access the search tool**

- In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Search** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_icon.png)) in the upper-right of the top toolbar to open the simple search box:

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_icon_click.png)

- You can also hover your cursor over the **+Add** button in the upper-left of the top toolbar, then select **Search** to open the Search page:

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_add_tab.png)

- Alternatively, use the keyboard shortcut (**Control + Alt + F**/**Control + Option + F**) to open the simple search box.

## Using search

You can perform a text search and filter your search by content record type. As you enter your search query text, the menu suggests results based on the text you’ve entered and any filters you’ve applied. You can access the suggested results directly from the search menu.

You can also access a list of all results related to your query.

**To perform a search**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Search** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_icon.png)) in the upper-right of the top toolbar.

   Your most recent searches and viewed content records appear in a menu. See [Accessing your recent searches](#topic_mn4_xxj_f1c) to learn more.
2. Optionally, select a content record type to filter by.
   You can choose from tickets, users, articles, organizations, and side conversations.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_menu_filters.png)

   If you’ve [turned on AI agent tickets](https://support.zendesk.com/hc/en-us/articles/9204149016346-Understanding-and-viewing-AI-agent-tickets-for-AI-agent-only-conversations-EAP#topic_myq_2r1_2gc), when you filter by **Tickets**, you can use **Support type** to further filter by **All** tickets, **AI agent only** tickets, or **Agent only** tickets.
3. Begin typing your query in the search box. As you type, results are suggested that match your search term.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_menu_suggested_results.png)
4. Select a suggested result to navigate directly to the content record. Alternatively, press **Enter** or click **All results** to view more results on a new tab on the toolbar.

   From the toolbar, you can apply additional filters. See [Filtering your search results](#id_amc_5f5_xr).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_results.png)

   If you anticipate performing this search often, you may want to [save](https://support.zendesk.com/hc/en-us/articles/8050806061210) it so that it's easily accessible.

In addition to full text search, you can perform a search using common search operators combined with data property keywords and values to narrow your results. See [Zendesk Support advanced search](https://support.zendesk.com/hc/en-us/articles/4408835086106).

## Accessing your recent searches

You can access your most recently viewed content records and searches from the search menu. Content records include tickets, users, articles, organizations, and side conversations.

By accessing your recent searches and viewed content, you can save time by reusing common searches and quickly accessing relevant records.
See [Accessing saved searches](https://support.zendesk.com/hc/en-us/articles/8050806061210#topic_kfx_ybg_5cc) if you've saved any of your common searches.

**To access your recent searches**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Search** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_icon.png)) in the upper-right of the top toolbar.

   Your most recent searches and viewed content appear in a menu.
2. Optionally, select a content record type to filter your recent searches and viewed content. You can choose from tickets, users, articles, organizations, and side conversations.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_recent_searches_filters.png)
3. Click a **Recently viewed** content record to navigate to it or a **Recently searched** query to perform the search.

## Reviewing your search results

Your search results are sorted into categories for tickets, users, articles, and organizations. Each category contains different columns, icons, and other elements, to help you identify, filter, sort, or otherwise organize your search results.

Note: Due to [API rate limits](https://developer.zendesk.com/rest_api/docs/support/search#results-limit), search returns only the first 1,000 results.

**To select the type of result you want to view**

- Click the category at the top of the search results page.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_categories.png)

### Tickets

The Tickets category returns a list of support requests that have your search term(s) in their subject line or comments. This category contains the most options for organizing your results. The Ticket category's columns display the following relevant ticket information:

- **ID**, the ticket's numeric identifier.
- **Subject**, the text from the ticket's subject line.
- **Requested**, the date the ticket was submitted.
- **Updated**, the last time the ticket was updated.
- **Requester**, the name of the user who submitted the ticket.
- **Group**, the group assigned to handle the ticket.

Each result is preceded by an icon indicating that ticket's current status:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_ticket_results_colors_new.png)

If you have [custom ticket statuses activated](https://support.zendesk.com/hc/en-us/articles/4412575841306), closed tickets may be included in your search results. Closed tickets are identified by an icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_status_closed_icon.png)), which you can hover over for more information. To learn more about how tickets are closed when custom ticket statuses are activated, see [About closed tickets solved with a custom ticket status](https://support.zendesk.com/hc/en-us/articles/8263915942938#topic_zlx_pyk_fdc).

You can exclude closed tickets from your results by clicking the **Filter** menu and clearing the **Include closed tickets** check box.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cts_search_closed_checkbox.png)

**To open a ticket from a search result**

- Click anywhere on a ticket result's row to open that ticket in a new tab.

**To sort your ticket search results**

- Click the **Requested** or **Updated** column in the search results to toggle between displaying results in ascending or descending order by date.

Note: The comment automatically added to a ticket solved by Answer Bot ("Yes, this article solved my issue") is not included in Explore.

### Users

The Users category returns a list of accounts who include your search term(s) in their names, or elsewhere in their profiles. This doesn't include custom user fields in profiles (see [Searching custom user and organization fields](https://support.zendesk.com/hc/en-us/articles/4408883318554#topic_pyt_m1s_vk)).

The results for this category contain the following columns:

- **Name**, the user's submitted name.
- **Email**, the user's email address.
- **Organization**, the company or group they work for.
- **Role**, the role assigned to that user (agent, admin, end-user, and the like).
- **Updated**, the last time the user's profile was updated.

**To open a user profile from a search result**

- Click anywhere in a user's row to open their profile in a new tab.

### Articles

The Articles category returns a list of knowledge base entries that mention your search term(s). The results for this category contain the following columns:

- **Title**, the article's title.
- **Updated**, the last time the article was updated.
- **Created**, the date the article was posted to the knowledge base.

**To open an article from a search result**

- Click anywhere on an article's row to open that article in a new browser window or tab.

### Organizations

The Organizations category returns a list of organizations that include your search term(s) in their names or elsewhere in their profiles. This doesn't include custom organization fields in profiles (see [Searching custom user and organization fields](https://support.zendesk.com/hc/en-us/articles/4408883318554#topic_pyt_m1s_vk)).

The results for this category contain the following columns:

- **Name**, the organization's name.
- **Notes**, any notes added to their profile.
- **Created**, the date the organization first registered.
- **Updated**, the last time the organization updated its profile.

**To open an organization profile from a search result**

- Click anywhere on an organization's row to open that organization's profile in a new tab.

## Filtering your search results

You can further narrow your search results using search filters. You can filter for just the type of elements you want to see: tickets, articles, users, or organizations. Each category offers relevant ways to further refine your results.

**To filter search results**

1. [Perform](#topic_htl_zbm_wf) a search.
2. On the search results page, click **Filters**.
3. Click the **Search** drop-down to select the type of element you want to include in your search.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_filter_options.png)
4. Fill out the options as needed to refine your search.

You can further narrow your filtered search results [using search operators and keywords](https://support.zendesk.com/hc/en-us/articles/4408835086106).

## Customizing columns in search results

You can select and organize the columns you want to display in your search results, to focus on the data you need. Available columns are based on the object type you’re searching for. You can include up to 10 columns in your search results.

Note: Currently, custom fields can’t be added to search results.

Your column customization will remain in place until one of the following occurs, after which your search results will revert back to the default columns:

- You sign out of Zendesk
- You delete your browser cache
- You do a hard browser refresh
- You close your browser

**To customize columns in your search results**

1. [Perform a search](https://support.zendesk.com/hc/en-us/articles/4408894221594#topic_htl_zbm_wf).
2. On the search results page, click the **Manage columns** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/manage_columns_icon.png)).
3. In the Manage columns panel, the current column selections are displayed.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/manage_columns_panel.png)

   Customize the columns as needed:

   - To add a column, click the **Add column** button.
   - To remove a column, click the **x** next to that column’s name.
   - To change the column order, click a column’s grabber icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/salesforce_grabber_icon.png)) and drag it to the desired position.
4. Click **Apply**.

## Previewing ticket details from search results

Hovering your cursor over the subject of a result displays a preview of that ticket, allowing you to glean more information about the ticket without having to open it. In the preview window, snippets of comments or fields containing your search term(s) are displayed, with the search term(s) highlighted, so you can determine whether the ticket is relevant to your search before opening it.

**To preview a ticket from the search results**

- Hover your cursor over the subject of a result to display a preview of that ticket.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/full_search_with_hover.png)

## Updating tickets in bulk from search results

You can make ticket updates to more than one ticket at a time. For example, to assign yourself to multiple tickets, you can select them in the search results and set yourself as the assignee. You can also delete, merge, or mark the selected tickets as spam.

**To update multiple tickets**

1. In your search results, select the tickets you want to update.

   You can pick and choose the tickets you want to update or select the entire list by clicking the check box at the top left of the results list.
2. Click **Edit** from the toolbar at the bottom of the list.
3. Update the ticket information as needed. See [Managing tickets in bulk](https://support.zendesk.com/hc/en-us/articles/4408886890906).
4. Click **Submit** to apply the changes to your selected tickets, or click the menu drop-down on the Submit button to apply the changes.

## Sharing search URLs

You can copy search query strings you create in Support to your clipboard so you can then share them with other users. When the other user clicks the search query you shared, the search is performed in their Support instance using the same query you created.

**To copy and share search queries**

1. [Perform](#topic_htl_zbm_wf) a search or [access](https://support.zendesk.com/hc/en-us/articles/8050806061210#topic_kfx_ybg_5cc) one of your saved searches.
2. On the Search page, click the **Actions** menu, then select **Copy link**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_actions_menu_save.png)

The search query is copied to your clipboard. You can now send the query to other users, for example, by pasting it into an email.
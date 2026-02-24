# Using the access log to monitor agent activity (ADPP add-on)

Source: https://support.zendesk.com/hc/en-us/articles/6066010357530-Using-the-access-log-to-monitor-agent-activity-ADPP-add-on

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Advanced Data Privacy and Protection (ADPP) |

Verified AI summary ◀▼

Use the access log to monitor agent activity and enhance data security with the Advanced Data Privacy and Protection add-on. Track which tickets, user profiles, and searches agents access within the last 90 days. Filter data to refine search results and export logs using the API. This tool helps you detect security risks and ensure compliance, providing valuable insights into agent interactions.

Location: Admin Center > Account > Logs > Access log

The access log, part of the [Advanced Data Privacy and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906), is a powerful tool that enhances data security and administrative control of your account. It's a record of access events for your account related to tickets, user profiles, and searches.
This differs from the [audit log](https://support.zendesk.com/hc/en-us/articles/4408828001434), which provides a detailed log of changes to settings or fields.

The access log is currently available as an [API](https://developer.zendesk.com/api-reference/ticketing/account-configuration/access_logs/) and in Admin Center, and captures what data an agent or admin has accessed in your account within the last 90 days. It doesn't capture end-user activity.

Access logs can help you answer the following questions:

- What tickets are agents accessing?
- What information are agents searching for?
- What user profiles are agents viewing?

Admins and [agents with permission](https://support.zendesk.com/hc/en-us/articles/4408882153882) can view the access log. See [Access logs use cases and workflows](https://support.zendesk.com/hc/en-us/articles/9972142485530) for examples of how to use the access log to detect security risks and help ensure compliance.

This article covers the following topics:

- [Turning on the access log](#topic_d1k_vph_xyb)
- [Viewing the access log in Admin Center](#topic_c4g_23m_pdc)
- [Filtering access log data to refine search results](#topic_mdl_fy5_3hc)
- [Using the API to export access logs](#topic_lkj_dmm_pdc)

## Turning on the access log

Before you can view access logs, you must turn on the Access Log API in Admin Center.
When you do, Zendesk begins capturing access events. Access events that occurred before you turned on the API aren't captured.

Only admins can turn on the access log. After you turn it on, data may take up to 60 minutes to populate.

**To turn on the access log**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Logs > Access log**.
2. Select **Turn on the Access Log API**.
3. Click **Save**.

## Viewing the access log in Admin Center

The Access log page in Admin Center lets you view a detailed list of access events in your account. You must first [turn on the access log](#topic_d1k_vph_xyb) before viewing it in Admin Center.

**To open the access log in Admin Center**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
 **Account** in the sidebar, then select **Logs > Access log**.

 The Access log page appears. Each row in the access log represents a single access event by an agent or admin in your Zendesk account. Log entries are sorted by time (newest entry first). Click an event to display its details in the right panel.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/access_log_event_detail_5.png)

Use the **Show and hide columns** menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/access_log_column_icon.png)) in the upper-right corner of the table to adjust the columns that are visible in the log.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/access_log_show_columns.png)

The following information appears for each event in the access log.

| Column | Description |
| --- | --- |
| Time | The time and date when the page or record was accessed, displayed in [your account's time zone](https://support.zendesk.com/hc/en-us/articles/4408887059866#topic_dil_hnc_xe). If you're unsure what time the access log is using, hover over the information icon in the **Time** column heading. |
| Actor | The team member or user who accessed the page or record in Zendesk. This helps track which users are interacting with a specific account. |
| IP address | The IP address of the user who made the request. |
| Authorization type | The method used for user authorization. Examples: Basic, Session, Digest, Bearer |
| Client | The client software that is initiating the request. Example: a web browser |
| Category | The type or classification of access that occurred, such as Users, Profiles API, or Phone numbers. This helps identify the function or system component involved. Some access events don't have an associated category, so this field may be empty. |
| Summary | A brief and easy-to-understand description of the access event, such as Show user, Get profile by identifier, or List phone numbers. Summarizes the purpose of the access entry. Some access events don't have an associated summary, so this field may be empty. |
| HTTP Status | The HTTP status code of the response. |
| Method | The HTTP method of the request. Possible values are GET, POST, PUT, and DELETE. |
| Accessed URL | The API endpoint path of the request. |

## Filtering access log data to refine search results

Since the access log can include a large volume of events, filtering makes it easier to find what you’re looking for.

Tip: If you repeat the same access log filters, bookmark them in your web browser after you apply them. The filter displays in the URL.

**To filter the access log**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Logs > Access log**.
2. Click **Filter**.

   Filters appear in a panel.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/access_log_drawer.png)
3. To filter by date, set the fields **Start date**, **Start time**, **End date**, and **End time**.

   The default date reflects the maximum number of days the log can capture data (90 days). The time reflects the local time for your account in your [localization settings](https://support.zendesk.com/hc/en-us/articles/4408887059866).
4. Enter a name or email address in the **Actor** field to filter by the people or systems responsible for the access events.
5. Apply an activity filter for a more refined search:
   - **Category**: Type or select a category to filter events by type (such as Users, Permissions, or Tickets). The drop-down shows a limited number of categories and displays suggestions after typing three characters.

     After you select a category, you can narrow your results by selecting one or more items from the **Summary** drop-down list. For example, if you selected the Users category, you can add the **Show User** and **Update User** summary items to display only those access events.
   - **Accessed URL**: Use this field to filter by the accessed API endpoint path. Example:
     `/api/v2/users/6649960843290/related.json`
6. Click **Apply filters**.

## Using the API to export access logs

Use the Access Logs API to export access logs to a CSV file. The API lets you filter the logs using the same filters as the Admin Center user interface, as described in [Filtering the data to refine search results](#topic_mdl_fy5_3hc). You can also use scripting to filter the returned data.

You’ll need to work with a developer or other technical resource at your company to export the data. See [Exporting access logs to a CSV file](https://developer.zendesk.com/documentation/ticketing/using-the-zendesk-api/exporting-access-logs/) and [Zendesk API Reference: Access Logs](https://developer.zendesk.com/api-reference/ticketing/account-configuration/access_logs/).
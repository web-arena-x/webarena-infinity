# About WFM custom report templates

Source: https://support.zendesk.com/hc/en-us/articles/6443331692698-About-WFM-custom-report-templates

---

In Zendesk Workforce Management (WFM), you can create custom reports to gain insight into a variety of metrics, such as your workforce performance over a selected period of time. You can group data in multiple ways and apply specific filters for a more granular view from the Reports page.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Create custom WFM report templates to analyze workforce metrics over time. Customize data grouping and filtering for detailed insights. Save templates for reuse with different parameters. Edit templates to adjust settings like name or timezone. Export reports as CSV files for further analysis. Use these tools to tailor reports to your needs and enhance your understanding of workforce performance.

In Zendesk Workforce Management (WFM), you can create custom reports to gain insight into a variety of metrics, such as your workforce performance over a selected period of time. You can group data in multiple ways and apply specific filters for a more granular view from the Reports page.

When you create custom report templates, they're saved and can be reused for different time periods or parameters.

This article contains the following topics:

- [Understanding data aggregation in custom reports](#topic_tmj_khs_3fc)
- [Accessing the Reports page](#topic_kcp_yv1_cbc)
- [Creating a custom report template](#topic_tq4_kvr_3fc)
- [Duplicating custom report templates](#topic_vyn_yvr_3fc)
- [Editing a custom report template](#topic_tlt_pw1_cbc)
- [Exporting a report](#topic_mjm_nwr_3fc)

Related articles:

- [About WFM system report templates](https://support.zendesk.com/hc/en-us/articles/6443363334810)
- [Custom WFM report metrics](https://support.zendesk.com/hc/en-us/articles/6443376913818)

## Understanding data aggregation in custom reports

On the WFM reporting page, data is grouped differently depending on the time period you select. Here’s how it works:

- **1 day or less:** Data is displayed in 15 or 30-minute intervals.
- **Up to 7 days:** Data is grouped by hour or day.
- **Up to 31 days:** Data is shown by day or week.
- **Up to 13 weeks:** Data is grouped by week, month, or quarter.
- **Up to 58 weeks (about 13 months):** Data is shown by month or quarter.

These rules ensure the data remains easy to read and understand, regardless of the time period.

You can select up to three different grouping attributes from the following options:

- Activity type
- Agent name
- Custom field
- Location
- Organization
- Team
- Ticket group
- Ticket ID
- Ticket status
- Ticket via type
- Time breakdown

When using the [Organization](https://support.zendesk.com/hc/en-us/articles/4408886146842) attribute as a grouping criterion, you may notice two additional “N/A” folders appearing in the reporting layout:

1. The first “N/A” folder aggregates tickets that have no associated organization. This is typically observed in ticket-related metrics.
2. The second “N/A” folder relates to agent activity that is not associated with any ticket (and therefore has no organization). This can be identified by metrics related to [general tasks](https://support.zendesk.com/hc/en-us/articles/7069811858586), [unified agents statuses](https://support.zendesk.com/hc/en-us/articles/10114746509978), and [untracked time](https://support.zendesk.com/hc/en-us/articles/6443376913818#topic_xwv_3n4_52c__untracked_time).

## Accessing the Reports page

**To access the Reports page**

- In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_reports_folder_icon.png)
 **Reports** in the navigation bar, then select **Reports**.

## Creating a custom report template

**To create a custom report template**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_reports_folder_icon.png)
   **Reports** in the navigation bar, then select **Reports**.
2. Click the plus icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_plus_icon.png)) to create a template.
3. Enter a **Title**.
4. The timezone defaults to your account's timezone. Click the menu if you want to select a different timezone.
5. Click the arrow to expand the **Metrics** section, then select one or more metrics.
6. Click the arrow to expand the **Attributes** section, then choose how to **Group** the data.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ts_customreports_create_dimensions.png)
7. Click the arrow to expand the **Filters** section, then select the report filters.

   Filters allow you to specify which data you want to analyze in the report.
8. When you're done setting up your report, click **Save**.
9. Select the time period for the report. After selecting a time period, the data is presented in the Reports page.

## Duplicating custom report templates

Duplication is useful when you want to reuse most of the configurations of a template already set and only need to change filtering criteria or make some adjustments to the attributes or grouping.

**To duplicate a custom report template**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_reports_folder_icon.png)
   **Reports** in the navigation bar, then select **Reports**.
2. Hover over the template you want to reuse and click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_options_vertical.png)) next to it.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_duplicate_template.png)

You can also create custom reports by copying system report templates.
See [Creating a custom report from a system report template](https://support.zendesk.com/hc/en-us/articles/6443363334810#topic_rxy_bjr_tzb).

## Editing a custom report template

**To edit a report template**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_reports_folder_icon.png)
   **Reports** in the navigation bar, then select **Reports**.
2. Select a template you want to edit and then click the **Edit** icon (![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/wfm_edit_pencil_icon.png)).

   When editing a template, you can select and modify different templates without needing to click the Edit icon again.
3. From the edit view, you can update a report's name, timezone, or parameters, or delete the report template.
4. Click **Save**.

## Exporting a report

You can export a maximum of 406 days or 58 weeks in one export. Agent activity–related metrics, both on the Reports and Agent Activity pages, show accurate information only from the date the Reports feature was activated in your Zendesk account onward. The more metrics, attributes, or filters added in the reports, the longer it takes to generate.

You can also generate a partial export for each grouping level in the report by hovering over the grouping name and clicking the action menu next to the name. The Export CSV option appears. This exports the selected grouping section only.

**To export a report**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_reports_folder_icon.png)
   **Reports** in the navigation bar, then select **Reports**.
2. Select the **Report template** you want to export.
3. Select the **Time period** for which you want to export the report data.
4. Click **Export CSV**.

   A message appears confirming that the report is being generated and a link to download the report will be sent to your email. The report is exported in hh:mm:ss format, but you can use the following formula to convert it to seconds: `=VALUE([CELL#]*24*3600)`
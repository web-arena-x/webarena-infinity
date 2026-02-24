# Exporting dashboard tabs and reports

Source: https://support.zendesk.com/hc/en-us/articles/4483481898266-Exporting-dashboard-tabs-and-reports

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Light, Professional, or Enterprise |

Sometimes, you might want to save the current version of a dashboard tab or
report. Or, you might want to view the data in a different format. You can save
individual dashboard tabs or reports to your computer using the **Export** option.

This article contains the following topics:

- [Exporting a dashboard tab](#topic_spz_dpz_5sb)
- [Exporting a report from report
  builder](#topic_abw_h4c_zsb)
- [Choosing an export format](#topic_jds_34c_zsb)

## Exporting a dashboard tab

When exporting dashboard tabs, you must export them one at a time. It's not possible
to export all of a dashboard's tabs at once.

**To export a dashboard tab**

1. [With a dashboard tab open](https://support.zendesk.com/hc/en-us/articles/4408831997466), click
   the Export dashboard icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dash_ex_1.png)).
2. On the **Export dashboard** page, select an export format of **CSV**,
   **Excel**, **PNG**, or **PDF**. See [Choosing an export format](#topic_jds_34c_zsb)
   for more details about each option.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/dash_ex_2.png)
3. Click **Export dashboard**.

## Exporting a report from report builder

**To export a report from report builder**

1. With a report open, click the dropdown arrow next to the **Save** button
   and select **Export**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_export_query_query_builder.png)
2. In the **Export report** window, select an export format of
   **CSV**, **Excel**, **Image**, or **PDF**. See [Choosing an export
   format](#topic_jds_34c_zsb) for more details about each option.
3. Click **Export**.

## Choosing an export format

When you export a report, you can choose between **CSV**, **Excel**,
**Image**, or **PDF** export formats.

Note: Style information such as the metric display format, date display format, and other styling
applied to the report is not exported to Excel and CSV files.

The **CSV** format is a raw data export. All attributes are placed in rows, even
if they're placed in columns or explosions in Explore. Metric and date formats
aren't carried over. If there are multiple reports exported at the same time, a
separate CSV file is generated and compressed into a ZIP file.

The **Excel** format exports your report as data in rows and columns.
Visualizations and chart configurations are not preserved. If multiple reports are
exported at the same time (as when you export a dashboard tab), they're placed in
different tabs within the same Excel file. Excel exports are limited to 50,000 rows
and 16,000 columns.

Tip: When you export a report, any filters you applied are not included. To export
the report with filters applied, use your browser's print option to create a PDF
file.

If you choose either **PNG** or **PDF**, you can further specify the quality
and size of the exported file:

- **Medium** : Exports the dashboard at its current size. This option is
  selected by default for manual and scheduled exports. It can be changed for
  manual exports, but not for scheduled exports.
- **Low**
- **High**

Note: When exporting an image or PDF, make sure the report in
the dashboard is wide enough and tall enough to show all the information. Any
information hidden behind horizontal or vertical scroll bars won't be
exported.
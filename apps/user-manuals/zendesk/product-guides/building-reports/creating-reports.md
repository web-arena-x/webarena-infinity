# Creating reports

Source: https://support.zendesk.com/hc/en-us/articles/4408821589530-Creating-reports

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

A report is a request for information from your Zendesk data. For example, you might want to ask "How many open support tickets do I have?"

In Explore, users with the [Admin or Editor role](https://support.zendesk.com/hc/en-us/articles/4408836002970) can create and store multiple reports in the Reports library. You can then arrange these reports on dashboards, which you can share with others.

This article contains the following sections:

- [Creating a report](#topic_ol4_zwc_zsb)
- [Adding metrics to your report](#topic_zt4_3xc_zsb)
- [Adding attributes to your report](#topic_m34_jxc_zsb)
- [Saving your report](#topic_of3_kxc_zsb)

**Related articles**

- [Using metrics and attributes in reports](https://support.zendesk.com/hc/en-us/articles/4408846733722-Adding-metrics-and-attributes)
- [Customizing reports](https://support.zendesk.com/hc/en-us/articles/4408839246618)
- [Working with reports](https://support.zendesk.com/hc/en-us/articles/4408829048602-Working-with-queries)

## Creating a report

In Explore, you can create a report from three different places: the Reports library, a dataset, and a dashboard.

### Creating a report from the Reports library

You can create a new report directly from the Reports library. The Reports library includes all of your created and cloned reports. You must have added a dataset or duplicated a dashboard to add a report from the Reports library (see [Working with datasets](https://support.zendesk.com/hc/en-us/articles/4408846513050-Creating-a-dataset) or [Cloning Explore dashboards](https://support.zendesk.com/hc/en-us/articles/4408821374362-Cloning-pre-built-and-shared-dashboards)).

**To create a report**

1. Click the reports icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_query_icon.png)).
2. Click the **New report** button.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_creating_a_new_report.png)
3. Choose the dataset containing the information you want to use in your report.

   For help choosing a dataset, see [Working with datasets](https://support.zendesk.com/hc/en-us/articles/4408846513050-Choosing-and-creating-datasets).

   ![Explore choosing a dataset page](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_select_a_dataset.png)
4. Click **Start report**.

The report builder opens a new report using the dataset you chose.

### Creating a report from a dataset

You can create new, blank reports from a dataset. To add reports from a dataset, you must connect to a Zendesk Support dataset (see [Working with datasets](https://support.zendesk.com/hc/en-us/articles/4408846513050-Creating-a-dataset) or [Cloning Explore dashboards](https://support.zendesk.com/hc/en-us/articles/4408821374362-Cloning-pre-built-and-shared-dashboards)).

**To create a new report from a dataset**

1. Click the **Dataset library** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dataset_icon.png)).
2. Hover over the dataset you want to create a report from.
3. Click the **Settings** icon to the right of the dataset name.
4. Select **New report from this...** from the dropdown list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_new_report_from_dataset.png)

   The report builder opens with a blank report using the dataset you chose.

### Creating a report from a dashboard

While you're creating a dashboard, you can start a new report directly from the dashboard builder. For help creating dashboards, see [Creating dashboards](https://support.zendesk.com/hc/en-us/articles/4408831595418-Creating-dashboards) and [Adding reports to dashboards](https://support.zendesk.com/hc/en-us/articles/4408827904794-Adding-queries-to-dashboards).

**To create a report from a dashboard**

1. Make sure that the dashboard you have opened is in edit mode. In the dashboard customization menu of the dashboard builder, click **Add**.
2. From the dropdown list, select **Add report**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_add_report_dropdown.png)
3. On the **Add report** page, click **New report**.
4. Choose the dataset containing the information you want to use in your report.

   For help choosing a dataset, see [Working with datasets](https://support.zendesk.com/hc/en-us/articles/4408846513050-Choosing-and-creating-datasets).

   ![Explore choosing a dataset page](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_select_a_dataset.png)
5. Click **Start report**.

If you need help creating a report, follow the articles in the [Building reports](https://explore.zendesk.com/hc/en-us/sections/207347787-Building-queries) section.

## Adding metrics to your report

Metrics are quantifiable values, such as the number of tickets, replies to tickets, and agent or customer wait times. You must add at least one metric to your report.

**To add a metric**

1. In the **Metrics** panel, click **Add**.
2. From the list, select the metric you want to add. You can expand or collapse the folders to show or hide specific metrics.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_adding_a_metric.png)
3. Click **Apply**. Your metric results automatically appear in your report.

Explore automatically uses the most suitable aggregator for the metric. However, you can change the aggregator by clicking the metric and selecting a new aggregator. See [Changing metric aggregators](https://support.zendesk.com/hc/en-us/articles/4408846897178).

You can also select whether the metric results are measured in different sizes or colors, on a separate axis, or as datatips. See [Using metrics and attributes in reports](https://support.zendesk.com/hc/en-us/articles/4408846733722).

## Adding attributes to your report

Attributes slice your data by non-quantifiable values, such as ticket ID, ticket tags, and assignee names. They can also be used to select or exclude results from your chart. You can add one or multiple attributes to a report, or none at all.

Attributes can be added in the **Columns**, **Rows**, **Explosions**, and **Filters** panels. Where you add an attribute changes the way your report works:

- **Columns** renders your results in one chart. See [Adding attributes to columns](https://support.zendesk.com/hc/en-us/articles/4408846733722-Adding-metrics-and-attributes#topic_uws_xnb_y5).
- **Rows** renders your results into individual charts or tables for each of your attribute values by using a row selector. See [Adding attributes to rows](https://support.zendesk.com/hc/en-us/articles/4408846733722-Adding-metrics-and-attributes#topic_egq_xnb_y5).
- **Explosions** renders your results into multiple charts, each representing a different value for the added attributes. Charts are shown side-by-side in one report. See [Adding attributes to explosions.](https://support.zendesk.com/hc/en-us/articles/4408846733722-Adding-metrics-and-attributes#topic_b2v_11k_y5)
- **Filters** restricts which results are shown without the attribute appearing on your report. See [Adding attributes as filters](https://support.zendesk.com/hc/en-us/articles/4408846733722-Adding-metrics-and-attributes#topic_s2p_xnb_y5).

**To add an attribute**

1. In the **Columns**, **Rows**, **Explosions**, or **Filters** panel, click **Add**.
2. From the list, select the attribute you want to add. You can expand or collapse the folders to show or hide specific attributes.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_adding_an_attribute.png)
3. Click **Apply**. Your attribute results automatically appear in your report.

## Saving your report

When you finish building your report, make sure to save it. Reports don't save automatically. If you navigate away from your report without saving, all changes will be lost.

**To save a report**

1. In the report builder, make sure you've given your report a descriptive name. If you don't, Explore automatically names your report according to the metrics and attributes you've added.
2. Click **Save** in the top-right corner.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_saving_a_query.png)

Note: You can also click the dropdown arrow next to **Save** and choose **Save as new** to save a new copy of the report. This is helpful if you want to make modifications to an existing report without overwriting the original.
# Working with the report builder (Beta)

Source: https://support.zendesk.com/hc/en-us/articles/5455225532954-Working-with-the-report-builder-Beta

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

Note: This article describes the beta version of the Explore report builder. For information on the classic report builder, see [Creating reports](https://support.zendesk.com/hc/en-us/articles/4408821589530).

The beta report builder helps you create reports that request information from your Zendesk data. For example, you might want to ask, "How many open support tickets do I have?"

In Explore, [users with the appropriate permissions](https://support.zendesk.com/hc/en-us/articles/4408820154266) can create and store reports in the Reports library. You can [add these reports to dashboards](https://support.zendesk.com/hc/en-us/articles/4408827904794), which you can then [share with others](https://support.zendesk.com/hc/en-us/articles/4408827282714).

The beta report builder is built into Explore. No sign-up is required.

This article contains the following topics:

- [Starting a report](#h_01GXRAHWYRSKBEH6ZAW6ANT7K7)
- [Adding metrics to a report](#h_01GXRAJ3Q49A51PBB787CG6WY0)
- [Adding attributes to a report](#h_01GXRAJ90JSPQTVAJBGW5V6MK1)
- [Changing the unit of a time-based attribute](#h_01HGZQZJ3VD1FSMKYYTPXXYWD3)
- [Removing metrics or attributes from a report](#h_01GXRAJE7JAKV827KAPASY3DKV)
- [Filtering a report](#h_01GXRAJMXXPE8ZKFDATR07VKV1)
- [Changing a report’s visualization](#h_01GXRAJTK12DFQZKS43EF5BE79)
- [Naming and saving a report](#h_01GXRAK0B9M4X1QHP90F4QEWSJ)
- [Editing a report](#h_01GXRAK6TN46KVPGSFMG6M22TH)
- [Adding tags to a report](#h_01HGZRM7BA5J8TY2CM5JPANVNA)
- [Changing how often a report reloads](#h_01HGZRMF1PWD6Q0X0X9F3H7PGS)
- [Cloning a report](#h_01HGZRMKBPRT2ZKXRCH5VP8WRG)
- [Exporting a report](#h_01HGZRMQ51R5NCMJQW3T7Q89MR)
- [Deleting a report](#h_01HGZRMV8VMQF2QV6MDF8KJ7C9)
- [Setting the beta report builder as default](#h_01HGZRN299MF6JTW11YS2N8838)

Related articles:

- [Understanding reports](https://support.zendesk.com/hc/en-us/articles/4408839341082)
- [Adding reports to a dashboard](https://support.zendesk.com/hc/en-us/articles/4408827904794)

The following video walks you through an example of creating a report with the beta report builder.

## Starting a report

You can create a report with the beta report builder from the Reports library. If you’re already in a report, you can quickly start a new one without returning to the Reports library. If you're in an existing report, you can switch to working in the beta report builder.

**To create a report**

1. In Explore, click the Reports icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_query_icon.png)) to open the Reports library.
2. In the banner titled **Report Builder beta is available**, select **Try beta**. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_beta_report_builder_banner.png)
3. On the **Select a dataset** page, choose the dataset that contains the information you want to report on. For help choosing a dataset, see [Understanding the available default datasets](https://support.zendesk.com/hc/en-us/articles/4408839218842#topic_hr1_tfk_jkb).

   Tip: If you begin creating your report and realize that you used the wrong dataset, you can quickly return to this screen by selecting the **Change dataset** option within the report builder.
4. Click **Start report**.

The beta report builder opens a new report using the dataset you chose.

**To create a new report from within the beta report builder**

1. From within the beta report builder, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) in the top-right.
2. Select **Create new report**. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_beta_report_builder_create_new_quick_action.png)

A new browser window opens with a fresh instance of the beta report builder.

**To edit an existing report in the beta report builder**

1. From within a report, at the bottom of the page, click **Switch to builder beta**.
2. Your report opens in the beta dashboard builder.

## Adding metrics to a report

Metrics are quantifiable values, such as the number of tickets or customer wait times. You must add at least one metric to your report.

**To add a metric to a report**

1. Make sure the **Metrics** tab is selected in the leftmost column.
2. Find the metric you want to add. The beta report builder gives you several options for finding the right metric: 
   - Search for a specific metric using the search bar.
   - Sort the available metrics by clicking **Popular** or **Recently used**.
   - Filter your search results by clicking the filter icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_filter.png)) and selecting the category the metric belongs to. This category is analogous to the metric folders in the classic report builder.
3. Click and drag the metric you want to use into the **Metrics** panel. Alternatively, you can click the plus sign (+) to the right of the metric name to add it. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_beta_report_builder_adding_metric.png) 
   Explore automatically uses the most suitable aggregator for the metric.
4. (Optional) If you want to change the metric aggregator, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) next to the metric and select a different aggregator. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_beta_report_builder_changing_aggregator.png)

## Adding attributes to a report

Attributes slice your data by non-quantifiable values, such as ticket ID, ticket tags, and assignee names. You can add one or multiple attributes to a report, or none at all.

Attributes can be added in the **Rows** or **Columns** panels. Which panel you add an attribute to changes the way your report works:

- The **Rows** panel allows you to add primary attributes that break down the metrics to show details.
- The **Columns** panel allows you to add secondary attributes that divide the results again for more insights.
- The **Filters** panel restricts which results are shown without the attribute appearing on your report. See [Filtering a report](#h_01GXRAJMXXPE8ZKFDATR07VKV1).

Note that the labels for the **Rows** and **Columns** panels change depending on which visualization you select.

| | | | | |
| --- | --- | --- | --- | --- |
| **Chart type** | **Primary attributes** | | **Secondary attributes** | |
| **Panel label** | **What it does** | **Panel label** | **What it does** |
| Table | Rows | Breaks down the metrics to show details | Columns | Divides the results again for more insights |
| KPI | View by | Breaks down the metrics to show details | Segment by | Divides the results again for more insights |
| **Charts showing trends** | | | | |
| Line, Column, Area | Trend by | Breaks down the metrics on X axis to show trend | Segment by | Divides the results into additional series for more insights |
| **Charts with axes** | | | | |
| Dot, Waterfall | View by | Breaks down the metrics on X axis to show details | Segment by | Divides the results into additional series for more insights |
| Bar | View by | Breaks down the metrics on Y axis to show details | Segment by | Divides the results into additional series for more insights |
| **Charts without axes** | | | | |
| Gauge, Sparkline, Treemap, Bubble, Bubble pack, Picto, Bullet, Radar, Sunburst, Relational, Parallel sets, World cloud | View by | Breaks down the metrics to show details | Segment by | Divides the results again for more insights |

**To add an attribute to a report**

1. Select the **Attributes** tab in the leftmost column.
2. Find the attribute you want to add. The beta report builder gives you several options for finding the right attribute: 
   - Search for a specific attribute using the search bar.
   - Sort the available attributes by clicking **Popular** or **Recently** used.
   - Filter your search results by clicking the filter icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_filter.png)) and selecting the category the attribute belongs to. This category is analogous to the attribute folders in the classic report builder.
3. Click and drag the attribute you want to use into the **Rows** or **Columns** panel. Alternatively, you can click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) to the right of the attribute name to add it.
4. (Optional) If you added a time-based attribute, see [Changing the unit of a time-based attribute](#h_01HGZQZJ3VD1FSMKYYTPXXYWD3).

## Changing the unit of a time-based attribute

In the beta report builder, time-based attributes are always appended with “ - Time” in the **Attributes** panel. In the classic builder, there is a separate instance of the attribute for all available time units (for example, “ - Date,” “ - Month,” “ - Year,” and so on).

When you add a time-based attribute in the beta report builder, the **Date** time unit is automatically applied. However, you can change the applied time unit.

**To change the unit of a time-based attribute**

1. Click the three dots to the right of a time-based attribute that you’ve [added to your report](#h_01GXRAJ90JSPQTVAJBGW5V6MK1).
2. Under **Time**, select the time unit you want. Options include: 
   - Date (default)
   - Month
   - Year
   - Other 
     - Half year
     - Quarter
     - Week of year
     - Year and week
     - Day of month
     - Day of week
     - Hour
     - Minute
     - Second
     - Timestamp 
       ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_beta_report_builder_time_unit.png)

[Copying a time unit to the Filters panel](#h_01GXRAJ90JSPQTVAJBGW5V6MK1:~:text=To%20copy%20an%20attribute%20to%20the%20Filters%20panel) strips the time unit and lets you [filter by a time range](#h_01GXRAJMXXPE8ZKFDATR07VKV1) instead.

## Removing metrics or attributes from a report

If you add a metric or attribute to your report that you no longer want, you can easily remove it.

**To remove a metric or attribute from a report**

1. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) next to the metric or attribute you want to remove and select **Remove**. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_beta_report_builder_removing_metric.png) 
   Alternatively, you can click and drag any metric or attribute to the **Drop here to remove** panel at the bottom of the screen. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_beta_report_builder_drop_here_to_remove.png)

Tip: If you add or remove any metrics or filters and your report doesn’t refresh as expected, you can manually refresh the report by clicking the **Reload** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_reload_icon.png)) in the upper right.

## Filtering a report

You can filter a report by adding an attribute in the **Filters** panel to control which values are included in the report. If you’ve already added an attribute in the **Rows** or **Columns** panel, you can quickly copy it to the **Filters** panel.

**To filter a report**

1. Select the **Attributes** tab in the leftmost column.
2. Find the attribute you want to add. The beta report builder gives you several options for finding the right attribute: 
   - Search for a specific attribute using the search bar.
   - Sort the available attributes by clicking **Popular** or **Recently** used.
   - Filter your search results by clicking the filter icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_filter.png)) and selecting the category the attribute belongs to. This category is analogous to the attribute folders in the classic report builder.
3. Click and drag the attribute you want to use into the **Filters** panel. Alternatively, you can click the plus icon (+) to the right of the attribute name and select **Filters** to add it.
4. In the **Filters** panel, the attribute you just added. Alternatively, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) next to the attribute you just added and select **Edit**. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_beta_report_builder_edit_filter.png)
5. Select the values you want to filter your report by. Or, if you want to exclude certain values, click **Select all** and then deselect the values you don’t want to be included in your report. 

   If you’re filtering by a time attribute, you also have the option to filter by fixed or rolling time ranges:

   - **Fixed range**: Select the static period of time you want to see report results for (for example, November 1 to 30). 
     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_beta_report_builder_fixed_range.png)
   - **Rolling range**: Select the dynamic period of time you want to see report results for (for example, the past 30 days). You can set a rolling range based on hours, days, weeks, months, quarters, semesters, or years. 
     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_beta_report_builder_rolling_range.png)
6. Click **Apply**. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_beta_report_builder_filter_values.png)

The report returns only results where the attribute values you selected are present.

**To copy an attribute to the Filters panel**

1. In the **Rows** or **Columns** panel, click an attribute you’ve added.
2. Click **Copy to Filters**. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_beta_report_builder_copy_to_filters.png) 
   The attribute is added to the **Filters** panel. If you want the attribute to act as a filter but not appear in the report, you can [remove it from the Rows or Columns panel](#h_01GXRAJE7JAKV827KAPASY3DKV).
3. Click the attribute you just added to the **Filters** panel, select the values to include in the report, and click **Apply**.

## Changing a report’s visualization

By default, Explore renders your report results using the **Table** visualization. You can also apply suggested visualizations that are likely to work best for your report’s data, or select a visualization manually.

**To apply a suggested report visualization**

1. In your report, hover your mouse over the **Suggested** bar to the right of the visualization button. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_beta_report_builder_suggested_visualizations.png)
2. Select one of the suggested visualizations to quickly apply it to your report. When you do, the name of the visualization button changes to reflect your currently applied visualization.

**To manually select a report visualization**

1. Click the visualization button above the report results. The name of this button reflects the currently applied visualization. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_beta_report_builder_visualization_selector.png)
2. Select the visualization you want to apply to your report. The option at the top always shows the default visualization, Table. The other available options are sorted into the following categories:
   - **Change over time**: Includes Column, Line, Area, Sparkline, and Waterfall.
   - **Comparison of parts**: Includes Bar, Pie, Funnel, Sunburst, Treemap, Word cloud, Bubble pack, and Bubble plot.
   - **Infographics**: Includes KPI, Gauge, Bullet, and Picto. 
       
     For help choosing a visualization, see [Choosing the right chart type for your data](https://support.zendesk.com/hc/en-us/articles/4408827297946#topic_ih2_vxd_zsb).

Tip: If at any time you want more room to see your report’s visualization, you can collapse either or both of the columns on the left.

## Naming and saving a report

After you’ve added any metrics, attributes, and filters to a report, you need to name it and save it so that your work isn’t lost when you exit the beta report builder.

**To name and save your report**

1. Click the pencil icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_pencil.png)) in the top left.
2. Give your report a descriptive name and click the checkmark.
3. (Optional) Click the star icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_favorite.png)) to add this report to your favorites. Your favorite reports appear in the Favorites section of the Reports library.
4. Click **Save** in the top right.

## Editing a report

The beta report builder is compatible with the reports created in the classic builder and vice versa. This means that you can create a report in one of the builders and continue editing it later in the other one.

Multiple users can access and edit the same report at the same time. Any updates made to a report are applied in the order that they were saved. If user A updates the report that user B is looking at, user B must refresh the page to see user A’s updates.

**To edit a report**

1. In the Reports library, open the report you want to edit.
2. Click **Switch to builder beta** at the bottom of the screen. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_beta_report_builder_switch_to_builder_beta.png)

The beta report builder opens the report for editing.

Tip: Within a report, the **Manage dashboards** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_manage_dashboards_icon.png)) next to the report name shows you whether this report has been added to any dashboards. This is a quick and helpful way to determine whether your updates will affect any published dashboards.

## Adding tags to a report

You can add tags to a report to make them easier to find in the Reports library. For example, you could create tags like:

- **Tickets**: For any reports relating to tickets
- **Articles**: For any reports relating to article views
- **Managers**: For any reports created by the management team

**To add tags to your report**

1. In your report, click the **Manage tags** icon. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_beta_report_builder_manage_tags.png)
2. In the **Manage tags** window:
   1. (Optional) Add a new report tag by clicking **New tag**, entering a tag name, and clicking **Save**.
   2. Select the tags you want to add. If you created a new tag, you still need to select it.
3. Click **Done**.

For more information about managing report tags, see [Organizing your reports with tags](https://support.zendesk.com/hc/en-us/articles/4408829048602#topic_i1m_52h_r4b).

## Changing how often a report reloads

You can choose how often your report reloads as you’re building it. Your options are:

- **Automatic**: The report reloads every time you add a metric, attribute, filter, or other configuration option.
- **Manual**: (Default) The report reloads only when you click the **Run report** button or **Reload** icon. 
 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_beta_report_builder_reload_run_report.png)

**To configure the report reloading behavior**

1. From within the beta report builder, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) in the top-right.
2. Select **Reloading mode**.
3. Select either **Automatic** or **Manual**. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_beta_report_builder_reloading_mode.png)

Your current selection is remembered whenever you open the report builder.

## Cloning a report

You clone a saved report to quickly create a copy of it within the same dataset. You might do this if you want to edit an existing report without modifying the original. You can’t copy reports between datasets.

**To clone a report**

1. In your report, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) in the top-right.
2. Select **Clone**.

   Tip: If you don’t see this option, save your report first.

A copy of the report opens in a new browser tab. By default, the copy is saved and named **Copy of <report name>**.

## Exporting a report

You can export your report’s results to create a CSV, image, PDF, or Excel file of your report.

When you export a report as CSV, only the data from the report is exported. Any formatting you've applied to the report is not exported. When you export a report in Excel format, the report formatting is maintained.

**To export a report**

1. In your report, click the **Export report** icon in the top-right. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_beta_report_builder_export.png)
2. In the **Export report** window, select an export format of **CSV**, **Excel (formatted)**, **PNG**, or **PDF**. See [Choosing an export format](https://support.zendesk.com/hc/en-us/articles/4483481898266#topic_jds_34c_zsb) for more details about each option.
3. Click **Export report**.

## Deleting a report

If you no longer need a report, you can delete it from your Reports library.

**To delete a report**

1. In your report, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) in the top-right.
2. Select **Delete**.

   Tip: If you don’t see this option, your report hasn’t yet been saved and therefore doesn’t need to be deleted. When you navigate away from the report builder, the report is gone.
3. In the confirmation window, click **Delete report**.

## Setting the beta report builder as default

You can set the beta report builder as your default report building experience in Explore. When you do, the beta report builder will open whenever you create or edit a report.

**To set the beta report builder as default**

1. [Open the beta report builder.](#h_01GXRAHWYRSKBEH6ZAW6ANT7K7)
2. In the bottom-right, select **Use beta for all reports**. Explore remembers your selection the next time you create or edit a report. To use the classic builder by default, deselect the checkbox. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_beta_report_builder_use_beta_default.png)
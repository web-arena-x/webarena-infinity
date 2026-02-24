# Working with tables

Source: https://support.zendesk.com/hc/en-us/articles/4408830467866-Working-with-tables

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

Although Explore features many visualizations to help you present your report results, sometimes a simple table is the best way to present information. Tables are a great way to compare data collected over a period of time, for example:

![Explore sample table](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_tables_1.png)

This table was created using the Support: Tickets dataset, using two metrics, **COUNT(Tickets)** and **SUM(Agent replies)**, the column **Ticket created - Quarter**, and the row **Ticket type**. If the report doesn't show a table, use the visualization selector (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_visualization_type.png)) to change the chart format.

Creating a table is just the start. This article shows some of the many customization options that help you present your tables in the form you need.

This article contains the following topics:

- [Changing the look of your table](#topic_bk3_zxc_chb)
- [Sorting data in tables](#topic_jdz_1yc_chb)
- [Working with links in tables](#topic_xnb_dyc_chb)
- [Manipulating table results](#topic_plp_fyc_chb)
- [Copying table data to another application](#topic_nyn_yxk_znb)

## Changing the look of your table

In the chart configuration menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_chart_configuration.png)), the following areas contain customization options which are particularly useful when working with tables:

- [Chart](#topic_ugr_jk5_cv)
- [Columns](#topic_x1q_jk5_cv)
- [Colors](#topic_hd4_jk5_cv)

### Chart

The chart menu helps you to customize the text style of your table. Additionally, further options can be accessed if your table has hyperlinks. For more information about using links in tables, see [Working with links in tables](#topic_xnb_dyc_chb).

Text style options include editing the size, color, and formatting for headers, results, totals, and subtotals. If you add totals or subtotals, you can change their labels and their repetition text.

![Explore chart configuration options](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_tables_2.png)

### Columns

Columns are added to your table every time you add an attribute or metric. You can control how columns appear under **Chart configuration** > **Columns**. The following options are available:

- **Metrics on rows.** Determines whether the report’s metrics are listed together in one column. See [Adding metrics to rows](#topic_dtl_ghs_nv).
- **Allow column sorting.** Determines whether a column can be sorted by clicking its header. Selected by default.
- **Show row number.** Determines whether a row number appears to the left of the row in the table.
- **Allow sort on row number.** Determines whether the row number stays the same when a sort is applied to a metric column. When selected, the original row number is preserved. When deselected, the row number is renumbered to be in numerical order when a metric column is sorted. Available only if **Show row number** is selected.
- **Allow multi-line.** Determines whether a cell’s content can wrap to multiple lines. Appears only if **Fit to content** is not selected. See [Expanding text](#topic_ykh_ghs_nv).
- **Multi-line margin.** Determines the number of pixels between the lines of a cell’s content. Appears only if **Allow multi-line** is selected. See [Expanding text](#topic_ykh_ghs_nv).
- **Discoverable multi-line.** Determines whether a Read more link appears to show the full text of the cell. Appears only if **Allow multi-line** is selected. Works only with the [HTML text interpretation](https://support.zendesk.com/hc/en-us/articles/4408830467866#topic_xnb_dyc_chb). See [Expanding text](#topic_ykh_ghs_nv).
- **Fit to content.** Determines whether the column width is automatically set to the width of the existing content. Selected by default. You must deselect this option to be able to set the **Width** option. Not available if **Allow multi-line** is selected.
- **Responsive columns.** Determines whether the report’s columns automatically scale to the width of the screen. You must deselect this option to be able to set the **Width** option. Not available if **Allow multi-line** is selected.
- **Automatic alignment.** Determines whether a column is left-justified by default.
 You must deselect this option to be able to set the **Alignment** option.
- **Rows height.** Determines the height of the row in pixels. The default is 40. Not available if **Allow multi-line** is selected.
- **Column.** Shows the column number. Not available if the report contains [explosions](https://support.zendesk.com/hc/en-us/articles/4408846733722#topic_b2v_11k_y5).
- **Width.** Determines the width of the column in pixels. See [Setting column width](#topic_gyj_ghs_nv). Not available if the report contains [explosions](https://support.zendesk.com/hc/en-us/articles/4408846733722#topic_b2v_11k_y5).
- **Arrow.** Determines whether a green or red arrow appears in a column to indicate the direction of the result. See [Using arrows to indicate direction of results](#topic_c4c_5sb_nsb). Not available if the report contains [explosions](https://support.zendesk.com/hc/en-us/articles/4408846733722#topic_b2v_11k_y5).
- **Alignment.** Determines whether a column’s content is justified to the left, center, or right. Left-justification is selected by default. Available only if **Fit to content** is deselected. Not available if the report contains [explosions](https://support.zendesk.com/hc/en-us/articles/4408846733722#topic_b2v_11k_y5).
- **Visible.** Determines whether the specified column appears in the table. See [Hiding columns](#topic_gp5_hhs_nv). Not available if the report contains [explosions](https://support.zendesk.com/hc/en-us/articles/4408846733722#topic_b2v_11k_y5).

See the following sections for additional help:

- [Adding metrics to rows](#topic_dtl_ghs_nv)
- [Expanding text](#topic_ykh_ghs_nv)
- [Setting column width](#topic_gyj_ghs_nv)
- [Using arrows to indicate direction of results](#topic_c4c_5sb_nsb)
- [Hiding columns](#topic_gp5_hhs_nv)

#### Adding metrics to rows

By default, metrics are placed in different columns. You can list the metrics together in one column by selecting **Metrics on rows**.

If you've selected **Metrics on rows** or added an attribute on **Rows**, you can select **Show row number** to display the number of rows in your table.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_table_rows.png)

#### Expanding text

If you select a column width that removes a portion of your text, you can expand your text onto additional lines by checking **Allow multi-line**. This option appears only if **Fit to content** is not selected. You can set the spacing between the lines by typing a new number in **Multi-line margin**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/multiline_12.png)

If your text exceeds the selected number of lines, you can check **Discoverable multiline**. Discoverable multiline lets you expand text by clicking a **Read more** link.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/multiline_2.png)

To use discoverable multiline, on the **Chart** panel of the chart configuration menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_chart_configuration.png)), change the **Text interpretation** setting to **HTML**.

#### Setting column width

Columns are fitted to their content and aligned automatically, unless you change these options in **Columns**. To input a new width and alignment for individual columns, you must deselect **Fit to content** and **Automatic alignment**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/grids_5.png)

#### Using arrows to indicate direction of results

You can add red and green arrows to visually indicate trends in your data. In the **Chart configuration** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_chart_configuration.png)) menu > **Columns**, use the **Arrow** check boxes in the table at the bottom to indicate which columns you want to add arrows to. Then [use a result path calculation](https://support.zendesk.com/hc/en-us/articles/4408845886362) to specify what type of calculation the system should use to determine whether to display a red arrow for a downward trend, a green arrow for an upward trend, or a black equal sign for no change.

By default, the result path calculation will replace the original metric in the column. For a way to show both the original metric as well as the result path calculation, see [How do I add a column in my report for the result path calculation?](https://support.zendesk.com/hc/en-us/articles/4408838542874)

In the example report below, the result path calculation calculates the percentage of difference based on the previous period.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_hide_column.png)

#### Hiding columns

You can hide any columns in your table. This keeps your reports looking cleaner by hiding columns that are empty or show unnecessary data. In the **Chart configuration** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_chart_configuration.png)) menu > **Columns**, click the eye icon under the **Visible** header for any column(s) that you don’t want to appear in your report.

![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/explore_articles_with_no_views_3.png)

### Color options

You can customize the colors of your table in **Colors**. You can edit the background, header, rows, totals, subtotals, and table colors. You can choose your own colors or select from Explore's color palettes.

Note: For the **Total background color** formatting to show up on column-based totals, you must be using an advanced total. See [Adding totals to results](https://support.zendesk.com/hc/en-us/articles/4408846476698).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_table_colors.png)

## Sorting data in tables

You can sort the results of your table based on any of its metrics. To do this, click the heading at the top of any metrics column in the table.

You can also control the default sort order for tables in the Result manipulation (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_result_manipulation.png)) > **Sorts** menu.

To turn off the ability to sort, under Chart configuration > **Columns**, deselect **Allow column sorting**.

If you want to display totals at the bottom of the table, choose Result manipulation (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_result_manipulation.png)) > **Totals**, and then choose the setting you want.

Note: If you sort a table that has a totals row, the row containing the totals will be sorted along with the rest of the table data. You can turn off Chart configuration >
**Columns**, deselect **Allow column sorting** to prevent viewers from sorting the table.

## Working with links in tables

If your table contains links, for example to tickets from a ticket ID, more options appear in the chart configuration menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_chart_configuration.png)) to help you control how the links work:

**Text interpretation:** Choose from:

- **Text only:** Links are shows as text, and can't be clicked.
- **Raw:** Links are shown as text, but any embedded HTML text is also displayed.
- **HTML:** The link text is displayed. If it is contained in a valid HTML link, the link will be clickable.

If you chose **HTML**, the following additional options are displayed:

- **Clickable URL:** Enables report viewers to click the link and visit the associated URL.
- **URL alias** and **Image URL alias:** Enables you to enter text that will appear instead of the URL.
- **Display image:** If your URL points to an image, the image will automatically appear when a user hovers over the link. You can disable this by deselecting **Display images**.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_url_image.png)

For some examples of using links in reports, see [Explore recipe: Configuring clickable links to tickets](https://support.zendesk.com/hc/en-us/articles/4408839123226-Explore-recipe-Configuring-clickable-links-to-tickets).

## Manipulating table results

Just like with charts, you can use result manipulations to change the data in your table.
For example, you can apply a default sort order, add totals, restrict the range of results that are presented, and more.

For a full list of result manipulations, see [Calculation type reference](https://support.zendesk.com/hc/en-us/articles/4408831146266-Calculation-types-reference).

Note: You can switch the column and row attributes by clicking the Pivot table button (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Pivot_Table_Icon.png)) to the right of the **Columns** panel. This saves you time by automatically moving your attributes, so you don't have to drag and drop.

## Copying table data to another application

Sometimes, you might want to copy the information in an Explore table to another application for example, Microsoft Excel or Google Sheets. Explore lets you copy and paste data from a table into the application of your choice.

Note: You can't select or copy table headers.

**To copy the contents of a table**

1. Position your mouse pointer over the first table cell you want to copy and hold down the left mouse button.
2. Keeping the mouse button held down, drag the pointer over the cells you want to copy.
3. When you have selected the cells you want to copy, release the left mouse button, then click **Copy**. The contents of the cells you selected are copied to your computer clipboard.
4. Open your application, and paste the contents of the clipboard into it.
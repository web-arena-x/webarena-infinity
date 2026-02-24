# Reporting glossary

Source: https://support.zendesk.com/hc/en-us/articles/4408824134810-Reporting-glossary

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Light, Professional, or Enterprise |

This glossary describes the key concepts and terminology used in Zendesk reporting. If you're
looking for help getting up and running with reporting, see [Getting started with Zendesk Explore](https://support.zendesk.com/hc/en-us/articles/4408831710618-Getting-started-with-Zendesk-Explore).

[A](#topic_ynn_k5n_qz) - [B](#topic_gvs_grk_rz) - [C](#topic_fp5_234_qz)  - [D](#topic_z3m_qxk_rz) - [E](#topic_t14_qvf_sz) - [F](#topic_ec5_xvr_rz) - [G](#topic_dpb_gzr_rz) - H - [I](#topic_nsv_xzj_rz) - J - K - [L](#topic_h5w_ngt_ffc) -
[M](#topic_fxs_k5n_qz) - N - [O](#topic_pb5_3yr_rz) - [P](#topic_e33_z4m_vnb) - [Q](#topic_cgz_nvg_sz) - [R](#topic_kjc_fx4_qz) - [S](#topic_uqc_f34_qz) - [T](#topic_a3g_gvr_rz)  - U - [V](#topic_h4k_bzr_rz) - W - X - Y - Z

## A

### Admin

A user role. Admins have the same permissions as [editors](#topic_qjy_qvf_sz). Additionally, they can edit their own, and others
permissions, and update account settings.

See [Giving users access to Explore](https://support.zendesk.com/hc/en-us/articles/4408836002970-Adding-users-to-Explore).

### Aggregator

Determine how your results are calculated. When you add a [metric](#topic_ak4_d34_qz) to a [report](#topic_abl_4vg_sz), you can select an aggregator. For example the AVG aggregator shows the
average of a metric's results or MED shows the median of a metric's results.

See [Setting a metric's default and visible aggregators](https://support.zendesk.com/hc/en-us/articles/4408834928794).

### Attribute

Attributes slice your results by qualitative data. Attributes represent the *how* in
your data. Examples of attributes include ticket tags, dates, support groups, and ticket
ID. For example, if you are using the [metric](#topic_ak4_d34_qz)
**Full resolution time** and added the attribute **Agent name**, you would see the
full resolution time for each agent.

See [Adding Attributes](https://support.zendesk.com/hc/en-us/articles/4408846733722-Adding-metrics-and-attributes#topic_mwx_hmb_y5).

## B

### Bookmark

A bookmark is an interactive component you can add to your dashboard. When an [admin](#topic_jdj_gwf_sz) or [editor](#topic_qjy_qvf_sz) is applying filters in [Dashboard Builder](#topic_lrv_h5g_sz), they can save the different filtered views as a
bookmark. [Viewers](#topic_xpt_nwf_sz) can then select the
different bookmarks to see each saved filtered state.

See [Saving filtered dashboard states](https://support.zendesk.com/hc/en-us/articles/4408828331290-Adding-dashboard-interactions#topic_kbd_rzg_2v) and [Switching between filtered dashboard versions](../viewing-and-using-dashboards/interacting-with-dashboards.md#topic_fpr_tjy_ry).

## C

### Calculated attribute

A custom attribute you can manually create and add to your data. Calculated attributes
are created in the [Calculations menu](#topic_cjl_byg_sz)
(![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_calculations.png)). Some calculated attributes will require you to write
functions using Explore's formula writing language (see [Formula writing resources](../writing-formulas/formula-writing-resources.md)), while others will
provide you with templates for creating calculations. You can use any metrics or
attributes in your formulas, regardless of if they're currently added to your report or
calculated.

See [Calculation types reference](https://support.zendesk.com/hc/en-us/articles/4408831146266-Calculation-types-reference).

### Calculated metric

A calculated metric is a custom metric you can manually create and add to your data.
Calculated metrics are created in the [Calculations menu](#topic_cjl_byg_sz). Some calculated metrics will require you to write functions
using Explore's formula writing language (see [Formula writing resources](../writing-formulas/formula-writing-resources.md)), while others will
provide you with templates for creating calculations. You can use any metrics or
attributes in your formulas, regardless of if they're currently added to your report or
calculated.

See  [Calculated types reference](https://support.zendesk.com/hc/en-us/articles/4408831146266-Calculation-types-reference#Calculations).

### Calculations menu

The Calculations menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_calculations.png)) is found in the report builder and contains all of the
available [calculated metrics](#topic_fbb_wsk_rz) and [attribute](#topic_xwk_yk3_tz) options. These calculated
elements require you to either use Explore's formula writing language (see [Formula writing resources](../writing-formulas/formula-writing-resources.md)) or pre-built templates.

### Change attribute

A type of [interactive component](#topic_e4g_zzj_rz) you
can add to a dashboard. The change attribute interactive component lets viewers switch an
[attribute](#topic_rdj_s5n_qz) used on a dashboard to a
different attribute from the dataset. This is useful for testing different outcomes,
without having to create multiple, similar reports.

You can add a change attribute component by clicking **Add** on the [dashboard builder](#topic_lrv_h5g_sz) toolbar.

See [Changing metrics and attributes](../viewing-and-using-dashboards/interacting-with-dashboards.md#topic_yxw_v4z_ry) and [Selecting a different attribute](https://support.zendesk.com/hc/en-us/articles/4408828331290-Adding-dashboard-interactions#topic_rcq_jvg_2v).

### Chart configuration menu

The chart configuration menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_chart_configuration.png)) is found in the [report builder](#topic_nxv_4wg_sz), and contains most of the available customization options. You
can customize your chart colors, text, interactions, and additional options. Depending on
the visualization you are using, the options available will differ.

See [Customizing reports](https://support.zendesk.com/hc/en-us/articles/4408839246618-Customizing-queries).

### Color-encoded metric

When adding [metrics](#topic_ak4_d34_qz) to your report,
you can choose to make them color-encoded by clicking the ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_add_color_icon.png) icon. If you add a metric as color-encoded, the difference in
results will be shown in a color gradient. For example if you are using a blue to red
gradient, your highest values will be red, lowest blue, and middle varying shades of
purple.

See [Measuring results by color and size](https://support.zendesk.com/hc/en-us/articles/4408846733722-Adding-metrics-and-attributes#topic_esg_kmb_y5).

### Columns

Like [Rows](#topic_afk_jx4_qz) and [Explosions](#topic_tc1_w3n_sz), when you add an attribute to
Columns your metric results will be sliced by that attribute's values. Unlike Rows and
Explosions, Columns will render the results in *one* chart.

See [Adding metrics and attributes to reports](https://support.zendesk.com/hc/en-us/articles/4408846733722-Adding-metrics-and-attributes).

### Comparison lines

Comparison lines can be enabled as an addition to [datatips](#topic_qkn_g5r_rz). When a user hovers over a data point, a dashed line will
connect the different metrics' results for the data point's attribute value. For some
visualizations, comparison lines will highlight the difference between the data point and
the highest result.

See [Working with datatips](https://support.zendesk.com/hc/en-us/articles/4408838176538-Adding-datatips-to-your-query) .

### Component

Everything you add to a dashboard, excluding tabs, is called a component. This includes
reports, text, filters, and other interactive options. There are two types of component;
static and interactive.

See [Adding and arranging dashboard components](https://support.zendesk.com/hc/en-us/articles/4408838017690-Adding-and-arranging-dashboard-widgets).

#### Static components

This component type cannot be used to change report results or how users interact with
your dashboard. Static components include text, and reports.

See [Adding and arranging dashboard components](https://support.zendesk.com/hc/en-us/articles/4408838017690-Adding-and-arranging-dashboard-widgets).

#### Interactive components

Enable users to set which report results to view and how to view them. Interactive
components include the data and time filters, as well as the change metric and
attribute.

See [Adding interactive dashboard components](https://support.zendesk.com/hc/en-us/articles/4408828331290-Adding-and-using-dashboard-interactions) and
[Interacting with dashboards](https://support.zendesk.com/hc/en-us/articles/4408834682778) .

## D

### Dashboards

Dashboards are customizable locations where you can share multiple reports with several
viewers at the same time. You can break dashboards into different [tabs](#topic_a3g_gvr_rz), add [interactive components](#topic_e4g_zzj_rz), and share [reports](#topic_cgz_nvg_sz).

### Dashboard builder

The dashboard builder is the primary location for creating, customizing, and sharing
dashboards. The dashboard builder is automatically launched whenever an editor or admin
edits a dashboard. You can make all of your changes to a dashboard in Dashboard builder,
then share it with [viewer groups](#topic_hz2_dsg_xz).

See [Creating dashboards](https://support.zendesk.com/hc/en-us/articles/4408831595418).

### Dashboards library

The Dashboards library (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dashboard_icon.png)) lists all of your created and shared [dashboards](#topic_js1_wkh_sz), as well as your pre-built
dashboards for Zendesk products.

If you are an editor or admin, you can share, edit, delete, and duplicate dashboards from
the Dashboards library.

See [Creating dashboards](https://support.zendesk.com/hc/en-us/articles/4408831595418).

### Data filter

A data filter is one type of [dashboard
filter](#topic_lfr_cjn_sz). You can use data filters to restrict your report results to specific
attribute values. For example you can add a data filter for the attribute channel, then
select Chat to only view results from the Chat channel.

Data filters are added as [interactive
components](#topic_e4g_zzj_rz) by clicking **Add** from the dashboard builder toolbar.

See [Adding data filters](https://support.zendesk.com/hc/en-us/articles/4408828331290-Adding-dashboard-interactions#topic_jj5_srg_2v) and [Filtering by attribute values](../viewing-and-using-dashboards/interacting-with-dashboards.md#topic_y5y_qky_ry).

### Datasets

To access your information in Explore, you must choose a dataset. Datasets represent the
different Zendesk data models and contain metrics and attributes relevant to each product.

See [Working with datasets](https://support.zendesk.com/hc/en-us/articles/4408846513050-Creating-a-new-Zendesk-Support-connection).

### Datatips

Datatips (sometimes known as tooltips) can be added to your report to show any additional
information about your results. Datatips appear in a text box whenever a viewer hovers
over a data point. You can enter custom information for the datatip to display or add a
metric as a datatip to show a metric's results only in the text box.

See [Adding datatips to reports](https://support.zendesk.com/hc/en-us/articles/4408838176538-Adding-datatips-to-your-query).

### Date range calculated metric

A date range calculated metric is a type of [calculated metric](#topic_fbb_wsk_rz) that enables you to limit one metric's results to a specific
date range before adding it to your report. You can create a date range calculated metric
in the [Calculations menu](#topic_cjl_byg_sz). A date range
calculated metric limits results before they are processed, which can improve your report
load time.

See [Adding date range calculated metrics](https://support.zendesk.com/hc/en-us/articles/4408827660186-Adding-time-and-date-calculated-metrics#topic_mg4_hx1_fv).

### Decompose

Decompose is one option you can use to drill in to your results. Like [drill in](#topic_lyw_whm_sz), you can decompose your results
by clicking on a data point. Decompose will filter your results by the attribute value
used in the selected data point, then allows you to slice the filtered results by
additional attributes. The attributes you select are added to [Columns](#topic_zyw_frm_sz), and the original attribute of the
selected data point will be added to [Filters](#topic_thh_cjn_sz).

See [Interacting with reports](https://support.zendesk.com/hc/en-us/articles/4408829009818-Interacting-with-queries#topic_uw1_4mz_nv).

### Drill in

Use drill in to refine the results of your Explore report by slicing the result using
extra attributes you choose or by allowing the report viewer to choose from a range of
attributes. For example, you create a report showing all of your tickets by assignee name.
You could configure drill-in to additionally display the status for each ticket or add an
optional attribute for the ticket channel.

See [Using drill in to refine your reports](https://support.zendesk.com/hc/en-us/articles/4408826499482).

### Dual axis

On some chart types, you can add a metric as a dual axis, or secondary axis. When you add
a metric as a dual axis, a second axis will appear on your chart for the metric. This can
be useful if your added metrics contain drastically different scales. You can add a dual
axis metric by clicking the dual axis icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_dual_axis_icon.png)).

See [Adding metrics and attributes to reports](https://support.zendesk.com/hc/en-us/articles/4408846733722-Adding-metrics-and-attributes#topic_tg5_hw3_y5).

## E

### Editor

A user role you can assign to your agents. Editors can create and customize new
dashboards, reports, and datasets. They can also edit shared dashboards, reports, and
datasets. Unlike [admins](#topic_jdj_gwf_sz), editors
cannot set their own permissions. An admin must give editors permissions manually in
**Admin**(![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/manage_icon.png)) > **Editor authorizations** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_permissions_icon.png)).

See [Adding users to Explore](https://support.zendesk.com/hc/en-us/articles/4408836002970-Adding-users-to-Explore).

### Explosions

Explosions are accessed from the [report
builder](#topic_nxv_4wg_sz). Similar to [Rows](#topic_afk_jx4_qz),
Explosions present you with *multiple* charts, each representing a different value
for the added attributes. If you add more than one attribute, Explosions display charts
for every combination.

See [Adding metrics and attributes to reports](https://support.zendesk.com/hc/en-us/articles/4408846733722-Adding-metrics-and-attributes#topic_b2v_11k_y5).

## F

### Filters (report)

When adding [attributes](#topic_rdj_s5n_qz) to your report
one of the available locations is Filters. Filters will allow you to restrict which
results are shown *without* the attribute appearing on your report. You must select
attribute values to include or exclude, or else your results will not be filtered.

See [Adding attributes to filter](https://support.zendesk.com/hc/en-us/articles/4408846733722-Adding-metrics-and-attributes#topic_s2p_xnb_y5).

### Filters (dashboard)

When building a dashboard, you can add filters, so viewers can restrict results to
specific attribute values, date and result ranges, or the highest and lowest results.
Filters are a type of [interactive
component](#topic_e4g_zzj_rz). Dashboard filters include the [data filter](#topic_nfc_5zg_sz), [time
filter](#topic_o5b_k1h_sz), [metric filter](#topic_zs2_4ch_sz), and
[top/bottom filter](#topic_kvg_pdh_sz).

See [Filtering results](https://support.zendesk.com/hc/en-us/articles/4408828331290-Adding-dashboard-interactions#topic_efy_2rg_2v).

### Forecasting

Forecasting is a [result manipulation](#topic_kr5_5wg_sz)
that analyzes patterns in your data to predict future results. Forecasting will show you a
selected number of future date values. If you are looking to test the different outcomes
when results are affected by a specific factor, you should use a [global variable](#topic_yw1_13h_sz).

See [Using forecasting to predict results](../performing-calculations/using-forecasting-to-predict-results.md).

## G

### Group

An alternative to a [set](#topic_cqy_wxr_rz) for
organizing attribute values. You can use groups to aggregate an attribute's values
together under one new value. The new group attribute will show all results for the
aggregated values as the new value.

See [Creating groups](../performing-calculations/organizing-values-by-groups-and-sets.md#topic_epc_gw1_fv).

## I

### Interactive components

When you are building your dashboard, you can add interactive components to allow your
viewers to customize what results to view and how to view them. Interactive components
include filters, change attributes, and more. Interactive components can be added by
clicking the **+** icon in dashboard builder toolbar.

See [Adding dashboard interactivity](https://support.zendesk.com/hc/en-us/articles/4408828331290-Adding-and-using-dashboard-interactions) and [Interacting with dashboards](https://support.zendesk.com/hc/en-us/articles/4408834682778).

### L

#### Legacy dashboards

In November, 2024, Zendesk introduced a new dashboard builder that simplifies how you
can create and share dashboards. All dashboards created before this time are known as
*legacy dashboards*.

## M

### Metric

Metrics are quantifiable results like the number of tickets, the agent wait time in
minutes, the number of replies, first reply time in minutes, and more. A report must
always contain at least one metric. When you add an attribute, your metric results will be
divided into the different attribute values. By default when you add a metric to your
report, the sum of results is calculated. You can change this by selecting a different
[aggregator](#topic_sdr_tvn_qz).

See [Adding metrics](https://support.zendesk.com/hc/en-us/articles/4408846733722-Adding-metrics-and-attributes#topic_ghz_hmb_y5).

### Metric filter

When used in reports, metric filters are a [result manipulation](#topic_kr5_5wg_sz). Metric filters let users filter reports to a specific
numeric range. For example, you can use a metric filter to show only the months where the
number of tickets solved was between 10 and 20.

See [Selecting the metric result range](../performing-calculations/selecting-the-metric-result-range.md) for information
about metric filters on reports.

## O

## Ordered set

An ordered set is a type of [set](#topic_cqy_wxr_rz) that
lets you list attribute values in a custom order. In an ordered set attribute, you can drag
an attributes' values above or below each other to set their position. Ordered sets can be
created in the [Calculations menu](#topic_cjl_byg_sz).

See [Organizing values by ordered sets](../performing-calculations/organizing-values-by-groups-and-sets.md#topic_ssy_cnw_fv) for more
information.

## P

### Preview (dashboards)

When you preview a dashboard, you'll see a view of how the dashboard will appear to
viewers. However, until you initially share or subsequently publish the dashboard, users
won't see your changes. See [Sharing dashboards](https://support.zendesk.com/hc/en-us/articles/4408827282714).

### Publish (dashboards)

When you make changes to a dashboard, dashboard viewers don't automatically see those
changes. To make them available, you must publish the dashboard changes. See [Sharing dashboards](https://support.zendesk.com/hc/en-us/articles/4408827282714).

## Q

## R

### Renamed set

A renamed set is a type of [set](#topic_cqy_wxr_rz) that
allows you to enter new names for your attribute values. You can use renamed sets to
create aliases, shorten results, or replace technical text with more common labels. This
is the only way to rename an attribute's values. Renaming the metric or attribute is
performed separately (see [Editing metric and attribute names](https://support.zendesk.com/hc/en-us/articles/4408821925914-Editing-metric-and-attribute-names)). You can
create renamed sets in the [Calculations
menu](#topic_cjl_byg_sz).

See [Organizing values by renamed sets](../performing-calculations/organizing-values-by-groups-and-sets.md#topic_exv_bnw_fv).

### Reports library

You can view all of your report in the Reports library. You can create a new report or
edit, delete, and duplicate existing reports. You open the library by clicking the (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_query_icon.png)) icon on the left sidebar. Only admins and editors can see the
Reports library.

See [Creating reports](https://support.zendesk.com/hc/en-us/articles/4408821589530-Creating-a-new-query).

### Result manipulation

Result manipulations are simple calculations you can create that do not require you to
enter any formula or create new metrics or attributes. You can add result manipulations to
calculate the percentage difference, total, future results, and more. After you add a
result manipulation it will appear in the list of applied filters, directly above the
**Filters** panel.

You can find result manipulations in the [Result manipulation menu](#topic_utl_vwg_sz) (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_result_manipulation.png)). Result manipulations are applied after your report results
are processed and can only use metrics and attributes already added to your report. If you
want to apply calculations before your report results are processed or use elements not on
the report, create a [calculated metric](#topic_fbb_wsk_rz)
or [attribute](#topic_lzv_nhh_sz) from the [Calculations menu](#topic_cjl_byg_sz).

See [Result manipulation reference](https://support.zendesk.com/hc/en-us/articles/4408831146266-Calculation-types-reference#Result).

### Result metric calculation

The result metric calculation allows you to create calculations on already manipulated
results. The result metric calculation is an available [result manipulation](#topic_kr5_5wg_sz) and requires you to enter functions using
Explore's formula writing language (see [Formula writing resources](../writing-formulas/formula-writing-resources.md)). Unlike calculated
metrics and attributes, the calculation will be applied to the report's current state,
including other result manipulations applied.

See [Performing calculation on manipulated results](https://support.zendesk.com/hc/en-us/articles/4408831485466-Performing-calculations-on-manipulated-results).

### Result path calculation

The result path calculation is the easiest and fastest way to perform important
calculations on your results. The result path calculation is an available [result manipulation](#topic_kr5_5wg_sz) that enables you to
perform the following calculations on your results like percentage, rank, and running
totals.

See [Performing calculations without calculated
metrics](https://support.zendesk.com/hc/en-us/articles/4408845886362-Performing-calculations-without-calculated-metrics).

### Rows

When adding [attributes](#topic_rdj_s5n_qz) to your report
one of the available locations is the **Rows** panel. Rows show you individual charts
for each of your attribute's values. For example, if you add the Ticket Type attribute to
the **Rows** panel, you will see individual charts for Incident, Problem, Question, and
Task. You can flip through each value by using the [Row Selector](#topic_mxm_fx4_qz) to the left of the chart.

See [Adding attributes to Rows](https://support.zendesk.com/hc/en-us/articles/4408846733722-Adding-metrics-and-attributes#topic_egq_xnb_y5).

### Row Selector

When you add an attribute to the [Rows](#topic_afk_jx4_qz)
panel, all of the attribute's values will be shown to the left of the chart in the Row
Selector. You can click on an attribute value to show a chart for that value.

In the [Chart configuration menu](#topic_vjs_yy4_qz) you
can edit various row selector options like type, width, and header color.

See [Adding attributes to Rows](https://support.zendesk.com/hc/en-us/articles/4408846733722-Adding-metrics-and-attributes#topic_egq_xnb_y5).

## S

### Set

In Explore, attribute values are arranged by their default import order. You can modify
this by creating a set. Sets let you arrange your attribute's values in a custom list, or
remove them from the set completely. There are two other types of sets you can create, an
[ordered set](#topic_g2j_kyr_rz) and a [renamed set](#topic_gcr_5yr_rz). You can create sets in the
[Calculations menu](#topic_cjl_byg_sz).

See [Organizing values by groups and sets](../performing-calculations/organizing-values-by-groups-and-sets.md#topic_fsd_gw1_fv).

### Size-encoded metric

When adding [metrics](#topic_ak4_d34_qz) to your report,
you can choose to make them size-encoded by clicking the ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_add_size_icon.png) icon. If you add a metric as size-encoded, the difference in
results will be shown by width or circumference, depending on your visualization. For
example, if you are using a bar chart, values with a higher number of results will have
wider bars, while values with fewer number of results will have narrower bars.

A size-encoded metric cannot be the first or only metric on your report and is not
available for all visualization types.

See [Measuring results by size](https://support.zendesk.com/hc/en-us/articles/4408846733722-Adding-metrics-and-attributes#topic_esg_kmb_y5).

### Sort

When you add data to your report, your results will be displayed in the default order,
such as A-Z. You can change the order your results appear in by using the sort [result manipulation](#topic_kr5_5wg_sz).

You can apply sort in the [Result
manipulation menu](#topic_utl_vwg_sz).

See [Sorting results](../customizing-reports/sorting-results.md).

### Standard calculated attribute

Standard calculated attributes are the most general type of [calculated attributes](#topic_xwk_yk3_tz). Standard calculated
attributes are custom attributes you can create using solely Explore's formula writing
language (see [Formula writing resources](../writing-formulas/formula-writing-resources.md)) and elements from your
dataset. You have complete freedom of what to create, and are not restricted by pre-built
templates as in other attributes.

See [Creating basic calculated attributes](https://support.zendesk.com/hc/en-us/articles/4408824243738-Creating-basic-calculated-metrics-and-attributes#topic_hjf_hdb_hv) .

### Standard calculated metric

Standard calculated metrics are the most general type of [calculated metric](#topic_bp5_nhh_sz). Standard calculated metrics are custom metrics
you can create using solely Explore's formula writing language (see [Formula writing resources](../writing-formulas/formula-writing-resources.md)) and elements from your
dataset. You have complete freedom of what to create, and are not restricted by pre-built
templates as in other calculated metrics.

See [Creating basic calculated metrics](https://support.zendesk.com/hc/en-us/articles/4408824243738-Creating-basic-calculated-metrics-and-attributes#topic_g2g_hdb_hv).

## T

### Tab

When creating a dashboard, you can add tabs to separate your dashboard into different
screens. Tabs allow you to group different reports together, while being able to share one
dashboard. Tabs can be added by clicking the **+**  button on the Dashboard Builder
toolbar. After you have added a tab, you can add another by clicking the **+** next to
the last tab title.

See [Adding and arranging dashboard components](https://support.zendesk.com/hc/en-us/articles/4408838017690-Adding-and-arranging-dashboard-widgets#topic_zcc_5yr_my) and
[Customizing dashboards](https://support.zendesk.com/hc/en-us/articles/4408819770906#topic_n44_whg_2v).

### Time comparison calculated metric

A time comparison calculated metric is a type of [calculated metric](#topic_fbb_wsk_rz) that compares a metric's results to a set dynamic
time period. To create a time comparison calculated metric, you will select a metric and a
time range to represent how long the time range is measuring. A time comparison calculated
metric is dynamic, so as your date changes, the metric will adapt.

See [Adding time and date calculated metrics](https://support.zendesk.com/hc/en-us/articles/4408827660186-Adding-time-and-date-calculated-metrics).

### Time filter

On your dashboards, you can limit results to a specific date ranges using a time filter.
A time filter is a type of [interactive
component](#topic_e4g_zzj_rz) that lets viewers select dates to display. Time filters are useful for
focusing into results or breaking down reports with several values.

To add a time filter, click the **+** icon in dashboard builder, then select Time
filter.

See [Selecting a specific date range](../viewing-and-using-dashboards/interacting-with-dashboards.md#topic_mp2_2gz_ry) and [Adding time filters](https://support.zendesk.com/hc/en-us/articles/4408828331290#topic_qht_srg_2v).

### Top/bottom filter

The top/bottom filter restricts your report to the highest or lowest results. There are
three different types of top/bottom filters in Explore:

- **Top/bottom result manipulation**: This is the most simple option. The filter will
  only be applied after your report results have been processed, and you can only use
  attributes already added to the report.

  See [Creating a top/bottom result
  manipulation](../performing-calculations/creating-a-topbottom-filter.md#topic_n51_qhb_fv).
- **Top/bottom filtered attribute**: Add a top/bottom filtered attribute from the
  [Calculations menu](#topic_cjl_byg_sz). This calculated
  attribute allows you to filter results before they are added to the report frame.

  See
  [Creating a top/bottom filtered
  attribute](../performing-calculations/creating-a-topbottom-filter.md#topic_rmz_phb_fv).
- **Top/bottom dashboard filter**: Enables viewers to limit all reports on a
  dashboard to the highest or lowest results.

  See [Adding a top/bottom filter](https://support.zendesk.com/hc/en-us/articles/4408828331290-Adding-dashboard-interactions#topic_olp_srg_2v) and [Filtering dashboard by top/bottom
  values](../viewing-and-using-dashboards/interacting-with-dashboards.md#topic_znw_qky_ry).

### Trend line

A trend line is similar to the [Dual axis](#topic_itt_rpm_5z) option for
adding metrics. You can create two types of trend lines. If you add a metric as a trend
line by clicking the (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trendline_icon.png)), the metric results will appear as a line separate from the
rest of your report results. If you add trend lines in the [Chart configuration menu](#topic_vjs_yy4_qz), additional lines will be added to your
report, demonstrating the trend of each metric's results.

See [Displaying a metric's result as a trend line](https://support.zendesk.com/hc/en-us/articles/4408846733722-Adding-metrics-and-attributes#topic_tg5_hw3_y5).

## V

### Viewer

Viewer is an available user role you can assign to your agents. Viewers cannot edit or
create dashboards. They are only able to view dashboards shared with them, and cannot
access the [Reports library](#topic_apt_bwg_sz), [Datasets library](#topic_wxb_y1h_sz), and the Admin menu.

See [Add users to Explore](https://support.zendesk.com/hc/en-us/articles/4408836002970-Adding-users-to-Explore).

### Viewer groups

When you share a dashboard, you can select the viewer groups to receive it. Viewer groups
contain Explore users and are automatically imported from Zendesk Support. You must change
a user's group in Zendesk Support to change their viewer group in Explore.

See [Sharing dashboards](https://support.zendesk.com/hc/en-us/articles/4408827282714-Sharing-dashboards).

### Visualization selector

An interaction option you can add to your report. The visualization selector permits
viewers to change the report's chart type on a dashboard. You can choose which chart types
your viewers can select from in the chart configuration menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_chart_configuration.png)) >**Visualization Selector**.

See [Visualization types reference](https://support.zendesk.com/hc/en-us/articles/4408827297946-Visualization-types-reference).

### Visualization type menu

The visualization type menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_visualization_type.png)) is found on the right sidebar of the report builder, Use this
menu to change your report's chart type, or select **Auto** to let Explore choose the
most suitable type.

See [Visualization types reference](https://support.zendesk.com/hc/en-us/articles/4408827297946-Visualization-types-reference).
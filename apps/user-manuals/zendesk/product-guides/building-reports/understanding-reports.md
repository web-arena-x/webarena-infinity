# Understanding reports

Source: https://support.zendesk.com/hc/en-us/articles/4408839341082-Understanding-reports

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

In Explore, data is calculated in reports. This article introduces you to reports, including
what they are, how they’re structured, and how you interact with them in Explore. It also
gives you some resources where you can find more detailed information about working with
reports.

This article contains the following topics:

- [What are reports?](#topic_cd3_k4d_d1b)
- [How reports interact with datasets](#topic_gdb_3sc_zsb)
- [How reports are structured](#topic_kgp_jsc_zsb)
- [Prebuilt Explore reports](#topic_x5k_stw_3jb)
- [Report resources](#topic_thp_shb_x2b)

## What are reports?

Reports are questions you ask about the information stored in your Zendesk account. For
example, you could ask, "What percentage of this month's tickets have a priority of urgent?"
Or, "Which agents have solved the most tickets this month?"

You create reports in the report builder. To learn more about navigating the report
builder, see [Getting started with the Explore interface](https://support.zendesk.com/hc/en-us/articles/4408839345306-Introduction-to-the-Zendesk-Explore-interface).

Reports are stored in the Reports library. You can open the Reports library anytime by
clicking the (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_query_icon.png)) icon on the left sidebar.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_reports_library.png)

## How reports interact with datasets

Before you create a report, you need to define the data source that
contains the business information you want to report on. In Explore, these data sources
are referred to as datasets. These datasets connect you to information about other
Zendesk products, like Support.

Whenever you create a report, you’ll be
prompted to choose the dataset you want. Typically, you’ll use the out-of-the-box
datasets for the product you want to report on. More advanced users might create new
datasets for testing and customization purposes.

For more information on datasets,
see [Understanding Explore datasets](https://support.zendesk.com/hc/en-us/articles/4408839218842).

## How reports are structured

A typical report contains the following pieces:

- **Metrics**: Quantifiable data that represents the things you want to
  measure. A report must always contain at least one metric. Examples: Number of tickets,
  number of updates, number of comments, and more
- **Attributes**: Qualitative data that “slices” your metric into groups
  defined by the values of the attribute. Examples: Dates, user groups, tags, and more

For example, the attribute **Assignee name** lists your different Zendesk Support
assignee names as the values. If your report includes the **Tickets** metric and the
**Assignee name** attribute, Explore displays the number of tickets for each
assignee.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_query_structure_updated.png)

In the report builder, metrics are added in the **Metrics** panel.
Attributes can be added to the **Columns**, **Rows**, **Explosions**, and
**Filters** panels.

For more information on adding metrics and attributes, see
[Adding metrics and attributes to reports](https://support.zendesk.com/hc/en-us/articles/4408846733722-Adding-metrics-and-attributes).

## Prebuilt Explore reports

Explore provides some out-of-the-box reports that help you start reporting on your Zendesk
product data faster. When you first open Explore, you’ll find the following types of
prebuilt reports in the default datasets.

### Sample reports

Sample reports showcase the data available in the default datasets and
act as the foundation for your first custom reports. You can edit these reports to
suit your needs or clone them.

You can identify these reports by the
**[sample]** label in their titles.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_reports_library_sample.png)

### Default dashboard reports

Default dashboard reports are created by the system when one of the
[prebuilt dashboards](https://support.zendesk.com/hc/en-us/articles/4408846844826-Getting-started-with-prebuilt-dashboards) is [cloned](https://support.zendesk.com/hc/en-us/articles/4408821374362). To customize a cloned dashboard, you can edit these
reports or delete any that aren’t needed.

You can identify these reports by the
**[default]** label in their titles.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_reports_library_default.png)

## Report resources

Now that you know the basics about reports, dig deeper with the articles in the
following sections:

- [Building reports](https://support.zendesk.com/hc/en-us/sections/4405298911258)
- [Customizing reports](https://support.zendesk.com/hc/en-us/sections/4405298857498)
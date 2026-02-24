# Setting a metric's default and visible aggregators

Source: https://support.zendesk.com/hc/en-us/articles/4408834928794-Setting-a-metric-s-default-and-visible-aggregators

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

When you create a custom calculated metric, Explore chooses a default aggregator but you can change this to any other aggregator. However, depending on the nature of the metric, you might want to use another default aggregator and deactivate aggregators that are not compatible with the metric.

The best practice is to set the default aggregator and restrict unnecessary aggregators for each newly created metric. Read this article to learn how to set a new default aggregator for a metric and restrict users from selecting other aggregators.

Important: You cannot modify aggregators for pre-built metrics and attributes. You must create an editable copy of the metric or attribute to do this.

To learn more about the different aggregators you can use, and how to use them, see [Changing metric aggregators](https://support.zendesk.com/hc/en-us/articles/4408846897178-Changing-metric-aggregators).

**To edit a metric's default aggregator and visibility**

1. In the **Metrics** panel of the report builder, click **Add**.
2. Expand **Calculated metrics**, then find the custom metric you want to edit.
3. Click the pen icon next to the metric. In the example below, the **Tickets** metric is shown.

   ![Explore editable metric](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_metric_update_1.png)
4. Click the pen icon to open the metric menu. In this menu, you can rename your metrics and update its formula.
5. From the **Options** menu, choose **Edit aggregators**:

   ![Explore metric options menu](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_metric_update_2.png)
6. In the **Default** column, click the circle next to the aggregator you would like to make the default for the metric.
7. In the **Visible** column, click the eye icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_aggregator_visible_icon.png)) next to the aggregators you want to hide from viewers.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_set_default_agg.png)
8. Click **Save**.

The new default aggregator will automatically be applied to that metric. Any metrics you selected to hide will be removed from the metric's aggregators list.
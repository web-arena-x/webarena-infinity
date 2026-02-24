# Choosing metric aggregators

Source: https://support.zendesk.com/hc/en-us/articles/4408846897178-Choosing-metric-aggregators

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

Metric aggregators define how the data queried by a metric is calculated. For example, the
metric **Full resolution time (days)** defaults to showing the median (MED) of the time in
days it took to resolve tickets, but you can change the aggregator to show the average time,
the minimum time, the maximum time and more.

Use this article to learn about the different aggregators you can use, and how to use
them.

Note: For custom metrics, you can change the default aggregator it will use (see [Setting a metric's default and visible aggregators](https://support.zendesk.com/hc/en-us/articles/4408834928794)).

This article contains the following sections:

- [Changing the metric aggregator](#topic_ycz_vxv_ngb)
- [Metric aggregators reference](#topic_mrr_xtv_ngb)
- [Choosing the right metric aggregator](#topic_jkk_m5v_ngb)

## Changing the metric aggregator

**To change the metric aggregator**

1. In the report builder, add a metric to the **Metrics** panel.
2. Click the metric you added.
3. From the list, select a new aggregator.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_change_agg.png)

   The available aggregators will differ depending on the
   metric you choose. Use the [Metric aggregators reference](#topic_mrr_xtv_ngb) to find out
   more about each aggregator.
4. To save the new metric aggregator, click **Apply**.

Tip: You can also select multiple aggregators to use with a metric. When you add
the metric to the **Metrics** panel, click the down arrow next to the metric, and
select the aggregators you want to use.

## Metric aggregators reference

Use this table to learn about the different aggregators and when to use them.

| Aggregator | Description | When to use |
| --- | --- | --- |
| **COUNT** | Counts all values of an attribute. If the same value is recorded more than once, each occurrence is counted. | Used for counting objects like tickets, calls, chats, users, organizations, etc. |
| **D\_COUNT** (distinct count) | Counts the number of different (unique) values. Values recorded more than once are counted only once. | Used for distinct counting objects like tickets, calls, chats, users, organizations, etc. |
| **SUM** | Adds up all numeric values. | Used for database counted, arithmetical operation and time duration metrics like Chat Messages, % Satisfaction Score, Resolution Time. |
| **AVG** (average) | Calculates the arithmetic mean of numeric values. | Used for time duration and database counted metrics like Resolution Time and Chat Messages. |
| **MED** (median) | Identifies the numeric value that separates the higher half of the values from the lower half. | Used for time duration and database counted metrics like Resolution Time and Chat Messages. |
| **MIN** (minimum) | Identifies the lowest numeric value. | Used for time duration and database counted metrics like Resolution Time and Chat Messages. |
| **MAX** (maximum) | Identifies the highest numeric value. | Used for time duration and database counted metrics like Resolution Time and Chat Messages. |
| **VARIANCE**  **STD\_DEV**  (standard deviation) | Measures how far numeric values are spread out from their average value. If it is low the numeric values are close to the average. If it is high the numeric values are spread out. | Used for time duration and database counted metrics like Resolution Time and Chat Messages. |
| **VALUE** | Returns the exact value of a metric without any additional manipulation | Used only in the formula editor when creating [calculated metrics or attributes](https://support.zendesk.com/hc/en-us/articles/4408831146266-Calculation-types-reference#Calculations). Can be applied only to database-level metrics, not to other calculated metrics. See the [VALUE](#topic_jkk_m5v_ngb__section_yy1_pbr_5sb) topic below. |

## Choosing the right metric aggregator

By default, metrics use the most relevant aggregator. In some situations, a different
aggregator might better suit your reporting needs or you might need to decide which
aggregator to use on a new calculated metric. Use the following sections to help you to
decide which metric aggregator to use.

### COUNT and D\_COUNT

Often, you need to count specific objects (tickets, calls, chats, users) or events that
relate to these objects. The metric aggregators you use to count are COUNT and D\_COUNT.

- **COUNT:** Counting all recorded values.
- **DCOUNT:** Counts only unique values.

In many cases, both aggregators will return the same results because the values they are
counting are not repetitive. For example, if you count Ticket IDs in the [Tickets dataset](metrics-and-attributes-for-zendesk-support.md#topic_zlf_slp_4y), the results for both aggregators
are equal, because the ID of each ticket appears only once in this dataset. If you do the
same in the [Updates history dataset](metrics-and-attributes-for-zendesk-support.md#topic_as3_slp_4y), the COUNT aggregator
returns a much higher result, because Ticket ID is recorded for each update.

For more information, see [What is the difference between COUNT and D\_COUNT?](https://support.zendesk.com/hc/en-us/articles/4408843488794)

### SUM

This aggregator is often used for database counters and arithmetical operation metrics,
but it also can be used for duration metrics, for example, to calculate the total time
spent by agents on calls or chats.

The database counted metrics are computed outside of Explore and appear in Explore as
ready to use metrics. They normally measure the number of specific events or objects like
Agent Replies, Assignee Stations, Reopens, or Chat Messages.

The arithmetical operation metrics are calculations created in Explore that perform
numerical operations with existing metrics. For example, SUM should be used for %
Satisfaction Score metric, which is a division of Good Satisfaction Tickets by Rated
Satisfaction Tickets.

### AVG, MED, MIN, MAX, VARIANCE and STD\_DEV

Team efficiency and performance is analyzed in Zendesk using time duration and database
counted metrics aggregated using AVG, MED, MIN, MAX, VARIANCE and STD\_DEV.

AVG and MED play a similar role in understanding the tendency of a metric. If the data
you are comparing is mostly uniform then the AVG aggregator can be used. However, in many
cases, Zendesk data has a high number of outliers, meaning that MED is the best option.
See [Average vs Median](https://support.zendesk.com/hc/en-us/articles/4408839402906) for a closer look at these aggregators.

The MIN and MAX aggregators can be used to identify the highest and lowest metric
outliers.

VARIANCE and STD\_DEV are more advanced analytical aggregators and are rarely used, but
they are helpful in measuring how uniform or spread out the metric values are. If you
never used these aggregators start with STD\_DEV. Standard deviation is expressed in the
same units as average and median aggregators and can be easily compared with them.

### VALUE

The VALUE aggregator is different from other aggregators in that it’s available
only inside of formulas. This means that you can’t set this aggregator from the
**Metrics** panel as described above, but you can use it in the formula editor when
creating a calculated metric or attribute.

The VALUE aggregator returns the exact value of a metric without any additional
manipulation. In other words, it returns exactly what’s stored in the database for the
metric it’s being applied to.

For example, in the following formula, each value of the **First reply time
(min)** metric is evaluated. If that value is less than 5 minutes, the formula returns
TRUE. If that value is greater than 5 minutes, the formula returns FALSE.

```
IF VALUE(First reply time (min))<5       
THEN TRUE     
ELSE FALSE       
END
```

Additionally, it’s important to understand that the VALUE aggregator is
intended to be used inside of formulas as part of a calculated metric or attribute—but
within a formula, it can be applied only to database-level metrics, not to other
calculated metrics.

To see what this means, consider the example above alongside a new example:

```
IF VALUE(Comments)<5 
THEN TRUE
ELSE FALSE
END
```

In the first example, VALUE is being applied to the **First reply time
(min)** metric in the **Support: Tickets** dataset. Looking at the [formula for that metric](metrics-and-attributes-for-zendesk-support.md#topic_sq4_mhq_4y), you’ll see that it’s
simply **(First reply time (min))**. Because there’s no calculation applied to that
metric, it’s considered a database-level metric.

In the second example, VALUE is being applied to the **Comments** metric in the
**Support: Updates history** dataset. The [formula for that metric](metrics-and-attributes-for-zendesk-support.md#topic_krx_1lq_4y) is **IF ([Comment
present] = TRUE) THEN [Update ID] ENDIF**. Because additional calculation is applied
to that metric, it’s considered a calculated metric, although one that’s built into
Explore. This means that VALUE can’t be used with the **Comments** metric inside of a
formula.

For more help, see [Troubleshooting errors in Explore formulas](https://support.zendesk.com/hc/en-us/articles/5870960937498).
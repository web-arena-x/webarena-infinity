# Using average or median aggregators

Source: https://support.zendesk.com/hc/en-us/articles/4408839402906-Using-average-or-median-aggregators

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

It can be tricky to decide which aggregator to use, especially when it comes to average and median. You can always use both of them - one metric to calculate the average and another the median. This lets you see which measure will be most useful in a particular case. However, understanding these statistical terms will make it easier to choose the right aggregator.

*Average* (or *mean*) and *median* play the similar role in understanding the central tendency of a set of numbers. Average has traditionally been a popular measure of a middle point in a set, but it has a disadvantage of being influenced by single values which are much higher or lower than the rest of the values. That’s why the median is a better midpoint measure for cases where a small number of outliers could drastically skew the average.

### Average                                                       Median

| | | |
| --- | --- | --- |
| **Definition** | The average is the arithmetic mean of a set of numbers. | The median is a numeric value that separates the higher half of a set from the lower half. |
| **When is it applicable?** | The mean is used for normal number distributions, which have a low amount of outliers. | The median is generally used to return the central tendency for skewed number distributions. |
| **How is it calculated?** | The average is calculated by adding up all the values and dividing the sum by the total number of values. | The median can be calculated by listing all numbers in ascending order and then locating the number in the centre of that distribution. |
| **Example:** **Normal distribution** | 2, 3, 3, 5, 8, 10, 11 (2+3+3+5+8+10+11)/7= 6 **AVG = 6** | 2, 3, 3, **5**, 8, 10, 11    **MED = 5** |
| **Example: Skewed distribution** | 2, 2, 3, 3, 5, 7, 8, 130 (2+2+3+3+5+7+8+130)/8= 20 **AVG = 20** | 2, 2, 3, **3**, **5**, 7, 8, 130 (3+5)/2=4 **MED = 4** |

## Conclusion

If the data you are comparing is mostly uniform then you can safely use the average (AVG) aggregator. However, if your number set has some outliers then you need to consider using median (MED) to filter out the values that are skewing the results.

## Examples

A few practical examples:

- In order to report on full resolution time, use the Explore **Full Resolution Time (hrs) [MED]** metric. Choose the median operator because a number of tickets have been under investigation for a while and these tickets might skew your report.

- To check the average amount of replies posted by the agents use the **# Replies [MED]** metric because the number of replies is more or less constant.

- To figure out how fast the support team replies to new requests, use the Explore **First Reply Time (hrs) [MED]** metric. Since first reply time is normally constant, create a metric that will count the average first reply time. Additionally, you can filter out proactive tickets, created by agents from the report because they might have a high first reply time.

Note: For changing the metric aggregator in Explore, see [Choosing metric aggregators](choosing-metric-aggregators.md).
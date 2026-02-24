# Editing dates and date ranges

Source: https://support.zendesk.com/hc/en-us/articles/4408828872602-Editing-dates-and-date-ranges

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

You can use date attributes to limit your report results to a selected date range or rolling periods. If you are creating calculated elements, you can use dates in formulas and functions (see [Explore functions reference](https://support.zendesk.com/hc/en-us/articles/4408834558746-Using-dates-in-functions)).

This article contains the following sections:

- [Adding date attributes](#topic_ufr_fnk_w5)
- [Editing date ranges](#Editing)

## Adding dates

In Explore, you can view dates broken down by years, half-years, quarters, months, weeks, weekdays, and days. You can also view a complete date in *yyyy-mm-dd* format with the Date attribute. In addition to dates you can view timestamps broken down by hour, minutes, and seconds or view date and time together with the Date\_Time attribute.

You can add dates just like any other attribute (see [Adding attributes](https://support.zendesk.com/hc/en-us/articles/4408846733722-Adding-metrics-and-attributes#topic_mwx_hmb_y5)). If you do not want to view specific dates, you can exclude them from your results.

**To select or exclude dates from your results**

1. In Report Builder, add your date attribute to any attribute location, for example, the **Columns**, or **Rows** panel.
2. Click the attribute you added to open the attribute properties panel.
3. Click the **Selected** panel to select specific dates to include.
4. Click the **Exclude** panel to select specific dates to exclude.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_select_date.png)

## Editing date ranges

Once you add a date attribute to your report, you can specify the period of time by editing the date range options. You can edit your date ranges by clicking on a date attribute, then selecting **Edit date ranges**.

There are two types of date range options, *Simple* and *Advanced*. In the simple panel, you can choose from a list of named periods or use the custom option to select a unique time period. You can include these date ranges in your results, but not exclude them.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_custom_date.png)

In the advanced panel, you can choose separate beginning and end dates. For each date you can select from a list of named periods, calendar dates, a rolling time period, or all available history. In a rolling period, you can select options, such as seven days in the past or a year in the future.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_advanced_dates.png)

Note: Year-based date ranges always begin on the first of the year, not 365 days in the past or future. For example, "1 year in the past" would begin on January 1 of the current year, "2 years in the past" would begin on January 1 of the previous year, and so on.

You can use date ranges to measure period-on-period results by adding a repeat pattern.
With a repeat pattern, you can compare a data point this year to the exact same point last year. For example if your date range is This year to Today, and today is September 16th, a repeat pattern of one year in the past will compare figures for this year with January 1st to September 16th of last year. Without a repeat pattern, your report would compare the figures for this year and the overall total of last year.

**To add a repeat pattern**

1. Click the **Advanced** panel in Edit date ranges.
2. Select your date range settings.
3. Click the **Add repeat pattern** button.
4. Select your repeat pattern options.
5. Click **Apply**

You can click the **Add repeat pattern** button again to add an additional repeat pattern.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_repeat_pattern.png)

If you do not have a seven day working pattern, you can use a repeat pattern to look at a single day's results.

There are three options for checking your most recent full day's results:

- **Yesterday** will show results for the previous day.
- **Yesterday (working day)** will show either the previous day's results if the current day is between Tuesday through Saturday or the previous Friday if the current day is a Sunday or Monday.
- **Yesterday (workable day)** will show the previous day's results if the current day is between Tuesday and Sunday or the previous Saturday if the current day is Monday.
# Using forecasting to predict results

Source: https://support.zendesk.com/hc/en-us/articles/4408832082970-Using-forecasting-to-predict-results

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

*Forecasting* is a result manipulation that uses patterns in your data to predict future results.

Forecasting uses values from date fields with at least two cycles of data. A cycle of data is a period broken down into multiple values. For example, a year is broken down by month or week. In auto-mode, the forecast will recognize each year as a cycle, so you need two years of data to generate a forecast.

This article contains the following topics:

- [Forecasting basics](#topic_zgd_bzv_b3b)
- [How forecasting works (advanced)](#rob_stack_working_topic)

## Forecasting basics

Use this procedure to learn how to add a forecast to your report.

**To add a forecast to your report**

1. In the report builder, create a time-based report. For example, you could add **COUNT(Tickets)** to the **Metrics** panel and **Ticket created - Year** to the **Columns** panel.

   Note: The **Ticket created - Hour** attribute can't be used for forecasting.
2. Click the result manipulation icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_result_manipulation.png)), then click **Forecast**.
3. In the **Forecast** menu, check **Calculate a forecast on the result**

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_forecast.png)

   The options to configure forecasting are displayed.
4. **Path** determines whether the forecast is based on the columns, or the rows in your chart. Whichever you choose must contain a date-based attribute. The path always contains the date-based attribute for your forecast.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_forecast_path.png)
5. Under **Method**, choose either **Additive trend and multiplicative season** or **Additive trend and additive season**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_forecast_method.png)

   To learn more about the forecasting methods you can use, see [How forecasting works](#rob_stack_working_topic)
   below.
6. Under **Values to predict**, choose one of the following:
   - **Auto:** Let Explore automatically calculate the optimum number of values ahead to predict.
   - **Custom**: Specify the number of values to look ahead. For example, if your attribute is year based, you'll specify the number of years you want to forecast ahead.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_forecast_values.png)
7. Under **Values per cycle**, you can configure the number of data points you include in each cycle. For example, for 12 months of data, you can select 6 values per cycle. If you select **Auto**, Explore calculates the optimum number of values to use.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/forecasting_4.png)
8. When you are finished, click **Apply**.
9. From the visualization menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_visualization_type.png)), choose either a bar, column, area, line, or sparkline chart. Forecast results are not displayed on other chart types.

The forecasted porting of the chart is shown in a different style. For example, the forecasted portion of a line chart is shown as a dotted line, for example:

![Explore forecasting recipe 2](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_forecasting_2.png)

Tip: If you are forecasting based on recurring attributes such as day or month, the data in that attribute is aggregated and will cause forecasting to fail with the error message **forecast\_error\_year\_missing**. You can resolve this error by including a year-based attribute in your report also (because year-based attributes do not recur).

For example, if your report contains the attribute **Ticket created - Month** and you have been collecting data for over a year, then the values in this field are aggregated and you'll see the error message. Add the attribute **Ticket created - Year** also to resolve the error.

## How forecasting works (advanced)

The forecasting method that Explore uses is based on the **Holt winters** model, which is a **triple exponential smoothing**​ that relies on the level, the trend, and the season of a time series.

Explore, uses two sub-models that fit most use-cases, and also take into account seasonal variations.

### The AA method

The AA (Additive trend and Additive season) model is the default because it is the most commonly used, and produces the most realistic results.

Initial values are processed with the formula below:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_aa_1.png)

Then, we can apply the Holt Winters AA model:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_aa_2.png)

### The AM method

The AM (Additive trend and Multiplicative season) model is, in some cases, a time-based trend.

Initial values are processed with the formula below:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_am_1.png)

Then, we can apply the Holt Winters AM model:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_am_2.png)

## Periods per cycle

In the calculation, we also use the value “Periods per cycle”. It is used to determine the length of a season, needed to process seasonal indices. In the formulas above, this value is named “h”.

## Smoothing parameters

Three other parameters must be defined before the processing of the forecast. They correspond to smoothing parameters, called “α” for the level, “β” for the trend, “γ” for the seasonality. In brief, they correspond to a ratio of the importance given to the firsts and lasts values of the time-based series, and will influence the results of each period. Here is an example:

*“The estimated values of alpha, beta and gamma are 0.41, 0.00, and 0.96, respectively.
The value of alpha (0.41) is relatively low, indicating that the estimate of the level at the current time point is based upon both recent observations and some observations in the more distant past. The value of beta is 0.00, indicating that the estimate of the slope b of the trend component is not updated over the time series, and instead is set equal to its initial value. This makes good intuitive sense, as the level changes quite a bit over the time series, but the slope b of the trend component remains roughly the same. In contrast, the value of gamma (0.96) is high, indicating that the estimate of the seasonal component at the current time point is just based upon very recent observations.”*

For the three optimization parameters, there is no official algorithm to find the best ones. This turns into a NP-Complete problem, where the optimization problem is to minimize the mean squared error of the forecasted results, with 0≤α≤1, 0≤β≤1, 0≤γ≤1.

Thus, Explore has its own algorithm to find in a linear time the best three parameters, with an accuracy of 0.01.
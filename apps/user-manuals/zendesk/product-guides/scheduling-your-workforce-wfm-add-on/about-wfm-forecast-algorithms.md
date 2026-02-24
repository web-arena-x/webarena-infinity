# About WFM forecast algorithms

Source: https://support.zendesk.com/hc/en-us/articles/6443365725210-About-WFM-forecast-algorithms

---

A forecasting algorithm is a tool that predicts future outcomes based on past data. It looks for patterns in historical information to estimate what might happen next. These tools use statistical methods or machine learning to improve their accuracy and consider factors like seasonal changes and overall trends to make better predictions.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Workforce Management (WFM) offers various forecasting algorithms to optimize your customer support operations. You can use statistical methods for short-term predictions, machine learning like Prophet and XGBoost for complex data patterns, and AI algorithms such as NeuralProphet and LSTM for advanced time-series forecasting. Choose the best fit based on your historical data, trends, and specific needs.

A forecasting algorithm is a tool that predicts future outcomes based on past data. It looks
for patterns in historical information to estimate what might happen next. These tools use
statistical methods or machine learning to improve their accuracy and consider factors like
seasonal changes and overall trends to make better predictions.

In Zendesk Workforce management (WFM), the best forecasting algorithm for each workstream is
automatically selected by analyzing your historical data and testing all algorithms. This is
to determine which will perform best for the specific workstream.

However, you can overwrite the automatic algorithm selection and choose any algorithm Zendesk
WFM offers.

This article contains the following topics:

- [Understanding statistical
  algorithms](#topic_csg_pcj_fgc)
- [Understanding machine learning
  algorithms](#topic_c2j_fdj_fgc)
- [Understanding AI algorithms](#topic_hm4_f2j_fgc)

Related articles

- [Understanding WFM forecasting](https://support.zendesk.com/hc/en-us/articles/9858048119194)

## Understanding statistical algorithms

For both of the [eight-weeks average](#topic_mqp_rnk_fgc)
and the [eight-weeks average with
momentum](#topic_cmj_tnk_fgc) algorithms, you'll need to frequently recalculate the forecast to get the
most accurate prediction.

### Eight-weeks average

The eight-weeks average forecasting algorithm is straightforward, reliable, and popular.
Use this algorithm to describe running averages. This algorithm takes the averages from
the past eight weeks (or less, if eight weeks is not available) to generate forecasts for
the next 12 weeks.

Note: A minimum of two weeks of historical data is required. Four weeks will then be
forecasted, and the remaining eight weeks will repeat the forecast.

This algorithm looks at the previous eight weeks, period by period. The periods are then
averaged to produce a forecasted value.

For example, to forecast the volume for a specific time period, such as Wednesday from
9:00 am to 9:15 am, Zendesk WFM calculates the average volume of the same time periods
from the previous eight Wednesdays to produce the forecasted value.

**When to use it:**

- If you have limited historical data
- Short term forecasts (up to 12 weeks)
- No large upward or downward trends in volume that can be observed over the past
  weeks
- Simplicity and predictability of results

### Eight-weeks average with momentum

This algorithm is similar to the [eight-weeks average algorithm](#topic_mqp_rnk_fgc). It differs from that algorithm by replicating the
general upwards or downwards trends in your volume over the previous eight weeks and
adjusts the forecast to match.

Similar to the eight-weeks average, this algorithm looks at the previous eight weeks and
then averages those periods to produce the forecasted value. After the average value is
defined, Zendesk WFM reviews how the volume is distributed throughout weekdays and hours
of the day. For instance, if data typically shows higher or lower values during this
specific time of day compared to the overall average. Then, based on the defined deviation
from the average, the forecasted value is adjusted.

For instance, use the same Wednesday 9:00 am to 9:15 am period as an example. Using the
eight-weeks average with momentum algorithm, Zendesk WFM calculates the average volume
from the same time period on the previous eight Wednesdays. It then compares this specific
interval to other intervals on Wednesdays. If it typically has 10% lower volume than other
intervals, Zendesk WFM reduces the average volume of the 9:00 am to 9:15 am periods on
Wednesdays by 10% to adjust the forecasted value.

**When to use it**

- If you have limited historical data
- Short term forecasts (up to 12 weeks)
- Have large upward or downward trends in volume that can be observed over the past
  eight weeks

## Understanding machine learning algorithms

### Prophet daily and historical patterns

[Prophet](https://research.facebook.com/blog/2017/2/prophet-forecasting-at-scale/) is an open source algorithm developed by
Meta. It's built for forecasting time series data based on an additive model where
non-linear trends are fit with yearly, weekly, and daily seasonality.

**How it works**

It works best with time series that have strong seasonal effects and several seasons of
historical data. Prophet is robust to missing data and shifts in the trend. It typically
handles outliers well. Not all forecasting problems can be solved by the same procedure.
Prophet is optimized for the business forecasting tasks that Meta encounters.

Zendesk WFM uses Prophet to forecast daily values and then uses historical averages for
the last four weeks to distribute forecasted daily values and generate an intraday
forecast.

**When to use it:**

- At least a few months and preferably a year of historical data
- Strong multiple “human-scale” seasonalities: day of week and time of year
- A reasonable number of missing observations or large outliers are detected in your
  data
- Historical trends that change. For example, due to product launches.
- Trends that are non-linear growth curves, where a trend hits a natural limit or
  saturates

### XGBoost

eXtreme Gradient Boost (XGBoost) is a gradient boosting algorithm that can be used for
solving different machine learning (ML) issues, such as classification and regression.
It's one of the most used ML algorithms for forecasting.

**How it works**

A boosting algorithm is an ensemble algorithm of decision trees that increases the
complexity of models that suffer from high bias. That means it's constructed of multiple
learning algorithms to achieve better results. XGBoost is an implementation of Gradient
Boosting algorithm under the open-source software library. It's focused on the computation
speed and model performance. This library has the ability to distribute model training to
generate faster, more accurate results.

**When to use it**

- At least a few months and preferably a year of historical data
- If there is not much data (zero data for most of the historical period)
- If the data has a lot of existing outliers, such as special events or unexpected
  peaks, because this model is robust and less sensitive to outliers

### LightGBM

Light Gradient-Boosting Machine (LightGBM) is a gradient boosting framework developed by
Microsoft that can be used for solving different machine learning (ML) issues, such as
ranking, classification, and regression.

**How it works**

LightGBM is a boosting algorithm and works similarly to [XGBoost](#topic_ewv_p4k_fgc). These algorithms differ in how they "grow the trees" -
XGBoost uses level-wise (horizontal) growth, while LightGBM uses leaf-wise (vertical)
growth. This difference in certain scenarios makes LightGBM a faster and more accurate
choice compared to XGBoost. However, it depends on a specific use case.

**When to use it**

- At least a few months and preferably a year of historical data
- If data has complex non-linear patterns
- Large-scale data
- If performance is more important

## Understanding AI algorithms

### NeuralProphet daily and historical patterns

NeuralProphet bridges the gap between traditional time-series models and deep learning
methods. It is open source, based on [PyTorch](https://pytorch.org/), and builds on [Meta Prophet](https://research.facebook.com/blog/2017/2/prophet-forecasting-at-scale/). The biggest upgrade related to
Prophet is the possibility for extensions such as new features, new algorithms, etc.

NeuralProphet uses a fusion of classic components and neural networks to produce highly
accurate forecasts:

- Provides automatic hyperparameter selection
- All modules are trained with mini-batch stochastic gradient descent (SGD)
- Includes all the components from the original Prophet model (trend, seasonality,
  recurring events and regressors)

NeuralProphet computes predictions faster than the original Meta Prophet while providing
additional functionality. Zendesk WFM uses a similar approach: it employs Prophet to
forecast daily values with NeuralProphet and leverages historical patterns for intraday
forecasting.

**When to use it:**

- At least a few months and preferably a year of historical data
- Strong multiple “human-scale” seasonalities: day of week and time of year
- Important holidays (or seasonalities) that occur at irregular intervals that are known
  in advance (for example, the Super Bowl)
- A reasonable number of missing observations or large outliers
- Historical trend that changes due to product launches, for example
- Trends that are non-linear growth curves, where a trend hits a natural limit or
  saturates

### Long Short-Term Memory (LSTM) Neural Network

Long Short-Term Memory (LSTM) Neural Network is one of the most advanced models for
forecasting time series. Its ability to learn long-term sequences of observations makes it
a popular approach to modern forecasting.

It's an artificial recurrent neural network (RNN) used in the field of deep learning. A
common LSTM unit is composed of a cell, an input gate, an output gate and a forget gate.
The cell remembers values over arbitrary time intervals and the three gates regulate the
flow of information into and out of the cell.

The LSTM is capable of capturing the patterns of both long term seasonalities, such as a
yearly pattern, and short term seasonalities, such as weekly patterns. It works well with
outstanding events. Such events impact demand on the day when it's happening, as well as
the days before and after the event is happening. The different gates inside LSTM boost
its capability for capturing non-linear relationships for forecasting.

For example, people may book more days of accommodation in order to attend a sports
event. The LSTM has the ability to triage the impact patterns from different categories of
events.

Zendesk WFM has several LSTM models trained on different frequencies of the data:

- 15 min - Raw data that is used for training and, as a result, gets intraday forecasts
  immediately.
- Hourly - Data aggregated on an hourly level is used for training the model, which then
  produces a forecast on an hourly level.
- Daily - Data aggregated on daily level is used for training the model. The model then
  produces a daily forecast and applies historical patterns to get an intraday
  forecast.

**When to use it:**

- A good amount of historical data, preferably over a year
- Medium to high volume workstreams
- Working hours that usually don't have periods with no inbound volume
- Need to account for strong seasonality patterns as well as some outstanding repeated
  events
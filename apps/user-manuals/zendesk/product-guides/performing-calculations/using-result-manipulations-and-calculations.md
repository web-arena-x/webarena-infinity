# Using result manipulations and calculations

Source: https://support.zendesk.com/hc/en-us/articles/4408831146266-Using-result-manipulations-and-calculations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

In Explore, you can perform calculations on your results using one or both of the
following methods:

- **Result manipulations:** Perform calculations on metrics and attributes
  you've already added to a report to change the results.
- **Calculated metrics and attributes:** Create entirely new metrics and
  attributes based on the built in metrics and attributes, formulas, and
  values.

This article contains the following topics:

- [Result manipulations](#topic_ygm_fc2_zsb)
- [Calculated metrics and
  attributes](#topic_m4c_hc2_zsb)

## Result manipulations

In the report builder, you use the **Result manipulation** menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_result_manipulation.png)) to create simple calculations based on
metrics or attributes you've already added to a report.

Examples of a result manipulation include calculating percentage differences, sorting
or totaling your results, forecasting, and more. Result manipulations are processed
after your report runs.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_gsg_result_manipulation_menu.png)

Result manipulations are applied after your metrics and attributes are processed in
the report, and they will appear in the **Filters** list below your report. If
you add several result manipulations, the order you apply the result manipulations
might affect the outcome of your result. See [Setting the order for your result manipulations](https://support.zendesk.com/hc/en-us/articles/4408822111770-Setting-the-order-for-your-result-manipulations)for more information.

The available result manipulations include:

- [Sort results](https://support.zendesk.com/hc/en-us/articles/4408839379482)
- [Totals](https://support.zendesk.com/hc/en-us/articles/4408846476698-Adding-totals)
- [Top/bottom filter](creating-a-topbottom-filter.md#topic_n51_qhb_fv)
- [Metric filter](selecting-the-metric-result-range.md)
- [Result path calculation](https://support.zendesk.com/hc/en-us/articles/4408845886362-Performing-calculations-without-calculated-metrics)
- [Result metric calculation](https://support.zendesk.com/hc/en-us/articles/4408831485466-Performing-calculations-on-manipulated-results)
- [Hide part of your result](https://support.zendesk.com/hc/en-us/articles/4408828776090-Hiding-rows-and-columns)
- [Forecast](using-forecasting-to-predict-results.md)
- [Order of result manipulations](https://support.zendesk.com/hc/en-us/articles/4408822111770-Setting-the-order-for-your-result-manipulations)
- [SQL options](https://support.zendesk.com/hc/en-us/articles/6467453826202)

## Calculated metrics and attributes

In the report builder, you create custom calculated metrics and attributes in
the **Calculations** menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_calculations.png)).

Sometimes the prebuilt metrics and attributes supplied with Explore might be
insufficient for your needs. In this case, try creating calculated metrics
and calculated attributes to get the results you need. You can use
calculated metrics and attributes to create unchanging metric results (such
as a per-hour cost), rename attribute values, create completely custom new
metrics and attributes, and more.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_gsg_calculation_engine.png)

Similar to the prebuilt metrics and attributes, you add calculated metrics
and attributes to your report by selecting them from the one of the metric
or attribute locations (see [Creating reports](https://support.zendesk.com/hc/en-us/articles/4408821589530)).

When you add a calculated metric or attribute to your report first, it
filters your results before they're processed. As a result, calculated
metrics and attributes can help speed up loading time for large datasets by
filtering results before they're processed.

The available calculated metrics and attributes include:

**Metrics**

- [Standard calculated metric](https://support.zendesk.com/hc/en-us/articles/4408824243738-Creating-basic-calculated-metrics-and-attributes#topic_g2g_hdb_hv)
- [Date range calculated metric](https://support.zendesk.com/hc/en-us/articles/4408827660186#topic_mg4_hx1_fv)
- [Time comparison calculated
  metric](https://support.zendesk.com/hc/en-us/articles/4408827660186#topic_g2p_hx1_fv)

**Attributes**

- [Standard calculated attribute](https://support.zendesk.com/hc/en-us/articles/4408824243738-Creating-basic-calculated-metrics-and-attributes#topic_hjf_hdb_hv)
- [Group](organizing-values-by-groups-and-sets.md#topic_epc_gw1_fv)
- [Set](organizing-values-by-groups-and-sets.md#topic_fsd_gw1_fv)
- [Ordered set](organizing-values-by-groups-and-sets.md#topic_ssy_cnw_fv)
- [Renamed set](organizing-values-by-groups-and-sets.md#topic_exv_bnw_fv)
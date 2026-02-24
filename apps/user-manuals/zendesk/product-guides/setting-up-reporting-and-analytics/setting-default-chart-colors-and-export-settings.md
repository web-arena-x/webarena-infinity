# Setting default chart colors and export settings

Source: https://support.zendesk.com/hc/en-us/articles/6456984924442-Setting-default-chart-colors-and-export-settings

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

In Explore, admins can set default chart colors and export settings that apply across the
entire account. This helps you maintain consistency across the charts and exports
generated from your account.

This article contains the following topics:

- [Setting default chart colors](#topic_wwl_5pv_qzb)
- [Setting export separators and decimal precision](#topic_rxp_vpv_qzb)

Related articles:

- [Setting the start of the week for reports and
  filters](https://support.zendesk.com/hc/en-us/articles/4418307079322)

Note: Prior to July 15, 2024, it was possible to set any special
characters as column separators in CSV exports, but now only [certain characters](#topic_rxp_vpv_qzb) are allowed.
If you save any settings on the Formatting tab of the Settings page (even settings
unrelated to exports), the new export settings are enforced. This may break
automated export workflows you have created that rely on certain special
characters.

## Setting default chart colors

Admins can set the default chart colors and color coding that apply when new reports
are created in Explore.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_admin_settings_formatting_chart_colors.png)

**To set default chart colors**

1. In Explore, click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_admin_icon.png)) in the left sidebar.
2. Select the **Formatting** tab.
3. Under **Chart colors**, select the colors for the following options:
   - **Colors**: Colors applied to chart elements. Applied in the order
     shown. For example, if you used the color scheme from the image above
     and added two metrics to a report, the chart would show the first metric
     in red and the second in teal.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_account_info_default_colors_in_graph.png)
   - **Color scale**: Colors applied when a [metric is color-encoded](https://support.zendesk.com/hc/en-us/articles/4408846733722#topic_esg_kmb_y5) in a
     report. For example, if you used the color scheme from the image above
     and added a color-encoded metric, the results would be colored as shown
     in the screenshot below.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_color_encoded_metric.png)
4. Click **Save**.

## Setting export separators and decimal precision

Admins can set the separator characters and decimal precision that apply to data
exported from Explore to a CSV file.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/explore_admin_settings_formatting_csv_exports.png)

**To set export separators and decimal precision**

1. In Explore, click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_admin_icon.png)) in the left sidebar.
2. Select the **Formatting** tab.
3. Under **CSV exports**, set the following separators and precision that should
   apply when data is exported to a CSV file:
   - **Columns separator**: Select the character that should act as a
     column separator. Options include **comma**, **dot**,
     **semicolon**, **tab**, and **pipe**.
   - **Decimal separator**: Select the character that should act as a
     decimal separator. Options include **dot** and **comma**.
   - **Decimal precision**: Select the number of decimal places that data
     should have. Options include **0–5**.
   - **Thousands separator**: Select the character that should act as a
     thousands-place separator. Options include **nothing**, **space**,
     **comma**, and **dot**.
4. Click **Save**.
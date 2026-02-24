# Importing historical volume for WFM forecasts

Source: https://support.zendesk.com/hc/en-us/articles/6443365713946-Importing-historical-volume-for-WFM-forecasts

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Importing historical volume data for WFM forecasts allows you to enhance forecasting accuracy by using your own data. You need at least two weeks of data, but two years is recommended. Ensure your data is in UTC, follows the template format, and includes 15-minute intervals. After preparing your CSV file, upload it and save your settings to improve your forecast precision.

While setting up your WFM forecasts and [selecting the historical volume period in Zendesk Workforce management (WFM)](https://support.zendesk.com/hc/en-us/articles/6443407875354-Setting-up-and-reading-WFM-forecasts#topic_ub5_whd_tzb), you have the option to import your historical volume into your forecast.

Related articles

- [Setting up WFM forecasting](https://support.zendesk.com/hc/en-us/articles/6443407875354)

## Importing historical volume

For imports, a minimum of two weeks of data is required for forecasting. For best results, import two years worth of data.

Note: After the data is uploaded, Zendesk WFM only uses the available data in your import and will not combine it with your historical Zendesk data. You can always switch back to using Zendesk data.

**To import historical volume**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_forecasts_icon.png)
   **Forecast** in the navigation bar, then select **Forecast**.
2. Select a workstream.
3. In the **Historical volume** panel, select use **Imported data** as your Data source.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_forecast_uploaded_historical_data.png)
4. Download and use the **Import volume template**. For best accuracy, import 2 years of data.
5. Open the spreadsheet and edit it to include your own historical data.

   To avoid errors when uploading your CSV file, ensure the following aspects are taken into consideration:

   - The first row of the example must be deleted
   - The data's timezone must be UTC
   - Ensure that no special characters are used that are not on the template spreadsheet.
   - Data must be uploaded with 15-minute increments starting at 00:00:00 on the first day. Entries like 09:10 will result in errors.
   - Fill in any 15-minute period without volume with zeros in the CSV file, as intervals cannot be skipped (e.g., 00:00-00:15-00:30-00:45-01:00).
   - Check that ' : ' has not been accidentally replaced with ' ; '.
   - Check that ' . ' has not been accidentally replaced with ' , '.
   - Ensure that the days are in chronological order.
6. Upload your new historical volume CSV file.
7. Click **Save**.
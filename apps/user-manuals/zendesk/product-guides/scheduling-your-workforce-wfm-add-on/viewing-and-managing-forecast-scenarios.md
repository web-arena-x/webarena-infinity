# Viewing and managing forecast scenarios

Source: https://support.zendesk.com/hc/en-us/articles/9940824842394-Viewing-and-managing-forecast-scenarios

---

Forecasting in Zendesk Workforce Management (WFM) estimates future contact volumes and staffing needs by analyzing historical data and applying advanced algorithms. This ensures the appropriate number of agents are scheduled at the right times, allowing you to optimize resources efficiency and consistently achieve service objectives.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Workforce Management (WFM) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Forecast scenarios, available in early access, let you create and manage multiple forecasts for different workstreams. Adjust forecasts for unique events like marketing campaigns or holidays to ensure accurate planning. You can test various algorithms and settings, activate scenarios, and manage historical data to optimize staffing and resource allocation. Admins and authorized team members can create, edit, and activate these scenarios.

Forecasting in Zendesk Workforce Management (WFM) estimates future contact volumes and staffing needs by analyzing historical data and applying advanced algorithms. This ensures the appropriate number of agents are scheduled at the right times, allowing you to optimize resources efficiency and consistently achieve service objectives.

Some events, such as marketing campaigns, product launches, seasonal holidays, and service issues, often cause significant, non-typical increases or decreases in expected volumes. Forecasts can be adjusted to account for these unique events, ensuring accurate planning and resource allocation.

To manage these variations, forecast scenarios allow [admins and team members in custom roles with permission](https://support.zendesk.com/hc/en-us/articles/6443374440090) to create and save multiple forecast versions for each workstream. You can test different algorithms and settings to determine the ideal scenario for your needs before [activating a forecast for a workstream](https://support.zendesk.com/hc/en-us/articles/9940054229402).

Each workstream can have only one active system created forecast scenario and one active imported forecast scenario.

This article contains the following topics:

- [Viewing and managing forecast scenarios](#topic_awg_gt1_hhc)
- [Creating new forecast scenarios](#topic_xgw_qkp_c3c)
- [Importing forecast scenarios (EAP)](#topic_g3r_ntl_33c)
- [Duplicating forecast scenarios](#topic_mgq_blp_c3c)
- [Activating forecast scenarios](#topic_bgk_mlp_c3c)
- [Renaming forecast scenarios](#topic_wwl_tlp_c3c)
- [Deleting forecast scenarios](#topic_zkf_zlp_c3c)

Related articles:

- [Viewing your active forecasts](https://support.zendesk.com/hc/en-us/articles/9940054229402)
- [Setting up WFM forecasting](https://support.zendesk.com/hc/en-us/articles/6443407875354)
- [Understanding WFM forecasting](https://support.zendesk.com/hc/en-us/articles/9858048119194)

## Viewing and managing forecast scenarios

You must be a [WFM admin or have permission](https://support.zendesk.com/hc/en-us/articles/6443374440090) to access the Forecast scenarios page.

**To view and manage forecast scenarios**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_forecasts_icon.png)
   **Forecasting** in the navigation bar, then select **Forecast scenarios**.
2. Under Workstreams, use the drop-down menu to select a workstream.
3. Click the scenario you want to view.

   When a selected forecast is available, it's displayed under [Inbound volume](https://support.zendesk.com/hc/en-us/articles/9858048119194#topic_qq1_cts_tfc).

   Based on the forecast, Zendesk WFM also calculates the staff count needed to handle the expected workload under [Required staffing](https://support.zendesk.com/hc/en-us/articles/9858048119194#topic_qrb_mgf_bhc).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_forecast_scenarios.png)

   By default, a table for your current week displays.
   However, you can take any of the following actions:

   - Under View, use the drop-down menu to select daily, weekly, monthly, or yearly views of the incoming workload and required staffing for the workstream scenario.
   - Under Date range, use the date picker to select a specific date or date range.
   - Under Layout, select either a table or chart view.
   - Click the download icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/DownloadIcon.png)) to export your selected scenario data to a CSV file.
   - [Edit and manage your forecast scenario settings](#topic_vsp_fw1_hhc).
   - Forecast settings trigger the calculation process automatically when saved. However, if you want to consider additional historical data, you can force an update by clicking Recalculate (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_forecast_recalculate.png)).

     Note: Recalculation is available only when the workstream's [historical volume](https://support.zendesk.com/hc/en-us/articles/6443407875354#topic_ub5_whd_tzb) uses Zendesk data and not imported data.
   - Click the reset icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_reset_to_default.png)) to restore your settings to the default values.
   - Click the plus icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_plus_icon.png)) next to Forecast scenarios to create a new forecast scenario.
   - Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) next to a scenario to activate, rename, duplicate, or delete it. Once you’ve [created new forecast scenarios](#topic_xgw_qkp_c3c) or [duplicated existing ones](#topic_mgq_blp_c3c), you can [set a different scenario as active](#topic_bgk_mlp_c3c).
     An active forecast scenario means that [scheduling](https://support.zendesk.com/hc/en-us/articles/6443348279194) and [reporting](https://support.zendesk.com/hc/en-us/articles/8920679615258) consider that forecast. A workstream’s default scenario is set to active and is visible in the [Active forecast page](https://support.zendesk.com/hc/en-us/articles/9940054229402).
   - Use the forecast scenario panels on the right side to:
     - [Set the historical volume for your workstream](https://support.zendesk.com/hc/en-us/articles/6443407875354#topic_ub5_whd_tzb). Decide which historical data you want to include or exclude in your forecast calculation.
     - [Choose a forecasting algorithm](https://support.zendesk.com/hc/en-us/articles/6443407875354#topic_fy3_4ct_tfc). The best forecasting algorithm for each workstream is automatically selected by analyzing your historical data and testing all algorithms. This is to determine which will perform best for the specific workstream. However, you can overwrite the automatic algorithm selection and choose any algorithm Zendesk WFM offers. See [About WFM forecast algorithms](https://support.zendesk.com/hc/en-us/articles/6443365725210) to learn more.
     - [Make volume adjustments](https://support.zendesk.com/hc/en-us/articles/6443407875354#topic_kgl_ymt_xbc) to account for any unique events that you expect will drive up the number of contacts you'll receive (for example, marketing campaigns or scheduled maintenance windows).
     - [Exclude historical inbound volume outliers](https://support.zendesk.com/hc/en-us/articles/6443407875354#topic_jjz_h4t_xbc)
       to help make your forecast more precise.
     - Configure [staffing parameters](https://support.zendesk.com/hc/en-us/articles/6443407875354#topic_ptn_jpt_xbc) to calculate how many agents you should expect to schedule to meet your staffing targets and projections.

## Creating new forecast scenarios

All your [workstreams](https://support.zendesk.com/hc/en-us/articles/6443314489242) have one default forecast scenario that can’t be deleted. However, you can create new forecast scenarios or duplicate existing ones, then activate a different scenario.

You must be a [WFM admin or have permission](https://support.zendesk.com/hc/en-us/articles/6443374440090) to create new forecast scenarios.

**To create a new forecast scenario**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_forecasts_icon.png)
   **Forecasting** in the navigation bar, then select **Forecast scenarios**.
2. Click the plus icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_plus_icon.png)) next to Forecast scenarios, , then click **Create scenario**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_create_scenario.png)
3. Enter a name for your new scenario and click **Create scenario**.
4. [Set up your forecast scenario](https://support.zendesk.com/hc/en-us/articles/6443407875354).

## Importing forecast scenarios (EAP)

Importing forecast scenarios is currently in an Early Access Program (EAP). You can [sign up for the EAP here](https://docs.google.com/forms/d/e/1FAIpQLSeRQetLcRD25rsNQh2F7krVzkjs1eYznJaX6YiM5LRHJaJDoA/viewform).

If you’ve previously used an Excel spreadsheet or a third‑party tool to forecast your inbound volume and required staffing, you can import it into your Zendesk WFM account using a CSV file.

Imported forecast data ranges replace existing forecast data when it exists or are added to it when it does not.

You must be a [WFM admin or have permission](https://support.zendesk.com/hc/en-us/articles/6443374440090) to import a forecast scenario.

**To import a forecast scenario**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_forecasts_icon.png)
   **Forecasting** in the navigation bar, then select **Forecast scenarios**.
2. Click the plus icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_plus_icon.png)) next to Forecast scenarios, then click **Import scenario**.
3. Enter a name for your scenario.
4. Under Import,select whether you want to import your **Forecasted inbound volume** only or both your **Forecasted inbound volume and required staffing**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_import_scenario.png)
5. (Optional) If you selected Forecasted inbound volume, download and use the **Import forecasted inbound volume template**. You can import up to one year of data counting from today.
6. (Optional) If you selected Forecasted inbound volume and required staffing, download and use the **Import required staffing template**. You can import up to one year of data counting from today.
7. Open the downloaded *importTemplate.csv* file and edit it to include your own data.

   To avoid errors when uploading your CSV file, keep the following aspects in mind:

   1. The first row of the example must be deleted
   2. The data's timezone must be UTC
   3. Use a data range up to 365 days from today.
   4. Past timestamps in the file are discarded.
   5. Ensure that the days are in chronological order.
   6. Use numeric values only.
   7. Ensure that no special characters are used that are not on the template spreadsheet.
   8. Data must be uploaded with 15-minute increments starting at 00:00:00 on the first day. Entries like 09:10 will result in errors.
   9. Add at least one row of data.
   10. Delete timestamp duplicates.
8. Upload your scenario CSV file.
9. Click **Import scenario**.

## Duplicating forecast scenarios

You must be a [WFM admin or have permission](https://support.zendesk.com/hc/en-us/articles/6443374440090) to duplicate an existing forecast scenario.

**To duplicate a forecast scenario**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_forecasts_icon.png)
   **Forecasting** in the navigation bar, then select **Forecast scenarios**.
2. Under Workstreams, use the drop-down menu to select a workstream.
3. Next to the scenario you want to duplicate, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)), then select **Duplicate**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_forecast_scenario_options.png)
4. Enter a scenario name.
5. Click **Duplicate scenario**.

## Activating forecast scenarios

Once you’ve created new forecast scenarios or duplicated existing ones, you can set a different scenario as active.

An active forecast scenario means that [scheduling](https://support.zendesk.com/hc/en-us/articles/6443348279194) and [reporting](https://support.zendesk.com/hc/en-us/articles/8920679615258) consider that forecast. A workstream’s default scenario is set to active and is visible in the [Active forecast page](https://support.zendesk.com/hc/en-us/articles/9940054229402).

You must be a [WFM admin or have permission](https://support.zendesk.com/hc/en-us/articles/6443374440090) to activate forecast scenarios.

**To activate a forecast scenario**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_forecasts_icon.png)
   **Forecasting** in the navigation bar, then select **Forecast scenarios**.
2. Under Workstreams, use the drop-down menu to select a workstream.
3. Click the scenario you want to activate to open it.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_forecast_scenario_options.png)
4. Click **Activate**.

## Renaming forecast scenarios

You must be a [WFM admin or have permission](https://support.zendesk.com/hc/en-us/articles/6443374440090) to rename forecast scenarios.

Note: You can’t change the name of the workstream's default forecast scenario.

**To rename a forecast scenario**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_forecasts_icon.png)
   **Forecasting** in the navigation bar, then select **Forecast scenarios**.
2. Under Workstreams, use the drop-down menu to select a workstream.
3. Next to the scenario you want to duplicate, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)), then select **Rename**.
4. Enter a new scenario name.
5. Click **Save**.

## Deleting forecast scenarios

You must be a [WFM admin or have permission](https://support.zendesk.com/hc/en-us/articles/6443374440090) to delete a forecast scenario.

Deleting a scenario is permanent and it can’t be restored.

**To delete a forecast scenario**

1. In [Workforce management](https://support.zendesk.com/hc/en-us/articles/4408838272410), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wfm_forecasts_icon.png)
   **Forecasting** in the navigation bar, then select **Forecast scenarios**.
2. Under Workstreams, use the drop-down menu to select a workstream.
3. Next to the scenario you want to duplicate, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)), then select ****Delete****.
4. Click **Delete scenario**.
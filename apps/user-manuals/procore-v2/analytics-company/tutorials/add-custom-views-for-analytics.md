# Add Custom Views for Analytics

Source: https://v2.support.procore.com/product-manuals/analytics-company/tutorials/add-custom-views-for-analytics

---

## Background

For Analytics 2.0, a custom budget view and a custom advanced forecasting view must be selected for the data to populate as tables in the database.

## Things to Consider

- [Required User Permissions](/product-manuals/analytics-company/permissions)
- For additional configuration options, see [Configure a Custom Budget Report](/product-manuals/analytics-company/tutorials/configure-custom-budget-report).

## Steps

1. Navigate to **Analytics 2.0**.
2. Click the **Budget and Forecasting** tab.
3. Select both the budget view and the advanced forecasting view you would like to sync for the report.
4. Click **Save Changes**.

##### Â Note

- This will populate data in [budget\_views] and [budget\_view\_details] tables.
- All snapshots will be synced regardless of your selection. Snapshot data is located in:

 - [budget\_snapshot\_line\_item\_headers]
 - [budget\_snapshot\_line\_items]
 - [budget\_snapshot\_line\_item\_forecasts]
- Please allow up to 24 hours for any changes to the selected views to take effect.
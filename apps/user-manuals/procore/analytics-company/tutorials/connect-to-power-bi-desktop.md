# Connect to Power BI Desktop

Source: https://v2.support.procore.com/product-manuals/analytics-company/tutorials/connect-to-power-bi-desktop

---

## Overview

This guide covers the steps for establishing new data connections and utilizing Power BI templates.

## Prerequisites

- Download the zipped package from the company level **Analytics** tool (via **Analytics** > **Getting Started** > **Connection Options** > **PowerBI**) in Procore.

## Things to Consider

- For details on connecting Analytics to Power BI Desktop, see Microsoft's [Connect to data sources in Power BI Desktop](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-connect-to-data) article.

## Steps

- Connect New Data
- Connect to an Existing Template

##### Â Note

These methods of connection are typically used by data professionals.

### Connect New Data

1. Open your Power BI Desktop.
2. Click **Get Data** and select More.
3. In the search bar, type 'Delta Sharing'.
4. Select **Delta Sharing**, then click **Connect**.
5. Type or paste the **Delta Sharing Server URL** you received from Procore.
6. Click **Okay**.
7. If this is the first time you are connecting to this source, you will be prompted to provide your **Delta Sharing Bearer Token**.
8. Click **Connect**.
9. After authentication, select the **Analytics** tables you want to bring into your Power BI report.
10. Select **Load** to view your report or select **Transform Data** to make more transformations in Power Query.

### Connect to an Existing Template

1. Open **Power BI Desktop**.
2. Click the **Transform Data** drop-down and select **Data Source** settings.
3. Select **Edit Permissions**.
4. Click **Edit**.
5. Enter the token you received from Analytics 2.0.
6. Click **Refresh**.
7. You custom budget columns will now appear in the Budget and BudgetSnapshots tables.
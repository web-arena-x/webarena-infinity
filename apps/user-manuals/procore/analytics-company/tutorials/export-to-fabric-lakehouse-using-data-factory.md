# Export to Fabric Lakehouse Using Data Factory

Source: https://v2.support.procore.com/product-manuals/analytics-company/tutorials/export-to-fabric-lakehouse-using-data-factory

---

## Overview

Integrating Delta Sharing with Microsoft Fabric Data Factory enables seamless access and processing of shared Delta tables for your analytics workflows with Analytics 2.0. Delta Sharing, an open protocol for secure data collaboration, ensures organizations can share data without duplication.

## Prerequisites

- Analytics 2.0 SKU
- Delta Sharing Credentials:

 - Obtain the **share.json** (or equivalent) [Delta Sharing credentials](/process-guides/getting-started-with-analytics/generate-data-access-credentials) file from your data provider.
 - This file should include:

    - **Endpoint URL:** The Delta Sharing Server URL.
    - **Bearer Token:** Used for secure data access.
- Microsoft Fabric Setup:

 - A Microsoft Fabric tenant account with an active subscription.
 - Access to a Microsoft Fabric-enabled workspace.

## Steps

- Switch to the Data Factory Experience
- Configure the Dataflow
- Perform Data Transformations
- Validation and Monitoring

### Switch to the Data Factory Experience

1. Navigate to your **Microsoft Fabric Workspace**.
2. Select **New**, then choose **Dataflow Gen2**.

### Configure the Dataflow

1. Go to the dataflow editor.
2. Click **Get Data** and select **More**.
3. Under **New source**, select **Delta Sharing Other** as the data source.
4. Enter the following details:

   - **URL**: From your Delta Sharing configuration file.
   - **Bearer Token**: Found in your config.share file.
5. Click **Next** and select the desired tables.
6. Click **Create** to complete the setup.

### Perform Data Transformations

After configuring the dataflow, you can now apply transformations to the shared Delta data. Choose your Delta Sharing Data option from the list below:

- Add Data Destination
- Create/Open Lakehouse

### Add Data Destination

1. Go to Data Factory.
2. Click **Add Data Destination**.
3. Select **Lakehouse** as the target and click **Next**.
4. Choose your destination target and confirm by clicking **Next**.

### Create-Open Lakehouse

1. Create/open your Lakehouse and click **Get data.**
2. Select New Dataflow Gen2.
3. Click **Get Data**, then **More** and find **Delta Sharing.**
4. Enter the URL bearer token from your config.share file and then select **Nex**t.
5. Choose your data/table/s to download and click **Next.**
6. After these manipulations, you should have all the selected data in your Fabric Lakehouse.

### Validation and Monitoring

Test your data pipelines and flows to ensure smooth execution. Use monitoring tools within Data Factory to track progress and logs for each activity.
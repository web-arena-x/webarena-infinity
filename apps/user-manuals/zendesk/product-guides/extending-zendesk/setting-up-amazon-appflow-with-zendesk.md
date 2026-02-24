# Setting up Amazon AppFlow with Zendesk

Source: https://support.zendesk.com/hc/en-us/articles/4408828305306-Setting-up-Amazon-AppFlow-with-Zendesk

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Amazon AppFlow is an AWS service which allows secure data transfer from Zendesk to AWS and other SaaS apps.  
![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/appflow_overview.png)

An interface is provided to configure data flows within your AWS account. AppFlow then establishes the connection, extracting the appropriate data from Zendesk, actioning transformations, and loading the data into your chosen target service.

This article guides you through the process to set up a Zendesk data flow in Amazon AppFlow. To use Amazon AppFlow, you will need:

- Administrator permissions in Zendesk Support
- Access to your AWS account console
- An OAuth client for your Zendesk account

This article contains the following topics:

- [Registering your application with Zendesk](#topic_lk1_xxn_4lb)
- [Creating a flow](#topic_hfv_qzn_4lb)
- [Step 1: Specify flow details](#topic_bs3_xzn_4lb)
- [Step 2: Configure flow](#topic_smh_214_4lb)
- [Step 3: Map data fields](#topic_z2q_1b4_4lb)
- [Step 4: Add filters](#topic_c5c_hb4_4lb)
- [Step 5: Review and create](#topic_fn4_mb4_4lb)
- [AppFlow integration limits](#topic_cbf_sb4_4lb)

Related information:

- [Using OAuth authentication with your application](https://support.zendesk.com/hc/en-us/articles/4408845965210)

## Registering your application with Zendesk

To use Amazon AppFlow, you need to register the application to generate OAuth credentials that your application can use to authenticate API calls to Zendesk. This is done in Zendesk Support.

**To register Amazon AppFlow with Zendesk**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png) **Apps and integrations** in the sidebar, then select **APIs > Zendesk API**.
2. Click the **OAuth Clients** tab, and click **Add OAuth client** on the right side of the client list.
3. Complete the following fields to create an OAuth client for AppFlow:
   - **Client Name** - Enter a name for your AppFlow application. This is the name that users will see when asked to grant access to your application, and when they check the list of third-party apps that have access to their Zendesk.
   - **Description** - Optional. This is a short description of your app that users will see when asked to grant access to it.
   - **Company** - Optional. This is the company name that users will see when asked to grant access to your application. The information can help them understand who they're granting access to.
   - **Logo** - Optional. This is the logo that users will see when asked to grant access to your application.
   - **Unique Identifier** - The field is auto-populated with a reformatted version of the name you entered for your app. You can change it if you want.
   - **Redirect URLs** - Enter “ https://`{aws_region}`.console.aws.amazon.com/appflow/oauth”. Replace `{aws_region}` with the AWS region where you're creating the flow. Example: "https://ap-southeast-2.console.aws.amazon.com/appflow/oauth".
4. Click **Save**. A new pre-populated Secret field appears on the lower side.
5. Copy and save the secret key somewhere safe.
6. Click **Save.**  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/appflow_oauth.png)

## Creating a flow

A flow is created in your AWS account console by completing a series of steps in the setup process.

**To create a flow**

1. [Log in to your AWS account console](https://docs.aws.amazon.com/console/appflow) and select **AppFlow** from the services menu.
2. Click **Create flow**.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/appflow_create.png)  

   Complete setting up a flow as described in the following sections.

## Step 1: Specify flow details

In **Step 1: Specify flow details**, you configure the name and details about the flow.

**To specify flow details**

1. In **Step 1: Specify flow details**, enter the following details for your flow:
   - **Flow name** - Enter a name for your flow.
   - **Flow Description** - A description of your flow.
   - **Data Encryption** - Configure the encryption for your flow. You have the option to use the default key, or customize encryption by creating an AWS KMS key or using an Amazon Resource Name.
   - **Tags** -Add tags to your flow as key value pairs to your flow.  
     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/appflow_flow_details.png)
2. Click **Next**.

## Step 2: Configure flow

In **Step 2: Configure flow**, you nominate your Zendesk source data and where you want the data to go such as S3, Redshift, or selected SaaS apps.

**To configure your flow**

1. In **Step 2: Configure flow**, under **Source details**, select “Zendesk”in the **Source name** drop-down selection.
2. Click **Connect.**
3. In the modal, enter the client Id and secret of the OAuth client you created earlier in Support, your Zendesk subdomain, and connection name.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/appflow_flow_details.png)  

   Note: If you receive an error message, first check the redirect URL in your AppFlow OAuth client in Support. If you still encounter errors, contact your AWS admin to check your AWS roles or permissions.
4. In the pop-up window, click **Allow** to let AppFlow access your Zendesk data. You must be a Zendesk admin to allow access.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/appflow_zendesk_access.png)
5. In the **Choose Zendesk object** drop-down selection, select the type of Zendesk data to sync.
6. Under **Destination details** in the **Destination name** drop-down selection, select the destination for your Zendesk data.
   - If you select S3 as your destination, select the S3 bucket to send data
   - If you select another destination, click **Connect** and follow the prompts in the modal to complete the connection  
     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/appflow_destination.png)
7. In **Flow trigger** under **Choose how to trigger the flow**, select either “Run on demand” to activate the flow manually, or “Run on schedule” to activate the flow on a schedule. If you choose “Run on schedule”, set the schedule frequency.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/appflow_flow_trigger.png)
8. Select **Transfer only new data** to only transfer new data that is new when the flow is triggered, or **Transfer all data** if you want the flow to transfer all data.
9. Click **Next**.

## Step 3: Map data fields

In **Step 3: Map data fields**, you specify how the fields in your Zendesk data map to the fields in the destination.

**To map data fields**

1. Choose the mapping method to map fields.
   - **Manually map fields** - To map all fields, choose **Source field name**, **Bulk actions**, and **Map all fields directly**. Otherwise, select one or more fields from **Source field name**, **Source fields**, and then choose **Map fields directly**.
   - **Upload csv file with mapped fields** - Use a CSV file to define the mapping. The CSV file contains comma-separated values of the source field name and destination field name.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/appflow_destination.png)
2. To concatenate fields together, select the mapped fields and select **Add formula**.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/appflow_addformula.png)
3. To mask fields or truncate field names, select the mapped fields and select **Modify values**.
4. For **Validations**, click **Add validation** configure how data fields are handled based on the condition.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/appflow_validations.png)
5. Click **Next**.

## Step 4: Add filters

In **Step 4: Add filters**, you create rules that determine which data is extracted from your Zendesk account each time the flow is triggered.

**To add filters**

1. In **Filters**, click **Add filter**, then select the field, select a condition, and specify the criteria.  
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/appflow_addfilters.png)
2. Click **Next.**

## Step 5: Review and create

In **Step 5: Review and create**, you can review your flow configuration before creating it.

**To finish creating a flow**

1. Check your configuration is correct. Click **Edit** in the upper-right if you need to revise the configuration.
2. Click **Create flow**.

Your flow is now created!

## AppFlow integration limits

Amazon imposes the following limits on AppFlow:

- One million flows per account
- 10 million flow runs a month
- Each flow can have no more than one source and one destination
- Each flow can include no more than 10 tasks

[Zendesk API limits](https://developer.zendesk.com/rest_api/docs/support/introduction#rate-limits) also apply, with each flow execution consuming one API call from the [Zendesk incremental export API](https://developer.zendesk.com/rest_api/docs/support/incremental_export).
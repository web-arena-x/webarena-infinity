# Export to ADLS Using Azure Functions

Source: https://v2.support.procore.com/product-manuals/analytics-company/tutorials/export-to-adls-using-azure-functions

---

## Overview

This guide walks you through setting up and deploying an Azure Function for integrating Delta Sharing data with Analytics. The Azure Function enables efficient data processing and sharing workflows with Delta Sharing profiles.

#### Prerequisites

- Analytics 2.0 SKU.
- Delta Sharing profile file:

 - Your **\*.share** file containing [Delta Sharing credentials](/process-guides/getting-started-with-analytics/generate-data-access-credentials). For convenience, place it inside the downloaded package.
 - Python Environment:

    - Installed Python 3.9+ and **pip** on your system.
- Azure Setup:

 - Azure CLI installed and logged in.
 - Azure Functions Core Tools installed.

#### Steps

- Prepare the Package
- Install Dependencies
- Generate Configuration
- Azure CLI Setup
- Install Azure Functions Core Tools
- Prepare the Azure Function
- Deployment
- Validation

##### Prepare the Package

1. Download the required package (adls\_azure\_function or sql\_server\_azure\_function).   
   *Note:* You can download the zipped package from the company level **Analytics** tool (via **Analytics > Getting Started** > **Connection Options** > **Azure**).
2. Extract the package files to a local directory.
3. Place Delta Sharing file:

   - Copy your \*.share Delta Sharing profile file into the extracted directory.

##### Install Dependencies

1. Open a terminal in the package directory.
2. Run the following command to install the required Python dependencies:

   - *pip install -r requirements.txt*

##### Generate Configuration

1. Generate the config.yamlfile by running:

   - *python user\_exp.py*
2. The script will prompt you to enter credentials such as:

   - Tables
   - Database name
   - Host
   - Additional credentials..
3. The configuration can be reused or updated manually or by re-running *python user\_exp.py.*

##### Azure CLI Setup

1. Log in to Azure.
2. Run the following command to log in:   
   *az login*
3. Verify Azure Account:

   - *az account show*
   - If the az command is not available, install the Azure CLI by following the instructions found here: [Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).

##### Install Azure Functions Core Tools

Go to [Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-csharp) to for instructions on installing Azure Functions Core Tools.

##### Prepare the Azure Function

1. Use the [Azure Portal guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-python#install-the-azure-functions-core-tools) to create the following:

   - A function app
   - A resource group
   - Consumption plan
   - Storage account
2. Set Custom Cron schedule (Optional).

   - Open function\_app.py in an editor.
   - Locate the line: `@app.timer_trigger(schedule="0 0 */8 * * *",`
3. Replace the schedule with your custom Cron expression and save the file.

##### Deployment

1. Open a terminal in the package directory (adls\_azure\_function).
2. Run the following deployment command:

   - *func azure functionapp publish <FunctionAppName>* *--build remote --python --clean*
3. Replace *<FunctionAppName>* with the name of your Azure function app in your Azure subscription.

##### Validation

- Ensure the deployment is successful by checking the Azure Portal for your function app status.
- Monitor logs to verify that the function is executing as expected.
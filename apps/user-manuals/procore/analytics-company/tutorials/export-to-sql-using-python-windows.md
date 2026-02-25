# Export to SQL Server Using Python Library

Source: https://v2.support.procore.com/product-manuals/analytics-company/tutorials/export-to-sql-using-python-windows

---

## Overview

This guide provides detailed instructions for setting up and using the Delta Sharing integration package on a Windows operation system to seamlessly integrate data into your workflows with Analytics. The package supports multiple execution options, allowing you to choose your desired configuration and integration method.

## Prerequisites

Ensure you have the following before proceeding:

- Analytics 2.0 SKU
- Delta Sharing pofile file: Obtain your **\*.share** file containing [Delta Sharing credentials](/process-guides/getting-started-with-analytics/generate-data-access-credentials). For convenience, copy it into the package directory.
- Python Environment: Install Python 3 and **pip** on your system.

 - [Download Python](https://www.python.org/downloads/windows/).
 - Alternatively, use the Microsoft Store.

## Steps

- Prepare the Package
- Install Dependencies
- Generate Configuration
- Configure Cron Jobs and Immediate Execution
- Execution and Maintenance

### Prepare the Package

1. Create a new file named config.share with your Delta Share credentials in JSON format. 
   `{ "shareCredentialsVersion": 1, "bearerToken": "xxxxxxxxxxxxx", "endpoint": "`[https://nvirginia.cloud.databricks.c...astores/xxxxxx](https://nvirginia.cloud.databricks.com/api/2.0/delta-sharing/metastores/xxxxxx)`" }`
2. Get required fields. 
   *Note:* These details can be obtained from the Analytics web application.

   - ShareCredentialsVersion: Version number (currently 1).
   - BearerToken: Your Delta Share access token.
   - Endpoint: Your Delta Share endpoint URL.
3. Download and extract the package. 
   *Note:* You can download the zipped package from the company level **Analytics** tool (via **Analytics > Getting Started** > **Connection Options** > **SQL Server**).
4. Unzip the package to a directory of your choice.
5. Copy the \*.share Delta Sharing profile file into the package directory for easy access.

### Install Dependencies

1. Open a terminal in the package directory.
2. Run the **pip install -r requirements.txt** command to install the dependencies.

### Generate Configuration

1. Generate the config.yaml file by running python user\_exp.py: This script helps to generate the config.yaml file that contains the necessary credentials and settings.
2. When configuring the data source, you'll be asked to provide:

   - List of tables (comma-separated).
   - Leave blank to sync all tables. Example: table1, table2, table3.
   - Path to your config.share file.
3. For the first time, you will provide your credentials like Delta Share source configuration location, tables, database, host and etc.   
   *Note:* Afterwards, you may reuse or update the config manually or by running python user\_exp.py again.

### Configure Cron Jobs and Immediate Execution (Optional)

1. Decide whether to set up a cron job for automatic execution.
2. Provide a cron schedule:

   - Format: `* * * * *` (minute, hour, day-of-month, month, day-of-week).
   - Example for daily execution at 2 AM: **0 2 \* \* \***
   - To check scheduling logs, the file procore\_scheduling.log will be created as soon as scheduling is set up.

You can also check scheduling by running in terminal command:

**For Linux and MacOs:**

To edit/delete - edit scheduling cron by using:

`bash EDITOR=nano crontab -e`

- After running the command above, you should see something similar to:
- **2 \* \* \* \* /Users/your\_user/snowflake/venv/bin/python /Users/your\_user/snowflake/sql\_server\_python/connection\_config.py 2>&1 | while read line; do echo "$(date) - $line"; done >> /Users/your\_user/snowflake/sql\_server\_python/procore\_scheduling.log # procore-data-import**
- You can also adjust the schedule cron or delete the whole line to stop it from running by schedule.

**For Windows:**

- Check the schedule task is created: **powershell schtasks /query /tn "ProcoreDeltaShareScheduling" /fo LIST /v**
- To edit/delete - scheduling task:   
 Open the Task Scheduler:

 - Press Win + R, type taskschd.msc, and press Enter.
 - Navigate to the scheduled tasks.
 - In the left pane, expand the Task Scheduler Library.
 - Look for the folder where your task is saved (e.g., Task Scheduler Library or a custom folder).
- Find your task:

 - Look for the task name ProcoreDeltaShareScheduling.
 - Click on it to view its details in the bottom pane.
- Verify its schedule:

 - Check the Triggers tab to see when the task is set to run.
 - Check the History tab to confirm recent runs.
- To delete a task:

 - Delete a task from the GUI.

**Immediate Execution question:**

- Option to run the script for copying data immediately after configuration.
- After generating the config.yaml, the CLI is ready to be run anytime independently, by running the script for copying data, depending on your package.
- Examples:

 - python delta\_share\_to\_azure\_panda.py
 - python delta\_share\_to\_sql\_spark.py
 - python delta\_share\_to\_azure\_dfs\_spark.py

### Execution and Maintenance

**Common Issues and Solutions**

1. Cron Job Setup:

   - Ensure system permissions are correctly configured.
   - Check system logs if the job fails to run.
   - Verify the script delta\_share\_to\_azure\_panda.py has execute permissions.
2. Configuration File:

   - Ensure the file config.yaml is in the same directory as the script.
   - Back up the file before making changes.

**Support**

For additional help:

1. Review script logs for detailed error messages.
2. Double-check the config.yaml file for misconfigurations.
3. Contact your system administrator for permission-related issues.
4. Reach out to Procore support for issues related to Delta Share access.
5. Review log for failed tables: failed\_tables.log.

**Notes**

1. Always back up your configuration files before making changes.
2. Test new configurations in a non-production environment to prevent disruptions.
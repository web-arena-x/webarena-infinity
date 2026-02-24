# Export to Snowflake Using Python

Source: https://v2.support.procore.com/product-manuals/analytics-company/tutorials/export-to-snowflow-using-python

---

## Overview

The Analytics Cloud Connect Access tool is a command-line interface (CLI) that helps you configure and manage data transfers from Procore to Snowflake.

It consists of two main components:

- **user\_exp.py**: Configuration setup utility
- **ds\_to\_snowflake.py**: Data synchronization script

## Prerequisites

- Python is installed on your system
- Access to Procore Delta Share
- Snowflake account credentials
- Download the zipped package from the company level **Analytics** tool (via **Analytics > Getting Started** > **Connection Options** > **Snowflake**).
- Install the required dependencies using:

 - pip install -r requirements.txt

## Steps

- Initial Configuration
- Data Synchronization
- Delta Share Source Configuration
- Snowflake Target Configuration
- Scheduling Options
- Best Practices
- Troubleshooting

### Initial Configuration

Run the configuration utility using python user\_exp.py.

### Data Synchronization

**After configuration, you have two options to run the data sync:**

- Direct Execution:

 - **python ds\_to\_snowflake.py**
- Scheduled Execution

 - If configured during setup, the job will run automatically according to your Cron schedule.
 - To check scheduling logs, the file **procore\_scheduling.log** will be created as soon as scheduling is set up.
 - Also, you can check scheduling by running in terminal command:

**For Linux and MacOS:**

- To edit/delete - edit scheduling cron by using:   
 `bash`

 `EDITOR=nano crontab -e`
- After running the command above, you should see something similar to:   
 `2 * * * *``/Users/your_user/snowflake/venv/bin/python 
    
 /Users/your_user/snowflake/sql_server_python/connection_config.py``2>&1 | while read line; do echo "$(date) - $line"; done>> 
    
 /Users/your_user/snowflake/sql_server_python/procore_scheduling.log # procore-data-import`
- You can also adjust the schedule cron or delete the whole line to stop it from running by schedule.

**For Windows:**

- Check that the schedule task is created: `powershell`

 `schtasks /query /tn "ProcoreDeltaShareScheduling" /fo LIST /v`
- To edit/delete a scheduling task, open the Task Scheduler.
- Press Win + R, type **taskschd.msc**, and press enter.
- Navigate to the scheduled tasks.
- In the left pane, expand the Task Scheduler Library.
- Look for the folder where your task is saved.   
 Example: Task Scheduler Library or a custom folder.
- Find your task.
- Look for the task name: **ProcoreDeltaShareScheduling**.
- Click on it to view the details in the bottom pane.
- Verify its schedule:

 - Check the Triggers tab to see when the task is set to run.
 - Check the History tab to confirm recent runs.
- To delete a task:

 - Delete the task from the GUI.

### Delta Share Configuration

- Creating **config.share** file
- Before running the configuration utility, you need to create a **config.share** file with your Delta Share credentials. The file should be in JSON format:   
 `{`

 `"shareCredentialsVersion": 1, "bearerToken": "xxxxxxxxxxxxx", "endpoint": "`<https://nvirginia.cloud.databricks.c...astores/xxxxxx>`"`

 `}`
- Required fields:

 - ShareCredentialsVersion: Version number (currently 1).
 - BearerToken: Your Delta Share access token.
 - Endpoint: Your Delta Share endpoint URL.
 - These details can be obtained from the Procore web UI.
- Steps to create config.share:

 - Create a new file named config.share.
 - Copy the above JSON template.
 - Replace the placeholder values with your actual credentials.
 - Save the file in a secure location.
 - You'll need to provide the path to this file during configuration. When configuring the data source, you'll be asked to provide:

    - List of tables (comma-separated).
    - Leave blank to sync all tables.
    - Example: table1, table2, table3.
- Path to your **config.share** file.

### Snowflake Configuration

You'll need to provide the following Snowflake details:

- Authentication (choose one):

 - User Authentication

    - Username
    - Password (entered securely)
- Key Pair Authentication

 - Username
 - Private key file path
 - Private key file password
- Connection Details:

 - Account identifier
 - Warehouse name
 - Database name
 - Schema name
 - Number of concurrent threads

### Scheduling Options

The tool offers the ability to schedule automatic data synchronization.

- **Cron Job Configuration**

 - Choose whether to set up a daily job
 - If yes, provide a cron schedule
 - Format: `* * * * *` (minute hour day-of-month month day-of-week)
 - Example for daily at 2 AM: `0 2 * * *`
- **Immediate Execution**

 - Option to run the ds\_to\_snowflake.py immediately after configuration
- **File Structure** `Unset`

 `âââ requirements.txt # Dependencies`

 `âââ user_exp.py # Configuration utility`

 `âââ ds_to_snowflake.py # Data sync script`

 `âââ config.yaml # Generated configuration`

 `âââ config.share # Delta Share config file`

 `âââ procore_scheduling.log # Log of scheduling runs`

**Example Usage**

- **Step 1**: Install dependencies **$ pip install -r requirements.txt**
- **Step 2**: Run configuration utility **$ python user\_exp.py**
- **Analytics Cloud Connect Access**

 - This CLI will help you choose your source and destination store to access/write Procore data into Snowflake.
 - Press Enter to Continue.
 - Enter list of tables (comma-separated), leave it blank for all tables: projects, users, tasks.
 - Enter path to config.share: **/path/to/config.share.**
 - Enter user name: snowflake\_user.
 - What authentication type do you want to use? (user/key\_pair): Enter.

    - 1 for user,
    - 2 for key-pair:
    - 1
    - Enter password
    - Enter Account: my\_account
    - Enter warehouse: my\_warehouse
    - Enter database name: procore\_db
    - Enter schema name: procore\_schema
    - Enter number of threads: 4
    - Do you want to configure this as a daily job on cron? (Yes/No): Yes
    - Enter the schedule in cron format (e.g., `* * * * *` ): `0 2 * * *`
    - Do you want to execute the job now? (Yes/No): Yes
- **Step 3**: Manual execution (if needed)   
 **$ python ds\_to\_snowflake.py**
- **Configuration Reuse** The tool saves your configuration in the config.yaml file and offers to reuse previously stored settings:

 - Source configuration can be reused.
 - Target (Snowflake) configuration can be reused.
 - You can choose to update either configuration independently.

### Best Practices

- Authentication

 - Use key pair authentication when possible.
 - Regularly rotate credentials.
 - Use minimal required permissions.
- Performance

 - Adjust thread count based on your system capabilities.
 - Start with a smaller subset of tables for testing.

### Troubleshooting

- Common issues and solutions:

 - Invalid Authentication Type

    - Ensure to select either 1 (user) or 2 (key\_pair) when prompted.
- Cron Job Setup

 - Verify you have appropriate system permissions.
 - Check system logs if the job fails to run.
 - Ensure the ds\_to\_snowflake.py has correct permissions.
 - Verify the cron job setup by checking system logs:   
    See **procore\_scheduling.log** file.
- Configuration File

 - Located in the same directory as the script,
 - Named **config.yaml.**
 - Backup before making any changes.
- Support

 - Check the script's logging output.
 - Review your **config.yaml** file.
 - Contact your system administrator for permission-related issues.
 - Reach out to Procore support for Delta Share access issues.

*Note:* Remember to always back up your configuration before making changes and test new configurations in a non-production environment first.
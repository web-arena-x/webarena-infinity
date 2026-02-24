# Connect to Amazon S3 Using Python

Source: https://v2.support.procore.com/product-manuals/analytics-company/tutorials/export-to-aws-using-python

---

## Overview

The Analytics Cloud Connect Access tool is a command-line interface (CLI) that helps you configure and manage data transfers from Procore to Amazon S3 with Analytics 2.0.

It consists of two main components:

- **user\_exp.py**: Configuration setup utility
- **delta\_share\_to\_s3.py**: Data synchronization script

## Prerequisites

- Analytics 2.0 SKU
- Python is installed on your system
- Access to Procore Delta Share
- S3 Access Keys
- Download the zipped package from the company level **Analytics** tool (via **Analytics > Getting Started** > **Connection Options** > **AWS**).
- Installation of required dependencies using:

 - **pip install -r requirements.txt**

## Steps

- Initial Configuration
- Delta Share Source Configuration
- S3 Configuration
- Scheduling Options
- Best Practices
- Troubleshooting

### Initial Configuration

Run the configuration utility using **python user\_exp.py**.

This will help you set up the following:

- Delta Share Configuration
- S3 Target Configuration
- Scheduling Preferences

### Delta Share Configuration

- Creating **config.share** file
- Before running the configuration utility, you need to create a **config.share** file with your Delta Share credentials. The file should be in JSON format: 
 `{ "shareCredentialsVersion": 1,`

 `"bearerToken": "xxxxxxxxxxxxx",`

 `"endpoint": "xxxxxx"`

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

### S3 Configuration

You'll need to provide the following S3 details:

- Authentication:

 - Access key
 - Secret Key
 - Bucket name without s3://
 - key - directory

### Scheduling Options

The tool offers the ability to schedule automatic data synchronization.

- **Cron Job Configuration**

 - Choose whether to set up a daily job.
 - If yes, provide a cron schedule.
 - Format: `* * * * *` (minute hour day-of-month month day-of-week).
 - Example for daily at 2 AM: 0 2 `* * *`
 - To check scheduling logs, the file **'procore\_scheduling.log'** will be created as soon as scheduling is set up.

You can also check scheduling by running in terminal command

**For Linux and MacOs:**

To edit/delete - edit scheduling cron by using:

`bash EDITOR=nano crontab -e`

- After running the command above, you should see something similar to:
- `2 * * * * /Users/your_user/snowflake/venv/bin/python /Users/your_user/snowflake/sql_server_python/connection_config.py 2>&1 | while read line; do echo "$(date) - $line"; done >>   
 /Users/your_user/snowflake/sql_server_python/procore_scheduling.log # procore-data-import`
- You also can adjust schedule cron or delete the whole line to stop it running by schedule.

**For Windows:**

- Check the schedule task is created: 
 **`powershell`**

 **`schtasks /query /tn "ProcoreDeltaShareScheduling" /fo LIST /v`**
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
- To delete task:

 - Delete task from the GUI.
- **Immediate Execution**

 - Option to run the **delta\_share\_to\_s3\_.py** **File** **Structure**
- `Unset`

 `âââ requirements.txt # Dependencies âââ user_exp.py # Configuration utility âââ delta_share_to_s3.py # Data sync script âââ config.yaml # Generated configuration âââ config.share # Delta Share config file âââ procore_scheduling.log # Log of scheduling runs`
- **Example Usage**

 - **Step 1**: Install dependencies **$ pip install -r requirements.txt**
 - **Step 2**: Run configuration utility **$ python user\_exp.py**
 - **Analytics Cloud Connect Access**

    - This CLI will help you choose your source and destination store to access/write Procore data into S3.
    - Press Enter to Continue.
    - Enter list of tables (comma-separated), leave it blank for all tables: projects,users,tasks.
    - Enter path to config.share: **/path/to/config.share.**
    - Enter access key: s3 key.
    - Enter secret: secret.
    - Enter bucket: bucket name.
    - Do you want to configure this as a daily job on cron? (Yes/No): Yes
    - Enter the schedule in cron format (e.g., `* * * * *` ): `0 2 * * *`
    - Do you want to execute the job now? (Yes/No): Yes
 - **Step 3**: Manual execution (if needed)   
    `$ python delta_share_to_s3.py`
- **Configuration Reuse** The tool saves your configuration in the config.yaml file and offers to reuse previously stored settings:

 - Source configuration can be reused.
 - Target (S3) configuration can be reused.
 - You can choose to update either configuration independently.

### Troubleshooting

**Common issues and solutions**:

- Cron Job Setup

 - Ensure system permissions are correctly configured.
 - Check system logs if the job fails to run.
 - Verify the script (**delta\_share\_to\_s3.py)** execute permissions.
- Configuration File

 - Confirm the file **config.yaml** is in the same directory as the script.
 - Backup before making any changes.
- Support

 - Review script logs for detailed error messages.
 - Review your **config.yaml** file for misconfigurations.
 - Contact your system administrator for permission-related issues.
 - Reach out to Procore support for Delta Share access issues.
 - Verify cron job setup by checking system logs: See **procore\_scheduling\_log** file.

**Notes:**

1. Remember to always backup your configuration before making changes.
2. Test new configurations in a non-production environment first.
# Export to SQL Server Using Python (SSIS)

Source: https://v2.support.procore.com/product-manuals/analytics-company/tutorials/export-to-sql-using-python-ssis

---

## Overview

The Analytics Cloud Connect Access tool is a command-line interface (CLI) that helps you configure and manage data transfers from Procore to MS SQL Server. It consists of two main components:

- user\_exp.py (Configuration setup utility)
- delta\_share\_to\_azure\_panda.py(Data synchronization script)

## Prerequisites

- Python and pip installed on your system.
- Access to Procore Delta Share.
- MS SQL Server account credentials.
- Download the zipped package from the company level **Analytics** tool (via **Analytics > Getting Started** > **Connection Options** > **SQL Server**).
- Install required dependencies: pip install -r requirements.txt.

## Steps

- Initial Configuration
- Data Synchronization
- Delta Share Configuration
- MS SQL Server Configuration
- SSIS Configuration

### Initial Configuration

- Run the configuration utility: python user\_exp.py

This will help you set up the following:

- Delta Share source configuration
- MS SQL Server target configuration
- Scheduling preferences

### Data Synchronization

After configuration, you have two options to run the data sync:

1. Direct Execution python delta\_share\_to\_azure\_panda.py OR
2. Scheduled Execution If configured during setup, the job will run automatically according to your cron schedule.

### Delta Share Configuration

1. Create a new file named config.share with your Delta Share credentials in JSON format. 
   `{ "shareCredentialsVersion": 1, "bearerToken": "xxxxxxxxxxxxx", "endpoint": "`[https://nvirginia.cloud.databricks.c...astores/xxxxxx](https://nvirginia.cloud.databricks.com/api/2.0/delta-sharing/metastores/xxxxxx)`" }`
2. Get required fields: 
   *Note:* These details can be obtained from the Analytics web application.

   - ShareCredentialsVersion: Version number (currently 1).
   - BearerToken: Your Delta Share access token.
   - Endpoint: Your Delta Share endpoint URL.
   - Save the file in a secure location.
3. When configuring the data source, you'll be asked to provide:

   - List of tables (comma-separated).
   - Leave blank to sync all tables.
   - Example: table1, table2, table3.
   - Path to your config.share file.

### MS SQL Server Configuration

You'll need to provide the following MS SQL Server details:

- database
- host
- password
- schema
- username

### SSIS Configuration

1. Using the command line, navigate to the folder by entering 'cd '.
2. Install required packages using 'pip install -r requirements.txt' or 'python -m pip install -r requirements.txt'.
3. Open SSIS and create a new project.
4. From SSIS Toolbox, drag and drop 'Execute Process Task' activity.
5. Double-click on 'Execute Process Task' and navigate to Process tab.
6. In 'Executable', enter the path to python.exe in python installation folder.
7. In 'WorkingDirectory' enter a path to the folder containing the script you want to execute (without script file name).
8. In 'Arguments' enter the name of the script **'delta\_share\_to\_azure\_panda.py'** you want to execute with the .py extension and save.
9. Click on 'Start' button in upper pane:
10. During the execution of the task, output of the Python console is displayed in the external console window.
11. Once the task is done it will display a green tick:
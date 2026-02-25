# Connect Your Procore Data by Downloading Analytics Models

Source: https://v2.support.procore.com/product-manuals/analytics-company/tutorials/connect-your-procore-data-by-downloading-analytics-models

---

## Considerations

- **Requirements**:

 - Python 3.6 or higher installed on your system.
 - 'config.share' file received from Procore.
 - The necessary Python packages installed on your system.
 - The script supports both PySpark and Python.
 - If you are using PySpark, make sure you have installed Spark 3.5.1 or later, Java and configured the SPARK\_HOME environment variable.
 - If you are using Python and the target location is MSSQL DB, install the ODBC driver 17 for SQL Server on your system.

## Steps

##### Â Note

This method of connection is typically used by data professionals.

- **Create Credentials File**
- **Run user\_exp.py script**
- **Run as PySpark**
- **Run as Python**
- **Choose Your Own Method**

### Create Credentials File

You must first generate a data token within the Procore web application. See [Generate Access Token](/process-guides/getting-started-with-analytics/generate-data-access-credentials).

1. Create a file called config.share.
2. Add the fields below: 
    { "shareCredentialsVersion": 1, "bearerToken": "", "endpoint": "", "expirationTime": "" }
3. Add the Bearer Token, Endpoint, Share Credentials Version, and Expiration Time values received from Procore to the config.share file.

### Run user\_exp.py script

You can use the following scripts to create a config.yaml file with the necessary configurations.

- **For Azure Storage**: 
   cron\_job: #true/false run\_as: #pyspark/python source\_config:
   config\_path: #path to the config.share file tables:
   - '' # table name if you want to download a specific table. Leave it empty if you want to download all tables 
   source\_type: delta\_share target\_config:
   auth\_type: service\_principal client\_id: #client\_id secret\_id: #secret\_id storage\_account: #storage-account name storage\_path: #@.dfs.core.windows.net/ enant\_id: #tenant\_id target\_type: azure\_storage
- **For MSSQL DB**: 
   cron\_job: #true/false run\_as: #pyspark/python source\_config:
   config\_path: #path to the config.share file tables:
   - '' # table name if you want to download a specific table. Leave it empty if you want to download all tables 
   source\_type: delta\_share target\_config:
   database: #target database host: #target hostname:port password: #password schema: #target schema (default to procore\_analytics)
   username: #username target\_type: sql\_server

### Run as PySpark

If your environment is already set up with Spark, choose the 'pyspark' option when requested or once the 'config.yaml' is generated, you can run the following commands to download the reports to the data directory.

- **For Writing to ADLS Gen2 Storage**: 
   spark-submit --packages io.delta:delta-sharing-spark\_2.12:3.1.0,org.apache.hadoop:hadoop-azure:3.4.0,com.microsoft.azure:azure-storage:8.6.6,org.apache.hadoop:hadoop-common:3.4.0 --exclude-packages com.sun.xml.bind:jaxb-impl delta\_share\_to\_sql\_spark.py
- **For Writing to MSSQL DB:** spark-submit --packages io.delta:delta-sharing-spark\_2.12:3.1.0 --jars **mssql** **-jdbc jar> delta\_share\_to\_sql\_spark.py**

### Run as Python

1. From the command line, navigate to the folder by entering the **âcd** **â** command.
2. Install required packages using **âpip install -r requirements.txtâ** or **âpython -m pip install -r requirements.txtâ.**
3. Execute the command **python delta\_share\_to\_azure\_pandy.py.**

### Using SSIS

1. Open SSIS and create a new project.
2. From the SSIS Toolbox drag and drop **Execute Process Task**.
3. Double click **Execute Process Task**.
4. Go to the Process tab.
5. Next to **Executable**, enter the path to python.exe in the Python installation folder.
6. In **WorkingDirectory**, enter the path to the folder containing the script you want to execute (without the script file name).
7. In **Arguments**, enter the name of the **script delta\_share\_to\_azure\_panda.py** you want to execute with the .py extension and click **Save**.
8. Click **Start** in the top ribbon menu.
9. During the execution of the task, the output of the Python console is displayed in the external console window.
10. Once the task is done it will display a checkmark.

### Choose Your Own Method

Delta Sharing is an open protocol for secure data sharing. You can find the public GitHub repository for Delta Sharing at <https://github.com/delta-io/delta-sharing>. The repository includes examples and documentation for accessing shared data using various languages such as Python and Spark Connector (SQL, Python, Scala, Java, R).

##### Â Note

Make sure you have appropriate permissions and access rights to download the required files and run Docker containers on your system. Always follow security best practices and guidelines provided by Procore when handling sensitive data and credentials.
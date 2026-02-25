# Integrate a Primavera P6 Schedule using Procore Drive

Source: https://v2.support.procore.com/product-manuals/procore-drive/tutorials/integrate-a-primavera-p6-schedule-using-procore-drive

---

## Overview Diagram

## Things to Consider

- **Required User Permissions**:

  - 'Admin' permissions on the Schedule tool in Procore.
- **Additional Information**:

  - This article provides steps to integrate a **Primavera P6** schedule with a Procore project. **Oracle Primavera Cloud** does NOT integrate with Procore Drive.
  - When you integrate a Primavera P6 schedule with its associated project in Procore, anyone with âRead Onlyâ or higher level permissions on the projectâs Schedule tool will be able to view your P6 schedule directly in Procore.
  - Your schedule cannot be changed directly in Procore. Any changes to your P6 schedule must be performed using Oracleâs Primavera P6 Professional Project Management software.
  - You can only link a single schedule to a Procore project. When a new version of the schedule becomes available, you must upload it to Procore Drive to overwrite the previous version. To do this, you must export the schedule by clicking the Export Schedule button in Procore Drive.   
    *Note:* Each time a file is uploaded a file is saved in the Documents tool for versioning history.
  - The following items will be imported through the Primavera P6 integration:

    - Work Breakdown Schedule (WBS)
    - Activity Names
    - Activity ID
    - Baseline Start *Note:* Only one Baseline Start is supported in Procore.
    - Baseline Finish *Note:* Only one Baseline Finish is supported in Procore.
    - Start
    - Finish
    - Duration
    - % Complete (Duration, Physical or Units based on settings)
    - Predecessors, Successors
    - Notes
    - Resources, Resource Assignments

*Note*: The WBS and Activities in Procore will appear as a hierarchy of tasks.

## Prerequisites

### Install the Current Version of Procore Drive

- Install the latest version of Procore Drive. If you do not have the most recently published version, please see [Procore Drive Set Up Guide.](/product-manuals/procore-drive/tutorials/procore-drive-setup-guide)

### Obtain the Appropriate Database Credentials

- Obtain the appropriate database credentials for the private user (i.e. privuser) of the Microsoft SQL or Oracle database. Typically, the default private username is 'privuser.' However, some organizations change this. See your organization's Database Administrator for the credentials.   
  *Note*: Any Oracle user account that has at least read only access to the relevant P6 schedule information you want to integrate into Procore will work to use as the username and password you enter into Procore Drive.

## Steps

### Configure the Project Level Schedule Tool for Primavera P6

1. Navigate to the project's **Schedule** tool in Procore's web application.
2. Click the **Configure Settings**  icon.
3. Click the **Schedule Settings** page.
4. Set the Primavera Project ID, found in the **File** > **Open** window of the Primavera P6 project.  
   *Note:* This is the Schedule ID number that Primavera P6 uses to identify a specific project schedule.  
    At any time you can change the Project ID or Schedule ID to pull in a different P6 schedule via Procore Drive.
5. Scroll down and click **Update** to save your changes.

### Configure the P6 Database Server Settings in Procore Drive

1. Open **Procore Drive** on your computer.
2. Select your company and project from the drop-down menus.
3. Select the **Schedule** tool.
4. Verify that **Primavera Integration** is selected under your project name.  
   *Note:* Any Oracle or SQL Server user account that has at least read-only access to the relevant P6 schedule information you want to integrate into Procore will work to use as the username and password you enter into Procore Drive.
5. Verify the **Schedule ID**.  
   *Note:* This is the Schedule ID number that Primavera P6 uses to identify a specific project schedule.
6. Select the **Database Type**.
7. Follow the appropriate instructions below, depending on your database type:

   - Microsoft SQL Database Instructions
   - Oracle Database Instructions
   - SQLite Database Instructions

---

## Microsoft SQL Database Instructions

1. **Host Name**: Enter the IP address (e.g., 184.106.123.123) or computer name (e.g. primavera-p6-2) of the machine where Primavera P6 is currently installed. If Procore Drive is installed on the database server itself, you can enter 'localhost' or the computer's name.  
   *Tip*: To find your computer name, go to Start > Control Panel > System. Under the Computer Name section, copy and paste the value for 'Full Computer name' (do not include any ending period).
2. **Database Name**: Enter the name of the SQL database for Primavera P6. (e.g. PMDB)  
   *Tip*: To find this value, go to the login prompt for Microsoft SQL Primavera P6. The value next to Database is what you will enter.
3. **Instance**: If Primavera 6 is locally installed on the machine (default), leave this field blank. If itâs installed on a network server, specify the instanceâs name on the network. (e.g. PRIMAVERA).
4. **Database Credentials**: Enter your database credentials. Procore must use the login credentials for your 'privuser' in order to access the required data from the P6 database.

   - **Username**: Enter the name of the private user. The default value is 'privuser'.
   - **Password**: Enter the matching password.  
     *Note*: Any Oracle or SQL Server user account that has at least read-only access to the relevant P6 schedule information you want to integrate into Procore will work to use as the username and password you enter into Procore Drive.
5. Click the **Test Connection** button to validate that the provided database information is correct. If it is not correct, please check your credentials and try again.
6. Once the connection is validated, click the **Save** button to save your changes.
7. Click the **Export Schedule** button to upload and apply the project schedule to your project in Procore. It will take a few minutes for your schedule to finish the upload process.
8. After you see a 'Export complete' message, log in to Procore and verify that you can see your schedule and all of its data under your projectâs Schedule tool.

---

## Oracle Database Instructions

1. **Hostname**: Enter the IP address (e.g. 184.106.123.123) or computer name (e.g. primavera-p6-2) of the machine where Primavera P6 is currently installed. If Procore Drive is installed on the database server itself, you can enter 'localhost' or the computer's name.  
   *Tip:* To find your computer name, go to Start > Control Panel > System. Under the Computer Name section, copy and paste the value for 'Full Computer name' (do not include any ending period).
2. **Database Name**: Enter the databaseâs Oracle Connection String for this value. (e.g. XE)  
   *Tip:* To find this value, go to the login prompt for Oracle Primavera P6. The value next to Database is what you'll want to enter.
3. **Instance**: If Primavera P6 is locally installed on the machine (default), leave this field blank. If itâs installed on a network server, specify the instanceâs name on the network. (e.g. PRIMAVERA).
4. **Schema**: Enter the database schema name. (e.g. privuser)  
   *Note:* Any Oracle or SQL Server user account that has at least read-only access to the relevant P6 schedule information you want to integrate into Procore will work to use as the username and password you enter into Procore Drive.
5. **Database Credentials**: Enter your database credentials. Procore must use the login credentials for your âprivuserâ in order to access the required data from the P6 database.

   - **Username**: Enter the name of the private user. The default value is 'privuser'.
   - **Password**: Enter the matching password.
6. Click the **Test Connection** button to validate that the provided database information is correct. If it is not correct, please check your credentials and try again.
7. Click the **Save** button to save your changes.
8. Click the **Export Schedule** button to upload and apply the project schedule to your project in Procore. It will take a few minutes for your schedule to finish the upload process.
9. After you see the 'Export complete' message, log in to Procore and verify that you can see your schedule and all of its data under your projectâs Schedule tool.

---

## SQLite Database Instructions

1. Click **Browse**.
2. Select your SQLite schedule from your computer.
3. Click **Save**.
4. After you see the 'Export complete' message, log in to Procore and verify that you can see your schedule and all of its data under your projectâs Schedule tool.  
   *Note*: Any Oracle or SQL Server user account that has at least read-only access to the relevant P6 schedule information you want to integrate into Procore will work to use as the username and password you enter into Procore Drive.

## Next Steps

1. Navigate to the Project level **Schedule** tool in Procore's web application.
2. Use the various 'View by' options to change how the information is displayed.
3. See [Schedule](/product-manuals/schedule-project-beta/) for more tutorials on actions you can perform on an integrated schedule.  
   *Note*: Any Oracle or SQL Server user account that has at least read-only access to the relevant P6 schedule information you want to integrate into Procore will work to use as the username and password you enter into Procore Drive.
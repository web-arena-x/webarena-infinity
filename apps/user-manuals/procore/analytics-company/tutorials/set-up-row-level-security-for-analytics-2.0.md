# Set Up Row-Level Security for Analytics 2.0

Source: https://v2.support.procore.com/product-manuals/analytics-company/tutorials/set-up-row-level-security-for-analytics-2.0

---

## Background

If a user's Procore login credentials are the same as their Power BI login credentials, row-level security (RLS) filters can be set up in Power BI Desktop to limit a user's access in the Power BI service to data only from Procore projects they have been added to. For more information, see Microsoft's [Row-level security (RLS) with Power BI](https://docs.microsoft.com/en-us/power-bi/service-admin-rls) .

## Things to Consider

- **Required User Permissions**:

 - Your login information for Power BI and Procore must use the same email address.
 - You must be assigned the 'Viewer' role in the Power BI workspace.
 - If using the Procore OOTB Reports, the 'project\_users' table will be 'ProjectUser'.

## Steps

### Configure 'projects' and 'project\_users' Power BI Relationship

Configuring a Power BI relationship between the projects and project\_users tables connects the data from these tables. See Microsoft's [Create and manage relationships in Power BI Desktop](https://docs.microsoft.com/en-us/power-bi/desktop-create-and-manage-relationships) . Two options for configuring this relationship are outlined below.

#### Option 1

1. Open an Analytics report in Power BI Desktop.
2. On the Home tab, click **Manage Relationships**.
3. In the 'Manage relationships' window, scroll through the options and select **project\_users** **(project\_id)** and click **Edit**.
4. Complete the following in the 'Edit relationship' window:

   - Under 'Cardinality', select **Many to one (\*:1)** and mark the 'Make this relationship active' checkbox. These options should be selected by default.
   - Under 'Cross filter direction', select **Both** and mark the 'Apply security filter in both directions' checkbox.
5. Click **OK** to close the 'Edit relationship' window.
6. Click **Close** to close the 'Manage relationships' window.
7. Save the report.

#### Option 2

1. Open an Analytics report in Power BI Desktop.
2. Click the **Model** view.
3. Check the relationship between the 'projects' and 'project\_users' tables. The relationship should have a (1) next to the 'projects' table and an asterisk (\*) next to the 'project\_users' table.

   ##### Â Tip

   To only view the relationship betweeen the 'projects' and 'project\_users' tables (as shown below), click the plus icon (+) next to the 'All tables' tab to create a new layout and add the 'Project' and 'ProjectUser' tables to the layout by dragging and dropping them from the Properties > Fields menu into the gray space.

- Select the relationship by double-clicking on the connecting line between them.
- Complete the following in the 'Edit relationship' window:

 - Under 'Cardinality', select **Many to one (\*:1)** and mark the 'Make this relationship active' checkbox. These options should be selected by default.
 - Under 'Cross filter direction', select **Both** and mark the 'Apply security filter in both directions' checkbox.
- Click **OK** to close the 'Edit relationship' window.
- Save the report.

### Create a New RLS Role

1. On the 'Modeling' tab, click **Manage Roles**.
2. In the 'Manage roles' window, complete the following in each column:

   - In the 'Roles' column, click **Create** and enter a name for the role in the 'New role' field. *Project User* is the role name used in the image below.
   - In the 'Tables' column, select **project\_users**.
   - Select **Switch to DAX editor**.
   - In the 'Table filter DAX expression' column, enter **[email\_address] = userprincipalname()**.
3. Click **Save** in the 'Manage security roles' window.
4. Save and publish the report.

### Add Users to a RLS Role

Once the RLS table relationship is configured, users must be added to RLS roles in the Power BI service in order to view a Procore Analytics report. For more information, see Microsoft's [Row-level security (RLS) with Power BI: Working with members](https://docs.microsoft.com/en-us/power-bi/service-admin-rls#working-with-members) .

1. Open a Procore Analytics report in the Power BI service.
2. Under 'Datasets', click the ellipsis (...) next to the report you want to set up RLS for and click **Security**.
3. Select the role you want to add one or more users to.

   ##### Â Tip

   Using Office 365 Distribution Groups can simplify the process of adding multiple users to an RLS role at one time. See Microsoft's [Get started with Microsoft 365 Groups in Outlook](https://support.office.com/en-us/article/get-started-with-office-365-groups-in-outlook-b86c141b-39cf-49d9-a4db-124c3d786204) .

- Enter their email addresses and click **Add**.
- Click **Save**.
# Connect Power BI Report to Read Only Replica

Source: https://v2.support.procore.com/product-manuals/procore-analytics/tutorials/connect-power-bi-report-to-read-only-replica

---

## Background

The Azure read replica feature allows you to duplicate data from your Procore database. Duplicating your data will cause 'read' operations (report refreshes) to no longer contend with 'write' operations (data syncs) for server resources.

## Things to Consider

- **Required User Permissions**:

  - 'Admin' level permissions on the Company level Admin tool.

## Steps

1. Open a Procore Analytics Report in Power BI .
2. Select **Transform Data** from the **Home** tab.
3. Select the appropriate table.
4. Go to the **Query Settings** panel on the right.
5. Click the  icon next to **Source**.
6. Select **Enable SQL Server Failover support**.
7. Select **OK**.
8. Optional:For queries where editing the source step is not possible, such as budget queries with parameters, add 'MultiSubnetFailover=true' at the end of the **SQL statement**.

##### Â Note

These options can also be set when connecting to your SQL Server with a program such as SSIS or Azure Data Studio:

1. Connect to your SQL Server.
2. Click **Options**, then select **Additional Connection Parameters**.
3. Add 'Application=ReadOnly' in the space provided.
4. Select **Connect**.
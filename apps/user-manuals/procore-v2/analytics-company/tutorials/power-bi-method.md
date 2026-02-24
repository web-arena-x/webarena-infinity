# Power BI Method

Source: https://v2.support.procore.com/product-manuals/analytics-company/tutorials/power-bi-method

---

## Steps

1. Navigate to Procore Analytics from your **Company Tools** menu.
2. Go to the **Getting Started** section.
3. Under **Power BI Files**, select and download the available Power BI reports.
4. Log in to the [Power BI service](/process-guides/getting-started-with-analytics/upload-reports-to-power-bi-if-applicable) using your Power BI login credentials.
5. Create a workspace where you want to store your company's Procore Analytics reports. See [Microsoft's Power BI support documentation](https://learn.microsoft.com/en-us/power-bi/) for more information. 
   *Notes:* Licensing requirements may apply.
6. In the workspace, click **Upload**.
7. Now click **Browse**.
8. Select the report file from its location on your computer and click **Open**.
9. After uploading the file, click **Filter and select Semantic Model**.
10. Hover your cursor over the row with the report's name and click the vertical **ellipsis**icon.
11. Click **Settings**.
12. On the settings page, click **Data source credentials** and then click **Edit Credentials**.
13. In the 'Configure [Report Name]' window that appears, complete the following:

- **Authentication Method:** Select 'Key'.
- **Account Key**: Enter the token you received from the token generation page in Procore.
- **Privacy level setting for this data source**: Select the privacy level. We recommend selecting 'Private' or 'Organizational'. See [Microsoft's Power BI support documentation](https://learn.microsoft.com/en-us/power-bi/)for more information about the privacy levels.

1. Click **Sign in**.
2. Click **Scheduled refresh** and do the following: 
   *Note:* You may add up to 8 refresh times.

- Click the 'Keep your data up to date' toggle to the ON position.
- **Refresh frequency**: Select 'Daily'.
- **Time zone**: Select the time zone you want to use for scheduled data refreshes.
- **Time**: Click **Add another time** and select 7:00 a.m.
- *Optional*:\* Mark the 'Send refresh failure notifications to the dataset owner' checkbox to send refresh failure notifications.\* Enter the email addresses of any other colleagues you want the system to send refresh failure notifications to.

1. Click **Apply**.
2. To verify that the settings were configured correctly and that the report's data will refresh properly, return to the 'Filter and select Semantic Model' page and complete the following steps:

- Hover your cursor over the row with the report's name and click the circular arrow icon to refresh the data manually.

1. To verify that the settings were configured correctly and that the report's data will refresh properly, return to the 'Filter and select Semantic Model' page and complete the following steps:

- Hover your cursor over the row with the report's name and click the circular arrow icon to refresh the data manually.
- Check the 'Refreshed' column to see if there is a **warning** icon.\* If no warning icon displays, the report's data was successfully refreshed.\* If a warning icon displays, an error has occurred. Click the **warning** icon to see more information about the error.

1. To delete the blank dashboard the Power BI service created automatically, complete the following steps:

- Hover your cursor over the row with the dashboard's name. Click the **ellipsis** icon and click **Delete**.

1. To verify that the report renders properly, navigate to the 'All' or 'Content' page and click on the report's name to view the report in the Power BI service.

   ##### Â Tip

   Reference the 'Type' column to ensure you click on the report instead of a different asset.

- Repeat the steps above within Power BI for each Procore Analytics report file.
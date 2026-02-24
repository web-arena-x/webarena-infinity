# Upload Your Company's First Procore Analytics Files to the Power BI Service

Source: https://v2.support.procore.com/product-manuals/procore-analytics/tutorials/upload-your-companys-first-procore-analytics-files-to-the-power-bi-service

---

## Background

This tutorial covers information about uploading your company's first version of one or more Procore Analytics files to the Power BI service. If your company has already uploaded a previous version of a Procore Analytics file and you want to replace that file with an updated version, see [Upload Updated Procore Analytics Files to the Power BI Service](/product-manuals/procore-analytics/tutorials/upload-updated-procore-analytics-files-to-the-power-bi-service).

## Steps

1. Download a Procore Analytics report file from the Google Drive location provided to your company by the Procore Analytics team.
2. Log in to the Power BI service at <https://app.powerbi.com/> using your Power BI login credentials.
3. Create a workspace where you want to store your company's Procore Analytics reports. See [Microsoft's Power BI support documentation](https://learn.microsoft.com/en-us/power-bi/) for more information.
4. In the workspace, click **Upload**.
5. Click **Browse**.
6. Select the report file from its location on your computer and click **Open**.
7. After uploading the file, click **Filter and select Semantic Model**.
8. Hover your cursor over the row with the report's name. Click the vertical **ellipsis**icon and click **Settings**.
9. On the settings page, click **Data source credentials** and then click **Edit Credentials**.
10. In the 'Configure [Report Name]' window that appears, complete the following:

    - **Server**: This field is filled in automatically with 'constructionbi.database.windows.net'.
    - **Database**: This field is filled in automatically with 'Procore'.
    - **Authentication method**: Select 'Basic'.
    - **User name**: Enter the user name provided to your company by the Procore Analytics team.
    - **Password**: Enter the password provided to your company by the Procore Analytics team.
    - **Privacy level setting for this data source**: Select the privacy level. We recommend selecting 'Private' or 'Organizational'. See [Microsoft's Power BI support documentation](https://learn.microsoft.com/en-us/power-bi/)for more information about the privacy levels.
    - *Optional*: Mark the 'Report viewers access this data source with their own Power BI identities in DirectQuery mode.
    - Click **Sign in**.
11. Click **Scheduled refresh** and complete the following:

    - Click the 'Keep your data up to date' toggle to the ON position.
    - **Refresh frequency**: Select 'Daily'.
    - **Time zone**: Select the time zone you want to use for scheduled data refreshes.
    - **Time**: Click **Add another time** and select 7:00 a.m.
    - *Optional*:

      - Mark the 'Send refresh failure notifications to the dataset owner' checkbox to send refresh failure notifications.
      - Enter the email addresses of any other colleagues you want the system to send refresh failure notifications to.
    - Click **Apply**.
12. To verify that the settings were configured correctly and that the report's data will refresh properly, return to the 'Filter and select Semantic Model' page and complete the following steps:

    - Hover your cursor over the row with the report's name and click the circular arrow icon to refresh the data manually.
    - Check the 'Refreshed' column to see if there is a **warning**  icon.

      - If no warning icon displays, the report's data was successfully refreshed.
      - If a warning icon displays, an error has occurred. Click the **warning**  icon to see more information about the error.
13. To delete the blank dashboard that the Power BI service created automatically, complete the following steps:

    - Hover your cursor over the row with the dashboard's name. Click the **ellipsis**  icon and click **Delete**.
14. To verify that the report renders properly, navigate to the 'All' or 'Content' page and click on the report's name to view the report in the Power BI service.

    ##### Â Tip

    Reference the 'Type' column to ensure you click on the report instead of a different asset.

- Repeat the steps above for each Procore Analytics report file.
# Upload Updated Procore Analytics Files to the Power BI Service

Source: https://v2.support.procore.com/product-manuals/procore-analytics/tutorials/upload-updated-procore-analytics-files-to-the-power-bi-service

---

## Background

This tutorial covers information about replacing a previous version of one or more Procore Analytics files to the Power BI service. If your company has not already uploaded a version of a Procore Analytics file and you want to upload the first version, see [Upload Your Company's First Procore Analytics Files to the Power BI Service](/product-manuals/procore-analytics/tutorials/upload-your-companys-first-procore-analytics-files-to-the-power-bi-service).

##### Â Warning

Any changes made to a previous version of a Procore Analytics file (including adding or hiding pages, changing text, and changing visuals) will be overwritten when the file is replaced in the Power BI service.

## Steps

1. Download a Procore Analytics report file from the Google Drive location provided to your company by the Procore Analytics team.
2. Log in to the Power BI service at <https://app.powerbi.com/> using your Power BI login credentials.
3. Navigate to the workspace where your company's Procore Analytics reports are stored.
4. In the workspace, click **Upload**.
5. Click **Browse**.
6. Select the new report file from its location on your computer and click **Open**.
7. In the 'A dataset with the same name exists' window, click **Replace it**.
8. To verify that the new report's data will refresh properly as scheduled, click **Filter** and select **Semantic Model**:

   - Hover your cursor over the row with the report's name and click the circular arrow icon to refresh the data manually.
   - Check the 'Refreshed' column to see if there is a warning icon.

     - If no warning icon displays, the report's data was successfully refreshed.
     - If a warning icon displays, an error has occurred. Click on the icon to see more information about the error.
9. To verify that the report renders properly, navigate to the 'All' or 'Content' page and click on the report's name to view the report in the Power BI service.

   ##### Â Tip

   Reference the 'Type' column to ensure you click on the report instead of a different asset.

- Repeat the above steps for each new Procore Analytics report file.
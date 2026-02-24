# Importing data from Salesforce into Sell

Source: https://support.zendesk.com/hc/en-us/articles/4408834112538-Importing-data-from-Salesforce-into-Sell

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

You can import contacts from Salesforce into Sell, but first you'll need to export them from Salesforce.

Due to Salesforce's limitations, you can only export data from your Salesforce account once every 30 days.

**To export your contacts**

1. Login to your Salesforce account and click on your name in the top right corner to reveal your account options, then click **Setup.**
2. In the left side menu of the Setup page, click Data Management. It is listed under the Administrator options.
3. Click to request an export of all your salesforce.com data. 
    Select these options:
   - Unicode UTF-8 for the file encoding
   - Replace carriage returns with spaces

     Note: Uncheck the Include images, documents, and attachments box. Sell cannot import these files and including these types of data will cause the Sell import to fail.
4. In the exported data section of the same page, check Include all data.
5. Click **Start Export**.

Due to differences in the way Zendesk Sell and Salesforce handle user data, some categories might be changed (but not lost) in the import process.

For example:

- Categories such as Account and Contact are assigned to Sell as Contacts, and as company entries in the Contacts list
- Opportunities are assigned as Deals
- Leads are imported as Leads and retain their statuses (including custom lead statuses)
- All custom fields are retained and imported

 You are now ready to import your Salesforce data to Sell.

**To import your data into Sell**

1. Click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then select [**Data > Import**](https://app.futuresimple.com/settings/imports).
2. Select the application you're importing from: **Salesforce.**
3. Click **Upload** and select the file you exported from Salesforce.
4. Click **Import**.  
   Your contacts will appear in Zendesk Sell shortly.
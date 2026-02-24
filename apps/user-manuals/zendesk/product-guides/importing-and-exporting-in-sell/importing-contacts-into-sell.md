# Importing contacts into Sell

Source: https://support.zendesk.com/hc/en-us/articles/4408843688346-Importing-contacts-into-Sell

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

You can import contacts into Sell from a variety of sources, but first you must export them from those sources. Learn how to export contacts from an external source, how to [create a CSV file](https://support.zendesk.com/hc/en-us/articles/4408838742682), and how to import your contacts into Sell in a .CSV file or VCF (vCard).

This article covers the following topics:

- [Exporting contacts from Outlook](#topic_ew5_yvm_ktb)
- [Exporting contacts from Google](#topic_l2d_zvm_ktb)
- [Exporting a CSV file from Google spreadsheets](#ariaid-title4)
- [Exporting contacts from iCloud](#topic_ijl_zvm_ktb)
- [Exporting contacts from LinkedIn](#topic_avt_zvm_ktb)
- [Exporting contacts from Zoho](#topic_tmn_1wm_ktb)
- [Exporting contacts from Salesforce](#topic_zmd_1bm_mtb)
- [Importing contacts into Sell](#topic_lfj_cnj_ltb)

## Exporting contacts from Outlook

Before you can import contacts from your Outlook account (OWA) into Sell, you must first export them from Outlook.

**To export your contacts from Windows Outlook**

1. Log on to your [Outlook account (OWA)](https://outlook.office365.com)
2. On the menu on the left, click **Contacts**.
3. Select your contacts.
4. In the top, right corner, click **Settings** (![](https://lh3.googleusercontent.com/r0cxjqI_eBpDzaNjjE4XpR8GGPVWNQY1J5I_VmzohBBkie2ackoHbONmYjAamF4g1iLBDRYecKDgYbVE9hs48mXS4jEWZNTGONFK-dwJsKsArl2--ruqoPner3CIQIFQFiX6cxYo66P4IWjHgA)) > **Manage**.
5. Click **Export contacts**.
6. Choose the folder you want to export.
7. Click **Export**.

Note: Currently, exporting custom fields in a .CSV file by default is not supported by Microsoft Outlook. However, you can export custom fields by using an Outlook desktop client for Windows with a [plugin](https://www.codetwo.com/freeware/outlook-export/).

You are now ready to [import your data into Sell](#topic_lfj_cnj_ltb).

**To export private/non-private contacts**

1. Export your contacts to a .PST file.
2. Convert the .PST file to an .CSV file, or use an extra [plugin](https://www.codetwo.com/freeware/outlook-export/).

Note: Splitting contacts into private/non-private is only supported for Windows Outlook clients. It is not supported for OWA and Mac desktop clients.

**To export contacts from Mac OS Outlook 2017 or later**

1. [Log in to OWA](https://outlook.office.com/mail/).
2. Follow the instructions on the Microsoft website.

You are now ready to [import your data into Sell](#topic_lfj_cnj_ltb).

**To export contacts from Mac OS Outlook 2011 or 2016**

1. In Outlook, click **File > Export**.
2. Under **What do you want to export?**, select **Contacts to a list**, then click the right arrow.
3. Under **Where**, select your path.
4. Under **Save As**, enter Outlook Contacts.
5. Click **Save**, then click **Done**.
6. Next, open Microsoft Excel, and click **File > Open**.
7. Click the **Outlook Contacts.txt** file you saved, then click **Open**.
8. In the **Text Import Wizard**, select **Delimited**.
9. Under **Start**, enter 113.
10. Under **File origin**, select **Macintosh**.
11. Click **Next**.
12. Under **Delimiters**, select **Tab**.
13. Click **Next**.
14. Under **Column data format**, click **General**.
15. Click **Finish**.
16. Click **File** > **Save As**. Enter Outlook Contacts.
17. Under **Where**, select the path to save the .CSV file to.
18. Under **File Format**, click **MS-DOS Comma Separated**.
19. Click **Save** > **Continue**.

You are now ready to [import your data into Sell](#topic_lfj_cnj_ltb).

## Exporting contacts from Google

Before you can import contacts from Google into Sell, you must first download them as a .CSV file or VCF (vCard), taking the opportunity to ensure everything is formatted correctly, before you export them from Google.

**To export your contacts from Google Contacts**

1. Log in to Gmail, then click **Contacts**.
2. Select the checkbox next to the contacts you want to export. To bulk export all of your contacts, select the checkbox at the top left of the Contacts list.
3. In the top left corner, click **More** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) > **Export**.
4. Click **Google CSV** to back up your contacts.
5. Click **Export**, to save your file.

You are now ready to [import your data into Sell](#topic_lfj_cnj_ltb).

Zendesk also supports a two-way sync for your contacts in Sell and Google.

**To integrate your Sell contacts with Google**

1. On the Sell sidebar, click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then click [**Data > Import new data**](https://app.futuresimple.com/settings/imports).
2. Click **Google contacts**.
3. Click **Integrate with Google**.
4. Click the account you want to integrate with Sell.
5. Review the integration terms, then click **Allow**.
6. Select what you want to integrate. For **Sync my Sell contacts with Google**, select the type of contacts you want to sync.
7. Click **Apply**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_contacts_google_synch.png)

**To disable the integration of your Sell contacts with Google**

1. On the Sell sidebar, click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then click **[Integrations > Integrations](https://app.futuresimple.com/settings/integrations)**.
2. Under **Google**, click **Disable**.

## Exporting a CSV file from Google spreadsheets

Before you can export your data from a Google spreadsheet, check the data in your spreadsheet to ensure everything is formatted correctly (see [Creating a CSV file to import leads, contacts, and deals](https://support.zendesk.com/hc/en-us/articles/4408838742682)).

**To export a .CSV file from Google Sheets**

1. Open the Google spreadsheet that contains the data that you want to export.
2. Click the tab that has the data you want to export.
3. On the top toolbar, click **File**. A drop-down menu appears.
4. Click **Download**. Another menu appears.
5. Click **Comma-separated values (.csv, current sheet)**.

The .CSV file containing your contacts downloads to your predefined location (for example, your Downloads folder). You are now ready to [import your data into Sell](#topic_lfj_cnj_ltb).

## Exporting contacts from iCloud

You can export your contacts from iCloud in a .VCF file. In Sell choose to import data as .VCF, then you can then drag the .VCF into Sell.

**To export a vCard of your contacts from iCloud**

1. Go to [iCloud](https://www.icloud.com) and log on to your account.
2. Click **Contacts**, select one or more contacts in the contacts list.
   - To select multiple contacts, use CMD + click (iOS) or CTRL+ click (Windows).
   - To bulk select all of your contacts, click the first contact in the list then SHIFT + click the last contact in the list.
3. On the sidebar, click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then **Export vCard**.

If you select multiple contacts, Contacts exports a single vCard containing all of them. You are now ready to [import your data into Sell](#topic_lfj_cnj_ltb).

## Exporting contacts from LinkedIn

You can export your contacts and connections from LinkedIn to a .CSV file, ready to import into Sell.

**To export your contacts from LinkedIn**

1. In LinkedIn, on your **Profile** page, click the **Me** dropdown menu.
2. Under **Account**, click **Settings & Privacy**.
3. In the left hand menu, click **Data privacy**.
4. Under **How LinkedIn uses your data** > **Get a copy of your data**, click **Change**.
5. Select whether you want to bulk download everything (for example, connections, contacts, account history) or specific data (such as imported contacts and connections).
6. Click **Request archive**.
7. Enter your LinkedIn password and click **Done**. Your request is pending while LinkedIn sends you an email with a download link.
8. Click the download link in your notification email.
9. In LinkedIn, click **Download archive**.

The .CSV file containing your data is immediately downloaded. You are now ready to [import your data into Sell](#topic_lfj_cnj_ltb).

## Exporting contacts from Zoho

You can export your contacts from Zoho ContactManager as a .CSV file using the following instructions. If you have a lot of contacts to export (over 2000), then first [create a report](http://www.zoho.com/crm/help/reports/) to export to Excel, then continue to export the records as a .CSV file.

**To export your contacts from Zoho ContactManager**

1. Log on to **Zoho ContactManager**.
2. Click **Contacts module**.
3. Click **Export**.
4. Click **Select all**.
5. Click **Export**.

Your contacts are exported as a .CSV file and you are now ready to [import your data into Sell](#topic_lfj_cnj_ltb).

## Exporting contacts from Salesforce

You must first [export your contacts from Salesforce](https://support.zendesk.com/hc/en-us/articles/4408834112538), before you can import them into Sell.

Note: Salesforce limits how often you can export your data from your Salesforce account, which is once every 30 days.

After you've finished exporting your contacts from Salesforce, you are ready to [import your data into Sell](#topic_lfj_cnj_ltb).

## Importing contacts into Sell

After you have exported your contacts from another source, you can import them into Sell.

**To import your contacts from another source**

1. On the Sell sidebar in Sell, click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then click [**Data > Import new data**](https://app.futuresimple.com/settings/imports).
2. Click .CSV or .VCF or the application you're importing from.
3. In **Importing data**, select the type of data you are importing (Leads, Contacts, or Deals and Contacts).
4. Either
   - Drag and drop the .CSV or .VCF file onto the **Importing data** page
   - Click **Select file**, then select the .CSV or vCard (.VCF file) that you've exported from another source.
5. Click **Next**.
6. Under **We need some more information to complete your import**, review how you want Sell to import your data.
7. Click **Next**.
8. For the information found, use the dropdown menus to match your columns to the Sell fields.
9. Click **Show summary**.
10. Review your import selections, then click **Import**.

Your contacts appear in Zendesk Sell shortly afterwards.
# Installing and using the Advanced Search app

Source: https://support.zendesk.com/hc/en-us/articles/4408830673306-Installing-and-using-the-Advanced-Search-app

---

The [Advanced Search app](https://www.zendesk.com/apps/support/198393/advanced-search/) is a tool for building complex search queries against tickets in Zendesk Support by using a form. The results are displayed in table form or can be exported as a CSV file. The app is available in the [Zendesk Marketplace](https://www.zendesk.com/apps/support/advanced-search). 

This article contains the following topics:

- [Installation](#h_5e1e8c89-e124-4ed6-92c6-f10218e03279)
- [Using the Advanced Search app](#h_cf631d39-194c-458e-87b6-a917e3115be3)
- [Searching custom fields](#h_49f77529-1181-4916-a33f-81577ec50f0b)
- [Exporting search results to CSV](#h_f5133dc6-f21b-4c4e-93fd-64ee5b84fa45)
- [Release Notes](#h_94659fa1-f93b-4964-8315-96a77dd5dd4e)

## Installation

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Apps and integrations** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)) in the sidebar, then select **Apps > Zendesk Support apps**.
2. Click **Marketplace** at the top of the page and then enter "Advanced Search" in the Marketplace search bar.
3. Double-click on the Advanced Search app icon, and click **Install**.
4. In the Installation section, enter a name for the Advanced Search, enable group and role restrictions if required. These configuration options are also available after installation by navigating to  **Admin** > **Apps** > **Manage.**
5. On the app details page, click **Install.**

## Using the Advanced Search app

Click on the **Advanced Search** icon on the left sidebar, and the full-page application opens in a tab:

![](https://support.zendesk.com/hc/article_attachments/7856365060762)

You can search for all the fields displayed, including searching date fields using a "between" operator.  Multiple search criteria can be used at the same time, and multiple criteria are joined using "AND." You can also choose which columns are displayed in the results.

Search for data in custom user fields and custom organization fields using the key that identifies the custom field.

To return all results, enter an asterisk (**\***) in the Search field, then click **Search**.

### Turning on group and organization names

By default searching tickets will return the group\_id and org\_id rather than the names.  If you want to enable the display of the names then these 2 settings have to be enabled.

![mceclip0.png](https://support.zendesk.com/hc/article_attachments/4408852536090)

**Note:  If your account has a large amount of groups or orgs, you will want to wait for about 20 seconds after opening, before performing a search.**

### Searching custom fields

Custom fields can only be searched by keywords.  For example, to search for the word "Platinum" across all custom fields, enter "Platinum" in the search box.

![](https://support.zendesk.com/hc/article_attachments/7856387547034)

To search for multiple values across all custom fields, enter a space between each keyword or phrase.  This example searches for "Standard" in one custom field and "Diamond" in another custom field. This also returns results if both keywords are in the same custom field.

![](https://support.zendesk.com/hc/article_attachments/7856365060250)

### Exporting search results to a CSV

Once a search is done, you have the ability to click into any of the results. The results can also be exported in CSV format by clicking the **Download CSV.**

![](https://support.zendesk.com/hc/article_attachments/7856365059866)
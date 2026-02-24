# Setting up and using smart links in Sell

Source: https://support.zendesk.com/hc/en-us/articles/4408824279962-Setting-up-and-using-smart-links-in-Sell

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

Smart links let you quickly access other applications or web pages from your Zendesk Sell account. If you have systems that use a unique URL ID, you can use smart links to dynamically link to them from your leads, contacts, and deals in Sell.

**Note**: Smart links are available on both the web and [mobile app](https://getbase.com/download/), but must be set up from Sell [web settings](https://app.futuresimple.com/settings/profile).

This article covers the following topics:

- [Configuring smart links](#h_6f66e8d4-f3c5-4aae-b9f8-6377ad373e78)
- [Examples of using smart links](#h_aa3cae48-9253-495c-9524-3015ed16f7c4)
- [Using smart links from a mobile device](#h_dfd788ba-6006-40f0-b404-492e31aba821)

## Configuring smart links

You must configure smart links before you can use them, and you'll also need to create a custom field to hold the unique identifier (see [Creating and managing custom fields](#h_aa3cae48-9253-495c-9524-3015ed16f7c4)).

You need admin rights to configure smart links.

**To configure smart links**

1. Click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then select **[Customize > Leads](https://app.futuresimple.com/settings/leads/)**for leads, **[Customize > Contacts](https://app.futuresimple.com/settings/contacts/)**for contacts, or **[Customize > Deals](https://app.futuresimple.com/settings/deals/)** for deals.
2. If you haven't done so already, on the **Fields**  tab, create a custom field to hold your unique identifier. For example, we've used a custom field called **YouTube video**.  
   Note: The custom field used for storing a unique identifier must be a "Single Line Text" field type (see [Creating and managing custom fields](https://support.zendesk.com/hc/en-us/articles/4408838289562-Creating-and-managing-custom-fields)).  
   Each YouTube video has a unique identifier at the end of its URL, for example:  
   https://www.youtube.com/watch?v=**dQw4w9WgXcQ**. This would be the unique identifier that you enter into the custom field on your contact card.
3. Select the **Smart links**tab.
4. Click **Add Smart Link** to start setting up your new link.
5. Give your smart link an App name and URL.  
   For example, if you were setting up a smart link for YouTube, the App name might be **YouTube** and the URL would be:  
   <https://www.youtube.com/watch?v=>
6. Click **Insert merge tag** to add the custom field that you've used to store the unique identifier.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_smart_link_overview.png)
7. Choose where the application should open.  Click either the **Open in new window** or **Open inside Sell**.
8. Click **Save**to save the new smart link.
9. On a contacts page, add a value to the new custom field, for example, dQw4w9WgXcQ.  
   You'll see a new **Smart Links**button appear on the right side of your lead, contact, or deal page and you'll see the new smart link as a clickable link. Click the link to take you directly to your application or web page.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_smart_link_card.png)

## Examples of using smart links

You can see one example of using smart links to link to a video site like YouTube in [Configuring smart links](#h_6f66e8d4-f3c5-4aae-b9f8-6377ad373e78).

### Tracking ID example

A common example for using smart links is to track shipments. For example, you could set up a custom field called **Tracking ID** on each deal.  The field would be updated with the tracking ID when a shipment is made. A URL link including this ID would take you to the tracking details page provided by the courier. You could then create a smart link so that you can click the tracking ID and view the shipment progress for that deal.

### Reporting and billing system example

Some customers use smart links to connect to reporting systems or ERP billing systems. For example, you could set up a custom field called **Reporting system**.  The field would contain an external ID, for example, 123990092. A URL link including this ID would take you to the reporting details page for that contact. You could then create a smart link so that you could click your company's equivalent of:   
https://abcinc.tableau.com/views/customer/**123990092**/dashboard   
to view the reporting details.

## Using smart links from a mobile device

You can access smart links from your Sell mobile app (iOS or Android) to quickly jump to other apps or web pages on your mobile device.

Click **Smart links**from the app, and you'll see the list of smart links you have configured.  Click to access the application or web page.
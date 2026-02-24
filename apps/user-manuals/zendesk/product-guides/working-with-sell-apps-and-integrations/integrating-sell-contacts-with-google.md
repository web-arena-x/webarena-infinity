# Integrating Sell contacts with Google

Source: https://support.zendesk.com/hc/en-us/articles/4408834233498-Integrating-Sell-contacts-with-Google

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

Important: Enabling this functionality leverages Google API Services. Zendesk’s use and transfer to any other app of information received through the Google API Services connecting Zendesk Sell to your Gmail accounts will adhere to Google's Limited Use Requirements described in the [Google API Services: User Data Policy](https://developers.google.com/terms/api-services-user-data-policy).

As described in [Integrating your Google Calendar in Sell](https://support.zendesk.com/hc/en-us/articles/4408843420314), you can add an external Google calendar to manage your calendar appointments in Sell, and if you want to integrate tasks between Sell and Google, this is described in [Integrating Sell tasks with Google](https://support.zendesk.com/hc/en-us/articles/4408834630042).

Using the Google integration that is available in Sell, you can sync your Google contacts with Sell. However, Google has a limitation of 25,000 contacts that can be synced *from* Sell *to* Google Contacts. Sell has no such limitation.

Note: Google is available as an app in Zendesk Marketplace (see [Google for Sell](https://www.zendesk.com/apps/sell/google-for-sell/?source=new_apps)).

**To sync your Google contacts with Sell**

1. Click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then select [**Integrations > Integrations**](https://app.futuresimple.com/settings/integrations).
2. Locate the Google integration in the list of integrations and then click **Enable**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-google-integration.png)
3. You’ll be prompted to allow Sell to integrate with your Google account. Click **Integrate Sell with Google**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-google-integration-setup.png)
4. As part of the Google authorization process, you’ll then be prompted to choose the Google account you want to use to integrate with Sell. Choose the account you want to use then click **Allow**.
5. Select the **Sync my Sell contacts with Google**, then click **Apply**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-google-integration-sync-settings.png)

Note: You can select contact groups, rather than all of your contacts, if you prefer.

The integration set up is now complete and you’ll see a new contacts group called **Base CRM** in your Google Contacts page. Sell and your Google contacts are now synced, which means that when you create a new contact in Sell it will also appear in your Google contacts and vice versa.

In Sell, every new contact that was synced from Google is tagged with ‘from google’ (or the name of the Google contact group it came from).

Note: Zendesk Sell and Google sync every 15 minutes; therefore, you may not immediately see new contacts in both Sell and Google.

Some other important notes about how contacts sync in this integration:

- Each of your team members can enable the Google contacts integration for any Google account they have access to, but each user can only integrate with a single Google account at a time. Only the Sell contacts owned by the user will be synced to their Google account.
- After the initial sync with Google, Sell only syncs new contacts that you add to Google.
- If you delete a synced contact in Google, it will not be deleted from Sell.
- If you delete a contact in Sell, it will not be deleted from the **Base CRM** contact group in Google. Sell does not delete anything from your Google contacts.
- Updates to contacts follow these rules:

- If you update a contact in Google that originated in Google, the update will be synced to Sell.
- If you update a contact in Google that originated in Sell, the update will not be synced to Sell.
- If you update a contact in Sell, the update will not be synced to Google.

- If you move a synced contact in Google to a different contact group in Google, the sync tag that was added in Sell will not also be updated. The ‘from google’ tag is only added when a contact is first synced into Sell.
- Only person contacts are synced from Sell to Google. Company contacts are not synced.

Note: We recommend using the Google contacts integration as a quick way to add your contacts from Google into your Sell account. After adding your contacts from Google, we recommend using Sell as the master contacts database and make all your updates and deletions in Sell.
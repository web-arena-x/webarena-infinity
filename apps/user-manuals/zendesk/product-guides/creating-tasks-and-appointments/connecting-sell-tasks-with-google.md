# Connecting Sell tasks with Google

Source: https://support.zendesk.com/hc/en-us/articles/4408834630042-Connecting-Sell-tasks-with-Google

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

Important: Enabling this functionality leverages Google API Services. Zendesk’s use and transfer to any other app of information received through the Google API Services connecting Zendesk Sell to your Gmail accounts will adhere to Google's Limited Use Requirements described in the [Google API Services: User Data Policy](https://developers.google.com/terms/api-services-user-data-policy).

As described in [Integrating your Google Calendar in Sell](https://support.zendesk.com/hc/en-us/articles/4408843420314), you can add an external Google calendar to manage your calendar appointments in Sell. Using the Google integration that is available in Sell, you can also sync your Google tasks.

Integrating contacts between Sell and Google is described in [Integrating Sell contacts with Google](https://support.zendesk.com/hc/en-us/articles/4408834233498).

**To sync your Google tasks with Sell**

1. Click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then select [**Integrations > Integrations**](https://app.futuresimple.com/settings/integrations).
2. Locate the Google integration in the list of integrations and then click **Enable**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-google-integration.png)
3. You’ll be prompted to allow Sell to integrate with your Google account. Click **Integrate Sell with Google**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-google-integration-setup.png)
4. As part of the Google authorization process, you’ll then be prompted to choose the Google account you want to use to integrate with Sell. Choose the account you want to use then click **Allow**.
5. Select the **Sync my Sell tasks with Google**, then click **Apply**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-google-integration-sync-settings.png)

The integration set up is now complete and you’ll see a new calendar called **Base Tasks** in your Google account. Tasks that you create in Sell *for contacts and deals* will appear in this new Google Calendar.

Note: Zendesk Sell used to be called Base.

Some other important notes about how tasks sync in this integration:

- Tasks that are not associated with a contact or deal will not be synced to the Google calendar.
- To see a Sell task in the Google calendar, you must be the owner and the creator of the task in Sell. For example, If an admin creates a task and assigns it to you, you won't see it in your Google Calendar.
- Sell does not delete anything from your Google calendar. If you delete a task in Sell, it will not be deleted from the **Base Tasks** calendar in Google.
- However, if you delete a synced task in Google, it will be deleted from Sell.
- Tasks that you create directly in the integrated Google calendar are not synced to Sell. You may however edit the tasks that were created in Sell that have been synced to your Google calendar.

Note: Zendesk Sell and Google sync every 15 minutes; therefore, you may not immediately see new tasks in both Sell and Google.
# Managing duplication settings in Sell

Source: https://support.zendesk.com/hc/en-us/articles/4408821762458-Managing-duplication-settings-in-Sell

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

To prevent duplicates in Zendesk Sell, you can configure what fields must match in order to merge two similar contacts or leads.

Choosing a deduplication strategy means that Sell will use the settings you choose to merge contacts or leads during imports, or during lead conversion.

This method applies to automated methods of adding items, like importing and lead conversion, not to manually adding a contact or lead.

**To configure a deduplication strategy**

1. Click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then select [**Data > Duplicate Management**](https://app.futuresimple.com/settings/deduplication).
2. Click **Configure** to change the default duplicate management configuration.

   If you don't edit the settings, Sell uses a default configuration to detect duplicates that is based on Name, and either Email or Phone Number.
3. Choose which fields you’d like to include when detecting duplicates.

- Make sure that either Name, Email, or Phone is checked - at least one of them is required to detect duplicates.
- Choose which fields can be empty when Sell is matching your chosen fields together.

 For example, you might have chosen to match Name, Email, Phone, and LinkedIn fields, but also specified that the LinkedIn field can be empty. For example, if Sell finds two contacts and one contact has a LinkedIn entry, and the Name, Email, and Phone fields match between the two contacts, Sell will merge these two contacts together.

- Note that at least one field must have an entry to accurately make matches.
- Click **Save**.

The next time that you import a file or convert a lead to a contact, Sell uses these settings to deduplicate your leads and contacts.
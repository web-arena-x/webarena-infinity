# Merging leads or contacts

Source: https://support.zendesk.com/hc/en-us/articles/4408836188442-Merging-leads-or-contacts

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

If you discover that you’ve added duplicate versions of leads or contacts, you can easily merge the two (or more) records into one. Specifically, you can merge one or more contacts with a contact, or one or more leads with a lead.

This article contains the following topics:

- [Best practices for merging leads or contacts](#topic_xm3_3m4_3nb)
- [Merging leads or contacts](#topic_ym3_hm4_3nb)
- [Interesting facts about merging leads or contacts](#topic_dyh_gm4_3nb)

Related articles:

- [Using smart lists to bulk update and take action on your leads, contacts, and deals](https://support.zendesk.com/hc/en-us/articles/4408828971290-Using-smart-lists-to-batch-update-and-take-action-on-your-leads-contacts-and-deals)

## **Best practices for merging leads or contacts**

While you can merge multiple records in Leads or Contacts, you cannot merge leads with contacts. However you can convert a lead into a contact (but the not the other way round).

*Before* you merge two or more records together, check the following:

- The information is correct
- There are no typos
- The information is consistent (for example, the names and phone numbers match)

If the information was inconsistent (for example the records had two different phone numbers) then Sell automatically creates additional custom fields to retain the non-identical information.

**To clean up the additional fields**

1. In Sell, click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)), then go to**Customize > Leads** or **Customize > Contacts**.
2. In **Fields**, click the trashcan (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_reset_query.png)), icon next to the field you want to delete.

   Note: Deleting the field also deletes the data of that field.

## **Merging leads or contacts**

You can access the merge feature from the **Index** or **Table** views in the **Leads** and **Contacts** pages.

You must have permissions to update and delete leads or contacts in order to merge them.

**To merge leads or contacts**

1. From the **Leads** or **Contacts** page, use either the **Index** or **Table** views to select the duplicate records.

   ![Sell merge leads](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_merge_leads.png)
2. Click the **Merge** button.
3. You’ll be prompted to confirm that you want to merge the records.

   ![Sell merge leads confirm](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_merge_leads_confirm.png)
4. Click **Merge**.

The topmost selected record is the one that the other record(s) will be merged into. You’ll see a confirmation of the merge in the notes for leads or contacts.

![Sell merge note](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_merge_note.png)

## Interesting facts about merging leads or contacts

The merge feature follows certain rules and has the following limitations:

- If the records you've merged had different values in the same data field, Sell automatically creates a custom field to store this data. None of your data is deleted. For example, if the email field contained different values, Sell creates a new custom field called *Email#1* and preserves the data.
- You can merge up to 5 records at one time.
- You can’t merge a person contact into a company contact.
- You can’t merge person contacts that have different companies assigned to them.
- You can’t merge a lead into a contact, and vice versa.
- You can convert a lead into a contact.
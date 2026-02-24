# Converting leads in Sell

Source: https://support.zendesk.com/hc/en-us/articles/4408834823066-Converting-leads-in-Sell

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

After progressing an opportunity with a potential customer (your lead) through the sales pipeline, the lead becomes a qualified lead. The next step is to convert them from a lead to a contact. At this stage, you can also create a new deal for the converted lead and create a task for it, such as follow-up with the potential customer.

When you convert leads to contacts, the contact details automatically merge. Best practice is to adjust the deduplication settings to ensure customer leads don't merge with an unrelated contact that shares the same name (even if the contact is connected to a different company).

This article covers the following topics:

- [Converting a lead to a contact in Sell](#topic_nwf_hxg_fxb)
- [Converting leads in bulk](#topic_ghl_3xg_fxb)
- [Considerations for relevant conditions and rules](#topic_afs_jxg_fxb)

## Converting a lead to a contact in Sell

There are two ways you can convert a lead to a contact: via the Sell REST API or manually in Sell. To create or read lead conversions using the Zendesk REST API, see [Lead conversions](https://developers.getbase.com/docs/rest/reference/lead_conversions).

**To convert a lead to a contact in Sell**

1. On the Sell sidebar, click the **Leads** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_lead_icon.png)) icon, then click the lead you want to convert.
2. Click **Convert**.
3. Update the profile information of the lead as needed.
4. (Optional) You can also create a new deal or task by selecting the checkbox for **Create a deal for the converted lead** or **Create a task for each converted lead**.
5. Click **Convert**.

Note: If you want to convert a lead to a contact, and a name exists on the lead record, then a person contact will be created. If a company name also exists on the lead record, then the company contact will also be added. If a company name exists, but not the name of a person - then a person contact won't be created at all, (just a company).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-convert-lead.png)

## Converting leads in bulk

You can also convert multiple leads at one time using either the **Index** or **Table** views on the **Leads** page.

**To convert leads in bulk**

1. On the Sell sidebar, click the **Leads** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_lead_icon.png)) icon, then click the check box next to the name of the leads that you want to convert.
2. (Optional) Make any modifications to the lead name and company prior to the conversion.
3. When you have selected all of the leads or contacts that you want to convert, click **Convert** at the top of the list.

   You will see a dialog similar to the one for converting a single lead. You won’t have the option to edit the lead name and company.
4. (Optional) You can create a new deal or task by selecting the checkbox for **Create a deal for the converted lead** or **Create a task for each converted lead**.
5. Click **Convert**.

Your leads are converted to contacts and if you add any new deals and tasks, then they are included on the contact card of the lead. New deals are classified as **Incoming** in your sales pipeline.

The following conditions and rules apply when converting leads to contacts:

- A lead’s tags are handled in the following ways:
  - When you convert a lead, their tags are also added to the new contact card and the new deal card, (if you had chosen that option).
  - If you chose to also add a deal when converting, the lead’s tags are added to the **Tags** tab in the **Prospects and Customers** settings page.
  - If you did not create a deal when converting a lead, then their tags are only added to the **Tags** tab in the **Contacts** settings page.
  - If you change a contact from a prospect or customer back to a regular contact, no tags are removed, (all tags remain).
- If you have allowed it, when you convert a lead to a contact, your custom fields are also transferred into the new contact card. You can define this when you set up the custom field (see [Creating and managing custom fields](https://support.zendesk.com/hc/en-us/articles/4408838289562)).
- When you convert multiple leads in bulk and choose to also create a new deal, the new deal is named after the lead’s name. You can edit the deal to update the name as needed.
- Converting a lead to a contact is a one-way action in Sell. You cannot convert contacts back to leads. However, if you have accidentally converted a lead to a contact, then you have several options for undoing the conversion. For more information (see [Converting a contact back into a lead](https://support.zendesk.com/hc/en-us/articles/4408834839194)).
- When a lead is converted to a contact, the lead source field is not converted along with the other data. If you want to retain that data, store it in another field or create a deal when converting a lead to a contact so that the source field transfers to the deal and is not lost.
- A lead's notes are handled in the following ways:
  - When you convert a lead person to a company person, the notes on the lead person go to the company person.
  - When you convert a lead company to a contact company, the notes on the lead company go to the contact company.
- Default fields can't be modified as custom fields can. Therefore, if a lead has both a first name and a last name, plus a company name, this creates both a company contact and a person contact in the conversion, and the two different contacts inherit different fields accordingly:
  - A company contact inherits the following fields: Industry, Website, Address, and Tags
  - A person contact inherits the following fields: Mobile number, Work number, Email, Fax number, Socials (X, Facebook, Skype, Linkedin), Industry, Website, Description, Address, and Tags

Note: If a Deal card is created as a result of conversion, then the associated notes will also be reassigned to that deal.

## Considerations for relevant conditions and rules

When you create a lead, you must enter information into default fields. These fields have specific behavior that you cannot modify (unlike custom fields, which can be modified). Leads can contain a first name, last name, and a company name, which creates both a person and a company contact. With this in mind, consider the following default fields and their inheritances when converting leads.

- **Company Contact**: Inherits the following default fields: Industry, Website, Address, and Tags
- **Person Contact**: Inherits the following default fields: Mobile Number, Work Number, Email, Fax Number, Socials (X, Facebook, Skype, LinkedIn), Industry, Website, Description, Address, and Tags

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_error_message_prohibited_country.png)
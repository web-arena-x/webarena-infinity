# Creating and managing Sell custom fields

Source: https://support.zendesk.com/hc/en-us/articles/4408838289562-Creating-and-managing-Sell-custom-fields

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on all Sell plans](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_all.png)

In addition to the many data fields that are available for you to use on your leads,
contacts, and deals details pages, you can also create custom fields to store
additional information. For example, you can add a Skype name or an anniversary date
to the contact card. Use the Sell interface to add custom fields; you can't add them
via the API.

After you have added custom fields, you can also use them to filter your leads, contacts,
and deals by information specific to your business. To do this, set your custom fields
as filterable.

This article covers the following topics:

- [Adding custom
  fields](#sell_Creating_and_managing_custom_fields_in_sell__h_858631ff-39c2-4390-9719-0a75c31fccf4)
- [Setting the order of custom
  fields](#sell_Creating_and_managing_custom_fields_in_sell__h_aaa6f310-8b73-4b65-8b14-209c0c5d235d)
- [Editing and deleting custom
  fields](#sell_Creating_and_managing_custom_fields_in_sell__h_bcf85e0a-951d-4d6d-89ca-8eebefefb09d)

## Adding custom fields

You must have admin rights to create custom fields. Admins create and add custom
fields separately for leads, contacts, prospects and customers, and deals. Admins can define custom fields, that appear as additional fields, for
Sell users to add if they choose to.

After they’ve been added to the account, custom fields can be applied by all Sell
users.

Admins can create the following types of custom fields:

- Single Line Text
- Paragraph Text
- Number
- Checkbox
- Drop-down
- Multi-select
- Date
- Email
- Phone
- Address
- URL

Note: You can't use the following types of custom fields as filters: checkbox,
paragraph text, email, address, phone number, and URL.

**To add a custom field for leads**

1. On the Sell sidebar, click the **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_settings.png)) icon, then select [**Customize > Leads**](https://app.futuresimple.com/settings/leads).
2. Under **Custom fields**, click **Add Field**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-custom-field-lead.png)
3. Add the **Field Label**.
4. Select the **Field Type**.

   Be careful when you select the Field Type. You
   cannot [edit](#topic_gc3_52r_zvb) it later,
   instead you must delete and recreate the custom field.
5. Set the following options:

   - **Filterable**: When selected, you can use this field as a filter
     to view leads.

     Note: This filter only applies to reports, not smart
     lists.
   - **Value editable only by admin** : When selected, only admins can
     change the value of this field.
   - **Upon conversion transfer to deal** - Checking this box
     transfers the custom field to the deal card if a deal is created as
     part of the lead conversion process.
   - **Upon conversion transfer to person** - Checking this box
     transfers the custom field to the individual contact card if an
     individual contact's first and last name are present on the
     lead.
   - **Upon conversion transfer to company** - Checking this box
     transfers the custom field to the company contact card if a company
     name is present on the lead.
6. Click **Save**.

**To add a custom field for contacts**

1. On the Sell sidebar, click the **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_settings.png)) icon, then select [**Customize > Contacts**](https://app.futuresimple.com/settings/contacts).
2. Under **Custom fields**, click **Add Field**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-custom-field-contact.png)
3. Add the **Field Label**.
4. Select the **Field Type**.

   Be careful when you select the Field Type. You
   cannot [edit](#topic_gc3_52r_zvb) it later,
   instead you must delete and recreate the custom field.
5. Set the following options:

   - **Filterable**: When selected, you can use this field as a
     filter to view contacts.
   - **Value editable only by admin** : When selected, only admins can
     change the value of this field.
   - **Show on person cards** - Select this option if you want the
     custom field to appear on person cards.
   - **Show on company cards** - Select this option if you want the
     custom field to appear on company cards.
6. Click **Save**.

**To add a custom field for prospects and customers**

1. On the Sell sidebar, click the **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_settings.png)) icon, then select [**Customize > Prospects and Customers**](https://app.futuresimple.com/settings/sales_accounts).
2. Under **Custom fields**, click **Add Field**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-custom-field-prospect.png)
3. Add the **Field Label**.
4. Select the **Field Type**.

   Be careful when you select the Field Type. You
   cannot [edit](#topic_gc3_52r_zvb) it later,
   instead you must delete and recreate the custom field.

   The
   Multi-select field type is not an option for custom fields that are in the
   Prospects and Customers section of Sell.
5. Set the following option:

   **Filterable**: When selected, you can use this
   field as a filter to view prospects and customers.
6. Click **Save**.

Note: When you qualify a contact as a prospect or customer, the custom fields for that
contact are automatically added as Prospects and Customers custom fields. This means
the custom fields exist in both locations in the Admin settings. If you want to
delete a custom field that exists in both places, you must delete each separately.
For example, deleting a shared custom field in Contacts doesn't also
delete it in Prospects and Customers.

**To add a custom field for deals**

1. On the Sell sidebar, click the **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_settings.png)) icon, then select [**Customize > Deals**](https://app.futuresimple.com/settings/deals).
2. Under **Custom fields**, click **Add Field**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell-custom-field-deal.png)
3. Add the **Field Label**.
4. Select the **Field Type**.

   Be careful when you select the Field Type. You
   cannot [edit](#topic_gc3_52r_zvb) it later,
   instead you must delete and recreate the custom field.
5. Set the following options:

   - **Filterable**: When selected, you can use this field as a
     filter to view deals.
   - **Value editable only by admin** : When selected, only admins can
     change the value of this field.
6. Click **Save**.

Note: The two highest Sell plans include an option to create custom fields for your
sales pipelines (see [Working with multiple sales pipelines](https://support.zendesk.com/hc/en-us/articles/4408824107802)).

## Setting the order of custom fields

When creating multiple custom fields, users with admin rights can also set the order
in which they are displayed on the lead, contact, prospect, customer, and deal
cards, as well as the fields in add or edit forms.

**To set the order of custom fields in the add or edit form**

1. In your list of custom fields, click the sort arrows (up or down) to change the
   order of the custom fields.
2. (Alternatively) You can drag the custom fields up and down the list using the
   sort handle that appears when you move your cursor over the custom field (the
   handle is located on the right edge). Click the handle and drag the custom field
   to the position you want in the list.

   Your sort order is saved automatically
   and updated on the corresponding forms immediately.

**To set the order of custom fields on details cards**

1. On the Sell sidebar, click the **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_settings.png)) icon.
2. Click **Layouts**.
3. Click the appropriate tab for the record type that you want to customize the
   layout for (**Leads**, **People (Contacts)**, **Companies
   (Contacts)**, or **Deals**).
4. In the fields column, click **Edit**.

## Editing and deleting custom fields

Admins can edit custom fields. However, if a custom field has been used and populated
with data, you cannot change it to a different type. To change the Field Type of a
custom field, you must delete and recreate the custom field.

**To edit a custom field**

1. On the Sell sidebar, click the **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_settings.png)) icon.
2. Navigate to [**Customize > Leads**](https://app.futuresimple.com/settings/leads) or [**Customize > Contacts**](https://app.futuresimple.com/settings/contacts), then click either
   [**Customize > Prospects and
   Customers**](https://app.futuresimple.com/settings/sales_accounts), or [**Customize > Deals**](https://app.futuresimple.com/settings/deals).
3. In your list of custom fields, click **Edit** for the fields you want to
   change.
4. Update your custom fields as needed, then click **Save**.

You can also delete custom fields, but keep in mind that when you delete a custom
field, you also delete all data that has been stored in that custom field.

**To delete a custom field**

1. In your list of custom fields, click the **Trashcan** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_trashcan.png)) icon for the fields you
   want to delete.
2. You are prompted to confirm that you want to delete the field. Click
   **Remove** to delete the field.
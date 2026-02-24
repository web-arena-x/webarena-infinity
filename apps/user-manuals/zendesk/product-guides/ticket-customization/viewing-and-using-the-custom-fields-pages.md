# Viewing and using the custom fields pages

Source: https://support.zendesk.com/hc/en-us/articles/4420210121114-Viewing-and-using-the-custom-fields-pages

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

[Custom fields](https://support.zendesk.com/hc/en-us/articles/4408838961562) provide a way to store additional information
about tickets, users, and organizations. The custom fields are visible to all team
members, and can be used in business rules and reporting.

This article contains the following topics:

- [Accessing the custom fields pages](#topic_gcw_yxs_gtb)
- [Reordering custom fields on the fields pages](#topic_j2z_wy5_dfc)
- [Exporting a list of your custom fields](#topic_wnt_bz5_dfc)

## Accessing the custom fields pages

The custom field pages are located in Admin Center and provide a list of existing
custom fields. You can also see information about each field, search, filter, see
the status of the fields, add new fields, edit the order of fields, and export a CSV
of your custom fields.

**To access the User fields page**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
  **People** in the sidebar, then select **Configuration > User fields**.

**To access the Ticket fields page**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
  **Objects and rules** in the sidebar, then select **Tickets > Fields**.

**To access the Organization fields page**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
  **People** in the sidebar, then select **Configuration > Organization
  fields**.

**To access the Custom objects page**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
  **Objects and rules** in the sidebar, then select **Custom objects >
  Objects**.

  When creating or editing a custom object, use the **Fields** tab
  to manage the object's custom fields.

## Reordering custom fields on the fields pages

The order of your custom ticket fields on the Fields page determines the order in
which they're displayed in various places:

- **Custom user fields** ordering determines the order that your active
  custom user fields are displayed in user profiles.
- **Custom organization fields** ordering determines the order that your
  active custom org fields are displayed in organization profiles.
- **Custom ticket fields** ordering affects how fields are ordered on the
  business rules pages in Admin Center and when tickets are bulk updated in
  the Agent Workspace. If your account has a [single ticket form](https://support.zendesk.com/hc/en-us/articles/5494868102426), reordering
  custom fields on this page also reorders the fields on your form. Reordering
  ticket fields doesn’t change the order in which they appear in a ticket if
  your account has [access to multiple ticket
  forms](https://support.zendesk.com/hc/en-us/articles/4408846520858).

  For example, let’s say you have a custom field named "US
  region" and you reorder your ticket fields so that this field appears at
  the top of the Ticket fields page. When you create a trigger, and other
  business rule, this field will appear first in the list of custom fields
  in the Conditions drop-down. And, if you bulk update tickets, the
  position of this field is also affected.

  As shown here when creating triggers
  and bulk updating tickets:

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_fields_order_triggers.png)
  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bulk_edit_fields_order.png)

**To change the order of custom user fields**

1. [Open the custom fields page](#topic_gcw_yxs_gtb)
   for tickets, users, or organizations.
2. Click **Actions** and select **Edit order**.
3. Click and drag the rows into the order you want or use the arrows on each row to
   move them up or down in the list.
4. Click **Save**.

## Exporting a list of your custom fields

If you want to use your custom field data in another app, you can export it to a
comma-separated-values (CSV) file.

**To export your custom fields**

1. [Open the custom fields page](#topic_gcw_yxs_gtb)
   for tickets, users, or organizations
2. Click **Actions** and select **Download CSV**.

   Your field data is
   exported and stored in the downloads folder of your computer.
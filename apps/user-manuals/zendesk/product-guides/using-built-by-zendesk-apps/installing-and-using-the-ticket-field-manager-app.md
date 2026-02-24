# Installing and using the Ticket Field Manager app

Source: https://support.zendesk.com/hc/en-us/articles/4408893441818-Installing-and-using-the-Ticket-Field-Manager-app

---

The [Ticket Field Manager](https://www.zendesk.com/apps/support/ticket-field-manager) app allows an administrator to quickly hide, require, and disable certain ticket fields and drop-down options in the ticketing interface. This app only works with ticket fields.

This article contains the following topics:

- [Installation](#h_cc5354a3-b593-4464-b380-5ce8c556dbd7)
- [Configuring the app](#h_1e774ace-d8bb-4447-8f39-ca6cf588cece)
- [Using the app](#h_a01f8f7d-066b-43df-b557-1eed7dcc5598)

Related articles:

- [Zendesk Support placeholders reference](https://support.zendesk.com/hc/en-us/articles/4408886858138-Zendesk-Support-placeholders-reference)

## Installation

You need to install the Ticket Field Manager app from the [Zendesk Marketplace](../apps-and-the-zendesk-marketplace/using-the-zendesk-marketplace.md).

**To install the app**

1. Visit the [Marketplace](http://zendesk.com/apps?_ga=2.107038978.1483345384.1684319369-246124537.1684319369), then use the search bar to search for the Ticket Field Manager app.
2. Click the app's icon to go to the app's info page.
3. Click **Install** in the upper-right of the page.
4. Select [your account](https://support.zendesk.com/hc/en-us/articles/4409381383578-Where-can-I-find-my-Zendesk-subdomain-) and click **Install**.
5. Configure any app settings as needed and click **Install**.

## Configuring the app

Once the app is installed, go to [Admin Center](../account-administration/using-zendesk-admin-center.md#topic_hfg_dyz_1hb) **> Apps and integrations > Apps > Zendesk Support apps**, hover over the Ticket Field Manager, and click the arrow near the gear icon. Them, select **Change settings**.

![Ticket Field Manager app](https://support.zendesk.com/hc/article_attachments/7856386941210)

In the settings, you can configure the ticket field behavior by updating the provided fields and adding a comma separated list of fields. For custom ticket fields, use the field ID except when specifying hidden drop-down field options which use the format full `custom_field_` and `ID`

![](https://support.zendesk.com/hc/article_attachments/7856364481690)

**Note**: The list of fields must have a space after each comma.

- **Required form fields**: Ticket fields that are required when creating or updating a ticket. For example:

  ```
  field1, field2, field3, 360015591993
  ```
- **Read-only form fields**: Ticket fields that are shown to the user but are not editable. For example:

  ```
  field1, field2, field3, 360015591993
  ```
- **Allowed groups for read-only form fields**: This is a list of IDs of groups that should not have the read-only restrictions applied.
- **Hidden form fields**: Ticket fields that should be hidden from the agent when creating or updating a ticket. For example:

  ```
  field1, field2, field3, 360015591993
  ```
- **Allowed groups for hidden form fields**: This is a list of IDs of groups that should not have the hidden field restrictions applied.
- **Allowed groups for hidden drop-down options**: A comma separated list of group IDs that do not have any hidden options in drop-down applied.
- **Hide drop-down form options**: Hide options for a given drop-down field. The format is `[{"name": "type", "value": "problem"}]`, or, for custom fields `[{"name": "custom_field_3600152073", "value": "brushed_silver"}]`

Note: When setting your value, use the **Tag** of your drop-down option.  
![Tag.png](https://support.zendesk.com/hc/article_attachments/7856386942234)

To hide multiple drop-down values including those in the same field, use the format as shown in the example below.

```
 [{"name": "type", "value": "problem"},  
 {"name": "custom_field_360015592073", "value": "diamond"},  
 {"name": "custom_field_360015592073", "value": "nickel_plated"},
```

The name must be listed with the name and value for each option to be hidden, even for options in the same drop-down field. It's not possible to hide the assignee field with the Ticket Field Manager app, but you can do that with the [Assignment Control app](https://www.zendesk.com/marketplace/apps/support/223590/assignment-control/).

### Available ticket fields

- requester
- collaborator
- sharedWith
- status
- ticket\_form\_id (the ticket form drop-down)
- tags
- type
- priority
- problem
- custom field

For a complete listing of available fields for use in the form settings, see [Zendesk Support placeholders reference](https://support.zendesk.com/hc/en-us/articles/4408886858138).

### Restricting app functionality

The functionality of the app is restricted to agents and admins who have been granted access through the **Enable role restrictions** and **Enable group restrictions** settings. For more information, see [Restricting app access](../apps-and-the-zendesk-marketplace/managing-your-installed-apps.md#topic_xyf_wmw_qfb).

![restrict_app_access.png](https://support.zendesk.com/hc/article_attachments/7856386942490)

## Using the app

After creating a ticket or opening an existing ticket, you will see that the fields are now required based on the list defined in the **Required form fields**. The example below includes **Assignee** and **Tags**.

![required_fields.png](https://support.zendesk.com/hc/article_attachments/7856386941978)

## Release notes:

**Version 2.2.0 - 2020-08-05**

- Created allow list for hidden drop-down options
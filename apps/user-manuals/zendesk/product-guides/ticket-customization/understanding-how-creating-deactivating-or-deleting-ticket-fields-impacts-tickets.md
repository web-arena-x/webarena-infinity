# Understanding how creating, deactivating, or deleting ticket fields impacts tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408886624410-Understanding-how-creating-deactivating-or-deleting-ticket-fields-impacts-tickets

---

When using custom ticket fields, there are different actions available. Each of these actions affect tickets and the API differently.

Note: You can't alter a field type after the custom ticket field is created. You will need to [create a new custom field](https://support.zendesk.com/hc/en-us/articles/4408883152794) and remove the original from your ticket form.

This article includes the following topics:

- [Creating new custom ticket fields](#topic_hks_zt4_htb)
- [Altering drop-down field options](#topic_cc1_5pp_htb)
- [Deactivating custom ticket fields](#topic_clx_ss4_htb)
- [Deleting custom ticket fields](#topic_d1j_mt4_htb)

## Creating new custom ticket fields

When you [create new custom ticket fields](https://support.zendesk.com/hc/en-us/articles/4408883152794), you are adding the option to capture additional information in each ticket.

**Agent interface**

For all tickets, regardless of status, the new ticket field appears on the ticket form in the agent interface. It displays a null '-' or empty value depending on the type of custom field.

**API**

The newly created ticket field alters all tickets with a status less than closed when a value is added to the field. If the new field is added to a ticket form, but data is never added to the field, it won't appear in the ticket audit endpoint. This is true for all tickets with custom fields but no data added, regardless of when the fields are created.

## Altering drop-down field options

Drop-down fields display the same behavior as other custom ticket fields in tickets, reporting, and the API. However, drop-down field options can be changed and deleted.
It is important to note drop-down field options are directly connected to their assigned tag. For example, in the image below, the drop-down field value *red* has the tag *color\_red*.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_dropdown_value_tag.png)

### Changing drop-down field options and tags

Changing the field value but not its tag effectively replaces the old field option. Reusing tags for new fields isn't recommended because it replaces the existing value on all tickets, including closed and archived tickets, and can skew reporting.

If you want to edit an existing drop-down field value, you can ensure the value is replaced in all instances by keeping the same tag. This is useful for reporting if you only want to report on a new value, not a new tag.

If you edit a drop-down field by only changing its tags, existing tickets (including closed and archived tickets) aren't updated and retain the original tag. In this case, the original tag is no longer associated with a field value so the field is removed from those tickets. This effectively removes historic field values from tickets and can skew your reports.

Note: When editing ticket fields, keep the following objects in mind:

- Macros
- Views
- Triggers
- Automations

If you have any of these objects that use the custom field being edited, the tag must remain the same for the object to continue functioning. If the tag no longer exists for a given field value, the object will return an error.

### Deleting drop-down field options

When you delete a drop-down field option, your tickets are affected in the following ways:

- **Closed and archived tickets** display a yellow caution icon with a *Missing field value* warning next to a deleted value selected in a drop-down field.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_deleted_dropdown_value.png)
- **Unclosed tickets (including solved)** replace the deleted value with a null '-' value. No error is displayed in the ticket.

The tag from the drop-down field isn't deleted from the ticket tag field, so you can still use the tag in your reports. This also means that if you create a new drop-down field option with an identical tag, the ticket field will change back to the selected value. See [Reporting with custom fields](https://support.zendesk.com/hc/en-us/articles/4408824384538).

## Deactivating custom ticket fields

Any data lost from a deactivated field can be recovered again by reactivating the field. After reactivation, the field is available in the ticket view of the agent interface again.

**Agent interface**

For all tickets, regardless of status, deactivating a ticket field removes it from the agent interface.

**API**

The data in a deactivated ticket field remains stored in the [ticket audits endpoint](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_audits/?_ga=2.56954026.1002092961.1650288474-999012820.1649788949#show-audit).

## Deleting custom ticket fields

If you delete a custom ticket field, you won't be able to recreate or recover the field or its data. If you'd like to preserve the field data, deactivate the field instead.

**Agent interface**

For all tickets, regardless of status, deleting a ticket field removes it from the agent interface permanently.

**API**

When a custom field is deleted, its data (including the field ID), is saved in the API. The [ticket audits endpoint](https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_audits/?_ga=2.56954026.1002092961.1650288474-999012820.1649788949#show-audit) tracks and stores every change to a ticket, including custom ticket field data after the field itself is deleted. This is the only location deleted custom ticket field data is stored.
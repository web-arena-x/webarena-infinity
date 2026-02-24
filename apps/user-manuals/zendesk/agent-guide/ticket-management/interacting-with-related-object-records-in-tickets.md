# Interacting with related object records in tickets

Source: https://support.zendesk.com/hc/en-us/articles/6097369527322-Interacting-with-related-object-records-in-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Support > Custom objects

When viewing a ticket in the Zendesk Agent Workspace, you can use the record preview panel to view details about records that are related to the ticket you're working on without navigating away from the ticket. Record preview is part of the [context panel](https://support.zendesk.com/hc/en-us/articles/4408836526362) and is closed by default. The record preview displays an empty state until you select a related record you want to preview.

Note: The Record preview only supports custom object records.

This article contains the following topics:

- [Setting values in lookup relationship fields on tickets](#topic_ttd_ypg_qyb)
- [Previewing related records](#topic_krs_4d1_qyb)

## Setting values in lookup relationship fields on tickets

[Lookup relationships](https://support.zendesk.com/hc/en-us/articles/4591924111770) provide a way to associate data in your account with other objects. When lookup relationship fields are added to tickets, they can point to standard Zendesk objects (users, organizations, and other tickets) or [custom objects](https://support.zendesk.com/hc/en-us/articles/5914453843994). Populating the lookup field with a record creates the association and enables the preview functionality. However, to use the record preview functionality, the following must be true:

- Your account must have at least one custom object.
- Your ticket form must have at least one active lookup relationship field pointing to a custom object.
- Within the ticket, a valid value must be set in the lookup field.

When all of these conditions are met, the record preview icon is displayed on the right side of the workspace and next to each lookup relationship field with a valid record selected.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_object_record_preview.png)

When setting a value for a lookup relationship field, start typing the record's name in the lookup field. You can also match custom object records against other text-based fields within the object. Autocomplete matches are displayed as you type.
When you find what you're looking for, select it to set the field's value and associate the record with the ticket.

## Previewing related records

When the lookup field points to a custom object, admins and [agents with permission](https://support.zendesk.com/hc/en-us/articles/6073847712282) can select related records in the ticket lookup fields and preview details for custom object records that have been added. In the preview, you can see the first 20 fields with values for the record.
Previewing related records directly in the customer context panel allows you to view relevant information without navigating away from the ticket. When you need to see more than 20 fields for a record or you need to modify the record, you can navigate directly to the record from the preview.

Note: You may see only certain fields in the record preview if an admin has [configured a custom object’s card](https://support.zendesk.com/hc/en-us/articles/5768595554714).

The record preview displays an empty state until you select a related record to preview.

**To preview a related record**

1. In the ticket fields panel, click the **Record preview** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_omnipanel_record_preview.png)) next to a lookup relationship field.

   Note: The record preview icon is only visible when a valid value is set in a lookup field.
2. (Optional) If needed, from the record preview, click the **View details** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_LURF_ticket_view_details.png)) to navigate directly to the record's details page.
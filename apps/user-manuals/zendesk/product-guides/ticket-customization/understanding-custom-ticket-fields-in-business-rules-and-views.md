# Understanding custom ticket fields in business rules and views

Source: https://support.zendesk.com/hc/en-us/articles/4408834953114-Understanding-custom-ticket-fields-in-business-rules-and-views

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

When you [add custom ticket fields](https://support.zendesk.com/hc/en-us/articles/4408883152794), you can use them in triggers, automations, and views.

Note: For information on the business rules and views conditions available for each custom field type see, [Using custom ticket fields in business rules and views](https://support.zendesk.com/hc/en-us/articles/4408887162394).

This article covers the following topics:

- [Understanding custom ticket fields, tags, and business rules](#id_kxq_ydx_qcb)
- [Understanding custom ticket fields and views](#topic_znk_mnk_xj)
- [About required fields and automations](#topic_pqw_5dx_qcb)

## Understanding custom ticket fields, tags, and business rules

Custom fields are available as conditions and actions in business rules, which means that you can directly access the custom fields in your business rules.

Additionally, the drop-down list, multi-select, and checkbox custom ticket fields can add tags to tickets that can be used in your business rules.

With drop-down and multi-select fields, Zendesk Support automatically generates tags as you enter field options for your custom field. You can modify the automatically generated tags by editing the **Tag** field. You must have a tag for each field option.

With checkbox fields, you have the option of associating a tag with the field.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_field_checkbox_tag.png)

These tags can be used in a variety of ways in your business rules. For example, you can use the tag to automatically assign the ticket to a specific group.

For more information, see:

- [About tags](https://support.zendesk.html#topic_umd_ona_vb)
- [Understanding tags and ticket fields](https://support.zendesk.com/hc/en-us/articles/4408881943194)

## Understanding custom ticket fields and views

After creating a custom ticket field, you can add it to your views. For example, suppose you create a custom field to let users select one of your product lines. After adding the custom field as a column in a view, you can sort the tickets by product line by clicking the column's heading. See [Creating views to build customized lists of tickets](https://support.zendesk.com/hc/en-us/articles/4408888828570).

Note: Multi-select fields are not supported in table columns.

The sort order of custom-field columns in views is by the underlying tags used for the custom field. For example, if you sort the tickets by ascending order, the order is by the alphabetical order of the field's tags, not its titles.

For example, suppose you create a custom drop-down field with the following value:tag pairs:

- Photography (tag: photography)
- Video (tag: audiovisual)
- Medical (tag: endoscopy)

If you add the field to a view and sort by ascending order, the tickets would be grouped and ordered as follows:

1. Video tickets (tag: audiovisual)
2. Medical tickets (tag: endoscopy)
3. Photography tickets (tag: photography)

If you want to list your photography tickets at the top of the view, click the column heading again to sort by descending order.

If you want to use text, multi-line text, numeric, decimal, and regular expression custom fields, drag the fields to the columns included in the table section.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_ticket_fields_views_1.png)

Once added, the columns will appear in the view.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_ticket_fields_views_2.png)

Important: Custom date fields used in business rules or views always reference GMT time and not the account timezone. For example, if your timezone is set to GMT+2 and you have a business rule or view with a custom date field named "Next review date", any conditions using this will evaluate the date as GMT, not GMT+2 timezone.

## About required fields and automations

If you have automations that set the ticket status to Solved, the ticket will be set as solved even if the ticket has "required" custom fields that are still blank. The reason is that automations check the automation conditions, not the ticket field conditions.

A workaround is to use tags to prevent the automation from running until the required fields are completed. For example, you can tell the automation to hold off until the okay\_to\_close tag is present, then set a trigger to add the tag when the required field is no longer blank. Here's how. Add the following "All" condition to your automation: **Ticket: Tags** > **Contains At Least One of the Following** > okay\_to\_close. Next, create a trigger with the following "All" condition:
**Ticket:{custom\_field\_name}** > **Is Not** >
**-** (blank). Set its action as **Ticket: Add Tags**
> okay\_to\_close.

For more information, see the following articles:

- [Creating and managing automations for time-based events](https://support.zendesk.com/hc/en-us/articles/4408883801626)
- [Setting up automatic ticket updates and notifications with triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466)
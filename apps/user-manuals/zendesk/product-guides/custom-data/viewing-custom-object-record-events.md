# Viewing custom object record events

Source: https://support.zendesk.com/hc/en-us/articles/9174563278874-Viewing-custom-object-record-events

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Enterprise |

[Custom object](https://support.zendesk.com/hc/en-us/articles/5914453843994) record events show all updates made to records, whether by a person or business rule, such as an object trigger. By looking at the record events, you can see the complete history of the record. Events include record properties that are added, removed, or changed. However, object-level events, such as modifications to a custom object's schema of custom fields, and object trigger notifications associated with a record aren't reflected in the record events.

This article contains the following topics:

- [Viewing custom object record events](#topic_ulf_sfx_bfc)
- [Understanding what is shown in record events](#topic_icw_sfx_bfc)

## Viewing custom object record events

When viewing a custom object record, you can use the Events tab to view a list of the record's events. By default, the 20 most-recent events are displayed, but you can expand the list to see more events.

**To view custom object record events**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Custom objects** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_custom_objects_records_page.png)) in the sidebar.
2. Select the custom object for which you'd like to view record events.
3. [Search](https://support.zendesk.com/hc/en-us/articles/6088606067866#topic_bxl_dxq_fyb) for and click the name of the record you want to view the event history for.
4. Click the **Events** tab.
5. (Optional) If there are more than 20 events for the record, click **Show more** to see all of them.

## Understanding what is shown in record events

Custom object record events show most events related to a record, such as creation, changes to values, some object trigger actions, and more. However, the list doesn't include changes to the custom object itself, even though that can affect the object's records. For example, if an admin deletes a field from a custom object's schema, the field and any values stored in that field are also removed from that object's records, but this is considered a change to the object rather than the record.

The following events are visible in custom object record events:

- Record created
- Values added
- Values changed
- Object trigger actions (excluding notifications)
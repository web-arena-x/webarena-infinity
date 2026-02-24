# Using the Jira field syncing feature (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/4408825394458-Using-the-Jira-field-syncing-feature-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Use the field syncing feature to sync data between Support and Jira, enhancing collaboration between support and engineering teams. Map fields to share information in near real-time, but remember that syncing is case-sensitive and unidirectional per field. Test in a sandbox first, as synced data can't be easily unsynced. Be aware of compatibility limitations and potential errors when syncing closed tickets.

The field syncing feature allows near real-time data sync between Zendesk Support and Jira.
This provides information sharing between the two systems for better collaboration between
support and engineering teams. This is done by mapping Jira issue fields to Zendesk Support
ticket fields.

This article contains the following topics:

- [Requirements and limitations](#topic_cnd_yzh_2z)
- [Setting up field syncing](#topic_ith_yzh_2z)

Related articles:

- [Configuring a Jira Cloud webhook for field syncing](https://support.zendesk.com/hc/en-us/articles/4408821582362)
- [Setting up the Zendesk Support for Jira integration](https://support.zendesk.com/hc/en-us/articles/4408837969946)
- [Using the Zendesk Support for Jira integration](https://support.zendesk.com/hc/en-us/articles/4408827996058)

## Requirements and limitations

- The supported versions are Jira Cloud and Jira Data Center.
- The field syncing feature is case-sensitive. Support field values must exactly match
  Jira field values.
- Once data is synced, it cannot be removed easily. However, you can disable field
  syncing altogether, which disables all field links.
- Sync direction can be set on a per-field basis, but only one mapping per field is
  allowed.
- Bidirectional syncing of the same field is not supported.
- The field mapping screen displays custom field types from all Jira projects in a
  single list.
- Custom ticket status fields aren't supported and cannot be mapped.
- All mapped fields for a particular issue or ticket are updated via a single API call.
  If a mapped field is misconfigured, all fields will not be updated.
- Syncing a field from multiple linked tickets to a Jira issue field, or from multiple
  Jira issues to a field on a ticket, is not supported and causes the sync to stop for the
  particular ticket or issue. See [Many-to-one-syncing](#topic_dmz_wc3_2z).

### Field type syncing compatibility

There are some restrictions on the field types that are compatible with syncing. For
example, a Zendesk decimal field with a numeric display cannot sync with a Jira multi-line
text field.

The tables below list field mapping compatibility.

Table 1. Zendesk ticket fields and compatible Jira issue fields

| Field title/type | Display type | Compatible Jira issue field type(s) |
| --- | --- | --- |
| Priority (default) | Drop-down Note: You can't sync the Zendesk Priority field to the Jira Priority field | Text field (read-only) Select list  Text field (single line)  Text field (multi-line) |
| Type (default) | Drop-down | Text field (read-only) Select list  Text field (single line)  Text field (multi-line) |
| Date (custom) | Date | Date picker Due date |
| Decimal (custom) | Number | Number field |
| Numeric (custom) | Number | Number field |
| Drop-down list (custom) | Drop-down | Text field (read-only) Select list  Text field (single line)  Text field (multi-line) |
| Text (custom) | Single line text | Description Environment Text field (read-only) Select list  Summary  Text field (single line)  Text field (multi-line) |
| Multi-line text (custom) | Multi-line text | Text field (multi-line) |

Table 2. Jira issue fields and compatible Zendesk ticket fields

| Field title/type | Display type | Compatible Zendesk ticket field type(s) |
| --- | --- | --- |
| Description (default) | Multi-line text | Multi-line text |
| Due date (default) | Date | Date |
| Environment (default) | Multi-line text | Multi-line text |
| Fix versions (default) | Fix versions | Text Multi-line text |
| Priority (default) | Priority Note: Only syncs from Jira to Zendesk | Text Multi-line text  Drop-down list |
| Sprint (default) | Sprint | Text Multi-line text |
| Status (default) | Status | Text Multi-line text  Drop-down list |
| Summary (default) | Single line text | Text Multi-line text |
| Date (custom) | Date | Text Multi-line text  Date |
| Number (custom) | Number | Numeric Decimal |
| Read-only text field (custom) | Read-only text field | Text Multi-line text |
| Select (custom) | Drop-down | Text Multi-line text  Drop-down  Type  Priority |
| Text field (custom) | Single line text | Text Multi-line text |
| Text area (custom) | Multi-line text | Multi-line text |

## Setting up field syncing

Field syncing is set up using a mapping interface.

Note: Field syncing only affects tickets and issues created after the sync feature is set up. It
does not update previously created tickets and issues. However, when a previously created
ticket or issue is edited or updated, field syncing is applied.

Zendesk Support and Jira have different field types, which adds complexity to the syncing
process. It requires following certain rules when creating field mapping to ensure syncing
works as expected.

Both system (default) and custom fields are supported. However, only a subset of all
available field types are supported. Additionally, there are limitations as to which Jira
field type can be synced to a Zendesk Support field type, and vice-versa. For instance, a
text field cannot be synced to a datetime field. To prevent misconfiguration, the user
interface hides field types that are not supported, and greys out invalid mapping
options.

Because data synced fields cannot be unsynced, we recommend that you test your field
syncing in a test environment or sandbox. If necessary, you can disable the field syncing
feature by removing all field mappings. This stops syncing subsequent data changes.

**To configure and activate field syncing**

1. Log in to your Jira account with admin privileges.
2. In the top navigation bar, select **Apps** > **Manage your apps** >**Zendesk Support for Jira** > **Configure** > **Field Mapping**.
3. Use the drop-down menus to select the Jira issue ticket field and Zendesk Support
   ticket fields you want to map.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sync_to_jira.png)
4. Click **Add**. The synced fields are added to the Field Mapping list.
5. Repeat for additional mapped fields.
6. When you're finished mapping fields, click **Save & Sync**.

### Many-to-one syncing

You can sync a field from a single Jira issue to multiple Zendesk Support tickets, or a
field from a single Support ticket to multiple Jira issues. In this case, the syncing only
occurs in one direction, from the single issue or ticket to multiple tickets or issues,
respectively.

However, syncing a field from multiple linked tickets to a Jira issue field, or from
multiple Jira issues to a field on a ticket, is not supported. Configuring field sync this
way causes syncing to stop for this particular ticket or issue. To link multiple tickets
to a Jira issue and use sync, we recommend implementing a problem/incident concept as
described in [Working with problem and incident tickets](https://support.zendesk.com/hc/en-us/articles/4408835103898).

The Jira issue key is a special case. If multiple issues are linked to the same ticket,
all their keys will appear on the ticket.

### Syncing closed tickets

Unlike Jira, Zendesk does not allow closed tickets to be updated. This means that when
attempting to sync Jira issues to Zendesk tickets, it may fail if the ticket is already
closed. You will be able to see this error on the Zendesk Support for Jira add-on [Error Report](#topic_qgx_fh3_2z) screen.

### Errors

Since syncing happens behind the scenes, errors are displayed on a dedicated screen. The
error report screen allows the user to identify and resolve invalid field mappings as well
as other configuration issues.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sync_error.png)
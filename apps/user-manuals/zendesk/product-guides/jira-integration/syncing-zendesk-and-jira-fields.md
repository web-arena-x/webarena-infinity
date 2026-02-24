# Syncing Zendesk and Jira fields

Source: https://support.zendesk.com/hc/en-us/articles/9827183512730-Syncing-Zendesk-and-Jira-fields

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

The field syncing feature enables real-time data synchronization between
Support and Jira, enhancing collaboration between support and engineering
teams. By mapping Jira issue fields to ticket fields, you can share information
effectively. Note that syncing is unidirectional and doesn't support
Jira Data Center or Server. Test configurations in a sandbox environment,
and use the integration log to troubleshoot errors.

The field syncing feature allows near real-time data sync between Zendesk
Support and
Jira. This provides information sharing between the two systems for better
collaboration
between support and engineering teams. This is done by mapping Jira issue
fields to
Zendesk Support ticket fields.

Note: This integration doesn't support
Jira Data Center and Jira
Server, as Atlassian is planning to discontinue these platforms. See
Atlassian's
announcements for
[Jira Data Center](https://www.atlassian.com/migration)
and
[Jira Server](https://www.atlassian.com/licensing/server-end-of-support#serv-end-of-support).

This article contains the following topics:

- [Requirements and
  limitations](#topic_cnd_yzh_2z)
- [Setting up field
  syncing](#topic_ith_yzh_2z)
- [Turning off field syncing](#topic_o43_xxx_xgc)

Related articles:

- [Configuring the Jira app for Zendesk
  Support](https://support.zendesk.com/hc/en-us/articles/9810169980058)
- [Setting up Zendesk ticket view for
  Jira](https://support.zendesk.com/hc/en-us/articles/9810155413146)

## Requirements and limitations

- Once data is synced, it cannot be removed easily. However,
  you can turn off
  field syncing altogether, which disables all field links.
- Bidirectional syncing of the same field is not supported.
- The field mapping screen displays custom field types from
  all Jira projects
  in a single list.
- Custom ticket status fields aren't supported and cannot be
  mapped.
- All mapped fields for a particular issue or ticket are updated
  via a single
  API call. If a mapped field is misconfigured, all fields
  will not be
  updated.

### Field type syncing compatibility

There are some restrictions on the field types that are compatible
with syncing.
For example, a Zendesk decimal field with a numeric display cannot
sync with a
Jira multi-line text field.

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

Note: Field syncing only affects tickets
and issues created after
the sync feature is set up. It does not update previously created
tickets and
issues. However, when a previously created ticket or issue is edited
or updated,
field syncing is applied.

Zendesk Support and Jira have different field types, which adds complexity
to the
syncing process. It requires following certain rules when creating
field mapping to
ensure syncing works as expected.

Both system (default) and custom fields are supported. However, only
a subset of all
available field types is supported. Additionally, there are limitations
on which
Jira field type can be synced to a Zendesk Support field type, and
vice versa. For
instance, a text field cannot be synced to a datetime field. To prevent
misconfiguration, the user interface hides field types that are not
supported and
greys out invalid mapping options.

Because data-synced fields cannot be unsynced, we recommend that
you test your field
syncing in a test environment or sandbox. If necessary, you can
[turn off field syncing](#topic_o43_xxx_xgc).

**To turn on and configure field syncing**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the **Jira** link.
3. If you have multiple connections, click the name of the connection
   you are
   setting up.
4. Click the **Field mapping** tab.
5. To turn on field sync from Zendesk to Jira, select
   **Turn on Zendesk to
   Jira sync**,
   then map the fields you'd like to sync:
   1. Click **Add mapping**.

      ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/jira_v2_mapping_add.png)
   2. Use the drop-down menus to select the Jira issue
      ticket field and
      Zendesk Support ticket fields you want to map.
   3. Repeat for additional mapped fields.
6. To turn on field sync from Jira to Zendesk, select
   **Turn on Jira to
   Zendesk sync**.
7. [Create a webhook](https://support.zendesk.com/hc/en-us/articles/4408821582362)
   in Jira and copy
   the generated secret from the webhook. Then, paste it in
   the **Secret**
   field and click **Save secret**.
8. Map the fields you'd like to sync:
   1. Click **Add mapping**.
   2. Use the drop-down menus to select the Jira issue
      field and Zendesk
      Support ticket fields you want to map.
   3. Repeat for additional mapped fields.
9. When you're finished mapping fields, click
   **Save**.

### Many-to-one syncing

To link multiple tickets to a Jira issue and use sync, we recommend
implementing
a problem/incident concept as described in
[Working with problem and incident
tickets](https://support.zendesk.com/hc/en-us/articles/4408835103898).

### Syncing closed tickets

Unlike Jira, Zendesk doesn't allow closed tickets to be updated.
This means that
when attempting to sync Jira issues to Zendesk tickets, it may
fail if the
ticket is already closed. You will be able to see this error
on the Zendesk
Support for Jira add-on
[Error
Report](#topic_qgx_fh3_2z)
screen.

### Errors

The integration log allows you to identify and resolve invalid
field mappings as
well as other configuration issues. See
[Viewing the integration log](https://support.zendesk.com/hc/en-us/articles/4408819871130).

## Turning off field syncing

Turning off field syncing stops syncing subsequent data changes.

**To turn off field syncing**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Integrations >
   Integrations**.
2. Click the **Jira** link.
3. If you have multiple connections, click the name of the connection
   you are
   setting up.
4. Click the **Field mapping** tab.
5. Deselect the
   **Turn on Zendesk to Jira sync**
   and
   **Turn on Jira to
   Zendesk sync**
   checkboxes.
6. Click **Save**.
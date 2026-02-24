# Migrating triggers with the live chat-to-messaging migration wizard

Source: https://support.zendesk.com/hc/en-us/articles/9863791207066-Migrating-triggers-with-the-live-chat-to-messaging-migration-wizard

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Verified AI summary ◀▼

The live chat-to-messaging migration wizard helps you transition your
chat triggers to messaging triggers. You'll review and activate migrated
triggers, ensuring they perform as expected. Access the migration review
page to manage triggers, including activating, deleting, or updating
them in bulk. Stay informed about triggers that couldn't be migrated
and take necessary actions to recreate them manually.

Important: This article applies
only to customers with scheduled live
chat-to-messaging migration assistance. Affected customers are notified
of the
update by an in-product banner and email notifications 30 days before
the migration.
See
[our announcement](https://support.zendesk.com/hc/en-us/articles/9460252937114)
information on affected
accounts, pre-migration steps, and the migration process.

As part of the assisted live chat-to-messaging migration process,
your Zendesk Chat triggers will be converted to messaging triggers. This
process
includes the option to review and triage your migrated triggers before
activating them.

This article provides an introduction to the
Chat triggers migration review page in Admin Center, and additional resources
for understanding and working with messaging triggers.

For more information
on the migration process, see
[About the live chat-to-messaging migration wizard](https://support.zendesk.com/hc/en-us/articles/9435865466906).

This article includes the following topics:

- [About trigger migration](#topic_lcf_mgg_khc)
- [Viewing and using the Chat triggers migration review page](#topic_xdn_mgg_khc)
- [Activating migrated triggers](#topic_mps_mgg_khc)

## About trigger migration

When you migrate from live chat to messaging, Zendesk uses AI to
assess how each Chat
trigger is used in your live chat configuration and recreates them
as Support
triggers, messaging triggers, or proactive messages. Our AI is constantly
learning
and improving its performance, so while most triggers are recreated
accurately, we
recommend that you review all migrated triggers to make sure they
will perform as
expected. See
[Changes to your Chat triggers when migrating from
Chat to messaging](https://support.zendesk.com/hc/en-us/articles/4408822204698#topic_ot4_bmp_pnb)
for more information.

**Chat triggers migrated to messaging triggers**
will keep their activation status
when they are migrated. If the original Chat trigger was active in
your live chat
configuration, it will be active after migration. When you configure
and launch your
messaging channel, active messaging triggers will run when their
conditions are met.
You can access messaging triggers at
**Admin Center > Objects and Rules > Business
rules > Messaging triggers**.
See the following articles for more information
on messaging triggers:

- [Accessing messaging triggers](https://support.zendesk.com/hc/en-us/articles/5973077601562)
- [About the standard messaging
  triggers](https://support.zendesk.com/hc/en-us/articles/8567613882522)
- [Messaging triggers conditions and actions
  reference](https://support.zendesk.com/hc/en-us/articles/8015292388378)

**Chat triggers migrated to Support triggers**
will be deactivated after
migration, regardless of their activation status before migration.
You will need to
review and manually activate the new Support triggers before they
run when their
conditions are met in the messaging environment. You can access these
triggers at
**Admin Center > Objects and Rules > Business rules > Triggers**.
See the
following articles for more information:

- [About triggers and how they
  work](https://support.zendesk.com/hc/en-us/articles/4408822236058)
- [About the standard ticket
  triggers](https://support.zendesk.com/hc/en-us/articles/4408828984346)
- [Ticket triggers conditions and actions
  reference](https://support.zendesk.com/hc/en-us/articles/4408893545882)

**Chat triggers designed to proactively contact visitors will become
proactive messages**.
These triggers will be deactivated after migration,
regardless of their activation status before migration. You can access
proactive
messages at
**Admin Center > Channels > Messaging > Proactive messages**.
See the
following articles for more information:

- [About proactive messages](https://support.zendesk.com/hc/en-us/articles/5381304334234)
- [Proactive messaging conditions and events
  reference](https://support.zendesk.com/hc/en-us/articles/5511218058650)

Chat triggers that can’t be migrated can be viewed in the
**Not
migrated** tab
of the Chat triggers migration review page. Reasons for
unsuccessful migration include:

- The trigger contains functionality that is not available in the
  messaging environment.
- Something went wrong with the trigger’s migration, and you will
  need to re-create the trigger manually.

## Viewing and using the Chat triggers migration review page

After the migration is complete, you can access the Chat triggers
migration review
page, where you can view the list of migrated triggers and update
them as
needed.

### Viewing the Chat triggers migration review page

You can access the Chat triggers migration review page from the
Messaging
settings page in Admin Center.

**To access the Chat triggers migration review page**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. On the Messaging page, click
   **Manage settings**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_migration_landing_page.png)
3. Click
   **Review and activate messaging rules**
   to view the Chat
   triggers migration review page.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_triggers_migration_review_page-to_review.png)

This page includes the following tabs:

- **To review** lists all migrated
  Chat triggers and
  the messaging rules they are mapped to. From this tab, you
  can review,
  activate, and delete the migrated rules. You can (and should)
  review these
  triggers before creating and launching a messaging channel.
- **Activated** lists the migrated
  triggers that are
  now active. These include Chat triggers that were active
  when the migration
  occurred and became messaging triggers, as well as migrated
  triggers you
  activated manually.
- **Not migrated** lists the Chat
  triggers that could not be mapped
  to Support triggers, messaging triggers, or proactive messages,
  and were not
  included in the migration.

The trigger lists on these tabs
include the following columns:

- **Chat trigger**, a link to the
  original Chat
  trigger on the Chat dashboard. Clicking this link opens the
  Chat
  trigger in a new tab.
- **Chat trigger status**, the original
  Chat trigger’s status when
  the migration occurred. Note that if you change a trigger’s
  status after
  migration, this column will still reflect the status at the
  point of
  migration.
- **Messaging rule** (To review and
  Activated tabs
  only), whether the original trigger was converted to a Support
  trigger, messaging trigger, or a proactive message.
- **Link to rule** (To review and
  Activated tabs
  only), a link to the messaging version of the trigger on
  the
  Support triggers page, the Messaging triggers page, or the
  Proactive messages page. Clicking this link opens the Support
  trigger or proactive message in a new tab.

### Deleting migrated triggers

**To delete a migrated trigger**

1. In the **To Review** tab,
   click the selection box next
   to the active trigger you want to deactivate.
2. At the bottom of the list, click
   **Delete**, then
   confirm your selection.

### Updating triggers in bulk

**To update the status of triggers in bulk**

1. In the **To Review** tab, select
   the triggers you want
   to update:
2. Click the **Chat trigger** selection
   box at the top
   of the triggers list to select all triggers in the list,
   OR

   Filter the list to display
   only the triggers you want to update, then click the
   selection box at
   the top of the list.
3. At the bottom of the list, click
   **Activate** or
   **Delete**, then
   confirm your selection.

### Filtering the triggers lists

You can filter the triggers lists on all tabs by Chat trigger
status.

**To filter the triggers list**

1. In any tab, click the **Filter**
   button.
2. In the filter options panel, select the status on which you
   want
   to filter the list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/trigger_filter_panel.png)
3. Click **Apply filters**.

## Activating migrated triggers

By default, migrated Chat triggers maintain the status – active or
inactive – applied
to them when the migration occurred. You can activate the new versions
of the
migrated Chat triggers in the **To review**
tab.

Activated triggers will run when you configure and launch your
messaging channel.

**To activate a migrated trigger**

1. In the **To Review** tab, click the
   selection box next to
   the inactive triggers you want to activate.
2. At the bottom of the list, click
   **Activate**.
3. On the confirmation page, click
   **Activate [X]
   rules**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/activate_rules_confirmation.png)
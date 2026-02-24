# Migrating to the Zendesk Agent Workspace

Source: https://support.zendesk.com/hc/en-us/articles/4583448479514-Migrating-to-the-Zendesk-Agent-Workspace

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > Workspaces > Agent tools > Agent
Workspace

This article describes how to migrate your account to use the [Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930), which enables agents to manage email, chat,
voice, and messaging conversations all within a single ticket interface.

The workspace enables agents to work seamlessly across all Zendesk channels. Agents
can use the appropriate channels to address issues, without being restricted to the channel in
which the customer originally made contact. Zendesk has found that, on average, companies see
significant improvements to customer reply and resolution times after moving over.

This article includes the following sections:

- [Before you migrate](#topic_c1g_2fq_wnb)
- [About the migration](#topic_m1x_qhq_nkb)
- [Starting the migration](#topic_cyn_4lq_nkb)
- [After the migration](#topic_lwk_2xq_nkb)

**Related articles**

- [About the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930)
- [Resources for migrating to the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408843572762)
- [Migrating social messaging channels to the Zendesk Agent
  Workspace](https://support.zendesk.com/hc/en-us/articles/4408824569114)

## Before you migrate

The Agent Workspace provides a completely-new working environment for your agents
with a great set of tools to manage interactive, cross-channel conversations. The benefits
are significant, but there are some considerations.

Make sure you consider these items before you migrate:

**Account management**

- Activating the workspace applies to your entire account. You cannot restrict
  the activation to individual agents or agent groups. If you have an Enterprise account,
  you can test out the activation in a Sandbox first before you activate it in your
  production account. See [Preparing to activate](https://support.zendesk.com/hc/en-us/articles/4581758611866#topic_jpk_lwg_rlb).
- With migration to the Agent Workspace, Chat is
  integrated with Support. To make it more a seamless experience, chats are created as
  tickets and have the ticket rules applied to them. This means that both [Support triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466) and [Chat triggers](https://support.zendesk.com/hc/en-us/articles/4408884148762) can have an impact on chats or other messaging
  types in the Agent Workspace.

  For example, a trigger that changes the status of the
  ticket to Solved and is encompassing enough to catch an incoming chat, might force an
  incoming chat to be auto-closed. Before you migrate, Zendesk recommends checking any
  triggers that change ticket status to make sure they are compatible with Chat and other
  messaging channels and don't have any conflicts.
- If Data Center Location (DCL) is important to your account, make sure you understand our
  Zendesk [Regional Data Hosting Policy](https://support.zendesk.com/hc/en-us/articles/4408883599130-Regional-Data-Hosting-Policy). Also, make sure you
  understand which Agent Workspace features [support DCL](https://support.zendesk.com/hc/en-us/articles/4408821805338#topic_lts_bdf_vpb).

**Chat and messaging**

During the migration, Chat departments and Support groups are merged. Admins manage agents
through Support groups, instead of departments on the Chat dashboard. Admins have a single
location for managing collections of agents instead of switching between interfaces. See
[Managing groups of agents](https://support.zendesk.com/hc/en-us/articles/4408821752346).

Warning: This merge cannot
be reversed. After migration, all activities associated with adding, updating, and
deleting groups of agents in Support also affect Chat departments.

- To migrate your Chat account, you need an account with Chat Phase 3 or Chat Phase 4. See
  [Determining your Zendesk Chat account version](https://support.zendesk.com/hc/en-us/articles/4408836197658).
- Chats are served directly from the ticket interface, agents cannot serve chats
  from the Chat dashboard. Agents have one single location to manage all their conversations
  (chats, social messages, web messages). [See Answering a message](https://support.zendesk.com/hc/en-us/articles/4408843683226-Receiving-and-sending-social-messages-in-the-Zendesk-Agent-Workspace#topic_fzy_pxj_2mb).
- Agents cannot see the contents of a chat or message before accepting it, but
  chat routing for messaging has been improved to help get chats and messages to the right
  agents at the right time. See [Setting triggers, automations, and views for
  messaging](https://support.zendesk.com/hc/en-us/articles/4408824058138#topic_nbm_dsl_2mb) and [Business rules for messaging](https://support.zendesk.com/hc/en-us/articles/4408821905434#topic_zgt_l3h_3nb).
- Multi-agent chats are not supported, but agents can transfer chats to other
  agents. See [Sharing chats with other agents](https://support.zendesk.com/hc/en-us/articles/4408822136346). The chat visitor
  path is only available during a live chat.

**Ticket interface**

- To provide a more-natural flow, conversations are arranged with the
  most-recent comments at the end of the flow. This takes some adjustment for agents who
  work with email messages and are familiar with seeing the latest comment at the top of the
  ticket. See [Sample ticket.](https://support.zendesk.com/hc/en-us/articles/4408821259930#topic_j53_h5h_bhb)
- Customer context has moved to a new location in the ticket interface. It has
  been expanded to include information from third-party applications. See [Viewing customer context](https://support.zendesk.com/hc/en-us/articles/4408829170458#topic_ehg_1qz_vkb).
- The ticket tab interface in the workspace has changed to work better with
  interactive conversations. Ticket numbers aren’t included on chat and messaging ticket
  tabs, but conversation status, recent comments, and channel type are highlighted. See
  [Using ticket tabs to manage conversations](https://support.zendesk.com/hc/en-us/articles/4408844108826).
- The composer maintains separate text buffers for each conversation type (for
  example, internal notes vs public comments). This may be confusing for agents when they
  first start to use it, but it enables them to switch quickly between threads without
  losing content. See [Switching channels in the composer.](https://support.zendesk.com/hc/en-us/articles/4408831849882#topic_gtw_j1h_rmb)
- The Zendesk Agent Workspace includes native [ticket redaction](https://support.zendesk.com/hc/en-us/articles/4408846470170) which provides additional functionality that
  the [Zendesk Ticket Redaction app](https://www.zendesk.com/apps/support/42515/ticket-redaction/) doesn’t support.
  Zendesk recommends uninstalling the app and using Zendesk Agent Workspace native ticket
  redaction. Ticket redaction via API commands is also fully supported with the
  workspace.

**Composer updates**

The Agent Workpace includes a new composer, powered by [CKEditor](https://ckeditor.com/), that combines support for both rich text
formatting and Markdown commands. You no longer have to switch between composers.

- Because the Agent Workspace handles markdown and formatting syntax differently, it is
  *expected* and *intended* for new markdown conventions to apply on
  pre-existing tickets comments. This can cause minor ticket formatting and spacing issues
  for legacy comments that were generated in the standard agent interface.
- After migration, Zendesk recommends that you review and possibly update any API scripts
  you use to that generate comments. This will help make sure your API scripts work as
  expected with the new composer.

Finally, it’s important to check out the current product limitations to see how they might
impact your particular situation. For example, if your account serves a very high volume of
chats. See [Limitations for the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821805338). Zendesk
recommends [evaluating your account for migration](https://support.zendesk.com/hc/en-us/articles/4408843642394-) before you
migrate.

## About the migration

Before you can activate the workspace, you have to migrate your account. During
migration, your Chat departments are merged into Support groups. This enables you to manage
collections of agents in one location, rather than switching between two separate locations.
Mapping Chat departments to Support groups is necessary for Chat transfer to work properly
in the Zendesk Agent Workspace.

Note: The migration from Chat departments to Support groups
can't be reversed.

Before migration:

- Chat agents are arranged in departments.
- Support agents are arranged in groups.
- Groups and departments are managed from Support and Chat respectively.

After migration:

- Agents are organized in groups, instead of departments. You add agents to
  groups rather than departments.
- Administrators manage groups (for Chat and Support) from Support
  settings.

Migration is required only once for your account. Going forward, you’ll manage
all your agents from Support settings. The migration from Chat departments to Support groups
can't be reversed.

Important: Only migrate your account when Chat traffic is stopped and there are no
ongoing chats. Otherwise, your active chat sessions may be lost.

If you prefer, you can test out the migration on a Sandbox account first. This
gives you time to try out the Agent Workspace and train your agents before using the
workspace in a production environment.

## Starting the migration

To prepare your account for the Zendesk Agent Workspace, Zendesk Support provides
a migration wizard to help you update your account.

Most Zendesk Suite and Support accounts are already using the Agent Workspace.
Only a few legacy accounts need to be migrated. You don't need to migrate your account
unless you see a **Get started** button on the Agent Workpace page.

Before you migrate, do the following to ensure a smooth process:

- Plan your migration for the beginning of day or when you'll have the lowest possible
  volume globally for your account, ideally before your agents start working on tickets
  for the day.
- Send a communication to your agents to let them know the migration is about to start.
  Ask them to close out their tickets and refresh their browser as soon as they see the
  [Switch workspace](https://support.zendesk.com/hc/en-us/articles/4581758611866#topic_xjc_3d3_b3b) message in the Zendesk
  interface.
- Deactivate the Web Widget on your [contact form](https://support.zendesk.com/hc/en-us/articles/4408838063258-#topic_ldx_wlc_vfb) to help agents refresh
  faster.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/contact_form_disable.png)

**To start the migration**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Agent Workspace**.

   If the Agent Workspace is available on your account, you’ll see a
   description of how to migrate.

   If you see this message, migration has been
   disabled for your account. Work with your account representative or [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to get your account
   migrated.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_migration_blocked.png)
2. Click **Get started**.

   A page appears with a description of
   what happens during the migration.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_migration_intro3.png)
3. Review the description, then click **Next** to proceed.

   If you have
   groups and departments with the same names, a page appears with instructions on **How
   to handle duplicate names**. If there’s no duplication, this page does not appear.

   To fix the duplication, you can:

   - Automatically merge groups and departments with the same name into a
     single group. This is the default.

     For example, if you have a Chat
     department named **General** and a Support group named **General**, all agents
     in the **General** Chat department are combined with all the agents in the
     **General** Support group, resulting in one large **General** group that
     included both types of agents.
   - Keep the groups separate and append the word **copy** to
     similarly-named groups.

     For example, if you have a Chat department named
     **General** and an Support group named **General**, the Support group is
     renamed **General\_copy** to distinguish it from the existing Chat department. The
     Support agents remain in the renamed **General\_copy** group and the Chat agents
     are moved to the **General\_copy** group.
4. If necessary, select **Automatically merge** or **Don’t merge**, then click
   **Migrate**.

   Depending on how many departments you have, it may take a
   few minutes or hours for the migration to complete.

   When the migration is
   complete, return to the Agent Workspace page. You'll see a checkbox to turn on the
   workspace. You may need to refresh your browser to see the change.
5. Select **Turn on the Agent Workspace**.
6. **Save** your changes.

   A tutorial appears that shows you how to use the
   new workspace.

## After the migration

Once migration is complete and the workspace is activated, agents can start [serving chats](https://support.zendesk.com/hc/en-us/articles/4408824439194) from the Zendesk Agent Workspace and administrators
can [manage agents](https://support.zendesk.com/hc/en-us/articles/4408821752346) in Support groups, instead of Chat departments. For
more information on how to work with the Zendesk Agent Workspace, see [Documentation Resources](https://support.zendesk.com/hc/en-us/articles/4408827107226).

After migration, open (or refresh) the Chat dashboard.

- All groups are listed in the **Department** tab on the Chat dashboard.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_groups_dashboard.png)
- Department settings on the Chat dashboard are changed. See example below. To edit
  group names, descriptions, and group memberships, you are automatically redirected to
  the [Groups page](https://support.zendesk.com/hc/en-us/articles/4408821199258#topic_zhr_14b_wqb) in Admin Center.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_groups_dashboard_edit.png)

Although agents are managed in groups instead of departments, departments still exist in
Chat and can be used in [routing triggers](https://support.zendesk.com/hc/en-us/articles/4565311804186).

Note: If you use custom apps in your account, after migrating Chat departments to Support
groups, your app developers should update all public APIs for Chat department Create,
Update, and Delete to public APIs for Support group Create, Update, and Delete.
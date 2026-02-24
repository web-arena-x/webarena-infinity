# Migrating to the updated CCs and followers experience

Source: https://support.zendesk.com/hc/en-us/articles/4408839371418-Migrating-to-the-updated-CCs-and-followers-experience

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Important: This article is for accounts created before May 2019 that need to update the CCs and followers experience. Accounts created after that date already use the updated CCs and followers experience.

The updated CCs and followers experience makes the behavior for when and how CCs are included on a Zendesk ticket more consistent and expected. This article describes how to migrate to the updated CCs and followers experience.

You can easily check to see if you need to update your account or if it's already using the current experience. If you see a **Followers** field in your tickets (beneath the **Assignee** field), this setting is already activated and you don't need to update your account.

This article contains the following sections:

- [About migrating to CCs and followers](#topic_gsd_sns_y2b)
- [Using the migration wizard](#topic_vjd_lws_y2b)
- [After migration](#topic_sbs_x4k_mfb)

## About migrating to CCs and followers

Previously, the behavior for CCs you included on a Zendesk ticket varied depending on whether the person you copied was an internal user (someone within your company) or an external user (a customer or other person outside your organization). It also depended on whether your reply to a ticket was an internal note or a public comment. This caused confusion.

Zendesk tickets have changed to include both followers and CCs. See the following illustration.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_onboarding_old_new.png)

When you migrate, Zendesk tickets change to include both followers and CCs. You have better options to manage public and private comments within conversation threads. For example:

- Both agents and end users can add and remove CCs just like in email.
- Agents who are followers can receive updates on the ticket without exposing their identity to end users. Agents who are added as CCs will have their email addresses exposed.
- Followers receive notifications when ticket updates occur, and they can view and create internal notes.

For a complete list of documentation about CCs and followers, see [CC and followers resources](https://support.zendesk.com/hc/en-us/articles/4408836035866).

## Using the migration wizard

To help you migrate your account for CCs and followers, Zendesk Support provides a migration wizard to help you update your account. When you migrate, you can use the wizard to:

- Automatically update business rules (triggers, automations, and macros) in your account.
- Receive guidance on how to manually update business rules, including a downloadable list of the affected rules you need to change.

In most cases, Zendesk recommends using the wizard to automatically update business rules. If you are not sure which method to use, you can choose the manual method and review the list of rules you need to change. Then, if you decide the automatic method will work for you, you can restart the wizard to automatically make the updates.

Note: If you have a sandbox installation, try updating your sandbox account first (either manually or automatically) before upgrading your production site.

**To run the migration wizard**:

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **CCs** to expand it.

   If the CCs and Followers feature is available on your account, you’ll see a highlighted section.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_get_started3A.png)
3. In the **New CC and followers experience** box, click **Set up CCs and followers**. A page appears with an introduction to CCs and followers.
4. Take a moment to read the description, then click **Next** to continue. A business rules page appears with information on how your business rules will be impacted.
5. Click **Download** to review a list of affected rules for your account.

   Use this list to make sure all the rules on your account are included. Contact Zendesk if you have any questions about the rules listed.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_onboarding_config_download.png)

   Important: Zendesk recommends you keep a backup of the affected rules list in a safe location. It can be useful if you ever need to [rollback](https://support.zendesk.com/hc/en-us/articles/4408834737434) your account and remove CCs and followers. If you **Automatically change** your account, account admins will receive an email with a link to the affected rules list.
6. Review the list of recommended changes to your account. Some changes happen automatically when you enable CCs and followers (any **Add CC** action changes to **Add follower**). Other changes require you to run the migration wizard or make the changes manually.

   The wizard displays the following summary of account rules that should be updated.

   For each trigger and automation that includes action **Email user - (requester)**:

   - Change action to **Notify by: User Email > (requester and CCs)**.
   - Remove condition **Requester > Is not > (current user)** if it exists.
   - Under **Meet ALL of the following conditions**, add condition **Ticket: Comment > Is > Public**.
7. Select how you want to make changes to your account.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_onboarding_config_man_auto2.png)

   If you are not sure which method to use, choose **Manually change**.

   - To manually change the affected rules, select **Manually change**, then click **Next**.
   - To automatically change the affected rules, select **Automatically change**, then click **Next**.

     Changes made automatically by the migration script will match the changes described in the “Recommended changes” section of the wizard.

   An activation page appears with a list of items to enable.
8. Select the items you want to enable for your account:
   - **Allow followers**: All tickets in your account will include a **Followers** field for agents, light agents, and admins.
   - **Allow CCs**: All tickets in your account will include a **CC** field for Public comments.
     - **Allow light agents to be added to tickets**: When CCs are enabled, you can also enable light agents to be added as CCs or followers on tickets, not just as followers. If this setting is not selected, light agents can only be added as followers.
     - **Allow end users to add CCs to requests**: Enable end users to add CCs to requests they submit using the help center ticket form.
   - **Automatically make a CCed agent a follower**: When an agent is added as a CC on a ticket, they will be added automatically as a follower.

   You can modify these settings later if desired.
9. Acknowledge your changes, then click **Turn on**.
   - For **Automatic** updates, the migration wizard will enable the items you selected for your account. It will also update your triggers and automations. Automatic updates may take several minutes. When the changes are complete, you’ll receive an email with a link to a file that describes the changes.
   - For **Manual** updates, your account will be upgraded to include the settings you choose to activate, but you’ll need to manually update your triggers, automations, and macros. See [Manually updating business rules](https://support.zendesk.com/hc/en-us/articles/4408845914138--Draft-Manually-updating-business-rules) for more information.

## After migration

After migration, if the new CCs experience is enabled, you should see a new **Followers** field in your tickets (beneath the **Assignee** field) and a new **CC** field in the **Public reply** area.

When an existing ticket is updated, legacy CCs on the ticket are automatically split into followers (for agents and light agents) and new CCs (for users who aren't agents).

There are also changes to the **CCs** settings for tickets. To view the changes:

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **CC and followers on tickets** to expand it.

   Notice that the name has changed From **CCs** to **CCs and followers on tickets**.
3. Choose the settings that make sense for your workflow. For example:
   - The **Only agents can add CCs** setting has been replaced. Use the new **Allow CCs** setting instead to enable (or disable) CCs for all types of users.
   - There's a new setting to **Allow agents to change the requester**. Previously, enabling CCs on tickets automatically allowed agents to change the requester. Now, you can configure this setting independently from CCs.

   Additional settings are available, including a **CCs and followers blocklist** to prevent the email addresses and domains you specify from being added as CC. For more information, see [Configuring CCs and followers permissions](https://support.zendesk.com/hc/en-us/articles/4408843795482).
4. If you have email templates, check to make sure the placeholders work as expected.
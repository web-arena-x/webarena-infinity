# Manually updating business rules for CCs and followers

Source: https://support.zendesk.com/hc/en-us/articles/4408845914138-Manually-updating-business-rules-for-CCs-and-followers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center > Objects and rules > Tickets >
Settings

When you migrate to CCs and followers, you have a choice to automatically or manually update some of your business rules as part of the migration. If you don’t update these business rules for your account, you may miss valuable notifications and emails. This article describes how to manually change business rules to work with the new CCs experience.

If you decided to automatically update your business rules as part of migration to CCs and followers, you can skip this topic. For more information, see [Migrating to CCs and followers.](https://support.zendesk.com/hc/en-us/articles/4408839371418)

This article contains the following sections:

- [Download the affected rules](#topic_otd_jyn_gfb)
- [Review affected rules](#topic_hj1_wb4_gfb)
- [Manullay update triggers](#topic_dw3_214_gfb)
- [Create a trigger that allows agents to receive "request received" email notifications](#topic_t2z_zhx_nnb)
- [Manually update automations](#topic_hz1_m14_gfb)
- [Manually update macros](#topic_qnj_5s4_gfb)
- [Manually update email templates](#topic_cjl_414_gfb)

For a complete list of documentation about CCs and followers, see [CCs and followers resources](https://support.zendesk.com/hc/en-us/articles/4408836035866).

## Download the affected rules

If you haven’t done so already, use the [migration wizard](https://support.zendesk.com/hc/en-us/articles/4408839371418--Draft-Migrating-to-CCs-and-followers#topic_vjd_lws_y2b) to download a list of affected rules for your account.

**To download the affected rules:**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **CCs and followers on tickets** to expand it.
3. Click **Set up CCs and Followers**.
4. On the **Effects on business rules** page, **Download** a list of your account’s affected rules.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_onboarding_download2.png)

   You’ll use these rules as a guideline for manually updating the business rules in your account. The affected rules are customized for your account and includes a complete list of the changes, removals, and additions you need to make to triggers and automations.

## Review affected rules

The zip file you downloaded (**affected\_rules\_list.zip**) contains these documents:

- **affected\_rules\_list.txt**: Contains the names of each trigger or automation you need to change and the URL where the trigger or automation is located. For example:

 ```
 Notify requester of received request,https://my.zendesk.com/agent/admin/triggers/8807896
 Pending notification 24 hours,https://my.zendesk.com/agent/admin/automations/8807705
 Pending notification 5 days,https://my.zendesk.com/agent/admin/automations/8807706
 ```

- **Instructions\_txt**: Contains a list of the rules that need to be changed. For example:

 ```
 * Change Email user - (requester) to Email user - (requester and CCs).
 * * When you make this change, also remove the Requester - is not - (current user) condition if it exists.
 Important: Now that CCs and followers is activated, any "Add CC" action has changed to "Add follower" to prevent exposing agent email addresses.
 ```

With this download, you can match up the instructions with the rule that is affected. For example:

- Open **Admin > Triggers > Notify requester of received request**(https://my.zendesk.com/agent/admin/triggers/8807896)
 and remove this condition:

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_onboarding_conditions2.png)
- **Open Admin > Automations > Pending notification 24 hours**(https://my.zendesk.com/agent/admin/automations/8807705)
 and change this action from **(requester)** to **(requester and CC)**:

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_onboarding_actions.png)

## Manually update triggers

Update your triggers as described in the affected rules list.

1. In the sidebar, click the **Admin** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/manage_icon.png)), then select **Business Rules > Triggers**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_onboarding_triggers.png)
2. For each affected trigger, change the trigger conditions and actions as described in the affected rules. For example, in **Actions** for a trigger, make the following changes:
   - **Before**: Email user: (requester)
   - **After:** Email user: (requester and CC)
3. Review the **Email body** text to make sure it still makes sense for the types of users who will receive the message.
4. Save your changes.

## Create a trigger that allows agents to receive “request received” email notifications

If needed, you can create a trigger that notifies the requester and agents (including light agents) that a request has been received and has become a ticket.

**To create a trigger that allows agents to receive “request received” email notifications**

1. Create a new trigger, or update an existing trigger, and title it as **Notify agent of internal note request received**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/notify_agent_internal_note_received.png)
2. Under **When ALL of these conditions are met**, add these actions:
   - **Ticket | Is | Created**: An end user or agent submits a request, which has created a new ticket.
   - **Status | Is not | Solved**: When created, the new ticket has one of the following statuses applied to it: New, Open, Pending, or On-hold.
   - **Comment | Is | Private**: Use this condition because comments about “request received” are private comments (internal notes)
   - **Current user | Is | (agent)**: The user that last updated the ticket is anyone who is a registered user, but not an agent or an administrator.
3. Add this action:
   - **Email user | (requester)**: The email defined in this action is sent to the end user or agent listed as the ticket's requester and anyone who is copied on the ticket. The requester is most-commonly the person who submitted the ticket; however, an agent can [submit a ticket request on behalf of another user](https://support.zendesk.com/hc/en-us/articles/4408882462618), in which case that user is listed as the requester.
4. Save your changes.

## Manually update automations

Update your automations as described in the affected rules list.

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Macros**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_onborading_automations.png)
2. For each affected automation, change the business rules definitions as described in the affected rules. For example, in a **Notifications** action for an automation, you might make the following changes:
   - **Before**: Email user: (requester)
   - **After:** Email user: (requester and CC)
3. Review the **Email body** text to make sure it still makes sense for the types of users who will receive the message.
4. Save your changes.

## Manually update macros

Update your macros.

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Macros**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_admin_onboarding_macros.png)
2. For each macro, make sure the action is appropriate for the current macro.
3. Save your changes.

## Manually update email templates

When you enable followers, the **CCs** email template is replaced by a **Follower** email template. Check this template to make sure the placeholders work as expected. To update the template:

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **CCs and followers on tickets** to expand it.
3. Click **Allow followers**.
4. Customize your follower email template.
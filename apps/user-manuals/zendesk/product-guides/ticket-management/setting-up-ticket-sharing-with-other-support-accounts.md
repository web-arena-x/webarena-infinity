# Setting up ticket sharing with other Support accounts

Source: https://support.zendesk.com/hc/en-us/articles/4408893967514-Setting-up-ticket-sharing-with-other-Support-accounts

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center > Objects and rules > Tickets > Settings

You can share tickets from your Support account with other accounts by establishing sharing agreements. You can specify the terms under which sharing can occur and how shared tickets are managed. The other accounts you establish sharing agreements with can also share their tickets with you if they establish sharing agreements with your account.

Ticket sharing allows you to assign tickets to affiliated accounts. Those accounts' agents can either provide information toward resolving the issue or solve the issue themselves. The ticket status and comments stay synced between the tickets in each account.

Once you've activated a sharing agreement with another account you can begin [sharing tickets](https://support.zendesk.com/hc/en-us/articles/4408886265370).

Note: This article refers to manual ticket sharing. You can also [use business rules to share tickets](https://support.zendesk.com/hc/en-us/articles/4408887148698) (not available on Team plans).

This article contains the following sections:

- [Understanding how ticket sharing works](#topic_pxh_wkz_sq)
- [Setting up a ticket sharing agreement](#topic_kjg_hhz_kc)
- [Opting out of all sharing invites](#topic_cvt_atz_kc)
- [Deactivating a sharing agreement](#topic_vam_qtz_kc)
- [Referring to shared tickets in business rules](#topic_ktu_ttz_kc)
- [Syncing custom fields with another account](#topic_uxg_hfr_hf)

## Understanding how ticket sharing works

Here's how ticket sharing works:

- Any Support account can invite another account to establish a sharing agreement.
- The initiating account (the *sender*) sets the terms of the sharing agreement, which the receiving account can accept or not.
- Sharing agreements are one way. Once the receiver accepts the agreement, the sender may share tickets with the receiver. For the receiver to share tickets with the sender, they must create and initiate a sharing agreement with the other account.
- If you only have receiving agreements, the sharing ticket field will not appear and you cannot stop sharing received tickets.
- The sender can only share a ticket with one other account. However, the receiver can share the ticket with an account that they have a sharing agreement with.
- A shared ticket becomes a new ticket in the receiver's account with a separate ticket ID.
- The ticket status, custom fields, and comments can remain synced between the ticket versions in both accounts. The custom fields must be created in both accounts (see [Syncing custom fields with another account](#topic_uxg_hfr_hf) below). CC recipients are not carried over from the original ticket to the shared ticket.

 Note: Any public or private comments added to a shared ticket will be visible to agents in both the original Support account, and the Support account the ticket is shared with. Any public comment to the shared ticket will also notify any users copied on the original ticket.
- All ticket statuses can match, except for On-hold. When a ticket is changed to On-hold in one account, it will be submitted as Open in the other.
- Tickets in the Closed status can't be shared.
- Call recordings (including voicemail recordings) in a shared ticket can only be accessed by signed-in agents of the Support account that the original call is associated with. For example, Account A shares a call ticket with Account B, which includes the calls recording. The agents in Account B will not be able to listen to that recording in the shared ticket. If they are agents in **both** accounts they can listen to the recording by signing into Account A, locating the original ticket and listening to the file there. Transcriptions of voicemails remain visible, as lines of text within the shared ticket.
- Depending on the terms of the agreement, the receiver may directly communicate with the ticket requester and solve the ticket.
- Sharing tickets creates a placeholder user in the receiving account for each user associated with the sending account ticket. The user is created even if there is a user in the receiving account with the same name and email address as the placeholder user. If an agent in the receiving account makes a comment on this shared ticket, a placeholder end user account is created in the sending account to represent this agent. Placeholder users created during ticket sharing can't be deleted.

 It's important to note that shared tickets do not pass on user information – that is, customer information such as email address or phone number are not stored. Tickets are never linked to matching users in the receiving accounts, unless an agent of the receiving account manually adjusts the requester of the shared ticket when the user is created in the receiving account. This adjustment is not recommended as it can cause issues with the sharing agreement. When a ticket is *unshared*, the receiving account cannot communicate with the requester unless the user profile is updated with a profile that includes an email address.
- Each account's business rules remain separate.
- A shared ticket cannot be merged with another ticket.
- An account can automatically refuse to accept all sharing agreement invites.
- Sharing agreements can be cancelled at any time by either the sender or the receiver.
- Sending email to another Support instance is not supported when a ticket sharing agreement is in place. Automatic email notifications from a shared Support instance are suppressed. If an agent action generates an email notification, the email is also suppressed.
- When tickets are shared between Support accounts, user fields and organization fields are not shared with the ticket.
- [Renaming an account](https://support.zendesk.com/hc/en-us/articles/4408842817434#topic_j34_xj2_4nb) involved in a sharing agreement breaks the agreement.
- If you [enable private attachments](https://support.zendesk.com/hc/en-us/articles/4408832757146#topic_nrp_bnx_xdb), then add a comment that contains an attachment, any shared accounts will not be able to view or download the attachment.
- [AI agent tickets](https://support.zendesk.com/hc/en-us/articles/9204149016346) cannot be shared.

### Understanding how custom ticket statuses map

If the sending or receiving accounts in a ticket sharing agreement have [activated and created custom ticket statuses](https://support.zendesk.com/hc/en-us/articles/4412575841306) their, ticket status options may not always match. The table below shows how a custom status on a shared ticket is managed when both accounts have the same custom status and, more importantly, what happens when they don't. Keep in mind that custom statuses are only matched when *both* the status name and category are the same.

| Is the status available on both accounts? | Change made to ticket by sending account | Update to ticket status on receiving account |
| --- | --- | --- |
| Yes | Sender changes ticket status and/or status category | Receiver’s ticket status updated to match sender’s custom status. |
| No | Sender changes ticket status and status category | Receiver’s ticket status updated to the [default custom ticket status](../ticket-customization/managing-ticket-statuses.md#topic_zgh_dbh_vrb) in the new category. |
| No | Sender changes ticket status only; no change to status category | Receiver’s ticket status does not change. |
| N/A | Sender does not change ticket status or status category | Receiver’s ticket status does not change. |

## Setting up a ticket sharing agreement

Set up ticket sharing by creating a ticket sharing invite and defining the terms (permissions) of the sharing agreement. You must be an admin to set up a ticket sharing agreement. If you have multiple brands, you can use ticket sharing with any brand; however, the sharing agreement must be set up with your account's default brand.

A sharing agreement grants another account permission to work on your tickets. You can grant one of the two following permissions:

- Make public & private comments, sync status
- Make private comments, do not sync status

The first option allows the receiver to communicate directly with the requester and to change the ticket status (for example, setting it to Solved). These ticket updates are also reflected in the sender's version of the ticket. Although the receiver may be allowed to make public comments and directly interact with the requester, email notifications will link back to the account where the request was originally submitted.

The second option (private comments only and no status syncing) limits the other account to providing you with information needed to resolve the support request. For example, imagine a company that builds something that includes components from other companies. Each affiliated company (business partner) can set up a Support account and a sharing agreement to provide more details on issues related to the components they supply. In this scenario, the sender controls the ticket from initial request through to resolution, gathering information as needed from the affiliated account.

**To create a ticket sharing invite**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Tickets > Sharing**.
2. Select **add sharing invite**.
3. In the window that appears, select **another Zendesk Support account** or **a third-party system**.
4. Enter the URL for the account you're sharing tickets with. Depending on the option you selected in the previous step, you'll see one of the following fields:
   - Zendesk Support account: **Partner Zendesk domain** field
   - Third-party systems: **Sharing URL** field
5. Select an option from the **Comment status and permissions** field:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sharing_comments.png)

   - Make public & private comments, sync status
   - Make private comments, do not sync status
6. Select an option from the **Tag synchronization** field:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sharing_tag.png)

   - No, do not share tags between me and the receiver
   - Yes, share tags between me and the receiver

     Note: Tags that are added by business rules are not synced between shared tickets.
7. (Applies only if sharing with another Zendesk Support account) Select the custom fields syncing setting. You have two options:
   - No, do not sync custom fields between me and the receiver
   - Yes, sync custom fields between me and the receiver
8. Click **Send Invite**.

The receiver is notified of the invite on their Ticket Sharing page, as shown here:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_sharing_invite_notification.png)

The receiver can view the terms of the sharing invite and either accept, decide later, or decline the agreement.

When accepted, both accounts can immediately share tickets.

If you decline an agreement, the sender is free to try again at another time. If you don't want to establish sharing agreements with any other accounts, you can set your account to automatically decline invites (see [Opting out of all sharing invites](#topic_cvt_atz_kc)). You can also deactivate sharing agreements at any time (see [Deactivating a sharing agreement](#topic_vam_qtz_kc)).

All of your sharing agreements (accepted, pending, and rejected) are displayed on the Ticket Sharing page.

## Opting out of all sharing invites

If you decide to not share tickets with any other account, you can choose to opt out of all sharing invites.

**To opt out of sharing invites**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Tickets > Sharing**.
2. In the **Opt out of sharing** section, select the **Decline all sharing agreement invites**.
3. Click **Save Tab**.

With this option set, you will never be informed of a sharing invite.

## Deactivating a sharing agreement

Sharing agreements can be deactivated by either the sender or the receiver at any time. Deactivated agreements can't be reactivated, but both accounts are free to invite the other to accept a new sharing agreement.

**To deactivate a sharing agreement**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png) **Objects and rules** in the sidebar, then select **Tickets > Sharing**.
2. Locate the agreement you want to deactivate and then select **View**.
3. Click **Deactivate agreement**.

Your agreement partner will be informed of the deactivation via email and this will also be reflected on their Ticket Sharing page. Deactivating an agreement means that no new tickets can be shared and that tickets that have already been shared will no longer be synced.

## Referring to shared tickets in business rules

Tickets that have been created in your Support account via ticket sharing can be referenced as conditions in automations, triggers, and views. The condition **Update via** also includes **Ticket sharing** as a value.

You can create a view of the tickets generated from ticket sharing, as in this example:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_sharing_view_new.png)

This will show you all the tickets that were shared to you. If you want to create a view of the all tickets you shared to another account, you can add a tag to the tickets and create business rules from that.

You can create automations or triggers that include the ticket sharing conditions. Again, using **Update via is Ticket sharing** as a condition you can create a trigger to escalate the shared ticket to a specific support group, to add tags, and so on.

Additionally, you can filter the view to show only inbound or outbound tickets if you have set up receiving agreements in your account.

- For inbound tickets, add a clause: **Ticket sharing: Received from** > (*instance name of who you are sharing tickets with*).
- For outbound tickets, add a clause: **Ticket sharing: Sent to** > (*instance name of who you are sharing tickets with*).

Note: In some cases, when a trigger in the receiving account sends notification for the new, shared ticket, if the ticket has multiple comments, the notification might include only a few comments and not all of the comments that are actually in the ticket.

## Syncing custom fields with another Support account

As described in [Setting up a ticket sharing agreement](#topic_kjg_hhz_kc), you can select to sync custom fields with another Support account. To make this work, each account must create the custom fields separately. For example, if you want to sync a custom field called "Camera model" it must exist in both accounts and must have the same title and data type.

The custom field title is not case sensitive so the sync will be successful even if one custom field is called "Camera model" and the other is called "Camera Model".

What is important to keep in mind is the data types used in each custom field; they must be compatible. The simplest way to ensure this of course is to use the same data type for each. In our example, both versions of "Camera model" are drop-down lists.

Note: It's possible to sync data between different kinds of custom fields if they both support the same type of data. For example, it's possible to sync a drop-down list with a text field since both contain a text string. This is not recommended but is mentioned here so that you're aware of the compatibility.

Other syncing rules include:

- Support includes two types of ticket fields: custom ticket fields and system ticket fields. It's not possible to sync system ticket fields. For more information about the differences between these two types of fields, see [About ticket fields](https://support.zendesk.com/hc/en-us/articles/4408886739098).
- If an incompatibility between custom fields does exist, the ticket will sync, but the incompatible custom fields will fail (no data will be transferred).
- If you're using a ticket field that has tags associated with its corresponding values (for example, drop-down fields), the tags must be the same across both instances. If you have matching ticket field names and values, but the tags differ, the sync between ticket fields will fail.
- If a ticket is shared between two accounts, only the account where changes to the field value are made will see a record of that change in the ticket events/audits. The other account will see the altered field value, but will not see any details about the change, such as who made it or when it was made.
- When syncing custom fields between two accounts, the custom fields must be present in at least one ticket form of the receiving account.
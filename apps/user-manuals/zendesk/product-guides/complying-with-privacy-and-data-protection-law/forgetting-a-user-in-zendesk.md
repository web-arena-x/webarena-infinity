# Forgetting a user in Zendesk

Source: https://support.zendesk.com/hc/en-us/articles/4408845703194-Forgetting-a-user-in-Zendesk

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

This guide describes how to delete an end user or agent in Zendesk Support to
help meet your obligations under the General Data Protection Regulation
(GDPR). GDPR is a European privacy regulation that aims to strengthen the
security and protection of personal data of citizens of the European Union
(EU).

Individuals from certain regions have a *right to erasure*, or the right to be forgotten or
deleted. On request, you may have an obligation to delete the personal data of an
individual.

Topics covered in this guide:

- [What is personal data?](#topic_w3d_vck_hdb)
- [Understanding the workflow](#topic_jkm_qjj_hdb)
- [Understanding the effects of deleting users or tickets](#topic_z5p_xs1_sdb)
- [Deleting personal data in ticket conversations](#topic_jdr_c2w_zcb)
- [Deleting personal data in other Zendesk products](#topic_nrr_44z_hdb)
- [Permanently deleting the end user or agent](#topic_ojp_mjj_hdb)
- [Disclaimer](#topic_tgb_yyf_gdb)

In this article, *users* can be end users or agents as the terms are defined
in the [Zendesk Customer Agreement](https://www.zendesk.com/company/agreements-and-terms/zendesk-customer-agreement/).

To learn more about GDPR, your role as data controller, or meeting your
obligations in other Zendesk products, see [Complying with GDPR in Zendesk
products](https://support.zendesk.com/hc/en-us/articles/4408834005530).

## What is personal data?

Personal data, or personal information, is any data that can be used to identify an individual.
Examples include an email address, a phone number, or a social security number.
Personal data may also include any data that could be used indirectly to identify an
individual. For example, a person's nickname such as "Gerry" may not be personal
data because many people may have the same nickname. However, if the nickname can be
combined with other data such as a work address, the nickname could be considered
personal data because it helps identify the individual.

Your organization needs to decide what personal data is. Is it simply an email address or phone
number, or do you further disambiguate using a combination of identities or
attributes? This decision is up to you.

If you’re unsure whether or not a piece of information is personal data, it’s best to err on the
side of caution. Another option is to seek legal advice.

## Understanding the workflow

You should delete an end user or agent only as the last step in the
workflow for deleting personal data. The order of the tasks is
important because you need the user's profile data to find their
personal data in tickets and other resources. If you permanently
delete the user first, finding their personal data will be more
difficult.

The high-level workflow for deleting the personal data of an end user or
agent is as follows:

1. Delete personal data in ticket conversations.
2. Delete personal data in Zendesk Guide, Zendesk Chat, or Zendesk
   Talk if you use any of those products.
3. Permanently delete the end user or agent from Zendesk Support.

This article follows the general workflow:

- [Deleting personal data in ticket conversations](#topic_qb1_frh_gdb)
- [Deleting personal data in other Zendesk products](#topic_nrr_44z_hdb)
- [Permanently deleting the end user or agent](#topic_ojp_mjj_hdb)

## Understanding the effects of deleting users or tickets

### Effects of permanently deleting a user in Zendesk Support

**Admin interface**

- Deletes the end user or agent profile
- Replaces the user's name in any system field with the
  placeholder string "Permanently Deleted User"
- Deletes the user from any organization or group in
  Zendesk Support
- Deletes the user from Insights and all product
  reports

**NPS and CSAT results**

- Scrubs the user's CSAT comments, but preserves the
  user's ratings
- Scrubs the user's email and any comments in NPS survey
  results, but preserves the user's ratings

**Zendesk products**

- Deletes the end user or agent from Zendesk Guide
- Deletes the agent from Zendesk Chat
- Deletes the end user or agent from Zendesk Talk
- Deletes the end user or agent from Zendesk Explore

Deleting an end user or agent in Support has no effect on the
imported users or product users in Zendesk Connect. The two
products don't share users.

### Effects of permanently deleting a ticket

Permanently deleting a ticket deletes the ticket's conversation
(comments), inline images, attachments, and call recordings.
For reporting purposes, the following attributes of a
permanently deleted ticket are preserved:

- Ticket id
- Channel the ticket came from
- Created at time
- Updated at time
- Status: deleted
- Requester id
- Submitter id
- Assignee id
- Group id
- Brand id
- Generated timestamp

Any user id in the record is not traceable to an actual person if
that user has been permanently deleted. See [Permanently deleting the end user or agent](#topic_ojp_mjj_hdb).

## Deleting personal data in ticket conversations

The first step is to find personal data in ticket conversations and then
delete it. A ticket conversation consists of all the comments on the
ticket. You have several options for deleting the data, including
redacting strings in the conversation and deleting the ticket
itself.

Tip: With the [Advanced Data Privacy and
Protection add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906), you can use [redaction suggestions](https://support.zendesk.com/hc/en-us/articles/6669399593882)
to automatically highlight certain types of personally identifiable
information (PII) within a ticket for agents with appropriate
permissions. Redaction suggestions proactively identify PII rather
than rely on the agent to identify PII that needs to be
redacted.

You might not be able to delete certain data from a ticket conversation.
In particular, closed tickets can't be edited and the bulk of your
tickets might be closed. You'll have to delete those tickets.

At this stage, you can ignore any personal data in the ticket that the
system retrieves from the user profile, such as the requester's name
that appears in the ticket locations in the following screenshot.
The data will be replaced with the placeholder string "Permanently
Deleted User" when you delete the user in the last step of the
workflow.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gdpr_system_user_fields.png)

Topics covered in this section:

- [Creating a list of search terms](#topic_jgs_54f_3db)
- [Searching for personal data](#topic_nkh_spk_hdb)
- [Deleting personal data in ticket conversations](#topic_qb1_frh_gdb)
- [Permanently deleting tickets](#topic_fhk_pgt_ycb)
- [Using the Zendesk API](#topic_cyj_kbg_3db)

### Creating a list of search terms

You need a list of possible search terms to find the user's
personal data in ticket conversations. You can get the
initial search terms from the user's profile in Zendesk
Support.

**To create an initial list of search terms**

1. In the agent interface, click the **Search** icon
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_icon.png)) in the upper-right of
   the top toolbar and search for the user's name or
   other identifying information.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_search_box.png)
2. On the results page, switch to the **Users** tab and
   select the user to open their profile page.
3. Add any of the following information from the profile to
   your list:
   - name and alias
   - primary email address and any other email
     addresses
   - any Facebook or X (formerly Twitter) contact
     info
   - any other identifying information in custom
     ticket fields

### Searching for personal data

Go through your list of search terms to find personal data in
ticket conversations. Inline images, attachments, and call
recordings may contain personal data that isn't searchable.
Make sure to manually check any image, attachment, and call
recording in the tickets in your search results.

**To search for personal data**

1. In the agent interface, click the **Search** icon
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_icon.png)) in the upper-right of
   the top toolbar and search for each of your search
   terms to find tickets that contain the information.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gdpr_search.png)
2. Select a ticket from the results and review the
   conversation, including any inline images,
   attachments, and call recordings.

   If during your
   review you discover other identifying information
   that your organization defines as personal data,
   add it to your search list. For example, if you
   find out that the user included their home address
   in a comment, add it to the list.

   Note: Your
   organization decides what personal data is.
3. Confirm that the personal data in the conversation
   belongs to the user.

   Make sure to positively
   identify the user before deleting data. The
   conversation may be referring to another person
   with the same name or alias.
4. Delete the personal data as follows:
   - If the ticket is closed, permanently delete
     the ticket. There's no way to redact information
     in conversations of closed tickets. See [Permanently deleting tickets](#topic_fhk_pgt_ycb).
   - If the data consists of a string in the
     conversation, redact the string. See [Deleting personal data in ticket conversations](#topic_jdr_c2w_zcb).
   - If the data is in an inline image or an
     attachment, permanently delete the ticket. See
     [Permanently deleting tickets](#topic_fhk_pgt_ycb).
   - If the data is in a call recording, delete the
     call recording. See [Deleting personal data in call recordings](#topic_l3h_1jz_hdb).

### Deleting personal data in ticket conversations

You can redact personal data in ticket conversations. With
redaction, you specify a text string to redact from the
conversation, and it replaces the characters in the string
with a replacement character. For example:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_ticket_redaction.png)

Note: Redaction may have limitations when used with rich text or
languages containing non-ASCII characters.

In the [Zendesk Agent
Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930), you can use native ticket
redaction to redact personal data. You don’t need to install
a separate app. See [Redacting ticket
content](https://support.zendesk.com/hc/en-us/articles/4408846470170).

Some notes about ticket redaction:

- Redaction completely deletes the string from
  Zendesk databases, but it doesn't purge it from
  any existing logs of when the ticket was
  originally created. The logs are automatically
  deleted after a period of time.
- Similarly, you can redact phone numbers in
  strings, but it doesn't delete the phone numbers
  used as identities in the system.
- You can use redaction to delete inline
  attachments.

### Permanently deleting tickets

Both administrators and agents with delete permissions can delete
tickets in the agent interface. Deleted tickets are moved
into a Deleted Tickets view, where you then permanently
delete them.

Agents must have [permission to delete
tickets](https://support.zendesk.com/hc/en-us/articles/4408832689818).

Tip: Consider creating a data
retention policy using a [ticket deletion
schedule](https://support.zendesk.com/hc/en-us/articles/6388012977306). A ticket deletion schedule
automatically deletes archived tickets that have been
*closed and not modified* for a specified
period of time, helping you remain compliant. The [Advanced Data Privacy
and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6119316155930) allows you to activate
multiple ticket deletion schedules to delete tickets that
meet specific criteria, such as by brand, group, or type.
Deleted archived tickets can't be restored, so exercise
caution when activating deletion schedules.

**To delete one or more tickets**

1. With the ticket open in the agent interface, click the
   Ticket options menu in the upper right, then select
   **Delete**.

   The Ticket options menu looks
   slightly different in the [Zendesk Agent
   Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) (shown on the left) and the
   standard agent interface (shown on the
   right).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_options_delete.png)
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket-options-menu.png)
2. If you want to delete more than one ticket, select
   multiple tickets in the search results.

   A toolbar
   appears at the bottom of the list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gdpr_delete_tickets.png)
3. Click **Delete**.
4. When prompted, click **OK** to confirm the
   deletion.

   The tickets are deleted and moved to
   the Deleted tickets view. The next step is to
   permanently delete them.
5. Click the **Views** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_icon.png)) in the sidebar, then
   click **Deleted tickets** in the Views list.
6. Click the checkbox beside the ticket or tickets you want
   to permanently delete.

   A toolbar appears at the
   bottom of the list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gdpr_delete_tickets_perm.png)
7. Select **Delete permanently**.
8. Confirm that you want to permanently delete the
   tickets.

### Using the Zendesk API

You can use the Zendesk API to find and delete personal data in
ticket conversations.

The following deletion rules apply with the API:

- If the ticket is closed, permanently delete the ticket.
  There's no way to redact information in
  conversations of closed tickets.
- If the data consists of a string in the conversation,
  redact the string.
- If the data consists of an attachment in the
  conversation, redact the attachment.
- If the data is in an inline image, permanently delete
  the ticket.

#### Searching ticket conversations with the API

Use the following endpoints:

- [Search](https://developer.zendesk.com/rest_api/docs/support/search)
- [List
  Comments](https://developer.zendesk.com/rest_api/docs/support/ticket_comments#list-comments)

#### Deleting personal data in conversations with the API

Use the following endpoints:

- [Redact String in
  Comment](https://developer.zendesk.com/rest_api/docs/support/ticket_comments#redact-string-in-comment)
- [Redact Comment
  Attachment](https://developer.zendesk.com/rest_api/docs/support/attachments#redact-comment-attachment)

#### Permanently deleting tickets with the API

Use the following endpoints:

- [Delete Ticket
  Permanently](https://developer.zendesk.com/rest_api/docs/support/tickets#delete-ticket-permanently)
- [Delete Multiple
  Tickets Permanently](https://developer.zendesk.com/rest_api/docs/support/tickets#delete-multiple-tickets-permanently)

## Deleting personal data in other Zendesk products

If you use other Zendesk products, make sure to delete the personal data
of the end user or agent in the products before you delete the user
in Zendesk Support. Permanently deleting an end user or agent in
Support also deletes them from the following products:

- Zendesk Guide
- Zendesk Sell
- Zendesk Chat (for agents)
- Zendesk Message
- Zendesk Talk
- Zendesk Explore

Note: Deleting an end user or agent in Support has no effect on the product
users or imported users in Zendesk Connect. If your organization
receives a request to delete a user from Connect, send an email to
**support@connect.zendesk.com** requesting the deletion
of the user's data and their user journey from Connect. The data is
permanently deleted.

Personal data can be found in the following resources in other Zendesk
products:

- Help center content
- Leads, deals, and contacts information in Sell
- Chat transcripts
- Message conversations
- Call recordings
- Data stored in Explore for analytics purposes

Topics covered in this section:

- [Deleting personal data in your help center](#topic_v1s_fjz_hdb)
- [Deleting leads and contacts data in Sell](#topic_jnd_lrb_5qb)
- [Deleting personal data in Zendesk Chat](#topic_iqm_2jz_hdb)
- [Deleting personal data in message conversations](#topic_ewr_bjz_hdb)
- [Deleting personal data in call recordings](#topic_l3h_1jz_hdb)
- [Deleting personal data in Explore](#topic_lmn_q52_kdb)

### Deleting personal data in your help center

Personal data may be contained in articles, posts, and comments
in your help center.

**To delete personal data in help center content**

1. Create a list of search terms, as described in [Creating a list of search terms](#topic_jgs_54f_3db).
2. Use your help center search to find the personal data in
   the content.
3. Confirm that the personal data in the content belongs to
   the user.

   Make sure to positively identify the
   user before deleting data. The content may be
   referring to another person with the same name or
   alias.
4. Delete the personal data as follows:
   - **Articles** Delete the article. You must
     archive the article first, then delete the
     archived article. The procedure soft deletes the
     article, making it unavailable for everyone
     including Knowledge admins through the UI or the API.
     The article will still be in the Zendesk database
     and accessible on a limited basis to employees
     with certain database privileges. Soft deleting
     the article will also soft delete any inline and
     block attachments. See [Deleting an article
     from your knowledge base](https://support.zendesk.com/hc/en-us/articles/4408832480154) in the Guide
     docs.

     Simply editing the article to remove the
     personal data is not enough. On the Zendesk Suite
     Growth plan and above and Guide Professional and
     Enterprise plans, the data is maintained in the
     system to show [article revisions
     and history](https://support.zendesk.com/hc/en-us/articles/4408829321498) in the Guide interface. You can
     create a new article that doesn't contain the
     personal data.
   - **Community posts** Edit or delete the
     post. Deleting the post soft deletes it, meaning
     it's no longer accessible by anybody, including
     admins, in the Guide interface. Any comments and
     inline attachments associated with the post are
     soft deleted too. The attachments will no longer
     be accessible through the URL. See [Editing and
     deleting community posts and comments](https://support.zendesk.com/hc/en-us/articles/4408823846170#topic_gzn_4hf_4k) in
     the Guide docs.
   - **Comments** Edit or delete the comment.
     Deleting an article or post comment soft deletes
     it, meaning it's no longer accessible by anybody,
     including admins, in the Guide interface. Any
     inline attachments associated with the comment are
     soft deleted too. The attachments will no longer
     be accessible through the URL.

### Deleting leads and contacts data in Sell

In alignment with GDPR, if your customer requests that their
information be removed from your database, you can delete
that lead and/or contact in Sell and any information
relating to them. For more information, see [Deleting leads and
contacts](https://support.zendesk.com/hc/en-us/articles/4408832226842).

### Deleting personal data in Zendesk Chat

Chat transcripts in Zendesk Chat may contain personal data.

An end user may also have a visitor profile in Chat. The visitor
profile is not deleted when you delete the end user in
Support.

Topics covered:

- [Deleting personal data from chat transcripts](#topic_h32_wng_3db)
- [Deleting a visitor profile from Chat](#topic_jwq_xng_3db)

#### Deleting personal data from chat transcripts

Chats may contain personal data. Images and attachments
in chat transcripts might have some too.

**To delete personal data in chat transcripts**

1. Create a list of search terms, as described in
   [Creating a list of search terms](#topic_jgs_54f_3db).
2. From the dashboard in Chat, select
   **History**.
3. In the History tab, search for the items on your
   search list.
4. Select a chat from the results and review the
   transcript, including images or attachments.
5. Confirm that the personal data belongs to the
   user.

   Make sure to positively identify the user
   before deleting data. It may refer to another
   person with the same name or alias.
6. Delete the personal data as follows:
   - **Images and attachments** Delete images
     and attachments in chat transcripts.
   - **Chats** Permanently delete the chat.

#### Deleting a visitor profile from Chat

An end user may have a visitor profile in Chat. However,
deleting an end user in Support doesn't delete the
end user's visitor profile in Chat.

**To delete an end user's visitor profile in
Chat**

- Delete all the chats involving the visitor.

### Deleting personal data in message conversations

Only admins can delete a message conversation.

**To delete a conversation**

1. In the dashboard, click the **Done Conversations**
   icon in the left sidebar.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/done_conversations.png)
2. Select the conversation to delete, then select **Delete
   session** from the extended (...) menu in the
   upper-right side of the page.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/delete_session.png)

### Deleting personal data in call recordings

If you use Zendesk Talk, personal data may be contained in call
recordings. The call recordings are included in tickets in
Zendesk Support.

You can delete call recordings from tickets as described in this
section.

Call recordings are also deleted if you permanently delete a
ticket. See [Permanently deleting tickets](#topic_fhk_pgt_ycb).
The recording is soft deleted at first, then hard deleted
automatically 7 days later. The call recordings are also
deleted from Zendesk Talk’s service provider, Twilio.

**To manually delete a call recording from a ticket**

1. In Zendesk Support, select the ticket with the recording.
2. Next to the recording, click **delete recording**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/talk_delete_recording.png)

   Important: Once deleted, the recording will be permanently removed from the ticket and cannot be recovered. The deletion will not be noted in the ticket events log.
3. Click **OK**.

**To automatically delete call recordings after an
interval**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Talk**.
2. Select the **Lines** tab.
3. Click the line you want to automatically delete recordings for.
4. In the **Call recording** tab, select a timeframe for live call recordings in the
   **Automatic deletion** field.
5. Click **Save changes**.

### Deleting personal data in Explore

The data that Explore stores for analytics purposes may contain
personal data. Explore replicates this data from upstream
products such as Support, Talk, Chat, or Guide. To delete
the personal data, delete the information in the upstream
products. See the instructions for each product for details.
It takes up to 24 hours for corrections to be reflected in
Explore.

## Permanently deleting the end user or agent

After deleting personal data from any resources in Zendesk products, you
can proceed to delete the end user or agent from Zendesk Support.
Deleting the user in Support also deletes the user in Guide, Chat
(for agents), Message, Talk, and Explore. The user is also deleted
from all product reports.

You can't delete an end user or agent who's a requester on a ticket that
hasn't been *closed* yet. See [What is the difference
between a Solved ticket and a Closed ticket?](https://support.zendesk.com/hc/en-us/articles/4408887712154) First,
the ticket must be solved before it can be closed. Second, the
solved ticket must be closed by a trigger or automation. The ticket
can't be closed directly in the agent interface. To close the ticket
immediately, you can create a trigger for the specific purpose of
closing the ticket. For details, see the tech note [How can I manually close a
ticket?](https://support.zendesk.com/hc/en-us/articles/4408827596570-How-can-I-manually-close-a-ticket-)

Deleting a user permanently is a 2-step procedure:

1. Soft delete the user.

   This deletes the user from the account,
   but the user is still in the Zendesk database for 30
   days and accessible on a limited basis to Zendesk
   employees with certain database privileges.
2. Permanently delete the user.

   Zendesk permanently deletes
   soft-deleted users after 30 days automatically.
   Administrators can permanently delete soft-deleted
   users before the 30 days timeframe.

You can't permanently delete the user unless you soft delete them
first.

Both agents and administrators can soft delete end users or agents in the
agent interface in Zendesk Support. Agents can delete end users
while administrators can delete all users except the account owner.
Zendesk retains information about the account owner to continue
providing its services. When the account is terminated, Zendesk
follows its [Data Deletion Policy](https://www.zendesk.com/company/policies-procedures/data-deletion-policy/)
to purge the remaining profile data.

Only administrators can hard delete a user after they've been soft
deleted.

### Soft delete a user

**To soft delete a user**

1. In the agent interface, click the **Search**
   icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_icon.png)) in the upper-right of
   the top toolbar and search for the user's name or
   other identifying information.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_search_box.png)
2. On the results page, switch to the **Users**
   tab and select the user to open their profile
   page.
3. Make sure the user is in fact the person
   requesting to be deleted.
4. In the user's profile, click the User options
   arrow in the upper right, then select
   **Delete**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/user-options-top-right.png)
5. When prompted, click **OK** to confirm the
   deletion. If you want to cancel the deletion,
   click **Cancel** instead.

The user is soft deleted, meaning the user is still in the
Zendesk database and accessible on a limited basis to
Zendesk employees with certain database privileges. You can
now permanently delete the user, or take no additional
action, and Zendesk deletes the user permanently after 30
days.

Only administrators can permanently delete an end user or
agent.

Depending on the amount of data currently queued for deletion, it
may take time for the system to delete users
permanently.

### Permanently delete a user

**To permanently delete a user**

1. Soft delete a user as described in [Soft delete a user](#topic_wtk_xhz_wvb).
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Deleted users > Deleted users**.
3. Click the user you want to delete permanently from the
   list. A screen appears with the user's name and
   their associated tickets.
4. Click **Delete User**.

## Using the Zendesk Support API to delete a user

You can use the Zendesk Support API to find and delete an end user or
agent in Zendesk Support, which deletes the user in Guide, Chat (for
agents), Message, Talk, and Explore.

### Identifying the user

You must specify user ids in the delete endpoints. Use any of the
following endpoints to get the id of the user:

- [Search
  Users](https://developer.zendesk.com/rest_api/docs/support/users#search-users)
- [List
  Users](https://developer.zendesk.com/rest_api/docs/support/users#list-users)

You can also get a user id from the profile page of the end user
or agent in Zendesk Support. The id appears in the URL of
the profile page:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/user_id_in_profile_page.png)

### Permanently delete one or more users with the API

A user must be soft deleted before you can permanently delete
them.

Use the following endpoints:

- [Delete User](https://developer.zendesk.com/rest_api/docs/support/users#delete-user)
  (preliminary soft delete)
- [Bulk Delete
  Users](https://developer.zendesk.com/api-reference/ticketing/users/users/#bulk-delete-users) (preliminary soft delete)
- [Permanently Delete
  User](https://developer.zendesk.com/rest_api/docs/support/users#permanently-delete-user)

## Disclaimer

This document is for informational purposes only and does not constitute legal advice. Readers should always seek legal advice before taking any action with respect to the matters discussed herein.
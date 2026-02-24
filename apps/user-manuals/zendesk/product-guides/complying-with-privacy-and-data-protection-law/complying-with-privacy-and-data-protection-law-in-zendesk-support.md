# Complying with Privacy and Data Protection Law in Zendesk Support

Source: https://support.zendesk.com/hc/en-us/articles/4408823195930-Complying-with-Privacy-and-Data-Protection-Law-in-Zendesk-Support

---

This guide describes how certain features and functionality in Zendesk
Support can assist with your obligations under privacy law.

To learn more about meeting your obligations in other Zendesk products,
see [Complying with GDPR in Zendesk
products](https://support.zendesk.com/hc/en-us/articles/4408834005530).

In this guide, *users* can be End-Users or Agents as the terms are defined
in the [Zendesk Customer Agreement](https://www.zendesk.com/company/agreements-and-terms/zendesk-customer-agreement/).

Topics covered in this guide:

- [Meeting an access obligation](#topic_qdm_yhk_gs)
- [Meeting a correction obligation](#topic_ezm_pcv_4v)
- [Meeting an erasure or deletion obligation](#topic_p3p_zhk_gs)
- [Meeting a data portability obligation](#topic_ekz_13k_gs)
- [Meeting the objection obligation](#topic_gcn_swl_ycb)
- [Disclaimer](#topic_tgb_yyf_gdb)

## Meeting an access obligation

Individuals from certain regions have a *right of access*. On request, you may
have an obligation to inform an end user or agent where their personal data is being
held and for what purposes.

If a data subject requests a copy of their personal data, you can export
the data from Zendesk Support as described in [Meeting a data portability obligation](#topic_ekz_13k_gs).

## Meeting a correction obligation

Individuals from certain regions have a *right to rectification*, or the right to have
inaccuracies in their personal data corrected. On request, you may have an
obligation to provide the individual with their personal data and fix inaccuracies
or add missing information.

Both agents and administrators can access and update user data in Zendesk
Support. End users can also access and update some of their personal
data.

The following topics describe how to access and update user data:

- [Updating personal data](#topic_fkc_xqn_zcb)
- [Letting end users update some personal data](#topic_klj_35n_zcb)
- [Updating personal data with the API](#topic_bdz_dm4_zcb)

If an end user or agent requests their personal data, you can export the
data from Zendesk as described in [Meeting a data portability obligation](#topic_ekz_13k_gs).

### Updating personal data

**To update an end user's or agent's personal data as an agent
or administrator**

1. Navigate to a user's profile in Zendesk Support (see [Viewing a user's profile in Zendesk
   Support](https://support.zendesk.com/hc/en-us/articles/4408822762650)).
2. Click the user's name to enter a new profile name.
3. Click the down arrow next to the **+New ticket** button at the top right of the profile to merge, suspend, delete, or assume the identity of the user.
4. To edit a user's details, click the field box you would like to edit. You can also add user's
   contact information from this location.

For details of the default user fields, see the table in [Viewing a user's
profile in Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408893585178#topic_vmc_tvn_x1b). The sidebar may
also include [custom user
fields](https://support.zendesk.com/hc/en-us/articles/4408822051866).

For more information, see the following topics in the Support
Help Center:

- [Editing and
  deleting users](https://support.zendesk.com/hc/en-us/articles/4408893585178#topic_ifn_tvn_x1b)
- [Adding user contact
  information](https://support.zendesk.com/hc/en-us/articles/4408893585178#topic_n4q_r14_x1b)

### Letting end users update some personal data

In some cases, end users can use Help Center to view or update
certain personal data in their Help Center community
profile. You must meet the following account
requirements:

- Help Center is activated
- You have the Zendesk Suite Growth plan or above or
  Zendesk Support with Guide
- User profiles are [enabled](https://support.zendesk.com/hc/en-us/articles/4408832453658) in
  Help Center

If you meet these requirements, the end user can use Help Center
to change their community profile, which includes their
name, profile photo, email address, phone number, and the
short description of themselves. This also updates the
corresponding data in the user profile in the agent
interface.

Note: If the name, avatar, phone number, and email were set in the
user profile in the agent interface, the fields are grayed
out in the community profile. The fields must be updated in
the agent interface. See [Updating personal data](#topic_fkc_xqn_zcb).

**To update personal data as an end user**

1. Sign in to Help Center.
2. Open your profile by clicking your name in the upper
   right corner of any page in Help Center and
   selecting **My profile**.

   You can also click
   your name in an article, post, comment, or search
   result in Help Center.
3. On your profile page, click **Edit Profile**.
4. Make changes and click **Close**.

### Updating personal data with the API

Administrators and agents can use the [Users API](https://developer.zendesk.com/rest_api/docs/support/users) to
update the personal data of end users or agents. When an
agent or admin makes the API request, the user records
returned have the attributes described in [JSON Format for Agent
or Admin Requests](https://developer.zendesk.com/rest_api/docs/support/users#json-format-for-agent-or-admin-requests).

Zendesk also has a [User Identities
API](https://developer.zendesk.com/rest_api/docs/support/user_identities#user-identities) for updating the *identities* of end
users or agents. An identity is something that can be used
to identify an individual. It's typically an email address,
a phone number, or an X (formerly Twitter) handle. See the [JSON format](https://developer.zendesk.com/rest_api/docs/support/user_identities#json-format)
table in the User Identities doc for the attributes of each
record.

The following endpoints take one or more user ids as parameters.
See [Getting the id of an end user or agent](#topic_dn5_jlp_zcb).

**To update the personal data of a specific end user or
agent**

- `PUT /api/v2/users/{user_id}.json`
- `PUT
  /api/v2/users/{user_id}/identities/{identity_id}.json`

See [Update User](https://developer.zendesk.com/rest_api/docs/support/users#update-user)
and [Update
Identity](https://developer.zendesk.com/rest_api/docs/support/user_identities#update-identity) in the developer documentation. Use
the [List
Identities](https://developer.zendesk.com/rest_api/docs/support/user_identities#show-identity) endpoint to get the id of the
identity you want to update.

**To update the user record of multiple users or agents**

- `PUT /api/v2/users/update_many.json`
- `PUT
  /api/v2/users/update_many.json?ids={user_ids}`

See [Update Many
Users](https://developer.zendesk.com/rest_api/docs/support/users#update-many-users) in the developer documentation.

#### Getting the id of an end user or agent

Use any of the following endpoints to get a user id:

- [Search
  Users](https://developer.zendesk.com/rest_api/docs/support/users#search-users)
- [List
  Users](https://developer.zendesk.com/rest_api/docs/support/users#list-users)

You can also get a user id from the profile page of the
end user or agent in Zendesk Support. The id appears
in the URL of the profile page:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/user_id_in_profile_page.png)

## Meeting an erasure or deletion obligation

Individuals from certain regions have a *right to erasure*, or the right to be forgotten or
deleted. On request, you may have an obligation to delete the personal data of an
individual.

The workflow for deleting the personal data of an end user or agent is as
follows:

1. Delete personal data from ticket comments, which is also known
   as the ticket conversation.
2. Delete the end user or agent from Zendesk Support.

The order of operations is important because user data might be required
to find the tickets containing personal data. For details
instructions, see [Forgetting a user in
Zendesk](https://support.zendesk.com/hc/en-us/articles/4408845703194).

**To delete personal data in ticket conversations**

You can use the agent interface to find personal data in ticket
conversations. See the following topics in this guide:

- [Searching for personal data in ticket conversations](#topic_qb1_frh_gdb)
- [Deleting personal data in ticket conversations](#topic_jdr_c2w_zcb)

You can also delete personal data in tickets by permanently deleting the
tickets themselves. Permanently deleting tickets also deletes
attachments, call recordings, and images in the ticket. See the
following topics in this guide:

- [Permanently deleting tickets](#topic_fhk_pgt_ycb)
- [Permanently deleting tickets with the API](#topic_dj3_qgt_ycb)

At this stage, you can ignore any personal data in ticket fields that the
system retrieves from the user profile, such as the requester's
name. The data will be replaced with the placeholder string
"Permanently Deleted User" when you delete the user in the next step
of the workflow.

**To delete the end user or agent**

After deleting personal data from ticket conversations, you can delete
the end user or agent from Zendesk Support. See the following topics
in this guide:

- [Deleting end users or agents](#topic_ktc_drs_ycb)
- [Permanently deleting an end user or agent](#topic_zhf_qwq_1db)
- [Deleting end users or agents with the API](#topic_pdg_nbs_ycb)

### Searching for personal data in ticket conversations

Before you start, create a list of possible search terms to find
the user's personal data in tickets. Go through your list of
search terms to find personal data in ticket conversations.
Inline images, attachments, and call recordings may contain
personal data that isn't searchable. Make sure to manually
check any image, attachment, and call recording in the
tickets in your search results.

With the [Advanced Data Privacy
and Protection add-on](https://support.zendesk.com/hc/en-us/articles/6561144266906), you can use [redaction
suggestions](https://support.zendesk.com/hc/en-us/articles/6669399593882) to automatically highlight
certain types of personally identifiable information (PII)
within a ticket for agents with appropriate permissions.
Redaction suggestions proactively identify PII rather than
rely on the agent to identify PII that needs to be
redacted.

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
     call recording. See [Deleting call
     recordings](https://support.zendesk.com/hc/en-us/articles/4408821829402#topic_lbr_pfj_1db) in *Complying with Privacy and
     Data Protection in Zendesk Talk*.

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
tickets in the agent interface in Zendesk Support. Deleted
tickets are moved into a Deleted Tickets view, where you
then permanently delete them.

Agents must have [permission to delete
tickets](https://support.zendesk.com/hc/en-us/articles/4408832689818).

For reporting purposes, several anonymous attributes of a
permanently deleted ticket are stored as a record. See [Effects of
permanently deleting a ticket](https://support.zendesk.com/hc/en-us/articles/4408845703194#topic_fv5_w51_sdb) in [Forgetting a user in
Zendesk](https://support.zendesk.com/hc/en-us/articles/4408845703194).

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

1. If you want to delete one ticket, open the ticket you
   want to delete in the agent interface, click the
   Ticket options menu in the upper right, then select
   **Delete**.

   The Ticket options menu looks
   slightly different in the [Zendesk Agent
   Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) (shown on the left) and the
   standard agent interface (shown on the
   right).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_options_delete.png)
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket-options-menu.png)
2. If you want to delete more than one ticket, open one of
   your views, select the tickets you want to delete,
   then select **Delete** from the toolbar at the
   bottom of the list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tickets_bulk_menu.png)

   Tip: You can create a view consisting only
   of tickets you want to delete. See [Adding
   views](https://support.zendesk.com/hc/en-us/articles/4408888828570-Using-views-to-manage-ticket-workflow#topic_vcr_xfp_ec).
3. When prompted, click **OK** to confirm the
   deletion.

   The tickets are deleted and moved to
   the Deleted tickets view. The next step is to
   permanently delete them.
4. Click the **Views** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_icon.png)) in the sidebar, then
   click **Deleted tickets** in the Views list.
5. Click the checkbox beside the ticket or tickets you want
   to permanently delete.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/tickets_delete_restore.png)

   A
   toolbar appears at the bottom of the
   list.
6. Click **Delete permanently**.
7. Confirm that you want to permanently delete the selected
   tickets.

### Permanently deleting tickets with the API

You can use the [Tickets API](https://developer.zendesk.com/rest_api/docs/support/tickets) to
delete tickets that contain personal data. Your application
logic can start by using the [Search](https://developer.zendesk.com/rest_api/docs/support/search) API to
find the tickets with the personal data, then use one of the
following endpoints to delete the ticket or tickets.

**To delete a single ticket permanently**

- `DELETE
  /api/v2/deleted_tickets/{id}.json`

See [Delete Ticket
Permanently](https://developer.zendesk.com/rest_api/docs/support/tickets#delete-ticket-permanently) in the developer
documentation.

**To delete multiple tickets permanently**

- `DELETE
  /api/v2/deleted_tickets/destroy_many?ids={ids}`

The endpoint accepts a comma-separated list of up to 100 ticket
ids.

See [Delete Multiple
Tickets Permanently](https://developer.zendesk.com/rest_api/docs/support/tickets#delete-multiple-tickets-permanently).

**To get ticket ids for the delete endpoints**

Use any of the following endpoints:

- [Search](https://developer.zendesk.com/rest_api/docs/support/search)
- [List
  Tickets](https://developer.zendesk.com/rest_api/docs/support/tickets#list-tickets)

You can also get a ticket's id from several places the ticket
page in Zendesk Support:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_id_in_ticket_page.png)

### Deleting end users or agents

After deleting personal data from ticket conversations, you can
proceed to delete the end user or agent from Zendesk
Support. Deleting the user in Support also deletes the user
in Guide, Chat (for agents), Message, Talk, and Explore. The
user is also deleted from all product reports. For details,
see [Forgetting a user in
Zendesk](https://support.zendesk.com/hc/en-us/articles/4408845703194).

Both agents and administrators can delete end users or agents in
the agent interface in Zendesk Support. Agents can delete
end users while administrators can delete all users except
the account owner. Zendesk retains information about the
account owner to continue providing its services. When the
account is terminated, Zendesk follows its [Data Deletion
Policy](https://www.zendesk.com/company/policies-procedures/data-deletion-policy/) to purge remaining profile data.

You can't delete an end user or agent who's a requester on a
ticket that hasn't been *closed* yet. See [What is the
difference between a Solved ticket and a Closed
ticket?](https://support.zendesk.com/hc/en-us/articles/4408887712154) First, the ticket must be solved
before it can be closed. Second, the solved ticket must be
closed by a trigger or an automation. The ticket can't be
closed directly in the agent interface. To close the ticket
immediately, you can create a trigger for the specific
purpose of closing the ticket. For details, see the tech
note [How can I manually
close a ticket?](https://support.zendesk.com/hc/en-us/articles/4408827596570-How-can-I-manually-close-a-ticket-)

**To delete an end user or agent**

1. In the agent interface, click the **Search** icon
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_icon.png)) in the upper-right of
   the top toolbar and search for the user's name or
   other identifying information.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_search_box.png)
2. On the results page, switch to the **Users** tab and
   select the user to open their profile page.
3. Make sure the user is in fact the person requesting to
   be deleted.
4. In the user's profile, click the User options arrow in
   the upper right, then select **Delete**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/user-options-top-right.png)
5. When prompted, click **OK** to confirm the deletion.
   If you want to cancel the deletion, click
   **Cancel** instead.

The user is soft deleted, meaning the user is still in the Zendesk
database for 30 days and accessible on a limited basis to
Zendesk employees with certain database privileges. Zendesk
permanently deletes soft-deleted users after 30 days
automatically. If you'd like to permanently delete the user
before the 30-day timeframe, continue to [Permanently
deleting an end user or agent](#topic_zhf_qwq_1db).

### Permanently deleting an end user or agent

**To permanently delete a user**

1. Soft delete a user as described in [Deleting end users or agents](#topic_ktc_drs_ycb).
2. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Deleted users > Deleted users**.
3. Click the user you want to delete permanently from the
   list. A page appears with the user's name and their
   associated tickets.
4. Click **Delete User**.

### Deleting end users or agents with the API

You can use the [Users API](https://developer.zendesk.com/rest_api/docs/support/users) to
delete an end user or agent from your account. You can also
use the [User Identities
API](https://developer.zendesk.com/rest_api/docs/support/user_identities#user-identities) to delete the *identities* of an end
user or agent. An identity is something that can be used to
identify an individual. It's usually an email address, a
phone number, or an X (formerly Twitter) handle.

A user must be soft deleted before you can permanently delete
them.

The following endpoints take one or more user ids as parameters.
See [Getting the id of an end user or agent](#topic_dn5_jlp_zcb) in [Accessing or
updating personal data with the API](#topic_bdz_dm4_zcb).

**To soft delete a single end user or agent before permanently
deleting them**

- `DELETE
  /api/v2/users/{user_id}.json`

See [Delete User](https://developer.zendesk.com/rest_api/docs/support/users#delete-user) in
the developer documentation. You can permanently delete the
user after soft deleting them.

**To soft delete multiple end users or agents before permanently
deleting them**

- `DELETE
  /api/v2/users/destroy_many.json?ids={user_ids}`

The endpoint accepts a comma-separated list of up to 100 user
ids. See [Bulk Deleting
Users](https://developer.zendesk.com/rest_api/docs/support/users#bulk-deleting-users). You can permanently delete the users
after soft deleting them.

**To permanently delete an end user or agent**

- `DELETE
  /api/v2/deleted_users/{user_id}.json`

See [Permanently Delete
User](https://developer.zendesk.com/rest_api/docs/support/users#permanently-delete-user). The user must be soft-deleted before
running this endpoint.

**To delete one of the user's identities**

- `DELETE
  /api/v2/users/{user_id}/identities/{identity_id}.json`

See [Delete
Identity](https://developer.zendesk.com/rest_api/docs/support/user_identities#delete-identity). Use the [List
Identities](https://developer.zendesk.com/rest_api/docs/support/user_identities#show-identity) endpoint to get the id of the
identity you want to update.

## Meeting a data portability obligation

Individuals from certain regions have a *right to data portability*. On request, you may
have an obligation to provide an individual with their personal data or to transmit
the data to another organization.

The following topics describe how to export user data:

- [Exporting user data](#topic_n5j_d4p_zcb)
- [Exporting user data with the API](#topic_n5f_f4p_zcb)

### Exporting user data

You can use the agent interface in Zendesk Support to export user
data to a JSON file. The file lists all your users
(end-users, agents, and administrators). The exported data
doesn't include all the users' possible personal data in
Zendesk.

You must be an administrator on a Zendesk Suite Growth plan or
above or a Support Professional or Enterprise plan to export
this data.

To protect the data in your Zendesk Support account, data export
is not enabled by default in the account. You must contact
[Zendesk Customer
Support](https://support.zendesk.com/hc/en-us/articles/4408843597850) to activate it. Be sure to include
your Zendesk Support subdomain name.

**To export user data to a downloadable file** 

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Tools > Reports**.
2. If necessary, click the **Export** tab to
   display the data export options. Some legacy
   versions of Zendesk show the export options on a
   separate tab.
3. Under **Full JSON Export**, set a date range
   and select "users" as Type.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/export_users_json.png)
4. Click **Export**.

   A build starts, and
   you're notified by email when it's
   complete.
5. Click the link in your email notification to
   download a zip file containing the report.

   The
   download link is valid for at least three
   days.
6. Filter the JSON results for the person or
   persons requesting their data.

See [Exporting account
data](https://support.zendesk.com/hc/en-us/articles/4408886165402#topic_lz3_mb5_hl) for more information on exporting data
from your Zendesk account.

### Exporting user data with the API

You can use the [Users API](https://developer.zendesk.com/rest_api/docs/support/users) to
export JSON data that can be transformed or imported into
other systems. The JSON objects in responses have the
attributes described in [JSON Format for Agent
or Admin Requests](https://developer.zendesk.com/rest_api/docs/support/users#json-format-for-agent-or-admin-requests).

End users and agents can also use the Users API to export some of
their own data. When an end user makes the API request, the
user record has the subset of attributes described in [JSON Format for
End-user Requests](https://developer.zendesk.com/rest_api/docs/support/users#json-format-for-end-user-requests).

Zendesk also has a [User Identities
API](https://developer.zendesk.com/rest_api/docs/support/user_identities#user-identities) for accessing the *identities* of
end users and agents. An identity is something that can be
used to identify an individual. It's typically an email
address, a phone number, or an X (formerly Twitter) handle. See the [JSON format](https://developer.zendesk.com/rest_api/docs/support/user_identities#json-format)
table in the User Identities doc for the attributes of the
JSON objects in responses.

Most of the following endpoints take one or more user ids as
parameters. See [Getting the id of an end user or agent](#topic_dn5_jlp_zcb) in [Accessing or updating personal data
with the API](#topic_bdz_dm4_zcb).

Your application logic can start by using the [Search Users](https://developer.zendesk.com/rest_api/docs/support/users#search-users)
API to get the id of one or more end users or agents, then
use the Users API to export their data.

**To export the user data of a specific end user or
agent**

- `GET /api/v2/users/{user_id}.json`
- `GET
  /api/v2/users/{user_id}/identities.json`

See [Show User](https://developer.zendesk.com/rest_api/docs/support/users#show-user) and
[List
Identities](https://developer.zendesk.com/rest_api/docs/support/user_identities#show-identity) in the developer
documentation.

**To export the user data of multiple end users or
agents**

- `GET
  /api/v2/users/show_many.json?ids={user_ids}`

The endpoint accepts a comma-separated list of up to 100 user
ids.

See [Show Many
Users](https://developer.zendesk.com/rest_api/docs/support/users#show-many-users).

**To let the end user or agent export their own personal
data**

- `GET /api/v2/users/me.json`

The end user or agent must authenticate the request with their
Zendesk email address and password. See [Show the Currently
Authenticated User](https://developer.zendesk.com/rest_api/docs/support/users#show-the-currently-authenticated-user).

## Meeting the objection obligation

Individuals from certain regions have a *right of objection*, or the right to object to
direct marketing. You may have an obligation to stop processing personal data for
direct marketing purposes when you receive an objection from an individual.

If you get an objection from an individual about the notifications sent
by Zendesk, you can stop all notifications by suspending the user in
Zendesk Support. A suspended user is no longer able to sign in and
any new support requests you receive from the user are sent to the
suspended tickets queue.

**To suspend a user**

1. Click the **Search** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_icon.png)) in the top toolbar.
2. Enter the name of the user you want to suspend in the search box and click the user's name when it appears.

   Alternatively, you can open a user's profile from one of their tickets.
3. Click the Ticket options menu in the upper right, then select **Suspend**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/user-options-suspend2.png)
4. Enter a reason for the suspension, then click **Suspend user** to confirm the
   suspension.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/user-options-suspend-reason.png)

For more information, see [Suspending a user](https://support.zendesk.com/hc/en-us/articles/4408889293978) in
the Support Help Center.

## Disclaimer

This document is for informational purposes only and does not constitute legal advice. Readers should always seek legal advice before taking any action with respect to the matters discussed herein.
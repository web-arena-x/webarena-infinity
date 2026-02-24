# Using CCs and followers

Source: https://support.zendesk.com/hc/en-us/articles/4408822451482-Using-CCs-and-followers

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

This article describes an updated CCs and followers experience. If
your account was created before May 2019, [your admin might need to migrate](https://support.zendesk.com/hc/en-us/articles/4408839371418) to this updated
experience.

You can add CCs and followers to tickets. You might do this if you want
someone else to be aware of a ticket or provide some feedback on it.

Depending on your plan and how your admin has configured your account, you can also CC and
BCC users in email side conversations.

This article includes these sections:

- [About CCs and followers](#id_czc_pfg_svb)
- [Adding CCs from the ticket interface and
  ticket notifications](#topic_h5l_1yb_chb)
- [Adding CCs and BCCs in email side
  conversations](#topic_q5k_wz1_mvb)
- [Adding agents as followers from the ticket
  interface](#topic_wm2_zgq_qgb)

Related articles:

- [Understanding CCs and followers](https://support.zendesk.com/hc/en-us/articles/5179445630234)
- [CCs and followers resources](https://support.zendesk.com/hc/en-us/articles/4408836035866)

## About CCs and followers

- *CCs* allow you to include end users and agents on ticket
  notifications. Internal and external users can add CCs (copied users) to
  tickets. Agents who are added as CCs will have their email addresses visible
  to all end users in the thread (agents are not copied separately). CCs can
  respond to ticket notifications publicly, or they can remove the requester
  from the notification to submit a private response. A ticket can have up to
  48 email CCs.
- *Followers* allow you to include additional internal users (agents or
  administrators) on ticket notifications. Internal users can add followers to
  tickets. Followers receive updates on the ticket without exposing their
  identity to end users. There's no limit to the number of followers you can
  include on a ticket.

It's important to understand what happens when different users (your end users,
agents, CCs, and followers) reply from email. See the following related articles
for more information:

- [Understanding when email replies become
  public or private comments](https://support.zendesk.com/hc/en-us/articles/4408842992538)
- [Best practices for using email clients
  with CCs and followers](https://support.zendesk.com/hc/en-us/articles/4408824667930)
- [Understanding suppression of CCs email
  notifications](https://support.zendesk.com/hc/en-us/articles/4408843347866)
- [Using the Notify by > User email |
  (requesters) action in ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408893545882#topic_ncz_4kz_1cb__d37e20)

## Adding CCs from the ticket interface and ticket notifications

You can copy users by adding them to the ticket from a public reply in the ticket interface
or from the ticket notification. To learn more about using CCs, see [About copying internal and external users on
tickets](https://support.zendesk.com/hc/en-us/articles/5179445630234#topic_nw3_try_rvb).

Note: A ticket can have up to 48 email CCs. If you have an email notification that includes a
large number of users (for example, over 25), Zendesk may create multiple emails, split into
different batches of users, to send the notification.

**To CC a user from the ticket interface**

1. From Support, open the ticket in the agent interface.
2. In the comment stream, click **Public reply**.
3. Click **CC** on the right side of the comment header.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ccs_click_cc.png)

   If there are already other users copied on the
   ticket, you can click on the CC line to add additional CCs.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ccs_add_to_cc_line.png)
4. Begin entering the name or email address of the user you want to copy. Registered users’
   names will appear as suggestions.
5. If you see the user you want to include, click their name; otherwise, click **Add
   user** and enter the user’s email address.

   When the header is expanded to show CCs,
   a warning icon ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_ticket_missing_address_icon.png) appears next to any
   users without email addresses.
6. Repeat as necessary.
7. Enter and submit your public comment (public reply). Copied users receive a notification
   and are included in subsequent replies until they are removed from the CC line.

**To CC a user from ticket notifications**

1. From your email client, open the ticket notification.
2. Open the CC line, per your email provider’s instructions.
3. Add the name of the user you want to copy. Repeat as necessary.
4. Add your comment and send the email. Copied users will receive an email notification,
   and will be included in subsequent replies, until they are removed from the CC line.

## Adding CCs and BCCs in email side conversations

Note: You must be on a Suite Professional plan or above to use side conversations. Side
conversations are not available on Support only plans. See [About side conversations](https://support.zendesk.com/hc/en-us/articles/4408844206746).

You can CC and BCC both agents and end users in an email side conversation. Side
conversation CCs and BCCs differ from CCs on a ticket in some ways. For example, you can use
trigger conditions and actions to check for and/or add CCs to a ticket but can’t for side
conversations.

**To add CCs or BCCs to existing email side conversations**

1. In a ticket, click **Side Conversations** in the upper-left and select an existing
   email side conversation.

   For more information about using side conversations, see [Creating side conversations](https://support.zendesk.com/hc/en-us/articles/4604286879642#topic_dj2_jj4_l2b)
2. Click **Write a reply**.
3. Click **CC** on the right side of the comment header.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_convo_existing_cc.png)

   The CC recipient field and the option to BCC users
   appears.

   Note: Adding a user as a CC or BCC on a side conversation doesn’t add them
   as a CC on the ticket.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/side_convo_existing_bcc.png)
4. If you want to BCC a user instead of or in addition to copying a user, click
   **BCC**.

   BCC recipients aren't visible to other recipients on the email, but are
   visible to anyone who can view the side conversation within Support. See [About BCCs in email side
   conversations](#topic_glr_z1y_rvb).
5. In the corresponding field, begin entering the name or email address of the end user or
   agent you want to CC or BCC.

   Users who already exist in your account appear as
   suggestions.
6. If you see the user you want to add, click their name; otherwise, type the email address
   of the person you want to CC or BCC.

   Users you add by email [automatically become end users](https://support.zendesk.com/hc/en-us/articles/4408829243162) in your account if they aren't
   there already.
7. Click **Send**.

### About BCCs in email side conversations

Similar to traditional email, when you add a recipient in the BCC field on an email side
conversation, the BCC’d recipient can see other recipients in the To and CC fields.
However, the BCC’d recipient won’t see that they were added to the BCC field.

When a BCC’d recipient replies to an email side conversation, their reply is threaded
into the side conversation. Other recipients won’t receive the BCC’d recipient’s
email.

If a BCC’d recipient replies via “reply all”, other visible recipients (that is,
recipients in the To and CC fields) are also included in their email. By using “reply
all”, the BCC’d recipient makes a public reply to the side conversation and is included in
all subsequent replies from the side conversation. You can remove them from the recipients
list if you don’t want them included in further replies.

## Adding agents as followers from the ticket interface

Internal users (your company's agents and admins) can add followers from the Followers
field from the properties panel in the ticket interface. Followers receive email
notifications when a ticket is updated. To learn more about using followers, see [About adding followers to tickets](https://support.zendesk.com/hc/en-us/articles/5179445630234#topic_r3l_xry_rvb).

**To add agents as followers from the ticket interface**

1. Select a ticket from one of your views.

   The **Followers** field appears in the
   ticket properties panel on the left side.
2. In the **Followers** field, enter a user's name, email domain, or organization name
   and the relevant results appear.

   Internal users such as agents, light agents, and
   administrators can be followers.

   To quickly add yourself as a follower, click
   **follow**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/followers_follow.png)

**To remove a follower from the ticket interface**

- Click the delete button (X) in the person's name box in the **Followers**
  list

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/followers_unfollow.png)

  To quickly remove yourself as a follower, click
  **unfollow**.

**To add agents as followers from ticket notifications**

1. From your email client, open the ticket notification.
2. Open the **CC** line, per your email provider’s instructions.
3. Add the name of the user you want to add as a follower. Repeat as necessary.
4. Add your comment and send the email.

   If you're an agent who is not already a
   requester or assignee on the ticket, you're also added as a follower.
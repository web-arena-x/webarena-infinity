# Configuring messaging responses and business hours

Source: https://support.zendesk.com/hc/en-us/articles/4500737327258-Configuring-messaging-responses-and-business-hours

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

The messaging response is available
on all plans. Business hours are
available on all plans except Team.

Your customers' first interaction with
your business is important. You can customize the default messaging response
that greets
your customers in the Web Widget or mobile channel. You can apply a schedule
to set
business hours for your messaging channel, if you'd like, then configure
different
responses for during business hours and outside of business hours.

If you add an AI agent to your messaging channel, the messaging response
is deactivated
and replaced by the AI agent's
[standard responses](https://support.zendesk.com/hc/en-us/articles/8774095741466).

This article contains the following sections:

- [About the messaging
  response](#topic_nxy_njd_btb)
- [Setting the messaging response and business hours schedule](#topic_kzg_ync_gnb)

## About the messaging response

The default messaging response is activated when a customer launches
the Web Widget.
The messaging response includes:

- Basic greeting for customers
- Request for information about their support needs
- Message letting the customer know they’re being connected
  to a live
  agent

Without any configuration, the default messaging response appears
to end users as
follows.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/default_messaging_response_name.png)

Behind the scenes, agents are notified that a support request has
been received, and
they can accept the request and begin responding to the conversation.

You can apply a schedule to the messaging response so that you can
set different
responses during business hours and outside of business hours. Otherwise
you can set
one message that will always be sent.

If you want to add an AI agent to your channel, you can do that at
the bottom of the
Responses section, instead of setting the messaging response. In
that case, the
messaging response is deactivated and replaced by the
[AI agent's standard responses](https://support.zendesk.com/hc/en-us/articles/8774095741466).

The default messaging response does not support automatic translation
or dynamic
content in custom ticket fields, so to use those features you should
add an AI
agent.

## Setting the messaging response and business hours schedule

The default messaging response includes a basic greeting for customers,
a request for
information about their support needs, and a message letting them
know they’re being
connected to an agent.

You can apply a
[schedule you've created](https://support.zendesk.com/hc/en-us/articles/4408842938522)
so that you can set different
responses during business hours and outside of business hours. If
you do not apply a
schedule, customers receive the same response regardless of the time
or day they
contact you in your messaging channel.

**To customize the messaging response and set a schedule**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click the name of the channel you want to edit.
3. Scroll down, then click the **Responses**
   section to open it.
4. If you want to apply a business hours schedule for your messaging
   channel,
   under **Business hours**, select
   a saved schedule.

   If you haven't
   created a schedule and would like to, click
   **Manage schedules** to
   set up a schedule now.

   Note: Schedules are
   not available on Team plans, but you can use
   [out of office triggers](https://support.zendesk.com/hc/en-us/articles/4408842866074)
   to manage basic
   responses.
5. In the **Response during business hours**
   section, update the following,
   whether you've applied a business hours schedule or not:
   - **First message**: Enter
     the text that appears when a customer
     launches the Web Widget.
   - **Customer details**: Select
     the information you want to request
     from the customer before handing them off to an agent.
     You can
     request the customer's name or email address, or
     use custom text or
     drop-down ticket fields to gather information. If
     you use custom
     ticket fields you've created, keep in mind:

     - Permissions for ticket fields must be
       set to Editable
       for end users. When a field is included
       in an Ask for
       details step, end users are required
       to submit a
       response, regardless of the requirement
       configuration on
       the permissions page.
     - Nested drop-down fields are not supported.
     - Blank selection values are not displayed
       as options in the
       dropdown.

     Customers must complete these fields. If you're
     using
     [authentication for messaging](https://support.zendesk.com/hc/en-us/articles/4411666638746),
     signed-in users aren't asked for their name or
     email
     address.
   - **Follow-up message**:
     Enter the text that appears after the
     customer submits their details.
6. If you've applied a business hours schedule, click the
   **Outside business
   hours**
   tab, then update the first message, customer details, and
   follow-up message.
7. Click **Save**.
# Creating a ticket on behalf of the requester

Source: https://support.zendesk.com/hc/en-us/articles/4408882462618-Creating-a-ticket-on-behalf-of-the-requester

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

There may be times when you need to open a ticket on someone else's behalf. For example, you
may be providing support to someone using a telephone (and not Zendesk Talk, which creates a
ticket for you when you take the call), and you want to capture the support request in a
ticket. You can create a new ticket and then set the person you're providing support to as the
ticket requester.

Also known as proactive tickets, tickets created on behalf of an end user can be public (the
end user for whom it was created can view the ticket) or private (the end user cannot view the
ticket until it's manually made public).

This article contains the following topics:

- [Creating a public ticket for an end
  user](#topic_swv_ytz_y2b)
- [Creating a private ticket for an end
  user](#topic_q5c_ztz_y2b)

## Creating a public ticket for an end user

When an agent creates a public ticket for an end user, they will need
to add the end user as the requester. If the Requester field is not completed, the agent
will be set as the requester. When the end user is added to the ticket as the requester,
they can view and update the ticket.

When you create a public ticket for an end user, it triggers the following events:

- The end user receives a notification that a ticket was created on their behalf, if you
  have a [trigger](https://support.zendesk.com/hc/en-us/articles/4408886797466) enabled for this
  action.
- The ticket appears in the end user's My Activities list.
- The ticket appears in the end user's help center searches.

In most cases, a public ticket cannot be made private. However, in some cases, it's
possible. See [Changing a ticket from public to
private](#topic_x2r_141_z2b).

**To create a ticket on an end user's behalf**

1. Hover over the **+Add** tab in the top toolbar, then select **Ticket**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add_tab_options.png)
2. If private ticket creation is enabled, click **Public Reply** so the end user can
   access the ticket immediately. If private ticket creation is not enabled, the ticket is
   accessible by default, and no action is necessary.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/new_ticket_public_reply2.png)
3. If the requester is an existing user, begin entering the user's name, email domain,
   phone number, or organization name in the **Requester** field, and the relevant results
   appear. Select a user.

   Note: Alternatively, you can open the user's profile, then click**User options** in the bottom toolbar and select **New ticket**. The user's name
   automatically appears in the **Requester** field.

   If the requester does not
   yet have an account, add them by clicking **+Add user** at the bottom of the search
   results.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/requester_add_user2.png)
4. Enter the ticket data, then click **Submit as New**.

   The requester receives the
   new ticket email notification, if you have a [trigger](https://support.zendesk.com/hc/en-us/articles/4408886797466) enabled for this
   action.

## Creating a private ticket for an end user

Agents can open a private ticket that is not visible to the end user for whom they are
creating it, and can choose when (or if) to allow the end user to access the ticket. You can
create private tickets in the ticket interface or through a create event using the [Tickets API](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/). Private tickets cannot be created
through an inbound email message.

If private tickets are not enabled in your account, you might need to have an administrator
enable this feature (see [Enabling private ticket creation](https://support.zendesk.com/hc/en-us/articles/4408842918298)).

When a private ticket is created for an end user, the end user is included as the ticket
requester; however, some notifications and other ticket-related events are not triggered.
For instance:

- The end user is not notified that a ticket has been created on their behalf.
- Private tickets do not appear in the end user's My Activities list or help center
  searches.

These events are triggered when the ticket is [made public](#topic_nj1_d5z_y2b).

Once your admin enables private ticket creation, you can create a new ticket on behalf of
an end user.

**To create a private ticket on an end user's behalf**

1. Hover over the **+Add** tab in the top toolbar, then select **Ticket**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add_tab_options.png)

   The Internal note option
   should be selected by default.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/private_ticket_new2.png)
2. If the requester is an existing user, begin entering the user's name, email domain,
   phone number, or organization name in the **Requester** field, and the relevant results
   appear. Select a user.

   Note: Alternatively, you can open the user's profile and click
   **New ticket**. The user's name automatically appears in the **Requester**
   field.

   If the requester does not yet have an account, add them by clicking
   **+Add user** at the bottom of the search results.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/requester_add_user2.png)
3. Enter the ticket data, then click **Submit as New**.

All comments default to Internal note (private) from then on, including comments added via
email, voice recordings, and the like, until you [make the
ticket public](#topic_nj1_d5z_y2b).

### Using private tickets internally

There are a number of internal uses for private tickets. You can:

- Make records of calls and meetings with your customers. These can be stored as
  tickets, meaning you get a more accurate picture of your Support team's effort, without
  bothering your customer.
- Take action on issues that you can't share. Sometimes tasks need to be carried out on
  behalf of a customer account -- investigations or corrective actions -- that might be
  sensitive. With a private ticket, it can remain internal.
- Prepare for an interaction before communications open up. Because private tickets can
  be shared just by adding a public comment, you can use the ticket to gather materials,
  prepare, or take notes, then make the ticket public when you're ready to address it with
  the end user.
- Send someone else a task. Throw together a private ticket, record some steps or
  actions that need to be taken, and assign it to someone else, or set it in a queue for
  the next available person.

You can associate a private ticket with a customer, meaning the record is there for
future reference. You get the value of reporting, whether that's accurate accounting of
what your team is doing, or the amount of work you're doing on behalf of a particular
customer or organization, without involving the end user until you're ready.

### Changing a ticket from private to public

Private tickets can be made accessible to the requester and any newly added CC'd end
users. Once a ticket is made public, it cannot be made private again. However, internal
notes remain hidden from end users, as usual.

**To change a ticket from private to public**

1. Above the comment entry box, click **Public reply**.
2. Enter your comment, then click **Submit**.

### Changing a ticket from public to private

If a public ticket has only one comment, you can make the ticket private by changing the
[Public reply to an Internal comment](https://support.zendesk.com/hc/en-us/articles/4408835109018). This works *only* on
tickets where there is a single public comment.

Note that when you change a Public reply to an Internal comment, you cannot make it
public again.
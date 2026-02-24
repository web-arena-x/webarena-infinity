# Analyzing agent ticket touches with Explore

Source: https://support.zendesk.com/hc/en-us/articles/4408834719386-Analyzing-agent-ticket-touches-with-Explore

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Explore Professional or Enterprise |

At a high-level, an *agent touch* is an operation performed by the agent on a
ticket. For example, it could mean that the agent:

- Added a public or private comment to the ticket
- Changed a ticket field, for example the ticket group
- Changed the status of the ticket, for example from Open to Solved

The method you'll use to determine agent touches will depend on your business needs. In
this article, you'll learn about how you can use Explore to analyze agent touches in a
few different ways. The examples assume you have some familiarity with creating Explore
reports. If you need some help, see [Creating reports](https://support.zendesk.com/hc/en-us/articles/4408821589530).

This article contains the following sections:

- [Analyzing ticket comments](#topic_jzq_dpn_4nb)
- [Analyzing ticket updates](#topic_xt3_fpn_4nb)
- [Analyzing tickets with low agent touches](#topic_s5l_fpn_4nb)

## Analyzing ticket comments

If you want to measure agent touches by the number of comments your agents make on
tickets, then Explore has you covered. The **Updates history** dataset contains a
built-in metric that measures this when you add it to a query. You can add
attributes to slice this number however you want, for example by ticket ID and
subject.

### Example

This simple Explore report displays a table showing your tickets and how many
agent comments they received.

**To create a report to analyze ticket comments**

1. Create a [new report](https://support.zendesk.com/hc/en-us/articles/4408821589530) using the **Support:
   Updates history** dataset.
2. In the **Metrics** panel of the report, add the **Comments** >
   **Agent comments** metric. Explore displays the total number of agent
   comments received for all of your tickets.

   Tip: The Explore **Updates history** dataset might
   contain a lot of data causing your reports to take a long time to
   return results. Consider adding a filter like **Time - Ticket
   update** > **Update - Date** to reduce and focus the
   results returned by the report. For more information, see [Filtering a report](https://support.zendesk.com/hc/en-us/articles/4408825475354).
3. To break down the number of comments by ticket, add the attributes **Ticket
   ID** and **Ticket subject** to the **Rows** panel of the
   report.

   Explore displays a table showing all of your tickets broken
   down by the number of agent comments (each comment counts as one agent
   touch).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_agent_touches_1.png)

## Analyzing ticket updates

Sometimes, you might want to report all updates made to your tickets, not just
comments. For example, other updates might include changes to ticket status,
priority, assigning the ticket to someone else, and more. Again, the **Updates
history** dataset contains a built-in metric that measures this when you add
it to a report. You can add attributes to slice this number however you want, for
example by ticket ID and subject.

### Example

In this example, you'll create a report that shows all updates to all of your
tickets. You'll then add attributes to slice this number by the date of the
update, the ticket ID, and the person who made the update.

1. Create a [new report](https://support.zendesk.com/hc/en-us/articles/4408821589530) using the **Support:
   Updates history** dataset.
2. In the **Metrics** panel of the report, add the **Updates** >
   **Updates** metric. Explore displays the total number of updates made
   for all of your tickets.

   Tip: The Explore **Updates history** dataset might
   contain a lot of data causing your reports to take a long time to
   return results. Consider adding a filter like **Time - Ticket
   update** > **Update - Date** to reduce and focus the
   results returned by the report. For more information, see [Filtering a report](https://support.zendesk.com/hc/en-us/articles/4408825475354).
3. To break down the number of updates, add the attributes **Update -
   Date**, **Ticket ID**, and **Updater name** to the **Rows** panel
   of the report.

   Explore displays a table showing all of events where at
   least one ticket update was made, broken down by date, ticket ID, and
   the name of the person who made the update.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_agent_touches_2.png)

## Analyzing tickets with low agent touches

Explore records the number of agent replies it took to solve a ticket into the
following brackets:

- **One-touch tickets:** Tickets that were solved with only one agent
  reply.
- **Two-touch tickets:** Tickets that were solved with two agent replies.
- **Multi-touch tickets:** Tickets that were solved with more than two agent
  replies.

Note: If a ticket is reopened and an agent adds a further comment, the number of touches increases.
For example, a one-touch ticket will become a two-touch ticket.

### Example

In this example, you'll create a report that shows the number of one-touch
tickets created each year by your agents.

1. Create a [new report](https://support.zendesk.com/hc/en-us/articles/4408821589530) using the **Support:
   Tickets** dataset.
2. In the **Metrics** panel of the report, add the **Agent replies
   distribution** > **One-touch tickets** metric. Explore displays
   the total number of one-touch tickets in your account.
3. To break down the number of one-touch tickets by year, add the attribute
   **Ticket solved - Year** to the **Rows** panel of the
   report.

   Explore displays a table showing the number of one-touch
   tickets in your account each year.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Explore_agent_touches_3.png)
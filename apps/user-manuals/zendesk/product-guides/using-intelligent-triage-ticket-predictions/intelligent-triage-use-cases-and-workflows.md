# Intelligent triage use cases and workflows

Source: https://support.zendesk.com/hc/en-us/articles/5222280338202-Intelligent-triage-use-cases-and-workflows

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Copilot |

Intelligent triage is an AI-powered feature that automatically detects what a ticket is
about (its intent), what language it's written in, and whether the customer's message is
positive or negative (its sentiment). You can use this information to route tickets to
the right groups automatically, create views to group similar types of requests, and
report on trends in the types of tickets your customers are submitting.

This article describes example use cases to help you better understand how intelligent
triage can streamline your workflows and support your business. Specifically, you'll
learn how to use intelligent triage to automatically deflect tickets, route tickets to
the right groups, reduce resolution time and touches, and forward information to
external parties.

As you read through the use cases provided here, remember that you can always modify or
expand on them to better support your specific workflows.

For more information about intelligent triage, see [Intelligent triage resources](https://support.zendesk.com/hc/en-us/articles/4471123173402).

This article contains the following topics:

- [Deflect: Redirect customers to self-serve or correct destination](#topic_ojz_rdx_tvb)
- [Route: Send tickets to a specific language queue from a general queue](#topic_r4m_tdx_tvb)
- [Reduce: Proactively request more information](#topic_fjq_5dx_tvb)
- [Forward: Use webhooks to pass information to external resources](#topic_rcb_wdx_tvb)

Related articles:

- [Automatically detecting customer intent,
  language, and sentiment](https://support.zendesk.com/hc/en-us/articles/4550640560538)
- [Analyzing intelligent triage results and taking
  action](https://support.zendesk.com/hc/en-us/articles/5201262314266)
- [Using intelligent triage to identify and act on
  ticket escalations](https://support.zendesk.com/hc/en-us/articles/6353620565530)

Note: When creating triggers, views, or reports in Admin Center or
Explore, intelligent triage prediction values are available only in English.
However, intelligent triage is capable of evaluating content in the languages listed
[here](https://support.zendesk.com/hc/en-us/articles/4408821324826#h_01GYJ1PBVKD26QN3E8JNS3X3TX).

## Deflect: Redirect customers to self-serve or correct destination

**Scenario**: An end user is contacting you about a process where submitting a
ticket or contacting support is not the best course of action. Instead, the required
information is provided on your website or some other source, meaning the user can
self-serve by following a process or other documentation that’s readily
available.

**Examples**:

- Subscription cancellations
- User profile update requests
- Refund, return policy, and warranty questions
- Job applications

**How to use intelligent triage to address the scenario**:

1. Identify any intents that are frequently applied to the tickets submitted in the
   scenario described above (for example, "Cancel subscription"). If helpful, you
   can group multiple related intents together (like "Refund request" and "Refund
   via specific channel").
2. Determine the necessary confidence level that the intent must have for you to be
   comfortable taking automatic action on it. In other words, are false positives
   acceptable, where the end user can reply if they still need help?
3. [Create a trigger](https://support.zendesk.com/hc/en-us/articles/4766535251610#topic_k43_4hs_25b) that sends an
   automated reply to the end user. Include instructions on how they can complete
   the task, a link to where they need to go in their account or app to complete
   the task, or a link to an existing document that answers their question.
4. Leave the conversation open-ended in case the intent was accidentally
   mismatched, but set the ticket to a Solved status.

## Route: Send tickets to a specific language queue from a general queue

**Scenario**: All or most end users submit tickets to a common queue, with tickets
from different languages ending up in the same queue.

**Examples**:

- All end users use the same contact form or email address, regardless of language
- End users use the source platform in one language, but their preferred language
  is different from the current language of the platform or browser

**How to use intelligent triage to address the scenario**:

- **Option 1**: [Create a trigger](https://support.zendesk.com/hc/en-us/articles/4766535251610#topic_pxc_rhs_25b) (leaving out any
  intent conditions) that routes tickets to the appropriate agents or group based
  on language (and potentially language confidence, if necessary).

- **Option 2**: Use other integrations to reference the ticket’s language value
  and take an action based on that value. For example, if you currently [translate macros using dynamic
  content](https://support.zendesk.com/hc/en-us/articles/4776777747866), you could instead [use Liquid markup](https://support.zendesk.com/hc/en-us/articles/4408883291290) to determine which
  language the macro should use based on the [intelligent triage Language field](https://support.zendesk.com/hc/en-us/articles/4550640560538#topic_ebn_l4g_htb).
  This approach is useful if the requester's language isn't already set in their
  profile (for example, if they're contacting support from an unregistered email,
  or in a different language than the one they have set in their profile).

## Reduce: Proactively request more information

**Scenario**: Customers contact support, but don’t include the details required to
resolve the request. Agents have to reply asking for the necessary information
rather than being able to solve the request during the first touch.

**Examples**:

- Return/replacement requests where the customer needs to provide an address
- Processes where the customer must include a purchase order or invoice number

**How to use intelligent triage to address the scenario**:

1. Identify any intents that are frequently applied to the tickets submitted in the
   scenario described above (for example, "Return order"). If helpful, you can
   group multiple related intents together.
2. Determine the necessary confidence level that the intent must have for you to be
   comfortable taking automatic action on it.
3. [Create a trigger](https://support.zendesk.com/hc/en-us/articles/4766535251610#topic_k43_4hs_25b) that sends an
   automated reply to the end user, prompting them for the required details if they
   haven't already included them. This gives the customer the opportunity to reply
   before the agent sees the ticket, and makes it more likely that the agent can
   solve the ticket in a single touch.

Watch the video below for an example of how to set up intelligent triage to address
this scenario.

Intelligent triage: How to proactively request more information from your users in
tickets (3:10)

## Forward: Use webhooks to pass information to external resources

**Scenario**: Customers contact support for a request that requires involvement
from an external team or system. Agents must manually forward these requests to the
appropriate destinations.

**Examples**:

- End users reach out to customer support to change their email address or other
  contact details, but that’s owned by a team outside of Zendesk
- Certain requests require compliance or other processes to be followed outside of
  Zendesk

**How to use intelligent triage to address the scenario**:

1. Identify any intents that are frequently applied to the tickets submitted in the
   scenario described above (for example, "Change email address"). If helpful, you
   can group multiple related intents together.
2. Determine the necessary confidence level that the intent must have for you to be
   comfortable taking automatic action on it.
3. [Create a trigger](https://support.zendesk.com/hc/en-us/articles/4766535251610#topic_k43_4hs_25b) that sends an
   automated reply that does both of the following:
   1. Informs the requester that their ticket has been received.
   2. [Uses a webhook](https://support.zendesk.com/hc/en-us/articles/4408839108378), [email target](https://support.zendesk.com/hc/en-us/articles/4408883282458), or other means
      from within the product to forward the relevant details from the
      customer’s request to the appropriate external team. For example, you
      might send an email to an external team that includes the requester’s
      name, email address, subject, and original message. The external team
      can then process the customer’s request in their system.
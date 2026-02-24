# Available CRM actions for AI agents - Advanced and Zendesk Support

Source: https://support.zendesk.com/hc/en-us/articles/8357750876826-Available-CRM-actions-for-AI-agents-Advanced-and-Zendesk-Support

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

CRM actions allow communication between advanced AI agents and your CRM platform.

This article covers the following supported CRM actions for Zendesk Support:

- [Add tag](#topic_tvk_cp1_z2c)
- [Add internal note](#topic_pgf_cp1_z2c)
- [Get user info](#topic_apk_bp1_z2c)
- [Get ticket info](#topic_tfx_cp1_z2c)
- [Update ticket info](#topic_q5d_dp1_z2c)
- [Get ticket tags](#topic_etm_dp1_z2c)
- [Merge tickets](#topic_lxy_dp1_z2c)
- [Get organization info](#topic_u23_35k_1fc)
- [Add macros](#topic_mvl_j5k_1fc)

Related article:

- [Creating and adding actions for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756623770)

## Add tag

Adds a tag to tickets for easier management.

The following example shows how to set the Add tag action at the AI agent level. In this case, the tag bot\_reviewed set at the AI agent level applies to all tickets coming through the AI agent. If this is set at the intent level, it applies only to tickets that have triggered that intent, as opposed to all tickets.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_5755241363346.png)

The following example shows how to set the Add tag action at the content level. In this case, the tag payment\_terms\_change is added to all the messages that triggered the intent Changes to payment terms.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_4402231559698.png)

You can automatically update ticket forms by combining the Add tag action in the AI agents - Advanced dashboard and a trigger. Let's consider an example where all tickets for login issues are tagged and the ticket forms are updated.

**To tag tickets for login issues and update the ticket forms**

1. In the AI agents - Advanced dashboard, set up an Add tag action at the intent level to add a login\_problem tag.

   Make sure this action comes before all other actions

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_11184727794706.png)
2. [Create the trigger](https://support.zendesk.com/hc/en-us/articles/4408886797466#topic_qfk_s23_vsb).

   - Name the trigger to match the intent.
   - Add a condition for tickets with the "login\_problem" tag.
   - Add an action to select the form you want to update.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_11184727830930.png)

## Add internal note

Adds an internal note to keep your agents in sync. Internal notes are not visible to customers.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_5755243296274.png)

## Get user info

Retrieves customer information in Zendesk. You can use this information to personalize your messages or to create reply variations. This action works with the [Ticket Received event](https://support.zendesk.com/hc/en-us/articles/8357749555610#h_01JFDKCPKWX8GNW8HG99GMEB39) only.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_7244636580754.png)

The following user information can be retrieved:

- id
- email
- name
- created\_at
- locale
- locale\_id
- organization\_id
- phone
- shared\_phone\_number
- photo
- role
- time\_zone
- updated\_at
- url
- verified
- custom fields

In the Parameter field, enter the selected field name as is, but with the first letter capitalized. In addition, add the word "customer" as a prefix and without spaces in between. For example:

```
email --> customerEmail; locale_id --> customerLocale_id.
```

If you want to use the same value in your replies for personalization, put it in double curly brackets. For example, `{{customerEmail}}` .

## Get ticket info

Retrieves ticket information based on ticket fields. To retrieve a system field, use the field name as key. To retrieve a custom field, add `custom_fields` as the prefix followed by the custom field id.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_7244751365266.png)

## Update ticket info

Updates ticket fields to streamline your processes. The following fields can be updated:

- Assignee ID
- Assignee email
- Group ID
- Type
  - problem
  - incident
  - question
  - task
- Priority
  - urgent
  - high
  - normal
  - low
- Status
  - new
  - open
  - pending
  - hold
  - solved
  - closed

    Note: When using the Update ticket Info action to change the status to solved or closed, all required fields must be completed.

Both system ticket fields and custom ticket fields can be selected in the dashboard directly once your [AI agent is authorized](https://support.zendesk.com/hc/en-us/articles/8357750866970).

For more information about working with this action, see [Workflow: Updating ticket field values using a CRM action in an advanced email AI agent](https://support.zendesk.com/hc/en-us/articles/9984120855322).

## Get ticket tags

Gets the tags associated with the ticket and saves the tags in the session as a string, where each tag is separated by a comma. The action is available on the AI agent level for the event Ticket Received by Ultimate. It can also be configured on the intent, reply, and block level.

In the following example, the action gets the tags in the ticket and saves it under the session parameter myTags, where the value is `vip,premium`. All the tags fetched are saved under a string, where each tag is separated by a comma.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_7406919111954.png)

## Merge tickets

Merges tickets that are from the same customer (that is, the same requester) in a short period of time to ensure your agents are aware of all the messages coming from that customer.

The action allows your AI agent to:

1. Find tickets from the same customer email.
2. Check the tags on the tickets and finds common tags.
3. Merge the tickets "based on certain Zendesk tags" and "Zendesk tags to ignore" conditions set in the AI agents - Advanced dashboard into the oldest ticket found.

Mandatory fields are:

- Status
  - New
  - Open
  - Pending
  - On-hold
  - Solved
- Number of days back (1 day is 24 hours)
- Requester (customerEmail)
- Tags

You can further customize this by specifying which [existing ticket tags](https://support.zendesk.com/hc/en-us/articles/4408846535834#topic_hrf_1xn_bfb) should be included or excluded when performing this action.

In the following example, consider you want to merge the newly created ticket with tickets that have the same email and are still open in the past 48 hours. Note that the value customerEmail under Requester is captured through the Get Customer Info action.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_4406610015250.png)

### Example: Merge tickets based on ticket tags

In this example, you want to merge tickets that have the tag refund using the Merge tickets action. There are four tickets from the same customer, and each ticket has its own tags:

- Ticket 1: refund, EN, bot\_reviewed
- Ticket 2: package\_location, EN, bot\_reviewed
- Ticket 3: refund, FR, bot\_reviewed
- Ticket 4: refund, FR

The AI agent looks at the tickets that have the tag refund (Ticket 1, 3 and 4), and merges Ticket 3 and 4 to the oldest ticket (Ticket 1). In this example, Ticket 2 remains untouched.

### Example: Merge tickets based on ticket tags to ignore

In this example there are ticket tags to ignore. Keep in mind that after finding all the tickets from the same customer email, the AI agent looks for common tags and merges those tickets into the oldest ticket.

Consider the same four tickets from our previous example:

- Ticket 1: refund, EN, bot\_reviewed
- Ticket 2: package\_location, EN, bot\_reviewed
- Ticket 3: refund, FR, bot\_reviewed
- Ticket 4: refund, FR

The action looks for the common tags and counts the number of tickets with each tags:

- refund is on three tickets
- bot\_reviewed is on three tickets
- EN is on two tickets
- FR is on two tickets
- package\_location is on one tickets

Next, the action looks at the "based on certain Zendesk tags" and "Zendesk tags to ignore" conditions and determines these tags should be excluded:

- EN
- FR
- bot\_reviewed

That leaves the following tags:

- refund is on three tickets
- package\_location is on one tickets

From these two tags, the AI agent chooses the tag with the most tickets, which is the refund tag on three tickets. The AI agent next checks which of the three tickets with the tag refund is the oldest ticket. In this case Ticket 1 is the oldest, so Tickets 3 and 4 are merged into Ticket 1. Ticket 2 remains untouched.

## Get organization info

Retrieves system and custom fields of the user’s organization. This action is useful if you want to tailor the answers users receive based on their organization. A user can belong to multiple organizations, so the advanced AI agent retrieves information for the first organization it finds for the user. For example:

- **User belongs to only one org**: If **user X** belongs to **Org A** only, the AI agent gets the info from **Organization A**.
- **User belongs to multiple orgs**: If **user X** belongs to **Organization B and Organization A**, and Organization B is on top of the list, the AI agent gets the info from **Organization B**.

The action can be created on the AI agent, intent, reply, and block level. On the AI agent level, the action is available only on the event Ticket is received by Ultimate.

You can choose from a list of fields to fetch. The custom fields available to get are labeled as custom field. You can add more fields as needed.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_7244338357394.png)

## Add macros

Adds any active macro. You can choose to run these macros at the time a ticket is received by the advanced AI agent or once it has been processed. As with other actions, these can also be triggered within the dialogue builder within an intent.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_13516390263442.png)
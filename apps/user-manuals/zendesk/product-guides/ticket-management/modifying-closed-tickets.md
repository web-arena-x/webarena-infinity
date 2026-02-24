# Modifying closed tickets

Source: https://support.zendesk.com/hc/en-us/articles/7335734335258-Modifying-closed-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

In the final stage of a ticket’s life cycle, it automatically [enters the closed state based on automations](https://support.zendesk.com/hc/en-us/articles/8263915942938#topic_zxw_4yk_fdc) an admin
defines. This means that the ticket’s status changes to Closed or, if custom ticket statuses
have been activated in your account, it [retains its last Solved status](https://support.zendesk.com/hc/en-us/articles/8263915942938#topic_zlx_pyk_fdc). When a ticket enters
the closed state, most fields can no longer be edited and the ticket can’t be reopened.

You can modify closed tickets by editing ticket [tags](../business-rules/about-tags.md), subject, and priority [fields](https://support.zendesk.com/hc/en-us/articles/4408886739098) as well as a subset of custom fields. Modifying closed
tickets gives you more flexibility to correct mistakes, add context to historical tickets, and
ensure that your reports and data audits are accurate.

This article contains the following sections:

- [Understanding how closed tickets can be
  modified](#topic_nts_whq_4bc)
- [Activating the modify closed tickets
  setting](#topic_otn_2s3_qbc)
- [Modifying closed tickets](#topic_fnq_h3q_4bc)

Related articles:

- [Updating and solving tickets](../../agent-guide/ticket-basics/updating-and-solving-tickets.md)
- [About the ticket lifecycle and ticket statuses](https://support.zendesk.com/hc/en-us/articles/8263915942938)

## Understanding how closed tickets can be modified

Admins can modify closed tickets by adding or removing ticket tags and editing
the subject and priority ticket fields.

Some examples of how you might want to modify closed tickets include:

- An agent accidentally tags a ticket as coming from a VIP customer and the
  mistake is caught months later when auditing reports. An admin removes the tag from the
  closed ticket so that ticket analytics are reported correctly.
- Your organization uses the ticket tag “tier\_1”; however, the meaning of this
  tag has since changed. An admin removes the ticket tag from closed tickets where it no
  longer applies.
- An admin needs to identify closed tickets so that they’re included in a [ticket deletion schedule](https://support.zendesk.com/hc/en-us/articles/6388012977306). They add the tag
  “delete” to the closed tickets that should be included in the deletion schedule.
- Some tickets are received from your help center request form without a subject so the
  subject is filled in with the tickets’ initial text. An admin edits the subject of these
  closed tickets so that it reflects the ticket’s resolution.
- Incoming tickets from your messaging channel are automatically set as “urgent”
  priority. Agents solve the tickets without changing the priority type. Your reporting
  shows a high number of “urgent” priority closed tickets. As an admin, you edit the
  tickets to the correct priority type so that the agents’ CSAT score and your reporting
  are reflected accurately.

After you modify closed tickets, the changes are reflected in the tickets’ events and your
Explore reports. Updates are also reflected in your views and search results.

### Considerations and limitations

Consider the following before deciding to modify closed tickets:

- You can edit one closed ticket at a time in the Zendesk Agent Workspace.
  Use the API to update multiple closed tickets at once. See the [Update Ticket](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/#update-ticket) and [Update Many Tickets](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/#update-many-tickets) API references.
- The organization of a closed ticket may be updated, but only through an
  organization merge. See [Merging organizations](https://support.zendesk.com/hc/en-us/articles/6216929727898).
- You must have the [Agent Workspace activated](https://support.zendesk.com/hc/en-us/articles/4581758611866) to edit closed tickets’ subject,
  priority, and custom fields. If you don’t, you can edit closed ticket fields through
  the API only.

## Activating the modify closed tickets setting

You must be an admin to turn on the setting for modifying closed tickets.

**To turn on the modify closed tickets setting**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Tickets > Settings**.
2. Click **Modify closed ticket** to expand it.
3. Select **Allow admins to modify specific fields on a closed ticket.**
4. Click **Save**.

## Modifying closed tickets

Closed tickets can be modified one at a time. You must be an admin to modify a closed
ticket.

**To modify a closed ticket**

1. In the Agent Workspace, find the closed ticket you want to modify. For example, you can
   [search for the ticket](../../agent-guide/ticket-basics/searching-tickets.md) or you may want to [create a view](https://support.zendesk.com/hc/en-us/articles/4408888828570) of your accounts’ closed tickets.
2. Click the ticket to open it.

   Note that the fields you can’t edit appear
   dimmed.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/closed_tickets_modify_tags.png)
3. Modify the closed ticket as needed.
   1. In the **Tags** field, add or remove a ticket tag.
   2. Edit the **Subject** field.
   3. If it’s present on the ticket, edit the **Priority** field.
   4. Update any **Custom Fields** that are available for the selected
      ticket.

      Note: [The Agent Workspace must be activated](https://support.zendesk.com/hc/en-us/articles/4581758611866) to edit the subject,
      priority, and custom fields.
4. Click **Resubmit**.

   The ticket updates and the change is reflected in the [ticket’s events](https://support.zendesk.com/hc/en-us/articles/4408829602970-Viewing-all-events-for-ticket-updates).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/closed_ticket_modify_events.png)

   Note that even though the ticket is updated, it’s still closed.
   This means that business rules won't run on it, SLAs don’t apply, and routing isn’t
   evaluated. See [About system ticket rules](https://support.zendesk.com/hc/en-us/articles/4408894213018).
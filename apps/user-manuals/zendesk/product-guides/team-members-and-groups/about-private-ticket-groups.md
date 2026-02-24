# About private ticket groups

Source: https://support.zendesk.com/hc/en-us/articles/4767122732058-About-private-ticket-groups

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Enterprise |

Verified AI summary ◀▼

Private ticket groups let you control access to sensitive tickets by restricting visibility to designated agents. You can create or convert groups to private, but they can't be reverted to public. Only agents with specific permissions can view or search these tickets. Private tickets maintain visibility for existing CCs and followers and are included in reports, but have limitations with triggers and macros.

Location:  Admin Center > People > Team >
Groups

On Enterprise plans, admins can designate a group as private. This means that agents
outside the group generally can’t access tickets assigned to it, although agents may be
granted [permission to view private tickets](https://support.zendesk.com/hc/en-us/articles/4988173561370#topic_l21_rbj_dvb). While an
agent outside the group can assign a public ticket to a private group or a member of a
private group, the ticket is made private as a result. Additionally, an agent working on
a private ticket is prevented from opening [side conversations](https://support.zendesk.com/hc/en-us/articles/4408844206746) with team members outside the private
group.

This article contains the following sections:

- [Essential facts for private ticket groups](#topic_nsv_hcj_dvb)
- [Limitations of private ticket groups](#topic_jkk_wcj_dvb)

To learn how to set up private groups, see [Creating private ticket groups and granting agents
access](https://support.zendesk.com/hc/en-us/articles/4988173561370).

## Essential facts for private ticket groups

We've distilled some essential facts for you about private ticket groups.
To learn how to set up a private group or convert a public group to private, see
[Creating private ticket groups and granting
agents access](https://support.zendesk.com/hc/en-us/articles/4988173561370).

- When [creating a group](https://support.zendesk.com/hc/en-us/articles/4408894175130), you have the option
  to designate the group as private. It cannot be converted to public.
- You can convert an existing public group to private, but it can’t be
  converted back to public.
- Tickets in private groups have a *private* tag with a lock icon
  (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_private_icon.png)) as part of the ticket status tag and a lock icon
  next to the assigned group's name. In views, the lock icon appears next to the
  ticket status for each private ticket in the list.
- Access to tickets, including tickets in private groups, is [set at the role level](https://support.zendesk.com/hc/en-us/articles/4408882153882). Among [native agent roles](https://support.zendesk.com/hc/en-us/articles/4408882153882#topic_clf_k5q_qk), Admins and Team
  Leaders can see tickets in private groups by default. Custom roles can be
  configured to have access to tickets in private groups. See [Granting agents access to tickets in private
  groups](https://support.zendesk.com/hc/en-us/articles/4988173561370#topic_l21_rbj_dvb).
- A private ticket can’t be viewed or searched for by agents who don’t
  have access to it.
- Agents can [@mention](https://support.zendesk.com/hc/en-us/articles/4928739064986) team members outside of
  private groups, which adds them to the ticket as a follower or CC, depending on
  your account settings.
- If a ticket is reassigned from a public group to a private one, CCs
  and followers are kept on the ticket and continue to be able to see it.
- If a ticket is reassigned from a private group to a public one, the
  ticket becomes visible to public groups.
- Tickets in private groups are still included in reports run for all
  tickets.
- Tickets that aren't assigned to a group are treated as if they're in a public
  group.
- Admins can [configure the visibility of internal
  comments](https://support.zendesk.com/hc/en-us/articles/4408822560410#topic_km4_33s_dzb) on tickets an agent requested, regardless of the ticket
  group assignment. If you restrict agents in your account from seeing internal
  notes and agent-only fields, they will only be able to [access tickets they've requested](https://support.zendesk.com/hc/en-us/articles/4408829574810) as an
  end user.

## Limitations of private ticket groups

- The status of a group as private or public isn't available as a
  trigger or automation condition. (*Group | is / is not | Private /
  Public*)
- Macros can’t yet be made available to all private groups similar to
  the way they can be made available to all agent groups.
- When a [side conversation ticket](https://support.zendesk.com/hc/en-us/articles/4408836521498) is
  assigned to a private group, it is visible to members who don't belong to
  the group.
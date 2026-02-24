# Working with email address conflicts in ticket replies

Source: https://support.zendesk.com/hc/en-us/articles/4408843970842-Working-with-email-address-conflicts-in-ticket-replies

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

When the From and Reply-to addresses in an incoming ticket reply do not match, and
the Reply-to address
is
the email address of an
agent
in your Support account, Zendesk Support automatically suspends some agent abilities until an
administrator confirms the agent’s identity and manually restores those abilities.

In this article, we’ll explain how the Reply-to and From email addresses are
identified in an email, what happens automatically when a conflict is discovered involving an
agent’s email address, and how you can restore an agent’s suspended abilities.

Note: If the From and Reply-to addresses are different, and the Reply-to address is a known
end user, no user abilities are suspended. Instead, the comment is flagged and a warning
appears letting you know that the From and Reply-to in the messages do not match.

This article includes
the following
sections:

- [Understanding suspension criteria and suspended
  abilities](#topic_wrs_l51_3nb)
- [Restoring agent
  abilities](#topic_d45_j51_3nb)

Related articles:

- [How does Zendesk handle Reply-to?](https://support.zendesk.com/hc/en-us/articles/4408831413402)
- [Suspending a user](https://support.zendesk.com/hc/en-us/articles/4408889293978)
- [About flagged tickets from registered users who are not signed
  in](https://support.zendesk.com/hc/en-us/articles/4408843002650)

## Understanding suspension criteria and suspended abilities

When a user looks at an email notification from their email client, they often
see multiple email addresses in the message. The From and Reply-to address are not always
the same.

If an incoming ticket reply has conflicting From and Reply-to email addresses,
and the Reply-to address is an agent, Zendesk takes the following actions:

- Flagging the ticket
- Suspending agent abilities

### Flagging the ticket

When a ticket is flagged, a warning icon appears on the ticket in the ticket UI. You can
hover over the icon to view more information. The ticket is not flagged in any ticket
views – it only appears in the ticket interface.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/replyto_conflict_warning.png)

### Suspending agent abilities

Zendesk suspends certain abilities belonging to the user whose email address is
in the *Reply-to field*. See Automatically suspended abilities for more
information.

If suspended, agents will no longer be able to:

- Change ticket properties.
- Add or remove [CCs or followers](https://support.zendesk.com/hc/en-us/articles/4408843795482) from the ticket.
- Execute [Mail API](https://support.zendesk.com/hc/en-us/articles/4408839419034) actions.
- Attach files to the ticket, if end users are [not allowed to do so](https://support.zendesk.com/hc/en-us/articles/4408832757146#topic_c2w_1nx_xdb). Attempted attachments are
  dropped and are not added to the ticket.

Suspended agents will still be able to:

- Forward emails to create new tickets. However, related comments will be
  flagged.
- Submit new tickets, even when [ticket submission is restricted](https://support.zendesk.com/hc/en-us/articles/4408893912986).

## Restoring agent abilities

If
the From/Reply-to conflict is *not considered a security risk*, you can restore the
agent's suspended abilities by adding their email address or domain to the allowlist. If you
*do not* trust the From email address, you can add that email address or domain to
the blocklist.

**To add an address or domain to the allowlist or blocklist**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **People** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png))
   in the sidebar, then select **Configuration > End users**.
2. In
   the **Anybody can submit tickets** section,
   enter
   the agent's email address or domain to the allowlist or blocklist as needed:

   - **Allowlist**: All support requests from an email address or domain are
     accepted.
   - **Blocklist**: All incoming support requests from the email address or domain
     are suspended or rejected, depending on your [allowlist and blocklist settings](https://support.zendesk.com/hc/en-us/articles/4408886840986#topic_jqt_4b4_xz).
3. Click **Save
   tab**
   at
   the bottom of the page.

If you are blocking a user, you may want to also disable CCs (see [Setting permissions for CCs and followers)](https://support.zendesk.com/hc/en-us/articles/4408843795482#topic_x3t_4p5_cq)).
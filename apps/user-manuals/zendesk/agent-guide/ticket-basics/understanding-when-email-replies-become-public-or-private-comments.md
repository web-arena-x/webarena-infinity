# Understanding when email replies become public or private comments

Source: https://support.zendesk.com/hc/en-us/articles/4408842992538-Understanding-when-email-replies-become-public-or-private-comments

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Learn when email replies become public or private comments. Replies to notifications can be private if sent by agents not assigned to the ticket, end users not on the ticket, or third parties. Using "Reply" instead of "Reply all" often results in private comments. The Mail API can also set comment visibility. Understand these rules to manage ticket communication effectively.

Location: Admin Center > Objects and rules > Tickets >
Settings

There are a few rules that determine whether a reply to a notification sent from email becomes a public comment or a private comment.

A *private comment* appears in the agent interface as an *internal note*. Private comments and internal notes are the same thing. This article uses the term *private comment* to describe these types of comments.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ccs_comments_internal.png)

This article includes these sections:

- [Checklist: How Support determines comments privacy for inbound emails](#topic_mpz_nnl_xrb)
- [Using "Reply" instead of "Reply all"](#topic_a3q_z4l_fhb)
- [Third party replies to ticket notifications](#topic_lhb_c4l_fhb)
- [Using the Mail API](#topic_onr_z2v_ypb)

For more information about using CCs and followers with email clients, see [Best practices for using email clients with CCs and followers](https://support.zendesk.com/hc/en-us/articles/4408824667930).

For a complete list of documentation about CCs and followers, see [CCs and followers resources](https://support.zendesk.com/hc/en-us/articles/4408836035866).

## Checklist: How Support determines comments privacy for inbound emails

Support performs a series of checks to determine comment privacy for inbound emails. These are the checks and the order in which they are performed:

1. If the ticket is being updated (rather than created) and the ticket was identified from the encoded ID in the email, and the author cannot edit the ticket:
   1. If the author is an agent and is not an assignee, follower, or CC on the ticket, the comment will be private.
   2. If the author is an end user and is not the requester or a CC on the ticket, the comment will be private.
2. If the ticket is being updated (rather than created) and the ticket was not identified from the encoded ID in the email, and the author cannot edit the ticket:
   1. The new comment will be suspended (and if/when recovered, it will follow similar rules outlined here from the top).
3. If the author is a CC, and the requester was not a direct recipient of the email:
   1. If [Make email comments from CCed end users public](https://support.zendesk.com/hc/en-us/articles/4408843795482-Configuring-CC-and-follower-permissions#topic_tg2_ct2_hlb)
      is disabled, the comment will be private.
   2. If [Make email comments from CCed end users public](https://support.zendesk.com/hc/en-us/articles/4408843795482-Configuring-CC-and-follower-permissions#topic_tg2_ct2_hlb)
      is enabled, but there were recipients other than a support address of the account, the comment will be private.
4. If the author is an end user, the comment will be public.
5. If the author has a role that can't comment publicly, the comment will be private. On Enterprise plans, the [agent as requester](https://support.zendesk.com/hc/en-us/articles/4408822560410#topic_km4_33s_dzb) and custom role settings may impact whether the agent's comments are public or private.
6. If the [Mail API](https://support.zendesk.com/hc/en-us/articles/4408839419034-Using-the-Mail-API-to-update-ticket-properties-from-your-inbox) was used with the #note command (for internal note), the comment will be private.
7. If [Agent comments via email are public by default](https://support.zendesk.com/hc/en-us/articles/4408822560410) is disabled, the comment will be private.
8. If the [ticket being updated is private](../ticket-management/creating-a-ticket-on-behalf-of-the-requester.md#topic_q5c_ztz_y2b), the comment will be private.
9. If Support determines that the email contains content that was previously part of private comments, the comment will be private.
10. If none of the criteria above is met, the comment will be public.

## Using "Reply" instead of "Reply all"

When someone replies to a ticket notification from their email client using **Reply** (instead of **Reply all**), the reply becomes a private comment (internal note) on the ticket.

For example:

- By default, when an end user CC replies to a ticket notification using **Reply** (instead of **Reply all**), the reply becomes a private comment on the ticket because the requester is not on the reply. CCs are not removed from the ticket. However, if the [Make email comments from CCed end users public](https://support.zendesk.com/hc/en-us/articles/4408843795482) setting is enabled, the behavior changes and the reply becomes a public comment instead.
- Follower replies are meant to be seen by agents only and result in an internal comment, regardless of whether **Reply** or **Reply all** is used.
- Assignee replies follow the rules for agents (and the [Agent comments via email are public by default](https://support.zendesk.com/hc/en-us/articles/4408822560410) setting) that were mentioned earlier in this article, regardless of whether **Reply** or **Reply all** is used.

## Third party replies to ticket notifications

In some rare cases, your end users may forward ticket notifications to a third party. A third party is someone who isn't the requester or a CC, assignee, or follower on the ticket.
This scenario is not common.

If a third party replies to a ticket notification from an email client, these things happen:

- A warning like the following appears in the ticket interface (click the icon to expand the menu and see the message):

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ccs_third_party.png)
- The reply becomes a private comment (internal note) on the ticket.
- The third party is not automatically added to the ticket as a CC.

As a result, agents may need to do these things:

- If the reply needs to be a public comment, then the agent must manually copy/paste the text into a public comment on their behalf.
- If future replies from this person need to be public comments, then the agent needs to add them as a CC from the ticket interface.

## Using the Mail API

You can also use Mail API commands to make a reply into a public or private comment. By default the value of the `#public` Mail API command is `true`, so the reply will be public. A `#public false` command will make the reply private. Also, you can use the `#note` syntax to make a reply into a private comment. See [Using the Mail API to update ticket properties from your inbox](https://support.zendesk.com/hc/en-us/articles/4408839419034).
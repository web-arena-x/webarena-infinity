# Understanding suspended tickets and spam

Source: https://support.zendesk.com/hc/en-us/articles/4408889141146-Understanding-suspended-tickets-and-spam

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Email sent to Zendesk Support can be suspended or rejected. Suspended emails are
often, but not always, spam. This article explains what suspended tickets are
and your options for managing them.

This article discusses the following topics:

- [What are suspended
  tickets?](#topic_vpr_1sp_nj)
- [What causes emails to be suspended?](#topic_ywn_v2j_dwb)
- [What factors
  influence suspended tickets](#topic_ewp_qrl_zsb)

## What are suspended tickets?

In most cases, when an end user submits a support request by email, the
email becomes a new ticket or adds a comment to an existing ticket.
In certain cases, the email may be suspended. Suspending an email
means putting it aside for further review. It's not necessarily spam
but it's not a ticket in Support yet. It remains in limbo until
somebody reviews it and decides whether to accept or reject it.

Suspended emails are collected in a system-generated view. The [suspended tickets view](https://support.zendesk.com/hc/en-us/articles/4408893392922#topic_ukg_lbf_kd)
is visible to any agent with access to all tickets.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/suspended_tickets_view.png)

As a best practice, you should [review suspended tickets
frequently](https://support.zendesk.com/hc/en-us/articles/4408832102042). If nobody reviews a suspended email, it's
automatically deleted after 14 days.

Sometimes, rather than being suspended, an email is rejected. A rejected
email is not kept for further review and it can't be recovered.

The following are common reasons why email is rejected:

- If the email is rated as having a 99% or better chance
  of being spam, it's rejected. If the rating is less
  than 99%, the email is suspended to give you a
  chance to confirm that it's really spam.
- You blocked the email address or domain. See [Using the allowlist
  and blocklist to control access to Zendesk
  Support](https://support.zendesk.com/hc/en-us/articles/4408886840986).
- The email was sent by an automated system (for example,
  a non-delivery notification email).

## What causes emails to be suspended?

An email can be suspended for several reasons, including:

- The email is rated as spam. Spam is the most common
  cause for suspension.
- The sender is not allowed to create or update a ticket.
  For example, the email is from an unregistered user
  when you require users to register.
- The sender is not a person.
- The email failed [DMARC
  authentication](https://dmarc.org), which Zendesk uses to
  authenticate agent users.

For a full list of suspension causes, see [Causes for ticket
suspension](https://support.zendesk.com/hc/en-us/articles/4408828416282).

## What factors influence suspended tickets

For security purposes, Zendesk automatically performs some scanning of
tickets to identify malicious content. However, the way you
configure your account also influences how many emails are
suspended.

If you're trying to balance the spam-prevention efforts with the workload
of reviewing the suspended ticket queue, consider the following:

- Who do you [allow to submit
  tickets](https://support.zendesk.com/hc/en-us/articles/4408883052442#topic_vbt_qsv_kj)?

  If you have [restricted ticket
  submission](https://support.zendesk.com/hc/en-us/articles/4408893912986) to only users with approved
  email addresses or [closed ticket
  submission](https://support.zendesk.com/hc/en-us/articles/4408883658906) to everyone except the users
  you've added, you'll see more suspended tickets
  than you would if you [allowed anyone to
  submit tickets](https://support.zendesk.com/hc/en-us/articles/4408881989018).
- Have you enabled [DMARC, SPF, or DKIM
  authentication for incoming emails](https://support.zendesk.com/hc/en-us/articles/4408821985818)?

  Each
  of these methods works differently to detect spam
  and spoofed emails, so they do result in more
  suspended tickets, but they also add a layer of
  security to the inbound emails that generate
  tickets.
- Are you using the [allowlist and
  blocklist](https://support.zendesk.com/hc/en-us/articles/4408886840986)?

  Emails submitted by end users
  on the blocklist are suspended by default, but you
  can configure it so that they are rejected. The
  allowlist specifies who is exempt from the
  blocklist rules as well as bypassing some other
  standard causes for email suspension.

  If
  you find that some of your security settings are
  resulting in too many suspended tickets, look for
  patterns of similarity to the valid tickets that
  are being suspended. Then use the allowlist and
  blocklist to permit emails that match that
  pattern.

We recommend [implementing a process for
reviewing suspended emails](https://support.zendesk.com/hc/en-us/articles/4408832102042) frequently. Any emails
that remain in the suspended tickets queue for 14 days without
review are automatically deleted.
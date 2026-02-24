# A complete guide to understanding email in Zendesk - Part 2: Incoming email requests and notifications

Source: https://support.zendesk.com/hc/en-us/articles/4408887388058-A-complete-guide-to-understanding-email-in-Zendesk-Part-2-Incoming-email-requests-and-notifications

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center > Channels > Talk and email > Email

Articles in the series

- [Introduction: A complete guide to understanding email in Zendesk](https://support.zendesk.com/hc/en-us/articles/4887918604058)
- [Part 1: How the email channel works](https://support.zendesk.com/hc/en-us/articles/4408888639258)
- [Part 2: Incoming email requests and notifications](https://support.zendesk.com/hc/en-us/articles/4408887388058)
- [Part 3: Outgoing email notifications](https://support.zendesk.com/hc/en-us/articles/4408893474202)
- [Part 4: Common email channel problems](https://support.zendesk.com/hc/en-us/articles/4408887479834)

In [Part 1](https://support.zendesk.com/hc/en-us/articles/4408888639258) of this guide, we explained the essentials of how the email channel works. In part 2 we explain how incoming support requests via email are handled and how to customize the incoming email channel workflow.

- [Choosing the email addresses you want to use to receive support requests](#topic_v3b_zfd_v3)
- [Understanding how incoming emails set the ticket requester](#topic_f4r_8hs_v4)
- [Understanding how incoming emails are matched to tickets](#topic_r1f_4gd_v3)
- [Spam filtering and suspended tickets](#topic_uv2_331_53)
- [Controlling who can use email to create tickets](#topic_krx_lrp_vcb)
- [Managing user accounts created by email requests](#topic_zgl_1sp_vcb)
- [Disabling rich content in incoming email notifications](#topic_hgh_5sp_vcb)
- [How a customer’s language is detected](#topic_wcp_ysp_vcb)
- [Including other people in a support conversation as a CC or follower](#topic_mtr_htp_vcb)

## Choosing the email addresses you want to use to receive support requests

One support address is created for you by default when you create your Zendesk Support account. This system support address is support@*yoursubdomain*.zendesk.com. The *yoursubdomain* portion of the address is your [Zendesk subdomain](https://support.zendesk.com/hc/en-us/articles/4408883411354#topic_swn_h2f_3xb). However, you can provide your users with alternative email addresses for submitting tickets by adding other support addresses and by forwarding email into your Zendesk Support account from external email systems.

You can receive support requests through multiple email addresses simultaneously. The email addresses you use to receive support requests in Zendesk Support are referred to as [*support addresses*](https://support.zendesk.com/hc/en-us/articles/4408842868506#topic_wg1_1zk_zm). If you use multiple support addresses, one of them is set as the default support address.

There are several ways to customize the email addresses that you use to receive support requests using support addresses:

- [Changing the user name of your default support email address](#topic_tpt_nmp_vcb)
- [Allowing any user name to be a valid support email address](#topic_j3c_zmp_vcb)
- [Using an external email domain instead of your Zendesk Support email domain](#topic_z5y_fnp_vcb)
- [Agent email forwarding and redirecting](#topic_nqx_wnp_vcb)

### Anatomy of an email address

Before showing you how you can customize your support email addresses, here’s a quick overview of the elements of an email address.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_parts.png)

The friendly name, referred to in Zendesk Support simply as ‘name,’ is optional and is usually the full name of your business or organization. The user name, technically known as the *local-part*, is the word that precedes the @ character. The domain can be either your Zendesk Support domain or an external domain.

### Changing the user name of your default support email address

You can easily create new support email addresses if you want variations of the email user name. For example:

- help@*yoursubdomain*.zendesk.com
- sales@*yoursubdomain*.zendesk.com
- billing@*yoursubdomain*.zendesk.com

By using different email addresses for different situations, you can manage and track your tickets based on the email address at which the support request was received. For example, if your end users send email to sales@*yoursubdomain*.zendesk.com, you can create a trigger to route tickets received at that address directly to the Sales team. You can also track, via views and reports, tickets received at those different addresses.

Zendesk Support provides a simple wizard for creating new support email addresses. For more information, see [Using Zendesk email addresses as support addresses](https://support.zendesk.com/hc/en-us/articles/5000599601050#topic_sb3_wfp_3n).

### Allowing any user name to be a valid support email address

You can also allow any variation of the user name to be a valid support address. For example, if a customer misspelled your support email address as *biling@yoursubdomain.zendesk.com* rather than *billing@yoursubdomain.zendesk.com*, the email can be accepted and a ticket created. These types of variations are referred to as *wildcards*.

Wildcards handle incoming support address errors (as in the example above). When they are received, the default support address replaces the incorrect address. Note that wildcard addresses cannot be used in business rules.

To enable wildcards for incoming support requests, see [Accepting wildcard email addresses for support requests](https://support.zendesk.com/hc/en-us/articles/5318946039578).

### Using an external email domain instead of your Zendesk Support email domain

You can also add external email domains as support email addresses in Zendesk Support. You can forward all the email that’s coming into your external email account (Gmail, for example) into Zendesk Support. Your customers can continue to use the same email address you had before you started using Zendesk Support, and there’s no ‘Zendesk’ in the email *Sent To* and *Reply From* addresses.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_domain.png)

There are three steps to using an external email domain.

1. First, create a new external email-based support address in Zendesk Support.
2. Next, you must set up email forwarding by configuring your email account outside of Zendesk Support.
3. Finally, [add a sender policy framework (SPF) record](https://support.zendesk.com/hc/en-us/articles/4408832543770) to verify that Zendesk can send outgoing email on behalf of your email server.

See [Forwarding incoming email from your existing email address to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408886828698) for details.

### Agent email forwarding and redirecting

[Setting up a support email address from an external email system](https://support.zendesk.com/hc/en-us/articles/4408886828698) allows you to automatically forward customer emails into your Zendesk Support account. It’s also possible to manually forward or redirect one-off support requests that you may receive at an email address that has not been added as a support address.

You can allow your agents to forward email to your support address to create a ticket on behalf of the original sender. To do this, [enable the email forwarding option for agents](https://support.zendesk.com/hc/en-us/articles/4408836514202#topic_ym4_2ng_3k). Agents can also set the original sender of the email as the requester using a simple text command in the forwarded email (see [Specifying the requester in the forwarded email](https://support.zendesk.com/hc/en-us/articles/4408836514202#topic_mtw_hbs_2k)).

Another option is to [redirect the email using the email application where it was received](https://support.zendesk.com/hc/en-us/articles/4408836514202#topic_q4l_bwr_2k). For example, in Microsoft Exchange an email message can be redirected using the **Actions > Resend this Message** command.

## Understanding how incoming emails set the ticket requester

The email body is not used in any way to assist in identifying the requester of a ticket. Zendesk uses information from the email headers to determine the ticket requester. Usually a requester is set based on the **reply-to:** header flag. If the **reply-to:** header is not present, **from:** is used in its place. This behavior can't be changed.

![The reply to: and from: fields in the email header](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zug_email_getting_started_part2_headers.png)

Agents can [use the mail API](https://support.zendesk.com/hc/en-us/articles/4408839419034) *#requester* syntax to set the requester on a ticket.

For more information on email threading, see [How can I troubleshoot threading issues?](https://support.zendesk.com/hc/en-us/articles/4408821051034)

## Understanding how incoming emails are matched to tickets

A ticket in Zendesk Support is similar to a threaded email conversation. Keeping the thread together as part of the same ticket is done using references embedded in both the outgoing and incoming email notifications. For example, when a customer replies to an email notification, the reply includes references to the ticket so that the incoming email can be matched to the correct ticket in Zendesk Support.

Email notifications include ticket references in the following places:

- A reply back from a customer contains ticket references in the email header using *In-Reply-To* and *References*. You can [view the header and source of any email that you receive](https://support.zendesk.com/hc/en-us/articles/4408832876442).
- The email body includes a hidden reference to the ticket.
- If you're using an address in your Zendesk domain, the *Reply To* email address includes an encoded reference to the ticket ID. For example:  
 MondoCam Support <support+id1G7EOR-0Q2J@mondocam.zendesk.com>
- Note: If you're using an external domain for email, the encoded ticket ID is not included in the Reply To email address.

After an email conversation has been started and ticket references have been embedded into the thread, any replies back and forth are tied to that ticket. If, for some reason, you wanted to create a new ticket from that email thread, you’d need to copy the content of the email message and create a new email message. Forwarding the email thread to one of your other support email addresses won't create a new ticket because the embedded ticket references will tie it back to the original ticket.

## Spam filtering and suspended tickets

Zendesk uses spam filtering to prevent your Zendesk Support account from getting cluttered with bogus tickets. Spam email is caught and may be held in the suspended tickets queue or completely rejected (meaning that you’ll never see them) if there's a high probability that the email is spam.

Keep in mind that spam filtering is not perfect and that legitimate support requests may end up in the suspended tickets queue. When that happens, you can manually retrieve them. For a detailed explanation of why some incoming email ends up in the suspended tickets queue, see [What does "Detected as spam" mean?](https://support.zendesk.com/hc/en-us/articles/4408832769306-What-does-Detected-as-spam-mean-).

All of your suspended tickets are listed in a system-generated view that won't appear in your list of views until the first time a ticket is suspended. Use the Suspended tickets view to review the emails and accept them as legitimate tickets or reject them as spam. See [Understanding and managing suspended tickets and spam](https://support.zendesk.com/hc/en-us/articles/4408889141146).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/suspended_tickets_view.png)

## Controlling who can use email to create tickets

Another way to prevent bogus or unwanted tickets is to prevent specific users or groups of users from creating tickets with email. To do this, [add their email domains or individual email addresses to your blocklist](https://support.zendesk.com/hc/en-us/articles/4408886840986). This causes their emails to be suspended or completely rejected. If you want to allow exceptions to your blocklist, you can add specific email addresses or domains to your allowlist. For example, if specific users within a blocked email domain are allowed to submit support requests via that email domain, you can add email addresses for those specific users to the allowlist.

You can also set up a closed Zendesk where [only the users that you add to your Zendesk Support account can submit support requests](https://support.zendesk.com/hc/en-us/articles/4408883658906). When you place access restrictions like this on your Zendesk Support account, you’re creating a *restricted* account. For more information, see [Understanding options for end-user access and sign-in](https://support.zendesk.com/hc/en-us/articles/4408887573274-Configuring-how-end-users-access-and-sign-in-to-Zendesk-Support).

## Managing user accounts created by email requests

All the customers you support have a user account in Zendesk Support. Unless you restrict or close access to your Zendesk Support account, new user accounts are created when you receive a customer’s first support request via email, excluding suspended or rejected emails. A customer’s user account tracks of all their support requests, contains their contact information, and all of the data that’s gathered in the course of interacting with them.

Because most people use more than one email address, you may receive support requests from an existing customer who has used one of their other email addresses. When this happens, a new and separate user account is created. It's best to avoid duplicate accounts, so you can [merge the newly created account into the customer’s original user account](https://support.zendesk.com/hc/en-us/articles/4408887695898).

Using more than one email address is supported, as long as the customer’s other email addresses are also added to their user account. If you give end users access to [edit their profile via the customer portal in your help center](https://support.zendesk.com/hc/en-us/articles/4408837910426), they can add other email addresses to their user account themselves.

If users have more than one email address associated with their profile, one of the email addresses is set as their primary email address. The other contact email addresses that are added to their profile are used to associate support requests from those email addresses with their user account. All outgoing email notifications to customers use the primary email address.

### Assigning email requesters to organizations

When you receive an email support request from a customer for the first time, which creates their user account, you can assign that customer to an organization based on their email domain. For example, you might want to segment your customers based on the company they work for, which you’ll know by their email domain. This is referred to as *user mapping* and admins can set this up by editing an organization's settings.

For more information, see [Automatically adding users to organizations based on their email domain](https://support.zendesk.com/hc/en-us/articles/4408882246298#topic_nxl_vdt_bc).

## Disabling rich content in incoming email notifications

By default, Zendesk Support uses the rich content formatting contained in incoming HTML-based email messages (bold, italic, underline, tables, etc.). The rich content is retained and displayed in tickets. If you prefer to use the plain text version of email messages, you can [disable rich content in incoming emails](https://support.zendesk.com/hc/en-us/articles/4408828563866).

## How a customer’s language is detected

Zendesk Support provides a number of ways to identify a customer’s language and reply to them in their preferred language. [User profiles include a language setting](https://support.zendesk.com/hc/en-us/articles/4408887059866), which users and agents can specify. Additionally, Zendesk also attempts to [detect their language from incoming email](https://support.zendesk.com/hc/en-us/articles/4408882016666) support requests from new customers.

## Including other people in a support conversation as a CC or follower

Support conversations aren’t always limited to the customer who needs support and the assigned agent to provide that support. You can use the [CCs and followers feature](https://support.zendesk.com/hc/en-us/articles/5179445630234) to include other people in the conversation and alert them to responses.

Admins can [allow agents and signed-in customers to add CCs to tickets](https://support.zendesk.com/hc/en-us/articles/4408843795482), but enabling CCs can add complexity because of the increased number of recipients. When other agents are added as CCs, they receive email notifications for all ticket updates, including both public and private comments added to the tickets. Customers that are CC’d only receive email notifications for public comments and ticket updates.

Followers get email notifications when comments are added to tickets they are following. There’s no way to disable email notifications to followers (other than to stop using followers), but you can customize the text in email notifications to followers using the [followers email template](https://support.zendesk.com/hc/en-us/articles/4408843866394#topic_vb5_sqr_jhb).

When [rich text formatting](https://support.zendesk.com/hc/en-us/articles/4408884153242) is enabled, you can also add other people to a ticket by [using an @mention](https://support.zendesk.com/hc/en-us/articles/4928739064986) within the body of a ticket comment.
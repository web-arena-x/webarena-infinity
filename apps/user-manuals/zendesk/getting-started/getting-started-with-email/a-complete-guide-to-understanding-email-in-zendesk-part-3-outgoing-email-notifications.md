# A complete guide to understanding email in Zendesk - Part 3: Outgoing email notifications

Source: https://support.zendesk.com/hc/en-us/articles/4408893474202-A-complete-guide-to-understanding-email-in-Zendesk-Part-3-Outgoing-email-notifications

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > Channels > Talk and email > Email

Articles in the series

- [Introduction: A complete guide to understanding email in Zendesk](https://support.zendesk.com/hc/en-us/articles/4887918604058)
- [Part 1: How the email channel works](https://support.zendesk.com/hc/en-us/articles/4408888639258)
- [Part 2: Incoming email requests and notifications](https://support.zendesk.com/hc/en-us/articles/4408887388058)
- [Part 3: Outgoing email notifications](https://support.zendesk.com/hc/en-us/articles/4408893474202)
- [Part 4: Common email channel problems](https://support.zendesk.com/hc/en-us/articles/4408887479834)

In [Part 1](https://support.zendesk.com/hc/en-us/articles/4408888639258), we explained the essentials of how the email channel works.
[Part 2](https://support.zendesk.com/hc/en-us/articles/4408887388058) covered incoming email support requests and the customization
and workflow you can make.

Here in part 3, we explain how you can manage and customize your outgoing email notifications
and customer experience.

- [A note about email security](#topic_v3b_zfd_v3)
- [Personalizing the sender information in
  your outgoing email notifications](#topic_r1f_4gd_v3)
- [Customizing the design of the email
  template used for your outgoing email notifications](#topic_uv2_331_53)
- [Changing the wording of the messages in
  your automated email notifications](#topic_krx_lrp_vcb)
- [Supporting multiple languages in your
  outgoing email notifications](#topic_zgl_1sp_vcb)
- [Notifying external targets with outgoing
  email notifications](#topic_hgh_5sp_vcb)
- [Creating and updating tickets from an
  email inbox using the Mail API](#topic_wcp_ysp_vcb)
- [Creating tickets for customers without
  notifying them](#topic_mtr_htp_vcb)

## A note about email security

Outgoing email notifications are not encrypted; however, Zendesk Support provides opportunistic
support for Transport Layer Security (TLS), a cryptographic protocol for email exchanges.
When not in use, ESMTP is used instead.

When you set up an external email domain to use as a support address, you should also
consider adding an additional layer of security to prevent spoofing and verify that email
from you to your customers is legit. This is done by [digitally signing your outgoing email with DKIM or DMARC](https://support.zendesk.com/hc/en-us/articles/4408822303386).

## Personalizing the sender information in your outgoing email notifications

You can personalize how you respond to your customers via email notifications. Aside from
customizing the wording in the email notification messages (see [Changing the wording of the messages in your
automated email notifications](#topic_krx_lrp_vcb) below), you can modify your outgoing email
notifications to create a more personalized agent-to-customer experience.

### Personalized email replies

Personalized email replies let you see who has updated the ticket on both sides of the
support conversation. The agent’s name is added as the Sent From address in outgoing email
notifications, and the customer's name appears in the Reply From address in email replies
to the agent. This experience is enabled for you by default.

If you leave personalized email replies enabled, customers see the agent’s name:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_personal_replies_example_on2.png)

If you disable personalized email replies, this is what customers see (the name you’ve
used for your Zendesk Support account):

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_personal_replies_example_off.png)

For more information, see [Enabling personalized email replies](https://support.zendesk.com/hc/en-us/articles/4408887209498).

### Agent aliases

In the Professional and Enterprise versions of Zendesk Support, you can also use an agent
alias instead of the agent’s real name to protect their identity or use nicknames and
personas.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lotus_alias.png)

For more information, see [Adding an agent alias](https://support.zendesk.com/hc/en-us/articles/4408893352986).

### Agent signatures

Each agent's signature can be added to ticket comments and outgoing email notifications.
This is set as the default on the **Agents** settings page. A placeholder is used to
insert the signature that agents add to their own profiles. An agent's signature can
include any text, such as their name, the name of their support group, contact
information, and so on.

You can also create a signature template for your Zendesk if, for example, you want all
agent signatures to include a standard wording and format for the company address.

For more information, see [Adding an agent signature to ticket email notifications](https://support.zendesk.com/hc/en-us/articles/4408822471322). You can
add an agent signature to outgoing messages.

### Rich text formatting in outgoing email notifications

You can add rich text formatting to your outgoing email notifications. Agents can add
bolding, italics, lists, and other formatting, as well as images. For more information
about rich text formatting, see [Enabling formatting options for agents](https://support.zendesk.com/hc/en-us/articles/4408884153242).

## Customizing the design of the email template used for your outgoing email notifications

All of your email notifications are sent using an email template that you can customize to match
your branding. The template is in both HTML and plain text.

You can also make some minor modifications to words used in the template (such as the words
used in the footer). This is not be confused with the words used in the messages contained
in your email notifications (see [Changing the
wording of the messages in your automated email notifications](#topic_krx_lrp_vcb) below).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_html_after.png)

This example shows that a header graphic has been added to the HTML template, and the
colors have been changed.

For information about customizing your email templates, see [Customizing templates for your email notifications](https://support.zendesk.com/hc/en-us/articles/4408886168090).

## Changing the wording of the messages in your automated outgoing email notifications

As discussed in [How triggers and automations generate email notifications](https://support.zendesk.com/hc/en-us/articles/4408888639258#topic_r1f_4gd_v3), you
can change the wording of the messages in the automated email notifications that are
generated by triggers and automations, and also the default macros. This can be as simple as
editing the text, or you can add different types of ticket and user data using placeholders
and customize how this data is selected and displayed as output using Liquid markup.

### Changing the system-generated registration, welcome, and email verification email notifications

Three of the email notifications that customers typically receive when they request
support and create a user account are the registration, welcome, and email verification
emails. These can be easily edited by an administrator in the Account emails section of
the **Customers** settings page.

For more information about updating these email messages, see [Customizing end-user account emails](https://support.zendesk.com/hc/en-us/articles/4408824350746).

### Changing the wording in email notifications generated by triggers, automations, and macros

You can edit the messages contained in the email notifications that are generated by
triggers, automations, and macros. You can do this by editing the existing versions or by
cloning them and then editing the clones. With triggers and automations, you need to think
about the effect creating clones will have on your support workflow, so make sure you
understand how triggers and automations work before editing them or creating clones.

To edit the messages in triggers, automations, and macros, see the following articles:

- [Editing and cloning triggers](https://support.zendesk.com/hc/en-us/articles/4408882237722#topic_dwq_zoy_tb)
- [Editing and cloning automations](../../product-guides/business-rules/creating-and-managing-automations-for-time-based-events.md#topic_rsh_miv_ub)
- [Editing, cloning, deactivating, and deleting
  macros](../../agent-guide/ticket-automation-and-collaboration/organizing-and-managing-your-macros.md#topic_mtv_gmx_tb)

### Using Liquid markup for more advanced control of how email notifications are generated

Liquid markup (available in the Professional and Enterprise versions of Zendesk Support)
allows you to create simple programming logic such as case statements, if statements, for
loops, and so on. It’s useful when you need more advanced control of how email
notifications are generated. For example, you can create email notifications that display
different messages based on when they were received (within your business hours or not),
as shown in this
example:

```
{% if ticket.in_business_hours == 'true' %}
Hello {{ticket.requester.first_name}}
Your request (#{{ticket.id}}) has been received and is being reviewed by our support staff. 
To review the status of the request and add additional comments, follow the link below:
http://{{ticket.url}}
{{ticket.comments_formatted}}
```

For more information about Liquid markup, see [Understanding Liquid markup and Zendesk
Support](../../product-guides/business-rules/understanding-liquid-markup-and-zendesk-support.md).

## Supporting multiple languages in your outgoing email notifications

If you support customers in multiple languages, you can create translated versions of your
automated messages that will be sent to your customers based on their language. There’s no
need to create separate versions of your triggers, automations, and macros for each language
you support.

This is available in the Professional and Enterprise versions of Zendesk Support and can be
done using [Dynamic Content](https://support.zendesk.com/hc/en-us/articles/4408882999066-Providing-multiple-language-support-with-dynamic-content-Professional-and-Enterprise-) (the recommended approach) and also
using [Liquid markup](https://support.zendesk.com/hc/en-us/articles/4408842967578).

For information about how a customer’s language is set and detected, see [Configuring Zendesk Support for your locale and
language](../../product-guides/multiple-language-support/configuring-zendesk-support-for-your-locale-and-language.md) and [Detecting an end-user's language from an email
message](https://support.zendesk.com/hc/en-us/articles/4408882016666).

## Notifying external people and systems

It’s possible to use webhooks to notify people and systems that are external to your
Zendesk Support account. For example, you might want to notify one of your suppliers when
customers have issues with their products. Web developers typically use webhooks to invoke
behavior in another system, such as Salesforce or X (formerly Twitter), but can also send emails if the
email provider supports that.

To learn more about creating and using webhooks, see [Creating webhooks](https://support.zendesk.com/hc/en-us/articles/4408839108378).

## Creating and updating tickets from an email inbox using the Mail API

Agents can create new tickets using text commands in an email message. They can also update
ticket properties by adding text commands when replying to email notifications. For example,
to set a ticket as solved using an email notification, an agent can add the text command
`#status solved` in their reply. For a more detailed explanation of the
Mail API and a list of commands that may be used, see [Using the Mail API to update ticket properties from your
inbox](https://support.zendesk.com/hc/en-us/articles/4408839419034-Using-the-Mail-API-to-update-ticket-properties-from-your-inbox).

## Creating tickets for customers without notifying them

While agents often [create tickets for customers](../../agent-guide/ticket-management/creating-a-ticket-on-behalf-of-the-requester.md), sometimes it’s useful
to create a ticket for a customer and be able to control when the customer is notified that
the ticket has been created. These are referred to as private tickets. You can create them
by simply creating a new ticket in Zendesk Support for a customer and adding a private
comment rather than a public comment. Customers don’t receive email notifications when
private comments are added to a ticket. If and when you’re ready to include the customer in
the support conversation, you add a public comment and an email notification is sent to the
customer. To learn more about how private tickets can be used, see [Creating a private ticket for an end-user](../../agent-guide/ticket-management/creating-a-ticket-on-behalf-of-the-requester.md#topic_uyq_5rx_yy).
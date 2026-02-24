# Adding support email addresses for users to submit tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408842868506-Adding-support-email-addresses-for-users-to-submit-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Add support email addresses to centralize customer inquiries into tickets. You can use variations of your existing email or external addresses. Admins can add up to 3000 addresses. For external emails, set up forwarding to ensure emails become tickets. Use these addresses to organize tickets, apply business rules, and manage multiple brands effectively.

As described in [Understanding the default email setup in Zendesk](https://support.zendesk.com/hc/en-us/articles/5612728377754), you
have one email address when you set up Zendesk Support:
support@*yoursubdomain*.zendesk.com. Emails received at this address become tickets.

You can provide your users with alternative email addresses for submitting tickets. These
addresses are known as *support addresses*. Support addresses can be either variations of
your Zendesk email address or external email addresses. Any email address you want to use to
receive support requests as tickets (whether it's a Zendesk address or an external address)
must be added to your Zendesk as a support address.

Only a Support admin can add support email addresses. You can have up to 3000 support
addresses.

Note: If you are adding support addresses for external email
addresses, additional steps are required to set up forwarding from your email server to your
Zendesk (see [Forwarding incoming email from your existing email address
to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408886828698)).

For each support address you add, the from address will match the support address the ticket
is sent to. For example, tickets sent to help@acme.zendesk.com will reply from
help@acme.zendesk.com.

This article contains the following sections:

- [Adding support addresses](#topic_wg1_1zk_zm)
- [Receiving email at your support
  addresses](#topic_133_rwk_zs)

Related articles:

- [Understanding the support address end-user experience](https://support.zendesk.com/hc/en-us/articles/5000599601050)
- [Managing your support addresses](https://support.zendesk.com/hc/en-us/articles/5279521301914)
- [Accepting wildcard email addresses for support requests](https://support.zendesk.com/hc/en-us/articles/5318946039578)

## Adding support addresses

Support addresses can be either variations of your Zendesk email
address or existing external email addresses, using these options:

- **Connect external address** Use this option to add an existing external email
  address.
- **Create new Zendesk address** Use this option to add variations of your Zendesk
  email address.

This section covers the following topics:

- [Adding a Zendesk support
  address](#topic_kby_k3w_jw)
- [Adding an external support
  address](#topic_glt_l3w_jw)

### Adding a Zendesk support address

Zendesk addresses are variations of your original support address,
support@*yoursubdomain*.zendesk.com. For example,
help@*yoursubdomain*.zendesk.com. You can add additional support addresses as
needed.

Note: If you want to add your own external support address, see [Adding an external support
address](#topic_glt_l3w_jw).

**To add a Zendesk support address**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Email**.
2. Click **Manage support addresses**.
3. Click **Add address**, then select **Create new Zendesk address**.
4. If you have multiple brands, select the brand for the email address from the
   drop-down menu.
5. Enter an address you'd like to use for receiving support requests.
6. Click **Save**.

   The email address is added to your list of support addresses.

### Adding an external support address

External email addresses are owned and maintained by you, outside of Zendesk (for
example, support@mycompany.com). You can receive support requests at an external email
address and forward the incoming email to Zendesk.

In turn, Zendesk can send email replies to your customers through your external email
address. If you're using the [Gmail connector](https://support.zendesk.com/hc/en-us/articles/4408835030426), [authenticated SMTP connector](https://support.zendesk.com/hc/en-us/articles/6740880198810), or [Exchange connector](https://support.zendesk.com/hc/en-us/articles/8979947090586), sent copies of emails are stored with your
external email address. Enterprise accounts can optionally turn on [automatic email archiving](https://support.zendesk.com/hc/en-us/articles/4408893355418), which allows you to send a copy of
every outbound email notification to a BCC address. This BCC address should be an external
email address, ensuring the archive is maintained outside of Zendesk.

If you add an external email address, additional steps are required to set up forwarding
from your email server to Zendesk. For more information, see [Forwarding incoming email from your existing email address to Zendesk
Support](https://support.zendesk.com/hc/en-us/articles/4408886828698).

## Receiving email at your support addresses

Emails sent to any of your known support addresses become tickets in your Zendesk account.
If you've enabled wildcard emails (see [Accepting wildcard email addresses for support requests](https://support.zendesk.com/hc/en-us/articles/5318946039578)), emails
sent to any variation of your Zendesk address, regardless of whether it's a known support
address, also become tickets.

Note: If an email containing more than 65,000 characters is sent to your Zendesk, the
resulting ticket comment is truncated. This can sometimes happen when an email thread
contains many replies, and is forwarded to your Zendesk support address.

For tickets received via email, you can see which address it was sent to at the top of the
ticket.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_via_supportaddress.png)

You can set up business rules, views, and SLA policies for tickets sent to your support
address by using the "Ticket: received at" condition.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_trigger_condition_received_at.png)

If you have set up multibrand, then the ticket receives the brand associated with the
support address the email was sent to (see [Adding email support addresses for multiple
brands](https://support.zendesk.com/hc/en-us/articles/4408836507162-Configuring-your-channels-to-support-multiple-brands-Enterprise-#topic_jzj_w3t_2r)).
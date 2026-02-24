# Authenticating incoming email (SPF, DKIM, DMARC, and ARC)

Source: https://support.zendesk.com/hc/en-us/articles/4408821985818-Authenticating-incoming-email-SPF-DKIM-DMARC-and-ARC

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Enhance email security by enabling SPF, DKIM, DMARC, and ARC authentication to reduce spoofed emails and spam. This feature suspends unauthenticated emails, which can be reviewed in the Suspended tickets view. Regularly check for suspensions to identify issues with sender authority or forwarding workflows. Adjust workflows if needed, rather than disabling the feature, to maintain email ecosystem health.

To decrease the number of spoofed emails and spam you receive, you can add an additional layer of
security to your inbound emails by turning on authentication with SPF, DKIM,
DMARC, and ARC support.

- Sender Policy Framework ([SPF](https://en.wikipedia.org/wiki/Sender_Policy_Framework)) is a
  path-based email authentication technique.
- DomainKeys Identified Mail ([DKIM](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail)) is a
  signature-based email authentication technique.
- Domain-based Message Authentication, Reporting, and Conformance
  ([DMARC](https://en.wikipedia.org/wiki/DMARC)) is a
  technical specification that allows email message senders
  and receivers to cooperate and better detect when messages
  don't originate from the internet domain they appear to
  represent.
- Authenticated Received Chain ([ARC](https://www.valimail.com/blog/what-is-email-arc/)) is a set
  of email headers used to preserve and validate
  authentication through auto-forwarding. You may want to
  check that your email provider supports this protocol.

Important: Turning on this type of security authentication can lead to
more cases where emails from unauthenticated workflows, spammers, or even
regular senders may end up in your Suspended tickets view. This can reveal
very important ways to improve the health of your email ecosystem. In
addition, Zendesk occasionally makes improvements and updates to our
authentication policies, which may result in minimal changes to ticket
suspensions.

This article includes the following topics:

- [Turning on sender authentication](#topic_jpl_mc3_cdb)
- [Checking for
  suspensions](#topic_axs_mc3_cdb)

Related articles:

- [Workflow: Ensuring
  email system compatibility with Zendesk](https://support.zendesk.com/hc/en-us/articles/4412991936922)
- [Understanding and
  managing suspended tickets and spam](https://support.zendesk.com/hc/en-us/articles/4408889141146)
- [Viewing, recovering,
  and deleting suspended tickets](https://support.zendesk.com/hc/en-us/articles/4408893392922)
- Support tip: [What does "Detected
  as spam" mean?](https://support.zendesk.com/hc/en-us/articles/4408832769306)

## Turning on sender authentication

SPF, DKIM, DMARC, and ARC alignment, also referred to as *sender
authentication*, is managed on the Email page in Admin
Center.

Note: Sender authentication is always turned
on for agents, regardless of any selections made at the
account level, and cannot be turned off.

**To turn on sender authentication**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Talk and email > Email**.
2. In the Email settings section, select **Authenticate
   emails received with SPF, DKIM, and DMARC
   alignment**.
3. Select an option: **Minimal**, **Native traffic**,
   or **Native and forwarded traffic**.

   Zendesk
   recommends turning on this feature for **Native
   traffic** first, then testing to ensure that
   **Native and forwarded traffic** isn't
   suspending traffic that should arrive with
   authentication verified.

   - **Minimal**: Basic protection across your
     Zendesk account that protects both native and
     forwarded email, suspending only emails that are
     blatant spoof attempts.
   - **Native traffic**: DMARC authentication is
     supported for emails sent directly to native
     Zendesk support addresses by end users.
   - **Native and forwarded traffic**: Zendesk
     runs authentication checks on email traffic
     forwarded to Zendesk, leveraging ARC headers and
     authentication results from the forwarding
     address.
4. Click **Save**.

Emails that don't pass this type of authentication are suspended. You can
view them in your [Suspended tickets
view](https://support.zendesk.com/hc/en-us/articles/4408893392922). Tickets suspended for failing to pass authentication
have *Failed email authentication* as the cause of suspension.
Be very careful recovering these, as they may not be from the sender
listed in the email.

## Checking for suspensions

After you turn on this feature, it's important to monitor your [Suspended tickets view](https://support.zendesk.com/hc/en-us/articles/4408893392922)
regularly for suspensions. Emails that are suspended indicate an
issue with the sender’s authority or possibly with your
auto-forwarding workflow. We advise correcting the workflow rather
than turning off the feature.

**To check your Suspended tickets view**

- In Zendesk Support, click the **Views** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/views_icon.png)) icon in the
  sidebar and then click the **Suspended tickets**
  view.

  You can arrange the view by **Cause of
  suspension** to make identifying issues
  easier.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/suspended_tickets_view.png)

If you find that many emails are suspended, turn off this feature
temporarily and contact your domain admin or provider. This is an
indication that your forwarding workflow may need to be examined and
corrected. You may also need to contact [Zendesk Customer
Support](https://support.zendesk.com/hc/en-us/articles/4408843597850).
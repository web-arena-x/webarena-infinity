# Enabling anyone to submit tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408881989018-Enabling-anyone-to-submit-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Enable anyone to submit support tickets by setting your instance to open. Choose between allowing unregistered users to submit tickets without email verification or requiring registration for added security. Unregistered users can still register later to access help center features. Adjust settings to manage ticket submissions and user registration according to your support needs.

Location:  Admin Center > People > Configuration > End users

You can configure your Zendesk Support instance to be open, closed, or restricted (see [Understanding options for end-user access and sign-in](https://support.zendesk.com/hc/en-us/articles/4408887573274-Configuring-how-end-users-access-and-sign-in-to-Zendesk-Support)). This
article describes how to set up an *open* Zendesk Support instance, so that any user can
see your help center and submit support requests.

This article contains the following sections:

- [Understanding what an open Zendesk
  Support instance means](#topic-1__ul_l2w_x13_4y)
- [Anybody can submit tickets, no registration
  required](#topic_5m2_5qm_mj)
- [Anybody can submit tickets, registration
  required](#topic_zcm_vqm_mj)

Related articles:

- [Permitting only added users to submit tickets](https://support.zendesk.com/hc/en-us/articles/4408883658906)
- [Permitting only users with approved email addresses to submit
  tickets](https://support.zendesk.com/hc/en-us/articles/4408893912986)

## Understanding what an open Zendesk Support instance means

Not requiring registration means that all of your users are *unverified* (users are
not prompted to verify their email addresses), which is fine if you don't need or want your
users to visit and use your help center (for example, see [Setting up to provide email-only support](https://support.zendesk.com/hc/en-us/articles/4408888722842)). Registered users are *verified*,
meaning that they (or you) have verified their email addresses and user accounts have been
created.

Even though you don't require users to register, your users still have the option of
registering and creating a login to use your help center, unless you modify your help center
to hide the **Sign Up** and **Login** pages.

If you would like to provide open support, you have two options: registered or unregistered
end-users. You can add users or they can add themselves.

Keep in mind that if your settings allow anyone to submit tickets, any visitor to your site
can register while submitting a support request. This means they'll be able to access Help
center content restricted to signed-in users. For more information, see [Configuring how end-users access and sign in to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408887573274).

## Anybody can submit tickets, no registration required

You can permit any user to submit a ticket without registering. If you don't require
registration, users do not receive the welcome email, which prompts them to verify their
email address and create a password so that they can sign in to your help center. Instead,
they get an email notification that their request has been received:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/unregistered_user_new_ticket_notify.png)

Note: When the [criteria for the placeholder suppression rules are
met](https://support.zendesk.com/hc/en-us/articles/4408833443226-Understanding-placeholder-suppression-rule#topic_qzn_wt1_wmb), certain placeholders, such as the end user's initial comment, are not
included in the email notification.

If you don't want your users to visit your help center, because you provide support via
email only for example, you can remove the link to the ticket that is contained in the
triggers that are used to send email notifications when tickets are received and updated
(see [Removing ticket links from your notifications](https://support.zendesk.com/hc/en-us/articles/4408888722842#topic_nha_nls_yb)).

If you leave the ticket link in the email notifications, the user has the option of
clicking the link to register and create a password so that they can sign in and use your
help center and track their existing tickets, submit new support requests, and so on. If a
registered end-user submits a ticket without signing in, it will be flagged (see [About flagged tickets from registered users who are not
signed-in](https://support.zendesk.com/hc/en-us/articles/4408843002650)).

**To allow anybody to submit tickets, no registration required**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > End users**.
2. In the **Anybody can submit tickets** section, select **Enabled**.
3. If you use the Zendesk API to let users submit tickets, make sure **Require
   authentication for request and uploads APIs** is not selected.

   See [Creating anonymous requests](https://developer.zendesk.com/documentation/ticketing/managing-tickets/creating-and-managing-requests/#creating-anonymous-requests) in the developer
   docs.
4. Make sure **Ask users to register** is not selected.

   This option is not visible
   if you haven't activated your help center yet.
5. Click **Save tab**.

If you want to allow end-users to add attachments to their requests, see [Enabling attachments in tickets](https://support.zendesk.com/hc/en-us/articles/4408832757146).

## Anybody can submit tickets, registration required

When you require your users to register, the support request workflow changes. Rather than
the user's support request immediately becoming a ticket, it is held in limbo until the
users (or you) have verified their email address. After verification, the ticket is added to
your Zendesk.

Note: Verifying users is described in [Verifying a user's email address](https://support.zendesk.com/hc/en-us/articles/4408886752410).

The registration workflow is described in [Options for end-user registration](https://support.zendesk.com/hc/en-us/articles/4408887573274#topic_rdm_jkx_53).

**To allow anybody to submit tickets and require registration**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > End users**.
2. Select **Anybody can submit tickets**
3. Select **Ask users to register**.
4. Click **Save Tab**.

If you want to allow end-users to add attachments to their requests, see [Enabling attachments in tickets](https://support.zendesk.com/hc/en-us/articles/4408832757146).
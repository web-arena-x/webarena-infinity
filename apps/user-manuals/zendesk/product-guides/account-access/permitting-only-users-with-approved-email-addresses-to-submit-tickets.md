# Permitting only users with approved email addresses to submit tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408893912986-Permitting-only-users-with-approved-email-addresses-to-submit-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location:  Admin Center > People > Configuration > End users

You can configure your Zendesk Support instance to be open, closed, or restricted (see [Understanding options for end-user access and sign-in](https://support.zendesk.com/hc/en-us/articles/4408887573274)). This article describes how to set up a *restricted* Zendesk Support
instance, so you can control end-user access through approved email domains.

This means that your Help Center is visible to all users, but only users with email addresses
in domains that you approve can register and submit support requests. Any unapproved user’s
support request will be either be completely rejected or sent to the Suspended Tickets
queue.

This article contains the following sections:

- [Enabling the 'Anyone can submit tickets' option](#topic_xlc_z1k_jj)
- [Requiring users to register](#topic_iv2_zmj_2z)
- [Restricting access using the allowlist and blocklist](#topic_rpw_bbk_jj)

## Enabling the 'Anyone can submit tickets' option

In a restricted Zendesk Support instance, you enable the option to allow anyone to submit
tickets and then use the allowlist and blocklist to accept or reject those requests.

**To enable the 'Anyone can submit tickets' option**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > End users**.
2. Select the **Anybody can submit tickets** option.
3. Click **Save tab**.

## Requiring users to register

After you enable the **Anyone can submit tickets** option, you can also require your
users to register.

Requiring registration means that your users must verify their email addresses and also
create a password to submit requests. Unverified users' requests are suspended. If you don't
require registration, you can still allow users to register using the **Sign Up** link in
your Help Center. users still have the option of registering themselves.

**To require that your users register**

- Select the **Ask users to register** option, which is displayed when you select the
  **Anyone can submit tickets** option.

  Note: This option is not available until you enable Guide (see [Getting started with your help center](https://support.zendesk.com/hc/en-us/articles/4408846795674)).

## Restricting access using the allowlist and blocklist

After you enable the **Anyone can submit tickets** option, the **allowlist** and
**blocklist** also appear. You use these to specify the email domains that are either
allowed to or prevented from registering and submitting support requests.

For details about using the allowlist and blocklist, see [Using
the allowlist and blocklist to control access to Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408886840986).
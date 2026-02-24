# Setting the password security level

Source: https://support.zendesk.com/hc/en-us/articles/4408822149018-Setting-the-password-security-level

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Enhance account security by setting password security levels to Recommended for both team members and end users, ensuring strong password requirements. You can customize security settings for team members if needed. Consider enabling session expiration and following password best practices to protect sensitive information. Avoid allowing administrators to set passwords to reduce security risks.

Location:  Admin Center > Account
> Security

A password security level refers to the strength or complexity of a password.
Zendesk provides the following levels of password security: Recommended,
High, Medium, and Low.

You can set one password security level for end users and a different
one for
team members. You can also create a custom password security level for
team
members (admins and agents) if your requirements differ for these users.

Zendesk strongly suggests setting the Recommended password security level
for
both team members and end users. This security level is configured with
strict password requirements, checks against known breached passwords,
and
is based on security best practices and industry standards.

Note: You can use a
 [single sign-on (SSO) solution](https://support.zendesk.com/hc/en-us/articles/4408883587226)
instead of Zendesk passwords. Zendesk recommends using SSO, if possible,
to
prevent users from setting weak passwords that can put their accounts
at
risk.

This article covers the following topics:

- [About password security levels](#topic_j41_j4r_2j)
- [Changing the password security level](#topic_tcn_ppr_2j)
- [Setting a custom password security level for team members](#topic_ncf_twp_jzb)

## About password security levels

Many organizations require complex passwords as part of their security
policies. Certain regulations, such as the General Data Protection
Regulation (GDPR), require organizations to take steps to ensure
the
security of personal data, which includes using complex passwords.

Zendesk strongly suggests setting the Recommended password security
level
for both team members and end users to safeguard your account.

When the Recommended password security level is in place, passwords
do
not expire. However, passwords must meet the following
requirements:

- Must be at least 12 characters
- Must include uppercase and lowercase letters (a-z and
  A-Z)
- Must include a number (0-9)
- Must include a special character (!, @, #, %, etc.)
- Must not include the word "Zendesk"
- Must not resemble an email address
- Must pass a check against a list of known breached
  passwords
- Five attempts are allowed before a temporary 10-minute
  lockout

The Low, Medium, and High password security levels have lower security
requirements. Zendesk recommends
[changing the security level](#topic_tcn_ppr_2j)
to
Recommended if you are using any of these other levels.

You can review the password requirements for the currently selected
security level on the team member or end user authentication
page.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/security_password_level_require.png)

The Custom security level is available only for team members and
can be
used if the Recommended password security level doesn't meet your
requirements. If you create your own password policy, ensure the
requirements are at least as strong as the Recommended level. See
[Setting a custom password security level for team members](#topic_ncf_twp_jzb).

Note: Zendesk enforces a 72-character
limit for all
passwords. The limit on password length is a reliability measure
to
prevent a form of DoS attack called “long password denial of
service.” To learn more about Zendesk security practices, visit our
[Security
website](https://www.zendesk.com/product/zendesk-security/).

## Changing the password security level

You must be an administrator to change the password security level.
When
you increase the security level (for example, Medium to
Recommended), all passwords, regardless of security level, are set
to expire in 5 days. All end users and team members must change
their passwords to comply with the new security level.

Increasing the password security level can cause some passwords to
expire
instantly. If a password is older than 90 days and the security
level is increased to a level with an expiration restriction, that
password is considered expired. Zendesk sends email notifications
to
administrators and agents three days before a password expires, and
then on the day it expires.

If you change the security level from Low, Medium, or High to either
Recommended or Custom, you can't revert back. You can change between
the Low, Medium, and High levels and revert back if needed.

**To change the password security level**

1. Open the password security settings for team members
   or end users.
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
     **Account** in the sidebar, then select **Security > Team member
     authentication**.
   - In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
     **Account** in the sidebar, then select **Security > End user
     authentication**.

     The end-users option is not available until
     you
     [set up and activate your help
     center](https://support.zendesk.com/hc/en-us/articles/4408846795674).
2. Select a **Password level**, then click
   **Save**.
3. If the Low, Medium, or High password security level was
   previously set and you are changing to Custom or
   Recommended, click **Save** to confirm
   that you
   understand the previous levels will no longer be
   available.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/security_password_level_switch.png)

## Setting a custom password security level for team members

If the Recommended password security level doesn't meet your company's
specific requirements for team members, you can create a custom
password security level.

Note: Changes to a custom password
security
policy won't impact expiration rules for existing passwords.
For example, if you change your password expiration from
**30 days** to
**Never**, passwords for
current users will still expire after 30 days. When they
reset their password, the new expiration rule is applied.

Most of the custom options are self-explanatory except for the
following:

- **Number of previous passwords to reject**
  - New passwords
  must be different from the number of previous passwords you
  set.
- **Failed attempts until lockout** -
  If an end user or agent
  fails to enter their password correctly the number of times
  you specify in a row, they are locked out for a certain
  period of time. They cannot sign in again until the lockout
  expires.
- **Password can resemble email** - Controls
  whether new
  passwords can include parts of an email address. For
  example, when this setting is **No**,
  a user with a
  david@mycompany.com email address cannot include the word
  **david** as part of their password.

**To set a custom password security level for team members**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Team member
   authentication**.
2. Select **Custom** in the
   **Password level**
   drop-down.
3. Click the **Edit** link to set
   password
   requirements.
4. Select your custom password requirements.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/admin_center_custom_passwords4.png)
5. Click **Set**.
6. Click **Save**.
7. If the Low, Medium, or High password security level was
   previously set for team members, you'll receive a
   message that these levels will no longer be
   available. Click **Save** to confirm.
# Resetting user passwords

Source: https://support.zendesk.com/hc/en-us/articles/4408831970202-Resetting-user-passwords

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Admins can reset user passwords by sending a reset email, allowing users to update their passwords securely. If single sign-on (SSO) is enabled, this option isn't available. If needed, account owners can enable admins to manually reset passwords. Avoid manually setting passwords due to security risks.

Admins can reset a user's password by sending a reset email to the user's
registered email
address. The email contains a link that lets the user reset their password.
Only
administrators can send the reset email.

If account owners have allowed it, admins can manually set passwords
for users. However, this
is not recommended as a security best practice. You should use the email
reset workflow
instead of setting passwords manually.

This article contains the following topics:

- [Sending a link to reset a user's password](#topic_j1j_mpy_xgc)
- [Manually setting passwords for
  users](#topic_ovj_mvf_fhc)

## Sending a link to reset a user's password

Admins can reset a password for an admin, agent, or end user by sending
a reset email to
the user's registered email address. The email contains a link that
lets the user reset
their password. Only admins can send the reset password email.

Note: If single sign-on (SSO)
is used, admins can't send password-reset links to
users.

**To reset a team member's password**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.
2. Find the agent's name, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png))
   on that row, and select
   **Manage in Support**.
3. On the user's profile page, click the
   **Security Settings** tab and click
   **Reset** in the Password section.

   Note: The password reset email
   is sent from the
   [agent brand](https://support.zendesk.com/hc/en-us/articles/4408829476378#topic_hyq_l1v_cr)*if*
   that brand has an active help center; otherwise, the email
   is sent from the
   account's oldest brand with an active help center.

**To reset an end-user's password**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Customers**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)) in the sidebar.
2. Locate the user who forgot their password, then click the
   user's name.
3. On the user's profile page, click the
   **Security Settings** tab and click
   **Reset** in the Password section.

### About password reset requests sent to end users in email

In certain situations, Support may not be able to send the password
reset email to an end
user's primary email address. Instead, it will send a
*reset email* to the end user’s
secondary email address that directs them to contact your company
directly so they can
verify their identity and reset their Support password.

The email looks like this:

```
You need to verify your email address to reset your password. Contact [company name] at [email address] to fix this.

If this wasn't you, contact [company name] at [email address].
```

This may occur when the following criteria are met:

- [Single sign-on (SSO)](https://support.zendesk.com/hc/en-us/articles/4408883587226)
  is disabled.

  If SSO is
  turned on, you can't send password-reset links to end
  users.
- The end user’s primary email address is undeliverable.
- The end user has a secondary email address.
- The end user submitted a request via email to reset their
  primary email
  address.

After the end user receives the reset email, you and the end
user need to
complete these steps:

1. The end user verifies their secondary email address or changes
   their primary
   email address.
2. An agent manually resets the end user’s password or updates
   their email address on
   file.

   Resetting passwords for end users is different from
   [setting passwords for users](#topic_ovj_mvf_fhc).
   Even if
   admins don't have permission to set passwords for users,
   they can still send end users
   password reset emails.

## Manually setting passwords for users

Account owners can allow admins to manually set passwords for users.
However, Zendesk
recommends that you not activate this option for security reasons.

### Recommendation and best practice for this setting

Zendesk recommends that you not activate the option for admins
to manually set passwords
for security reasons. It prevents hackers from using social engineering
techniques to
deceive well-meaning people into providing confidential information.

For example, one technique used by hackers is to repeatedly call
or spoof-email a support
center posing as a frustrated customer who forgot their password
and is unable to recover
it, and persisting until an agent has no choice but to change
the password manually for
the irate customer. Once the password is changed, the hacker
has access to confidential
information.

Rather than allow admins to set passwords for users, it is best
to allow users to
leverage user registration, change password and forgot password
flows to manage their own
passwords so admins never have access to a user's password.

### Allowing admins to set passwords

Account owners can allow admins to set passwords for users. Remember,
Zendesk recommends
that you not activate this option for security reasons. You must
be an account owner to
allow admins to set passwords.

**To allow admins to set passwords for users**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)
   **Account** in the sidebar, then select **Security > Advanced**.
2. On the **Passwords** tab, select
   **Enable admins to set passwords**.

   You must
   be the account owner to see this setting.
3. Click **Save**.

   When the admins sets passwords for users, users receive
   an email
   letting them know the administrator has set their password.

### Setting passwords for users

If allowed by the account owner, admins can manually set passwords
for users.

You can also set user passwords through the API (see
[Set a User's Password](https://developer.zendesk.com/api-reference/ticketing/users/user_passwords/#set-a-users-password)
in the developer docs).

**To set a team member's password**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Team members**.
2. Find the agent's name, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png))
   on that row, and select
   **Manage in Support**.
3. On the user's profile page, click the
   **Security Settings** tab and click
   **Set** in the Password section.
4. Enter a new password for the user.
5. Click **Save**.

**To set an end user's password**

1. In [Support](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Customers**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)) in the sidebar.
2. Locate the user who forgot their password, then click
   the user's name.
3. On the user's profile page, click the
   **Security Settings** tab and
   click
   **Set** in the Password section.
4. Enter a new password for the user.
5. Click **Save**.
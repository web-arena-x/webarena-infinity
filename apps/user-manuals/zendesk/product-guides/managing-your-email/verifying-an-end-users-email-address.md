# Verifying an end user's email address

Source: https://support.zendesk.com/hc/en-us/articles/4408886752410-Verifying-an-end-user-s-email-address

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

When you have an activated help center, verification emails are sent to users who register.
Ideally, users will verify their email address as soon as they receive the verification email message, but agents can also verify an end user's email address on the user's behalf.

If you require users to [register before submitting a request](https://support.zendesk.com/hc/en-us/articles/4408893912986#topic_iv2_zmj_2z), but a user doesn't verify their email address, they won't be able to create a password to sign in to your help center to submit a request. Any support requests submitted by the unverified user through email will remain in limbo in the Suspended tickets view. The ticket won't appear in your other views, and an agent cannot work on it.

This article covers the following topics:

- [Verifying a user's email address on their behalf](#topic_ryz_p4g_b2b)
- [When to verify for users](#topic_fcq_ggg_b2b)
- [Identifying unverified email addresses](#topic_fy2_tsh_15b)

## Verifying a user's email address on their behalf

Agents and admins can verify a user's email address on their behalf.
Agents can verify end-user accounts only. Admins can verify all users except the account owner.

You can also [resend the verification email](https://support.zendesk.com/hc/en-us/articles/4408832398618) so that the user can verify their own email address. Or you can verify user email addresses when adding users via the API (see [Zendesk API: Users](https://developer.zendesk.com/api-reference/ticketing/users/users/)).
In that case, you might want to disable verification emails for users (see [How can I disable end user verification emails?](https://support.zendesk.com/hc/en-us/articles/4408885856538)).

Note: The options for verifying email addresses are not available until you [activate your help center](https://support.zendesk.com/hc/en-us/articles/4408846795674#topic_ckn_wc4_qy).

**To verify a user's email address on their behalf**

1. After you add the user (see [Adding end users](https://support.zendesk.com/hc/en-us/articles/4408893585178)), open the [user's profile](https://support.zendesk.com/hc/en-us/articles/4408822762650).
2. Click the down arrow next to the user's email address and select **Verify Now**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_verify_now.png)

The user's email address is immediately verified. If the user has submitted any support requests, those requests are *not* automatically added as tickets to views but can be manually recovered from suspended tickets.

After the user's email address has been verified, you may also want your users to have a password. The password is required if users want to sign in to your help center. Like email verification, the user should create their own password. However, you can create passwords for them. You must be an administrator to use either of these options:

- Reset the password in the Security tab of the user's profile (see [Resetting user passwords](https://support.zendesk.com/hc/en-us/articles/4408831970202).)
- Use the Zendesk API (see [Zendesk API:
 Users](https://developer.zendesk.com/api-reference/ticketing/users/users/))

## When to verify for users

If your Zendesk Support is configured to require users to register, each user must create an account, verify their email address, and also create a password. You may want to verify for your users in these cases:

- **Testing** - You are testing your workflow, and you want to create test users and tickets to test automations and triggers. You can add some test users for email accounts that you own and easily verify those new users.
- **Adding Agents or Known Users** - When adding new agents (or other known users) to your account because you know that their email addresses are legitimate, you can verify them as you add them.

## Identifying unverified email addresses

If a user doesn't have a verified primary email address, a warning icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/suspended_icon.png)) is displayed next to the email address on the **Customers** page. If you hover over the icon, you’ll see the text “Unverified email.”

![Suite all](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/announcement_tag_2.png)

If an email address is unverified and owned by an existing user with a verified primary address, Zendesk flags the ticket with **User has yet to confirm ownership of the address used to deliver this email**. If you aren't certain the email was sent from that user, consider [resending a verification email](https://support.zendesk.com/hc/en-us/articles/4408832398618), reassigning the ticket to a security group for review, or solving the ticket with due caution.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_unverified_user_flag.png)

You can search for unverified primary email addresses by searching on the **Customers** page using the **is\_verified** term. For example:

- **is\_verified:false Sunita** returns all users named Sunita with an unverified primary email address
- **is\_verified:true** returns all users with a verified primary email address
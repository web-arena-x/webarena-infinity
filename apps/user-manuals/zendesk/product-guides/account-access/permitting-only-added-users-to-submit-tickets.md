# Permitting only added users to submit tickets

Source: https://support.zendesk.com/hc/en-us/articles/4408883658906-Permitting-only-added-users-to-submit-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center > People > Configuration > End users

You can configure your Zendesk Support instance to be open, closed, or restricted (see [Understanding options for end-user access and sign-in](https://support.zendesk.com/hc/en-us/articles/4408887573274)).

This article describes how to set up a *closed* instance, so that your Help Center is visible to everyone but only the users that you add to your Zendesk account can sign in and submit support requests. Each user's account must be created before they can sign-in and submit support requests.

Closed Zendesk Support, by default, has the following access rules:

- Your Help Center is visible to all visitors, whether they are signed in or not.
- Only verified users you have added to your Zendesk account can submit support requests through the Help Center. Unverified users that have been added to the account can verify themselves by going to the Help Center and requesting a password.
- Both verified and unverified users you have added to your Zendesk account can submit support requests via email to your Zendesk Support address.
- If you have a knowledge base, access is determined by the rules applied to it, as described in [Restricting access to knowledge base content](https://support.zendesk.com/hc/en-us/articles/4408824005914).

This article contains the following sections:

- [Disabling the 'Anyone can submit tickets' option](#topic_h1t_z42_h3)
- [Adding users to the closed Zendesk Support](#topic_xwj_jpn_f3)
- [About new user email address verification and passwords](#topic_m25_3ld_hj)
- [Restricting your content to signed-in users only](#topic_2kg_qct_f3)

## Disabling the 'Anyone can submit tickets' option

In a closed Zendesk you disable the option to allow everyone, even visitors who are not signed in, to submit tickets. This means that you have complete control over who uses Zendesk Support. Typically, you'll set up Zendesk Support in this way by adding all your users yourself. Although, there is a way for an anonymous user (someone not already added to Zendesk Support) to still submit support requests and have your agents approve of the request, add the user to Zendesk Support, and add the support request as a ticket to your queue (see [When anonymous users submit support requests](#topic_qpm_rs2_hj)).

**To disable the 'Anyone can submit tickets' option**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > End users**.
2. If it's selected, deselect the **Anybody can submit tickets** option.

   Note: Deselecting this option can impact Web Widget functionality (see [Using restricted Help Center content with Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408843923610)).
3. Optionally, in the **Account emails** section, select the **Also send a welcome email when a new user is created by an agent or administrator** option. For more information, see [About new user email address verification and passwords](#topic_m25_3ld_hj).
4. Click **Save tab**.

The settings you've just made removes the **Sign Up** link from the sign-in window of your Help Center.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sign_up_dialog.png)

This means that users who access Zendesk Support have no option for self registering (signing up and creating an account). This includes your agents as well. You need to add all your users yourself.

If you also restrict all your content to either agents or signed-in users only (see [Restricting your content to registered users only](#topic_2kg_qct_f3) below), the only page that visitors see when they access your Help Center is the sign-in page and, if they don't already have a user account in your Zendesk, they are unable to sign in.

## Adding users to a closed Zendesk Support

When Zendesk Support is closed, and restricted to only users you add, you need to add the users yourself. Here are the following ways you can add users:

- Manually adding users one at a time (see [Adding end users](https://support.zendesk.com/hc/en-us/articles/4408893585178) and [Adding agents and admins](https://support.zendesk.com/hc/en-us/articles/4408886939930))
- Adding many users in a bulk import (see [Bulk importing users and organizations](https://support.zendesk.com/hc/en-us/articles/4408893496218))
- Adding users via the Zendesk API (see [Zendesk API: Users](https://developer.zendesk.com/api-reference/ticketing/users/users/))

By default, when you add a user to your Zendesk, they are unregistered (and therefore unverified). At this stage, they can submit support requests via your support email address, but not through the Help Center. When they register themselves, they become verified users of Zendesk Support, and can submit support requests through both the email address and the Help Center.

The following section explains how email verification works and how user passwords are created when adding users.

## About new user email address verification and passwords

Since you're adding your users yourself, rather than allowing them to sign themselves up, you need to think about how the verification process happens. This is where the *Also send a welcome email when a new user is created by an agent or administrator* option can be helpful. If you set this option, all users you add to Zendesk Support receive the User welcome email message, which prompts them to click a link to verify their email address and then create a password so that they can sign in to your Zendesk. If you want new users to be able to sign in to your Help Center, they each need a password. So by enabling this option you're asking your users to manage email address verification and create passwords themselves.

If you don't want your users to receive the verification email message, don't select *Also send a welcome email when a new user is created by an agent or administrator*.
However, if you decide not to send the verification email, your users' email addresses aren't verified and they can't create passwords or sign in to your Help Center .

Note: Unverified users can still submit support requests to Zendesk Support via email, and these requests are handled in the same way as those submitted by verified users.

When you add your users, you have the following options for email verification and passwords if you elect not to send the User welcome email.

- You can tell your users to send support requests via email using your support email address (for example, support@*mycompany*.zendesk.com).
- Using the Zendesk API, it's possible to both add new users and to also set their passwords. You can automatically verify all your users' email addresses using the API `verified` parameter. This means that your users will be fully registered and verified. Assuming you also provide them with their passwords, they can immediately sign in to your Help Center. For more information, see [Zendesk API: Users](http://developer.zendesk.com/documentation/rest_api/users.html).
- You can manually verify a user's email address after you've added them to your Zendesk. See [Verifying a user's email address](https://support.zendesk.com/hc/en-us/articles/4408886752410) in the Zendesk Agent Guide.

### When anonymous users submit support requests

Despite your Zendesk Support being closed, it is possible for an agent to create a ticket from a support request from an anonymous user. When you receive a support request from an anonymous user, when you've configured Zendesk Support as closed, the request is added to the Suspended Tickets view. From there an agent can either delete the request or recover it. Recovering the ticket creates a new user account and adds the ticket to your Zendesk.
For more information, see [Viewing, recovering, and deleting suspended tickets](https://support.zendesk.com/hc/en-us/articles/4408893392922) in the Zendesk Agent Guide.

If you send a verification email when a new user is created by an agent or administrator, the User welcome email is sent to the user when the suspended ticket is recovered. The user clicks the link to verify their email address, creates a password, and is then signed in to your Help Center where they can use the knowledge base and submit and track requests.

If you don't send a verification email when a new user is created by an agent or administrator, the user remains unverified and can't sign in. The user receives the ticket received notification, and can respond to the notification via email.

### Using enterprise single sign-on (SSO)

If you're using JWT or SAML for user access to Zendesk Support, all user management and authentication happens outside of your Zendesk. Your single sign-on service is synced with Zendesk Support. So, for example, if you add a user account for a new employee, that employee has immediate access to your Zendesk.

When using SSO with a closed Zendesk Support, a few issues may arise. What happens if a user sends an email support request and they're not already a user within the closed Zendesk Support? The user's email support request will be suspended. In other words, if the user doesn't already exist in Zendesk Support, synced to it via your single sign-on service, then the user cannot submit support requests. Only known, legitimate users in your user management system will be able to access the closed Zendesk Support.

You also don't want to select the *Also send a verification email when a new user is created by an agent or administrator* option because you never want to users to create passwords directly in Zendesk Support. Remember that's all handled outside of your Zendesk.

It's important to remember that social media single sign-on is different. These provide your users with additional ways to sign in to your Zendesk. To use them, your users need to add these social media accounts to their user profiles themselves. You can't do it for them.

## Restricting your content to signed-in users only

When you close or restrict Zendesk Support, you also may want to hide all content in your Help Center so that only signed-in users can see it. To do this, you can require that users sign in to access your Help Center (see [Restricting Help Center access to signed-in users](https://support.zendesk.com/hc/en-us/articles/4408842656154)).

When all your content is restricted to signed-in users, visitors to your Help Center will only see the sign-in page. The users you added to your Zendesk can sign in there and access your content.
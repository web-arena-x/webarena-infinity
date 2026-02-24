# Managing end user settings

Source: https://support.zendesk.com/hc/en-us/articles/4408883052442-Managing-end-user-settings

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

On the End users configuration page, you can select the settings that affect how your users access
and use Zendesk. For example, if you want your Zendesk account to be
available to anyone, you can choose the setting to allow anybody to submit
tickets. This setting, and related end user settings, determine how open or
restricted Zendesk is to your end users.

This article covers the following topics:

- [Accessing and
  managing end user settings](#topic_mdp_4p5_rfc)
- [Selecting who can
  submit tickets](#topic_vbt_qsv_kj)
- [Using CAPTCHA to control spam tickets](#topic_snk_s21_w4b)
- [Requiring authentication for the Requests and Uploads API endpoints](#topic_nmz_421_w4b)
- [Requiring that your
  users register to use Zendesk](#topic_yzr_ssv_kj)
- [Controlling access
  to Zendesk Support with the email allowlist and
  blocklist](#topic_f2l_gtv_kj)
- [Registration
  message and verification email
  notifications](#topic_kpm_ktv_kj)
- [Sending the email
  verification message to users you add](#topic_kbl_nqr_lj)
- [Allowing your end
  users to edit their profiles and change their
  passwords](#topic_5gf_4tv_kj)
- [Validating phone
  numbers](#validate_phone)
- [Enabling user
  tagging](#topic_3gm_rtv_kj)

## Accessing and managing end user settings

You can configure end user access to your Zendesk account for the
following:

- Anybody can submit tickets and no registration or email
  verification is required. Users must prove that they
  are human based on CAPTCHA requirements.
- Anybody can submit tickets using the Zendesk API as long as the endpoint of
  the ticket is authenticated.
- Anybody can submit tickets but you also require
  registration and email address verification.
- Anybody can submit tickets but you restrict access to
  your Zendesk account based on email domains or IP
  restrictions. In other words, you only accept
  registration and tickets from approved users.
- Only users you add to your Zendesk account can
  submit tickets and use your help center.

There are variations of these configurations as well. For example, you
can allow anybody to submit tickets, require registration, and also
restrict access using email domains or via IP restrictions. These
configurations are also affected by using both social media and
enterprise single sign-on (see [Single sign-on (SSO) options in
Zendesk](https://support.zendesk.com/hc/en-us/articles/4408883587226)).

**To manage end user settings**

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
  **People** in the sidebar, then select **Configuration > End users**.

## Selecting who can submit tickets

The *Anybody can submit tickets* setting is one of the most
important end user settings because it determines which users can
access and use Zendesk. You can allow anybody to use your Zendesk
account, close it to all but the users you add, or restrict the use
of your Zendesk account to just users from specific email domains or
within a range of IP addresses. These configuration options are
referred to as *open*, *closed*, and *restricted* and
are explained in detail in the following articles:

- [Enabling anyone to submit tickets
  in Zendesk Support (open)](https://support.zendesk.com/hc/en-us/articles/4408881989018)
- [Permitting only added users to
  submit tickets (closed)](https://support.zendesk.com/hc/en-us/articles/4408883658906)
- [Permitting only users with
  approved email addresses to submit tickets
  (restricted)](https://support.zendesk.com/hc/en-us/articles/4408893912986)

## Using CAPTCHA to control spam tickets

The first is the [use of
CAPTCHA](#topic_snk_s21_w4b), which is automatically enabled when you
allow anyone to submit tickets. When anybody can submit tickets,
CAPTCHA is used to protect your account. That means users who are
not signed in may be prompted to complete a verification test before
they can submit a ticket.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/captcha_request2.png)

Allowing anybody to submit tickets might lead to some spam email
appearing as tickets in your Zendesk account. Requiring users who
are not registered and signed in to confirm they're human before
they can submit a ticket goes a long way to prevent spam. Zendesk
uses [Cloudflare's bot detection
and management software](https://www.cloudflare.com/products/bot-management/) to prevent bots and malicious
traffic. Most users can simply confirm they're human without having
to solve a CAPTCHA. A risk analysis engine predicts whether the user
is a human or an abusive agent. If the engine isn't sure, it
displays a CAPTCHA that the user must solve before they can submit a
ticket.

CAPTCHA is enabled by default, including on the Sign Up page, and can't
be disabled. CAPTCHA is not currently available with the Web
Widget.

## Requiring authentication for the Requests and Uploads API endpoints

If you're receiving spam from the Requests ([/api/v2/requests](https://developer.zendesk.com/rest_api/docs/support/requests)) and
Uploads ([/api/v2/uploads](https://developer.zendesk.com/rest_api/docs/support/attachments#upload-files)) API
endpoints, you can turn on the *Require authentication for
requests and uploads APIs* setting.

When this setting is turned on, authentication is required for these
endpoints. When this setting is turned off, [anonymous requests](https://developer.zendesk.com/documentation/ticketing/managing-tickets/creating-and-managing-requests/#creating-anonymous-requests) are
allowed. Other endpoints are not affected by this setting.

Although it's highly effective at preventing spam, requiring
authentication makes it harder for end users to open tickets
anonymously. Some methods of ticket creation, such as the Zendesk
Web Widget Contact form, custom apps, and external web forms, rely
on the unauthenticated anonymous ticket creation process to submit
tickets. Requiring authentication for the Requests and Uploads
endpoints will prevent the creation of anonymous tickets from these
sources. The *Require authentication for requests and uploads
APIs* setting is turned off by default and can only be
turned on in Admin Center.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/support_customer_settings_require_auth_apis.png)

## Requiring that your users register

The default configuration of the help center displays the Sign Up page
and allows your users to optionally create a user account. To
require users to register and create an account, enable the *Ask
users to register* setting. When creating an account, the
user's email address must be verified. Until it is, any support
requests they make (via the support request web form, the Web
Widget, or email) will be suspended and will not be added to your
Zendesk views.

Note: This option is not available until you enable your help center
(see [Getting started with your help
center](https://support.zendesk.com/hc/en-us/articles/4408846795674)).

To learn more about the registration process and the advantages of
requiring registration, see [Options for end-user registration](https://support.zendesk.com/hc/en-us/articles/4408887573274#topic_rdm_jkx_53).
If you don't want users to register, you can hide the Sign Up page.
See [Removing sign-in links from your knowledge
base](https://support.zendesk.com/hc/en-us/articles/4408888722842#topic_odm_ans_yb).

## Controlling access to Zendesk Support with the email allowlist and blocklist

When anybody can submit tickets, you can use the allowlist and blocklists
to restrict access to Zendesk Support. For example, you can accept
user registrations and support requests from users who have email
addresses in the email domains you add to the allowlist. You can
then reject all other users by adding an asterisk (\*) to the
blocklist. If you're not setting up a restricted Zendesk, leave both
the allowlist and blocklist blank.

The allowlist and blocklist are explained in more detail in [Permitting only users with approved email
addresses to submit tickets (restricted)](https://support.zendesk.com/hc/en-us/articles/4408893912986).

You can also control access using IP restrictions. See [Restricting access to Zendesk Support and
your help center using IP restrictions](https://support.zendesk.com/hc/en-us/articles/4408894156186).

## Registration message and verification email notifications

The Sign Up page in the help center contains a message prompting users to
fill out the registration form.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/captcha_signin2.png)

You can customize this message on the End users (customers) settings page
by editing the *User registration message*. You can also add
dynamic content to this message. See [Providing multiple language support with
dynamic content](https://support.zendesk.com/hc/en-us/articles/4408882999066).

When your users register they receive a welcome email message (called the
*User welcome email*) that prompts them to verify their
email address and create a password so that they can sign in to your
help center.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/welcome_email.png)

Users receive a similar email message (called the *Email verification
email*) when they add secondary email addresses to their
user profiles. Both of these messages can be customized and both
support dynamic content.

Note: The option to register online is not available until you enable your
help center (see [Getting started with your help
center](https://support.zendesk.com/hc/en-us/articles/4408846795674)).

## Sending the email verification message to users you add

You can also send a welcome email when a new user is created by a team
member. This is the same email message shown in the previous
section. When you add a user yourself you'll probably also want the
user to verify their own email address and then create a password so
that they can sign in to Zendesk. Of course you may not want to
enable this setting since Zendesk offers many access, registration,
and sign-in options, including single sign-on.

See the following topics for a more detailed description of using the
*Also send a welcome email when a new user is created by
an agent or administrator* setting:

- [Permitting only added users to
  submit tickets (closed)](https://support.zendesk.com/hc/en-us/articles/4408883658906)
- [Permitting only users with
  approved email addresses to submit tickets
  (restricted)](https://support.zendesk.com/hc/en-us/articles/4408893912986)

## Allowing your end users to edit their profiles and change their passwords

Users are allowed to view and edit their profile data by default. This
allows your users to add information to their user profiles. For
example, they can add secondary email addresses, their X (formerly
Twitter) account, and so on. You should disable *Allow users to
view and edit their profile data* if you use remote
authentication because your user data is handled outside of your
Zendesk account.

Users are also allowed to change their password by default. You would
normally want your users to be able to change their own passwords,
but should deactivate *Allow users to change their password* if
you administer users and passwords in another system and use remote
authentication.

## Validating phone numbers

With this setting enabled, phone numbers added to user profiles must be
in the internationally standardized E.164 format. E.164 numbers can
have a maximum of fifteen digits and are usually written as follows:
[+][country code][subscriber number including area code]. Numbers
that don't conform to this format won't save to user profiles.

## Enabling user tagging

Enabling user tagging allows you to add tags to a user's profile. These
tags are then added to the user's tickets, which you can then use to
control your workflow. For example, you can use a tag to escalate a
specific user's tickets.

The user does not see the tags that have been added to their profile.

For more information, see [Adding tags to users and
organizations](https://support.zendesk.com/hc/en-us/articles/4408881573658).
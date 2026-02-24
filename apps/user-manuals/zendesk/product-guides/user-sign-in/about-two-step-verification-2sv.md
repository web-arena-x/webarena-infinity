# About two-step verification (2SV)

Source: https://support.zendesk.com/hc/en-us/articles/8197975442330-About-two-step-verification-2SV

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Two-step verification enhances security by requiring a passcode when signing in from a new device. You'll receive a passcode via email, valid for five minutes, to complete the sign-in. If you can't access the passcode, an admin can generate a recovery code. This feature doesn't affect end users and is bypassed with two-factor authentication or single sign-on.

Two-step verification (2SV) is a security protocol that enhances protection by requiring
a passcode when signing in from a new or unrecognized device. It ensures that the
credentials used are associated with a legitimate user.

Two-step verification is active for all accounts using the [standard Zendesk sign-in](https://support.zendesk.com/hc/en-us/articles/4408887573274#topic_v1w_jsl_v3) (email and password)
for team members and cannot be turned off. This feature does not impact end users.

When signing in from a new device, team members are emailed a passcode, which they must
use to complete the sign-in. If [two-factor authentication](https://support.zendesk.com/hc/en-us/articles/4408826974874) is turned on or team members sign
in with single sign-on (SSO), they aren’t prompted for a passcode.

If team members can't retrieve their passcode and can’t sign in to Zendesk, a Zendesk
admin or account owner can [generate a recovery code](https://support.zendesk.com/hc/en-us/articles/8197977742874) to help them regain access to their
account.

This article covers the following topics:

- [Understanding how two-step verification works](#topic_x51_1dh_zcc)
- [Understanding the sign-in experience with two-step verification](#topic_bjj_jhy_1dc)

Related articles:

- [Zendesk In-Product Cookie Policy](https://support.zendesk.com/hc/en-us/articles/4408824378650)
- [General security best practices](https://support.zendesk.com/hc/en-us/articles/4408888782618)

## Understanding how two-step verification works

For added security, Zendesk [tracks the devices](https://support.zendesk.com/hc/en-us/articles/4408834578074) used to access your account using a
cookie named `_zendesk_cookie`. The first time any team member signs
in using the standard Zendesk sign-in (email and password) and passcode, the
application stores the `_zendesk_cookie` on the device.

Zendesk checks the `_zendesk_cookie` when team members sign in. If the
`_zendesk_cookie` doesn't exist or is invalid, Zendesk deems that
device as new and will prompt the agent for a passcode. If the cookie is valid, team
members who have signed in on the device before are not prompted for a passcode.
However, team members who haven’t signed in on the device are prompted for a
passcode.

Additionally, using incognito mode or clearing the browser cache and cookies can
cause Zendesk not to recognize the `_zendesk_cookie`.

When using two-step verification, passcodes are sent to the team member’s [primary email address](https://support.zendesk.com/hc/en-us/articles/6735805091098) listed in their Zendesk profile.
Passcodes expire after five minutes and can only be used once. If team members enter
an invalid or expired passcode, Zendesk emails them a new one.

## Understanding the sign-in experience with two-step verification

This procedure illustrates the typical workflow when team members sign in to Zendesk
from a new or unrecognized device.

1. The team member signs in to their Zendesk account using their email and password
   and clicks **Sign in**.

   If Zendesk doesn’t recognize the device, the
   Two-step verification dialog will appear, instructing the team member to
   retrieve a passcode from their email.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/2SV_passcode_prompt.png)
2. The team member checks their inbox for an email from Zendesk.

   The email
   includes the subject **Zendesk verification passcode** and a passcode
   that’s valid for five minutes.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/2SV_passcode_email.png)
3. The team member pastes the passcode into the **Passcode** field in the
   Two-step verification dialog and clicks **Verify**.

   If the team member
   enters an invalid or expired passcode, Zendesk automatically sends them
   another passcode instead of signing them in.
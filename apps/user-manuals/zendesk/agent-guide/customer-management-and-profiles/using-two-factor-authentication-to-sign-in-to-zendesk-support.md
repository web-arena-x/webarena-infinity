# Using two-factor authentication to sign in to Zendesk Support 

Source: https://support.zendesk.com/hc/en-us/articles/4408829277466-Using-two-factor-authentication-to-sign-in-to-Zendesk-Support

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Enhance your account security with two-factor authentication by requiring a passcode from an app, email, or SMS in addition to your password. If you lose access to your device or email, use recovery codes to regain access. You can enable or disable this feature in your security settings, ensuring only you can sign in to your account.

Location:  Agent UI > User Avatar > View
Profile Page > Security Settings

Two-factor authentication makes it difficult for somebody else to sign in as you.
After you enter your password as usual, you'll be asked to enter a passcode.
You can get the passcode from your email, a text message (SMS), or a
two-factor authentication app installed on your mobile device.

An admin can *require* two-factor authentication for all agents and
administrators, but the admin can't set it up for them. If it's required,
you'll be prompted to set it up when you sign in. Even if it's not a
requirement, you can still set up two-factor authentication for your own
use.

Admins can refer to [Managing two-factor
authentication](https://support.zendesk.com/hc/en-us/articles/4408826974874) to learn about important considerations before
turning it on.

This article covers the following topics:

- [Using a recovery code to regain access to your account](#topic_ekz_13k_gs)
- [Turning on two-factor authentication](#topic_qdm_yhk_gs)
- [Configuring how you'd like to receive passcodes](#topic_ry3_mrd_h2c)
- [Turning off two-factor authentication](#topic_p3p_zhk_gs)

## Using a recovery code to regain access to your account

If you can't access your device or email account, you can use one of your
recovery codes to reaccess your account. Recovery codes are
displayed once upon initial setup of two-factor authentication. When
prompted for a passcode at sign-in, enter one of your recovery
codes.

You can only use each code once. If you use up all your codes or can't
find them, ask your Zendesk admin or account owner to [get a recovery code for
you](https://support.zendesk.com/hc/en-us/articles/8197977742874).

## Turning on two-factor authentication

If two-factor authentication isn't required, you can turn it on for your
own use. After you turn it on, you'll be prompted for a passcode
every time you sign in.

**To turn on two-factor authentication**

1. In the Zendesk Support agent interface, click your user icon in
   the upper right and select **View profile**.
2. Click the **Security settings** tab.
3. In the Two-factor Authentication section, click
   **Manage**.
4. Click **Set up 2FA**.
5. Continue to the sections below, depending on how you'd like to
   receive passcodes:
   - [Receiving passcodes through an authenticator app](#topic_j2y_zzr_r2b)
   - [Receiving passcodes through email](#topic_oqr_mkz_4hc)
   - [Receiving passcodes through text message](#topic_dxp_d1s_r2b)

## Configuring how you'd like to receive passcodes

You can receive passcodes through a two-factor authentication app, email,
or text message.

### Receiving passcodes through an authenticator app

To use an authenticator app to receive passcodes, you must
install a two-factor authentication app on your mobile
device. Two-factor authentication apps include [Google Authenticator](https://support.google.com/accounts/answer/1066447), [Microsoft
Authenticator](https://support.microsoft.com/en-us/account-billing/download-microsoft-authenticator-351498fc-850a-45da-b7b6-27e523b8702a), [Authy](https://www.authy.com/), [Symantec VIP](https://m.vip.symantec.com/), and [Duo Mobile](https://duo.com/product/trusted-users/two-factor-authentication/duo-mobile).
The app displays a valid passcode on the opening screen. You
typically get 30 seconds to use it before it expires, then
the app displays a new passcode.

Note: You need to use the mobile
version of a two-factor authentication app, not a
desktop version.

**To receive passcodes through an authenticator app**

1. Select **Authenticator app** in the Set up
   two-factor authentication (2FA) dialog, then click
   **Next**.

   This dialog appears after turning
   on 2FA, or upon sign-in when 2FA is
   required.

   ![image](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/2FA_select_passcode_method.png)

   You are directed to
   the Connect your 2FA method step.

   ![image](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/2fa_qr_code_react.png)
2. Start the two-factor authentication app on your
   device, select the option to add an entry, and
   point your device's camera at the QR code (the
   blocky square) on the Zendesk dialog in your
   browser window.

   The mobile app might refer to
   this action as **Scan Barcode**.

   The app
   should automatically scan the QR code and generate
   a passcode. If you have trouble scanning the QR
   code, you can manually enter the secret key that's
   provided. Scanning the barcode is a one-time-only
   step.
3. Enter the passcode generated by the app, then
   click **Save**.
4. Click **Copy recovery codes** and save them
   in a safe location. If you lose your phone or
   can't get a passcode, you must use a [recovery
   code](#topic_ekz_13k_gs) to sign in.

From now on, when you sign in, you can get a valid passcode by
simply opening a two-factor authentication app on your
device. The app displays a valid passcode on the opening
screen. The app doesn't need an internet connection to
display valid passcodes.

### Receiving passcodes through email

If you'd like to receive passcodes through email, you must
provide the email address where you'd like them sent.

**To receive passcodes through email**

1. Select **Email** in the Set up two-factor
   authentication (2FA) dialog, then click
   **Next**.

   This dialog appears after turning
   on 2FA, or upon sign-in when 2FA is
   required.
2. Enter an email address, then click **Send passcode**.

   An email will be sent to the email address
   shortly.
3. Enter the code sent to you, then click
   **Next**.

   Email passcodes for 2FA are valid
   for 60 seconds.
4. Click **Copy recovery codes** and save them in a safe
   location. If you lose your phone or can't get a
   passcode, you must use a [recovery
   code](#topic_ekz_13k_gs) to sign in.
5. Click **Done**.

### Receiving passcodes through text message

To receive passcodes through text message, make sure you include
a phone number that is eligible to receive the
*transactional* SMS messages. Some countries,
such as India, have [restrictions](https://support.twilio.com/hc/en-us/articles/223134167).
For more information, see [SMS
Guidelines](https://www.twilio.com/guidelines/sms).

**To receive passcodes through text messages**

1. Select **SMS** in the Set up two-factor
   authentication (2FA) dialog, then click
   **Next**.

   This dialog appears after turning
   on 2FA, or upon sign-in when 2FA is
   required.
2. Enter a phone number that can receive text messages,
   then click **Send passcode**.

   A text message
   will be sent to the number shortly.

   Note: The phone number must be in
   E.164 format.
3. Enter the code sent to you, then click
   **Save**.

   SMS passcodes for 2FA are valid for
   60 seconds.
4. Click **Copy recovery codes** and save them in a safe
   location. If you lose your phone or can't get a
   passcode, you must use a [recovery
   code](#topic_ekz_13k_gs) to sign in.

From now on, when you sign in, you can get a valid passcode from
a text message sent to your phone.

## Turning off two-factor authentication

If two-factor authentication is not a requirement, but you turned it on
anyway, you can turn it off.

1. In the Zendesk Support agent interface, click your user icon in
   the upper right and select **View profile**.
2. Click the **Security Settings** tab.
3. In the **Two-Factor Authentication** section, click
   **Manage**.
4. Click **Turn off 2FA**.
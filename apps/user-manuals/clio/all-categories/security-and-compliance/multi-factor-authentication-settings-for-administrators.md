# Multi-Factor Authentication Settings for Administrators

Source: https://help.clio.com/hc/en-us/articles/9284724578715-Multi-Factor-Authentication-Settings-for-Administrators

---

Firm users with administrator permissions can invite, require, and disable multi-factor authentication (MFA) for other firm users on the Clio Manage account. Users who are invited can choose not to turn on MFA. Users who are required must enable MFA on their next login. Disabling MFA is beneficial when a user is locked out of their account and is unable to sign in or use backup codes.

**Important:** Only users with administrator permissions and the primary subscriber on the account can see the MFA status of active users at their firm and perform the actions below.

## Invite users

1. Go to **Settings** > **Security & Compliance** > **Firm Security**.
2. Click **Invite to enable MFA** beside a user’s name. This action will send the user an email requesting that they turn on MFA with instructions on how to do so.
3. *Optional:* Click **Send reminder** to send the invited user a reminder.

## Require MFA

1. Go to **Settings** > **Security & Compliance** > **Firm Security**.
2. Find the user and toggle on the button below **Require MFA**. The user will be required to enable MFA the next time they log in.

**Note:** If the column reads N/A, try again the next day. Newly created users may not immediately be migrated to the identity service that supports requiring MFA.

## Disable MFA

If a firm user is locked out of their Clio account and they are unable to sign in or use any backup codes, an administrator can disable MFA on their account as long as the administrator has MFA enabled on their own account first.

**Important:** An administrator cannot disable MFA on the primary subscriber’s account. If this method does not work, the user will need to contact Clio's support team to proceed with the account recovery process. Learn more [here](https://help.clio.com/hc/en-us/articles/9284748707739).

1. Go to **Settings** > **Security** **& Compliance** > **Firm Security**.
2. In the column below **Action,** click **Disable MFA**.
3. When the warning prompt appears, check the box confirming that you want to disable MFA and then click **Disable MFA**.

**Tip:** If a user runs out of backup codes, disabling and re-enabling MFA will produce a new set of backup codes.
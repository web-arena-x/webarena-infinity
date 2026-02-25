# Enable Security Settings for Logins, Passwords, and Session Timeout Intervals

Source: https://v2.support.procore.com/product-manuals/admin-company/tutorials/enable-security-settings-for-logins-passwords-and-session-timeout-intervals

---

## Background

If you are your company's Procore Administrator, or if your Procore user account has been granted 'Admin' level permissions to the Company level Admin tool, you can submit a request to modify select security settings for the your company's Procore account. You can request to enable settings for locking out users after failed login attempts, password expiration policies, and a timeout interval for idle user sessions. Requests to change security settings must be submitted to your Procore point of contact .

## Things to Consider

- **Required User Permissions**:

 - 'Admin' on the company's Admin tool.
- **Additional Information**:

 - For new company accounts, the settings below are configured during the Procore Implementation Process.
 - For existing company accounts, a user with the appropriate permissions must submit a request to your Procore point of contact .
- **Limitations**:

 - These are company-wide settings. They cannot be applied on a per-project or per-user basis.

## Steps

1. Request to Enable Security Settings
2. Review Your Company's Account Security Settings

### Step 1: Request to Enable Security Settings

If you want to make changes to your company's security settings, a user with 'Admin' level permission to the company's Admin tool can email a request to your Procore point of contact .

### Step 2: Review Your Company Account's Current Security Settings

1. Navigate to the Company level **Admin** tool.
2. Under 'Company Settings', click **General** **Settings**.
3. Under 'Security Settings', review the following:

       
   - **Lock Out After 3 Failed Sign In Attempts**:

     - **Yes**. If this setting is turned ON, users with be locked out of Procore after three (3) failed login attempts.
     - **No**. If this setting is turned OFF, there is no limit to the number of failed login attempts that can be made by an end user.
   - **Password Expiration**:

     - **Never**. User passwords never expire.
     - **Number of Days**. User passwords expire after a set number of days. Options are:
     - **None.** Passwords do not expire.
     - **30 days.** Passwords expire every 30 days.
     - **60 days.** Passwords expire every 60 days.
     - **90 days.** Passwords expire every 90 days.
   - **Session Idle Timeout**:

     - **No Timeout**. This is the default setting.
     - **15 minutes**. Ends an inactive user's session after 15 minutes of inactivity.
     - **30 minutes**. Ends an inactive user's session after 30 minutes of inactivity.
     - **60 minutes**. Ends an inactive user's session after 60 minutes of inactivity.
     - **120 minutes**. Ends an inactive user's session after 120 minutes of inactivity.
   - **Enforce Password Resets via Email**

     - **Yes**. If this setting is turned ON, users are only able to reset their passwords via email notification.
     - **No**. If this setting is turned OFF, users can reset their passwords via email or [My Profile Settings](/product-manuals/home-project/tutorials/manage-my-profile-settings).

       ##### Â Important

       The 'Session Idle Timeout' configured for your company will be only enforced on users actively working in your company's Procore account, meaning a user's timeout may change if and when they work in another company's Procore account.
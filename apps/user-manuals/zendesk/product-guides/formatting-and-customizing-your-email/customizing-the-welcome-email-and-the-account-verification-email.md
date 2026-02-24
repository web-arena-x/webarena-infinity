# Customizing the welcome email and the account verification email

Source: https://support.zendesk.com/hc/en-us/articles/4408824350746-Customizing-the-welcome-email-and-the-account-verification-email

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Verified AI summary ◀▼

Customize your welcome and verification emails to align with your brand and improve communication with users. You can modify the text in these system-generated emails and include a list of active help centers. Welcome emails are triggered by user actions like password resets or profile creation, while verification emails confirm additional identities. Personalizing these emails enhances user engagement and ensures consistent branding.

End-user account emails notify agents and end users about changes to their profiles. These system-generated emails are among the earliest communications you'll have with a customer and can be updated to better match your brand or organization's guidelines.

This article covers the following topics:

- [Customizing the user welcome email](#topic_vcv_xqj_v1b)
- [Customizing the email verification email](#topic_owc_yqj_v1b)

When you're updating these emails, you can include a list of all active help centers associated with your brand.

For more information on system-generated emails, see [Customizing your email notifications](https://support.zendesk.com/hc/en-us/articles/4408886168090). To customize the look and feel of the email notifications sent from your Zendesk account, see the [Zendesk email design cookbook](https://support.zendesk.com/hc/en-us/articles/8414886738970).

Tip: You can use HTML to customize both the user welcome and verification emails.

## Customizing the user welcome email

The user welcome email is sent when any of the following occurs:

- An unverified end user clicks **Forgot password?** and enters their email.
- An unverified user clicks the ticket link in the email they receive after submitting a support request. They are directed to Zendesk to provide their email address to get a verification link to set a password. (This workflow is the same as the "forgot password" steps. Both will send the end user a *welcome email, not a verification email.*)
- An end user completes the signup form to create a profile.
- An agent creates the user and **Also send a verification email when a new user is created by an agent or administrator** is enabled.
- An agent clicks **Resend verification email** on an end-user profile.

This email is sent from the default support address of the brand where the user signed up.
The exception is when profiles are created through the Web Widget; the welcome email is sent from the default support address of the default brand.

If a user is created by an agent using **+Add user** and **Also send a verification email when a new user is created by an agent or administrator** is enabled, the Welcome email is sent from the support address of the brand selection entered at the time of user creation.

If an agent creates the user by entering the user's email into the Requester field instead of clicking **+Add user**, the email is sent from the agent brand instead of the default or ticket brand. The agent brand is the brand that agents are routed to when they sign in to Zendesk. If the help center of the agent brand isn't active, but other help centers are active, the welcome email is sent from the oldest brand with an active help center.

Note: For end users to receive the welcome email, your help center must be active (see [Activating your help center](https://support.zendesk.com/hc/en-us/articles/4408846795674-Getting-started-with-Guide-for-your-help-center-Setting-up#topic_ckn_wc4_qy)). Agents receive the welcome email regardless of the activation status of your help center.

**To customize the user welcome email**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > End users**.
2. In the **Account emails** section, update the text in the **User welcome email text** field.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/welcome_email_settings_2.png)
3. (Optional) Select **Also send a welcome email when a new user is created by an agent or administrator** to send an email when a new user is created on behalf of an end user; deselect this option to send a welcome email only when the end user creates their own new user.
4. Click **Save tab** at the bottom of the page.

The user receives a welcome email, including a link to complete their registration:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/welcome_email.png)

If you have multiple brands, you also have the option to include a list of active help centers in the welcome email. Click **Include a list of active Help Centers in account emails** checkbox to enable this feature.

## Customizing the email verification email

The email verification email is sent when any of the following occurs:

- An end user adds an additional identity to their account.
- An agent manually sends the verification email to the new identity.

The email is sent from the default support address of the brand where the user signed up.
When agents create users, the email is sent from the default support address of your default brand. After the primary email address is verified, additional email addresses added by an agent or administrator are automatically verified.

**To customize the email verification email**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Configuration > End users**.
2. In the **Account emails** section, update the text in the **Email verification text** field.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/email_verification_settings.png)
3. Click **Save tab** at the bottom of the page.

If you have multiple brands, you also have the option to include a list of active help centers in the verification email. Click **Include a list of active Help Centers in account emails** checkbox to enable this feature.
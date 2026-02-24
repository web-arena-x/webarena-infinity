# Setup Guide: Microsoft Azure AD (Entra ID)

Source: https://v2.support.procore.com/product-manuals/azure-ad-sso/tutorials/setup-guide-microsoft-azure-ad

---

##### Azure Active Directory is now Microsoft EntraÂ ID

Microsoft has rebranded Azure Active Directory as **Microsoft Entra ID**. This instructions in this documentation are not impacted by the name change.

## Overview

To setup and configure the Procore-Initiated SSO solution with Microsoft Azure Active Directory (Azure AD).

## Preparation Phase

To prepare for the integration, complete these steps:

1. Send a request to your company's Procore point of contact to discuss your company's specific SSO requirements and goals.

   - Ensure that you or a user in your IT organization has an active account with Global Administrator rights to Azure AD.
   - In Azure AD, select and assign users to create an SSO group that contains the users who will be using your Procore-Initiated SSO solution. For instructions, see Microsoft's [Azure Active Directory Documentation](https://docs.microsoft.com/en-us/azure/active-directory/).

## Integration Phase

To complete the integration, complete these steps:

1. Complete the required configuration steps. See [Configure Procore SP-Initiated SSO for Microsoft Azure AD](/product-manuals/azure-ad-sso/tutorials/configure-procore-sp-initiated-sso-for-microsoft-azure-ad).
2. Notify your company's Procore point of contact that the configuration is complete. 
   *Note*: Your Procore point of contact or Procore Support must add the email domain(s) that will be targeted for login via SSO to Procore's Admin tool before you can enable Single Sign-On.
3. Log in to Procore. See [Log into Procore Using SP-Initiated Azure AD](/product-manuals/azure-ad-sso/tutorials/log-in-to-procore-using-sp-initiated-azure-ad).

## Management Phase

Once the integration has been completed, the following should be considered:

1. Users with login credentials that contain the email domain(s) that are targeted for login via SSO will be required to log in to Procore using the credentials for their Azure AD account. 
   *Note*: The log in process is supported by Procore Web, Procore for Android, and Procore for iOS.
2. Passwords and password policies are managed in your company's Azure AD account. 
   *Note*: If your company will be providing Procore access to end users whose login credentials do NOT contain a targeted email domain, those users will sign in using the login credentials in their Procore user profile.
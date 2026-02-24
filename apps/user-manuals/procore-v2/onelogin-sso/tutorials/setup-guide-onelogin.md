# Setup Guide: OneLogin

Source: https://v2.support.procore.com/product-manuals/onelogin-sso/tutorials/setup-guide-onelogin

---

## Overview

To setup and configure the Procore-Initiated SSO solution with OneLogin.

## Preparation Phase

To prepare for the integration, complete these steps:

1. Send a request to your company's Procore point of contact  to discuss your company's specific SSO requirements and goals.

   - Ensure that you or a user in your IT organization has an active account with Administrator rights to your OneLogin Domain.
   - In OneLogin, add your Procore users. See [Introduction to User Management](https://support.onelogin.com/hc/en-us/articles/202361060-Introduction-to-User-Management) at the OneLogin Help Center.

## Integration Phase

To complete the integration, complete these steps:

1. Complete the required configuration steps. See [Configure Procore-Initiated SSO for OneLogin](/product-manuals/onelogin-sso/tutorials/configure-sp-initiated-sso-for-procore-in-onelogin).
2. Notify your company's Procore point of contact  that the configuration is complete.  
   *Note*: A Procore Employee must perform a final configuration step.
3. Log in to Procore. See [Log into Procore-Initiated SSO for OneLogin](/product-manuals/onelogin-sso/tutorials/log-in-to-procore-initiated-sso-for-onelogin).

## Management Phase

Once the integration has been completed, the following should be considered:

1. Users with login credentials that match your company's SSO-configured domain will be required to log in to Procore using the credentials for their OneLogin account.
2. Passwords and password policies are managed in your company's OneLogin account.  
   *Note*: If your company will be providing Procore access to end users whose login credentials do NOT reside in your OneLogin domain, those users will sign into using the login credentials in their Procore user profile.
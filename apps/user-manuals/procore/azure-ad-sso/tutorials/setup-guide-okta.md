# Setup Guide: Okta

Source: https://v2.support.procore.com/product-manuals/azure-ad-sso/tutorials/setup-guide-okta

---

## Overview

To setup and configure the Procore-Initiated SSO solution with Okta.

## Preparation Phase

To prepare for the integration, complete these steps:

1. Send a request to your company's Procore point of contact to discuss your company's specific SSO requirements and goals.

   - Ensure your edition of Okta is supported by Procore-initiated SSO.
   - Ensure that you or a user in your IT organization has an active account with Administrator rights to Okta
   - In Okta, select and assign users to create an SSO group that contains the users who will be using your Procore-Initiated SSO solution. For instructions, see Okta's [Help Documentation](https://support.okta.com/help/oktaDocumentationPage).

## Integration Phase

To complete the integration, complete these steps:

1. Complete the required configuration steps. See [Configure Procore-Initiated SSO for Okta](/product-manuals/okta-sso/tutorials/configure-sp-initiated-sso-for-procore-in-okta).
2. Notify your company's Procore point of contact that the configuration is complete. 
   *Note*: A Procore Employee will perform a final configuration step.
3. Log in to Procore. See [Log into Procore-Initiated SSO for Okta](/product-manuals/okta-sso/tutorials/log-in-to-procore-initiated-sso-for-okta).

## Management Phase

Once the integration has been completed, the following should be considered:

1. Users with login credentials that match your company's SSO-configured domain will be required to log in to Procore using the credentials for their Okta account. 
   *Note*: The log in process is supported in Procore Web, Procore for Android, Procore for iOS, and Procore for Windows.
2. Passwords and password policies are managed in your company's Okta account. 
   *Note*: If your company will be providing Procore access to end users whose login credentials do NOT reside in your Okta domain, those users will sign into using the login credentials in their Procore user profile.
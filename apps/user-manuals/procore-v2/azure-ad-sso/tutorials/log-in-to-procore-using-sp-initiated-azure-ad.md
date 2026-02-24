# Log in to Procore Using SP-Initiated Azure AD (Entra ID)

Source: https://v2.support.procore.com/product-manuals/azure-ad-sso/tutorials/log-in-to-procore-using-sp-initiated-azure-ad

---

##### Azure Active Directory is now Microsoft EntraÂ ID

Microsoft has rebranded Azure Active Directory as **Microsoft Entra ID**. This instructions in this documentation are not impacted by the name change.

## Background

When your company's account is configured for Procore-Initiated SSO for Microsoft Azure Active Directory, you will need to know your email address and password for your Azure Active Directory domain.

## Things to Consider

- **Required User Permission**:

 - *To receive a 'Welcome to Procore' email,* a user with 'Admin' level permission to an organization's Company Directory must do the following for you:

    - Create a Procore user account for you in their company's Directory tool. See [Add a User Account to the Company Directory](/product-manuals/directory-company/tutorials/add-a-user-account-to-the-company-directory) or [Add a User Account to the Project Directory](/product-manuals/directory-project/tutorials/add-user-account-to-project-directory).
- **Supported Platforms**:

 - Procore Web
 - Procore for iOS
 - Procore for Android
- **Prerequisites**:

 - Your company's Procore Administrator and/or Azure Active Directory Administrator must complete the preparation and integration steps in [Setup Guide: Microsoft Azure AD](/product-manuals/azure-ad-sso/tutorials/setup-guide-microsoft-azure-ad).

## Steps

1. Navigate to the Procore login page at: <https://login.procore.com>
2. Enter your login email address. 
   *Note*: When your Procore-Initiated SSO application is properly configured, the Procore login page recognizes your email domain and automatically hides the password field. See [Setup Guide: Microsoft Azure AD](/product-manuals/azure-ad-sso/tutorials/setup-guide-microsoft-azure-ad).
3. Click **Log In**.   
    The system redirects you to the Azure login page.
4. Complete the following:

   - **Email and Password**. Enter your login credentials for your company's Azure Active Directory.   
     *Note*: If you do not know your login information, contact your company's Administrator for Azure Active Directory.
5. Click **Sign In**. 
    The system logs you into Procore.
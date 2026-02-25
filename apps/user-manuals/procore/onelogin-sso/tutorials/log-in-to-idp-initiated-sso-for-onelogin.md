# Log in to IdP-Initiated SSO for OneLogin

Source: https://v2.support.procore.com/product-manuals/onelogin-sso/tutorials/log-in-to-idp-initiated-sso-for-onelogin

---

[MindTouch Responsive Upgrade] INFO: Completed 1/17/18 8:24:53 PM UTC

[MindTouch Responsive Upgrade] INFO: Page already has page summary, no legacy overview section migration performed.

## Background

When your company's account is configured for IdP-Initiated SSO for OneLogin, you will need to know your email address and password for logging into your OneLogin portal.

## Things to Consider

- **Required User Permission:**

  - To complete the steps below, you must know your OneLogin Domain and your OneLogin credentials (i.e., email address and password). See your company's OneLogin Administrator for this information.
- **Prerequisites:**

  - Your company's OneLogin Administrator must configure the Procore Application to work with your company's OneLogin SSO. See [Configure IdP-Initiated SSO for OneLogin](/product-manuals/onelogin-sso/tutorials/configure-idp-initiated-sso-for-onelogin).
- **Limitations**:

  - OneLogin SSO is supported by the Procore web application only. It is not supported by Procore Mobile, Procore for Android, or Procore for iOS.

## Steps

1. Navigate to the OneLogin portal: <https://app.onelogin.com/login>
2. Enter your company's OneLogin Domain.   
    *Notes*:

   - If you do NOT know your OneLogin Domain, contact your company's OneLogin Administrator.
   - If you know your OneLogin Domain, you can also directly enter it into your browser's address bar using this format:  
      https://.onelogin.com/login
3. At the login page, do the following:

   1. Enter your email address and password in the space provided.
   2. Enter your password and click **Log In**.  
       This opens your App Home page. The Procore application should already be listed.  
       *Note*: If it is not, contact your company's [Procore Administrator](https://support.procore.com/procore-learning-paths/general-contractor/procore-administrator).
4. In the App Home page, click the **Procore** application.   
    *Note*: In this example, the OneLogin Administrator named the application 'Procore'. Your company's OneLogin Administrator may choose to use a different name.   
      
      
      
    The system authenticates your identity and redirects you to the Procore web application.  
    *Note*: If your Procore credentials have been granted access to more than one Procore company account, you will have the ability to switch between company accounts in Procore. See [How do I change companies in Procore's navigation bar?](/product-manuals/login-and-account-management/tutorials/change-companies-in-procores-navigation-bar)
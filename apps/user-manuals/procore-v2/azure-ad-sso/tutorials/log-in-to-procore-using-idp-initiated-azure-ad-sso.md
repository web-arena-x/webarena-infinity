# Log in to Procore Using IdP-Initiated Azure AD (Entra ID) SSO

Source: https://v2.support.procore.com/product-manuals/azure-ad-sso/tutorials/log-in-to-procore-using-idp-initiated-azure-ad-sso

---

##### Azure Active Directory is now Microsoft EntraÂ ID

Microsoft has rebranded Azure Active Directory as **Microsoft Entra ID**. This instructions in this documentation are not impacted by the name change.

## Background

If your company's system administrator has added the Procore Enterprise Application to Azure AD, you can use the Steps below to sign into Procore using your Azure AD login credentials (i.e., email address and password)

## Things to Consider

- **Required User Permission:**

 - To complete the steps below, you must obtain valid Azure AD login credentials (i.e., email address and password) from your company's Azure AD Administrator.
- **Prerequisites:**

 - Your company's Azure AD Administrator must add the Procore Enterprise Application to Azure AD and configure it properly. See [Configure IdP-Initiated Azure AD SSO](/product-manuals/azure-ad-sso/tutorials/configure-idp-initiated-sso-for-microsoft-azure-ad).
- **Limitations**:

 - Before your company's Azure AD Administrator adds Procore as an Enterprise Application in Azure AD, Procore recommends reviewing the table below to determine which configuration best satisfies your company's login requirements.

    | **SSO Integration** | **Procore for Web** | **Procore for Android** | **Procore for iOS** | **Procore Drive** | **Procore Sync** |
    | --- | --- | --- | --- | --- | --- |
    | SP-Initiated Azure AD | | | | | |
    | IdP-Initiated Azure AD | | | | | |

## Steps

1. Navigate to the Microsoft portal: <http://myapps.microsoft.com/>
2. Enter your email address and click **Continue**.
3. Enter your password and click **Sign In**.
4. Under **Applications** page, click the Procore application. *Note*: In this example, the Administrator named the application 'Procore SSO'. Your company's Administrator may choose to use a different name.

       

   The system authenticates the user's identity and redirects them to the Procore web application.

##### Â Note

If the a user has been granted access to more than one Procore company account under the same email address containing a targeted domain, the user will have the ability to switch between company accounts in Procore without needing to re-authenticate.
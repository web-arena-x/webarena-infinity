# Azure AD SSO

Source: https://v2.support.procore.com/product-manuals/azure-ad-sso

---

Table of Contents

## Overview

##### Azure Active Directory is now Microsoft EntraÂ ID

Microsoft has rebranded Azure Active Directory as **Microsoft Entra ID**. This instructions in this documentation are not impacted by the name change.

### Implement SSO for Procore with Azure Active Directory

If your company uses Microsoft Azure Active Directory (Azure AD), you can add Procore as an enterprise application to provide users in your organization with Single Sign-On (SSO) capabilities.

##### Â Notes

- If your organization is using the [Portfolio Financials and Capital Planning](/product-manuals/portfolio-financials/) products in Procore, you will need to reach out to your Procore point of contact or the Support team to set up your Azure AD SSO.
- Customers who license Procore Pay may require additional support enabling MFA for Payments when SSO is configured for their company. If you license Procore Pay and want to enable SSO, .

With Azure AD, you can log into Procore using a secure and consistent process defined by your company from any supported device (i.e., iOS, Mac OS X, Android, and Windows).

Currently, Procore's Azure AD application supports both SP- and IdP-Initiated SSO. See [What is the difference between SP- and IdP-Initiated SSO?](/faq-what-is-the-difference-between-sp-and-idp-initiated-sso)

| | |
| --- | --- |
| | [Configure SP-Initiated SSO for Azure AD](/product-manuals/azure-ad-sso/tutorials/configure-procore-sp-initiated-sso-for-microsoft-azure-ad) |
| | [Configure IdP-Initiated SSO for Azure AD](/product-manuals/azure-ad-sso/tutorials/configure-idp-initiated-sso-for-microsoft-azure-ad) |

*Microsoft, Windows, Azure, Entra ID, and Azure Active Directory are either registered trademarks or trademarks of Microsoft Corporation in the United States and/or other countries.*
# Setting up single sign-on using Active Directory with ADFS and SAML

Source: https://support.zendesk.com/hc/en-us/articles/4408834714650-Setting-up-single-sign-on-using-Active-Directory-with-ADFS-and-SAML

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

**Disclaimer**: This article is provided for instructional purposes only. Zendesk does not support or guarantee the code. Post any issues you have in the comments section or try searching for a solution online.

Zendesk supports single sign-on (SSO) logins through SAML 2.0. A SAML 2.0 identity provider (IDP) can take many forms, one of which is a self-hosted Active Directory Federation Services (ADFS) server. ADFS is a service provided by Microsoft as a standard role for Windows Server that provides a web login using existing Active Directory credentials.

This article contains the following sections:

- [Requirements](#01H8HPZF06BRMFYMKVQYM4K6V7)
- [Step 1 - Adding a Relying Party Trust](#01H8HPZF06P9W251K0NFY276K4)
- [Step 2 - Creating claim rules](#01H8HPZF06V59X0XJBQDB207BB)
- [Step 3 - Adjusting the trust settings](#01H8HPZF061W4W197MGW97DXR2)
- [Step 4 - Configuring Zendesk](#01H8HPZF06Q85PJG024M3VGX6E)
- [Switching authentication methods](#01H8HPZF06CPBA47NCSM0P1P6Q)

## Requirements

To use ADFS to log in to your Zendesk instance, you need the following components:

- An Active Directory instance where all users have an email address attribute.
- A Zendesk instance.
- A server running Microsoft Server 2012 or 2008. This guide uses screenshots from Server 2012R2, but similar steps should be possible on other versions.
- A SSL certificate to sign your ADFS login page and the fingerprint for that certificate.
- If you're using host mapping in your Zendesk instance, an installed certificate for hosted SSL.

After you meet these basic requirements, you need to install ADFS on your server. Configuring and installing ADFS is beyond the scope of this guide, but is detailed in a [Microsoft KB article](http://msdn.microsoft.com/en-us/library/gg188612.aspx).

When you have a fully installed ADFS installation, note down the value for the 'SAML 2.0/W-Federation' URL in the ADFS Endpoints section. If you chose the defaults for the installation, this will be '/adfs/ls/'.

## Step 1 - Adding a Relying Party Trust

At this point you should be ready to set up the ADFS connection with your Zendesk account. The connection between ADFS and Zendesk is defined using a Relying Party Trust (RPT).

Select the **Relying Party Trusts** folder from **AD FS Management**, and add a new **Standard Relying Party Trust** from the **Actions** sidebar. This starts the configuration wizard for a new trust.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wizzard%20start.png)

1. In the **Select Data Source** screen, select the last option, **Enter Data About the Party Manually**. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wizzard%20metadata.png)
2. On the next screen, enter a **Display name** that you'll recognize in the future, and any notes you want to make. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wizzard%20label.png)
3. On the next screen, select the **ADFS FS profile** radio button. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wizzard%20profile.png)
4. On the next screen, leave the certificate settings at their defaults. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wizzard%20cert.png)
5. On the next screen, check the box labeled **Enable Support for the SAML 2.0 WebSSO protocol**. The service URL will be https://***subdomain***.zendesk.com/access/saml, replacing ***subdomain*** with your Zendesk subdomain. Note that there's no trailing slash at the end of the URL. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wizzard%20URL.png)
6. On the next screen, add a **Relying party trust identifier** of ***subdomain***.zendesk.com, replacing ***subdomain*** with your Zendesk subdomain. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wizzard%20identifier.png)

   Note: If you enter *subdomain*.zendesk.com, and receive a request failure error, you may need to enter your subdomain as https://*subdomain*.zendesk.com or *subdomain*.zendesk.com/.
7. On the next screen, you may configure multi-factor authentication but this is beyond the scope of this guide. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wizzard%20multi-factor.png)
8. On the next screen, select the **Permit all users to access this relying party** radio button. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wizzard%20auth.png)
9. On the next two screens, the wizard will display an overview of your settings. On the final screen use the **Close** button to exit and open the Claim Rules editor. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/wizzard%20finished.png)

## Step 2 - Creating claim rules

Once the relying party trust has been created, you can create the claim rules and update the RPT with minor changes that aren't set by the wizard. By default the claim rule editor opens once you created the trust. If you want to map additional values beyond authentication, refer to our [documentation](https://support.zendesk.com/hc/en-us/articles/4408842661530-Mapping-Attributes-from-Active-Directory-with-ADFS-and-SAML-Plus-and-Enterprise-).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/claim_rules.png)

1. To create a new rule, click on **Add Rule**. Create a **Send LDAP Attributes as Claims** rule. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/claim%20LDAP%201.png)
2. On the next screen, using **Active Directory** as your attribute store, do the following: 
   1. From the **LDAP Attribute** column, select **E-Mail Addresses**. 
   2. From the **Outgoing Claim Type**, select **E-Mail Address**. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/claim%20ldap%202.png)
3. Click on **OK** to save the new rule.
4. Create another new rule by clicking **Add Rule**, this time selecting **Transform an Incoming Claim** as the template. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/claim_transform1.png)
5. On the next screen: 
   1. Select **E-mail Address** as the **Incoming Claim Type**. 
   2. For **Outgoing Claim Type**, select **Name ID**.3. For **Outgoing Name ID Format**, select **Email**. 
   Leave the rule to the default of **Pass through all claim values**. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/claim%20transform%202.png)
6. Finally, click **OK** to create the claim rule, and then **OK** again to finish creating rules.

## Step 3 - Adjusting the trust settings

You still need to adjust a few settings on your relying party trust. To access these settings, select **Properties** from the **Actions** sidebar while you have the RPT selected.

1. In the **Advanced** tab, make sure **SHA-256** is specified as the secure hash algorithm. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sha-1.png)
2. In the **Endpoints** tab, click on **add SAML** to add a new endpoint.
3. For the **Endpoint type**, select **SAML Logout**.
4. For the **Binding**, choose **POST**.
5. For the **Trusted URL**, create a URL using: 
   1. The web address of your ADFS server 
   2. The ADFS SAML endpoint you noted earlier 
   3. The string '?wa=wsignout1.0' 
   The URL should look something like this: https://***sso.yourdomain.tld***/adfs/ls/?wa=wsignout1.0. 
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/logout%20saml.png)
6. Confirm you changes by clicking **OK** on the endpoint and the RPT properties. You should now have a working RPT for Zendesk.

**Note**: Your instance of ADFS may have security settings in place that require all Federation Services Properties to be filled out and published in the metadata. Check with your team to see if this applies in your instance.  If it is, be sure to check the **Publish organization information in federation metadata** box.

## Step 4 - Configuring Zendesk

After setting up ADFS, you need to configure your Zendesk account to authenticate using SAML. Follow the steps in [Enabling SAML single sign-on](https://support.zendesk.com/hc/en-us/articles/4408887505690). You'll use your full ADFS server URL with the SAML endpoint as the SSO URL, and the login endpoint you created as the logout URL. The fingerprint will be the fingerprint of the token signing certificate installed in your ADFS instance.

You can get the fingerprint by running the following PowerShell command on the system with the installed certificate:

`C:\> Get-AdfsCertificate [-Thumbprint] <String[]> [<CommonParameters>]`

Look for the SHA256 thumbprint of the Token-Signing type certificate.

After you're done:

- In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Account** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_account_icon.png)) in the sidebar, then select **Security > Single sign-on.** The page should look like this:

![](https://support.zendesk.com/hc/article_attachments/7856556323482)

You should now have a working ADFS SSO implementation for Zendesk.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ADFS%20login.png)

## Switching authentication methods

**Important**: If you use a third-party SSO method to create and authenticate users in Zendesk, then switch to Zendesk authentication, these users will not have a password available for login. To gain access, ask these users to reset their passwords from the Zendesk sign in page.
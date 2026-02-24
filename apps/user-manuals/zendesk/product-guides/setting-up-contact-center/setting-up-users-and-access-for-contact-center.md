# Setting up users and access for Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9459000058010-Setting-up-users-and-access-for-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

To set up user access for Contact Center, configure Amazon Cognito for agent authentication using SSO with SAML providers. This keeps agent data secure in your AWS account. If not using SSO, manually add users in Cognito User Pools. For admins, add them to the LMAdmin group after their first login. Resources are available for setting up SSO with AWS, Azure AD, Okta, and Google Workspaces.

Now that the integration infrastructure is in place, you need to ensure that agents and admins can log into Contact Center and that Connect will allow the connection. The following sections detail how to configure Cognito for a variety of SAML providers.

Contact Center uses Amazon Cognito for agent authentication, including Single Sign On (SSO). The benefits of this approach are:

- No agent data is stored in the Zendesk environment, as all agent data resides within Amazon Cognito within the client's own AWS account
- Cognito caters to user pools where users can be manually created
- Cognito allows SAML federation, which turns on SSO, with most SAML providers

Note: To set up single sign-on (SSO) for Connect, configure the SAML application in the IAM Identity Center, which might be in a separate AWS account and region. However, the identity provider, role, and policy must be established within the same AWS account as Connect.

This article contains the following topics:

- [Configuring single-sign-on](#topic_wzn_pyv_2hc)
- [Manually adding users using Cognito User Pools (when not using SAML/SSO)](#topic_phr_5gj_jgc)
- [Setting up SSO with other services](#topic_gdv_ps4_2hc)

## Configuring single-sign-on

**To configure SSO**

1. Configure a SAML application and its associated XML configuration file. Specify the following settings for the application:

   | | |
   | --- | --- |
   | **Attribute** | **Value** |
   | ACS URL | https://${yourDomainPrefix}.auth.${region}.amazoncognito.com/saml2/idpresponse |
   | Application SAML audience | urn:amazon:cognito:sp:${yourUserPoolID} |
   | Application start URL (optional) | Contact Center sign in URL |
2. Specify the following SAML attributes for the application:The SAML application must have the following SAML attributes:

   | | | |
   | --- | --- | --- |
   | **SAML Attribute** | **Maps to this string value or user attribute** | **Format** |
   | Subject | ${user:email} | Persistent |
   | http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress | ${user:email} | |
3. Configure the following attributes for the identity provider in Cognito:

   | | |
   | --- | --- |
   | **User pool attribute** | **SAML Attribute** |
   | email | http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress |

## Manually adding users using Cognito User Pools (when not using SAML/SSO)

When the CloudFormation stack ran, it created an Amazon Cognito user pool for your Contact Center instance. The user pool is a set of user accounts who can authenticate to Contact Center. It also created an app client in Cognito, which the Contact Center web app uses to allow users to sign in, and an "LMAdmin group" for admin permissions. Next, create at least one user in this user pool so you can test signing into Contact Center.

**To create a user**

1. In the AWS console, navigate to the Cognito service.
2. Under User pools, click the user pool that was created to manage it.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_9.png)
3. On the Users page, click **Applications** > **App clients**.
4. On the Login pages tab, change the Identity Provider to the Congito user pool directory.
5. In the Cognito user pool console, find the section for Users and click **Create user** (or **Add user**). You'll be prompted to enter the following details for the new user account:
   - **Username:** Enter a username. For testing, you might use “testuser”, or your own name.
   - **Temporary Password:** Set an initial password for the user. Cognito might require the user to reset the password on first login. For internal testing, you can create a simple password and, optionally disable the reset requirement.
   - **Contact Info:** Depending on settings, you might need to provide a valid email or phone number for the user. These can be used for password recovery or multi-factor authorization.
   - **Account Status:** Ensure that **Mark phone/email as verified** is selected if you provided them and don’t want Cognito to request a verification step. Also, select **Temporary password** so the user must change it on first login (for production users).

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_10.png)
6. Click **Create user.** The new user will now appear in the user list for the pool.

   This user represents an **agent (or admin)** who can log into the Contact Center web application.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_11.png)

   By default, newly created users are regular users. If a user has administrator privileges in Contact Center (meaning they can configure Contact Center settings, view dashboards, and similar), they must be added to the **LMAdmin** user pool group that was created with the CloudFormation stack.
7. In the Cognito User Pool, go to the **Groups** page. You'll see a group named **LMAdmin**. Click the group and add your new user to the group.

   Note: If you use SSO, users can only be added to the LMAdmin group are after they have successfully signed into Contact Center at least once.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_12.png)

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_13.png)

## Setting up SSO with other services

The following resources provide additional information about setting up SSO with various services:

- [Amazon Web Services (AWS)](https://support.zendesk.com/hc/en-us/articles/9459034190746)
- [Azure AD](configuring-contact-center-sso-with-azure-ad.md)
- [Okta](https://support.zendesk.com/hc/en-us/articles/9459046854938)
- [Google Workspaces](configuring-google-workspaces-sso-for-contact-center.md)
- [Cognito Userpools](https://support.zendesk.com/hc/en-us/articles/9459000058010)
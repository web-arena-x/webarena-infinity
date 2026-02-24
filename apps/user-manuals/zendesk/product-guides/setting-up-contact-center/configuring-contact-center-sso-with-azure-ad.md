# Configuring Contact Center SSO with Azure AD

Source: https://support.zendesk.com/hc/en-us/articles/9696124990106-Configuring-Contact-Center-SSO-with-Azure-AD

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Configure Single Sign-On (SSO) with Azure AD for your Contact Center to streamline user access and enhance security. Set up involves creating a SAML application in Azure AD, configuring an identity provider in the Cognito Userpool, and specifying it for agent authentication. This integration simplifies login processes and centralizes user management across platforms.

Both Amazon Connect and Zendesk for Contact Center can be configured for SSO
with Microsoft Azure Active Directory (Azure AD) as the SAML-based identity provider.
Amazon Connect and Contact Center each require a SAML application. The required SAML
applications are created and configured in the Azure AD portal.

The Azure AD AWS SAML application along with an AWS IAM identity provider will
enable the federation between Azure AD and your AWS IAM users.

This article contains the following topics:

- [Configuring SSO for Amazon Connect](#topic_pg5_41x_qgc)
- [Configuring SSO for Contact Center](#topic_ufh_p1x_qgc)

## Configuring SSO for Amazon Connect

[This AWS guide](https://catalog.workshops.aws/amazon-connect-sso/en-US/3-sso-amazonconnect-azuread) describes how to configure
Amazon Connect SSO with Azure AD as the identity provider.

We recommended using Service Control Policies (SCPs) to manage permissions
regarding what users and roles can do in Amazon Connect, protecting important
resources and making your system more secure.

**Recommended reading:**[Security best practices for Amazon Connect](https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html)

Below is an example SCP that can be used to prevent the deletion of the
Amazon Connect instance and associated role:

```
<pre><code class="language-json">
&lt;pre&gt;&lt;code class=&quot;language-json&quot;&gt;
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AmazonConnectRoleDenyDeletion",
      "Effect": "Deny",
      "Action": [
        "iam:DeleteRole"
      ],
      "Resource": [
        "arn:aws:iam::*:role/***Amazon Connect user role***"
      ]
    },
    {
      "Sid": "AmazonConnectInstanceDenyDeletion",
      "Effect": "Deny",
      "Action": [
        "connect:DeleteInstance"
      ],
      "Resource": [
        "***Amazon Connect instance ARN***"
      ]
    }
  ]
}
&lt;/pre&gt;&lt;/code&gt;
</pre></code>
```

## Configuring SSO for Contact Center

Single Sign On (SSO) for Contact Center is implemented by configuring the
Cognito Userpool to use a SAML application for sign-in. The Cognito Userpool is the
one which was created by the Contact Center CloudFormation template.

The following summarizes the high-level process which needs to be
followed:

1. Gather the required Cognito Userpool details.
2. Create the SAML application in the Azure AD portal.
3. Configure an identity provider in the Cognito Userpool.
4. Specify this identity provider to be used for agent
   authentication.

**To configure SSO for Contact Center**

**Gather the required Cognito Userpool details**

1. Log into the AWS account in which the Contact Center CloudFormation stack was
   created. Navigate to the Cognito service (ensure that you are in the correct
   region) and open the Userpool which was created when the Contact Center
   CloudFormation stack was created. Note the Userpool ID as shown in the following
   image:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_ad_1.png)
2. Click the App integration tab and note down the Cognito domain prefix. This is
   the first part of the Cognito domain, before the '.auth.regionxxx'. This is also
   the value that was specified in the CloudFormation template so can be copied
   from the CloudFormation parameters tab if you prefer.

**To create the SAML application in the Azure AD portal**

1. Sign in to the Azure Portal and in the Azure Service section, choose Azure
   Active Directory.
2. In the left sidebar, choose **Enterprise applications**.
3. Click **New application** and then **Create your own application**. Fill
   in the following fields:
   - **Input name:** Give your application a name, for example 'Zendesk
     for Contact Center production'. Select ‘Integrate any other application
     you don’t find in the gallery (Non-gallery)’. Select ‘Create’.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_ad_2.png)

     It will
     take a few seconds for the application to be created in Azure AD,
     then you'll be redirected to the overview page for the newly added
     application.

**To set up Single Sign-on using SAML**

1. On the Getting started page, in the Set up single sign on tile, click **Get
   started**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_ad_3.png)
2. On the next screen, select SAML.
3. In the middle pane under Set up Single Sign-On with SAML, in the Basic SAML
   configuration section, click the edit icon.
4. Navigate to the middle pane under Set up Single Sign-On with SAML
5. In the User Attributes & Claims section, click **Edit**.
6. Enter the following field values:
   - **Identifier (Entity ID):** urn:amazon:cognito:sp:**${pool
     ID}**
   - **Reply URL (Assertion Consumer Service URL):**https://**${DomainPrefix}**.auth.**${RegionID}**.amazoncognito.com/saml2/idpresponse
   - [.callout-primary--alert-message]

   Replace the above placeholders with the values copied from the
   Cognito Userpool. [.callout-primary--alert-message]

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_ad_4.png)
7. Click **Add a group claim**.
8. On the User attributes & claims page, in the right pane under Group claims,
   select **Groups assigned to the application**. Leave Source attribute as
   Group ID, as shown in the screenshot below.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_ad_5.png)
9. Click **Save**.
10. Close the User attributes & claims page. You’ll be redirected to the Set up
    single sign-on with SAML page.
11. Scroll down to the SAML signing certificate section, and copy the app federation
    metadata URL by choosing the copy into clipboard icon. Keep this URL handy as
    you’ll need it in the next step.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_ad_6.png)

**To configure an identity provider in the Cognito Userpool**

1. Sign into the AWS account which contains the Cognito Userpool.
2. Navigate to Cognito and open the Userpool.
3. Select the Sign-in experience tab and then click **Add identity provider**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_ad_7.png)
4. On the next page, select SAML.
5. Under Set up SAML federation with this user pool, configure the following:
   - **Provider name:** Enter a name for this identity provider.
     It is recommended to not use any spaces in the name.
   - **Metadata document source:** Paste the metadata URL, from
     the previous step, in the metadata endpoint URL field.
6. Under Map attributes between your SAML provider and your user pool, set the
   following attribute:

   |  |  |
   | --- | --- |
   | **User pool attribute** | **SAML attribute** |
   | email | http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress |
7. Click **Add identity provider**.

   At this point the required
   identity provider has been created. The last step in the Cognito
   configuration is to specify that the app client will use this identity
   provider for agent authentication.

**To specify the identity provider to be used for agent authentication**

1. Select App integration from the tabbed view, scroll to the bottom and click
   **app-client** to open it.
2. Scroll down to the Hosted UI section and click **Edit**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_ad_8.png)
3. Under Hosted sign-up and sign-in pages scroll down to the Identity providers
   dropdown list. Select the identity provider that was configured in the previous
   step.
4. Click **Save changes**.
5. Zendesk requires the name of the IDP (as configured under Sign-in experience) to
   complete the setup of your account. Include this along with the CloudFormation
   outputs in the information you share with Zendesk.
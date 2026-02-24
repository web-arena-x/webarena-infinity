# Setting up Okta single sign-on for Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9459046854938-Setting-up-Okta-single-sign-on-for-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Set up Okta single sign-on for your Contact Center to streamline user authentication. This involves creating a SAML application in Okta, configuring SAML integration, assigning users, and specifying the identity provider for agent authentication. This setup enhances security and simplifies access management across Amazon Connect and your Contact Center.

You can configure Amazon Connect and Contact Center for SSO with Okta as the SAML-based identity provider. Each requires a SAML application to authenticate. You create the SAML applications in the Okta portal.

The Okta SAML application, along with an AWS Identity and Access Management (IAM)
provider, enables federation between Okta and your AWS IAM users.

This article contains the following topics:

- [Configuring SSO for Amazon Connect](#topic_lnb_rzw_zfc)
- [Configuring SSO for Contact Center](#topic_mtr_s3k_1gc)

## Configuring SSO for Amazon Connect

Refer to the [AWS guide](https://catalog.workshops.aws/amazon-connect-sso/en-US/1-sso-amazonconnect-okta) to configure Amazon Connect SSO with Okta as the identity provider.

Use Service Control Policies (SCPs) to manage user and role permissions in Amazon Connect, protecting important resources and making your system more secure. Refer to the [Security best practices for Amazon Connect](https://docs.aws.amazon.com/connect/latest/adminguide/security-best-practices.html)
for more best practices.

The following is an example SCP that you can use to prevent the deletion of the Amazon Connect instance and associated role.

```
<pre><code class="language-json">
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
</pre></code>
```

## Configuring SSO for Contact Center

Configuring SSO for Contact Center includes the following steps:

- [Step 1: Create a SAML application in Okta](#topic_arn_h4k_1gc)
- [Step 2: Configure SAML integration for your Okta application](#topic_kjj_34k_1gc)
- [Step 3: Assign users to your application](#topic_zwj_34k_1gc)
- [Step 4: Specify the identity provider to be used for agent authentication](#topic_imk_34k_1gc)

### Step 1: Create a SAML application in Okta

To enable the federation between Okta and your AWS IAM users, create a SAML application in Okta.

**To create a SAML application**

1. Open the Okta developer console.
2. In the navigation menu, expand Applications, then click **Applications**.
3. Click **Create app integration**.
4. In the Create a new app integration menu, select SAML 2.0 as the sign-in method.
5. Click **Next**.

### Step 2: Configure SAML integration for your Okta application

In this step, you'll configure the SAML integration for your Okta application.

**To configure SAML integration**

1. On the Create SAML integration page, under General settings, enter a name for your app, then click **Next**.
2. Complete the following fields:
   - **Single sign on URL:** https://*${yourDomainPrefix}*.auth.***$**{region}*.amazoncognito.com/saml2/idpresponse
   - **Audience URI (SP Entity ID):** urn:amazon:cognito:sp:
     *${yourUserPoolId}*

     Replace *${yourDomainPrefix}*, *${region}*, and *${yourUserPoolId}* with the values for your user pool.
   - Under ATTRIBUTE STATEMENTS (OPTIONAL), add a statement with the following information:

     | | |
     | --- | --- |
     | **SAML attribute Name** | **Value** |
     | http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress | user.email. |
   - Leave the other settings as their default values or set them according to your preferences.
3. Click **Next**, then click **Finish**.

### Step 3: Assign users to your application

In this step, you'll assign users to the application you created in step 1.

**To assign users to your application**

1. On the Assignments tab for your Okta app, under Assign, select **Assign to People**.
2. Click **Assign** next to the user that you want to assign.
3. Click **Save**, then click **Go back**.

   Your user is now assigned.
4. Click **Done**.

## Step 4: Specify the identity provider to be used for agent authentication

In this step, you'll add an identity provider to authenticate your agents.

**To specify the identity provider**

1. On the sign on tab for your Okta app, find the identity provider metadata hyperlink, then right-click the hyperlink and copy it.
2. Sign in to the AWS account containing the Cognito userpool.
3. Navigate to Cognito and open the userpool.
4. Click the Sign-in experience tab, then click **Add identity provider**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/LM_cc_3.png)
5. On the resulting page, select **SAML**.
6. Under Set up SAML federation with this user pool, do the following:
   - **Provider name**: Enter a name for the identity provider without using any spaces in the name.
   - **Metadata document source**: Paste the Metadata URL from the previous step in the metadata endpoint URL field.
7. Under Map attributes between your SAML provider and your user pool, set the following attribute:

   | | |
   | --- | --- |
   | **User pool attribute** | **SAML attribute** |
   | email | http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress |
8. Click **Add identity provider**.

   At this point the required identity provider has been created. The last step in the Cognito configuration is to specify that the app client must use this identity provider.
9. Click the **App integration** tab, then click **app-client** at the bottom of the page.
10. In the app-client, in the Hosted UI section, click **Edit**.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/LM_cc_4.png)
11. Under Hosted sign-up and sign-in pages, click **Identity providers**, then select the identity provider that you configured in the previous step.
12. Click **Save changes**.

You'll need the name of the IDP (as configured under Sign-in experience) to complete the setup of your account. Include this along with the CloudFormation outputs information shared with Zendesk.
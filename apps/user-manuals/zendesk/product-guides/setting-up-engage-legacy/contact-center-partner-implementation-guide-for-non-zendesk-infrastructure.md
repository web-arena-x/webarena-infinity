# Contact Center partner implementation guide (for non-Zendesk infrastructure)

Source: https://support.zendesk.com/hc/en-us/articles/9907359706650-Contact-Center-partner-implementation-guide-for-non-Zendesk-infrastructure

---

Verified AI summary ◀▼

This guide helps you set up a Contact Center using non-Zendesk infrastructure. You'll learn about key components like Amazon Connect and Cognito, setting up users and access, and linking Connect with a CloudFormation stack. The guide also covers configuring call recordings, adding admin users, and installing the app, ensuring a smooth integration with your existing systems.

Important: The information in this guide is for customers who are not running Contact Center on the Zendesk infrastructure. If you're looking for help setting up Contact Center on Zendesk infrastructure, see [Getting started with Contact Center](https://support.zendesk.com/hc/en-us/articles/9824150119450). If you're not sure which infrastructure you're on, contact [Zendesk Customer Support](https://support.zendesk.com/hc/en-us/articles/4408843597850).

This article helps you get up and running with Zendesk for Contact Center. Some of the processes mentioned below might need to be carried out by the Zendesk Professional Services team.

This article contains the following topics:

- [Understanding Contact Center components](#final_cc_understanding_components)
- [Setting up Amazon Connect for Contact Center](#final_cc_set_up_connect)
- [Linking Connect and Contact Center with a CloudFormation stack](#final_cc_link_cc_and_connect)
- [Setting up Contact Center users and access](#final_cc_users_access)
- [Configuring Contact Center to send call recordings to Zendesk (writeback)](#final_cc_writeback)
- [Adding a Contact Center admin user](#final_cc_add_admin_user)
- [Configuring allowed domains for Contact Center](#final_cc_allowed_domains)
- [Installing and configuring the Zendesk for Contact Center app](#final_cc_install_app)
- [Testing Contact Center](#final_cc_testing)
- [Next steps](#topic_wg3_ncc_vgc)

## Understanding Contact Center components

Before you start setting up Contact Center, it’s important to know the key building blocks of Contact Center and how they interact.

The following are the key components that make up your organizations contact center:

- **Amazon Connect** is AWS’s cloud contact center that powers Contact Center. It manages calls, chats, queues, and contact flows. Each Contact Center customer must run a Connect instance in their own AWS account, and a Contact Center account can link to only one Connect instance.
- **Amazon Cognito** is an AWS managed authentication service for web and mobile apps, handling sign-up, sign-in, and access control. For Contact Center, it hosts the *user pool* for agents, supervisors, and admins, securely managing passwords and logins so users can access the Contact Center app in Zendesk. The integration automatically creates this user pool using CloudFormation, avoiding a custom identity system.
- **Amazon CloudFormation** automates AWS setup with templates, deploying all resources and permissions for the Connect and Contact Center integration in a single stack. Think of it as an installer: the stack provisions and configures the components that let Amazon Connect and the Contact Center app work together, saving time and reducing errors.
- **The Zendesk Contact Center app** is a contact-center-as-a-service platform from Zendesk that works with Amazon Connect, adding an omnichannel inbox, AI-assisted tools, and advanced dashboards. Agents sign in to Contact Center to handle calls and messages, and these are handled by the customer’s own Connect instance.

 The app is deployed in the customer’s AWS environment using CloudFormation, so Contact Center data (for example, call recordings and customer information) stays in the customer’s environment, not on Zendesk servers. After linking the Connect instance and deploying the stack, Contact Center and Connect function as a unified solution.
- **Dual-stack upgrade process:** Upgrades use a *dual-stack* approach: instead of updating the existing CloudFormation stack, deploy a new stack from the latest template, switch Contact Center to it after testing, then retire the old stack. This ensures a safe rollback point, since in-place CloudFormation rollbacks can fail (for example, due to permissions). Dual-stack is the only supported upgrade path. To begin an upgrade, request the updated template URL from Zendesk and create the new stack in the customer’s AWS account.

## Setting up Amazon Connect for Contact Center

Amazon Connect is the platform on which Zendesk Contact Center runs. You must have a Connect instance to use Contact Center. Connect instances are created in the AWS Management Console. Generally, you'll create the Connect instance in the AWS region closest to your customer or as required.

Note: Not all regions support Connect, so you must choose from the supported list.

You can create a Connect Instance using a CloudFormation template, or manually.

This article contains the following topics:

- [Setting up Connect using a CloudFormation template](#topic_jl2_4x3_xgc)
- [Setting up Connect manually](#topic_q3q_px3_xgc)

### Setting up Connect using a CloudFormation template

When you use a CloudFormation template to set up Connect, much of the setup process is automated. During this step, you can also turn on single-sign-on (SSO) for Connect.

**(Optional) To turn on single sign-on for Connect instances**

1. Configure an application in your IdP with SAML authentication turned on.
2. Download the SAML metadata xml file.

   The value for Relay state in the application can be left blank and updated after your Connect instance is set up.

The template turns on SAML SSO on the Amazon Connect instance. If your SAML IdP app is already configured and you provide its metadata during deployment, the stack automatically provisions the IAM resources to integrate Connect with that IdP.

**To deploy the Connect instance template**

1. In the AWS console, navigate to the Cloudformation service.
2. Click **Create stack**, then enter the following Amazon Simple Storage Service (S3) URL:

   <https://zendesk-contact-center-us-east-1.s3.amazonaws.com/connect/cfn.yaml>

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_1.png)
3. Enter a unique value for InstanceAlias and paste the entire contents of the metadata xml file in the SamlXmlDocument field if you configured it, or else leave the field blank.

   Note: If you encounter an error that the metadata file is too large, leave the SamlXmlDocument parameter blank to complete the CloudFormation stack deployment, then setup the SAML configurations manually afterwards.
4. Click **Next** and complete the stack deployment.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_2.png)
5. Finally, note the SamlRelayState from the stack outputs and update the relay state in the SAML application configured in your SSO for your Connect instance.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_3.png)

The following resources are provisioned by the template:

- Connect Instance
- S3 bucket for transcripts
- KMS key for S3 bucket
- Kinesis Stream
- Customer Profiles domain
- KMS Key for Customer Profiles domain
- SAML Identity Provider in IAM
- IAM Role for SAML

### Setting up Connect manually

If you don't want to automatically create your Connect instance, you can configure it manually.

**To manually create a Connect instance**

1. Sign into the AWS console and open the Connect service.
2. On the Amazon Connect virtual contact center instances page, click **Add an instance**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_4.png)
3. Choose your preferred identity management method (usually, **SAML 2.0-based authentication** for client environments).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_5.png)
4. On the Set identity page, enter your Access URL and instance name.
   This name will become part of the instance’s URL. For example, if you name it 'MyDemoConnect', the instance URL will look like MyDemoConnect.awsapps.com/connect/). Choose a name that identifies the client or purpose (for example, *ClientName-ConnectEU*).
5. Specify whether an admin user for Connect needs to be created. For simplicity, you can create an admin username and a password. This will be the login used to access the Connect dashboard initially. In real deployments, customers often integrate with their single sign-on using SAML, but for training and sandbox purposes a manual admin user can be created.
6. Under Telephony and data settings, configure how the contact center will handle communications and store data:
   - **Telephony Options:** You can turn on inbound or outbound calling or both. For most uses, turn on both inbound and outbound calling (so the instance can receive and make calls).
   - **Data Storage:** Connect creates an Amazon S3 bucket to store call recordings, chat transcripts, and other data. In the setup wizard, make sure that the option: Enable customer profiles” is turned on.

     We recommend that the profile creation policy is set to Associate only.
7. Turn off Enable email. It's not used in Contact Center.
8. Uncheck Custom data storage (Advanced).
9. Continue through the wizard, reviewing the settings on the final page. Once everything looks good, click **Create instance**. Connect will begin provisioning the instance. It usually takes a a few minutes for the instance to be ready. During this time, AWS is setting up the service and resources in the background.

   Note: Avoid closing the browser or navigating away until setup is complete, to prevent any interruption. The creation process is fairly fast and robust, but it’s a good practice to wait.

   When the creation finishes, the AWS console shows your new instance.
10. If you didn't configure SSO, click **Access URL** (the instance URL) to open the Connect sign in page. Use the admin username and password you created to sign in.

    This opens the Connect dashboard, a web-based interface where you can manage your contact center. When you first sign in, you might see some default sample contact flows and a basic dashboard screen.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_gd_111.png)

    Note: If you set up SSO for login and authentication, you must complete the steps in [Setting up Contact Center users and access](https://support.zendesk.com/hc/en-us/articles/9459094577562) before you can sign in to the Connect environment.
11. Make sure that nsure that Kinesis data streaming is turned on in the new Connect instance. In the AWS Console, navigate to the new Connect instance > **Data Streaming** > **Enable data streaming** and be sure to select **Kinesis stream** and create a new stream if needed.

    Tip: Make sure to turn on *Kinesis data streaming*, not *Kinesis firehose*.
12. Click **Save**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_6.png)

You now have a working Amazon Connect instance.

Note: It is the AWS account owners responsibility to ensure that service limit increases are logged with AWS as required, for example, concurrent call limit, number of numbers that can be claimed, and whitelisting outbound countries.

## Linking Connect and Contact Center with a CloudFormation stack

To link Connect and Contact Center, use a CloudFormation stack provided by Zendesk. The stack is a pre-defined set of AWS resources and configurations that sets set up everything you need for the integration. This includes linking Connect with other AWS services such as Amazon Cognito for user management, Amazon Kinesis for streaming contact data, AWS Lambda functions for any custom logic, as well as establishing trust between Connect and the Contact Center app.

Before you start, make sure you have the following:

- Access to the Contact Center Admin app, with permission to access the relevant instance.
- Someone with access to the AWS Console will need to perform part of the process, Depending on the customer’s ability to share access, this could be a Zendesk employee or a member of the customer team.

This article contains the following topics:

- [Deploying the CloudFormation stack](#topic_szk_kpj_zgc)
- [Performing post-stack steps](#topic_dzz_npj_zgc)

### Deploying the CloudFormation stack

There are three scenarios in which a CloudFormation stack must be installed:

- A new Contact Center instance that has never had a CloudFormation stack installed.
- An existing Contact Center instance that has had a CloudFormation stack installed via the legacy (non-admin app) method.
- An existing Contact Center instance that has had a CloudFormation stack installed via the current (admin app) method.

The deployment process is similar for each of the above scenarios, with the differences being how automated the process is and how much manual review or updates might be required.

**To deploy the CloudFormation stack**

1. In the account admin console, for the newly created account, click **Create stack**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_gd_113.png)
2. Provide the required details for the CloudFormation template.
   - **Stack name:** A name for the CloudFormation stack.
     You can choose something such as: <*Account name*> + “CF” + “07-30-2025”. We recommend including a date in the stack name to help you remember when the stack was installed.
   - **Stack region:** This is the region in which you will deploy your CloudFormation stack.
   - **Amazon Connect instance ARN:** Enter the ARN (Amazon Resource Name, a unique identifier for AWS resources) of the Connect instance you created. You can find this in the AWS console on the Amazon Connect service, on the instance details page. Look for the *Instance ARN* (it typically looks like arn:aws:connect:region:account-id:instance/xxxxxxxx-xxxx-....). Copy this value from AWS and paste it into this field in the admin console. For more information, [see the AWS documentation](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html).
   - For new installations, configure the following:
     - Click **New setup**.
     - For the domain prefix, enter the URL domain of your Connect account.
     - Access your Connect account by navigating to the Account overview section from the Access URL which will have the following form:
       https://YOUR\_DOMAIN\_PART.my.connect.aws.
     - Copy the <*YOUR\_DOMAIN\_PART*> section and use it to fill in the domain profile section.
3. For existing installations, configure the following:
   - Select Use an existing user pool and app client.
   - Enter the User pool ID and App Client ID that are being used in AWS.
4. Configure the following:
   - **Dashboard and analytics:** Select **Enabled**.

     This is turned on by default and will remain turned on unless you turn it off. This turns on data flowing into the Contact Center dashboards app, which is a separate free app available from the Zendesk Marketplace.
   - **Resource tags:** These are optional.
5. After filling in the necessary fields, click **Launch stack**.

   In the pop-up page, you have two options:
   - **Automated launch:** After creating the CloudFormation stack, you will be automatically redirected to the AWS CloudFormation console with the template ready to deploy. This is convenient if you or someone on your team has access to the customer’s AWS account with sufficient permissions.
   - **Manual template copy:** If you don't have direct access to the AWS account, click **Copy instructions to clipboard** to export the CloudFormation template (usually as a JSON or YAML file or a link). This link or export can then be used by the relevant team with AWS access to implement the CloudFormation stack.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_gd_114.png)
6. A new browser tab opens on the AWS CloudFormation Quick create stack page with the template already loaded. The stack name and parameters are filled in with the values you provided.
7. Scroll down to the bottom of the page and, in the Capabilities and transforms section, check and mark all the acknowledgments.
8. Click **Create stack**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_7.png)

   Once initiated, CloudFormation will start creating resources. In the AWS CloudFormation console, you can watch the progress. It will list events such as “CREATE\_IN\_PROGRESS” for various components. This process can take a few minutes. The stack is doing a lot in the background: setting up IAM roles and policies, Lambda functions, Kinesis data streams, Amazon Cognito user pool and groups, Connect settings, and more . Typically, this completes without intervention. The status will change to **CREATE\_COMPLETE** when the process completes.

   While it runs, do not close the stack page.

   Tip: You can refresh your web browser to see updates, but we recommend waiting for the stack to complete. If the stack fails, it will roll back (you’ll see a status such as ROLLBACK\_COMPLETE).
   If you have any problems, see [Troubleshooting Contact Center](https://support.zendesk.com/hc/en-us/articles/9696137463066).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_8.png)
9. When the CloudFormation stack shows **CREATE\_COMPLETE**, the integration is complete. The CloudFormation template automated the previously manual steps. At this point, the following is in place:
   - An **Amazon Cognito user pool** (and associated identity pool, if applicable) specifically for this Contact Center instance’s users.
   - An **LMAdmin user group** in Cognito (created by the stack) that will be used to designate admin users in Contact Center.
   - AWS **Lambda functions** or other services for features such as transcription, bots, and others, connected between Connect and Contact Center (the exact resources depend on the template scope).
   - **IAM Roles/Permissions** that allow Zendesk’s platform to access the Connect instance (within the limits needed) and vice versa, without exposing unnecessary access.
   - Connect might need configuration adjustments using the API, for example, attaching Amazon Lex bots or setting up flow modules if the product requires, though these are optional, or configured later.

Now, the Connect account, the Contact Center account, and the CloudFormation resources are in place and connected.

### Performing post-stack steps

Once the stack begins deployment, it will show in the Still deploying state. While in this state, you can click **Check status** to check the status of the stack deployment. When it's fully deployed, it will display Ready to activate.

After the stack is complete, the Zendesk admin portal will now show that the new stack for the account is ready to be activated. Generally, once the AWS setup is complete, the Contact Center platform is ready to go live with that Connect instance.

- Once you are ready to link the new stack, click **Activate**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_guide_100.png)

## Setting up Contact Center users and access

Users in Amazon Connect are the agents and supervisors who manage your contact center. You can add users manually or by importing them in a CSV file. Each user has attributes that determine their roles and capabilities. The high-level requirement for configuring SSO is summarized and can be used as guidance for configuration of any new SAML providers that have not yet been documented.

Contact Center leverages Amazon Cognito for agent authentication, including single sign-on (SSO). The benefits of this approach are:

- No agent data is stored in the Zendesk environment. All agent data is stored in Amazon Cognito in the client's own AWS account.
- Amazon Cognito caters for user pools where users can manually be created.
- Amazon Cognito caters for SAML federation, which enables SSO, with most SAML providers.
- A SAML application (and an associated XML configuration file) is required.

Note: To set up single sign-on (SSO) for Connect, configure the SAML application in the IAM Identity Center, which is often in a separate AWS account and region.
However, the identity provider, role, and policy are established in the same AWS account as Connect.

This article contains the following topics:

- [Understanding required SAML application settings](#topic_l4s_wv3_zgc)
- [Manually adding users using Cognito user pools (if you're not using SAML/SSO)](#topic_syc_1z3_xgc)
- [Setting up users with SSO and SAML](#topic_lmp_xy3_xgc)
- [Setting up SSO with other services](#topic_owr_x53_zgc)

### Understanding required SAML application settings

Your SAML application must have the following settings:

| | |
| --- | --- |
| **Attribute** | **Value** |
| ACS URL | https://${yourDomainPrefix}.auth.${region}.amazoncognito.com/saml2/idpresponse |
| Application SAML audience | urn:amazon:cognito:sp:${yourUserPoolID} |
| Application start URL (optional) | Contact Center login URL |

The SAML application must have the following two SAML attributes:

| | | |
| --- | --- | --- |
| **SAML Attribute** | **Maps to this string value or user attribute** | **Format** |
| Subject | ${user:email} | Persistent |
| http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress | ${user:email} | |

Configure the identity provider in Cognito with the following attributes:

| | |
| --- | --- |
| **User pool attribute** | **SAML Attribute** |
| email | http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress |

### Manually adding users using Cognito user pools (if you're not using SAML/SSO)

When the CloudFormation stack ran, it created an Amazon Cognito user pool for this Contact Center instance. The user pool is a directory of user accounts who can authenticate to Contact Center. It likely also created an app client in Cognito (which the Contact Center app uses to allow users to lsign in), and an LMAdmin group for admin permissions. Next, you'll create at least one user in this user pool, so you can test signing in to Contact Center.

**To manually add a user**

1. In the AWS console, open the Cognito service.
2. Click the use pool you want to manage.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_gd_115.png)
3. On the Login pages tab of the app client setting, edit the Managed login pages configuration.
4. Change the Identity Provider to be the Congito user pool directory.
5. In the Cognito user pool console, find the section for Users” and click **Create user** (or **Add user**).
6. Enter the following details for the new user account:
   - **Username:** Choose a username (for example, the person’s email address or a simple name).
   - **Temporary Password:** Set an initial password for the user. (Cognito might require the user to reset the password on first sign in, but for internal testing you can set a simple password and, optionally, turn off the reset requirement).
   - **Contact Info:** Depending on settings, you might need to provide a valid email address and/or phone number for the user (these can be used for password recovery or multi-factor authentication).
   - **Account Status:** Make sure that Mark phone/email as verified is checked if you provided those and don’t want Cognito to expect a verification step. Also, check Temporary password so the user must change it on first sign in (for production users).
   - **Create the user:** The new user will now appear in the user list for the pool.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_gd_116.png)

This user represents an agent (or admin) who can log into the Contact Center web app.

### Setting up users with SSO and SAML

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_10.png)

### Setting up SSO with other services

The following resources provide additional information about setting up SSO with various services:

- [Amazon Web Services (AWS)](https://support.zendesk.com/hc/en-us/articles/9459034190746)
- [Azure AD](https://support.zendesk.com/hc/en-us/articles/9696124990106)
- [Okta](https://support.zendesk.com/hc/en-us/articles/9459046854938)
- [Google Workspaces](https://support.zendesk.com/hc/en-us/articles/9696174588954)
- [Cognito Userpools](https://support.zendesk.com/hc/en-us/articles/9459000058010)

## Configuring Contact Center to send call recordings to Zendesk (writeback)

To allow Contact Center to send call recordings back to Zendesk after a call (known as *writeback*), configure speech analysis in Contact Flow, and turn on the voice post call Lambda in AWS.

Tip: A *Lambda* is a small piece of code, stored on Amazon servers, that can be run on-demand.

This article contains the following topics:

- [Configuring speech analysis in Contact Flow](#topic_onw_z24_zgc)
- [Turning on writeback](#topic_akm_1f4_zgc)

### Configuring speech analysis in Contact Flow

The first part of setting up writeback is to configure speech analysis in your Contact Flow.

**To configure speech analysis**

1. In your Amazon Connect Contact Flow, ensure the Set recording and analytics behavior block is included in the flow.

   ‍![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_wb_1.png)
2. In the Set recording and analytics behavior block, enable Contact Lens speech analytics and set it to Real-time and post-call analytics.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_wb_2.png)
3. Under Redaction, select Redact sensitive data and customize the redaction settings as needed.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_wb_3.png)

Note: The data redaction is strict and could potentially redact non-sensitive data. Best practice is to only select critical sensitive data to be redacted.

### Turning on writeback

Next, configure your Lambdas, the triggers that will let you write the call transcript to a Zendesk ticket.

**To turn on writeback**

1. In your Amazon Console, navigate to the Lambdas page.
2. In the Functions section, search for "post". This returns a function with a name containing "VoicePostCa".
3. Click this function, and on the Function overview page, select **Configuration** > **Triggers** from the navigation menus.
4. Select the ‍Contact Center Zendesk Voice Post Call Lambda function.
5. For **Kinesis**, select its checkbox, then click **Edit**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_16.png)
6. On the Edit trigger page, select Activate trigger.
7. Click **Save**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_17.png)
8. Click the blue hyperlink next to **EventBridge**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_18.png)
9. On the **EventBridge** rule details page, click **Enable**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_19.png)

After these steps have been completed, your call transcripts from Contact Center voice calls will be shown in your Zendesk tickets.

Note: If a dual stack upgrade is performed, these triggers must be turned off on the old Lambda, and only then turned on for the new Lambda. See [Understanding Contact Center components](https://support.zendesk.com/hc/en-us/articles/9829206009242).

## Adding a Contact Center admin user

By default, newly created users are regular users. If a user has admin privileges in Contact Center (meaning they can configure Contact Center settings, view dashboards, and so on), they must be added to the LMAdmin user pool group that was created with the CloudFormation stack.

**To add a Contact Center admin user**

1. In the Amazon Cognito user pool, go to Groups. You'll see a group named LMAdmin.
2. Click the LMAdmin group and add your new user to the group.

.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_gd_117.png)

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_gd_118.png)

If you use SSO, the users available to add to this group are only created after they have successfully signed into Contact Center at least once. Once added, the user will gain access to the settings and dashboard pages in Contact Center.

Note: Connect provides the core contact center capabilities that Contact Center builds on.

## Configuring allowed domains for Contact Center

Amazon Connect includes a security setting that controls which web origins (domains)
are allowed to embed or access Connect streams (for example, the agent phone interface). Since Contact Center is a separate app that links to Connect, you must whitelist the Contact Center domain in the Connect instance settings. This ensures that when an agent uses Contact Center, Connect recognizes it and permits the connection.

**To configure approved origins**

1. In the AWS console, open the Amazon Connect service.
2. In Connect, click your instance name.
3. In the Approved origins section for your instance, enter the origin (domain URL)
   for the Contact Center web app that agents will use. Typically, Contact Center is accessed via a web app URL.
4. Add your Zendesk subdomain address:
   - https://<*subdomain*>.zendesk.com
5. Click **Save**. Connect now trusts requests coming from this domain.

If you skip this step, when a user tries to sign into Contact Center, and it attempts to open the Connect stream or perform actions using the Connect APIs, it might get blocked due to CORS (cross-origin request) restrictions. Whitelisting the domain prevents that issue. You must do this once for each Connect instance and integrating app.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_14.png)

## Installing and configuring the Zendesk for Contact Center app

The Zendesk for Contact Center app is the interface your agents use to make, receive, and manage Contact Center calls and chats. In this article, you'll learn how to install and configure the app.

This article contains the following topics:

- [Installing the Contact Center app](#topic_sfg_jvh_zgc)
- [Configuring the Contact Center app](#topic_hk4_jvh_zgc)

### Installing the Contact Center app

You install the Contact Center app from a link Zendesk generates for you.

**To install the Contact Center app**

1. [Request](https://support.zendesk.com/hc/en-us/articles/4408843597850) your legacy Contact Center app’s installation link. Zendesk uses your Zendesk domain to generate a link for you.
2. Once you receive the link, access it to install the app. For more details, see [Installing apps](https://support.zendesk.com/hc/en-us/articles/4408824421146#topic_n2x_hzw_15).
3. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Apps > Zendesk Support apps**.
4. Click the Contact Center app you just installed.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_gd_122.png)
5. Update the following settings using your existing Contact Center instance URL:
   - **Title:** Typically, use the suggested name.
   - **Contact Center workspace:** Once you've set up your Contact Center environment, you can retrieve the workspace value from the URL of your standalone Contact Center environment.
   - **Zendesk for Contact Center region:** Once you have your Contact Center environment set up, you can retrieve the region value from the URL of your Contact Center environment. For example:

     | AWS region | Engage region |
     | --- | --- |
     | ap-southeast-2 | apse2 |
     | ca-central-1 | cac1 |
     | eu-central-1 | euc1 |
     | eu-west-2 | euw2 |
     | us-east-1 | use1 |
   - **Enable role restrictions:** Restrict Contact Center access to specific roles.
   - **Enable group restrictions:** With this optional setting you can limit specific groups to have access to the Contact Center app.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/implementation_guidez_3.png)
6. Click **Update**.

The Contact Center app icon is now displayed in the top right corner of your Zendesk instance.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_login_1.png)

### Configuring the Contact Center app

Now that you've installed the Contact Center app, you can configure its settings.

**To configure the Contact Center app**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **APIs > API tokens**.
2. Click **Add API token**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_gd_124.png)
3. On the Add API token page, enter a descriptive name for the token, for example, "Connect Contact Center to Zendesk".
4. Click **Save**.

   Copy the token string and keep it handy for the next steps.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_gd_125.png)
5. In Contact Center, click the settings icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_settings_icon.png)), then click **Admin settings**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_gd_126.png)
6. Click the Zendesk settings icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zendesk-icon_cc.png)). You'll see helpful information about getting your Contact Center app connection to your Zendesk account.
7. Expand the Your Zendesk account panel, then click **Edit.**

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_gd_127.png)
8. In the **API key** field, paste the API key you copied previously.
9. In the **Zendesk user email** field, enter your Zendesk admin email address.
10. Click **Connect account**.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_gd_128.png)

    You'll see a page that helps you set up your creation rules for Zendesk tickets, as well as how transcripts and recordings will be handled. If you're not sure what to enter, you can configure these items later.
11. Click **Complete**.

    The Contact Center app and your Zendesk account are now linked.
12. In your Zendesk environment, perform a hard refresh of your browser.
13. Click the phone icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_zenphone.png)) to open the Contact Center app.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_gd_129.png)
14. Click **Continue**.
15. Sign in using the authentication process set up for your account.
16. Perform a test call by setting up a new number in the Connect dashboard, linking it to a new or preconfigured contact flow, and confirming whether the call reaches your agent in Zendesk through the app.

## Testing Contact Center

Once you've finished setting up Contact Center as described in [Getting started with Contact Center](https://support.zendesk.com/hc/en-us/articles/9824150119450), you can test it to make sure everything is working.

**To test Contact Center**

1. Sign out of the Contact Center admin console and navigate to the Contact Center agent login page, https://${Zendesk Instance Name}/agent.
2. Sign in with SSO or the user credentials you set up in Amazon Cognito (username and password).

   You'll now be in the Contact Center interface. This app links to Connect in the background (using the allowed origin you set and the integration configuration you deployed). If your Connect instance is new, there might not be much to see yet (until you set up a phone number or chat). However, you can verify connectivity by seeing if the Connect softphone and agent status controls load in Contact Center.

   For example, you might see your Connect agent status indicator in Contact Center and be able to change status or make a test outbound call if you've claimed a number. This indicates the integration is working.

If you're having problems, see [Troubleshooting Contact Center](https://support.zendesk.com/hc/en-us/articles/9696137463066).

## Next steps

Now you've completed the installation, here are some useful resources to get you started using Contact Center.

- [Accessing workflows in Contact Center](https://support.zendesk.com/hc/en-us/articles/9459009706266)
- [Contact Center general integration settings](https://support.zendesk.com/hc/en-us/articles/9611882665754)
- [Mapping and displaying Contact Attributes](https://docs.google.com/document/d/1IdcwY_ArKErKbV8tfANDLdrndmoVIGsd95n6KVyrmxY/edit?usp=sharing)
- [Manually associating Contact Center calls to tickets](https://support.zendesk.com/hc/en-us/articles/9611893524634)
- [Accessing call recording and transcription settings in Contact Center](https://support.zendesk.com/hc/en-us/articles/9459045766170)
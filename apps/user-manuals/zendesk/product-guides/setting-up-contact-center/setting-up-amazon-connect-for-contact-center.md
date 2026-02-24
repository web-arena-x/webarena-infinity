# Setting up Amazon Connect for Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9696121369370-Setting-up-Amazon-Connect-for-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Set up Amazon Connect for your contact center by creating a new instance in the AWS Management Console. Choose between automatic setup with a CloudFormation template or manual customization. Ensure SAML authentication, telephony options, and data streaming are configured. If using an existing instance, verify identity management and customer profiles are enabled. Each client requires a unique instance for optimal functionality.

Tip: If you already have a Connect instance, you can skip this step.

The first step is to create a new Connect instance. You create Connect instances in the AWS Management Console. Generally, you will create the Connect instance in the AWS region closest to your customer or as required.

Note: Not all regions support Connect. You can see [the available regions](https://docs.aws.amazon.com/connect/latest/adminguide/regions.html#amazonconnect_region) on the AWS website.

You can create the Connect instance automatically by using a CloudFormation template, or, if you want to customize it, you can create it manually.

This article contains the following topics:

- [Automatically creating a Connect instance from a CloudFormation template](#topic_ngh_xyf_3gc)
- [Manually creating a Connect instance](#topic_y4g_bzf_3gc)

## Automatically creating a Connect instance from a CloudFormation template

In this section, you'll discover how to create a Connect instance from a CloudFormation template. You'll need the information provided by Zendesk in the previous section to proceed.

A Connect instance created using a CloudFormation template will have SAML authentication turned on. If an application is already configured on the SAML Identity Provider (IdP), and the metadata file is available during the deployment of this template, the template will configure all required Identity and Access Management (IAM) resources to integrate your Connect instance.

**To automatically create a Connect instance**

1. (Optional) To turn on single sign-on for Connect instances, configure an application in your IdP with SAML authentication turned on. Once the application is configured, download the SAML metadata XML file.

   Note: The value for relay state in the application can be left blank. This can be updated after the Connect instance is set up.
2. Navigate to the CloudFormation service in the AWS console.
3. Click **Create stack**.
4. On the Create stack page, select the following:
   1. Choose an existing template
   2. Amazon S3 URL
5. In the Amazon S3 URL field, enter the following URL:

   <https://zendesk-contact-center-us-east-1.s3.amazonaws.com/connect/cfn.yaml>
6. Click **Next.**

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_1.png)
7. On the Specify stack details page, enter a name for the stack, a unique value for InstanceAlias.
8. If your SSO application is already configured, copy and paste the contents of the metadata XML file under SamlXmlDocument. This parameter can be left blank if the SAML application is not yet configured.

   Note: If you encounter an error that the metadata file is too large, leave the SamlXmlDocument parameter blank to complete the CloudFormation stack deployment, then set up the SAML configurations manually later.
9. Click **Next** to complete the stack deployment.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_2.png)
10. Optionally, configure your SAML application to your Connect instance. Note the SamlRelayState from the stack outputs and update the relay state in the SAML application configured in your SSO for your Connect instance.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_3.png)

When the stack runs, the template creates the following resources:

- Connect Instance
- S3 bucket for transcripts
- KMS key for S3 bucket
- Kinesis Stream
- Customer Profiles domain
- KMS Key for Customer Profiles domain
- SAML Identity Provider in IAM
- IAM Role for SAML

See your AWS documentation for more details about these resources.

## Manually creating a Connect instance

If you want to customize your Connect instance, you can manually create it.

**To manually create a Connect instance**

1. In your AWS console, open the Amazon Connect service. You’ll see a page listing any existing Connect instances in the selected region.
2. Click **Add an instance**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_4.png)
3. On the Set identity page, choose your preferred identity management method (typically SAML 2.0-based authentication for client environments).
4. Enter an access URL instance name. This name becomes part of the instance’s URL.

   For example, if you name it “MyDemoConnect”, the instance URL will resemble MyDemoConnect.awsapps.com/connect/. Choose a name that identifies the client or purpose, such as "ClientName-ConnectEU".
5. Click **Next**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_5.png)
6. On the Add administrator page, specify whether an administrator user for Connect needs to be created. To make things easier, you can create an admin username (for example, “admin”) and a password. This will be the login used to access the Connect dashboard initially. Customers often integrate with their single sign-on using SAML, but for training and sandbox purposes, you can configure a manual admin user.
7. Click **Next**.
8. On the Set telephony page, under Telephony and data settings, configure how your contact center will handle communications and store data:
   - **Telephony Options:** You can turn on inbound and/or outbound calling. For most uses, turn on both Inbound and Outbound calling (so the instance can receive and make calls).
   - **Data Storage:** Connect creates an Amazon S3 bucket in the background to store call recordings, chat transcripts, and other data. In the setup wizard, make sure that Enable customer profiles is turned on.
9. Click **Next**.
10. On the Data storage page, set the profile creation policy to Associate only.
11. Deselect the Enable email option. This is not used by Contact Center.
12. Make sure the Custom data storage (Advanced) option is unselected.
13. Click **Next**.
14. Complete the wizard and review the configuration. Once everything looks good, click **Create Instance**.

    Connect will begin provisioning the instance. It usually takes a couple of minutes for the instance to be ready.
    During this time, AWS is setting up the service and resources in the background.

    Important: To ensure successful installation, don't close your browser or navigate away from the status page until the provision completes.
15. When the creation is complete, the console will show your new instance. If you have set up the environment not to use SSO, you can click the Access URL (the instance URL), which opens the Connect login page. Use the admin username and password you set to log in. This will bring you to the Amazon Connect dashboard, a web-based interface where you can manage your contact center (configure contact flows, users, etc.). On first login, you might see some default sample contact flows and a basic dashboard screen. At this point, Connect is up and running.

    Important: If you have set up the environment to use SSO for login and authentication, you will need to complete the steps in [Setting up users and access](https://support.zendesk.com/hc/en-us/articles/9599145131034#topic_zdy_3nz_hgc)
    before you can log into Connect.
16. Before proceeding to create the Contact Center account or the CloudFormation stack, make sure that Kinesis Data Streaming is turned on in your Connect instance. In the AWS Console, navigate to your Connect instance, click **Data Streaming** > **Enable data streaming**, and select Kinesis Stream. Create a new stream if needed.

    Tip: Make sure to turn on "Kinesis data streaming" and not "Kinesis Firehose".
17. Click **Save**.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ig2_6.png)

You now have a Connect instance. Every client needs their own Connect instance to use Contact Center.

Note: It is the AWS account owners responsibility to ensure that service limit increases are logged with AWS as required, for example, concurrent call limit, number of numbers that can be claimed, and whitelisting outbound countries.

If you're using an existing Connect instance, make sure the following are configured:

- An identity management method
- Customer profiles are turned on
- The profile creation policy is set to Associate only
- Kinesis data streaming is configured
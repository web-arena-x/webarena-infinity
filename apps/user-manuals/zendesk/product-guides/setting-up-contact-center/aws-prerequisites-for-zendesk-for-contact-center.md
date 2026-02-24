# AWS prerequisites for Zendesk for Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9459105821210-AWS-prerequisites-for-Zendesk-for-Contact-Center

---

Before you set up Zendesk for Contact Center, you must configure specific components within your AWS account.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

To set up the Contact Center, configure your AWS account by creating an Amazon Connect instance, enabling customer profiles and data streaming, and adding approved origins. For web chat, enable attachments and set a CORS policy. If using cases, email routing, or smart tools, enable cases, configure a verified domain in Amazon SES, and select an AI provider like Amazon Bedrock or Azure Open AI.

Before you set up Zendesk for Contact Center, you must configure specific components within
your AWS account.

This article contains the following topics:

- [Configuring Amazon Connect](#topic_qvf_pnf_yfc)
- [Configuring cases, email, and smart
  tools](#topic_cs1_qnf_yfc)

## Configuring Amazon Connect

You must do the following to configure Amazon Connect:

- **Create the Amazon Connect instance**. The CloudFormation template requires the
  instance ARN (Amazon Resource Name) to be populated. See the Amazon Connect
  documentation to [create an Amazon Connect instance](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-instances.html).
- **Enable customer profiles** for the Amazon Connect instance. See the Amazon
  Connect documentation to [enable customer profiles](https://docs.aws.amazon.com/connect/latest/adminguide/enable-customer-profiles.html).
- **Enable data streaming** for the Amazon Connect instance and configure a valid
  Kinesis Data Stream for the Contact Trace Records events. See the Amazon Connect
  documentation to [enable data streaming](https://docs.aws.amazon.com/connect/latest/adminguide/data-streaming.html). Note that a Kinesis Data
  Stream is required, not a Kinesis Firehose.
- **Add the Zendesk for Contact Center URL as approved origins** for your Amazon
  Connect instance. To do so, go to AWS Console > Amazon Connect > Instance alias >
  Approved origins, then enter the following two entries. Be sure to substitute the region
  and workspace tags with the correct values. Within the Zendesk infrastructure:

  - https://${*Zendesk instance name*}
  - https://1162892.apps.zdusercontent.com
  - http://1162894.apps.zdusercontent.com

    Replace *Zendesk instance name*
    with your Zendesk subdomain. Example: https://demoinstance.zendesk.com.
- **Enable attachments**, if you are using web chat as a channel. See the Amazon
  Connect documentation to [enable attachments](https://docs.aws.amazon.com/connect/latest/adminguide/enable-attachments.html).

  If you enable
  attachments, you must configure a CORS policy for the S3 bucket where the attachments
  are stored. To do so, navigate to S3, then select the bucket. Click the Permissions
  tab, then paste the following configuration in the Cross-origin resource sharing
  (CORS) section. Be sure to substitute the region and workspace tags with the correct
  values.

  ```
  [
      {
          "AllowedHeaders": [
              "*"
          ],
          "AllowedMethods": [
              "PUT",
              "GET"
          ],
          "AllowedOrigins": [
              "https://${LMWorkspace}.my.connect.aws",
              "https://engage.${LMRegion}.localmeasure.com",
              "https://${LMWorkspace}.${LMRegion}.localmeasure.com"
          ],
          "ExposeHeaders": []
      }
  ]
  ```

## Configuring cases, email, and smart tools

You must do the following if you plan to use cases, email routing, or smart tools:

- **Enable cases** for the Amazon Connect instance, if you plan to use Amazon Connect
  cases. See the Amazon Connect documentation to [enable cases](https://docs.aws.amazon.com/connect/latest/adminguide/enable-cases.html).
- **Configure a verified Domain in Amazon Simple Email Services (SES)**, if you plan
  to use email routing. See [Corporate email routing](https://resources.localmeasure.com/articles/corporate-email-routing).
- **Select an AI provider**, either Amazon Bedrock or Azure Open AI, if you plan to
  use smart tools. See the [Smart tools prerequisites](https://resources.localmeasure.com/articles/smart-tools-prerequisites).
# Email: Auto-replies (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731449771034-Email-Auto-replies-Engage-Legacy

---

Local Measure Engage provides full email routing capabilities for Amazon Connect. A key benefit is that all emails are routed via Amazon Connect - and not brought into the agent desktop on the side - which means that all queue and agents reports are also available for the email channel.

Prerequisites

- Amazon Simple Email Services (SES) being configured correctly
- The Local Measure Engage CloudFormation stack having been deployed with the required information specified
- A Distribution flow having been specified in Local Measure Engage

‍

## Auto-replies

Some organizations require auto-replies to be sent to clients in order to acknowledge receipt of emails. This can be achieved by using a Lambda Function in the contact flow - which is used to route email - to send an email.

The below Python code snippet shows an example of how this can be achieved using Lambda:

```
<pre><code class="language-python">
import boto3

def lambda_handler(event, context):
    
    try:
        recipient = event['Details']['Parameters']['to']
        subject = event['Details']['Parameters']['subject']
        subject = 'RE: '+ subject
        
        #update the below with the message you want to send to the client
        body = "Replace with the message you want to send"
        
        # Create a new SES client
        ses_client = boto3.client('ses', region_name='us-east-1') #change to match the SES region you use
        
        # Specify the sender's email address
        # NOTE: the sender address MUST be configured as a verified identity in SES
        sender = 'noreply@myemaio.com' 
        
        # Send the email
        response = ses_client.send_email(
            Source=sender,
            Destination={'ToAddresses': [recipient]},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': body}}
            }
        )
        print('Email sent successfully!')
    except Exception as e:
        print('Error:', e)
</pre></code>
```

Note that the above is merely a snippet to get you started and that it will require updates.

‍

The above lambda can be invoked from a contact flow as illustrated below:

![](https://support.zendesk.com/hc/article_attachments/9731466306842)

Another option would be to configure email templates in SES and change the lambda code to use a template in order to send the auto reply. [This section](https://docs.aws.amazon.com/ses/latest/dg/send-personalized-email-api.html) in the SES admin guide provides the details on using email templates.
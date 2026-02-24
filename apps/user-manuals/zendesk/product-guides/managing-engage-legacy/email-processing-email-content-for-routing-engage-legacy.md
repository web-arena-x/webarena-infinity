# Email: Processing Email Content for Routing (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731498758426-Email-Processing-Email-Content-for-Routing-Engage-Legacy

---

Local Measure Engage provides full email routing capabilities for Amazon Connect. A key benefit is that all emails are routed via Amazon Connect - and not brought into the agent desktop on the side - which means that all queue and agents reports are also available for the email channel.

Prerequisites

- Amazon Simple Email Services (SES) being configured correctly
- The Local Measure Engage CloudFormation stack having been deployed with the required information specified
- A Distribution flow having been specified in Local Measure Engage

‍

### **Processing email content for routing**

Various aspects of the email can be used to make routing decisions. The simplest example of this is using the '\_hidden\_contact\_origin' (From email address) or '\_hidden\_contact\_destination' (To email address) to make routing decisions. The below image shows how the '\_hidden\_contact\_destination' attributes can be used to route emails sent to different email addresses to different queues:

![](https://support.zendesk.com/hc/article_attachments/9731449819290)

‍

In addition, the email content can also be evaluated in order to further enhance routing. In such a scenario a Lambda function is used to load and evaluate the email and to return values to Amazon Connect.

First, create a Lambda function that can load and evaluate the email. The below Python snippet shows how to fetch and load the email using the default Python [Email library](https://docs.python.org/3/library/email.html#module-email):

```
<pre><code class="language-python">
import json
import boto3
import email
import base64
from email import policy

###################          Important note.      ###########################
# 1) The execution role must be updated and will require S3 getObject access
# to the bucket storing the emails
# 2) If Comprehend is used to auto detect language then the execuation role
# must be updated to allow access to DetectDominantLanguage function in 
# Comprehend
#############################################################################

def decodeBase64String(str):
    base64_bytes = str.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message
    

def process_email(msg):
    #process the mail using the Python email library
    print('Processing email')
    #ADD YOUR CODE HERE
    
    return {
        'status' : 'OK'
    }
    

def lambda_handler(event, context):
    try:
        #get the base64 encoded emailID
        emailID = event['Details']['Parameters']['CC_emailID']
        #decode the base64 id to get the identifier that can be used to fetch this from S3
        emailID = decodeBase64String(emailID)
        
        #fetch the email onbject from S3
        bucketName = os.environ['EmailBucket'] #this is the bucket (SESBucketName) created by the Engage CloudFormation stack
        s3_client = boto3.client("s3")
        obj = s3_client.get_object(Bucket=bucketName, Key=emailID)
        
        #load the email message using the Python email library
        msg = email.message_from_bytes(obj['Body'].read(), policy=policy.default)
    
        #print("From="+msg['From'])
        #print("To="+msg['To'])
        #print("Subject="+msg['Subject'])
        
        return process_email(msg)
    except Exception as e:
        print("Exception in lambda_handler ->")
        print(str(e))
        response = {
            'status': 'FAIL'
        }
</pre></code>
```

Third-party open source libraries such as [html2text](https://pypi.org/project/html2text/) or [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) can be used to convert HTML based email bodies to text. Once the text has been extracted, the standard Python [Regular Expression library](https://docs.python.org/3/library/re.html) can be used for e.g. keyword spotting. Other options include using Amazon Comprehend for language detection or topic modeling to more accurately route based on the content of the email.

To invoke the lambda function, add a Lambda block to the contact flow as shown below:

![](https://support.zendesk.com/hc/article_attachments/9731498786970)

Ensure to change the 'Destination Key' name to match the name of the variable expected in your Lambda code. Specify the Value to be dynamic and set the key to '\_hidden\_key' as shown above. The '\_hidden\_key' attribute contains the required information of where the email is stored in S3.

‍
# Updating Contact Attributes with Contact Lens Rules (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731439519898-Updating-Contact-Attributes-with-Contact-Lens-Rules-Engage-Legacy

---

For enhanced customer engagement and satisfaction, there are instances where agents require assistance during active calls or chats. This assistance can be automated using Connect Contact Lens, which can process voice streams and chat transcripts in real-time and respond to predefined scenarios set by contact centre managers.

For instance, if a customer expresses dissatisfaction about a delivery delay (the running example that we will use in this document), the system can swiftly detect this issue and provide agents with optimal instructions to placate the customer, reassuring them that the matter is being addressed. This capability can be extended to various specific requirements for notifying agents about Connect Contact Lens detections or suggestions.

In Engage, we support not only standard Connect Contact attributes but also Label/Panel/Button attributes. This document outlines the solution for applying these attributes along with Connect Contact Lens to automatically assist and notify agents.

## Contact Attributes

Standard attributes are excellent for providing agents with context about the contact they are managing. Engage provides Label and Panel attributes, which are essentially the standard contact attributes but presented with a distinctive and noticeable appearance.

These attributes can be tailored to use a variety of colour themes and icons. Label attributes (shown in orange in the sample figure below) are excellent for concise pieces of information like status updates. Panel attributes (displayed in blue in the sample figure below) are ideal for longer pieces of information that extend across multiple lines and need extra formatting.

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731467555226)

For comprehensive guidance on configuring label and panel attributes within Engage, we recommend consulting the following resources

- [Label attributes](https://support.zendesk.com/hc/en-us/articles/9696142331034)
- [Panel attributes](https://support.zendesk.com/hc/en-us/articles/9731475641498)

## Engage Button Attribute

As depicted in the below sample figure ("View Ticket" and "Some other action" buttons), Engage also enables the creation of buttons that link to external URLs in new browser tabs.

- You can have the freedom to create as many buttons as needed.
- These buttons will appear in Active Contacts and Historical.
- URLS are not validated by Engage.
- Clicking on links will open the link in a new tab.

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731500411418)

For more information, please refer to the section "Button contact attributes" in : [Displaying attributes to agents](https://support.zendesk.com/hc/en-us/articles/9731466218650)

## Architecture

To react to events published by Connect Contact Lens Rules, we need to deploy this solution in AWS. The overall solution architecture is illustrated below:

The steps include:

1. **Create Connect Contact Lens Rule** with an action type of publishing an EventBridge event. This rule is designed for real-time call/chat conditions, ensuring that contact attributes are promptly updated (near real-time) immediately after the rule is triggered by Connect Contact Lens.
2. **Create a Lambda function** to handle the actions, specifically updating the contact's Standard/Label/Panel attributes. This ensures that agents will see these updates in real-time in the middle of Engage.
3. **Create an EventBridge rule** with a target of the Lambda function.

By following these steps and deploying this architecture, updates to contact attributes will be handled swiftly and seamlessly, providing real-time insights for agents during engagement.

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731439554714)

‍

‍

‍

‍

### Create Connect Contact Lens Rule

1. Navigate to the Rules section under Contact Lens, under the Analytics and Optimization Menu.
2. Click on "Create a rule".
3. Choose "Conversational analytics".
4. In the "When" dropdown, choose "A contact lens real-time call (or chat) analysis is available". In this example, we select "Chat".
5. Click "Add Condition" and select the condition you wish to apply to contacts. In our example, we choose "Words or Phrases - Exact Match" with the appropriate phrases. You can then select whether these phrases can be from the customer, agent, or both.
6. Click "Add Action" and choose "Generate an EventBridge Event". Provide a name for this action; this name will be visible in the EventBridge event received in Lambda later.
7. Review the rule and publish it.

For further information on setting up Contact Lens Rules in Connect please refer to [this AWS document](https://docs.aws.amazon.com/connect/latest/adminguide/build-rules-for-contact-lens.html).

### Create the Lambda Function

Create a lambda function to manage the events. In this instance, we name the function "\_ConnectHandleRulesActions" and utilize Python 3.12.

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731463974682)

Incorporate the provided sample code into the Lambda function. You can modify the code as needed to suit your requirements, such as adding new conditions or adjusting the text for custom attributes.

```
import json
import boto3
import os

def lambda_handler(event, context):

  # Check for Contact ID
  if 'contactArn' in event['detail']:
    contact_arn = event['detail']['contactArn']
    contact_id = contact_arn.split('/')[-1]
  else:
    print("INFO: Contact ID was not found. Skip.")
    return
  
  # Get Connect instance Id from Lambda env. variables
  ConnectInstanceId = os.environ['ConnectInstanceId']
  
  # Create a client for the Amazon Connect
  connect_client = boto3.client('connect')
  
  # Get values for rule and action
  ruleName = event['detail']['ruleName']
  actionName = event['detail']['actionName']
  
  # Handle rules and actions
  try:
    if ruleName == 'DelayInDelivery':
    	if actionName == 'ConnectDelayInDeliveryAction':

    # Update the contact with the new contact attribute
    response = connect_client.update_contact_attributes(
    InitialContactId=contact_id,
    InstanceId=ConnectInstanceId,
    Attributes={
    'label_DelayInDelivery': '{"text":"Delay in
    Delivery","theme":"warning","icon":"delivery"}',
    'panel_DelayInDelivery': '{"text":"## Instructions for Delay in
    Delivery: \\n\\n1. **Listen & Apologize:** Acknowledge customer frustration
    and apologize for the inconvenience.\\n1. **Gather Details:** Obtain order
    number or relevant info to check order status.\\n1. **Explain Delay:**
    Clearly communicate reason for delay (e.g., shipping issues,
    inventory).\\n1. **Offer Solutions & Follow-up:** Provide options
    (expediting, refund) and promise to update on progress.","theme":"info"}'
      }
    )
    # ...
    # Extend the rules and actions to cover different scenarios.
    # ...
  except Exception as e:
    print(f"An error occurred: {str(e)}")
    return
```

Ensure that the Lambda function has the necessary "connect:UpdateContactAttributes" permission. Refer to the sample policy below for guidance.

```
Unset
{
  "Version": "2012-10-17",
  "Statement": [
  {
    "Sid": "VisualEditor0",
    "Effect": "Allow",
    "Action": "connect:UpdateContactAttributes", 
    "Resource": "arn:aws:connect:{AWS region}:{AWS account
   number}:instance/{Connect instance ID}/contact/*"
       }
		] 
}
```

Replace all the placeholders with your relevant Amazon Connect and Account Information

### Create EventBridge Rule

1. Navigate to the Amazon EventBridge service.
2. On the left side, click on "Rules", then select "Create rule".
3. Choose "Rule with an event pattern" and proceed.
4. Opt for "Use pattern form" and configure the AWS service to "Amazon Connect" with the Event type set to "Realtime Rules Matched".
5. Specify the action by providing the name of the action set in the Connect Contact Lens Rule, or proceed by selecting "Any action type".
6. For the Target, select the Lambda function you previously created.
7. Review the details and create the rule.

### **Agent Experience**‍

Using our "Delay in Delivery" example, the outcome of deploying the solution will resemble the figure below.

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731506714650)
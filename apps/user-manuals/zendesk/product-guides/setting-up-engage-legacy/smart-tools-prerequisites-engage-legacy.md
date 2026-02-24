# Smart Tools Prerequisites (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731463660954-Smart-Tools-Prerequisites-Engage-Legacy

---

## Overview

Smart Tools are based on Generative AI technology. In order to utilise Generative AI, Local Measure has built integrations with a range of AI Services, enabling access to their Generative AI models. Smart tools include the following elements:

- **Smart Composer**  is a set of tools that Agents can use to supercharge the messages they send to your customers. Smart Composer uses Generative AI to perform spelling and grammar checks, shorten or lengthen a message at the request of an Agent.
- **Smart Notes**  is a new feature in Engage for Amazon Connect that utilises Generative AI to automatically summarise a contact, and then suggest a note for the Agent to add to the Contact in After Call Work.
- **Smart Tasks**  is a new feature in Engage for Amazon Connect that utilises Generative AI to automatically populate Task Template fields using the conversation transcript.

‍

## Prerequisites

The high-level steps to enable Smart Tools using Amazon Bedrock are as follows:

1. Client to review relevant EULA
2. Client to request access to Anthropic Claude model within Bedrock
3. Local Measure Engage CloudFormation stack to be updated
4. Engage configuration to enable the tools within Engage
5. Optional - review and update Task Templates to ensure they are optimised for Smart Task capabilities

## Client Actions

It is up to the client to review and accept the EULA for Claude and to request access to these models.

The following steps can be followed to perform these steps.

### 1. Navigate to the Bedrock service

Log into the AWS Console and enter 'Bedrock' into the search bar. Select 'Amazon Bedrock' from the dropdown showing the results.

**NB:** Ensure that you are in the correct AWS region. Note that Bedrock is not available in all regions. Engage can however leverage Bedrock remotely from any of the supported AWS regions.

### 2. Select 'Model access'

Select 'Model access' on the left hand navigation bar.

![](https://support.zendesk.com/hc/article_attachments/9731476256794)

### 3. Select 'Manage model access'

![](https://support.zendesk.com/hc/article_attachments/9731439398042)

### 4. Review Bedrock EULA

On the resulting screen - scroll to the bottom and review the EULA.

![](https://support.zendesk.com/hc/article_attachments/9731467401754)

### 5. Review Anthropic EULA

If the Bedrock EULA conditions are acceptable, scroll upwards until the 'Anthropic' section is visible. Click on the EULA next to the 'Claude Instant' model to review the Anthropic EULA.

![](https://support.zendesk.com/hc/article_attachments/9731500295962)

### 6. Submit use case

If the EULA conditions are acceptable, click on 'Submit use case details'.

![](https://support.zendesk.com/hc/article_attachments/9731476358810)

Fill in the form in the popup window. The below is an example of a use case description which can be added:

*I am requesting access to Amazon Bedrock. We plan to integrate it as an assistant in our Amazon Connect contact center to enhance agent efficiency and reduce customer interaction times. This model's advanced features in natural language processing align perfectly with our goal to streamline operations. We are eager to explore its capabilities and contribute valuable insights to further improve its functionalities.*

Click on 'Submit' at the bottom of the form.

### 7. Request access

Select the checkboxes next to the two Claude models. Then scroll down to the bottom of the page and click 'Request Model Access'.

**NB:** There will now also be EULA agreements for the Claude models which the client must review to ensure that Bedrock usage is acceptable.

![](https://support.zendesk.com/hc/article_attachments/9731450886298)

Access is typically granted within an hour. The 'Model access' section can be monitored to validate when access is granted.

## CloudFormation Stack Update

Local Measure will assist with updating the CloudFormation stack. Local Measure will need to know in which AWS region the Claude Model was enabled.

## Local Measure Engage Configuration

Local Measure will assist with the initial configuration of Engage in order to enable Smart Tools.
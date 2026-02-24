# How to Configure a Smart Tools Integration (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731462361882-How-to-Configure-a-Smart-Tools-Integration-Engage-Legacy

---

Engage offers a range of Smart Tools. In order to use Smart Tools, you must first set up your integration with an AI Service.

Engage currently supports the following AI Services:

- Amazon Bedrock
- Azure Open AI

# Prerequisite

1. Before configuring your Smart Tools, you need to have an AI Service configured with access to the required model.
   1. ‍[Click here for more information about managing your models in Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html)
   2. [Click here for more information about managing your models in Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/deploy-models-openai)
2. You will also need to be running CloudFormation Template v5.79.3 (20240514) or later, with the required Bedrock region enabled.

## To configure Amazon Bedrock

1. Navigate to Engage **Settings** page
2. Scroll down to the **Integrations** section
3. Expand the **Smart Tools** section
4. Select **Amazon Bedrock**
5. Turn on the **Enable Agent Visibility** toggle - note that agents will not have access to AI Assist at this stage - you will still need to enable AI Assist within Workflows for it to be made available to Agents
6. Select the **Model** you wish to use

Note that the cost of using your AI Service will vary based on the model you select. Local Measure recommends utilising Claude 3 Haiku.

‍

## To configure Azure Open AI

1. Navigate to Engage **Settings** page
2. Scroll down to the **Integrations** section
3. Expand the **Smart Tools** section
4. Select **Microsoft Azure**
5. Turn on the **Enable Agent Visibility** toggle - note that agents will not have access to AI Assist at this stage - you will still need to enable AI Assist within Workflows for it to be made available to Agents
6. Enter your AI Service details **Open AI Endpoint** (found in Azure Open AI)
7. Enter your **AI Key** (found in Azure Open AI)
8. Select the **Model** you wish to use

Note that the cost of using your AI Service will vary based on the model you select. Local Measure recommends utilising davinci.

![](https://support.zendesk.com/hc/article_attachments/9731498874906)

‍

‍
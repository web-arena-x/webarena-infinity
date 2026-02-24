# How to Set Up Bedrock Guardrails in Engage (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731466552090-How-to-Set-Up-Bedrock-Guardrails-in-Engage-Engage-Legacy

---

Amazon Bedrock Guardrails can be used in tandem with Engage Smart Tools to ensure that your Agents can only process specific types of data via Smart Tools.

‍

As an example, you can specify specific topics or words that you don't want Smart Tools to process so that they never suggest content to your Agents that relate to those topics or words.

‍

‍**Pre-Requisite**

To utilise Amazon Guardrails in Engage, you must be using Amazon Bedrock to power your Smart Tools.

‍

Before linking your Amazon Bedrock Guardrail to Engage, you will need to configure it within your AWS account.

This can be done via the console or via APIs.

[Click here](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-create.html) to see how to setup your Amazon Bedrock Guardrail.

‍

**Link your Guardrail to Engage**

Once you have setup your Guardrail, you can link it to Engage so that when Smart Tools process content, the Guardrail is applied.

1. In Engage, navigate to the **General Settings** page
2. Scroll down to the **Integrations** section
3. Click the **Edit Smart Tools settings** button
4. In the pop-up, select the relevant **Guardrail** and **Version** from the dropdowns
5. Click the **Save** button

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731475076378)

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731475094938)
# Configuring Bedrock Guardrails in Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9696124943770-Configuring-Bedrock-Guardrails-in-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Use Amazon Bedrock Guardrails with Smart Tools to control the data types processed in your Contact Center. Set up your Guardrail in your AWS account, then link it to your Contact Center to ensure Smart Tools avoid certain topics or words. This setup helps maintain content relevance and compliance by filtering out unwanted suggestions during customer interactions.

Amazon Bedrock Guardrails can be used in tandem with Zendesk for Contact Center
Smart Tools to ensure that your Agents can only process specific types of data via Smart
Tools.

‍

As an example, you can specify specific topics or words that you don't want
Smart Tools to process so that they never suggest content to your Agents that relate to
those topics or words.

This article contains the following topics:

- [Getting started](#topic_g35_1lr_sgc)
- [Linking your guardrail to Contact Center](#topic_wbd_blr_sgc)

## Getting started

To utilise Amazon Guardrails in Contact Center, you must be using Amazon
Bedrock to power your Smart Tools.

Before linking your Amazon Bedrock Guardrail to Contact Center, you will
need to configure it within your AWS account.

This can be done via the console or via APIs.

[Click here](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-create.html) to see how to setup your Amazon
Bedrock Guardrail.

## Linking your guardrail to Contact Center

Once you have setup your Guardrail, you can link it to Contact Center so
that when Smart Tools process content, the Guardrail is applied.

1. In Contact Center, navigate to the **General Settings** page
2. Scroll down to the **Integrations** section
3. Click **Edit Smart Tools settings**.
4. In the pop-up, select the relevant **Guardrail** and **Version**
   from the dropdowns
5. Click **Save**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_bg_1.png)

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_bg_2.png)
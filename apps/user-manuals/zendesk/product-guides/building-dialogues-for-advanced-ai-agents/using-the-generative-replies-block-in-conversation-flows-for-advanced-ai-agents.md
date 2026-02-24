# Using the generative replies block in conversation flows for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357749315098-Using-the-generative-replies-block-in-conversation-flows-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

In [AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/8725042447002), *generative replies* refers to the ability of [zero-training AI agents](https://support.zendesk.com/hc/en-us/articles/8357749447194) and [AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/8966284087066) to create and send AI-generated answers in response to customer questions.

Generative replies can be activated through either the generative replies [system reply](https://support.zendesk.com/hc/en-us/articles/8357749481882) or the generative replies block in the [dialogue builder](https://support.zendesk.com/hc/en-us/articles/8357749494810). This article covers how to use the generative replies block in the dialogue builder.

The article contains the following sections:

- [Adding and configuring a generative replies block in a dialogue](#topic_vph_yfm_yfc)
- [Showing which help center articles were used to generate a reply](#topic_lxs_zjm_yfc)
- [Creating a custom question to provide more context for a generative reply](#topic_zr3_1ht_fhc)

Related article:

- [Importing knowledge sources to power generative replies in advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749301658)

## Adding and configuring a generative replies block in a dialogue

Within a conversation flow, the generative replies block responds to a customer's question with information generated from an [imported knowledge source](https://support.zendesk.com/hc/en-us/articles/8357749301658).

**To add a generative replies block in a dialogue**

1. In AI agents - Advanced, [create a new dialogue](https://support.zendesk.com/hc/en-us/articles/8357749494810#topic_ygq_4ym_g2c) or [open one for editing](https://support.zendesk.com/hc/en-us/articles/9066753203738#topic_nvb_tzl_52c).
2. Click the plus icon (+) where you want to insert a generative reply and select **Generative replies**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_generative_replies_block_menu.png)

After you add a generative reply block, you still need to perform the following additional steps:

- [Configuring the child blocks](#topic_rcr_wdt_fhc)
- [Configuring the response fallback behavior](#topic_yz2_mjm_yfc)

### Configuring the child blocks

When you add a generative reply block in a dialogue, the following scenarios are automatically added as children of the block and must be configured:

- [Response generated](#topic_vrc_vgm_yfc)
- [Escalation needed](#topic_czf_fjm_yfc)

#### Response generated

In the response generated scenario, an AI agent successfully generates a response to a customer message by considering both the information from the knowledge source and the specific query.

Information is retained in two session parameters:

- **ugptResponse**: Retains the response from the AI agent, which can be used immediately in the conversation or saved for later reference.
- **dataSources**: Retains up to five of the knowledge base articles used as context for the generated response.

With each new generative reply, the content of these session parameters is overwritten. This ensures that the response captured is always the most recent.

You can choose from two options for integrating a generative reply into the conversation:

- **Share with the customer**: The AI agent immediately sends the generated response to the conversation.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_generative_replies_response_generated_share.png)
- **Save response only**: The AI agent does not send the response directly to the conversation, and only retains it in the session parameter *ugptResponse*. The dialogue continues with other blocks and logic.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_generative_replies_response_generated_save.png)

 The response can be used for testing or evaluation purposes. It can also be shared with the customer later using an AI agent message block along with the session parameter using the reference *{{ugptResponse}}*.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_generative_replies_response_generated_ugptresponse.png)

 Tip: For email AI agents, consider including additional response text to frame the AI agent’s reply. For example, including the text “Our AI agent has suggested the following answer:” as a lead in to the text of the generative reply.

#### Escalation needed

The escalation needed scenario is activated when the AI agent identifies that the customer wants to speak with a human. In this scenario, information is not saved to the *ugptResponse* and *dataSources* session parameters.

To handle this scenario, continue the dialogue by incorporating further blocks, such as another reply or an escalation block.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_generative_replies_escalation_needed.png)

Note: For email AI agents, generative replies blocks don’t offer an [escalation option](https://support.zendesk.com/hc/en-us/articles/8357749315098#h_01HP4MJRD6P1WN4BHDK6Q34ZVF). Instead, use a fallback block to address scenarios in which the AI agent can't answer the customer’s question with a generative reply.

### Configuring the response fallback behavior

By default, both of the scenarios of the generative reply block (Response generated and Escalation needed) are directly linked to their respective system replies. You have the option of building a dialogue branch for either or both of them by setting the Response fallback behavior toggle to off in the Details pane.

- **Not understood**: The AI agent is unable to find relevant articles or data to generate a response. By default, this scenario links to the default reply.
- **An error occurred**: The generative replies service is either unreachable, returns an error, or encounters another issue within the system. By default, this scenario links to the Technical error system reply

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_generative_reply_block_details.png)

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_generative_replies_not_understood.png)

## Showing which help center articles were used to generate a reply

The *dataSources* session parameter, which is returned with the generative reply, can be used to provide the customer with access to the articles that a messaging AI agent’s response was based on. Using carousels to provide this content can improve the customer experience by adding a visual element.

Note: Generative procedures used by [AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/8966284087066) don’t currently support rich-text formatting such as buttons or carousels.

**To create a carousel of data sources**

1. In AI agents - Advanced, [create a new dialogue](https://support.zendesk.com/hc/en-us/articles/8357749494810#topic_ygq_4ym_g2c) or [open one for editing](https://support.zendesk.com/hc/en-us/articles/9066753203738#topic_nvb_tzl_52c).
2. Click the plus (+) icon to add a conditional block in the appropriate location.
3. In the conditional block, **set the variable** `ugptClassifiedTask`.
4. As a condition, set the operator to `is` and include the value `question answering`.
5. Click the plus (+) icon to add an AI agent message to the fallback of the conditional block.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_generative_replies_carousel_1.png)
6. Click the plus (+) icon to add a carousel block to the `is` `question answering` condition block.

   The carousel block appears along with the first card block and a Details pane.
7. In the Details pane, click **Convert to dynamic carousel** and enter `dataSources` as the array type parameter.
8. In the template card block, enter text or parameters such as`%imageurl`, `%title` and `%description` in the respective fields.
9. In the template card button block, select **Button with external link** and enter text or a parameter such as `%buttontext`.
10. In the Details pane, deactivate the fallback block by setting the Fallback toggle to off.

    Omitting the fallback allows the conversation to restart if the customer asks another question.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_generative_replies_carousel_2.png)

## Creating a custom question to provide more context for a generative reply

By default, the generative replies block uses the customer's latest message as a prompt when searching your knowledge sources for an answer. However, if the customer's latest message doesn't actually include all the relevant information, the AI agent may be unable to generate an accurate response.

To address this, you can define a custom question that overwrites the customer's last message as the prompt the AI agent uses to search your knowledge sources. The custom question allows you to incorporate context from previous messages, including intents, specific user inputs, session parameters, and more. This enables the AI agent to provide more precise and contextually relevant generative replies, even when the original context is not readily available in the latest customer message.

For example, consider the following exchange:

- The customer inquires about their recommended shoe size.
- The AI agent asks for their foot length in centimeters and their sizing information (UK, US, or EU).
- The customer provides their answers, which are stored as session parameters
 {{foot\_length\_cm}} and {{location}}.

At this point in the dialogue, you can insert a generative replies block with the following custom question: "Which shoe size would you recommend based on my {{foot\_length\_cm}} and my
{{location}}?"

With this custom question, the AI agent has enough context to search your knowledge sources and deliver an accurate answer to the customer's sizing inquiry based on the stored session parameters. Without the custom question, the user's latest message would be their sizing location, which wouldn't provide the AI agent with enough context to generate a useful answer.

**To create a custom question**

1. In AI agents - Advanced, [create a new dialogue](https://support.zendesk.com/hc/en-us/articles/8357749494810#topic_ygq_4ym_g2c) or [open one for editing](https://support.zendesk.com/hc/en-us/articles/9066753203738#topic_nvb_tzl_52c).
2. Select an existing generative replies block or [add a new one](#topic_vph_yfm_yfc).
3. In **Custom question (optional)**, enter the text of your custom question.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_generative_reply_custom_question.png)
4. **Save** or **Publish** your changes.
# Using communication guidelines to improve AI assistance for agent comments

Source: https://support.zendesk.com/hc/en-us/articles/8761641980698-Using-communication-guidelines-to-improve-AI-assistance-for-agent-comments

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Copilot |

Communication guidelines allow [auto assist](../providing-ai-assistance-with-auto-assist/turning-on-and-configuring-auto-assist.md) and the [rewrite in your tone tool](https://support.zendesk.com/hc/en-us/articles/5608712782362#topic_fn1_bkp_22c) to adapt suggestions and responses based on the tone, topic, urgency, language, writing style, and context of an ongoing ticket conversation.

To further refine the suggestions and responses that Copilot AI tools make to agents, you can create your own communication guidelines that are specific to your business. Creating your own guidelines helps cover a wider range of writing rules, such as general communication principles, formatting, length, formality, structure, greetings, closings, wording, and more.

This article contains the following topics:

- [About communication guidelines](#topic_eck_hmp_22c)
- [Turning communication guidelines on or off](#topic_krn_2xp_22c)
- [Defining communication guidelines](#topic_arb_r43_zfc)

Related articles:

- [Best practices for creating communication guidelines to improve AI assistance](https://support.zendesk.com/hc/en-us/articles/9182110974746)
- [Enhancing ticket comments using generative AI](https://support.zendesk.com/hc/en-us/articles/5608712782362)

## About communication guidelines

The communication guidelines feature is available for any languages supported by OpenAI and works on any channel within Agent Workspace.

When the communication guidelines feature is turned on, it rephrases the content of agents' public comments or auto assist suggestions so that responses are adapted to the overall writing style and tone of a conversation. The system rewrites text based on past interactions between the end user and agent by analyzing certain conversation variables within a specific ticket. Some of the conversation variables that the system analyzes include:

- Overall tone and language
- Greetings, closures and signatures
- Writing style and language complexity (for example, length and format)
- Use of specific words/eponyms and special characters
- Ticket conversation sentiment, topic, criticality and urgency

You can also define your own guidelines to cover a wider range of brand-specific writing rules. For example, you may want to include words to use and avoid and formatting instructions. See [Best practices for defining communication guidelines](https://support.zendesk.com/hc/en-us/articles/9182110974746) for more information.

If you’ve defined your own guidelines, the system follows your guidelines in addition to analyzing the ticket context in an ongoing conversation. If there’s ever a conflict between the tone or writing style inferred from the ticket conversation and your guidelines, your guidelines take precedence.

When the communication guidelines feature is turned on, the [Rewrite in your tone option](https://support.zendesk.com/hc/en-us/articles/5608712782362#topic_fn1_bkp_22c) is added to the enhanced writing tools menu in the Agent Workspace and [auto assist](https://support.zendesk.com/hc/en-us/articles/8013454025114#topic_dx3_rww_xcc) adapts its suggestions to match an ongoing conversation.

Communication guidelines don’t change the core content of an AI-generated response. For example, they won’t override the actual steps in an auto assist procedure. Guidelines are applied to auto assist suggestions only after the system has interpreted the user’s message, searched for relevant content, and generated an initial draft.

Note: OpenAI will not use your data to train its models or improve its services. For more information about how your data is protected, see [Zendesk AI Data Use Information](https://support.zendesk.com/hc/en-us/articles/5729714731290).

## Turning communication guidelines on or off

Communication guidelines are turned on by default. Admins can turn this feature on or off in Admin Center.

If you turn this feature off, the [Rewrite in your tone option](https://support.zendesk.com/hc/en-us/articles/5608712782362#topic_fn1_bkp_22c) is removed from the enhanced writing tools menu in the Agent Workspace and auto assist doesn't adapt its suggestions to match the ongoing conversation.

**To turn communication guidelines on or off**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png) **AI** in the sidebar, then select **Agent copilot > Writing tools**.
2. Select or deselect **Communication guidelines**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_writingtool_comm_guidelines.png)
3. Click **Save**.

   Next, you can optionally [define brand-specific guidelines](#topic_arb_r43_zfc).

   Note: If you turn on communication guidelines but don’t define your own guidelines, the rewrite in your tone and auto assist features will be adapted based on context of the ticket conversation only.

## Defining communication guidelines

You can define your own brand-specific communication guidelines to help refine the tone, length, formality, structure, formatting, and word choice of AI-generated replies and suggestions.

For tips for creating effective guidelines, see [Best practices for defining communication guidelines](https://support.zendesk.com/hc/en-us/articles/9182110974746).

**To define communication guidelines**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png) **AI** in the sidebar, then select **Agent copilot > Writing tools**.
2. Make sure Communication guidelines [are turned on](#topic_krn_2xp_22c), then click **Manage guidelines**.
3. Click **Create guidelines**.
4. Enter a **Name**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/comm_guidelines_creating_new.png)
5. Optionally, select one or more brands where these guidelines will apply.
6. In the **Guidelines** field, enter your writing rules.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/comm_guidelines_create_example.png)

   See [Best practices for defining communication guidelines](https://support.zendesk.com/hc/en-us/articles/9182110974746).
7. Click **Save and close**.

   If some of the brands you selected are already connected to other communication guidelines, a message appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/comm_guidelines_brand_dialog.png)

   Click **Connect** to assign the brands to the new guidelines you created or **Go back** to edit the guidelines.
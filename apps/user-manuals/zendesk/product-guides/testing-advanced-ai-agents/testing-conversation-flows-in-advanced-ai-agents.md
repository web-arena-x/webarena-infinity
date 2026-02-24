# Testing conversation flows in advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357758879130-Testing-conversation-flows-in-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

After you create or update an advanced AI agent, you can test that it functions as intended before making it live. From within the add-on, you can access a test widget to safely test the overall customer experience or specific dialogue flows.

This article contains the following topics:

- [About the advanced AI agent test widget](#topic_k2d_l4l_khc)
- [Testing AI agent conversations end-to-end](#topic_esg_nnm_3fc)
- [Testing specific dialogues in AI agents](#topic_ct4_1qm_3fc)
- [Reviewing predicted use cases or intents](#topic_c23_3wm_3fc)

## About the advanced AI agent test widget

You can use the test widget to simulate the current customer experience of interacting with the AI agent. It starts from the welcome reply and includes all currently active [settings](https://support.zendesk.com/hc/en-us/articles/8357756721178), including [instructions](https://support.zendesk.com/hc/en-us/articles/8357749291290). Test conversations are recorded in [conversation logs](https://support.zendesk.com/hc/en-us/articles/8357749580186) for later review.

Note that you can't use the test widget to test the following elements, all of which are tied to your customer relationship management (CRM) platform:

- [CRM actions](https://support.zendesk.com/hc/en-us/articles/8357756651290#topic_kyv_jnl_rgc)
- Escalations triggered by the [Escalation dialogue block](https://support.zendesk.com/hc/en-us/articles/8357749494810#topic_krz_vym_g2c)
- [Rich-text messaging templates](https://support.zendesk.com/hc/en-us/articles/8357757976474)

The test widget isn't integrated with your CRM, as its main purpose is to test dialogue flows. If you want to test CRM-based events, use the [Web Widget](https://support.zendesk.com/hc/en-us/articles/4500748175258) embedded on your website or help center instead.

However, keep in mind that conversations in the test widget don't consume [automated resolutions](https://support.zendesk.com/hc/en-us/articles/5352026794010), but conversations in the Web Widget on your website or help center do.

## **Testing AI agent conversations end-to-end**

You can test the end-to-end behavior of an advanced AI agent using the test widget.

**To test an advanced AI agent**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Test AI agent**.

   The test widget appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_test_widget.png)
3. Use the widget to start a conversation with the AI agent.
4. To start the conversation over, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) in the test widget and select **Restart Chat**.
5. To go directly to the logged conversation, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) in the test widget and select **Open in Conversation Logs**.

## Testing specific dialogues in AI agents

While using the [dialogue builder](https://support.zendesk.com/hc/en-us/articles/8357749494810) to create conversation flows for your AI agent, you can test the dialogue you’re working on. You can also test a branch of the dialogue starting from a specific block.

**To test a dialogue**

1. [Create a new dialogue](https://support.zendesk.com/hc/en-us/articles/8357749494810), or [open a dialogue for editing](https://support.zendesk.com/hc/en-us/articles/9066753203738).
2. In the top-right, click **Test dialogue**.
3. In the Session parameters dialog, do one of the following:
   - To test the flow using a specific parameter, select a **Parameter** and enter a **Value**, then click **Test**.
   - To ignore all previously set parameters, click **Test without parameters**.

   Tip: To remember your selection for next time, deselect **Ask me every time**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_session_parameters_dialog.png)
4. In the test widget that appears, test the dialogue by sending messages to the AI agent.
5. To change session parameters during a test, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) in the test widget and select **Change parameters**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_test_widget_change_parameters.png)
6. To start a conversation over, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) in the test widget and select **Restart Chat**.
7. To go directly to the logged conversation, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) in the test widget and select **Open in Conversation Logs**.

**To test a branch of a dialogue**

1. In the dialogue builder, hover over the block you want to start from and click **Test branch** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_dialogue_builder_test_branch_icon.png)).

   You can start from any type of block except for Customer message and Link to blocks.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_dialogue_builder_test_branch.png)

## Reviewing predicted use cases or intents

In any test mode, you can review the top use cases or intents that the AI agent predicted for a customer message, including confidence level. If you’re using a zero-training AI agent or an AI agent with agentic AI, you see use case predictions.
If you’re using an expression-based AI agent, you see intent predictions.

**To review top predicted intents or use cases**

1. In the test widget, hover over a customer message.
2. Click the **View predicted intents** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon.png)) to the left of the message. The top predictions dialog appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_test_widget_view_predicted_intents.png)
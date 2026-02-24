# Collecting AI agent satisfaction (BSAT) ratings for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357749459482-Collecting-AI-agent-satisfaction-BSAT-ratings-for-advanced-AI-agents

---

AI agent satisfaction (BSAT) ratings are feedback from your users that measure their happiness with how your AI agent performed. When a BSAT rating request is sent, the user is asked to rate their support experience. Customers can rate the AI agent on a scale of 1 to 5 (using emojis or stars) or decline to answer.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

AI agent satisfaction (BSAT) ratings are feedback from your users that measure their happiness with how your AI agent performed. When a BSAT rating request is sent, the user is asked to rate their support experience. Customers can rate the AI agent on a scale of 1 to 5 (using emojis or stars) or decline to answer.

This article contains the following topics:

- [Turning on BSAT rating collection](#topic_zqh_xtg_52c)
- [Configuring the BSAT rating scale](#topic_upb_m5g_52c)
- [Configuring the BSAT system reply](#topic_thh_mch_52c)

## Turning on BSAT rating collection

BSAT ratings are collected using a [system reply](https://support.zendesk.com/hc/en-us/articles/8357749481882) called Collect BSAT reply. For this system reply to work, you must first configure how and when it should be sent during a conversation with a user. There are two methods to send BSAT collection:

- **Using a trigger** based on custom resolution states, reaching the end of a dialogue or generative procedure ([AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/8966284087066) only), or after a knowledge answer is shared (AI agents with agentic AI only).
- **Linking to the BSAT reply** from within a dialogue.

It's recommended to use one of these methods, not both. Links to a feedback reply always override triggers.

### Using a trigger to collect BSAT ratings

You can create a trigger to configure when the BSAT collection prompt should appear during a conversation between an AI agent and a user. This trigger can be based on a custom resolution state, reaching the end of a dialogue or generative procedure (AI agents with agentic AI only), or after a knowledge answer is shared (AI agents with agentic AI only).

Note: BSAT replies associated with a trigger aren't sent for conversations that were escalated to a human agent.

**To use a trigger to collect BSAT ratings**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Use cases**.
3. Select **Collect BSAT reply**.
4. Click the **Settings** tab.
5. Under **Triggers**, select **Activate triggers for BSAT replies**.
6. Under **Trigger reply when**, click the plus (+) icon and then select and configure one of the following trigger conditions:
   - **A custom resolution state is set**: This condition is satisfied when the specified [resolution state](https://support.zendesk.com/hc/en-us/articles/8357756466586) is reached and the specified amount of time has passed. You can add multiple resolution states and time periods per condition. A BSAT reply triggered by a resolution state can appear only once per conversation.
   - **The end of a procedure is reached**: (Available only for AI agents with agentic AI) This condition is satisfied when the AI agent has reached the end of a [generative procedure](https://support.zendesk.com/hc/en-us/articles/8979864563610)
     and the specified amount of time has passed. A BSAT reply triggered by reaching the end of a procedure can appear only once per conversation.
   - **The end of a dialogue is reached**: This condition is satisfied when the AI agent has reached the end of a [dialogue](https://support.zendesk.com/hc/en-us/articles/8357749494810) and the specified amount of time has passed. A BSAT reply triggered by reaching the end of a dialogue can appear only once per conversation.
   - **A knowledge answer is shared**: (Available only for AI agents with agentic AI) This condition is satisfied when the AI agent has shared an AI-generated answer.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_bsat_trigger_configuration.png)
7. (Optional) Repeat the previous step to configure additional conditions.
8. Click **Save**.

### Linking to the BSAT reply in a dialogue to collect BSAT ratings

You can choose to send a BSAT collection prompt at any point in a dialogue. You do this by linking to the Collect BSAT reply system reply from any block within a dialogue.

With this method, you must manually link to the BSAT reply in every dialogue where you want it to be sent. And if you want to turn off BSAT rating collection, you must manually remove the link in every dialogue. Disabling triggers for BSAT replies doesn't affect linked replies.

**To link to the BSAT reply in a dialogue**

1. [Open the dialogue builder](https://support.zendesk.com/hc/en-us/articles/9066753203738#topic_nvb_tzl_52c) for the dialogue where you want to add a BSAT reply link.
2. Choose an appropriate block, add a **Link to** block, and select **Collect BSAT reply**.
3. Save and publish your changes.

## Configuring the BSAT rating scale

You can select the type of rating scale that's displayed to users when a BSAT collection prompt is sent. By default, the Collect BSAT reply uses emojis, but you can also select a star️ rating system. In conversations, all options are rendered as buttons.

Note: For BSAT to work in WhatsApp, you must use the star rating scale, not the emoji rating scale.

**To configure the BSAT rating scale**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Use cases**.
3. Select **Collect BSAT reply**.
4. Click the **Settings** tab.
5. Under **Rating options**, select one of the following options:
   - **Emoji rating**

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_bsat_config_emoji_rating.png)
   - **Star rating**

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_bsat_config_star_rating.png)
6. Click **Save**.

## Configuring the BSAT system reply

If needed, you can configure the default Collect BSAT reply system reply in the dialogue builder.

**To configure the BSAT system reply**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Use cases**.
3. Select **Collect BSAT reply**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_bsat_reply_tab.png)
4. Select the language of the reply you want to edit.

   The dialogue builder opens, showing the dialogue for the Collect BSAT reply system reply.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_collect_bsat_response_example.png)
5. To change the question that's presented to the user when the BSAT collection prompt is sent, click the **BSAT question** block and select one of the following options:

   - **How would you rate your experience?**
   - **If you have a moment, please rate your experience**
   - **How would you rate the quality of your customer support experience?**
   - **Use translated question**

     You can use this last option to add a translated version for all the languages supported by your AI agent.
6. To configure what happens in the conversation flow, select the appropriate block and make updates as needed.

   For help, see [Using the dialogue builder to create conversation flows for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/9060706421274).
7. Save and publish your changes.
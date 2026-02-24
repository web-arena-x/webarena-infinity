# Automatically detecting customer intent, sentiment, and language

Source: https://support.zendesk.com/hc/en-us/articles/4550640560538-Automatically-detecting-customer-intent-sentiment-and-language

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Copilot |

Verified AI summary ◀▼

Use intelligent triage to automatically detect customer intent, sentiment, and language in support tickets. This feature enriches tickets with actionable details, helping you prioritize and route them effectively. Configure settings to tailor predictions to your needs, and leverage tags for streamlined workflows. Enhance your support operations by integrating AI detections into your ticket management strategy.

[Intelligent triage](https://support.zendesk.com/hc/en-us/articles/4964463770650) uses artificial intelligence (AI) to automatically analyze new support tickets by predicting customer intent, sentiment, and language, and enriches tickets with actionable details, such as product names.

You can use this information to identify and display helpful context about your incoming tickets. Additionally, you can improve your workflows by incorporating AI detections to more precisely deflect, route, and prioritize tickets.

This article describes how admins configure intelligent triage intent, sentiment, and language detection settings. To configure entity detection, see [Detecting unique information in tickets with entities](https://support.zendesk.com/hc/en-us/articles/6711181959194).

This article contains the following topics:

- [Understanding intelligent triage](#topic_l5w_fr4_pgc)
- [Configuring intent settings for intelligent triage](#topic_fh4_brd_hgc)
- [Configuring sentiment settings for intelligent triage](#topic_fcq_wr2_hgc)
- [Configuring language detection settings for intelligent triage](#topic_a3r_4h2_hgc)
- [Next steps](#topic_jyk_2bl_hgc)

Related articles:

- [Configuring intelligent triage for the agent experience](https://support.zendesk.com/hc/en-us/articles/6298065502874)

## Understanding intelligent triage

The Zendesk machine learning model automatically provides predictions about your tickets when intelligent triage is turned on. These predictions are added as [new custom fields to your tickets](#topic_ybp_w54_pgc), which provide insights into what a ticket is about, the language used, and the end user's emotional tone. Additionally, [related tags](#topic_xhg_y54_pgc) are generated to simplify the creation of automated workflows, views, and reporting, helping agents and admins efficiently handle and prioritize support requests.

### Understanding intelligent triage fields

When you enable intelligent triage, the system adds new custom fields to your tickets that are populated with prebuilt predictions by the Zendesk machine learning model:

- **Intent**: A prediction of what the ticket is about. The prediction is made based on the text of the first public comment in the ticket. If configured to do so, the intent is updated every time the end user replies.

 You can see the possible intent values [in the Intents page](https://support.zendesk.com/hc/en-us/articles/9488234915610). The Zendesk Intent Model includes intents for all of the supported industries. Your account has access to relevant intents and use cases based on your ticket conversation data.
- **Language**: A prediction of which language the ticket is written in. To see the possible values, open the Language page in Admin Center. For the Language field, intelligent triage can detect approximately [150 different languages](../multiple-language-support/zendesk-language-support-by-product.md#h_01K2J618F2V783VM0C8EXMZWCT).
- **Sentiment**: A prediction of how positive or negative the customer feels about their request. Possible values are Very Positive, Positive, Neutral, Negative, and Very Negative. The prediction is made based on the text of the first message in the ticket. If configured to do so, the sentiment is updated every time the end user replies.

 Intelligent triage is specifically calibrated for customer service. This means that a ticket isn’t assigned a negative sentiment just because a customer has an issue with their order, can’t find the information they need, or some other similar “negative” situation. Instead, the model is tuned to analyze sentiment with the assumption that the customer is contacting customer service because they have an issue that needs to be addressed.

In addition, each of these fields has an associated confidence field to indicate how likely the prediction is accurate. These fields are populated by the Zendesk machine learning model based on the content of the first message of a ticket when it’s submitted. Agents can [update the field values](https://support.zendesk.com/hc/en-us/articles/6298065502874#topic_vx1_4n3_fzb) if necessary.

### Understanding intelligent triage tags

When the Intent, Sentiment, and Language fields are populated, tags are also automatically added to the ticket to help you build views, triggers, automations, and reporting. These tags reflect the values in the Intent, Language, and Sentiment fields, and are structured as follows:

- intent\_\_*value of Intent field*
- language\_\_*value of Language field*
- sentiment\_\_*value of Sentiment field*

When creating business rules, you can use the field value or the tag, depending on which is easier. For example, when creating a trigger with multiple intents, it’s easier to use tags because you can add them faster than adding separate conditions for multiple field values.

## Configuring intent settings for intelligent triage

Intents are predictions about what each ticket is about. You can configure intent settings in Admin Center.

By default, intent detection is turned on. To turn off intent detection, see [Turning off intent detection](https://support.zendesk.com/hc/en-us/articles/9678056232858#topic_fh4_brd_hgc).

**To configure intent settings**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Intelligent triage > Intent**.
2. Click **Manage Settings**.
3. To update a ticket's intent based on the latest end user message in a conversation, click the checkbox under **Dynamic detection**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_intent_dynamic_detect_setting.png)

   Dynamic detection applies to only new tickets created after you turn this setting on.
4. Under **Channels**, configure the channels you want to detect intent:
   - For **Email and async** channels, click the drop-down, then select or deselect the channels.

     The Web form, Email, and Web service (API)
     channels are selected by default. If you create tickets via [channel integrations](https://support.zendesk.com/hc/en-us/articles/4408824097050#topic_amm_zbh_bhb), select Social messaging.

     The Closed tickets channel is for follow-up tickets. See [Follow-up ticket considerations](https://support.zendesk.com/hc/en-us/articles/8421655952026#topic_q4r_vk5_ncc).
   - For **Messaging** channels, click the drop-down, then select or deselect the channels.

     The Web Widget, WhatsApp, and Facebook Messenger channels are selected by default.

     Selecting any one of the Web Widget, iOS SDK, Android SDK, or Native Messaging channels automatically selects all four channels together.
   - Select the **Voice** checkbox to detect intent on post-call transcripts.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_intelligent_triage_channel_settings.png)

     [Call transcription must be turned on](https://support.zendesk.com/hc/en-us/articles/6170157307162) and transcripts must be shown on tickets for intent to be detected on the voice channel.
5. To exclude tickets created by agents from intent detection, click the checkbox under **Exclusion conditions**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Copilot_intelligent_triage_settings_exclusions.png)
6. Click **Save**.

## Configuring sentiment settings for intelligent triage

Sentiments are predictions about how the user feels about their request. You can configure sentiment settings in Admin Center.

By default, sentiment prediction is turned on. To turn off sentiment prediction, see [Turning off sentiment prediction](https://support.zendesk.com/hc/en-us/articles/9678056232858#topic_fcq_wr2_hgc).

**To configure sentiment settings**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Intelligent triage > Sentiment**.
2. Click **Manage Settings**.
3. Select the checkbox under **Dynamic detection** to update a ticket's sentiment based on the latest end user message in a conversation.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_sentiment_dynamic_detection_setting.png)

   Dynamic detection applies to only new tickets created after you turn this setting on.
4. Under **Channels**, configure the channels you want to predict sentiment:
   - For **Email and async** channels, click the drop-down, then select or deselect the channels.

     The Web form, Email, and Web service (API)
     channels are selected by default. If you create tickets via [channel integrations](https://support.zendesk.com/hc/en-us/articles/4408824097050#topic_amm_zbh_bhb), select Social messaging.

     The Closed tickets channel is for follow-up tickets. See [Follow-up ticket considerations](https://support.zendesk.com/hc/en-us/articles/8421655952026#topic_q4r_vk5_ncc).
   - For **Messaging** channels, click the drop-down, then select or deselect the channels.

     The Web Widget, WhatsApp, and Facebook Messenger channels are selected by default.

     Selecting any one of the Web Widget, iOS SDK, Android SDK, or Native Messaging channels automatically selects all four channels together.
   - Select the **Voice** checkbox to detect intent on post-call transcripts.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_intelligent_triage_channel_settings.png)

     [Call transcription must be turned on](https://support.zendesk.com/hc/en-us/articles/6170157307162) and transcripts must be shown on tickets for sentiment to be detected on the voice channel.
5. To exclude tickets created by agents from sentiment prediction, click the checkbox under **Exclusion conditions**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Copilot_intelligent_triage_settings_exclusions.png)
6. Click **Save**.

## Configuring language detection settings for intelligent triage

Language is a prediction of what language the ticket is written in. You can configure language detection settings in Admin Center.

By default, language detection is turned on. To turn off language detection, see [Turning off language detection](https://support.zendesk.com/hc/en-us/articles/9678056232858#topic_a3r_4h2_hgc).

**To configure intelligent triage language settings**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Intelligent triage > Language**.
2. Click **Manage Settings**.
3. Under **Channels**, configure the channels you want to detect language:
   - For **Email and async** channels, click the drop-down, then select or deselect the channels.

     The Web form, Email, and Web service (API)
     channels are selected by default. If you create tickets via [channel integrations](https://support.zendesk.com/hc/en-us/articles/4408824097050#topic_amm_zbh_bhb), select Social messaging.

     The Closed tickets channel is for follow-up tickets. See [Follow-up ticket considerations](https://support.zendesk.com/hc/en-us/articles/8421655952026#topic_q4r_vk5_ncc).
   - For **Messaging** channels, click the drop-down, then select or deselect the channels.

     The Web Widget, WhatsApp, and Facebook Messenger channels are selected by default.

     Selecting any one of the Web Widget, iOS SDK, Android SDK, or Native Messaging channels automatically selects all four channels together.
   - Select the **Voice** checkbox to detect intent on post-call transcripts.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_intelligent_triage_channel_settings.png)

     [Call transcription must be turned on](https://support.zendesk.com/hc/en-us/articles/6170157307162) and transcripts must be shown on tickets for language to be detected on the voice channel.
4. To exclude tickets created by agents from language detection, select the checkbox under **Exclusion conditions**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Copilot_intelligent_triage_settings_exclusions.png)
5. Click **Save**.

## Next steps

After you've configured intent, sentiment, and language detection features, it's recommended that you finish setting up intelligent triage by:

- [Creating entities](https://support.zendesk.com/hc/en-us/articles/6711181959194) to detect unique information in tickets.
- [Creating custom intents](https://support.zendesk.com/hc/en-us/articles/8718789695002) to personalize intelligent triage for your specific business needs.
- [Configuring how intelligent triage predictions are shown to agents](https://support.zendesk.com/hc/en-us/articles/6298065502874) to increase their productivity.

When you're done setting up intelligent triage, you can take these actions to maximize its impact on your support workflows by:

- [Creating views for your automatically triaged tickets](https://support.zendesk.com/hc/en-us/articles/4662504732954): Surface tickets based on AI predictions, such as intent and sentiment, so that your teams can quickly focus on high-priority or specialized issues. This streamlines ticket management and boosts response times
- [Choosing a routing method for automatically triaged tickets](https://support.zendesk.com/hc/en-us/articles/4973607684506): Automatically assign tickets to the right agents or teams using intelligent triage data. For example, route urgent or negative sentiment tickets to priority support, or direct product-specific issues to specialized experts. This can ensure faster and more accurate resolutions.
- [Leverage prebuilt analytics dashboards to analyze intelligent triage performance](https://support.zendesk.com/hc/en-us/articles/7934147095066): Gain actionable insights on how AI-powered predictions are enhancing ticket handling. Monitor trends in customer sentiment, popular intents, and language distribution to continuously optimize your workflows and improve customer satisfaction.
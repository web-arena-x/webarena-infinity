# Improving intent quality with personalized recommendations

Source: https://support.zendesk.com/hc/en-us/articles/9484697389210-Improving-intent-quality-with-personalized-recommendations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Copilot |

Verified AI summary ◀▼

Improve your intent quality with intelligent triage, which uses AI to classify tickets by intent, language, and sentiment. Get personalized recommendations for new intents and resolve conflicts like duplicates or overlaps to enhance ticket classification. You control whether to accept or decline suggestions, ensuring your intent setup aligns with your business needs.

[Intelligent triage](https://support.zendesk.com/hc/en-us/articles/4964463770650) leverages AI to automatically classify incoming tickets by intent, language, and sentiment. The Zendesk Intent Model includes pre-trained intents across several industries, providing relevant intents and use cases tailored to your account's ticket data.

Intelligent triage makes proactive recommendations to help you monitor the quality of your intents. When gaps are identified in your intent coverage, you'll see recommendations for new intents. Additionally, whenever you create, modify, or deactivate an intent, intelligent triage analyzes your account and identifies any duplicate or overlapping intents.

This article contains the following topics:

- [About intent recommendations](#topic_zyc_c1y_c2c)
- [Reviewing intent recommendations](#topic_hq4_zfj_zfc)
- [Resolving intent conflicts](#topic_kwc_gtn_yhc)

Related articles:

- [Automatically detecting customer intent, language, and sentiment](https://support.zendesk.com/hc/en-us/articles/4550640560538)
- [Accessing and viewing intelligent triage intents](https://support.zendesk.com/hc/en-us/articles/9488234915610)

## About intent recommendations

An intent is a prediction of what the ticket is about. When you activate intelligent triage, your account includes a prebuilt list of intents specific to your industry.

For example, if a customer submits a ticket saying that the item they ordered arrived damaged, then intelligent triage may automatically tag the ticket with an intent of *damaged on arrival*.

To improve and monitor the overall quality of your intents, intelligent triage makes two types of proactive recommendations:

- **Create new intent**: Intelligent triage identifies gaps in your intent coverage and makes data-driven suggestions every week for new, relevant intents that are tailored to your account’s ticket data. You can review and accept intent recommendations to further fine tune your setup.

 When you accept an intent recommendation, it's immediately added to your list of intents and starts detecting the intent of incoming customer requests.

 Intents aren't intended to identify details of the ticket, such as specific product or service names, branch locations, subscription types, or similar details. Instead, see the [entity detection](https://support.zendesk.com/hc/en-us/articles/6711181959194) feature to identify business-critical information in your incoming requests automatically.

 If you want to create your own custom intents, see [Personalizing intelligent triage by creating custom intents](https://support.zendesk.com/hc/en-us/articles/8718789695002).
- **Resolve intent conflict**: Intelligent triage analyzes your account whenever you create, modify, or deactivate an intent. If an overlapping or duplicate intent is identified, a recommendation is made to resolve the conflict.

 An intent is considered to be *overlapping* when it contains expressions that are similar to other intents. Recommendations for an overlapping intent contain suggested content changes that can help differentiate the intents during ticket classification.

 An intent is considered a *duplicate* when it fully overlaps with other intents, causing the system to treat them as identical. When you have a recommendation to review a duplicate intent, you can resolve the conflict by reviewing both intents and deactivating the unnecessary duplicate. Removing duplicate intents helps prevent confusion during ticket classification.

 For some duplicate intents, you may want to consider [creating an entity](https://support.zendesk.com/hc/en-us/articles/6711181959194#topic_qv4_xkt_zbc) after deactivating an intent. For example, say you have the following two intents that are considered duplicates:

 - Missing deposit
 - Missing deposit in Acme Bank

 In this case, you could deactivate the "Missing deposit in Acme Bank" intent and then create an entity to extract the bank name from the ticket.

You're always in control and must accept or decline a recommendation before any action is taken. If you decline a recommendation and want to come back to it later, you can filter your list of intent recommendations. See [Filtering intent recommendations](https://support.zendesk.com/hc/en-us/articles/9488234915610#topic_zwl_mlp_zfc).

### Understanding an intent recommendation

You can always review more details about a recommendation to help you decide if you want to accept or decline it. An intent recommendation includes the following details:

- Name, description, and category.
- Coverage, which is the percentage of tickets the intent would affect (new intent) or currently affects (intent conflict).
- The number of days used to calculate the suggestions. For example, seven days.
- The date the recommendation was created.
- For new intents, a list of five ticket examples that fit into this intent recommendation.

## Reviewing intent recommendations

As an alternative to manually creating custom intents, you can review and accept personalized intent recommendations to automate and simplify intent maintenance.

You can find intent recommendations on the Intent page in Admin Center every week when relevant suggestions are available.

Note: Intelligent triage starts suggesting intents one week after it’s been activated in your account.

**To review new intent recommendations**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Intelligent triage > Intent**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_intents_intent_list_new_columns.png)

   If you have new recommendations, a banner displays above your intents list.
2. Click the **Recommendations** tab.
3. Click a suggested intent’s **Name**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_intent_conflict_rec_list.png)

   The intent suggestion appears in the right-hand panel.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/intents_rec_add_new.png)

   See [Understanding an intent suggestion](#topic_zqx_1hj_zfc) to learn more.
4. Review the intent and click one of the following:
   - ****Add intent****

     If you accept the recommendation, it’s added to your list of intents and immediately starts detecting the intent in incoming requests.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_intent_suggestion_accepted.png)
   - **Decline**

     If you decline the recommendation, a dialog window opens asking for your feedback.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_intent_suggestion_decline_feedback.png)

     Select a reason and enter any additional comments and click **Submit feedback**.

## Resolving intent conflicts

Intelligent triage identifies duplicate or overlapping intents in your account. To help you fine-tune your intent coverage for your specific business needs, you can review and resolve any detected intent conflicts.

**To resolve intent conflicts**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Intelligent triage > Intent**.
2. Click the **Recommendations** tab.
3. Click the name of a recommendation to resolve an intent conflict.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_intent_conflict_rec_list.png)

   The recommendation opens on the right. You can view more information about why the recommendation was made, including the names of potential intent duplicates or intents with similar expressions.
4. Take one of the following actions:
   1. If the recommendation is for resolving a duplicate intent, click **Review duplicates**.

      ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_duplicate_intent_rec.png)

      Review the duplicated intents.

      ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_deactivate_duplicate_intent.png)

      Select an intent to deactivate, then click **Deactivate selected**. Confirm you want to deactivate the intent.
   1. If the recommendation is for resolving an overlapping intent, click **Review changes**.

      ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_intents_overlapping_rec.png)

      Review the suggested changes, then click **Save changes** to apply the suggestion.

      ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_intents_overlap_review.png)
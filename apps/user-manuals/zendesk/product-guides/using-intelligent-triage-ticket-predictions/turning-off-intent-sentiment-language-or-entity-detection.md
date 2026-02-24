# Turning off intent, sentiment, language, or entity detection

Source: https://support.zendesk.com/hc/en-us/articles/9678056232858-Turning-off-intent-sentiment-language-or-entity-detection

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Copilot |

Verified AI summary ◀▼

Learn how to turn off AI features like intent, sentiment, language, and entity detection in Admin Center. These settings are on by default, but you can manage them to suit your needs. Adjusting these features helps you control how AI analyzes support tickets, ensuring it aligns with your team's workflow and preferences.

[Intelligent triage](https://support.zendesk.com/hc/en-us/articles/4964463770650) uses artificial intelligence (AI) to automatically analyze new support tickets by predicting customer intent, sentiment, and language, and enriches tickets with actionable details, such as product names.

By default, intelligent triage intent, sentiment, and language detection settings are turned on. This article describes how admins can turn off these settings in Admin Center. If you've configured entity detection, you can turn off or delete an entity so that it's no longer detected in tickets.

This article contains the following topics:

- [Turning off intent detection](#topic_fh4_brd_hgc)
- [Turning off sentiment prediction](#topic_fcq_wr2_hgc)
- [Turning off language detection](#topic_a3r_4h2_hgc)
- [Turning off or deleting an entity](#topic_p4h_1lt_zbc)

Related articles:

- [Automatically detecting customer intent, sentiment, and language](https://support.zendesk.com/hc/en-us/articles/4550640560538)
- [Detecting unique information in tickets with entities](https://support.zendesk.com/hc/en-us/articles/6711181959194)

## Turning off intent detection

Intents are predictions about what each ticket is about. You can [configure intent settings](https://support.zendesk.com/hc/en-us/articles/4550640560538#topic_fh4_brd_hgc) in Admin Center.

By default, intent detection is turned on.

**To turn off intent detection**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Intelligent triage > Intent**.
2. Click **Manage Settings**.
3. Deselect **Detect intent**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_intent_turn_off_setting.png)
4. Click **Save**.

## Turning off sentiment prediction

Sentiments are predictions about how the user feels about their request. You can [configure sentiment settings](https://support.zendesk.com/hc/en-us/articles/4550640560538#topic_fcq_wr2_hgc) in Admin Center.

By default, sentiment detection is turned on.

**To turn off sentiment prediction**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Intelligent triage > Sentiment**.
2. Click **Manage Settings**.
3. Deselect **Detect sentiment**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_sentiment_turn_off_setting.png)
4. Click **Save**.

## Turning off language detection

Language is a prediction of what language the ticket is written in. You can [configure language detection](https://support.zendesk.com/hc/en-us/articles/4550640560538#topic_a3r_4h2_hgc) settings in Admin Center.

By default, language detection is turned on.

**To turn off language detection**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Intelligent triage > Language**.
2. Click **Manage Settings**.
3. Deselect **Detect language**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_language_turn_off_setting.png)
4. Click **Save**.

## Turning off or deleting an entity

If you no longer want an entity to be detected in tickets, you can delete the custom field associated with the entity. When you do this, entity-related highlighting is removed from all tickets, even tickets that were created while the entity was active.

You can also turn off entity detection for a custom field instead of deleting the field associated with the entity. When you do this, all entity-related highlighting is removed from all tickets, just like when you delete a custom field.

**To turn off entity detection for a custom field**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Intelligent triage > Entity**.
2. Click the entity you want to turn off.
3. Under **Update ticket fields with detected values** select **Don't update ticket fields**.
4. Deselect **Highlight entity values in all messages**.
5. Click **Save**.

**To delete a custom field associated with an entity**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Intelligent triage > Entity**.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) for the custom field associated with the entity you want to delete.
3. Click **Delete**.
4. Click **Delete** in the confirmation message.
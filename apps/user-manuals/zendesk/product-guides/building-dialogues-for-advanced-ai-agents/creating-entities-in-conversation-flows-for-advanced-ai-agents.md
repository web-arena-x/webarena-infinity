# Creating entities in conversation flows for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357749740698-Creating-entities-in-conversation-flows-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Entities hold pieces of information that have specific meaning. The advanced AI agent recognizes information as an entity and treats it in a particular way. You can add an entity to an AI agent by using a preset entity or by creating your own custom entity.

This article covers the following topics:

- [About entities](#topic_gy1_vqt_m2c)
- [Adding a preset entity](#topic_obw_1dt_m2c)
- [Creating a custom entity](#topic_owr_bdt_m2c)

## About entities

An entity represents information in a customer message that has a defined pattern, such as an email address. In that example, `email` is a preset entity. The information is attached to the conversation session and is available for later use by the AI agent.

Common uses for entities include the following:

- Sanitizing personally identifiable information (PII)
- Collecting and verifying a piece of information, such as an order number, so it can be used in a conversation flow
- Understanding and identifying product-specific descriptions in customer messages

After an entity is added, anything in customer messages that match the entity pattern can be identified and acted upon. For example, you might mask an email address with the placeholder <EMAIL>. Or you might ask for verification or security information, which can be sanitized before escalation. You can use the entity to validate that customer-entered information follows a format or is part of a list.

You can refer to this data later in the flow. For example, you can collect an email address from the user and save it to the conversation data for later use via [conditional blocks](https://support.zendesk.com/hc/en-us/articles/8357733406234) and [customer messages](https://support.zendesk.com/hc/en-us/articles/9060613203610). You can then apply an action using the information.

It’s recommended that you organize the entities list so that the highest priority and least sensitive ones are at the top.

When using numbers to represent scenarios in a channel where the customer can't use buttons, such as WhatsApp, you can create multilingual entity lists, including typos of each of the number scenarios. These should be ordered towards the top of the lists as they represent the greatest sensitivity.

If you're using entity recognition of numbers in your scenarios, ensure they’re not confused with other entities or intent predictions. Therefore, check the most specific first, in case you want to include an intent predicted, such as "wait a moment," in that customer message. Then check for the numbers. Otherwise, if a user says "wait a second," it would trigger scenario one instead of the intent.

## Adding a preset entity

Your advanced AI agent comes with the following preset entities:

- International bank account number (IBANs)
- Email
- Credit card
- United States Social Security number (SSN)
- Personal identity codes for various countries

**To add a preset entity**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Entities**.
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_entities.png)
3. Click **Add preset**.
4. Hover over the preset you want to add and click **Add entity**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_entity_presets.png)
5. Go back to the Entities page, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_menu_icon_verticle_sm.png)) in the upper-right corner, then select **Reorder entities** to change the order of the entities.

## Creating a custom entity

You can create a custom entity in order to build one with your own set of rules.

**To create a custom entity**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Entities**.
3. Select **New entity**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_entity_new.png)
4. Enter a name and optional description for your custom entity.

   The name can contain no spaces and alphanumeric characters only, in addition to underscores (\_) and hyphens (-).
5. Click **Sanitize** if you want the model to replace the detected custom information with a placeholder in order to protect PII.
6. Select a **Rule type** and create the rule.

   Types include the following options:

   - **Regular expression**: Also known as RegEx, this is a text string that appears as part of a repetitive pattern. It should represent all the possible patterns, formats, and length of the information you want to identify. See [RegEx reference for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756811162).
   - **Expression list**: A list of words to look for. For example, Berlin, Helsinki, Paris, Rome. You can implement partial words to identify a word as part of another word (such as "play" within "playing"), or whole words when the expression represents the whole word. Lemmatization recognizes when there are multiple ways to express the entity, such as "am," "are," "is," "was," "were," or "been" as the other forms of the verb "to be."
   - **Synonym list**: A list of word combinations provided in a CSV file. For example, product types or product colors. This cannot be mixed with other rules. Use the following example file format:

     ```
     item1, "item1-synonym1, item1-synonym2, item1-synonym3, item1-synonym4"
     item2, "item2-synonym1, item2-synonym2, item2-synonym3, item2-synonym4"
     item3, "item3-synonym1, item3-synonym2, item3-synonym3, item3-synonym4"
     ```
7. Select **Case sensitive** if the entity is case sensitive.
8. For expression lists, select **Whole words** if the expression represents the entire word.
9. Click **Add rule** to create additional rules as needed.
10. Click **Test and save**.

    The Validate rules pane opens.
11. Enter sample text and click **Test** to make sure the entity is working as expected.
12. Click **Save**.
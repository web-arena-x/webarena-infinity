# Editing and managing entities

Source: https://support.zendesk.com/hc/en-us/articles/9470811609370-Editing-and-managing-entities

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Copilot |

Verified AI summary ◀▼

Learn how to manage entity detection to enhance ticket processing. Add
synonyms to entity values for better detection of variations, ensuring
key information is captured. Customize how ticket fields update based
on detected values and choose whether to highlight these in messages.
Adjust settings to detect misspelled values, helping agents identify
and act on crucial details in customer interactions.

Customer requests often contain specific pieces of information that your agents need to
identify and act on in order to solve requests. Entity detection, which is part of [intelligent triage](https://support.zendesk.com/hc/en-us/articles/4550640560538), helps you define and detect this
information in tickets and messaging conversations so your tickets are automatically
updated with actionable details.

You can add synonyms to entity values to help detect different variations of entity
values. You can also manage and edit entities to ensure that entity detection works
accurately in your environment.

This article contains the following topics:

- [Adding synonyms to entity
  values](#topic_b1j_2v2_yfc)
- [Editing entity ticket field update behavior and highlighting](#topic_ath_zkt_zbc)

Related articles:

- [Detecting unique information in tickets with
  entities](https://support.zendesk.com/hc/en-us/articles/6711181959194)
- [Turning off intent, sentiment, language, or
  entity detection](https://support.zendesk.com/hc/en-us/articles/9678056232858)

## Adding synonyms to entity values

Adding synonyms to entities helps intelligent triage detect more variants
of entity values. For example, “Order ID” as a synonym for “Order number”.

Every time one of the synonyms appears in the ticket, it’s highlighted and
the corresponding entity value will be extracted if those settings are
activated.

**To add synonyms to entity values**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Intelligent triage > Entity**.
2. Click the entity you want to edit.
3. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) for a value name, then click **Edit
   synonyms**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_entity_settings_edit.png)
4. Enter synonyms for the value, then click **Save**.

   You can add up to 10
   synonyms.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_entity_values_syonyms.png)

   The synonyms are added
   and appear under the value name in the list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_entity_synonyms_values_saved.png)
5. Click **Save**.

   The synonyms you added are detected on new
   tickets.

## Editing entity ticket field update behavior and highlighting

You can edit entities to configure how the custom ticket field associated with the
entity is updated based on ticket comments or messages. You can also edit whether
entity values are highlighted in tickets and messaging conversations.

**To edit an entity**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Intelligent triage > Entity**.
2. Click an entity, then click **Manage settings**.
3. Under **Update ticket field with detected values**, update the behavior
   of the ticket field associated with the entity custom field by selecting one
   of the following options:
   - Don’t update ticket fields
   - Values in first message only
   - Values in subsequent messages only
   - Values in all messages
4. (Drop-down only) If you selected any option *except*
   **Don’t update ticket fields**, select **Replace existing ticket field
   value** if the new value in the ticket field should overwrite the old
   value. Otherwise, the ticket field will not be updated if it already has a
   value.
5. Under **Agent tools**, select or deselect **Highlight entity values in
   all messages**. When this option is selected, agents can [take action on highlighted
   entities](https://support.zendesk.com/hc/en-us/articles/9470696109338).
6. Under **Detection settings**, select or deselect **Detect misspelled
   values**.
7. Click **Save**.
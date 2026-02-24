# Adding entities to automatically detect information in tickets

Source: https://support.zendesk.com/hc/en-us/articles/8945765565594-Adding-entities-to-automatically-detect-information-in-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Copilot |

As part of the Copilot add-on, *entities* allow you to define and
automatically detect unique information in tickets and messaging conversations. You can then
use that information to populate associated custom ticket fields and power automated workflows
and reports. For more information, see [About entity detection](https://support.zendesk.com/hc/en-us/articles/6711181959194#topic_fb1_xkt_zbc).

To help you get the most out of Zendesk's AI Copilot features,
this article provides an overview on how admins can get started with adding entities.

This article contains the following sections:

- [Step 1: Create an entity](#topic_erm_rbf_m2c)
- [Step 2: Create workflows based on entities](#topic_usd_cfy_j2c)

**Related articles**:

- [About Zendesk Copilot](https://support.zendesk.com/hc/en-us/articles/5524125586330)
- [Detecting unique information in tickets with entities](https://support.zendesk.com/hc/en-us/articles/6711181959194)

## Step 1: Create an entity

An existing custom ticket field represents the piece of information (entity) you care
about. The values in the custom ticket field represent details about the entity.

For example, create an entity with a drop-down custom field named
Product Line that contains values such as Camera Model A, Camera Model B, and so on.

**To create an entity**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **Intelligent triage > Entity**.
2. Click **Create entity**.
3. Under **Select field type**, click either **Drop-down**, **Multi-select**, or
   **Regex**.
4. Under **Select custom field**, select a custom field.
5. Deselect **Detect entity** if you don't want to detect and
   highlight this entity in tickets yet. This option is selected by default.
6. Click **Create entity**.

   The entity's settings page opens. The
   options on the page will differ depending on which type of custom ticket field your
   entity is associated with:

   - If you created an entity associated with a drop-down or multi-select custom field,
     the page displays the entity's values.

     From this tab, you can optionally [add synonyms](https://support.zendesk.com/hc/en-us/articles/9470811609370) to the field values.
   - If you created an entity associated with a regex custom field, then the regular
     expression (regex) appears under Validation.

     You can enter text in the **Test
     detection** field in the right panel to check if the entity will be
     detected.
7. Click **Manage settings**.
8. Set the **Extraction rules**. Under **Update ticket field with
   detected values**, configure the behavior of the ticket field associated with the
   entity.

   **Values in all messages** is selected by default.
9. Under **Agent tools**, select **Highlight entity values in all
   messages** if you want entities to be highlighted in blue in tickets and messaging
   conversations. This option is selected by default.
10. Under **Detection settings**, select **Detect misspelled
    values** if you want to allow the system to find misspelled entity values. This option
    is selected by default.
11. Click **Save**.

When the entity is detected in tickets, the associated custom ticket field is populated or
updated. You can use the associated custom ticket field's tag and value to help you build
triggers, automations, and reporting.

## Step 2: Create workflows based on entities

You can use ticket triggers and other business rules to automate workflows based on
entities detected in tickets.

**To create a trigger based on entities**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_objects_rules_icon.png)
   **Objects and rules** in the sidebar, then select **Business rules >
   Triggers**.
2. On the Triggers page, click the **Ticket** tab, then click **Create
   trigger**.
3. Enter a **Name**, **Description**, and **Category** for your trigger. See [Creating ticket triggers](https://support.zendesk.com/hc/en-us/articles/4408886797466) for details.
4. In trigger **Conditions**, add the entity you want to use as part of the trigger
   condition.

   You can use the ticket tag related to value in the
   custom field that's associated with entity,

   For example:

   **Ticket > Tags
   | Contains at least one of... | Product\_Line\_Camera\_Model\_A**

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_gs_entity_trigger_condition.png)
5. In trigger **Actions**, add the actions you want to perform when the condition
   applies.

   For example:

   **Ticket > Group | Product Team A**

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_gs_entity_trigger_action.png)

   For more information on trigger conditions and actions, see [Ticket trigger conditions and actions reference](https://support.zendesk.com/hc/en-us/articles/4408893545882) and [Zendesk chat and messaging triggers conditions and actions
   reference](https://support.zendesk.com/hc/en-us/articles/4408842880282).
6. Click **Create trigger**.
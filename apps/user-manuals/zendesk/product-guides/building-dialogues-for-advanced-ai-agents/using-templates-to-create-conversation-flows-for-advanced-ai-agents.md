# Using templates to create conversation flows for advanced AI agents 

Source: https://support.zendesk.com/hc/en-us/articles/8357756562330-Using-templates-to-create-conversation-flows-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

A template is a specific version of a reply for advanced AI agents that you can use over and over in conversation flows, or dialogues. You can create a new template from scratch, or copy an existing reply to a new template. You can also create templates in multiple languages.

Since template replies aren’t triggered directly, you can use them to draft and edit new dialogues before making them visible to customers.

Templates are also useful for:

- Building reusable patterns, such as CSAT flow
- Editing dialogues that are live in production
- Saving a dialogue for reuse

This article covers the following topics:

- [Accessing and viewing existing templates](#topic_lg1_fbj_l2c)
- [Creating a new template](#topic_lv5_dbj_l2c)
- [Copying a reply to a new template](#topic_rqh_bg3_l2c)
- [Replacing a dialogue with a template](#topic_px3_dg3_l2c)
- [Grouping replies under a template](#topic_p43_2g3_l2c)
- [Changing the language for a reply](#topic_cyb_fg3_l2c)
- [Deleting replies and templates](#topic_ipc_gg3_l2c)
- [Reviewing replies linking to a template](#topic_tgt_gg3_l2c)

## Accessing and viewing existing templates

View existing templates or create a new one on the Templates page.

**To open the Templates page**

- In AI agents - Advanced, in the top-right corner, use the AI agent drop-down field to select the AI agent with the templates you want to view.
- In the left sidebar, click **Content** > **Templates**.

 If there are no templates yet, you’re prompted to create one. Otherwise, the Templates page opens.

 ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_template_page.png)

The Templates page shows the following information for each template:

- **Template name and description**.
- **Linked in replies**: Replies that link to the template.
- **Languages**: Status of dialogue for each active language.
- **Actions**: Number of actions applied within the template’s dialogue.
- **Last modified**: When the template was last changed.

Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_menu_icon_verticle_sm.png)) in each row to access the following actions:

- **View information**: View and update the template name and description.
- **Copy to another AI agent**: Share the template across AI agents within your organization.
- **Delete**: Remove the template, after deleting any links to it from replies.

## Creating a new template

You can create a template even if the AI agent is live. Since the template isn’t triggered automatically, customers cannot see it until you link to it from an active reply.

**To create a template**

1. On the [Templates page](#topic_lg1_fbj_l2c), click **Create your first template** if there are no existing templates, otherwise click **Add template**.
2. Enter a name and an optional **Description**.
3. Click **Save**.

Once you have created a template, you can add a conversation flow for it in the dialogue builder.

**To add a dialogue to a template** 

1. On the Templates page, click the plus icon (+) under the desired language.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_template_without_dialogue.png)

   If there is a green dot under the language, a dialogue already exists and can be edited.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_template_with_dialogue.png)
2. Review the settings and click **Next**.

   The dialogue builder opens.
3. [Create the dialogue](https://support.zendesk.com/hc/en-us/articles/8357749494810).

Once a template has a dialogue, you can use it in a conversation flow by selecting it in a Link to block in the [dialogue builder](https://support.zendesk.com/hc/en-us/articles/8357749494810).

## Copying a reply to a new template

You can copy an existing dialogue and save it as a new template. Some reasons to do this are to create a backup of the dialogue, to make edits to it in draft form, or to save it for later reuse.

**To copy a reply to a new template**

1. In AI agents - Advanced, in the top-right corner, use the AI agent drop-down field to select the AI agent you want to copy a dialogue from.
2. In the the left sidebar, click **Content** > **Use cases** (for zero-training AI agents or AI agents with agentic AI) or **Content** > **Intents** (for expression-based AI agents).
3. Select the use case or intent that contains the reply you want to copy.
4. Select the **Replies** tab.
5. Click the edit dialogue icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_edit_dialogue_icon.png)) for the reply you want to copy.

   The dialogue builder opens.
6. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_menu_icon_verticle_sm.png)) in the upper-right corner, then select **Copy to a new Template**.
7. Enter a template name and optional description, then click **Create template from dialogue**.

   The dialogue is saved as a template.

## Replacing a dialogue with a template

After you create a template reply dialogue, you can swap it into an existing reply in any AI agent you manage. One reason to do this is to edit and test a new dialogue for an active reply, and swap it with the old dialogue when ready.

**To replace a dialogue in a reply with a template**

1. In AI agents - Advanced, in the top-right corner, use the AI agent drop-down field to select the AI agent you want to copy a dialogue from.
2. In the left sidebar, click **Content** > **Use cases** (for zero-training AI agents or AI agents with agentic AI) or **Content** > **Intents** (for expression-based AI agents).
3. Select the use case or intent that contains the reply you want to use the template for.
4. Select the **Replies** tab.
5. Click the edit dialogue icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_edit_dialogue_icon.png)) for the reply with dialogue you want to replace.

   The dialogue builder opens.
6. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_menu_icon_verticle_sm.png)) in the upper-right corner, then select **Replace dialogue**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_replace_dialogue_menu.png)
7. Select the template dialogue you want to use.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_replace_dialogue_modal.png)
8. Click **Replace** to simultaneously replace the dialogue and save the reply.

## Grouping replies under a template

You can group each language reply under one template.

**To group replies under a template**

1. In the reply you want to add to a template, open the dialogue builder.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_menu_icon_verticle_sm.png)) in the upper-right corner, then select **Move to a different template**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_move_dialogue_menu.png)
3. Select the template where you'd like to move the reply, then select the language to associate it with.

   You can have only one template reply per language.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_move_dialogue_modal.png)

When you finish, you can [delete the template](#topic_urj_ng3_l2c) that no longer has a reply associated, if needed.

## Changing the language for a template reply

As with other replies, you can change the language for a template reply.

**To change a reply language**

1. In the [dialogue builder](https://support.zendesk.com/hc/en-us/articles/8357749494810), click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_menu_icon_verticle_sm.png)) in the upper-right corner, then select **View info**.

   The Dialogue settings pane appears.
2. Under **Dialogue language**, select the language you want to use.
3. Click **Save** to save the new language selection.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_template_reply_change_language.png)

## Deleting replies and templates

You can delete a reply associated with a template or you can delete a full template.

### Deleting a reply in a template

You can delete a reply associated with a template. You cannot delete a template reply if another reply [links to it](#topic_tgt_gg3_l2c).

**To delete a template**

- In the [dialogue builder](https://support.zendesk.com/hc/en-us/articles/8357749494810) for the reply you want to delete, click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_menu_icon_verticle_sm.png)) in the upper-right corner, then select **Delete**.

### Deleting a template

You can delete a template if you no longer need it. You cannot delete a template reply if another reply [links to it](#topic_tgt_gg3_l2c).

**To delete a template**

1. On the [Templates page](#topic_lg1_fbj_l2c), click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_menu_icon_verticle_sm.png)) beside the template you want to delete, then select **Delete**.
2. When asked to confirm, click **Delete**.

## Reviewing replies linking to a template

You can review a list of replies linking to a template to understand where a template is being used. Do this from the template details or from the dialogue settings.

**To view where a template is used in template details**

1. On the Templates page, review the **Linked in replies** column to view the number of times this template is being used.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_linkedin.png)
2. Click the row of the template you want to review.

   The Template details page opens with a list of replies that link to the template.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_linkedin_details_cropped.png)
3. Click the open dialogue icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_edit_dialogue_icon.png)) to navigate to the reply.

**To view where a template is used in dialogue settings**

1. In a reply, click **Edit dialogue** to open the dialogue builder.
2. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_menu_icon_verticle_sm.png)) in the upper-right corner, then select **View info**.
3. In the settings pane on the right, under Linked in responses, review the replies this template is routed to through the link to block.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_linkedin_dialogue_settings.png)
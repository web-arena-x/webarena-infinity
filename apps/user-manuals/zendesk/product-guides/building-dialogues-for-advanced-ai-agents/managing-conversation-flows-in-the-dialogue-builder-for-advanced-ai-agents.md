# Managing conversation flows in the dialogue builder for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/9066753203738-Managing-conversation-flows-in-the-dialogue-builder-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

The dialogue builder is where you manage conversation flows, or dialogues, for your advanced AI agents. A dialogue is a scripted conversation flow that uses branching logic to determine an advanced AI agent's responses and actions during a conversation with a customer.

Each dialogue is linked to a specific [reply](https://support.zendesk.com/hc/en-us/articles/9624068102682), and each reply is in turn linked to a [use case](https://support.zendesk.com/hc/en-us/articles/9041901679130).

This article contains the following topics:

- [Editing an existing dialogue](#topic_nvb_tzl_52c)
- [Viewing a dialogue's settings](#topic_pvb_tzl_52c)
- [Switching between dialogues](#topic_uvb_tzl_52c)
- [Viewing and managing block details](#topic_pfv_vzz_t2c)
- [Searching for content within a dialogue](#topic_ily_f2s_yhc)
- [Copying and pasting content in the dialogue builder](#topic_id2_22p_ghc)
- [Reverting a dialogue to a previous version](#topic_tyw_5zt_z2c)

Related articles:

- [Creating conversation flows in the dialogue builder for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749494810)
- [Using templates to draft conversation flows for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756562330)

## Editing an existing dialogue

After you [create a dialogue](https://support.zendesk.com/hc/en-us/articles/8357749494810), you can always edit it to update the conversation flow.

**To edit an existing dialogue**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Use cases**.
3. Select the use case that contains the dialogue you want to edit.
4. Select the **Replies** tab.
5. Select the reply you want to edit the dialogue for.
6. Click **Edit dialogue**.

   The dialogue builder opens, showing the existing dialogue. For more information on working within the dialogue builder, see [Creating conversation flows in the dialogue builder for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749494810).

## Viewing a dialogue's settings

In the dialogue builder, you can view a dialogue's settings. From here, you can change the language of the reply and see where the reply is linked to.

**To view a dialogue's settings**

1. [Open the dialogue builder](#topic_nvb_tzl_52c) for the dialogue you want to work with.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)) in the upper-right corner and select **View info**.

   The Dialogue settings panel appears, showing the following information:

   - **Intent**: Use case the dialogue is associated with.
   - **Dialogue language**: Language the dialogue is associated with.
   - **Linked in responses**: Other dialogues the current dialogue is linked from.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_dialogue_settings_panel.png)

## Switching between dialogues

From within the dialogue builder, you can easily switch between different dialogues.
This saves you time because you don't have to return to the list of use cases or replies every time you want to open a different dialogue.

Important: Make sure to save any edits to the current dialogue before switching to a different one. Any unsaved changes to the current dialogue are lost when you switch.

**To switch between dialogues**

1. [Open the dialogue builder](#topic_nvb_tzl_52c) for a dialogue you want to work with.
2. Click the drop-down menu in the top-left corner to search for and select the dialogue you want to open.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_agents_dialogue_builder_switch.png)

   The selected dialogue opens.

## Viewing and managing block details

Within the dialogue builder, you can view and manage the details of an individual block in the conversation flow.

**To view and manage block details**

1. [Open the dialogue builder](#topic_nvb_tzl_52c) for the dialogue you want to work with.
2. Click the block you want to view details for.

   The Details panel appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_block_details_example.png)

   The specific fields available in this pane depend on the type of block you selected, but you can always:

   - Click **Add action** to add or edit which [actions](https://support.zendesk.com/hc/en-us/articles/8357756651290) should be performed when this block is activated during a conversation. Any added actions are shown here.
   - Click the **Status** dropdown to configure which [custom resolution state](https://support.zendesk.com/hc/en-us/articles/8357756466586)
     should be set when this block is activated during a conversation.

## Searching for content within a dialogue

In the dialogue builder, you can search for specific content. You can search across all block input fields, drop-down selections, and attached actions, with support for case-sensitive and whole-word matching.

**To search for content within a dialogue**

1. [Open the dialogue builder](#topic_nvb_tzl_52c) for the dialogue you want to work with.
2. Click the magnifying glass icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/search_icon.png)) in the upper left.

   Alternatively, press Control+F on a PC or Command+F on a Mac.
3. Enter your search term.

   Matching results are highlighted in orange.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_search_in_dialogue_builder.png)
4. Cycle through matching results by clicking the Next (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/next_arrow_icon.png)) and Previous (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/previous_arrow_icon.png)) arrows.

   Alternatively, press Enter on a PC or Return on a Mac.
5. (Optional) Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_options_menu_horizontal.png)) to configure the following settings for your search term:
   - **Match case**: Matching results must have the same case (uppercase or lowercase) as the search term.
   - **Whole words**: Matching results must be surrounded by spaces (or be the only word, the first word with a space after it, or the last word with a space before it).

## Copying and pasting content in the dialogue builder

Within the dialogue builder, you can copy a block or an entire branch to use elsewhere in the same dialogue or a different dialogue. You can even paste the copied content in a dialogue for a different AI agent.

When pasting copied dialogue content between AI agents, keep the following points in mind:

- If the two AI agents don't have the same [use cases](https://support.zendesk.com/hc/en-us/articles/9041901679130), [replies](https://support.zendesk.com/hc/en-us/articles/9624068102682), [templates](https://support.zendesk.com/hc/en-us/articles/8357756562330), [segments](https://support.zendesk.com/hc/en-us/articles/9413046533530), or [entities](https://support.zendesk.com/hc/en-us/articles/8357749740698), the content is pasted, but it doesn't contain those missing components.
- Any pasted "Link to" blocks are empty, as you can't link to a reply in another AI agent.

**To copy and paste content in the dialogue builder**

1. [Open the dialogue builder](#topic_nvb_tzl_52c) for the dialogue you want to work with.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) on the the block you want to copy and select **Copy**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_dialogue_builder_copy.png)

   Everything below the block is saved to your clipboard. When you paste your content later, you can decide whether you want to paste only the first block or the whole branch.
3. Navigate to where you want to paste the copied content, either in the same dialogue or a different dialogue, even one in a different AI agent.
4. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_menu_icon_verticle_sm.png)) on an existing block or the plus icon (+)
   below a block, and then select **Paste block** or **Paste branch**.

   You can paste anywhere in the conversation flow as long as it doesn't conflict with a block placement restriction. If it does, the paste options aren't available. See [Available block types](https://support.zendesk.com/hc/en-us/articles/8357749494810#topic_krz_vym_g2c) for information on block placement restrictions.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_dialogue_builder_paste.png)

## Reverting a dialogue to a previous version

A version history is maintained for each dialogue. This means you can quickly revert to a previous version of a dialogue if a newer version includes changes you don’t want to keep.

**To revert a dialogue to a previous version**

1. [Open the dialogue builder](#topic_nvb_tzl_52c) for the dialogue you want to work with.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)) in the top-right and select **Version history**.

   The Version history panel appears. Versions are grouped by day.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_dialogue_builder_version_history.png)
3. (Optional) Use the **Type** drop-down to filter to the version history entries:
   - **Show only published versions**: Shows only publish events, not save events.
   - **Show only my published versions**: Shows publish events from your user only, not save events.
   - **Show only my saved and published versions**: Shows publish and save events from your user only.
4. Click to expand the day that includes the version you want to revert back to.

   Each version shows the timestamp and user who saved or published it. Any notes included when the user saved or published the version are shown as well.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_dialogue_builder_version_history_notes.png)
5. (Optional) To add, edit, or delete the notes a user entered when they saved or published a version of the dialogue, hover your mouse over a version, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)), and select **Add note**, **Edit note**, or **Delete note**.
6. Click the version you want to revert back to.

   The version opens in a read-only state.
7. In the read-only version, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)) in the top-right and select **Restore as draft**.

   The version is restored as the current draft, and the live AI agent is not affected.
8. To make the restored version live to customers interacting with the AI agent, click **Publish** or **Publish with note**.
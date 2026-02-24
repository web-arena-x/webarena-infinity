# Reviewing and managing actions for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8566644914202-Reviewing-and-managing-actions-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

After you [create actions](https://support.zendesk.com/hc/en-us/articles/8357756623770#topic_kkk_jyl_rgc) to allow AI agents to perform certain tasks during conversations with customers, you can review, edit, or delete those actions as needed.

This article contains the following topics:

- [Reviewing actions in conversation logs](#topic_c5x_ppl_rgc)
- [Editing an action](#topic_npt_qpl_rgc)
- [Deleting an action](#topic_wxn_rpl_rgc)

Related articles:

- [About actions for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756651290)
- [Creating and adding actions for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756623770)
- [About events for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749555610)

## Reviewing actions in conversation logs

In [conversation logs](https://support.zendesk.com/hc/en-us/articles/8357749580186), you can find detailed information about which actions were applied to a conversation.

**To review actions in conversations logs**

1. In [AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/8357756913178), use the AI agent drop-down field in the top-right corner to select the AI agent you want to review actions for.
2. Click **Conversation logs** in the sidebar.
3. Select a conversation.

   In the conversation pane that appears, any actions executed during the conversation appear in gray boxes.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_review_action_convo_log_1.png)
4. Select an action in the conversation to see which action was executed and at what level (AI agent, use case, or block).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_review_action_convo_log_2.png)

   Note: Actions that were applied to a conversation before the introduction of reusable actions don’t have a snapshot view.
   Clicking them takes you directly to where they were applied.
5. Click the action name to open the Executed action details pane.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_review_action_convo_log_3.png)

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_review_action_convo_log_4.png)

   This pane shows the configuration of the action as it was when it was executed during the conversation, even if the action’s configuration has since changed.
6. (Optional) Click **View action** to open the **Action details** pane.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_review_action_convo_log_5.png)

   From this pane, you can:

   - Click **Edit action** to [update the action’s configuration](reviewing-and-managing-actions-for-advanced-ai-agents.md#h_01JFDJ99S9K4PZ1ESQVMJYGQHQ) on the Actions page.
   - Select any of the entries under the **Usage** heading to jump to the action’s configuration at the [AI agent level](https://support.zendesk.com/hc/en-us/articles/8357756623770#topic_opk_kyl_rgc), [use case level](https://support.zendesk.com/hc/en-us/articles/8357756623770#topic_zbz_kyl_rgc), or [block level](https://support.zendesk.com/hc/en-us/articles/8357756623770#topic_b4n_lyl_rgc).

## Editing an action

Because actions can be reused at multiple levels, easy management is crucial for keeping your actions up to date. When you update an action, those updates are applied to every location where the action is used.

Actions can be edited from the Actions page, or from any place where actions can be added.

**To edit an action**

1. In [AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/8357756913178), use the AI agent drop-down field in the top-right corner to select the AI agent you want to edit actions for.
2. Click **Content** in the sidebar, then select **Actions**.
3. Select the action you want to edit.

   The Action details pane appears. Under Usage, note the locations where the action is currently used. All of these locations will be affected by any updates you make to the action.
4. Click **Edit action**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_edit_action.png)
5. Update the action’s configuration as necessary.

   For help filling out the fields, see [Creating an action](https://support.zendesk.com/hc/en-us/articles/8357756623770#topic_kkk_jyl_rgc).
6. Click **Apply to all instances**.

   The number included in the button’s label tells you how many locations will be affected by your changes.

Your changes are applied to the action going forward. Any instances of the action that were already executed in conversations are not affected.

## Deleting an action

Deleting an action affects all the locations where it’s used. Ensure that you no longer need the action anywhere before deleting it.

If an action is still needed in some areas but not in others, remove it from the specific locations where it should no longer be triggered instead of deleting it.

**To delete an action**

1. In [AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/8357756913178), use the AI agent drop-down field in the top-right corner to select the AI agent you want to delete actions for.
2. Click **Content** in the sidebar, then select **Actions**.
3. For the action you want to delete, click the options (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)) menu and select **Delete**.

   The Delete action dialog appears, showing you how many locations the action is currently used in.
4. Click **Delete**.
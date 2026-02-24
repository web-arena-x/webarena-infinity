# Creating and adding actions for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357756623770-Creating-and-adding-actions-for-advanced-AI-agents

---

You can createactionsto allow AI agents to perform certain tasks during conversations with customers. When you create an action, you can use it at the AI agent level, use case level, or block level.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

You can create [actions](https://support.zendesk.com/hc/en-us/articles/8357756651290) to allow AI agents to perform certain
tasks during conversations with customers. When you create an action, you can use it at
the AI agent level, use case level, or block level.

This article contains the following topics:

- [Creating an action](#topic_kkk_jyl_rgc)
- [Adding an action at the AI agent level](#topic_opk_kyl_rgc)
- [Adding an action at the use case level](#topic_zbz_kyl_rgc)
- [Adding an action at the block level](#topic_b4n_lyl_rgc)
- [Reordering actions](#topic_lgd_nyl_rgc)

Related articles:

- [About actions for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756651290)
- [Reviewing and managing actions for advanced AI
  agents](https://support.zendesk.com/hc/en-us/articles/8566644914202)
- [About events for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749555610)

## Creating an action

The actions you create are reusable for that AI agent across the AI agents - Advanced
add-on. When you create an action, you can easily add it at the AI agent, use case,
or block level.

Actions can be created from the Actions page, or from any place where actions can be
added.

Note: You can’t create actions with duplicate configurations,
even if the Name field is different.

**To create an action**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to
   work with.
2. Click **Content** in the sidebar, then select **Actions**.
3. Click **Create action**.
4. In **Name**, enter a descriptive name for the action.
5. In **Target**, select an appropriate target:
   - If you’re building a conversation action, select
     **Conversation**.
   - If you’re building a CRM action, select the specific CRM your AI
     agent is integrated with.
6. In **Task**, select which task the action should perform:
   - If you’re building a conversation action, see [Available conversation actions
     for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756631706) for more information about the
     available options, including additional fields associated with each
     task.
   - If you’re building a CRM action, see the appropriate article below
     for more information about the available options, including
     additional fields associated with each task:
     - [Available CRM actions for
       advanced AI agents and Zendesk Support](https://support.zendesk.com/hc/en-us/articles/8357750876826)
     - [Available CRM actions for
       advanced AI agents and Zendesk Chat](https://support.zendesk.com/hc/en-us/articles/8357750804250)
     - [Available CRM actions for
       advanced AI agents and Sunshine
       Conversations](https://support.zendesk.com/hc/en-us/articles/8357734565402)
7. Click **Create**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_create_action_window.png)

## Adding an action at the AI agent level

AI agent–level actions are executed in every conversation your AI agent engages in.
They require an [event](https://support.zendesk.com/hc/en-us/articles/8357749555610) and an associated action. You can:

- [Add an action at the AI agent
  level](#topic_xkq_n23_g3c)
- [Trigger a reply when a
  conversation starts or becomes inactive](#topic_axm_d23_g3c)

### Adding an action at the AI agent level

You can add an action at the AI agent level.

**To add an action at the AI agent level**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to
   work with.
2. Click **Settings** in the sidebar, then select **AI agent settings**.
3. Select the **Events and actions** tab.

   This page shows all the
   events you’ve configured an AI agent-level action for.
4. Click **Add action**.
5. From the drop-down list, select the event that should trigger the
   action.

   For more information about each event, see [About events for advanced AI
   agents](https://support.zendesk.com/hc/en-us/articles/8357749555610).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_bot-level_action_example.png)
6. From the next drop-down list, select an existing action or click
   **Create action** to [create a new one](#topic_kkk_jyl_rgc).

   Your action is added to the
   list under the event you associated it with.

### Triggering a reply when a conversation starts or becomes inactive

You can trigger a specific reply (dialogue) when a conversation starts or when it
becomes inactive. This special action can be triggered based only on the
Conversation started or Conversation inactive event.

**To trigger a reply when a conversation starts or becomes inactive**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to
   work with.
2. Click **Settings** in the sidebar, then select **AI agent settings**.
3. Click the drop-down arrow next to **Add action** and select Trigger
   reply on event.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_trigger_reply_on_event.png)

   The Activate reply on event
   dialog appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_activate_reply_on_event.png)
4. Select either **Conversation started** or **Conversation
   inactive** as the event that should trigger the reply.
5. In **Select reply**, select the reply (dialogue) that should be
   triggered when the event you selected above occurs.
6. Click **Save**.

## Adding an action at the use case level

Use case–level actions are executed when a specific use case is triggered during a
conversation. You select the action you want to execute when the use case is
triggered. Use case–level actions are particularly useful if you want to apply
actions to all replies within a use case.

**To add an action at the use case level**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to
   work with.
2. Click **Content** in the sidebar, then select **Use cases**.
3. Select the use case you want to associate an action with.
4. On the **General** tab, under **Actions**, click **Add action**.
5. From the drop-down list, select an existing action or click **Create
   action** to [create a new
   one](#topic_kkk_jyl_rgc).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_intent-level_action_example.png)

   Your action is added
   under Actions.
6. Click **Save**.

## Adding an action at the block level

Block-level actions are executed when a particular block within a conversation flow
is reached. These actions are useful for more granular control within your
dialogues.

Note: Actions are executed *before* the contents of the
block. For example, if an action is added to an AI agent message block, the
action occurs before the AI agent message is sent.

**To add an action at the block level**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to
   work with.
2. Click **Content** in the sidebar, then select **Use cases**.
3. Select the use case that contains the dialogue you want to add an action to.
4. Select the **Replies** tab.
5. Select the reply that contains the dialogue you want to add an action
   to.
6. Click **Edit dialogue**.

   The dialogue builder opens.
7. Select the block you want to add an action to.
8. In the **Details** pane on the right, under **Actions**, click **Add
   action**.
9. From the drop-down list, select an existing action or click **Create
   action** to [create a new
   one](#topic_kkk_jyl_rgc).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_block-level_action_example.png)

   Your action is added
   under Actions.
10. **Save** or **Publish** the dialogue.

## Reordering actions

You can change the order of the actions you’ve added so that they’re performed in the
correct order, regardless of the order you added them in.

**To reorder an action**

1. Open the actions you’ve added at the [AI agent](#topic_opk_kyl_rgc), [use case](#topic_zbz_kyl_rgc), or [block level](#topic_b4n_lyl_rgc).
2. Click the grabber icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/exp-dash-tab-112.png)) next to the action you want to
   reorder, then drag and drop it into another position.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_reordering_actions.png)

   When you reorder actions at
   the:
   - AI agent level, your changes are automatically saved.
   - Use case level, your changes are automatically saved for AI agents
     with agentic AI, but must be manually saved for zero-training AI
     agents.
   - Block level, you must manually save your changes.
# Adding and removing the welcome reply for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357756557594-Adding-and-removing-the-welcome-reply-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

The welcome reply is a [system reply](https://support.zendesk.com/hc/en-us/articles/8357749481882) for advanced messaging AI agents. It greets the
customer when they reach out and sets the tone for the conversation.

For Zendesk Chat, you must take an extra step to add a trigger reply action to trigger the
welcome reply. For Zendesk Chat with language detection, you must [create a template block](https://support.zendesk.com/hc/en-us/articles/8357756692890) as well.

This article covers the following topics:

- [Adding the welcome reply](#topic_y1g_5kf_p2c)
- [Removing the welcome reply](#topic_wkx_vkf_p2c)

## Adding the welcome reply

Add a welcome reply to greet customers when they reach out via messaging.

For instructions, see [Editing system replies](https://support.zendesk.com/hc/en-us/articles/8357749481882#topic_jhb_k4p_xfc).

If you use Zendesk Chat, also perform the applicable steps below.

### Adding a conditional block before the welcome reply (Zendesk Chat only)

If you use Zendesk Chat with an expression-based AI agent, you need to create a
conditional block to ensure [language detection](https://support.zendesk.com/hc/en-us/articles/8357756692890) works seamlessly.

**To set up a conditional block before the welcome reply for Zendesk Chat**

1. In the [dialogue builder](https://support.zendesk.com/hc/en-us/articles/8357749494810), click the plus (+) icon to
   add a conditional block.

   The conditional block appears along with the first
   condition block and the fallback block.
2. In the conditional block, select the `active_language` parameter.
3. Create condition blocks for each language.
4. For each condition block and the fallback block, click the plus (+) icon and select
   **Link to**.
5. Select **Welcome reply**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_conditional_welcome_reply.png)

### Adding a trigger reply action (Zendesk Chat only)

If you use Zendesk Chat, after you set up the welcome reply, you also need to add a
trigger reply action to trigger the welcome reply.

**To add the trigger reply action for Zendesk Chat**

1. In AI agents - Advanced, click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_side_settings_icon.png)
   **Settings** in the sidebar.
2. In AI agent settings, click **Events and actions**.
3. Click the options menu icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_menu_icon_verticle_sm.png)) next to the Add action button and select **Trigger reply
   on event**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_trigger_reply_on_event.png)
4. Complete the following fields:
   - For Select event, select **Conversation started**.
   - For Select reply, select the welcome reply you want to use.
5. Click **Save**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_activate_reply_on_event.png)

## Removing the welcome reply

You can remove the welcome reply if needed.

If you created a trigger reply action for Zendesk Chat, you can remove that too. It’s
recommended to remove the trigger reply action first.

**To remove the trigger reply action for Zendesk**

1. In AI agents - Advanced, click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_side_settings_icon.png)
   **Settings** in the sidebar.
2. In AI agent settings, click **Events and actions**.
3. Click the delete icon (x) next to the trigger reply action you want to remove.

**To remove the welcome reply**

1. In the main menu on the left, click **Content** > **Use cases** (for [zero-training AI agents](https://support.zendesk.com/hc/en-us/articles/8357749447194)) or **Content** > **Intents**
   (for [expression](https://support.zendesk.com/hc/en-us/articles/8357751704474)-based AI agents).
2. Select the Welcome reply.
3. Select the language version of the reply you want to edit and click **Edit
   dialogue**.
4. Delete all blocks from the dialogue except the first AI agent message block.
5. Delete all content from the AI agent message block.
6. Click **Save** or **Publish**.
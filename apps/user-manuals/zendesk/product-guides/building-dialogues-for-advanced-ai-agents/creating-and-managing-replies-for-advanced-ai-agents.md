# Creating and managing replies for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/9624068102682-Creating-and-managing-replies-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

In an advanced AI agent, a *reply* contains the [dialogue](https://support.zendesk.com/hc/en-us/articles/8357749494810) (or conversation flow) that’s presented to customers during a conversation when a specific [use case](https://support.zendesk.com/hc/en-us/articles/9041901679130) is detected.

Note: Replies are required only for [zero-training AI agents](https://support.zendesk.com/hc/en-us/articles/8357749447194). For [AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/8966284087066), replies are optional, as [procedures](https://support.zendesk.com/hc/en-us/articles/8979864563610) can be used instead.

This article contains the following topics:

- [Creating a reply](#topic_i1v_nzx_jgc)
- [Activating a reply](#topic_jyw_4zx_jgc)
- [Editing a reply's settings](#topic_xmy_pzx_jgc)
- [Viewing the change log for a reply](#topic_fhx_qzx_jgc)
- [Copying a reply to another AI agent](#topic_lmg_k54_3hc)
- [Deactivating a reply](#topic_b1m_rzx_jgc)
- [Deleting a reply](#topic_ayy_rzx_jgc)

Related article:

- [Viewing and editing system replies for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749481882)

## Creating a reply

After you [create a use case](https://support.zendesk.com/hc/en-us/articles/9041901679130), you need to create an associated reply. The reply, in turn, contains the dialogue that dictates what messages an advanced AI agent will send and what actions it will take during a conversation with a customer.

**To create a reply**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Use cases**.
3. Select the use case you want to create a reply for.
4. Select the **Replies** tab.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_reply_create_add_reply.png)
5. Click **Add reply**.

   The Create automation reply window appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_reply_create.png)
6. In **Language**, select the language you want to create a reply for.

   If you don’t see the language you want, [add a supported language](https://support.zendesk.com/hc/en-us/articles/8357749666714#topic_rmc_kzx_jgc) first.
7. In **Reply name**, enter a short name for the reply.

   This name doesn't appear to customers.
8. If you want the AI agent to immediately begin using the reply’s associated dialogue in conversations with customers, select **Activate reply**.

   Note: It’s recommended to wait to activate the reply until you’ve built and tested the dialogue associated with the reply first.
9. Click **Save and continue**.

   The dialogue builder opens. From here, you [create the dialogue](https://support.zendesk.com/hc/en-us/articles/8357749494810) (or conversation flow) that’s associated with this reply.

## Activating a reply

A reply must be activated before the AI agent can use its associated dialogue in conversations with customers.

**To activate a reply**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Use cases**.
3. Select the use case that contains the reply you want to activate.
4. Select the **Replies** tab.
5. Find the reply you want to activate, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)), and select **Activate**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_activate_reply.png)

## Editing a reply's settings

You can edit a reply’s settings, including the language and use case it’s associated with.

**To edit a reply’s settings**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Use cases**.
3. Select the use case that contains the reply you want to edit.
4. Select the **Replies** tab.
5. Click the reply you want to edit the settings for.
6. On the **Details** tab, click **Advanced settings**.
7. From here, you can edit the following settings for the reply:
   - **Language**: The language the reply is associated with.
   - **Intent**: The use case the reply is associated with.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_reply_edit_settings.png)
8. Click **Save**.

## Viewing the change log for a reply

You can view the change log for a reply to see what changes have been made to it, by whom, and when.

**To view the change log for a reply**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Use cases**.
3. Select the use case that contains the reply you want to view the change log for.
4. Select the **Replies** tab.
5. Click the reply you want to view the change log for.
6. Select the **Change log** tab.
7. Review the details in the following columns:
   - **Last update**: The timestamp of the change.
   - **Action**: What change was made to the reply and which user made the change.
   - **User**: The user who made the change.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_reply_view_change_log.png)

## Copying a reply to another AI agent

If you've already [created a reply](#topic_i1v_nzx_jgc), you can copy it to another AI agent to speed up the process of building multiple AI agents. Copying a reply also copies its associated dialogue.

Before you copy a reply, make sure any linked replies, [templates](https://support.zendesk.com/hc/en-us/articles/8357756562330), [segments](https://support.zendesk.com/hc/en-us/articles/9413046533530), or [entities](https://support.zendesk.com/hc/en-us/articles/8357749740698) in the reply's dialogue also exist in the AI agent you're copying to. These objects aren't copied automatically and must be created or copied manually.

Note: You can't copy a [system reply](https://support.zendesk.com/hc/en-us/articles/8357749481882#topic_edj_gnp_xfc) between AI agents. You can copy only replies that you've created.

**To copy a reply to another AI agent**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Use cases**.
3. Select the use case that contains the reply you want to copy.
4. Select the **Replies** tab.
5. Find the reply you want to copy, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)), and select **Copy reply**.

   The Copy reply to another AI agent window appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_copy_reply_to_another_agent.png)
6. In **Reply**, confirm the reply you want to copy is selected.

   If not, select the desired reply.
7. In **Destination AI agent**, select the AI agent you want to copy the reply to.

   Note: The destination AI agent must be on the same channel type (messaging or email) as the source AI agent.
8. In **Destination intent**, select the use case the copied reply should be associated with.

   If you don't see the use case you want, [create it](https://support.zendesk.com/hc/en-us/articles/9041901679130#topic_ik4_12r_mdc) in the destination agent first.
9. In **Destination language for the reply**, select the language the copied reply should be associated with.

   If you don't see the language you want, [add it as a supported language](https://support.zendesk.com/hc/en-us/articles/8357749666714#topic_rmc_kzx_jgc)
   in the destination agent first.
10. Click **Copy**.

    The reply and its associated dialogue are copied to the specified AI agent.

## Deactivating a reply

You can deactivate a reply so that an advanced AI agent no longer uses its associated dialogue in conversations with customers. Neither the reply nor its associated dialogue are deleted, and deactivated replies can be [reactivated](#topic_jyw_4zx_jgc) at any time.

**To deactivate a reply**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Use cases**.
3. Select the use case that contains the reply you want to deactivate.
4. Select the **Replies** tab.
5. Find the reply you want to deactivate, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)), and select **Deactivate**.

## Deleting a reply

If you’re sure you no longer need a reply, you can delete it. Deleting a reply also deletes the dialogue associated with it. This action cannot be undone.

**To delete a reply**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Use cases**.
3. Select the use case that contains the reply you want to delete.
4. Select the **Replies** tab.
5. Find the reply you want to delete, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)), and select **Delete** reply.
6. In the confirmation dialog, click **Delete reply**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_reply_delete_confirm.png)
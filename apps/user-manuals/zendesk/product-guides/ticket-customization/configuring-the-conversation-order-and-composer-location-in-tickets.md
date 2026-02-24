# Configuring the conversation order and composer location in tickets

Source: https://support.zendesk.com/hc/en-us/articles/6070249202202-Configuring-the-conversation-order-and-composer-location-in-tickets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Professional or Enterprise |

Location:  Admin Center > Workspaces > Agent tools > Layouts

Enterprise plans can have multiple layouts active at the same time for
different types of tickets. Professional plans can have only one active layout. See [Plan requirements for custom layouts](https://support.zendesk.com/hc/en-us/articles/5447690090138#topic_bt5_nq1_4bc).

To create the optimal conversation flow for your agents, you can use layout builder
to configure how conversations and the composer appear in a [custom ticket layout](https://support.zendesk.com/hc/en-us/articles/5447690090138) in the agent interface. You must have a
Professional plan or higher with the Zendesk Agent Workspace [activated](https://support.zendesk.com/hc/en-us/articles/4581758611866) to make these changes.

This article includes these sections:

- [About configuring ticket conversations](#topic_spr_n5h_4yb)
- [Changing conversation and composer settings](#topic_x4r_wy3_4yb)

**Related articles**

- [Creating custom layouts to improve agent workflow](https://support.zendesk.com/hc/en-us/articles/5447837546138)
- [Viewing and managing custom layouts](https://support.zendesk.com/hc/en-us/articles/5447837810714)

## About configuring ticket conversations

By default, the ticket interface in the Zendesk Agent Workspace shows the newest
comments at the bottom of the ticket conversation, followed by a composer for entering new
comments. This layout is useful for live conversations such as messaging and chat, but you
might prefer a different layout for your agents, suited to their unique workflows.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/conversation_flow_default_annotated3.png)

When you create a custom layout, you can:

- Change the order of comments that appear in a ticket.
- Change the position of the composer.
- Collapse (or expand) the composer window by default in a ticket.

Because these settings are part of custom ticket layouts, you can configure
different settings for each ticket layout. For example, if you have a layout that’s used
mainly for messaging tickets, you can have the configuration settings that work well for a
typical messaging conversation. If you have a layout that’s used mainly for email tickets,
you can have configuration settings that work well for a typical email conversation.

## Changing conversation and composer settings

The changes you make to a custom layout will apply to all tickets that use the
layout.

**To change the conversation flow**

1. Open a layout for editing. See [Editing a layout](https://support.zendesk.com/hc/en-us/articles/5447837810714-Viewing-and-managing-custom-layouts-EAP-#topic_rsb_zlp_qwb) for details.

   The layout builder
   appears.
2. Click **Customize layout** to make changes to your layout.
3. Select the conversation pane in the ticket layout.

   The conversation settings appear in
   the Customization area of the layout builder.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/custom_layouts_conf_conversations_2.png)
4. Select the **Conversation order**.

   You can choose between **Newest messages at the
   bottom** or **Newest messages at the top**.
5. Select the **Composer position.**

   You can set the composer to appear **Below the
   conversation** or **Above the conversation**.
6. Select a default for collapsing or expanding the composer window:
   - To see more of the conversation when you open a ticket, select **Collapse by
     default**. When selected, the composer window is collapsed by default when agents open tickets.
   - If you want the composer window expanded by default, deselect this option.

   Agents can expand or collapse the composer as needed within each ticket. When an
   agent expands the composer, it includes any [resizing changes](../../agent-guide/ticket-basics/composing-messages-in-the-zendesk-agent-workspace.md#topic_s55_zzg_rmb) the agent made previously.
7. **Save** your layout changes.

   When you create new tickets, you need to submit and
   reopen the ticket before you see the conversation and composer settings
   applied.
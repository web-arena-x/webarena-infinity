# Creating conversation flows in the dialogue builder for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357749494810-Creating-conversation-flows-in-the-dialogue-builder-for-advanced-AI-agents

---

The dialogue builder is where you create conversation flows, or dialogues, for your advanced AI agents. A dialogue is a scripted conversation flow that uses branching logic to determine an advanced AI agent's responses and actions during a conversation with a customer.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

The dialogue builder is where you create conversation flows, or dialogues, for your advanced AI agents. A dialogue is a scripted conversation flow that uses branching logic to determine an advanced AI agent's responses and actions during a conversation with a customer.

Each dialogue is linked to a specific [reply](https://support.zendesk.com/hc/en-us/articles/9624068102682), and each reply is in turn linked to a [use case](https://support.zendesk.com/hc/en-us/articles/9041901679130).

This article contains the following topics:

- [Creating a new dialogue](#topic_ygq_4ym_g2c)
- [Available block types](#topic_krz_vym_g2c)

Related articles:

- [Managing conversation flows in the dialogue builder for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/9066753203738)
- [Best practices for conversation design for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357751731610)

## Creating a new dialogue

In the dialogue builder, you can create a dialogue that contains the conversation flow your AI agent should follow when interacting with a customer.

**To create a dialogue**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Use cases**.
3. Select the use case you want to create a dialogue for.
4. Select the **Replies** tab.
5. Click **Add reply**.

   The dialogue builder opens.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_agents_dialogue_builder_example.png)

   To move around within the dialogue builder, click and drag an empty area. To zoom in and out, use the plus (+) and minus (-) icons in the top-right corner, or press CTRL and scroll the mouse wheel.
6. In the **AI agent message** block that is always populated at the start of a new dialogue, enter the text that your AI agent should greet a customer with.
7. To add additional message blocks, click the plus (+) icon.

   You can add them before or after the initial AI agent message block, or anywhere else the plus icon (+) appears. To learn more about the available message blocks, see [Available block types](#topic_krz_vym_g2c).
8. To manage an added block, hover your mouse over the block, select the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)), and select one of the following options:
   - **Collapse branch**: Collapses the branch starting with the selected block to make the overall dialogue easier to see.
   - **Move**: Allows you to select another block to move the selected block underneath.
   - **Copy**: Copies the selected block and the branch it begins, if applicable.
   - **Paste block**: Pastes a copied block underneath the selected block.
   - **Paste branch**: Pastes a copied branch underneath the selected block.
   - **Actions**: Allows you to copy, paste, or remove an action associated with the selected block. See [Creating and adding actions for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756623770#h_01JFDGYY1WPV42FCQ7KS3XAPVS) for more information about actions at the block level.
   - **Delete**: Allows you to delete the selected block or the branch starting with the selected block.
9. To link a block to another block, click the link icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_link.png)) underneath a block and then select the block you want the first block to link to.

   Note: A customer message block can’t be linked to another customer message block.
10. To validate that all blocks are correctly configured, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_edit_menu_icon_vertical.png)) and select **Validate dialogue**.
11. To [test the dialogue](https://support.zendesk.com/hc/en-us/articles/8357758879130) without affecting the live AI agent, do either of the following:
    - Test the entire dialogue by clicking **Test dialogue** in the upper-right.
    - Test a specific branch of the dialogue by hovering over the block you want to start from and clicking the icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_dialogue_builder_test_branch_icon.png)).
12. To save your progress without affecting the live AI agent, click either of the following:
    - **Save**: Saves your changes.
    - **Save with note**: Saves your changes and allows you to include a note about what you changed. This information can be viewed in the [Version history](https://support.zendesk.com/hc/en-us/articles/9066753203738#topic_tyw_5zt_z2c) pane. No logic check is performed when saving as a draft. If multiple people are working on the same dialogue at the same time, the person who saves last overwrites everything.
13. To make your changes live to customers interacting with the AI agent, click either of the following:
    - **Publish**: Publishes your changes.
    - **Publish with note**: Publishes your changes and allows you to include a note about what you changed. This information can be viewed in the [Version history](https://support.zendesk.com/hc/en-us/articles/9066753203738#topic_tyw_5zt_z2c) pane.

      A logic check happens at this time. If you can't publish, fix any errors highlighted in red.

Note: In the [Version history](https://support.zendesk.com/hc/en-us/articles/9066753203738#topic_tyw_5zt_z2c) pane, you can add, edit, or delete the notes a customer entered when they saved or published a version of the dialogue.

## Available block types

Block types define where a customer goes next within the conversation flow, including what information is asked for and expected.

| | |
| --- | --- |
| **Block type** | **Description** |
| AI agent message | This is a scripted message that the AI agent should say. If you’ve [activated rich messaging](https://support.zendesk.com/hc/en-us/articles/10050437105946#topic_yf3_1gk_jhc), this block type supports HTML and Markdown formatting. |
| Customer message | This is where you define how the customer might respond to an AI agent and how the dialogue should progress based on that response. Cannot be the first block in a dialogue. For more information, see [Using the Customer message block in conversation flows for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/9060613203610). Note: It's not possible to have two consecutive customer messages. |
| Generative replies | This is an AI-generated response to a customer's message. For more information, see [About the Generative replies block in conversation flows for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749315098). |
| Conditional | This is a way to personalize responses in a dialogue based on certain conditions, including parameters and segments. For more information, see [About conditional blocks in conversation flows for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357733406234). |
| API integration | This is a way to connect to business-specific services to retrieve information that can be used during the conversation (for example, retrieving order status information from a logistics provider). Available only if you have [integrations implemented](https://support.zendesk.com/hc/en-us/sections/8264334170906). |
| Carousel | This is a rich messaging type for displaying up to 10 different options with a visual card element. Available only for certain CRMs and channels. Not available for email AI agents. For more information, see [Adding carousels in conversation flows for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749513370). |
| Link to | This is a way to pass customers between dialogues. Must be the last block in a branch. Cannot be the first block in a dialogue. For example, you can create one escalation flow and link to it from other dialogues instead of creating an escalation flow as part of each individual dialogue. From this block, you can select the reply (dialogue) you want to link to. In the first field, select the [use case](https://support.zendesk.com/hc/en-us/articles/9041901679130) or [template](https://support.zendesk.com/hc/en-us/articles/8357756562330) you want to link to. In the second field, select the specific reply you want to link to within the use case or template. For advanced messaging AI agents, you can select the “Auto-select reply method” value in the second field. The effect that this value has depends on the type of AI agent:   - For [agentic AI   agents](https://support.zendesk.com/hc/en-us/articles/8966284087066), this value checks the [Reply method](https://support.zendesk.com/hc/en-us/articles/9041911005850#topic_elk_mcf_52c)   setting for the selected use case and, if that setting   is set to:   - Use a procedure, this value     automatically selects the generative procedure     linked to the use case.   - Use a dialogue, this value     automatically selects the active dialogue for that     use case in the relevant language of the     conversation. - For AI agents without agentic AI, this value   automatically selects the active dialogue for that use   case in the relevant language of the conversation.   Actions that link to another flow do not increase the [automated resolution count](https://support.zendesk.com/hc/en-us/articles/5352026794010#topic_m1n_sq4_jwb). |
| Availability | This is a way to respect your business's operating hours during a conversation to manage customer expectations and check for agent availability before escalating. Not available for email AI agents. For more information, see [Setting operating hours for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749686554). |
| Escalation | This is how you define the escalation path to a human agent, including the message the AI agent sends to the customer and whether the escalation uses the messaging or email channel. Must be the last block in a branch. For more information, see [About escalation strategies and flows for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357756604186). |
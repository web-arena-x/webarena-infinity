# Using instructions to influence advanced AI agent responses

Source: https://support.zendesk.com/hc/en-us/articles/8357749291290-Using-instructions-to-influence-advanced-AI-agent-responses

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Note: For equivalent functionality for AI agents - Essential, see
[Using instructions to influence AI agent
responses](https://support.zendesk.com/hc/en-us/articles/9203004883994).

You can create instructions for your AI agents that let you control their behavior in
ways beyond [customizing their persona, tone of voice, and pronoun
formality](https://support.zendesk.com/hc/en-us/articles/8357758773658). Instructions let you balance generative AI's automation potential
to solve more customer requests without requiring human intervention, while preserving a
precise level of control that helps you protect your brand.

This article contains the following topics:

- [About instructions](#topic_qrh_krf_52c)
- [Creating instructions](#topic_ccv_krf_52c)
- [Testing instructions](#topic_qrg_lrf_52c)
- [Editing instructions](#topic_p35_lrf_52c)
- [Deleting instructions](#topic_zlh_mrf_52c)

Related article:

- [Best practices for using instructions and custom
  tone of voice to influence advanced AI agent responses](https://support.zendesk.com/hc/en-us/articles/8719119396506)

## About instructions

Instructions let you customize your AI agents’ responses beyond tone of voice,
response lengths, and pronoun formality. For example, you can create instructions
that tell your AI agents to:

- Follow an in-house style guide that includes specific terminology or formatting.
- Avoid specific phrases or responses that shouldn’t be used with customers (for
  example, “According to the sources” or “Contact customer support”).
- Respond in specified ways to particular user messages (for example, to always
  include a specific hyperlink in responses about a given topic).

Instructions are configured at the AI agent–level.

### Limitations of instructions

Instructions allow you to refine an AI agent's responses beyond just tone of
voice. They can enforce specific language, avoid certain phrases, or ensure key
information is included in replies.

What instructions can’t do, however, is fundamentally change the content returned
by the AI agent. For example, instructions cannot be used to search a different
knowledge source or to cause an escalation.

Instructions are applied after the AI agent has understood the end user’s
message, queried a knowledge source accordingly, and generated an answer ready
to be sent back to the end user. At this point in the process, instructions can
be used to shape—but not fundamentally change—the way that answer is presented
to the end user.

Additionally, instructions have a specific limitation when it comes to links and
other content that appears in the source but was not directly used to generate a
factual answer. As a result, instructions similar to the following won’t work:
"When the article includes a product link, always include it in your response."
The process that interprets instructions has no visibility into the content of
the article that contains the link, so it either does nothing or risks
hallucinating a non-existent link.

## Creating instructions

For each AI agent, you can create up to 40 instructions that influence its responses
to customers.

**To create an instruction**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to
   work with.
2. Click **Content** in the sidebar, then select **Personalization**.
3. Select the **Instructions** tab.
4. Click **Create instruction**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_instructions_add_button.png)
5. In **Name**, enter a descriptive name for the instruction.

   The name is
   shown to admins on the Instructions settings page and is never shown to
   customers nor sent to the AI agent.
6. In **How would you like the AI agent to respond?**, enter a description
   of how the AI agent should respond to the customer.

   For example, “Always
   use the term Acme Labs™ instead of Acme.”
7. In **Status**, select either of the following options:
   - **Inactive**: (Default) The AI agent won’t follow the instruction
     in real situations with customers, but you can still test it behind
     the scenes.
   - **Active**: The AI agent immediately starts following the
     instruction. In production environments, it’s not recommended to set
     an instruction to Active until after you’ve tested it.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_instructions_add_window.png)
8. Click **Create**.

## Testing instructions

Before setting any instructions to active, it’s highly recommended to test them
thoroughly to help ensure that they affect the AI agent’s responses as you expect.

On the Instructions page, you can test instructions individually or in bulk. How and
where you conduct the testing affects what information the system evaluates as part
of the test:

- **When you test an individual instruction** using the in-line Test button,
  the system evaluates that instruction *plus* any currently active
  instructions. It does not evaluate any other inactive instructions.
- **When you test multiple instructions in bulk**, the system evaluates
  *only* the instructions you’ve selected. Any other non-selected
  instructions, regardless of their active/inactive status, are not evaluated.

Tip: From any page in AI agents - Advanced, you
can also use the Test AI agent button at the top to simulate the current
customer experience. This type of testing evaluates all currently active
settings, including instructions. See [Testing conversation flows in advanced AI
agents](https://support.zendesk.com/hc/en-us/articles/8357758879130).

**To test an individual instruction**

1. [On the Instructions
   page](#topic_ccv_krf_52c), click the instruction you want to edit.
2. Click **Test** to open a test window on the right, where you can get an
   idea of how the instruction affects the AI agent’s responses.

   During this
   testing, the system evaluates this instruction *plus* any currently
   active instructions. Any other inactive instructions are
   ignored.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_instructions_test_individual.png)

   Tip: If you want to test a single instruction and ignore all other
   instructions, regardless of their status, you can use the bulk testing
   method (described next) and select only a single instruction for
   testing.

**To test multiple instructions together**

1. [On the Instructions
   page](#topic_ccv_krf_52c), select the checkboxes to the left of the instructions you
   want to test.
2. In the menu that appears at the bottom of the screen, click the options menu
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) and select **Test
   selected**.

   A test window opens on the right, where you can get an
   idea of how these instructions affect the AI agent’s responses. During
   this testing, the system evaluates *only* the instructions you
   selected. All other non-selected instructions are ignored, even if
   they’re active.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_instructions_test_multiple.png)

## Editing instructions

You can edit an instruction, even if it’s active, and test the edits without
affecting the customer experience.

**To edit an instruction**

1. [On the Instructions
   page](#topic_ccv_krf_52c), click the instruction you want to edit.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_instructions_edit.png)
2. Update the instruction’s details as needed.

   For help, see [Creating instructions](#topic_ccv_krf_52c).
3. Click **Test** to open a test window on the right, where you can get an
   idea of how these edits affect the AI agent’s responses before
   proceeding.

   During this testing, the system evaluates this instruction
   *plus* any currently active instructions.
4. Click **Save changes**.
5. If the instruction is currently active, click **Proceed** in the **Save
   instruction** window to confirm that you want to overwrite the
   previous version of the instruction with this new version.

   Any changes to
   an active instruction will immediately affect the AI agent’s
   interactions with customers.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_instructions_save_live.png)

## Deleting instructions

You can delete instructions you no longer need, either one at a time or in bulk.

Deleting an instruction is permanent and cannot be undone. When an instruction is
deleted, the AI agent immediately stops following that instruction.

**To delete an individual instruction**

1. [On the Instructions
   page](#topic_ccv_krf_52c), find the instruction you want to delete.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) and select
   **Delete**.

**To delete multiple instructions**

1. [On the Instructions
   page](#topic_ccv_krf_52c), select the checkboxes to the left of the instructions you
   want to delete.
2. In the menu that appears at the bottom of the screen, click the options menu
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) and select **Delete
   instructions**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_instructions_delete_multiple.png)
3. In the **Delete instructions** window that appears, click
   **Delete**.
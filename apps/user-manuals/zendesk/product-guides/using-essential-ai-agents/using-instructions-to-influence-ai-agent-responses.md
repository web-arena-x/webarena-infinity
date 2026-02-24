# Using instructions to influence AI agent responses

Source: https://support.zendesk.com/hc/en-us/articles/9203004883994-Using-instructions-to-influence-AI-agent-responses

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

For equivalent functionality for [AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/8725042447002), see [Using instructions to influence advanced AI agent
responses](https://support.zendesk.com/hc/en-us/articles/8357749291290).

You can create instructions for your AI agents that let you control their behavior in
ways beyond customizing their [default persona options](https://support.zendesk.com/hc/en-us/articles/8753435048474). Instructions let you balance
generative AI's automation potential to solve more customer requests without requiring
human intervention, while preserving a precise level of control that helps you protect
your brand.

This article contains the following topics:

- [About instructions](#topic_ifs_wcj_4fc)
- [Creating instructions](#topic_rn1_ycj_4fc)
- [Viewing all instructions](#topic_vqt_zcj_4fc)
- [Testing instructions](#topic_snd_bdj_4fc)
- [Activating and deactivating instructions](#topic_nnx_w2j_4fc)
- [Editing instructions](#topic_ddz_cdj_4fc)
- [Deleting instructions](#topic_fkf_2dj_4fc)

Related articles:

- [Best practices for using instructions to
  influence AI agent responses](https://support.zendesk.com/hc/en-us/articles/9309367377050)

## About instructions

Instructions let you customize your AI agents’ responses beyond their [persona](https://support.zendesk.com/hc/en-us/articles/8753435048474) (which includes your business profile, tone of
voice, and reply length). For example, you can create instructions that tell your AI
agents to:

- Follow an in-house style guide that includes specific terminology or formatting.
- Avoid specific phrases or responses that shouldn’t be used with customers (for
  example, “According to the sources” or “Contact customer support”).
- Respond in specified ways to particular user messages (for example, to always
  include a specific hyperlink in responses about a given topic).

Instructions are configured at the AI agent–level.

## Creating instructions

For each AI agent, you can create up to 40 instructions that influence its responses
to customers. However, it’s recommended to keep the number of instructions low. The
fewer active instructions there are, the more likely the AI agent is to follow any
given instruction.

Instructions should always be created in English, regardless of any other AI agent
language settings.

Tip: See [Best practices for using instructions to
influence AI agent responses](https://support.zendesk.com/hc/en-us/articles/9309367377050).

**To create an instruction**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the AI agent you want to create instructions for.
3. Click the **Instructions** tab.
4. Click **Create instruction**.

   The Create instruction page
   opens.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_instructions_create.png)
5. In **Name**, enter a descriptive name for the instruction.

   The name is
   shown to admins on the Instructions settings page and is never shown to
   customers nor sent to the AI agent.
6. In **Instruction**, enter a description of how the AI agent should
   respond to the customer.

   For example, “Always use the term Acme Labs™
   instead of Acme.”
7. In **Channel type**, select whether the instruction should apply to
   **Messaging** channels, **Email** channels, or both types.
8. Click **Save**.
9. Click **Test instruction** to see how the instruction influences your AI
   agent’s responses.

   When you test an instruction this way, it’s tested
   alongside any other instructions that are either Active or To be
   activated.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_instructions_testing.png)

   Note: For other testing options, see [Testing instructions](#topic_snd_bdj_4fc).
10. Make changes as needed, then click **Save**.

Note: You must [activate the instruction](#topic_nnx_w2j_4fc) before it has any effect on your live AI
agent.

## Viewing all instructions

Within an AI agent, you can see all the instructions that have been created for it on
the Instructions tab.

**To view all instructions**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the AI agent you want to see instructions for.
3. Click the **Instructions** tab.

   On this page, you can see all the
   instructions you’ve created, including the following details:

   - **Status**: Which of the following statuses the instruction is in:
     - **Active**: The instruction is live and influences the AI
       agent’s responses to end users.
     - **To be activated**: The instruction is not currently live,
       but will be activated the next time the AI agent itself is
       published.
     - **Inactive**: The instruction is not live and doesn’t
       influence the AI agent’s responses to end users.
     - **To be deactivated**: The instruction is currently live, but
       will be deactivated the next time the AI agent itself is
       published.
   - **Channel type**: Whether the instruction applies to messaging
     channels, email channels, or both types.
   - **Updated**: When the instruction was last updated.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiae_instructions_viewing.png)

## Testing instructions

Before [activating any
instructions](#topic_nnx_w2j_4fc), it’s highly recommended to test them thoroughly to help
ensure that they affect the AI agent’s responses as you expect. Where you conduct
the testing affects what information the system evaluates as part of the test:

- **When you use the Test instruction button** (either when [editing](#topic_ddz_cdj_4fc) or [creating](#topic_rn1_ycj_4fc) an instruction), the
  system evaluates that instruction plus any currently Active or To be activated
  instructions.
- **When you use the Test AI agent button** in the AI agent settings, the
  system evaluates all Active and To be activated instructions. See [Testing an AI agent](https://support.zendesk.com/hc/en-us/articles/4408835784602#topic_ob1_lxx_r5b).

When [creating](#topic_rn1_ycj_4fc) or [editing](#topic_ddz_cdj_4fc) an instruction, make sure
you save the instruction before testing it.

**To test an instruction**

1. [On the Instructions
   tab](#topic_vqt_zcj_4fc), click the instruction you want to test.
2. Click **Test instruction**.
3. Use the test pane to test the instructions' influence on your AI agent's
   responses.

## Activating and deactivating instructions

After you [create an instruction](#topic_rn1_ycj_4fc),
you must activate it before it has any effect on your AI agent’s responses in
conversations with end users. Similarly, if you no longer want an instruction to
influence your AI agent, but you don’t want to [delete the instruction](#topic_fkf_2dj_4fc) completely, you can deactivate
it.

If needed, you can also cancel the pending activation or deactivation of an
instruction.

**To activate or deactivate an instruction**

1. [On the Instructions tab](#topic_vqt_zcj_4fc),
   hover over the instruction you want to activate or deactivate.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)) and select one of the following options:
   - **Activate**: The instruction is set to To be activated, and will be
     set to Active the next time you publish the AI agent unless you cancel
     the activation.
   - **Deactivate**: The instruction is set to To be deactivated, and will
     be set to Inactive the next time you publish the AI agent unless you
     cancel the deactivation.
3. [Publish the AI agent](https://support.zendesk.com/hc/en-us/articles/7232810932250) to apply your
   changes.

**To cancel a pending activation or deactivation**

1. [On the Instructions
   tab](#topic_vqt_zcj_4fc), hover over the instruction you want to cancel a pending
   activation or deactivation for.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)) and select one of the following options:
   - **Cancel activation**: The instruction is set to Inactive.
   - **Cancel deactivation**: The instruction is set to Active.

## Editing instructions

You can edit an instruction, even if it’s active, and test the edits without
affecting the customer experience.

**To edit an instruction**

1. [On the Instructions tab](#topic_vqt_zcj_4fc),
   click the instruction you want to edit.
2. Update the instruction’s details as needed and test the results.

   For help, see
   [Creating instructions](#topic_rn1_ycj_4fc) and [Testing instructions](#topic_snd_bdj_4fc).
3. Click **Save**.

   You’re returned to the Instructions tab, where the
   instruction’s status has changed to To be activated.
4. [Activate the
   instruction](#topic_nnx_w2j_4fc).

## Deleting instructions

You can delete instructions you no longer need. Only inactive instructions can be
deleted, so make sure you first [deactivate the instruction](#topic_nnx_w2j_4fc) you want to delete.

Deleting an instruction is permanent and cannot be undone. When an instruction is
deleted, the AI agent immediately stops following that instruction.

**To delete an instruction**

1. [On the Instructions tab](#topic_vqt_zcj_4fc),
   find the inactive instruction you want to delete.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)) and select **Delete**.
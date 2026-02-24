# Creating answers for common customer questions in AI agents for messaging (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/4422584657434-Creating-answers-for-common-customer-questions-in-AI-agents-for-messaging-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

This article describes
functionality available only to customers who had a drafted or published AI agent as
of February 2, 2025. For information about equivalent functionality in the [AI agents - Advanced add-on](https://support.zendesk.com/hc/en-us/articles/6970583409690), see [Building dialogues for AI agents - Advanced](https://support.zendesk.com/hc/en-us/sections/8264324615322).

If
you’ve [created](https://support.zendesk.com/hc/en-us/articles/4408824263578) and [set the standard responses](https://support.zendesk.com/hc/en-us/articles/7510607688730) for an AI agent for messaging,
you can create answers to define its behavior.

Answers tell an AI agent how to respond to customer questions. Each answer addresses a single
question your customers might ask. Answers are comprised of steps that determine how the
AI agent responds to customer input.

Note: Answers are no longer the recommended way to define how an
AI agent responds to a customer's question. Instead, you should [use generative replies](https://support.zendesk.com/hc/en-us/articles/6138268212634), which use your own trusted help
center content to deliver concise, AI-generated replies directly within a
conversation, all without requiring you to create or maintain answer flows.

This article contains the following sections:

- [Creating an answer](#topic_nm5_w5f_wbc)
- [Adding and removing steps in an
  answer](#topic_k3y_x5f_wbc)

## Creating an answer

You can build your own answer from scratch or use a pre-built answer template:

- [Creating your own
  answer](#topic_nm5_w5f_wbc)
- [Creating an
  answer from a template](#topic_nm5_w5f_wbc__ul_yhq_1rm_wbc)

### Creating your own answer

You can build an answer from scratch, starting with an empty answer flow. Answers
are comprised of steps that determine how the AI agent responds to customer
input. An answer can have multiple steps or a single step, but each answer must
have at least one step. When the AI agent matches a customer’s query to an
answer, the AI agent displays the behavior defined by the steps in the
answer.

An AI agent for messaging can include up to 2,000 steps and 500 answers.

**To create an answer for your AI agent**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the name of the AI agent you want to edit.
3. Click the **Answers tab**, then click **Create answer**.
4. Click **Build your own answer**, then click **Next**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bot_template_BYOA.png)
5. Enter the **Answer name**, then click **Next**.

   The name should be a brief, clear description of the issue addressed by the answer. For example, “Password reset,” “Request a refund,” or “Talk to a human."
6. Enter **Training phrases** in the available fields, then click **Add phrase** if you need
   to add more.

   Training phrases teach the AI agent how to interpret questions so it
   can match the most relevant answer. You can add up to 100 additional phrases.
   See [best practices for training phrases](https://support.zendesk.com/hc/en-us/articles/4965031536794#topic_lxh_cpq_tbc).

   Alternatively, if you have an intent model assigned to your account, you
   might see up to three AI-powered suggested intents to use instead of training
   phrases. You can select one or more intents. If none of the intents work, click
   **Train the AI agent yourself** to add training phrases.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/create_answer_pre-trained_intents.png)
7. Click **Next**.

   The answer opens in bot builder where you can build out the AI agent’s
   response.
8. Click **Add step** to create the first step in the answer.

   Each answer needs at least one
   step only.
9. Under **Choose step** in the configuration panel, select a step type, then enter options to
   **Configure** the step.

   For information on the available step types, see
   [Understanding answer step types](https://support.zendesk.com/hc/en-us/articles/4408836323738). Click
   **Preview** to view the step as a user.
10. Add additional steps to the answer as needed.

    For more information, see [Adding and removing steps in an
    answer](https://support.zendesk.com/hc/en-us/articles/4422584657434#topic_k3y_x5f_wbc).
11. Click **Done** when you’re finished.

    The answer appears as Ready to publish status.

At this point, you can click **Create answer** to create another answer or you
can click **Publish AI agent** to make your new answer available in the AI
agent. Before new or edited answers are available to customers, you must publish
the AI agent they’re attached to. When you publish the AI agent, all answers in
the Ready to publish state are published.

### Creating an answer from a template

You can choose from a number of templates to use as a starting point for an
answer. These templates provide examples of common answer topics and
construction. While each template has a complete answer framework, most will
require you to add information before you publish.

**To create an answer from a template**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the name of the AI agent you want to edit.
3. Click the **Answers tab**, then click **Create answer**.
4. Click the answer template you want to use, then click **Next**.

   The
   answer opens in bot builder.
5. Update the **Name** and **Training phrases** for the answer, if
   you'd like.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/intent_name_panel.png)
6. Click each step in the answer and make changes as needed.

   It's a good
   idea to check each step in the answer to make sure it is complete
   and has been personalized for your business.
7. Click **Done** when you are finished.

   Or, if you are just viewing
   the answer structure without making any changes, you can click your
   browser's **Back** button to return to the Create answer
   page.

At this point, you can click **Create answer** to create another answer or you
can click **Publish AI agent** to make your new answer available in the AI
agent. Before new or edited answers are available to customers, you must publish
the AI agent they’re attached to. When you publish the AI agent, all answers in
the Ready to publish state are published.

## Adding and removing steps in an answer

When using bot builder to create an answer, you might do any of the following to
build your answer:

- [Insert new steps in
  answer](#topic_l32_tf2_k1c)
- [Copy and paste steps in an
  answer](#topic_fm5_pf2_k1c)
- [Checking answer step usage and limit](#topic_vjg_dwh_22c)
- [Remove steps from an
  answer](#topic_gyq_5f2_k1c)

### Inserting new steps to an answer

In addition to copying and pasting steps into an answer, you can also insert a
step between two existing steps in an answer.

When you add a branching step, such as a **Present options** or **Add
business hours conditions** step, the subsequent, pre-existing steps will
be included under the new step's initial branch.

- **Present options**: Existing steps are included under *Option
  1*.
- **Add business hours conditions**: Existing steps are included under
  the *When open*branch.

You can't add the **Transfer to agent** step to an answer before another step.
It can be the final step in an answer only.

**To add a step into an answer**

1. Open an [answer for editing](https://support.zendesk.com/hc/en-us/articles/7510276767386#topic_msl_4f2_k1c).
2. In bot builder, hover over the line connecting two steps and click the
   **Add new** icon ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add_step_icon_flowb.png)).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add_message_step_middle.png)
3. In the Configuration panel, select the message type to insert into the
   answer and configure the step as needed.
4. Repeat as needed, then click **Done** when you're ready.

Remember to [publish the AI agent](https://support.zendesk.com/hc/en-us/articles/7232810932250) to make the
updated answer available.

### Copying and pasting steps in an answer

You can copy one or more consecutive steps and use them elsewhere
within the same answer. You can't copy a step from one answer to another answer.
You can paste copied steps only at the end of a branch in the answer, and that
branch can't currently end with a Transfer to agent step.

**To copy a step (or multiple steps) and paste it elsewhere in an answer**

1. Open an [answer for editing](https://support.zendesk.com/hc/en-us/articles/7510276767386#topic_msl_4f2_k1c).
2. Click the step you want to copy.
3. In the configuration panel, click the **Options** ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_flowbuilder.png)) menu, then select an option:

   - Select **Copy this step** to copy only the selected
     step
   - Select **Copy this and following steps** to copy the
     selected step and all subsequent steps

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copy_menu_flowbuilder.png)
4. Click the **Add new** icon ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add_step_icon_flowb.png)) or the **Add a step** icon (
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add_step_icon_flowb.png)) at the end of the branch.
5. Click the **Options** ( ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_flowbuilder.png)) menu again, then select
   **Paste step**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/paste_flowbuilder.png)
6. Click **Done** when you're finished.

Remember to [publish the AI agent](https://support.zendesk.com/hc/en-us/articles/7232810932250) to make the
updated answer available.

### Checking answer step usage and limit

You can use a maximum of 2000 steps across all of your answers. You can check how
many steps you're using by opening any answer and clicking the information icon
in the answer's mini-map.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/minimap_tick.png)

### Removing steps from an answer

Deleting a step removes all subsequent steps from the answer. If you want to
delete a step but retain the subsequent steps, you can copy and paste the
subsequent steps later in the answer.

**To delete a step in an answer**

1. Open an [answer for editing](https://support.zendesk.com/hc/en-us/articles/7510276767386#topic_msl_4f2_k1c).
2. In the configuration panel, click the **Options** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options_flowbuilder.png)) menu.
3. Select **Delete this step** or **Delete this and following
   steps**. If there are subsequent steps, click **Delete steps** in
   the warning box.
4. Click **Done** when you've finished making your changes.

Remember to [publish the AI agent](https://support.zendesk.com/hc/en-us/articles/7232810932250) to make the
updated answer available.
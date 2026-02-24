# Creating generative procedures for AI agents with agentic AI

Source: https://support.zendesk.com/hc/en-us/articles/8979864563610-Creating-generative-procedures-for-AI-agents-with-agentic-AI

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Generative procedures are AI-generated procedures that help power the
decision-making
capabilities of
[AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/8966284087066).
Instead of
[building scripted conversation flows in the dialogue
builder](https://support.zendesk.com/hc/en-us/articles/8357749494810),
you can simply enter your business policies and let the AI agent
generate a procedure to map out the best path to resolution.

This article contains the following topics:

- [About generative procedures](#topic_pgh_rs2_52c)
- [Creating generative procedures](#topic_ult_rs2_52c)

Related articles:

- [Best practices for creating generative procedures
  for AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/9424547622298)
- [Examples of generative procedures for AI agents
  with agentic AI](https://support.zendesk.com/hc/en-us/articles/9424547984026)
- [Managing generative procedures for AI agents with
  agentic AI](https://support.zendesk.com/hc/en-us/articles/10040865503898)

## About generative procedures

By leveraging agentic AI, generative procedures give AI agents the
freedom to
determine the best way to resolve a customer’s issue in line with
your business
policies. Generative procedures require less setup and maintenance
from you than
scripted dialogues do.

Each generative procedure is tied to a specific
[use case](https://support.zendesk.com/hc/en-us/articles/9041901679130).
When that use case is triggered during a
conversation with a user, the AI agent follows the associated procedure
to resolve
the issue.

Also, generative procedures power multilingual AI agents. You can
write a procedure
once, in a single language, and it can serve all the languages your
AI agent
supports.

## Creating generative procedures

Client admins and client editors can create a generative procedure
from within a use
case.

For helpful advice, see
[Best practices for creating generative procedures for AI agents
with agentic AI](https://support.zendesk.com/hc/en-us/articles/9424547622298).

Note: Generative procedures don’t
currently support rich-text
formatting, such as buttons or carousels.

**To create a generative procedure**

1. In
   [AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/8357756913178),
   use the AI
   agent drop-down field to select the AI agent you want to
   create a generative
   procedure for.
2. In the sidebar, click **Content**
   and select **Use cases**.
3. Click the use case you want to create a procedure for.
4. Under **Reply method**, make sure
   **Use procedure when use case is
   triggered**
   is selected.

   Tip: For
   more information about this setting, see
   [Configure whether a use case uses a
   dialogue or generative procedure](https://support.zendesk.com/hc/en-us/articles/9041911005850#topic_elk_mcf_52c).
5. On the **Procedure** tab, click
   **Create procedure**.
6. On the **Create procedure** screen,
   enter a free-text description of how
   the AI agent should solve a customer’s issue when this use
   case is
   triggered.

   Within a procedure description, you can:

   - List the steps required to solve this task as you
     would with a human
     agent. For best results, list them in a logical,
     sequential
     order.
   - Instruct the AI agent to search a knowledge source
     to answer the
     user’s question. For example, “Search in the help
     center for…” You
     can even use natural language to reference specific
     search rules
     (for example, “Search only in the English help center”).
   - Add instructions on how to phrase an answer (for
     example, “Always
     include {{brandName}}”).
   - Type a forward slash (/) or click the plus icon (+)
     to insert
     [actions](https://support.zendesk.com/hc/en-us/articles/8357756651290),
     [API integrations](https://support.zendesk.com/hc/en-us/articles/8357756844442),
     [parameters](https://support.zendesk.com/hc/en-us/articles/8920235767834),
     [search rules](https://support.zendesk.com/hc/en-us/articles/9185497386394), or links to other procedures or dialogues.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_create_procedure_field_updated.png)
7. Click **Generate procedure**.

   On the left, the procedure builder
   summarizes the procedure it generated, allowing you to
   read through the
   logic in a human-friendly way.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_generative_procedures_summarize_update.png)

   On the right, an
   AI-generated procedure map appears, showing you exactly
   what logic the
   AI agent will follow and what steps it will take during
   a conversation
   to solve a customer’s issue for this use case.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_gen_procedure_map_example_updated.png)
8. If necessary, make adjustments to the procedure using the
   free-text field at
   the bottom and click **Update procedure**.

   Make adjustments by
   instructing the procedure builder to add, change, or
   delete parts of the
   current version of the procedure. Don’t rewrite the whole
   procedure in
   your adjustment.

   For example, you might instruct the AI agent to:

   - Add a step at a certain point in the current procedure.
   - Change the content of a specific node in the procedure
     map.
   - Adjust content throughout the entire procedure, such
     as changing
     {{phone}} with {{telephone}}.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_generative_procedure_update.png)

   After each adjustment you
   submit, the procedure builder sends a reply summarizing
   the changes it
   made to the procedure, and the procedure map is updated
   with your
   adjustments. You cannot edit your previous entries or
   the procedure map
   directly.

   Repeat as necessary until the procedure map looks the
   way you expect.

   Tip: If you want to
   start your procedure from scratch, click the
   **Start over** icon
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_start_over_icon.png))
   in the upper right. Your changes are
   still saved to the
   [procedure’s version
   history](https://support.zendesk.com/hc/en-us/articles/8979864563610#topic_b2h_5cc_tgc).
9. Click **Publish procedure** in
   the upper right.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_publish_procedure.png)

After you create a procedure, you can
[manage it](https://support.zendesk.com/hc/en-us/articles/10040865503898)
at any time, including editing,
testing, and restoring previous versions.
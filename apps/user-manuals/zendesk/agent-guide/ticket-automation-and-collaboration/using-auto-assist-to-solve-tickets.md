# Using auto assist to solve tickets 

Source: https://support.zendesk.com/hc/en-us/articles/7051314237466-Using-auto-assist-to-solve-tickets

---

Auto assist is an AI-powered assistant that helps you solve tickets faster. Using a large language model (LLM), auto assist understands the contents of submitted tickets and makes suggestions on how to solve them.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Copilot |

Verified AI summary ◀▼

Auto assist is an AI-powered tool that helps you resolve tickets faster by suggesting replies, actions, or macros. You review and approve these suggestions, ensuring control over responses. It also provides admin-written instructions for ticket resolution. You can edit suggestions or take over manually if needed. Auto assist streamlines repetitive tasks, promoting consistent ticket handling and quicker resolutions.

Auto assist is an AI-powered assistant that helps you solve tickets faster. Using a large
language model (LLM), auto assist understands the contents of submitted tickets and
makes suggestions on how to solve them.

When you’re working on tickets in the Agent Workspace, suggestions made by auto assist
appear in the place where the composer would otherwise exist. These suggestions can be
replies that you can send to the customer, other actions that auto assist can execute
for you, or macros that you might already use regularly. However, you’re always in
control—you must accept a suggestion before a response is sent, an action is taken, or a
macro is applied.

Auto assist may also provide instructions written by your admin that are relevant to your
conversation. These instructions are steps you should follow to solve the ticket.

With auto assist, you spend less time on repetitive tickets, solve tickets in a more
consistent way, and ultimately close more tickets.

This article contains the following topics:

- [Reviewing and editing an auto assist suggestion](#topic_q1m_bth_4cc)
- [Following instructions provided by
  auto assist](#topic_lzb_nj3_5fc)t
- [Taking over from auto assist suggestions](#topic_qzh_cth_4cc)

Related articles:

- [Turning on and configuring auto
  assist](https://support.zendesk.com/hc/en-us/articles/8013454025114)
- [Using formatting options and controls in the
  Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408844184730)

## Reviewing and editing an auto assist suggestion

You must always review and approve the replies, actions, or macros suggested by auto
assist. Depending on how your admin has configured your account, auto assist adapts
its suggested text responses to match the [tone and writing style](https://support.zendesk.com/hc/en-us/articles/8761641980698#topic_eck_hmp_22c) of your
conversation with an end user.

You can edit the wording and formatting before sending a suggested reply. Suggested
actions can be removed, or you can [take over the ticket](#topic_qzh_cth_4cc) to perform a different one. New auto assist
suggestions may appear when you're editing a suggested reply and the ticket is
updated in any way. For example, if the end user sends another reply.

You can also edit the wording, formatting, and remove all actions from a suggested
macro before approving and applying it. Keep in mind that the auto assist composer
doesn't support internal notes or attachments but suggested macros may contain
these. If you approve a suggested macro with an attachment it'll be sent to the end
user but you won't be able to preview it.

**To review and edit an auto assist suggestion**

1. In the Agent Workspace, open a ticket.
2. In the ticket, review the suggestion in the **Auto assist** panel.
   Depending on the suggestion, you can do the following:

   Tip: Hover your mouse over the info
   icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/info_icon.png)) to see why auto assist generated the
   suggestion. If you have permission, you can also [view the source](#topic_abz_r5t_khc)
   used to generate the suggestion.

   - If the suggestion is what you want to send or the action is what you
     want to perform, click **Approve**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_agent_copilot_composer_updated_1213.png)
   - If the suggestion needs to be edited, click **Edit** to update
     the wording or [edit the formatting](https://support.zendesk.com/hc/en-us/articles/4408844184730) by
     clicking the **T** icon at the bottom of the comment
     field.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_auto_assist_edit_rtf.png)

     All formatting tools
     are available for auto assist suggestions on the email channel
     except for lists. On the messaging channel, indents and tables
     aren’t available.

     Click **Cancel edit** to return to
     the unedited suggestion.

     Actions can't be edited.

     If
     the ticket is updated while you're editing a suggestion, then
     new suggestions may be available. Click **View suggestions**
     to review the new suggestions.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_auto_assist_new_suggestions.png)

     Click **Apply** to approve the
     suggestion and overwrite the previous suggestion you were
     editing.
   - If the suggestion is a macro, click its name to open a
     preview

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_agent_auto_assist_macro.png)

     The macro's preview shows any
     ticket property actions it'll perform and its public reply. You
     can make changes in the Agent Workspace if needed.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_agent_auto_assist_macro_preview.png)
   - If the suggestion is an action and you don't want to perform the
     suggested action, click the X on the action to remove it. Or, [take over from auto
     assist](#topic_qzh_cth_4cc) instead.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_auto_assist_edit.png)
   - If the suggestion isn't helpful, click **Leave
     feedback**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_auto_assist_agent_feedback.png)

     Select one of the
     predefined feedback options or click **Other** and enter your
     feedback. Then, click **Share feedback**.

     Your feedback
     helps improve the quality of auto assist's suggestions.
3. When you're done, click **Save**, and then **Approve**.

   The message
   is sent under your name, and any actions taken are performed under your
   name. You can view approved replies and actions in the [ticket's events](https://support.zendesk.com/hc/en-us/articles/4408829602970).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_aa_approved_events_log.png)

   Auto assist
   provides a new suggestion after every customer response.

### Viewing sources for auto assist suggestions

If you have the appropriate permission, you can view the source auto assist used
when generating a suggestion.

Sources are displayed when suggestions are based on procedures or public help
center articles. Suggestions can be generated from other sources, but these
sources aren't displayed in auto assist's rationale.

**To view the source auto assist used for a suggestion**

1. In the Agent Workspace, open a ticket.
2. In the ticket, review the suggestion in the **Auto assist**
   panel.
3. Hover your mouse over the info icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/info_icon.png)).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/copilot_auto_assist_suggestion_sources.png)

   Auto assist displays
   its rationale and, if the suggestion was generated from a procedure
   or help center article, the source.

   Procedures are marked with
   a star icon, and articles with a book icon.
4. (Optional) Click the title of the source to open it.

## Following instructions provided by auto assist

If your admin has written instructions that are relevant to your ongoing
conversation, auto assist may show them to you so that you can follow them to help
solve the ticket.

The instructions auto assist suggests are different from other auto assist
suggestions. Auto assist doesn't generate the instructions it shows to you. They're
written by your admin. So instead of reviewing and approving as you would with
another auto assist suggestion, you'll perform the steps manually and mark them
complete when you're done.

For example, say you're working on a ticket for a product return. Auto assist
suggests a reply asking for the user's order number and other information, which you
approve. The user replies with the information and then auto assist provides
instructions on how to log into your internal inventory management system and submit
the return.

**Following instructions provided by auto assist**

1. In Agent Workspace, open a ticket.
2. Above the Auto assist panel, hover your mouse over the provided
   **Instructions** for an overview.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_auto_assist_agent_review_instructions.png)

   Auto assist might
   also suggest a reply. Click **Approve** to accept the suggestion and
   send the reply.
3. Click the instructions to open them in the Knowledge panel.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_auto_assist_agent_instructions_knowledge.png)
4. Perform the steps and click **Completed** when you're done.

   If you try
   to complete the steps but can't, click **Not completed**.

   If
   the instructions are irrelevant, you can ignore them and don’t need to
   click anything.
5. Continue the conversation with the user.

## Taking over from auto assist suggestions

If you don’t want to receive help from auto assist on a ticket, you can take over and
interact with the ticket as you normally would.

**To take over from auto assist suggestions**

1. In Agent Workspace, open a ticket.
2. In the Auto assist panel, click the auto assist icon (![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/ai_auto_assist_icon.png)) to toggle auto assist suggestions
   off.

   Note: You can reply with a macro without turning auto assist
   off.
3. [Compose messages in the Agent
   Workspace](https://support.zendesk.com/hc/en-us/articles/4408831849882) as normal.

   If you want to return to the auto assist
   suggestions, click the auto assist icon (![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/ai_auto_assist_icon.png)) again.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/ai_auto_assist_composer_return.png)
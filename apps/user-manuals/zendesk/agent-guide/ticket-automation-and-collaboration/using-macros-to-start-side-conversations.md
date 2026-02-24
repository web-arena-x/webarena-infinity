# Using macros to start side conversations

Source: https://support.zendesk.com/hc/en-us/articles/4408829558938-Using-macros-to-start-side-conversations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Collaboration add-on |

Location:  Admin Center > Workspaces > Agent tools > Macros

If [side conversations are
activated](https://support.zendesk.com/hc/en-us/articles/4408832279962-Enabling-and-disabling-side-conversations), it's the perfect way to reach out to other
departments or external partners. However, for many teams, they can become
repetitive, especially if there’s a specific structure to the initial
messages. You can use macros to start side conversations to ensure that key
information is included automatically when the conversation is started.

For example, let’s say that you want to start a side conversation with a few
things like:

- The requester’s initial message
- Some additional questions from the agent
- Some custom field values
- The originating ticket’s ID and URL

This article includes these topics:

- [About macros for side conversations](#topic_mt1_rng_gfb)
- [Creating macros for side conversations](#topic_kk5_rng_gfb)
- [Applying macros to side conversations](#topic_u4y_sng_gfb)

Related articles:

- [Creating macros for
  tickets](https://support.zendesk.com/hc/en-us/articles/4408844187034)

## About macros for side conversations

You can add a **Side conversation** action to any macro and when it
runs, a new side conversation is started and immediately pops open.
Ticket information and some extra boilerplate text are added
automatically to the body by means of placeholders, leaving you to
add any additional recipients or information that you want to
include.

There are a few important things to note about how this feature
behaves:

- When you use a macro to start a side conversation, the macro is
  not applied to any of the side conversations that are
  already on the ticket. It is only applied to the new side
  conversation that you're starting now.
- Keep in mind that your macro may include other actions that
  change ticket fields. If you don't submit the ticket, those
  changes will be lost.

There are three **Side conversation** actions in macros:

- **Side conversation via email:** When you add this action to
  a macro, you can also enter the email addresses of the users
  that you want to include in the email notification.

  If
  you manually enter an email address into the
  **To** field, make sure that the email address
  is correct. The email addresses you enter will
  become the recipients of a side conversation when
  the macro is used.
- **Side conversation via Slack:** End users receive ticket
  updates in Slack (see [Using Slack in side
  conversations](https://support.zendesk.com/hc/en-us/articles/4408844202778)).

  When you add this action to
  a macro, you can specify only one Slack channel and
  must enter its name manually. Enter an existing
  Slack channel name so that it automatically
  populates the "To" field in the side conversation
  when you apply the macro.

  If you enter a
  partial Slack channel name when adding this action,
  the "To" field will display a list of all channels
  that contain the partial name when the macro is
  applied. You can then select the channel from the
  list.
- **Side conversation via child ticket:** When you use this
  action, you create a side conversation on the original
  ticket and a new child ticket is created (see [Using side
  conversation child tickets](https://support.zendesk.com/hc/en-us/articles/4408836521498)).

  Note that you
  can specify only groups that you have access to and
  agents within those groups in the **To**
  field.

## Creating macros for side conversations

Anyone (agents or admins) can create a personal macro for side
conversations. Administrators can also create shared macros for side
conversations. You cannot create macros for specific channels.

You may want to use macros to start side conversations to ensure that key
information is included automatically when the conversation is
started.

**To create personal macros for side
conversations**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Macros**.
2. Click **Create macro**.
3. Enter the macro name, and add actions for your macro as
   described in [Building macro action
   statements](https://support.zendesk.com/hc/en-us/articles/4408832783642).
4. In the **Actions** section, choose one of the **Side
   conversation** actions from the drop-down list,
   enter then enter a subject and your message.
5. Fill in the **To**, **Subject**, and **Message** fields
   for information you regularly need or use.

   You can use
   [placeholders](../../product-guides/business-rules/using-placeholders.md)
   in these fields for information that you regularly
   need or use.

   For example, this macro starts a
   side conversation and includes the first message
   from the requester, plus some information from the
   original ticket:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/macros_with_side_conversation.png)

   Note: You cannot add images.
   Markdown in agent signatures does not render in
   emails sent through side conversations.
6. Click **Create**.

## Applying macros to side conversations

Macros for side conversations create a new side conversation and
automatically add ticket information and some extra boilerplate to
the body of the message.

**To apply macros to side conversations**

1. From the ticket, click the **Apply macro** button in the
   bottom toolbar.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/apply_macro_button.png)
2. Typically, your five most commonly used macros from the past
   week appear at the top of the macros list.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/apply_macros_small.png)

   You can select one of
   these, begin typing the name of the macro, or scroll through
   the list to find the one you want to use.

   The most-used
   macros display can be disabled, in which case,
   you'll only see the all macros list. For
   information, see [Disabling the most-used macros
   option](https://support.zendesk.com/hc/en-us/articles/4408884166554#topic_jf5_2cc_dx).

   The actions defined in the
   macro will be applied. If the macro updated the
   ticket comment, you can edit the text before
   submitting the ticket.
3. When the macro with a **Side conversation** action runs, it
   immediately starts a single new side conversation with the
   ticket information and boilerplate text specified by the
   macro. The side conversation is not saved though until you
   add a recipient and click **Send**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/thread_with_macro_message.png)
4. Add a recipient to the side conversation.
5. If needed, change the subject of the side conversation and add,
   remove, or change information in the message.
6. Click **Send**.
7. If the macro updated any ticket fields, make sure that you also
   submit the ticket. For example, if your macro starts a side
   conversation and also changes a ticket's group, the side
   conversation will be opened, but the ticket group change
   will not be saved until you submit the ticket.
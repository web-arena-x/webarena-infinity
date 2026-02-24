# Managing use cases for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/9041911005850-Managing-use-cases-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

*Use cases* are the mechanism by which [zero-training AI agents](https://support.zendesk.com/hc/en-us/articles/8357749447194) and [AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/8966284087066) understand what a customer is
asking about and connect them with the right [dialogue](https://support.zendesk.com/hc/en-us/articles/8357749494810) or [procedure](https://support.zendesk.com/hc/en-us/articles/8979864563610). After you [create a use case](https://support.zendesk.com/hc/en-us/articles/9041901679130), you can manage it from the Use cases
page.

This article contains the following topics:

- [Viewing all use cases](#topic_pcz_qdk_mfc)
- [Categorizing a use case](#topic_cyg_nhr_mdc)
- [Copying a use case to another AI agent](#topic_ajq_d54_3hc)
- [Deactivating a use case](#topic_qv3_c2r_mdc)
- [Deleting a use case](#topic_o23_22r_mdc)
- [Resolving conflicts between duplicate use cases](#topic_ns2_g2r_mdc)
- [Restoring a previous version of a use case](#topic_ugn_32r_mdc)
- [Configuring whether a use case uses a dialogue or generative procedure](#topic_elk_mcf_52c)

Related article:

- [Best practices for use cases for advanced AI
  agents](https://support.zendesk.com/hc/en-us/articles/8357733365402)

## Viewing all use cases

On the Use cases page, you can view all the use cases you've created for an advanced
AI agent.

**To view all use cases**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to
   work with.
2. Click **Content** in the sidebar, then select **Use cases**.

   On this page, you can see all the use cases you've created, including
   the following details:

   - **Usage**: The percentage of customer messages matched to the given
     use case over the last seven days, including today.
   - **Use case**: The name and description of the use case.
   - **Conflict**: Whether a conflict exists between this use case and
     another one. See [Resolving conflicts between duplicate use cases](#topic_ns2_g2r_mdc).
   - **Category**: The category assigned to the use case. See [Categorizing a use case](#topic_cyg_nhr_mdc).
   - **Reply method**: Whether the use case uses a dialogue or procedure.
     See [Configuring whether a use case uses a dialogue or generative procedure](#topic_elk_mcf_52c).
   - **Last edited**: The date and time the use case was last
     edited.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_use_cases_page_columns.png)

## Categorizing a use case

Categorizing use cases makes managing them easier, but it doesn’t affect how an
advanced AI agent connects use cases with a customer’s message (only use case names
and descriptions do that).

In the list of use cases, the Category column shows a use case’s category. You can
filter use cases using the Category drop-down at the top of the page.

**To categorize a use case**

1. [In the list of use
   cases](#topic_pcz_qdk_mfc), click the use case you want to categorize.

   The use case
   details page opens.
2. In **Category**, select an existing category, or start typing to enter a
   new category and click **Add a category**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_use_case_category_new.png)
3. Click **Save**.

## Copying a use case to another AI agent

To save time when configuring multiple AI agents, you can copy a use case from one AI
agent to another.

Any actions linked at the use-case level aren't automatically copied. After you copy
a use case to another AI agent, make sure you [recreate the actions](https://support.zendesk.com/hc/en-us/articles/8357756623770) in the target AI agent (if they
don't exist already) and [add them to the use case](https://support.zendesk.com/hc/en-us/articles/8357756623770#topic_zbz_kyl_rgc).

**To copy a use case to another AI agent**

1. [In the list of use
   cases](#topic_pcz_qdk_mfc), find the use case you want to copy.
2. Click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) on the right-hand side and select **Copy use
   case**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_copy_use_case_menu.png)

   The "Copy use case to
   another AI agent" dialog appears.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/aiaa_copy_use_case_window.png)
3. In **Use case**, confirm the use case you want to copy is selected.

   If
   not, select the desired use case.
4. (Optional) Deselect **All use case actions** if you don't want to copy
   the [actions that have been added at the use
   case level](https://support.zendesk.com/hc/en-us/articles/8357756623770#topic_zbz_kyl_rgc) for this AI agent.

   The number in parentheses tells
   you how many actions will be copied.
5. (Optional) Deselect **All replies** if you don't want to copy the
   [replies that have been created](https://support.zendesk.com/hc/en-us/articles/9624068102682#topic_i1v_nzx_jgc)
   for this AI agent.

   Note: [System replies](https://support.zendesk.com/hc/en-us/articles/8357749481882#topic_edj_gnp_xfc) can't be
   copied.
6. In **Destination AI agent**, select the AI agent you want to copy the use
   case to.

   Note: If the destination AI agent doesn't have
   the same supported languages as the source AI agent, an error message
   appears. [Add the languages](https://support.zendesk.com/hc/en-us/articles/8357749666714#topic_rmc_kzx_jgc) to the
   destination AI agent and try again.
7. Click **Copy**.

   The use case is copied to the specified AI
   agent.

## Deactivating a use case

Deactivating a use case allows you to retain its configuration (nothing is deleted),
but your AI agent won’t use it to connect customers with a dialogue until you
reactivate the use case.

**To deactivate a use case**

1. [In the list of use
   cases](#topic_pcz_qdk_mfc), find the use case you want to deactivate.
2. Click the options (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) menu, and select
   **Deactivate**.

   Your use case is immediately deactivated. You can
   reactivate it by clicking the options (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) menu and selecting
   **Activate**.

## Deleting a use case

If you’re confident that you don’t need a use case anymore, you can delete it. As
with deactivating a use case, deleting a use case ensures that your AI agent will no
longer use that use case to connect customers with a dialogue. Deleting a use case
is permanent and cannot be undone.

Important: Deleting a use case also removes the associated dialogues, intent, and
expression data, if there were any. This means that you won’t be able to [revert the use case back to an
expression](https://support.zendesk.com/hc/en-us/articles/8357749441690), if that were to become necessary. In addition, names of
deleted use cases no longer appear in reports.

**To delete a use case**

1. [In the list of use
   cases](#topic_pcz_qdk_mfc), find the use case you want to delete.
2. Click the options (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_menu_vertical.png)) menu, and select
   **Delete**.

   Your use case is immediately deleted.

## Resolving conflicts between duplicate use cases

If multiple use cases have names or descriptions that are too similar, they may be
considered duplicates. Duplicate use cases cause confusion in AI agent
conversations, as the wrong use case might be detected or the wrong reply might be
triggered. To prevent this confusion, you should review and resolve conflicts
between duplicate use cases.

**To resolve conflicts between duplicate use cases**

1. [In the list of use
   cases](#topic_pcz_qdk_mfc), look for use cases that have an entry in the Conflict
   column.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_use_cases_review_duplication.png)

   Tip: When you hover over a use case
   with a conflict, any conflicting use cases in the list are
   highlighted.
2. Click **Review duplication**.

   A new window appears and shows the
   details of the conflict.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_use_cases_duplication_resolve.png)
3. Resolve the conflict by taking one of the following actions:
   - Click **Investigate** and update the name and description of one
     or both of the use cases so they're more distinct.
   - Click the toggle to deactivate one of the use cases. Inactive use
     cases aren't analyzed for duplicates.
4. Click **Confirm**.

## Restoring a previous version of a use case

Any updates made to a use case’s name or description are tracked and can be rolled
back if necessary, making it safer to test changes or recover from errors.

**To restore a previous version of a use case**

1. [In the list of use
   cases](#topic_pcz_qdk_mfc), click the name of the use case you want to restore a
   previous version of.
2. In either the **Name** or **Customer request reason** field, click the
   **Show version history** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_use_cases_version_history_icon.png)) icon.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_use_cases_show_version_history.png)

   The **Version History**
   panel appears on the right, showing you the changes made to the use case’s
   name or description. The panel shows which user made the changes and when,
   and which version of the use case is the current version. You can expand the
   version history entries to see the content of the **Name** or **Customer
   request reason** field for each saved change.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_use_cases_version_history.png)
3. (Optional) Click the **Type** drop-down field, select the types of use
   case changes you want to see (**name**, **description**, or both), and
   click **Apply**.
4. Find the version of the use case name or description you want to restore and
   click the **Restore** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_restore_icon.png)) icon.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_use_cases_restore_version_history.png)
5. Click **Save**.

## Configuring whether a use case uses a dialogue or generative procedure

Note: This section applies only to [AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/8966284087066).

Within an AI agent with agentic AI, you can decide whether an individual use case
should use a scripted dialogue or a generative procedure. AI agents that use both
generative-AI responses and scripted responses are sometimes referred to as hybrid
AI agents.

- **A scripted dialogue** lets you determine the exact flow that an AI agent
  should follow for a particular use case.

  Dialogues give you a lot of control,
  but also require more maintenance than a procedure. Consider using dialogue
  for use cases where customer issues need to be handled in very specific ways
  and even small deviations from an exact process can’t be tolerated.

  For
  more information on creating dialogues, see [Using the dialogue builder to create
  conversation flows for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357749494810).

- **A generative procedure** gives the AI agent the freedom to determine the
  best way to resolve a customer’s issue in line with your business policies.

  Procedures require less setup and maintenance from you, but they also
  offer you less direct control over very fine details. Consider using
  procedures for use cases where customer issues are less sensitive and can be
  handled in a number of flexible ways.

  For more information on creating
  procedures, see [Creating generative procedures for AI agents
  with agentic AI](https://support.zendesk.com/hc/en-us/articles/8979864563610).

If a use case has neither an active dialogue nor a generative procedure, or if no
appropriate use case exists for a conversation, the AI agent forms responses using
only the content of your imported knowledge source, not dialogues or procedures. You
can configure a use case this way if you want to trigger some actions or track a
certain topic in analytics, but still let the response be purely generative.

For more guidance on which method to use, see [When to use a generative procedure or a dialogue](https://support.zendesk.com/hc/en-us/articles/9424547622298).

**To configure whether a use case uses a dialogue or procedure**

1. [In the list of use
   cases](#topic_pcz_qdk_mfc), click the use case you want to configure.
2. Under **Reply method**, click the drop-down field and select one of the
   following options:
   - **Use dialogue when use case is triggered**
   - **Use procedure when use case is triggered** (default for new use
     cases)

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_reply_method_setting.png)
# Managing generative procedures for AI agents with agentic AI

Source: https://support.zendesk.com/hc/en-us/articles/10040865503898-Managing-generative-procedures-for-AI-agents-with-agentic-AI

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Generative procedures are AI-generated procedures that help power the decision-making
capabilities of [AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/8966284087066). After you [create a generative procedure](https://support.zendesk.com/hc/en-us/articles/8979864563610), you can manage it at any
time.

This article contains the following topics:

- [Editing generative procedures](#topic_qcm_tcc_tgc)
- [Testing generative procedures](#topic_unp_tf3_cfc)
- [Viewing and restoring previous versions of generative procedures](#topic_b2h_5cc_tgc)
- [Adding a note to a generative procedure version](#topic_vp5_dnq_4hc)

Related articles:

- [Best practices for creating generative procedures
  for AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/9424547622298)
- [Examples of generative procedures for AI agents
  with agentic AI](https://support.zendesk.com/hc/en-us/articles/9424547984026)

## Editing generative procedures

You can edit a generative procedure at any time.

**To edit a procedure**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to
   work with.
2. Click **Content** in the sidebar, then select **Use cases**.
3. Click the use case you want to edit the procedure for.
4. Under **Reply method**, make sure the **Procedure** tab is selected.
5. Click **Edit procedure**.
6. Make adjustments to the procedure using the free-text field at the bottom and
   click **Update procedure**.

   The timestamp in the upper-right corner is
   updated to show your username and how long ago you edited the
   procedure.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_procedure_timestamp.png)
7. Review the AI-generated procedure map to ensure the logic the AI agent will
   follow is appropriate.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_gen_procedure_map_example_updated.png)
8. (Optional) Repeat the previous two steps until you’re satisfied with the
   procedure map.
9. If you want to make your edits live to customers, click **Publish
   procedure**.

   If you want to discard your edits, [restore a previous version of
   the procedure](#topic_b2h_5cc_tgc).

## Testing generative procedures

After you create or update a generative procedure, you can test it before making it
live for your AI agent.

Testing a procedure always tests the most recently made changes. For example, if you
draft updates to a live procedure and test it before publishing the updates, the
draft is tested, not the published version.

**To test a generative procedure**

1. [Open a procedure for
   editing.](#topic_qcm_tcc_tgc)
2. In the top-right, click **Test procedure**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_test_procedure_button.png)
3. In the Session parameters dialog, do one of the following:
   - To test a conditional branch of the procedure, select a
     **Parameter** and enter a **Value**, then click
     **Test**.
   - To test the procedure as a whole, click **Test without
     parameters**.

     Tip: To remember your
     selection for next time, unselect **Ask me every
     time**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_session_parameters_dialog.png)
4. In the test widget that appears, test the procedure by sending messages to
   the AI agent.

Tip: To view test conversation data, [filter the conversation logs](https://support.zendesk.com/hc/en-us/articles/8357749580186#topic_y3w_5gf_52c) by
**Display only test conversations**.

## Viewing and restoring previous versions of generative procedures

A version history is maintained for each procedure. This means you can quickly
restore a previous version of a procedure if a newer version includes changes you
don’t want to keep.

You can view and restore a specific version of a procedure from the procedure builder
update log on the left, or from the version history panel on the right.

**To view and restore a procedure from the update log**

1. [Open a procedure for
   editing.](#topic_qcm_tcc_tgc)
2. In the procedure builder update log on the left, click a version that you
   want to view.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_generative_procedures_update_log_versions.png)

   The selected version opens
   in a read-only view. You can use the **View previous version** and
   **View next version** icons (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_view_previous_icon.png)![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_view_next_icon.png)) in the upper right to move through different
   procedure versions.
3. In the upper right, click **Restore procedure**.

   Or, to return to the
   current, editable procedure, click **Close**.

**To view and restore a procedure from the version history panel**

1. [Open a procedure for
   editing.](#topic_qcm_tcc_tgc)
2. In the upper-right corner, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **View version history**.

   The
   Version history panel appears. Versions are grouped by day. A green
   checkmark indicates the currently published version of the procedure.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_procedure_version_history.png)
3. Click to expand the day that includes the version you want to revert back
   to.

   Each version shows the timestamp and user who saved or published
   it. Any [notes added](#topic_vp5_dnq_4hc)
   for the version are shown as well.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_procedure_version_history_expanded.png)
4. To view a previous version of the procedure, click its entry in the Version
   history panel.

   That version of the procedure opens in a read-only
   state.

   Tip: You can copy a direct
   link by clicking the options menu for that version and selecting
   **Copy link to version**. This is helpful if you need to
   share a specific version of the procedure with another user.
5. To restore the version, click **Restore procedure** in the upper
   right.

   Alternatively, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) for the version you want to restore and
   select **Restore as draft**.

   The version is restored as the
   current draft, and the live AI agent is not affected.
6. To make the restored version live to customers interacting with the AI
   agent, click **Publish procedure**.

At any point, you can return to the currently published version of the procedure for
comparison.

**To return to the currently published version of the procedure**

- With the procedure open, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **View published
  procedure**.

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_procedure_view_published.png)

  The current version of the
  procedure appears.

## Adding a note to a generative procedure version

Each time you update a generative procedure, it creates a new version in the
procedure's version history. For each version, you can add a note to help you
remember the changes you made to that version.

**To add a note to a generative procedure version**

1. [Open a procedure for
   editing.](#topic_qcm_tcc_tgc)
2. Make any necessary changes and click **Publish procedure**.

   A
   notification message appears in the lower-left corner.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_procedure_updated_notification.png)
3. Click **Add note** in the notification message.

   Alternatively, click
   the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) in the upper-right corner and select
   **View version history**. Click the options menu for the version
   you just updated and select **Add note**.

   The Add note dialog
   appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_procedure_add_note.png)
4. Enter the text of your note and click **Save**.

   The note is added
   underneath the version in the Version history panel.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_procedure_version_history_note_example.png)
5. (Optional) To edit or delete a note, click the options menu and select
   **Edit note** or **Delete note**.
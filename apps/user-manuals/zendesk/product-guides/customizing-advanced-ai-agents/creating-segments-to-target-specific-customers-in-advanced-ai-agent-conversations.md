# Creating segments to target specific customers in advanced AI agent conversations

Source: https://support.zendesk.com/hc/en-us/articles/9413046533530-Creating-segments-to-target-specific-customers-in-advanced-AI-agent-conversations

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Segments are collections of customers who share common traits. By creating segments, you can precisely tailor experiences for distinct subsets of your user base, enabling personalized communication and targeted automation.

This article contains the following topics:

- [About segments](#topic_w4v_vng_5fc)
- [Creating segments](#topic_s53_wng_5fc)
- [Viewing all segments](#topic_th5_wng_5fc)
- [Editing segments](#topic_gwm_xng_5fc)
- [Deleting segments](#topic_tfz_xng_5fc)

## About segments

Segments are defined by one or more [session parameters](https://support.zendesk.com/hc/en-us/articles/8357733406234#h_01GKHFXHVRFXJ7P392SW7FJH8V) that match whatever values you configure. For example, you can create segments based on locale, language, customer type, or any other custom session parameter tracked within the AI agents - Advanced add-on.

After you create segments, you can use them in [dialogues](https://support.zendesk.com/hc/en-us/articles/8357749494810) as part of a conditional block to shape conversation flows for different types of customers. You can also use segments to tailor your [search rules](https://support.zendesk.com/hc/en-us/articles/9185497386394) for [AI agents that use agentic AI](https://support.zendesk.com/hc/en-us/articles/8966284087066).

In the conversation logs, you can [filter conversations](https://support.zendesk.com/hc/en-us/articles/8357749580186#topic_y3w_5gf_52c) to see where specific segments were used. This helps you further analyze your AI agent’s interactions with specific subsets of your customer base.

## Creating segments

You can create segments to define specific collections of customers who share common traits.

**To create a segment**

1. In the top-right corner, use the AI agent drop-down field to select the AI agent you want to create a segment for.
2. In the left sidebar, click **Content** > **Segments**.
3. Click **Create segment**.

   The Create segment window opens.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_segments_create.png)
4. In **Name**, enter a unique and descriptive name for your segment.
5. In **Description**, enter a description that helps the underlying AI model understand what the segment is intended to identify.
6. Under **Conditions**, select how the conditions within a segment relate to each other:
   - **Match ALL conditions**: All listed conditions must match the session configuration for the segment to become active.
   - **Match ANY conditions**: At least one of the listed conditions must match the session configuration.
   - **Match NONE of these conditions**: None of the listed conditions can match the session configuration.
7. Define the segment’s criteria:
   1. Click **Select parameter** and select which existing parameter should be used to define the segment.

      Tip: If the parameter you want to use doesn’t exist yet, create it as part of an [action](https://support.zendesk.com/hc/en-us/articles/8357756651290) or [API integration](https://support.zendesk.com/hc/en-us/articles/8357756844442) first.
   2. Click **is** and select one of the following string operators for the selected parameter:
      - Is
      - Is not
      - Contains
      - Begins with
      - Ends with
      - Exists
      - Does not contain
      - Does not begin with
      - Does not end with
      - In
      - Not in
      - Does not exist
   3. In the blank field, enter the value that defines the parameter in relation to its operator.

      For example, if you selected the *active\_language* parameter and the *is* operator, enter the language ID.

      Note: When you use *active\_language* in a segment, you must use the language’s ID, not its name, as the parameter value. You can find the ID by going to **Settings** > **AI agent settings** > **Languages** and selecting a language.
8. (Optional) Click one of the following to add more conditions as needed:
   - **Add condition**: Adds a single condition, which is evaluated by the main Match ALL/ANY/NONE relationship.
   - **Add condition group**: Adds a group of conditions, which are evaluated by the group-level Match ALL/ANY/NONE relationship first, and then by the main relationship.

     For more information, see [Using condition groups](#topic_jgk_n4g_5fc).
9. (Optional) Repeat steps 7–8 to add more conditions or condition groups to fully define the segment.

   You can add any number of conditions and condition groups.
10. Click **Create segment**.

### Using condition groups

Condition groups count as a single condition. They are evaluated as either true or false based on their internal group relationship (Match ALL/ANY/NONE). You can add one level of conditional groups within a segment configuration (meaning you can’t add a group within a group).

Condition groups are best used when you want to apply different group conditions to your segments. For example:

- Parameter 1 must be A
- Parameter 2 must be B
- Parameter 3 can be C or D

To do this, you can apply a Match ALL relationship to the conditions for parameters 1 and 2, and then add a condition group with a Match ANY relationship for parameter 3.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_segments_condition_group_example.png)

## Viewing all segments

The Segments page shows you all existing segments.

**To view all segments**

1. In the top-right corner, use the AI agent drop-down field to select the AI agent you want to delete a segment for.
2. In the left sidebar, click **Content** > **Segments**.

   The Segments page lists the segments you’ve created and includes the following columns:

   - **Segment**: The name and description of the segment
   - **Usage**: Where the segment is currently being used
   - **Last updated**: The timestamp of when the segment was last edited

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_segments_view_all.png)

## Editing segments

You can edit an existing segment if you need to adjust its criteria.

Editing a segment doesn’t affect how or whether that segment was applied to conversations in the past. In other words, the edits aren’t retroactive.

**To edit a segment**

1. [On the Segments page](#topic_s53_wng_5fc), click the segment you want to edit.

   The Segment details pane opens.
2. Click **Edit segment**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_segments_edit.png)
3. Update the segment’s criteria as needed.

   For help, see [Creating segments](#topic_s53_wng_5fc).
4. Click **Save**.

## Deleting segments

You can delete a segment if you no longer need it to define a part of your user base.

**To delete a segment**

1. [On the Segments page](#topic_s53_wng_5fc), hover over the segment you want to delete, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)), and select **Delete**.

   A confirmation window opens, showing you where the segment is currently being used, if applicable.
2. Click **Delete**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_segments_delete.png)
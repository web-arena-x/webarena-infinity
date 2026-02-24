# Using the confusion matrix to improve advanced AI agent performance (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/8357756496922-Using-the-confusion-matrix-to-improve-advanced-AI-agent-performance-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

This article applies only to legacy [expression](https://support.zendesk.com/hc/en-us/articles/8357751704474)-based AI agents.

The confusion matrix provides a weekly visualization of the performance of an AI model,
measured by its intent recognition. It shows you whether your AI model is able to distinctly
recognize similar expressions under different intents or whether it is confused by them. This
information can help you understand your AI agent performance.

In assessing AI agent performance, you might find that a message you expect to be recognized
as one intent is picked up as another intent because two intents overlap in their expressions.
You can use the confusion matrix to understand where the overlap occurs. You can then use that
information to adapt the manually trained expressions to eliminate inconsistencies and improve
performance.

There is also a list of issues that you can sort by priority to help you determine what to
work on.

This article covers the following topics:

- [Viewing the confusion matrix](#topic_wx1_vg2_42c)
- [Viewing issues raised in the confusion
  matrix](#topic_w3m_xg2_42c)
- [Retraining the confusion
  matrix](#topic_syz_wg2_42c)

## Viewing the confusion matrix

The confusion matrix is a color-coded grid that indicates how well the model is
performing in terms of understanding intents. A good model should have a dark line running
diagonally across the table.

You should review the confusion matrix when you notice the AI agent answered rate is
decreasing. A baseline of 80% is recommended. You might also review the confusion matrix if
you notice that your AI agent is regularly categorizing messages under the wrong intent.

**To view the confusion matrix**

1. [In AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Training Center** in the
   sidebar, then select **Confusion Matrix**.
2. Click the **Confusion matrix** tab at the top.

   The two dimensions, the X
   (horizontal) and Y (vertical) axes, represent the actual and predicted intents
   respectively. In this example, column 1 and row 1 are the actual and predicted intent
   Affirmative, row 2 and column 2 are the intent Negative, and so on.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_mceclip0_ilBBF.png)
3. Review the colored cells in the matrix.

   The darker the cell, the more a predicted
   intent overlaps with an actual intent. A good model should have a dark line running
   diagonally across the table.

   Colored cells outside of the diagonal represent how
   often messages in an intent are predicted to another. Cells with darker colors outside
   of the diagonal indicate a problem in the accuracy of the AI model caused by potential
   overlaps of expressions between two intents.

Next, you can [view the list of issues](#topic_w3m_xg2_42c)
where overlapping issues are automatically listed according to priority.

## Viewing issues raised in the confusion matrix

You can use the list of issues to drill into issues surfaced in the confusion matrix.
Overlapping issues are automatically listed according to high, medium, or low priority to
help you determine what to focus on.

**To access the list of issues**

1. [In AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Training Center** in the
   sidebar, then select **Confusion Matrix**.
2. Click the **List of issues** tab at the top.
3. Click the **Priority** heading to sort by priority.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_9883273415698.png)
4. Use the **Advanced filters** to define the confusion level, as needed, or use
   **Search** to find a specific intent you think might be causing confusion with other
   intents.
5. Click **Solve issue**, then click **Manage expressions** to open the expressions
   management view.
6. To manage highlighted items:
   - Click the left and right arrows to move an expression to a different intent.
   - Click the x to delete the expression.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/bots_9883255076754.png)
7. Take any of the following actions as you work through the highlighted items:
   - Untrain the expressions or move them to the other intent.
   - Create a new intent with those expressions.
   - Merge the intents if they should be the same.
   - Help your AI model learn by training more expressions to those two confused intents.
     Only do this if you are absolutely certain the two intents are very different and
     should be separated.
8. Click **Mark as solved** to keep track of your progress.

## Retraining the confusion matrix

The confusion matrix is automatically generated every Tuesday night (Pacific time).

If your AI agent has recently undergone extensive training, or if major alterations have been
made to it (changes to expressions or intents), you can perform manual retraining outside of the
schedule.

**To retrain a confusion matrix**

1. [In AI agents - Advanced](https://support.zendesk.com/hc/en-us/articles/4408838272410), click **Training Center** in the
   sidebar, then select **Confusion Matrix**.
2. Click **Re-train** in the top-right corner.
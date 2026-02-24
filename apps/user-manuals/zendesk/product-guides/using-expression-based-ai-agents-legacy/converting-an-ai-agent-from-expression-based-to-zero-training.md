# Converting an AI agent from expression-based to zero-training

Source: https://support.zendesk.com/hc/en-us/articles/8357749441690-Converting-an-AI-agent-from-expression-based-to-zero-training

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | AI agents - Advanced |

If you’ve already created an AI agent that uses [expressions](https://support.zendesk.com/hc/en-us/articles/8357751704474), you can quickly convert it to a [zero-training AI agent](https://support.zendesk.com/hc/en-us/articles/8357749447194) that uses [use cases](https://support.zendesk.com/hc/en-us/articles/9041901679130).

Converting an existing AI agent lets you take advantage of the benefits of use cases without losing access to the AI agent’s historical data, which is useful for reporting purposes.

This process requires no downtime for the AI agent.

Watch the video below for a walkthrough of the process, or keep reading for step-by-step instructions.

*Migrating expression-based AI agents to zero-training AI agents (4:36)*

**To convert an AI agent from expression-based to zero-training**

1. In the top-right corner, use the AI agent drop-down field to select the AI agent you want to convert.
2. In the left sidebar, select **Settings** > **AI agent settings**.
3. Under **Generative AI**, select **Activate zero-training interface**.

   Important: Do not select **Use zero-training AI model** yet. While you proceed with the conversion process, the AI agent should continue to handle customer queries based on its trained expressions.
4. Click **Save**.
5. In the left sidebar, select **Content** > **Use cases**.
6. For each intent:
   1. Click **Convert**.

      ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_use_cases_convert.png)
   2. In the **Convert to use case** window, review the automatically populated suggestions for the **Name** and **Customer request reason** fields.

      ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_convert_to_use_case.png)

      These suggestions are AI-generated based on the content of the original intent. If not enough information was included in the original intent, a suggestion won’t be populated and you’ll see the message AI wasn’t able to generate a suggestion due to missing data.

      ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ultimate_convert_no_suggestion.png)
   3. (Optional) Edit any of the fields as needed.

      For more information, see [Creating use cases for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/9041901679130).
   4. Click **Convert**.
7. After you’ve converted all intents into use cases, in the left sidebar, select **Settings** > **AI agent settings**.
8. Under **Generative AI**, select **Use zero-training AI model**.

   This setting transitions the AI agent from using expressions to use cases. However, all your expressions are still stored in the background, meaning you won’t lose that content and can still revert back from use cases to expressions, if necessary.
9. Click **Save**.
10. [Test your AI agent](https://support.zendesk.com/hc/en-us/articles/8357758879130) to make sure it’s still performing as you expect.

    If anything seems off, you can deselect the **Use zero-training AI model** setting to revert back to expressions. Update your use case names and descriptions to improve the performance of the AI agent as needed, then reselect the **Use zero-training AI model** setting.
# Creating use cases for advanced AI agents to identify what customers are asking about

Source: https://support.zendesk.com/hc/en-us/articles/9041901679130-Creating-use-cases-for-advanced-AI-agents-to-identify-what-customers-are-asking-about

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

*Use cases* are the mechanism by which [zero-training AI agents](https://support.zendesk.com/hc/en-us/articles/8357749447194) and [AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/8966284087066) understand what a customer is asking about and connect them with the right [dialogue](https://support.zendesk.com/hc/en-us/articles/8357749494810) or [procedure](https://support.zendesk.com/hc/en-us/articles/8979864563610). Use cases are the topics that your customers need help with, such as order returns or refund requests.

This article contains the following topics:

- [Creating a use case manually](#topic_ik4_12r_mdc)
- [Creating use cases based on AI suggestions](#topic_gr4_l5n_s2c)

Related articles:

- [Managing use cases for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/9041911005850)
- [Best practices for creating use cases for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357733365402)

## Creating a use case manually

An advanced AI agent can start supporting customers with as little as one use case.
Before creating your first use case, see [Best practices for creating use cases for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/8357733365402).

As an alternative to creating use cases manually, you can [create them based on AI suggestions](#topic_gr4_l5n_s2c).

**To create a use case manually**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Use cases**.
3. Click **Create use case**.

   The Use case window appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_use_case_create.png)
4. In **Name**, enter a short, descriptive name for the use case (for example, "Order status").
5. In **Customer request reason**, enter a short description that identifies why a customer is reaching out.

   For example, "Customer is asking for the status of their order."
6. In **Category**, select an existing category, or start typing to enter a new category and click **Add a category**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_use_case_category_new.png)

   Categories make managing use cases easier, but they don’t affect how an advanced AI agent connects use cases with a customer’s message (only use case names and descriptions do that).
7. (Optional) In **Status**, select **Inactive** if you don't want your advanced AI agent to begin detecting this use case yet.
8. Click **Create**.

Your use case is created, but it won't begin guiding an AI agent's responses until you perform the following steps:

- **For a zero-training AI agent**: [Create a reply associated with the use case.](https://support.zendesk.com/hc/en-us/articles/9624068102682#topic_i1v_nzx_jgc)
- **For an AI agent with agentic AI**: [Configure whether the use case should be associated with a dialogue or a procedure.](https://support.zendesk.com/hc/en-us/articles/9041911005850#topic_elk_mcf_52c)

## Creating use cases based on AI suggestions

As an alternative to [creating use cases manually](#topic_ik4_12r_mdc), you can create them based on AI suggestions. Suggestions are generated based on historical conversations in your advanced AI agent to create use cases specifically tailored to the needs of your customers.

This section contains the following topics:

- [Generating use case suggestions for the first time](#topic_lpg_h2w_3hc)
- [Regenerating use case suggestions](#topic_chc_j2w_3hc)

### Generating use case suggestions for the first time

If you haven't generated any use case suggestions before, follow the steps below to get started.

**To generate use case suggestions for the first time**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Use cases**.
3. Select the **Suggestions** tab.
4. Click **Generate suggestions**.

   The Generate use case suggestions window opens.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_use_case_suggestions_generate.png)
5. In **Report preset**, leave **Quick** selected, or else select **Custom** to expand the advanced settings.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_use_case_suggestions_generate_custom.png)
6. (Optional) In **Source**, select one of the following options:
   - **This AI agent**: Historical data from the AI agent you selected above. This data includes only messages that were classified as Not understood.
   - **Zendesk messaging**: (Available only for messaging AI agents.) Historical messaging conversations from your Zendesk account.
   - **Zendesk Support**: (Available only for email AI agents.)
     Historical email tickets from your Zendesk account. Messaging tickets are not included. This data includes all public comments on email tickets, but does not include private notes.
7. (Optional) In **Conversations sample**, select the number of messages that the system should analyze (**500**, **1000**, or **2000**).
8. (Optional) If you selected Zendesk messaging or Zendesk Support as your source, configure the following additional options:
   - **Group**: Enter the group from which conversations should be selected for analysis.
   - **Tag**: Enter the tag that conversations should have to be selected for analysis.
9. Click **Generate suggestions**.

   After a few minutes, a suggested use case report appears.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_use_case_suggestions_report.png)

   The banner at the top summarizes the following details:

   - **Conversations**: The number of analyzed conversations the suggested use cases apply to.
   - **Sample size**: The number of conversations the report analyzed.
   - **Suggestions**: The number of use case suggestions that were generated.
   - **Content coverage**: The estimated percentage increase in use case coverage for your customer conversations if you create the suggested use cases.
   - **Source**: The source you selected when generated the suggestions.
   - **Time frame**: The time frame the analyzed conversations occurred in.
   - **Last updated**: The last time the use case suggestions were generated.

   The following columns include the use case suggestions:

   - **Freq.** (Frequency): Shows the estimated percentage of analyzed conversations that a suggested use case applies to.
     The higher the frequency, the more important it is to create a use case that covers this topic.
   - **Use case**: Shows a name and description for a suggested use case.
   - **Conversations**: Shows the number of conversations that a suggested use case applies to.
10. (Optional) Click the icon in the **Conversations** column to open the [conversation logs](https://support.zendesk.com/hc/en-us/articles/8357749580186) for the relevant conversations.
11. For each suggested use case, accept it as is, edit it before accepting it, or reject it altogether:
    - To accept a suggested use case, click the checkmark.

      The use case is accepted and added to the Use cases tab.
    - To edit a suggested use case before accepting it, click the use case name to open it in a new window.
      1. Edit any of the details as needed.

         For help, see [Creating a use case manually](#topic_ik4_12r_mdc).
      2. Click **Accept suggestion**.

         The use case is accepted and added to the Use cases tab.
    - To reject a suggested use case, click the **X**.

      Rejected use cases aren’t suggested again the next time you generate use case suggestions.

After a use case is created, it won't begin guiding an AI agent's responses until you perform the following steps:

- **For a zero-training AI agent**: [Create a reply associated with the use case.](https://support.zendesk.com/hc/en-us/articles/9624068102682#topic_i1v_nzx_jgc)
- **For an AI agent with agentic AI**: [Configure whether the use case should be associated with a dialogue or a procedure.](https://support.zendesk.com/hc/en-us/articles/9041911005850#topic_elk_mcf_52c)

### Regenerating use case suggestions

If you've already generated some use case suggestions for an advanced AI agent, you can regenerate the suggestions to create use cases based on fresh data. Each time you generate suggestions, new use case suggestions are added to already-existing suggestions.

**To regenerate use case suggestions**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Use cases**.
3. Select the **Suggestions** tab.
4. (Optional) If you want to change the settings the system uses when generating the suggestions, click the arrow next to **Generate suggestions** and select **Configure report**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_use_case_suggestions_configure.png)

   Update the settings as needed. For help, see [Generating use case suggestions for the first time](#topic_lpg_h2w_3hc).
5. Click **Generate suggestions**.

   After a few minutes, an updated suggested use case report appears.
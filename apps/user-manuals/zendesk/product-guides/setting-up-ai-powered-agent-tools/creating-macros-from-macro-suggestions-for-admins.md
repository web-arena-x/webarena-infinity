# Creating macros from macro suggestions for admins

Source: https://support.zendesk.com/hc/en-us/articles/5217191091354-Creating-macros-from-macro-suggestions-for-admins

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Copilot |

Location: Admin Center > Workspaces > Agent tools > Macros >
Suggestions tab

Macros are a valuable tool that save agents time and help provide end users with consistent support. But knowing which macros to create isn't always straightforward. The macro suggestions feature makes it easier to determine which macros will be most useful for your agents and end users.

Tip: Macro suggestions and [suggested macros](https://support.zendesk.com/hc/en-us/articles/4408826078362) are different, though related, features:

- **Macro suggestions are suggestions made to admins** about new macros that could be created based on repeated content from all agent replies in your account.
- **Suggested macros are suggestions made to agents** about which existing macro to apply to a ticket based on the content of that specific ticket.

*Macro suggestions for admins (0:56)*

This article contains the following topics:

- [Understanding macro suggestions for admins](#topic_w12_xbq_dwb)
- [Configuring access to macro suggestions (Enterprise only)](#topic_bbz_z5z_bzb)
- [Creating a macro from a macro suggestion](#topic_fgd_ccq_dwb)
- [Dismissing a macro suggestion](#topic_zfj_dcq_dwb)

Related articles:

- [Using suggested macros](https://support.zendesk.com/hc/en-us/articles/4408826078362)
- [Creating macros for tickets](https://support.zendesk.com/hc/en-us/articles/4408844187034)

## Understanding macro suggestions for admins

The macro suggestions feature uses machine learning to scan the agent comments across all tickets in your account. This analysis identifies common replies that can be turned into useful macros for your agents.

If many agents repeat similar comments without using existing macros, you’ll receive suggestions to create new shared macros to help agents respond faster and more consistently in the future.

You can see a list of up to 10 macro suggestions in Admin Center. From the available suggestions, you can choose to [create new macros](#topic_fgd_ccq_dwb) that you can then publish for agents, or [dismiss suggestions](#topic_zfj_dcq_dwb) that seem irrelevant.

On the first day of each month, new macro suggestions are added to your account.
These macro suggestions are based on the previous month's data.

Each week, existing macro suggestions are refreshed based on the previous week's data. This refresh affects the macro's suggested text as well as information about the number of repetitions, unique agents, and example tickets.

### Criteria for macro suggestions

For the machine learning model to suggest a macro, your account must have received at least 150 tickets in the last 3 months. The model analyzes agent replies from the email and webform channels in your account that meet the following criteria:

- Tickets must be from end users and written in English, French, German, Japanese, or Portuguese.
- Tickets must have public comments written by an agent.

 Note: The machine learning model only analyzes public comments added by agents. Comments from admins and all internal notes are excluded.
- There are no existing macros similar to the one being suggested.

Any suggestion the model makes is always based on at least two comments from at least two different agents.

If a new suggestion is similar to an existing, unreviewed suggestion made within the last six months, the existing suggestion is updated with a new description, title, repetition, and agent count. If the existing suggestion is older than six months, a new suggestion is made, even if the previous one was rejected.

Most personally identifiable information (PII) is automatically masked in suggestions made by the machine learning model. If necessary, you can further edit the text of the macro when creating it.

## Configuring access to macro suggestions (Enterprise only)

By default, only admins can see macro suggestions in Admin Center. If you’re on an Enterprise plan, you can [edit a custom role](https://support.zendesk.com/hc/en-us/articles/4408882153882) and define whether that role has access to macro suggestions.

**To configure access to macro suggestions**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_people_icon.png)
   **People** in the sidebar, then select **Team > Roles**.
2. Hover over the custom role you want to edit.
3. In the **Macros permissions** > **Macro suggestion permissions** section, choose the level of access the custom role should have:
   - **No access**
   - **Can view macro suggestions**
   - **Can view and edit macro suggestions**

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_macro_suggestions_permissions.png)

## Creating a macro from a macro suggestion

In Admin Center, you can review the list of up to 10 suggested macros and decide which ones you want to create new macros for.

Tip: If you don't see any macro suggestions in Admin Center, see [Why don't I see macro suggestions?](https://support.zendesk.com/hc/en-us/articles/6114342158234) for help.

**To create a macro from a macro suggestion**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Macros > Suggestions** tab.

   The list of suggestions includes the following columns:

   - **Name**: The name of the macro suggestion.
   - **Repetition**: The number of times a similar comment was repeated by agents across your account. This helps you understand the potential impact of a new macro—the higher the number, the more time that could be saved by the new macro.
   - **Agents**: The number of unique agents who used a comment similar to the suggestion. This helps you understand how widely repeated the comment is among agents.
   - **Date created**: The date the macro was suggested in your account.
2. Click a suggestion name to open the **Suggestion** pane with more details.
   The pane includes the following information:
   - **The number of similar agent replies** over the last three weeks.
   - **Suggested groups that the macro should be made available to.** The suggested groups are based on the group membership of the agents who made the similar comments that prompted the macro suggestion.
   - **Suggested text for the new macro’s comment.** This text is based on similar comments repeated by agents. If you choose to create the macro, you can edit the text as needed afterward.
   - **The languages you should consider** creating the macro in.
   - **Example tickets that include the agent replies** the macro suggestion is based on. Click **Based on these replies** to see this information, then click **Show more** to open a full list of example tickets in a new tab in Support.
   - **The date the macro was suggested** in your account.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_macro_suggestions_agent_reply_examples_updated_2.png)
3. Click **Review suggestion**. You're automatically redirected to the macro creation page.
4. Adjust any details of the macro as necessary. For help with editing macros, see [Creating macros for tickets](https://support.zendesk.com/hc/en-us/articles/4408844187034).
5. When you’re finished, click **Create**.

## Dismissing a macro suggestion

Sometimes, the macro suggestions feature might suggest a macro you don’t want to create for whatever reason. You can remove it from the list of suggestions by dismissing it.

**To dismiss a macro suggestion**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_workspaces_icon.png)
   **Workspaces** in the sidebar, then select **Agent tools > Macros > Suggestions** tab.
2. Click a suggestion to open the **Suggestion** pane.
3. Click **Dismiss**.
4. In the list that appears, select the reason that best describes why you're dismissing the macro. If you choose **Another reason**, you have the opportunity to share additional details about your reason.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ai_macro_suggestions_dismiss_reason.png)

   By giving feedback, you help to improve the model so that future suggestions are more precise.
5. Click **Submit**. The macro suggestion no longer appears in the list.
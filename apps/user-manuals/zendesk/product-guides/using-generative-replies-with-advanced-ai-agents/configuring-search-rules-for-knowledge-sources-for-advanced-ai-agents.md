# Configuring search rules for knowledge sources for advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/9185497386394-Configuring-search-rules-for-knowledge-sources-for-advanced-AI-agents

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Search rules let you define which [knowledge sources](https://support.zendesk.com/hc/en-us/articles/8357749301658) (or parts of knowledge sources) an advanced AI agent should use in different situations when creating AI-generated answers to questions from your customers.

You must be a [client admin](https://support.zendesk.com/hc/en-us/articles/4408832171034#topic_thq_lnf_dgc) to configure search rules.

This article contains the following topics:

- [About search rules](#topic_kzl_wmy_cfc)
- [Creating a search rule](#topic_ar3_pxw_cfc)
- [Adding a search rule to a procedure](#topic_rvx_cx3_vfc)
- [Adding a search rule to a dialogue](#topic_pf1_xmy_cfc)
- [Editing the default search rule](#topic_qrq_xmy_cfc)

Related articles:

- [Importing knowledge sources for an advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357749301658)

## About search rules

In AI agents - Advanced, a default search rule is already configured for you. This default rule is configured so that the AI agent searches all articles from all imported knowledge sources when sending an AI-generated answer to a customer.

However, you can create additional search rules to customize which knowledge sources are searched in specific scenarios. For example, you can create search rules based on URL, locale, article labels, and [segments](https://support.zendesk.com/hc/en-us/articles/9413046533530) to customize the conversational experience.

When you create a search rule, you can specify which [segments](https://support.zendesk.com/hc/en-us/articles/9413046533530) should trigger it. You can also add the rule to a [procedure](https://support.zendesk.com/hc/en-us/articles/8979864563610) or [dialogue](https://support.zendesk.com/hc/en-us/articles/8357749494810) later. During a conversation with a customer, the search rule is applied when either of the following is true:

- A conversation’s session data matches the segment specified in the search rule.
- The conversation reaches the point in a procedure or dialogue where the search rule was added.

In either of these scenarios, the AI agent searches only the knowledge sources configured in your rule when forming its AI-generated reply.

Without a specific search rule applied, the default search rule is applied, which searches all knowledge sources unless you've [configured it differently](#topic_qrq_xmy_cfc).

## Creating a search rule

Search rule control which knowledge sources your AI agent should use to create an AI-generated answer in a specific situation.

**To create a search rule**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Knowledge**.
3. Select the **Search rules** tab.
4. Click **Create search rule**.

   The Create search rule window opens.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_create_search_rule_updated_Jun25.png)
5. In **Name**, enter a descriptive name for your search rule.

   This name appears only on the Search rules page to help you recognize and maintain your rules.
6. In **Description**, add a description for the rule to help you remember what it’s for and to allow the AI to understand the purpose of the rule.
7. In **Knowledge source**, select a [knowledge source that you’ve previously imported](https://support.zendesk.com/hc/en-us/articles/8357749301658).
8. (Optional) If you want this rule to search only a subset of the selected knowledge source:
   1. Select **Set filter criteria**.
   2. Leave **Match ALL conditions** selected, or else select **Match ANY conditions** to determine how the rule’s conditions should be evaluated.

      Note: It's important to make sure your conditions make logical sense together. If you select **Match ALL conditions** but your conditions conflict, no results will be returned.
   3. In **Select a parameter**, select **url**, **locale**, or **labels**.

      Note: Search rules based on labels don't work for Confluence knowledge sources.
   4. In **Equals**, select one of the available operators:
      **Equals**, **Does not equal**, **Contains**, **Includes any**, **Includes all**, or **Includes none**

      Note: If you're creating a search rule based on a single label, use Contains. If you're creating one based on multiple labels, use Includes any, Includes all, or Includes none.
   5. In **Add value**, enter the actual URL, locale, or article label (based on the parameter you selected above) that you want the rule to evaluate.
   6. (Optional) Click **Add condition** and repeat the previous three steps to add a new condition to filter the search rule.

      ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_search_rules_set_filter.png)
9. (Optional) Click **Add knowledge source** and repeat steps 7–8 to add and configure another knowledge source for this search rule.
10. Under Application criteria, in **When to apply**, select one of the following options:
    - **Only when referenced in procedures or dialogues**: The search rule applies only when it’s been specifically referenced in a [procedure](#topic_rvx_cx3_vfc) or [dialogue](#topic_pf1_xmy_cfc).
    - **When ALL segments match or when referenced**: The search rule applies when it matches *all* of the segments you select in the next step, or when it’s been specifically referenced in a procedure or dialogue.
    - **When ANY segment matches or when referenced**: The search rule applies when it matches *any* of the segments you select in the next step, or when it’s been specifically referenced in a procedure or dialogue.
11. If you selected When ALL or When ANY above, click Apply to segments and select which [segments](https://support.zendesk.com/hc/en-us/articles/9413046533530) should trigger the search rule.

    If a conversation’s session data matches one of the selected segments, the search rule is applied to any AI agent response that uses generative replies or agentic AI.
12. Click **Save**.
13. (Optional) Add your search rule to a procedure or dialogue following the steps below.

## Adding a search rule to a procedure

Note: This section applies only to [AI agents with agentic AI](https://support.zendesk.com/hc/en-us/articles/8966284087066).

You can add your search rule to a procedure to determine which knowledge sources your AI agent should use when providing an AI-generated answer.

**To add a search rule to a procedure**

1. [Open the procedure](https://support.zendesk.com/hc/en-us/articles/8979864563610#topic_qcm_tcc_tgc) you want to add a search rule to.
2. In the free-text box, enter text describing when your search rule should be applied.
3. Specify the search rule by entering a forward slash (/) and selecting **Share knowledge answer with search rule**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_add_search_rule_procedure.png)
4. Select the search rule you want to apply.
5. Click **Update procedure**.

## Adding a search rule to a dialogue

You can add a search rule to a dialogue to determine which knowledge sources your AI agent should use when providing a generative reply.

Search rules must be added to a [Generative replies block](https://support.zendesk.com/hc/en-us/articles/8357749315098) within a dialogue.

Tip: It’s good practice to use search rules in combination with [conditional blocks](https://support.zendesk.com/hc/en-us/articles/8357733406234). That way, you can ensure that the AI agent provides the most relevant and accurate answers to your customer’s queries based on parameters in the conversation session.

**To add a search rule to a dialogue**

1. [Open the dialogue builder](https://support.zendesk.com/hc/en-us/articles/9066753203738#topic_nvb_tzl_52c) for the dialogue you want to add a search rule to.
2. Select the Generative replies block where you want the search rule to apply.
3. Toggle **Use default search rule** off.
4. In **Select rule**, select the search rule you created.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_search_rules_ugpt_block.png)
5. Click **Publish**.

## Editing the default search rule

A default search rule exists for your AI agent already. This rule is configured to use all imported knowledge sources.

You can’t delete the default rule, but you can edit it if you want to configure a different default behavior. For example, you can edit it to use one specific knowledge source as the default.

Because the default search rule controls the AI agent’s *default* search behavior, it doesn’t have to match any segments or be added to a procedure or dialogue.

**To edit the default search rule**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Knowledge**.
3. Select the **Search rules** tab.
4. To the right of the **Default (Default)** search rule, click the options menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) and select **View**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_search_rules_default.png)
5. In the Edit rule pane, configure the default search rule as desired.

   For help, see [Creating a search rule](#topic_ar3_pxw_cfc).
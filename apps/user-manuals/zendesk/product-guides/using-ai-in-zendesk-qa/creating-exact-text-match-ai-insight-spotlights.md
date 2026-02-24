# Creating exact text-match AI insight spotlights

Source: https://support.zendesk.com/hc/en-us/articles/9486586566170-Creating-exact-text-match-AI-insight-spotlights

---

In addition tocustomizingandusing the standard spotlight insights, you can also create new ones. Custom spotlight insights work with text-based conversations and voice transcripts, automatically surfacing newly synced closed conversations by identifying and labeling specific keywords or phrases.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Create custom AI spotlight insights to automatically identify and label specific keywords or phrases in text-based conversations and voice transcripts. This feature helps you monitor important topics, like competitor mentions, and ensures agents are prepared for discussions. You can create up to 20 insights, with options to apply advanced filters for more precise results.

Location: Zendesk QA > Settings > AI

In addition to [customizing](https://support.zendesk.com/hc/en-us/articles/8992300083226) and [using the standard spotlight insights](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_u4j_rth_xdc), you can also create new ones. Custom spotlight insights work with text-based conversations and voice transcripts, automatically surfacing newly synced closed conversations by identifying and labeling specific keywords or phrases.

For example, if you want to highlight cases where either the agent or the customer mentions a direct competitor, you could create a spotlight insight named *'Competitor'* and provide a list of competitor names, product names, and features. These segments are valuable for review, as it is important to ensure your agents are well-equipped to discuss your brand.

Admins and account managers can create up to 20 custom spotlight insights. If you reach this limit, you must [deactivate](https://support.zendesk.com/hc/en-us/articles/9483275885466#topic_hm4_fcn_nfc) or [delete](https://support.zendesk.com/hc/en-us/articles/9483275885466#topic_tyq_fcn_nfc) a spotlight before creating a new one.

**To create an exact text-match spotlight insight**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right corner.
2. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_settings.png)).
3. In the sidebar under **Account**, click **AI**.
4. Click **Create AI insight**.
5. Select the **Exact text-match** AI insight type.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_ai_text_match_spotlight.png)
6. Enter an **AI insight name** and **Description for reviewers (optional)**.
7. Under **If** , select if you want to search only the **Agent message**, the **Client message** or **Any message**.
8. Select the operator (default: *contains*) and enter one keyword or phrase per row that you want to detect if they occur in messages. See [Exact text-match conditions](#topic_ytx_gcn_zfc).

   You can:

   - Click **Add row** for each additional keyword or phrase you want to autoscore in this category.
   - Click **Add condition** to specify more complex keywords and phrases.
   - Enter '/' to add the variable {..}. You can use this dynamic content placeholder {..} to represent any name. For example, “Competitor {··}”
9. Select **Use as a Spotlight**.
10. (Optional) Select **Apply advanced filters** to narrow down where your insight applies by:
    - Call direction: [inbound](https://support.zendesk.com/hc/en-us/articles/4408821359002) or [outbound](https://support.zendesk.com/hc/en-us/articles/4408836235162)
    - [Conversation brand](https://support.zendesk.com/hc/en-us/articles/4408829476378)
    - [Conversation channel](https://support.zendesk.com/hc/en-us/articles/4408824097050)
    - [Escalation](https://support.zendesk.com/hc/en-us/articles/7043759586074-Using-Zendesk-QA-Spotlight-insights-to-filter-conversations#topic_gst_d1g_zdc)
    - [Help desk tag](https://support.zendesk.com/hc/en-us/articles/4408881573658)
    - [Language](https://support.zendesk.com/hc/en-us/articles/7043759449114-Finding-conversations-to-review-using-custom-filters#h_4e27ce74b3)
    - [Sentiment](https://support.zendesk.com/hc/en-us/articles/7043759586074#topic_u4j_rth_xdc)
    - [Source type](https://support.zendesk.com/hc/en-us/articles/7043759449114#h_4e27ce74b3)
11. Click **Create Spotlight**.

## Exact text-match conditions

You can add multiple rows and use the following conditions for complex findings:

| | | | |
| --- | --- | --- | --- |
| **Condition name** | **Condition type** | **Search query example** | **Do you get a thumbs up as a result for this conversation message?****"Thank you for contacting Acme Corporation, how can I help you today?"** |
| is | is any of | "Thank you for contacting" "how can I help you today?" | No, because we look for entirely equal matches. |
| is all of | "Thank you for contacting Acme Corporation, how can I help you today?" "how can I help you today?" | No, although the first query matches, the second does not. |
| contains | contains any of | "Thank you for contacting us” “how can I help you today?" | Yes, because the second query is part of the message. |
| contains all of | "Thank you for contacting” “how can I help you today?" | Yes, because both queries are part of the message. |
| is not | is not any of | "Thank you for contacting us” “we are unavailable today?" | Yes, because neither of these queries are an exact match of the message. |
| is not all of | "Our business is closed" "Please contact us tomorrow" | Yes, because none of these queries are an exact match of the message. |
| does not contain | does not contain any of | "Our business is closed" "how can I help you today?" | No, because the second query is part of the message. |
| does not contain all of | "Thank you for contacting” “how can I help you today?" | No, because both queries are part of the message |
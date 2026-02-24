# Creating exact text-match AI insights rating categories

Source: https://support.zendesk.com/hc/en-us/articles/9302967236890-Creating-exact-text-match-AI-insights-rating-categories

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Quality Assurance (QA) or Workforce Engagement Management (WEM) |

Verified AI summary ◀▼

Create exact text-match AI insights to automatically evaluate messages based on specific keywords or phrases. This feature helps you maintain quality standards by scoring agent responses. You can set up to 20 categories, using conditions like "contains" or "is not" to refine your criteria. Once created, add these categories to your scorecards to start using them.

Location:  Zendesk QA > Settings > AI

Exact text-match categories use [autoscoring](https://support.zendesk.com/hc/en-us/articles/7043669430426#topic_wsw_cly_ydc) to identify specific keywords or phrases
and evaluate whether responses meet your quality standards.

Admins and account managers can create exact text-match custom rating
categories.

You can create up to 20 exact text-match AI insights per account. When you reach
this limit, you must either mark one as inactive or delete it before you can create or
activate more.

**To create an exact text-match category**

1. In [Quality assurance](https://support.zendesk.com/hc/en-us/articles/4408838272410), click your profile icon in the top-right
   corner.
2. Click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_settings.png)).
3. In the sidebar under **Account**, click **AI**.
4. Click **Create AI insight**.
5. Select the **Exact text-match** AI insight type.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_ai_text_match.png)
6. Enter an **AI insight name** and **Description for reviewers (optional)**. This is
   displayed when hovering over a category name while rating a conversation.
7. Under **If** , select if you want to search only the **Agent message**, the
   **Client message** or **Any message**.
8. Select the operator (default: *contains*) and enter one keyword or phrase per row
   that you want to score automatically if they occur in messages. See [Exact text-match conditions](#topic_gss_cyf_zfc).

   You
   can:

   - Click **Add row** for each additional keyword or phrase you want to autoscore in
     this category.
   - Click **Add condition** to specify more complex keywords and phrases.
   - Enter '/' to add the variable {..}. You can use this dynamic content placeholder
     {..} to represent any name. For example, “Hello {··}!”
9. Under **Then score** and **Otherwise score**, select how you want to automatically
   rate the agent. For example, if the text does not include “let’s schedule a demo,” the
   agent receives a negative (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_thumbs_dowm.png)) score for this category. Otherwise, you can choose
   to score them positively (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zqa_thumbs_up.png)) or [use "N/A" if unsure](https://support.zendesk.com/hc/en-us/articles/8875998154906#topic_ufd_t3n_zfc).
10. Select **Use as a category on a scorecard**.
11. Click **Create category**.
12. After creating it, you must [add the category to your scorecards](https://support.zendesk.com/hc/en-us/articles/7043760215194) to start using it.

## Exact text-match conditions

You can add multiple rows and use the following conditions for complex findings:

|  |  |  |  |
| --- | --- | --- | --- |
| **Condition name** | **Condition type** | **Search query example** | **Do you get a thumbs up as a result for this conversation message?** **"Thank you for contacting Acme Corporation, how can I help you today?"** |
| is | is any of | "Thank you for contacting"  "how can I help you today?" | No, because we look for entirely equal matches. |
| is all of | "Thank you for contacting Acme Corporation, how can I help you today?"  "how can I help you today?" | No, although the first query matches, the second does not. |
| contains | contains any of | "Thank you for contacting us”  “how can I help you today?" | Yes, because the second query is part of the message. |
| contains all of | "Thank you for contacting”  “how can I help you today?" | Yes, because both queries are part of the message. |
| is not | is not any of | "Thank you for contacting us”  “we are unavailable today?" | Yes, because neither of these queries are an exact match of the message. |
| is not all of | "Our business is closed"  "Please contact us tomorrow" | Yes, because none of these queries are an exact match of the message. |
| does not contain | does not contain any of | "Our business is closed"  "how can I help you today?" | No, because the second query is part of the message. |
| does not contain all of | "Thank you for contacting” “how can I help you today?" | No, because both queries are part of the message |
# Using generative search to provide AI-powered answers to search queries

Source: https://support.zendesk.com/hc/en-us/articles/8888178335898-Using-generative-search-to-provide-AI-powered-answers-to-search-queries

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Verified AI summary ◀▼

Generative search provides AI-generated answers to user queries in your help center, enhancing the search experience by displaying answers directly above search results. This feature uses your knowledge base content, so maintaining high-quality content is crucial. You can manage search settings and update themes to support generative search, which is available by default in standard themes released after March 26, 2025.

Generative search provides AI-generated answers to users' search queries in your help
center based on your content. Users can view generated answers without clicking through
search results or scanning related articles. However, users can still easily click into
the articles for more information, because the generated answer is derived from the
primary search results. Users can only view AI-generated answers for articles that they
have permission to view.

Generative search is available with all Zendesk Suite and Guide plans. All Zendesk Suite
and Guide plans include up to 100,000 eligible searches per month that produce
generative search results. If you exceed 100,000 searches, you can buy the Generative
Search Extender add-on to perform additional searches. See [Managing your generative search usage](https://support.zendesk.com/hc/en-us/articles/9234074974874).

Generative search is turned on by default. Knowledge admins can disable generative search, if
needed, by deactivating it in your [search settings](https://support.zendesk.com/hc/en-us/articles/5589418656922).

Note: Generative search is available by default in [standard themes](https://support.zendesk.com/hc/en-us/articles/4408845834522) released after March 26, 2025. If your
help center was created before March 26, 2025 and uses a customized theme, you must
[update your custom theme to add generative
search](https://support.zendesk.com/hc/en-us/articles/4408832681626#topic_tjl_xqc_42c). Generative search is available for all templating API
versions.

Note: Based on your theme implementation and other factors, you may be
eligible to use the automatic theme updater for generative search. To learn more, see
[Automatically updating your help center theme for
generative search (Beta)](https://support.zendesk.com/hc/en-us/articles/9809445946778).

This article includes the following sections:

- [About generative search for help center](#topic_lgj_cmr_w1c)
- [Updating your help center theme](#topic_axj_kyb_jgc)
- [Using generative search for help center](#topic_acg_knr_w1c)

## About generative search for help center

Generative search works by evaluating the question that a user enters in the help
center search. The top matching articles and posts are evaluated by generative AI,
which then generates an answer. On Enterprise plans with [federated search](https://support.zendesk.com/hc/en-us/articles/4593564000410) configured, the generative AI also
evaluates external content and can be included in the answer. The generated answer
is posted by default at the top of the search results.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-gensearch-search-results.png)

Generative search is activated by default in your help center. To deactivate this
feature, see [Viewing and managing your search
settings](https://support.zendesk.com/hc/en-us/articles/5589418656922).

The quality of a generated answer depends on the following:

- **Quality of your knowledge base**: Because generative answers are based
  on your help center and your external content, the quality of the answer
  depends on the quality of your knowledge base.
- **Search input**: Depending on the format and structure of the search
  query, you may not see a generated answer for every search. For the best
  results, avoid one- or two-word search queries, and instead, structure your
  search query as a phrase, sentence, or question. Additionally, if there are
  no articles, posts, or external content that match the search, an answer
  can't be generated.

## Updating your help center theme

To use generative search, your theme must include the {{generative\_answers}} helper.
Newer accounts already include this helper, but accounts with themes that were
customized prior to March 25, 2025 must add it.

For detailed information about how to update your custom theme for generative search,
see [Add generative search results to your custom
theme](https://support.zendesk.com/hc/en-us/articles/4408832681626#topic_tjl_xqc_42c).

Note: Your help center theme can't be
customized to remove the text stating the suggestion was generated using
AI.

## Using generative search for help center

When generative search is activated, users can enter questions or phrases in the help
center search field and receive AI-generated answers to their questions. Derived
from the top search results for their query, answers show users the information
they're looking for in the search results, without requiring them to open each link
and scan through the articles for an answer.

Generated search answers are posted in a box above the search results, alongside
buttons that let users provide feedback about how helpful the answer is. Providing
feedback helps train the AI to produce better answers in the future. You can also
improve the quality of your answers by enhancing the content in your knowledge base.
Generative search uses the content in your help center to produce answers, so as a
result, the answer is only as good as your content.

You can find information about [supported languages](https://support.zendesk.com/hc/en-us/articles/4408821324826#h_01K1KB596BQQJMETKX79QBC0WE) for generative search
in the Zendesk language support article.

**To use generative search for help center**

1. Enter a question or phrase in the help center search field and press
   **Enter**.

   The search page opens, displaying the search results
   and, if available, an AI-generated answer.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-gensearch-search-results.png)

   If there is not enough information for AI to generate an
   answer, you'll receive instructions to rephrase your search to sound
   more like a question or phrase. For example, the search query "What
   documents do we need to provide to create a joint account?" is more
   likely to generate an answer than the search terms "joint
   account."

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-gensearch-noquick-hc.png)
2. (Optional) Submit your feedback about the quick answer.

   Zendesk retains
   feedback for up to 90 days and uses it to assess and improve the quality
   of answers produced by generated search.

   - Click the thumbs-up icon ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gensearch-thumbsup.png) to indicate the answer was
     helpful.
   - Click the thumbs-down icon ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/gensearch-thumbsdown.png) to indicate the answer was
     not helpful. Select the reason that best matches the reason for your
     rating. Type any additional feedback you may have, then click
     **Submit feedback**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/GenSearch-feedback-neg.png)
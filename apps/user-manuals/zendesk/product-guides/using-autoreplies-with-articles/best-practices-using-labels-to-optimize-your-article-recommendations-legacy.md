# Best Practices: Using labels to optimize your article recommendations (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/4408883075098-Best-Practices-Using-labels-to-optimize-your-article-recommendations-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

As of July 31, 2025, the autoreplies with articles feature is considered legacy functionality. Instead, [use AI agents](https://support.zendesk.com/hc/en-us/articles/6478272212506) to deliver generative AI-powered responses on messaging, email, and web form channels.

You can use labels to help with targeting articles for your autoreply triggers. Adding labels to your triggers is optional. Labels enable you to specify a limited subset of articles that you want to search within for article recommendations.

![configure_autoreply_labels.png](https://support.zendesk.com/hc/article_attachments/7856559967386)

Without labels, autoreplies search all article titles and content to identify suggested articles. By adding labels in triggers, you can restrict the search to articles containing those labels.

When you use multiple labels in triggers, each label is handled separately using OR logic to suggest content.

This article covers three scenarios for using labels in triggers to better target suggestions in autoreplies with articles. For information on using autoreply labels in the Web Widget (Classic), see [Using APIs to configure autoreplies in Web Widget (Classic): Filtering article suggestions by label](https://support.zendesk.com/hc/en-us/articles/4408831077018#topic_whx_yl5_yhb).

## Scenario 1: Targeting customer segments

The most common scenario for when to use labels in triggers is when you have different customer segments and you want to show each segment only the relevant articles. For example, suppose you are a mobile game developer and you support both Android and iOS platforms. When you get a request from a customer who's using Android, you want to suggest only Android-related articles.

To accomplish this, create an "Android" autoreply trigger with the condition based on your custom field "Platform = Android." Then, configure the trigger using labels to include only articles that contain the "android" label.

Likewise, set up an additional trigger for the iOS platform and label.

Note: This scenario only applies to autoreplies with articles for email responses.

## Scenario 2: Reducing the "noise" in your Help Center

Your Help Center might contain a lot of articles, many of which you may never want to recommend to your customers.

In this case, review your articles and add a "use\_for\_autoreply" label to ~200-300 of the best articles. This will allow autoreplies to focus and only suggest articles that make sense.

## Scenario 3: Conducting a limited trial for a specific type of inquiry

While not recommended (it's a slippery slope), some customers have proven the value of autoreplies by focusing them on a specific type of inquiry, such as "password reset" requests.

By creating a trigger that looks for specific words in the subject/description, and then using labels to restrict the articles suggested, you can limit the pilot and get some quantitative data to help support a broader rollout.
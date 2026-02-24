# Using autoreplies to recommend articles in web forms (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/4408820951450-Using-autoreplies-to-recommend-articles-in-web-forms-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

As of July 31, 2025, the autoreplies with articles
feature is considered legacy functionality. Instead, [use AI agents](https://support.zendesk.com/hc/en-us/articles/6478272212506) to deliver generative AI-powered responses on
messaging, email, and web form channels.

For customers on legacy plans or with standalone Zendesk Support +
Guide, autoreplies might be called article recommendations.

When a user submits a support request through a web form on your help center, autoreplies
with articles can immediately suggest up to three links to potentially relevant knowledge base
articles.

This article discusses the following topics:

- [Understanding the end-user experience](#topic_l55_wjt_kcb)
- [Activating and configuring autoreplies with articles for web forms](#topic_plc_xjt_kcb)
- [Testing autoreplies with articles](#topic_hcq_lqt_kcb)

Related articles:

- [Using autoreplies to recommend articles in email
  notifications](https://support.zendesk.com/hc/en-us/articles/4408833721498)

## Understanding the end-user experience

With autoreplies with articles enabled on your web forms, when an end user makes a help
request through your help center, they receive a list of suggested articles that may help
them self-solve their issue. As soon as they submit their request, an automated pop-up
window appears.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/answer_bot_after_submit_request-richhtml.png)

In this window, the end user can:

- Preview the article. Expand the article section to view it in the pop-up
  window.
- Click the article title to view the complete article in your help center in a
  new tab. See below for more information on this option’s behavior.
- Click **No, I need help** if the suggested article did not help solve the
  problem, or click **Yes, close my request** if they were able to self-solve with the
  suggested article.
- View any videos embedded in the article.
- Close the pop-up window.

When the end user opens the article, it opens in a new tab, along with a pop-up window allowing
them to perform a number of related actions:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/answer_bot_view_full_article.png)

While viewing the full article, a modal appears allowing them to perform a number of
related actions, including:

- Clicking the **support request number** to view their help request in a new
  tab.
- Clicking **Yes, close my request** to close the help request. If the end user
  clicks this button, they should not expect to receive any more communication about the
  request.
- Clicking **No** to open an optional feedback window, asking for more information
  about why the article didn't help. If the end user clicks this button, the ticket will
  be handled as usual.

If an end user submits a request and autoreplies is unable to find any recommended
articles, then the automated pop-up window will not appear.

## Activating and configuring autoreplies with articles for web forms

Just as email allows you to manage the autoreply with articles trigger used to respond with
the suggested articles via email, web forms allow you to select and configure each web form
experience that will render the autoreply pop-up window on all help centers and brands
within your account.

If the web form provides suggestions on submission, any trigger that includes the
`Autoreply with articles` placeholders will *not* send an email with
more suggestions.

Note: In some older accounts, autoreplies are known as article
recommendations.

**To enable autoreply with articles in web forms**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click **Manage autoreplies**.
3. Click the **Web form** tab.
4. Toggle on **Web form channel enabled**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/autoreplies_webform_tab.png)

   This displays an expandable list of your
   brands and their related webforms.
5. Click each brand and use the toggles to determine which brands, and web forms, will
   use autoreplies with articles.

## Testing autoreplies with articles

You can use labels (as with email and triggers) to segment and refine the overall article
suggested in autoreplies for each brand and form. Read about the [best practices for using labels with autoreplies](https://support.zendesk.com/hc/en-us/articles/4408883075098).

**To configure and test article labels**

1. After activating autoreplies with articles for a web form, hover over the form name to
   display the **Configure and test** link.
2. Click **Configure and test** to open the testing modal.
3. Enter sample subject and description text to view the possible recommended articles
   for those terms.
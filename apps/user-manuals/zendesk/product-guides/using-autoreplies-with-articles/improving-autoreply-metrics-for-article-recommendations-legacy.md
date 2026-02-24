# Improving autoreply metrics for article recommendations (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/4408889123610-Improving-autoreply-metrics-for-article-recommendations-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

As of July 31, 2025, the autoreplies with
articles feature is considered legacy functionality. Instead, [use AI agents](https://support.zendesk.com/hc/en-us/articles/6478272212506) to deliver generative AI-powered responses on
messaging, email, and web form channels.

[Autoreplies metrics](https://support.zendesk.com/hc/en-us/articles/4409155069466-) are available to help you understand how autoreplies with
articles for email and web form are performing. Based on the metrics, you can update
your help center content to improve your suggestion rate, click-through rate, and resolution
rate, and decrease your rejection rate.

This article contains the following sections:

- [Improving your suggestion rate for autoreplies
  with articles](#topic_jj2_zvd_ybc)
- [Improving your click-through rate for
  autoreplies with articles](#topic_izg_bwd_ybc)
- [Improving your resolution rate for autoreplies
  with articles](#topic_tzb_cwd_ybc)
- [Decreasing rejection rate for autoreplies with
  articles](#topic_oyz_1yd_ybc)

Related article:

- [Optimizing your help center content](https://support.zendesk.com/hc/en-us/articles/4408845739162)

## Improving your suggestion rate for autoreplies with articles

The *suggest rate* is the percentage of questions that autoreply capability was active
for *and* has sent suggestions for. If the suggest rate is low, or lower than expected, it
can indicate that article labels are misconfigured or that you receive a larger-than-usual
number of questions from [unsupported languages](https://support.zendesk.com/hc/en-us/articles/4408846760346).

You can improve your suggest rate by taking the following actions:

- **Check your autoreply trigger notification body** (email autoreplies only). Your
  autoreply triggers require the placeholders `{{answer_bot.article_list}}` or
  `{{answer_bot.article_body}}`. If these placeholders are not present in the
  body of the email notification the trigger will still fire, but no articles will be
  suggested. This can cause the suggest rate to reflect inaccurately. [Learn more about configuring autoreply triggers](https://support.zendesk.com/hc/en-us/articles/4408825385242).
- **Check your article labels.** If you're using labels, this might be the cause of a
  lower suggest rate. Labels restrict which articles are searched. If relevant articles aren't
  in the restricted set, then no articles are suggested. This can cause the suggest rate to
  decrease. [Learn more about using labels with autoreplies](https://support.zendesk.com/hc/en-us/articles/4408883075098).

## Improving your click-through rate for autoreplies with articles

*Click-through* is the percentage of answers clicked by end users from the
total articles suggested.

Th click-through metric highlights a disadvantage of emailed autoreplies with articles because users must
first open and read the body of the email before they are likely to click through to any
articles.

You can improve your click-through rate by taking the following actions:

- **Make the subject line more appealing and accurate.** The email isn't just an
  acknowledgement email, it's got valuable content within it that may answer the user's
  question. Be clear about this in the subject line.
- **Don't hide the content.** It's important that you craft the body of your message with
  purpose. Use [conditional logic](https://support.zendesk.com/hc/en-us/articles/4408825385242) to craft a message to your users and
  make sure the `{{answer_bot.article_list}}` or
  `{{answer_bot.article_body}}` placeholders are positioned at the best place in
  the email body.

## Improving your resolution rate for autoreplies with articles

You can improve your resolution rate by taking the following actions:

- **Retain as much question context as possible.** If you can retain as much similar
  phrasing of the original question within the article, the contextual match will be better. For
  example, the question "I can't log in, so how can I reset my password?" should result in an
  article with the title "How do I reset my password so I can log in?"
- **Keep the article focused on a single problem.** Each article should focus on one
  problem and one solution only. If you have long FAQ articles, consider breaking the FAQs
  into separate articles and grouping them together in an FAQ section. Also, remember that
  there is greater emphasis on the first paragraph or two of the article (approximately
  the first 75 words in English), so be sure to include as much contextually-relevant
  information into the top of the article as possible.

## Decreasing your rejection rate for autoreplies with articles

You can decrease your rejection rate by making sure that your help center content is optimized
for bots and autoreplies with articles. There are two ways you can optimize your
content and decrease your rejection rate:

- **Write articles with a clear title, concise introduction, and narrow focus.**
  Article titles should be phrased as a question or a simple, active phrase. The intro
  should include keywords and context in the first 75 words, and the article should be
  focused on a single, specific topic.
- **Use article labels to filter results.** Labels can help reduce "noise" in your
  help center by focusing retrieval results on the articles you want to be considered.
  Labels can also help target customer segments by showing each segment only the relevant
  articles.

For more information, see [Optimizing your help center content](https://support.zendesk.com/hc/en-us/articles/4408845739162).
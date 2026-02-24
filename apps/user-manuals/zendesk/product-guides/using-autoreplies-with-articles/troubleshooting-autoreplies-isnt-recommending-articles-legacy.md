# Troubleshooting: Autoreplies isn't recommending articles (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/4408883039130-Troubleshooting-Autoreplies-isn-t-recommending-articles-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

As of July 31, 2025, the autoreplies with articles feature is considered legacy functionality. Instead, [use AI agents](https://support.zendesk.com/hc/en-us/articles/6478272212506) to deliver generative AI-powered responses on messaging, email, and web form channels.

If autoreplies isn't returning any recommended articles, it may be caused by one of the following reasons:

- [Your trigger conditions aren't being met](#conditions_not_met)
- [The ticket is not in a supported language](#unsupported_language)
- [There are no relevant results](#no_results)
- [You've added article labels to limit the autoreplies search](#whitelisted_labels)
- [Your content is restricted](#access_rights)
- [There are no results for follow-up tickets](#no_followup)
- [The article recommendations already show on the contact form](#h_01H066PPXKAH1AVYB9RYK572NT)
- [A race condition between multiple triggers causes conflicts](#h_01JT6N15RP041CVR0XQD5FTTYN)

## Your trigger conditions aren't being met

Some triggers have the condition *Ticket: Status is New*. However, in some cases new tickets can be created with the status *Open* which prevents the autoreply trigger from firing. Double- and triple check all the conditions set on the trigger to make sure that the actual trigger is firing correctly.

**Pro tip**: Adding a tag when the autoreply trigger fires will ensure that it shows up in the ticket's Events, in the comment stream. If that tag is not being added to the ticket, then the trigger hasn't fired and you can continue debugging why.

## The ticket is not in a supported language

Any tickets from an unsupported language will either get no results, or potentially have articles in a supported language suggested. See the list of [languages supported](https://support.zendesk.com/hc/en-us/articles/4408846760346).

## There are no relevant results

If there are truly no close article matches relevant to the ticket content, autoreplies won't suggest any articles at all. Make sure that you have relevant, matching articles that should be suggested. Include commonly-used words in the article title and text to boost an article's suggestion chances.

## You've added article labels to limit the autoreplies search

You can [restrict the articles suggested](https://support.zendesk.com/hc/en-us/articles/4408883075098#ab_labels) by "allowing" access to only articles using a particular label. This function is extremely useful, but if used incorrectly it can cause situations where no articles are found. Double check your labels and remove any that aren't needed.

## Your content is restricted

Remember that autoreplies always considers the requester's access rights. As an admin, you will be able to see all articles within the configure and test tool. Just remember that autoreplies will only ever send articles to requesters that they have access to. This can create situations where no articles are suggested because they are all restricted in some way to that requester.

Note that when autoreplies is included as part of an answer flow for a conversation bot, it is configured in bot builder and may behave differently. See [Understanding answer flow step types: Show help center articles](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_grj_gwc_k4b) for more information.

## There are no results for follow-up tickets

Autoreplies has been specifically disabled for follow-up tickets.

## The article recommendations already show on the contact form

If you've configured your Help Center web form form to dynamically display article recommendations, any related bot placeholders from email notification triggers are suppressed. This prevents users from receiving the same list of recommended articles via email after just viewing the list on the web form.

## A race condition between multiple triggers causes conflicts

When multiple triggers fire on a ticket, a race condition between the triggers might cause conflicts that prevent autoreplies from recommending articles. For example, if you have one trigger that sets the brand and another that sends the autoreply, a race condition between the two triggers might mean that the autoreply is sent for the wrong brand.
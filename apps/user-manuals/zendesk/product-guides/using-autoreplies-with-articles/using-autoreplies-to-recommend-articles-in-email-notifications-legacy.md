# Using autoreplies to recommend articles in email notifications (Legacy) 

Source: https://support.zendesk.com/hc/en-us/articles/4408833721498-Using-autoreplies-to-recommend-articles-in-email-notifications-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

As of July 31, 2025, the autoreplies with articles
feature is considered legacy functionality. Instead, [use AI agents](https://support.zendesk.com/hc/en-us/articles/6478272212506) to deliver generative AI-powered responses on messaging,
email, and web form channels.

Autoreplies with articles are automated responses to customer support requests sent via email,
that include up to three recommended articles from your help center. These responses use the
autoreply with articles trigger action to identify relevant articles and add them to your
notification email.

This article includes the following topics:

- [Understanding the end-user experience](#topic_wwy_znk_jhb)
- [Setting up autoreplies with articles for email notifications](#topic_llx_14k_jhb)
- [Testing email notification results](#topic_wgc_b4k_jhb)

Related articles:

- [Using autoreplies to recommend articles in web forms](https://support.zendesk.com/hc/en-us/articles/4408820951450)

## Understanding the end-user experience

When you configure autoreplies with articles for email notifications, the end user receives an
automated email response to their support request. The email includes a list of recommended
articles, along with other information provided by the placeholders used in the
`autoreply with articles` trigger action.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/answerbot_email-callout.png)

In the email, the end user can read the top suggested article in its entirety, and click any
of the following options:

- **Suggested article links** opens the help center article in a new tab. From there, the
  user can read the article, click to see their help request, and indicate whether it helped them
  answer their question:

  ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/answer_bot_in_article_popup1.png)
- **Request number** opens the request in a new tab.
- **Yes, close my request** opens the article in the help center and close the help
  request.
- **No** opens a feedback screen requesting more information about why the article didn't
  help. This screen is optional for the end user.
- **Yes, close my request** on any of the suggested articles opens the article in the help
  center and closes the help request.
- **No** beneath the top article opens an optional feedback window asking for more
  information about why the article didn't help.

End users can return to the email and access the links as often as they like. Suggested
articles are sent in the language defined in the end user's profile, when available.

## Setting up autoreplies with articles for email notifications

Before you can set up autoreplies, you need a [help center
with articles](https://support.zendesk.com/hc/en-us/articles/4408846795674) that can address your customers' questions. When your help center is
ready, you can turn on autoreplies.

To send a list of recommended articles, your email notification triggers must include the
`Autoreply with articles` action. You can add this action to existing triggers,
such as the default [Notify requester and CCs of received request](https://support.zendesk.com/hc/en-us/articles/4408828984346#topic_ksk_znr_5t) and [Notify requester of new proactive ticket](https://support.zendesk.com/hc/en-us/articles/4408828984346#topic_zh3_wx5_d3b). See [Managing triggers](https://support.zendesk.com/hc/en-us/articles/4408882237722).

Autoreply triggers can run at any time, but will run only once on a ticket.

**To set up autoreplies with articles for email notifications**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click **Manage autoreplies**.
3. Click **Get started with autoreplies**. If autoreplies are already activated, this
   option doesn't appear. You can stop at this step and create your triggers later – autoreplies
   with articles will not be sent until you create the trigger.
4. Click **Create triggers**. An admin page to create a new trigger opens.
5. Configure the trigger conditions for requests submitted via email. For example:

   - Ticket > Ticket | Is | Created
   - Requester > Role | Is | (end-user)
   - Ticket > Channel | Is | Email
6. Next, configure the trigger action. The action needs to include `Notify by >
   Autoreply with articles | (requester)` to establish that all tickets meeting the
   conditions will send your autoreply email to the ticket requester. The autoreply email field
   appears:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/autoreply_wirth_articles_action.png)
7. Fill out the email subject and body text to include in the autoreply email. Use the
   placeholders listed below to customize the email text.
   - **{{autoreply.article\_list}}** (required). You must include this placeholder for the
     feature to work. This placeholder adds a list of up to three articles that best match the
     request, links to those articles, and inserts buttons the end user can use to choose which
     article solved the request.

     Note: This placeholder includes two pieces of text that are
     determined by the user's profile language: The header *Do any of these articles answer
     your question?*, and the two buttons located underneath each suggested article *Yes,
     close my request* and *View article*.
   - **{{autoreply.first\_article\_body}}** (optional). This placeholder renders the first
     matching article (full HTML) into the email body, allowing end users to read the article and
     solve their problem without needing to leave the email experience.
   - **{{autoreply.article\_count}}** (optional). This placeholder allows you to create an
     optional condition to send different body copy to customers based on how many articles are
     returned, for example:

     ```
             {% if autoreply.article_count > 0 %}
         Here are some great articles that may help:
         {{autoreply.article_list}}
         {{autoreply.first_article_body}}
     {% endif %}
     ```
8. In the section **Configure labels and test autoreply**, click **Configure and test**
   to filter the list of help center articles offered based on [labels](https://support.zendesk.com/hc/en-us/articles/4408845739162#topic_bdk_l1k_jhb):

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/configure_labels_and_test_autoreply.png)

   - **Ticket brand**: Select a brand to run the test on. The brand selected here is
     purely for testing purposes, and will not be added to the trigger you are creating.
   - **Ticket subject**: Enter a subject to test the articles returned when a ticket is
     filed with this subject.
   - **Ticket description**: Enter a short description of seven or more words, written
     from the ticket submitter's perspective.
   - **Search articles by label** (optional): Enter any [article labels](https://support.zendesk.com/hc/en-us/articles/4408835056154)you want to use to filter the results. As you type
     into the tag field, available labels beginning with the same word or characters are
     displayed. Any articles with the selected labels are considered in autoreplies.
9. Click **Show suggested articles** for a list of articles the user may receive if these
   labels are applied when submitting a similar ticket. If the results are acceptable, click
   **Done** to save the trigger. If the results are not acceptable, edit the entries and try
   again, or click **Cancel**.
10. Click **Create** (if you're creating a new trigger) or **Save** (if you're updating
    an existing trigger).

## Testing email notification results

**To test autoreply results**

1. [Create a new autoreply with articles
   trigger](#topic_llx_14k_jhb), or open an existing trigger already configured for autoreplies with articles.
2. At the bottom of the Actions section on the trigger's edit page, click the **Configure and
   test** button.
3. In the testing window, fill out the
   following information:

   - **Ticket brand**: Select a brand to run the test on. The brand
     selected here is purely for testing purposes, and will not be added to the trigger you are
     creating.
   - **Ticket subject**: This field is used to test the articles returned when a ticket is
     filed with this subject.
   - **Ticket description**: Enter a short description of seven or more words, written from
     the ticket submitter's perspective.
   - **Search articles by label** (optional): Enter any [article labels](https://support.zendesk.com/hc/en-us/articles/4408835056154) you want to use to filter the results. As you type
     in the field, available labels beginning with the same word or characters are displayed. Any
     articles with the selected labels are considered in autoreplies.
4. Click **Show suggested articles** to display a list of articles your user might receive
   in an email notification, for a ticket with the labels and ticket information applied.
5. If the results are acceptable, click **Done** to save the trigger. If the results are
   not acceptable, edit the entries and try again, or click **Cancel**.
# Enabling article recommendations in Web Widget (Classic)

Source: https://support.zendesk.com/hc/en-us/articles/4408843471642-Enabling-article-recommendations-in-Web-Widget-Classic

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

This functionality is part of [AI agents](https://support.zendesk.com/hc/en-us/articles/6970583409690).

You can add article recommendations wherever you've implemented Web Widget (Classic). For Zendesk
Chat customers, this also allows for a fluid and consistent self-service experience
prior to a chat escalation, freeing up your Chat and Support agents to focus on the
customer service issues that require a human touch.

Note: Bot functionality is different
for web messaging users. See
[Enabling a messaging bot for web and mobile
channels](https://support.zendesk.com/hc/en-us/articles/4408824263578).

This article discusses the following topics:

- [Understanding the end user
  experience](#topic_zhd_rjy_xhb)
- [Enabling article recommendations
  in Web Widget (Classic)](#topic_w25_qjy_xhb)

Related articles:

- [Using APIs to configure autoreplies in Web
  Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408831077018)
- [Zendesk bot resources](https://support.zendesk.com/hc/en-us/articles/4408834322842)
- [Web Widget (Classic) resources](https://support.zendesk.com/hc/en-us/articles/4408833907354)

## Understanding the end user experience

When article recommendations are enabled for the Web Widget (Classic), your end user's
experience with the widget changes. This section describes the workflow an end user may
experience.

When an end user clicks on the Web Widget (Classic) launcher, instead
of the standard text entry search box, they'll see a chat window, and a greeting from
the bot:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ab_widget_greeting.png)

The bot uses the
current brand's name in its initial greeting.

After the initial greeting, the workflow
depends on the action taken by the end user.

**If the end user enters a question
(within 10 seconds)**

1. The end user enters their question in the text box. They can use conversational
   language, as if they were chatting with a live agent, or use keywords.
2. The bot responds with article recommendations, a list of up to three articles that
   may be helpful, based on your article settings:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ab_article_list.png)
3. From here, the end user's path can go in a few directions:
   - If the end user **clicks on any of the suggested article links**, that help
     center article opens in the chat window. After three seconds, a feedback
     notification appears at the bottom of the window:

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ab_suggested_article.png)

     - **Yes** closes the feedback notification, and the article remains on the
       screen.

       The end user can return to the conversation by clicking the
       **Back arrow** at the top of the chat window.
     - **No, I need help**, opens a second feedback notification, asking for
       further information.

       ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ab_y_no_ok.png)

       After selecting an answer, the end user is returned to the
       conversation, where the bot presents a list of contact channels and the
       option to enter another question.

       ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ab_not_help_contact_options.png)

       The contact channels offered depend on [how your Web Widget (Classic) components are
       configured](https://support.zendesk.com/hc/en-us/articles/4408838063258). The end user can click on one of the channel options to
       open that channel in the widget.

       Note: If the end user
       clicked on at least one article preview link or clicked “Yes, problem
       solved,” an [automated resolution is counted](https://support.zendesk.com/hc/en-us/articles/5352026794010#topic_p4p_zqr_y1c).
       When this happens, a ticket is created for tracking purposes with a
       requester called *End user*, no assignee, and a tag called
       *ai\_agent\_automated\_resolution*. The *End user* profile cannot
       be edited or deleted.
   - If the end user **does not click on any of the suggested article links**
     within five seconds, they are returned to the conversation, where the bot presents
     a list of contact channels and the option to enter another question.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ab_no_click_contact_options.png)

     The
     contact channels offered depend on [how your Web Widget (Classic) components are
     configured](https://support.zendesk.com/hc/en-us/articles/4408838063258). The end user can click on one of the channel options to
     open that channel in the widget.

**If the end user remains idle**

1. After the initial greeting, if the end user does not interact with the conversation
   within 10 seconds, the bot suggests a list of contact channels. The contact channels
   offered depend on [how your Web Widget (Classic) components are configured](https://support.zendesk.com/hc/en-us/articles/4408838063258).

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ab_idle_contact_options.png)
2. The end user can click on one of the channel options to open that channel in the
   widget, or can enter a question, which launches the workflow [described above](#topic_zhd_rjy_xhb__ol_ixk_ykt_yhb).

## Enabling article recommendations in Web Widget (Classic)

Enabling article recommendations for the Web Widget (Classic) requires changing Web
Widget (Classic) admin settings.

**To enable article recommendations for the Web Widget (Classic)**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Classic > Web Widget**.
2. Click the
   **Basics**
   tab. If you have multiple brands, select the widget for
   the brand you want to use with the conversation bot, then click
   **Basics**.
3. Select the
   **Help Center** checkbox and then select the
   **Article
   Recommendations**
   checkbox. If you have Contextual Help enabled for the
   widget, it will be disabled.
4. At the bottom of the widget settings, click
   **Save**.
5. Repeat steps 2-5 for each brand you want to use with article
   recommendations.

After you complete these steps, the conversation bot appears in the Web Widget in
your help center. If needed, you can now configure additional bot functionality
using the API (see
[Using APIs to configure autoreplies for Web Widget
(Classic)](https://support.zendesk.com/hc/en-us/articles/4408831077018)).
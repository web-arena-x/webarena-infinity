# About Contextual Help for the Web Widget (Classic)

Source: https://support.zendesk.com/hc/en-us/articles/4408824357402-About-Contextual-Help-for-the-Web-Widget-Classic

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Contextual Help is a Web Widget (Classic) feature that uses the web page your visitor is currently on, along with your help center content, to suggest help center articles that may be relevant to their questions. Its goal is to reduce the effort required by an end user who may be trying to self-serve by suggesting contextually relevant articles.

This article includes the following topics:

- [Enabling Contextual Help](#topic_r1g_p2g_bw)
- [Understanding how Contextual Help works](#topic_obg_q2g_bw)
- [Customizing Contextual Help results](#topic_hvh_p3g_bw)

## Enabling Contextual Help

Before you can enable Contextual Help, make sure you meet the following requirements:

- You have public help center content (one that does not require sign-in).
- [Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408836216218) is installed on your website.
- You have enabled the help center option in the widget admin.

**To enable Contextual Help**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Classic > Web Widget**.
2. Click the **Customization** tab.
3. Make sure that Help Center is toggled on.
4. Click the toggle to enable Contextual Help.

## Understanding how Contextual Help works

The Contextual Help feature determines which articles should be suggested by looking at URL of the web page the end user is on It then uses the part of the URL after the hostname (that is, the part after *.com*, *.org*, etc.) to perform a search on your help center to find relevant articles, and displays the first three results as **Top suggestions**. Community posts are not included in the suggested articles list.

For instance:

- If an end user is viewing the page *myshop.com/apps*, the suggested articles will include the first three results of a help center search on the term "apps".
- If an end user is viewing a page deeper in your website, for instance *myshop.com/account/billing*, the suggested articles will include the first three results of a help center search on the term "account billing".
- If no articles match the search term, just the search box is displayed in the widget.

Note: Contextual Help is disabled for the Web Widget (Classic) inside of help center because any suggestions would return the article the user is currently viewing. You can manually set suggestions using the Zendesk API, see [Customizing Contextual Help results](#topic_hvh_p3g_bw) (below).

## Customizing Contextual Help results

If your URL paths are not likely to produce useful suggestions, or if you just want more control over the results, you can override the search by utilizing one of our SetHelpSuggestions API methods.

For information on customizing your results, visit our [Web Widget (Classic)
Developer Documentation](https://developer.zendesk.com/embeddables/docs/widget/help_center#helpcentersetsuggestions).
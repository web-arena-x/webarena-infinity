# Suggesting restricted help center articles in an AI agent answer (Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/5503198227738-Suggesting-restricted-help-center-articles-in-an-AI-agent-answer-Legacy

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

This article describes functionality available only
to customers who had a drafted or published AI agent as of February 2, 2025.
For information about equivalent functionality in the [AI agents - Advanced add-on](https://support.zendesk.com/hc/en-us/articles/6970583409690), see
[Building dialogues for AI agents -
Advanced](https://support.zendesk.com/hc/en-us/sections/8264324615322).

Bot builder’s [Show help center articles](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_grj_gwc_k4b) step recommends specific
help center articles to your customers that may help them self-solve their
questions. If you have public *and* restricted articles in your help center,
you can configure which articles to show anonymous (unauthenticated) end users and
which to show for authenticated end users.

Suggesting restricted help center articles in an AI agent answer is available on all plans that
can use messaging.

This article includes the following topics:

- [Restricted help center article overview](#topic_kth_jxs_wxb)
- [Showing the title of restricted help center articles](#topic_vbc_zys_wxb)
- [Searching for restricted help center articles](#topic_pwb_4zs_wxb)

## Restricted help center article overview

There are three use cases for AI agents and articles:

- The AI agent handles anonymous user queries and shares
  public help center articles
- The AI agent handles authenticated user queries and
  shares restricted help center articles
- The AI agent handles anonymous and authenticated user
  queries, builds conditions based on whether the user
  is authenticated, and shows all articles to
  authenticated users and only public articles to
  unauthenticated users

Authentication is based on
[messaging authentication with
JWT](https://support.zendesk.com/hc/en-us/articles/4411666638746/).

If the end user is authenticated with messaging JSON Web Token (JWT), we will
check if they can access the article based on the article permission rules
and the
[user segment](https://support.zendesk.com/hc/en-us/articles/4408837707290)
they’re part of. If
the end user has access, the article preview is shown. Only the placeholder
preview is shown if the end user is not part of the user segment.

If the end user is anonymous or authenticated through SSO or Zendesk authentication, the link to
the restricted article is displayed in the AI agent message, but
the title and preview are not displayed.

When the end user clicks the link to the restricted article, they are redirected to the help center sign-in page. An end user must have an account on your
help center and the correct [user permissions](https://support.zendesk.com/hc/en-us/articles/4408827797274) to view the
restricted article.

Note: If the article
permission is updated from public to restricted or from
restricted to public, there is a short delay before the
permission change is reflected to the end user.

## Showing the title of restricted help center articles

By default, restricted help center article titles and previews are not shown to users
not authenticated with messaging JWT. Only the link is shown.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/user-restricted-article-view.png)

You can, however, configure your AI agent to show the title and preview of restricted help center
articles to all users, regardless of which authentication method is used or
whether they are anonymous.

Note: Before configuring the AI agent to show restricted titles, you need to
[set up end-user authentication
for messaging](https://support.zendesk.com/hc/en-us/articles/4411666638746).

**To always show the title for restricted help center articles**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/icon_ai.png)
   **AI** in the sidebar, then select **AI agents > AI agents**.
2. Click the AI agent you want to work with.
3. Expand **Channels** settings and select **Always show the title and preview for restricted
   articles**. This option is visible only if you have an
   active help center. Only agents with [Knowledge admin permissions](https://support.zendesk.com/hc/en-us/articles/4408827842458) can
   set this option.

## Searching for restricted help center articles

The
[Show help center articles](https://support.zendesk.com/hc/en-us/articles/4408836323738#topic_grj_gwc_k4b)step recommends
specific articles to your customers that may help them self-solve their questions.
It presents up to six help center articles to the customer during a
conversation.

You must have an active help center to use this step.

If you have view access to a restricted article, you can add that article in bot builder and see
the article preview. The article does not appear in the bot builder search
results if you do not have view access. If, for example, a Knowledge admin
adds a restricted article and you do not have view access for that article,
it appears as a restricted article in bot builder for you.
# Understanding the semantic search roll out plan

Source: https://support.zendesk.com/hc/en-us/articles/6675063083418-Understanding-the-semantic-search-roll-out-plan

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

As Zendesk expands its AI model to cover more search channels, [semantic search](https://support.zendesk.com/hc/en-us/articles/5633225532826) will continue to be rolled
out into additional areas.

You can use the information in this article to better understand the rollout plan and how to
determine whether semantic search is enabled in your help center. If it is not yet enabled,
you can determine the rollout status, based on your content type, language, and search
channel.

This article contains the following sections:

- [How to check if your help center is enabled for semantic search](#topic_h42_c1y_3xb)
- [Understanding the rollout plan](#topic_bxx_h2z_gxb)

## How to check if your help center is enabled for semantic search

The semantic search implementation has started. As the rollout continues, it will
expand to all customers. You can use this procedure to determine whether your help center is
currently enabled for semantic search.

**To check whether your help center is enabled for semantic search**

1. [Perform a search](https://support.zendesk.com/hc/en-us/articles/4408894061338) in your help center.
2. On the search results page, open **Inspect element** in your browser.

   For
   example, in Chrome, right-click the search results page, select **Inspect** from
   the menu, then click the **Elements** tab.

   [View full size](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-semantic-search-search-term.png)![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-semantic-search-search-term.png)
3. Select the <head> tag, then examine the
   `guide_search/semantic_search_enabled` element.

   If the element is set
   to "false" (as shown in the image below), semantic search is not yet enabled in your
   help center. If the element is set to "true," then semantic search is
   enabled.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-sem-search-tool-head-050423.jpg)

## Understanding the rollout plan

As the Zendesk AI model expands to cover more search channels, semantic search will continue to be rolled out into additional areas. Specifically, the semantic search rollout will be
phased into content type, search type, search channel, and language.

If semantic search is not enabled in your environment, you can refer to the
following tables to understand the coverage status for each area.

For example, let's say your help center has the following characteristics:

- **Content type**: Articles, community posts, and external content
- **Help center search type**: Uses two-pane search
- **Search channel**: Uses help center search engine results page and
  knowledge in agent workspace
- **Language**: English and French

You can use the rollout tables to understand that while your content type and
help center search type are supported, only one of your two search channels is currently
supported by semantic search (search engine results). Knowledge in agent workspace is not
currently supported, but is planned, and will be supported in the future.

In addition, only one of your two help center languages is supported, English.
Your French help center content is not yet supported by semantic search, but will be in the
future.

## Rollout by content type

See the following table for the coverage status for each content type. Possible
coverage statuses include:

- **Covered**: Currently supported by semantic search
- **Planned**: Not yet supported by semantic search, but planned for a future
  release

| Content type | Coverage status |
| --- | --- |
| Articles | Covered |
| Community posts | Covered |
| External content | Covered |

## Rollout by help center search type

See the following table for the coverage status for each content type. Possible
coverage statuses include:

- **Covered**: Currently supported by semantic search
- **Planned**: Not yet supported by semantic search, but planned for a future
  release

| Help center search type | Coverage status |
| --- | --- |
| Two-pane search | Covered |
| Unified search | Covered |
| Federated search | Planned |

## Rollout by search channel

See the following table for the coverage status for each content type. Possible
coverage statuses include:

- **Covered**: Currently supported by semantic search
- **Planned**: Not yet supported by semantic search, but planned for a future
  release
- **Will not be supported**: Not supported by semantic search

| Search channel | Coverage status |
| --- | --- |
| Help center search engine results page (SERP) | Covered |
| Instant search | Planned |
| Request from article suggestions | Planned |
| Unified search API | Planned |
| Articles search API | Will not be supported |
| Posts search API | Will not be supported |
| Web Widget help center search | Planned |
| Knowledge in Agent Workspace | Planned |

## Rollout by language

See the following table for the coverage status for each content type. Possible
coverage statuses include:

- **Covered**: Currently supported by semantic search
- **Planned**: Not yet supported by semantic search, but planned for a future
  release
- **Not planned:** Not supported by semantic search, and not currently
  planned for a future release

| Language | Coverage status |
| --- | --- |
| Arabic | Covered |
| Bulgarian | Covered |
| Catalan | Covered |
| Croatian | Covered |
| Czech | Covered |
| Danish | Covered |
| Dutch | Covered |
| English (all variants) | Covered |
| Finnish | Covered |
| French (all variants) | Covered |
| German | Covered |
| Greek | Covered |
| Hebrew | Covered |
| Hindi | Covered |
| Hungarian | Covered |
| Icelandic | Not planned |
| Indonesian | Covered |
| Italian | Covered |
| Japanese | Covered |
| Korean | Covered |
| Latvian | Covered |
| Lithuanian | Covered |
| Norwegian | Covered |
| Persian | Covered |
| Polish | Covered |
| Portuguese (Brazil) | Covered |
| Romanian | Covered |
| Russian | Covered |
| Serbian | Covered |
| Simplified Chinese | Covered |
| Slovak | Covered |
| Slovenian | Covered |
| Spanish | Covered |
| Swedish | Covered |
| Thai | Covered |
| Traditional Chinese | Not planned |
| Turkish | Covered |
| Ukrainian | Covered |
| Urdu | Not planned |
| Vietnamese | Covered |

Note: It may not be possible to support some languages with semantic
search if there is insufficient data available to train the model.
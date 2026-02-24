# Knowledge product limits for your help center

Source: https://support.zendesk.com/hc/en-us/articles/4408831783962-Knowledge-product-limits-for-your-help-center

---

This article details the maximum product limits in Knowledge.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Verified AI summary ◀▼

This article outlines the limits for your help center's knowledge base, content blocks, search, federated search, management permissions, user segments, and themes. Understanding these limits helps you manage content effectively, ensuring optimal performance and security. Limits include article size, number of articles, search queries, and theme assets. These constraints are designed to maintain security, prevent misuse, and enhance performance.

This article details the maximum product limits in Knowledge.

Note: The limits in this article apply to all plans, except where noted.

This article covers the following topics:

- [Knowledge base limits](#topic_tq3_24g_3jb)
- [Content blocks limits](#topic_vky_znm_mpb)
- [Search limits](#topic_syc_yth_lhb)
- [External content limits](#topic_ndw_vxj_ytb)
- [Management permissions and user segment limits](#user-segment)
- [Theme limits](#topic_cnb_vnd_dcb)
- [Why are there limits?](#topic_rth_tzd_dcb)

## Knowledge base limits

The following table shows the maximum limits related to knowledge base functionality in Knowledge.

| Item | Maximum |
| --- | --- |
| Article size | 1MB per translation For example, the source language article is limited to 1MB, as is each additional translation. This translates to approximately 1,000,000 characters (excluding *āăą* or hidden html tags). |
| Token limit for each [AI-generated translation](https://support.zendesk.com/hc/en-us/articles/8717609637018) | 32,768 tokens (or roughly 24,576 words, including HTML tags) Tokens are the units of text processed by the OpenAI model. For more information, see OpenAI's article [What are tokens and how to count them](https://help.openai.com/en/articles/4936856). |
| Total number of words or phrases to exclude from AI-generated translations | 300 |
| Total number of articles, excluding archived articles and translations | 40,000 |
| Total number of articles in a single section | 5,000 |
| Total number of comments per article | 1,000 |
| Total number of labels per article (not available on Suite Team) | 50 |
| Total number of @mentions in an article | 15 |
| Total number of @mentions in a comment | 15 |
| Total number of content tags per article | 25 |
| Total number of content tags per account | 1,000 |
| Total number of article verification rules | 20 |
| Total number of items within each filter type in an article verification rule | Filter types and item limits: - Article owner: 10 - Author: 10 - Brand: 10 - Category: 10 - Label: 10 - Section: 10 - Permission groups: 10 - User segments: 10 |
| Total number of attachments per article | 500 |
| Article attachment size | 20 MB |
| Total number of media per account (images and attachments) | Plan limits: - Suite Enterprise and above or Guide Enterprise: 150,000 - Suite Professional and Growth or Guide Professional: 70,000 - Suite Team (includes Guide [Lite](https://support.zendesk.com/hc/en-us/articles/4408823905434-About-the-Zendesk-Guide-plan-types#topic_u2d_nww_tvb)): 15,000 |
| Total number of categories | 100 |
| Total number of sections in a single category | 100 |
| Total number of section levels (Enterprise plans only) | 5 |
| Total number of sections in a single section (Enterprise plans only) | 200 |
| Maximum length of an article content | Approximately 1,000,000 characters (excluding *āăą* or hidden html tags). |

## Content blocks limits

The following table shows the maximum limits for content blocks in the help center.

| Item | Limit |
| --- | --- |
| Total number of articles that a content block can be used in | 500 |
| Article size | 1MB This translates to approximately 1000000 characters (excluding *āăą*or hidden html tags). |
| Total number of content blocks in one article | 25 |
| Total number of content blocks in one account | 5000 |
| Total number of images per content block | 50 |
| Content block size | 500KB |
| Plan type | Enterprise plans. |

## Search limits

### General search limits

The following table shows the maximum limits related to help center search.

| Item | Maximum |
| --- | --- |
| [Native search](https://support.zendesk.com/hc/en-us/articles/4408834595738-Understanding-help-center-search-methods-instant-search-native-search-article-suggestions-KC-app#topic_k4p_jbr_vjb) queries | 300 characters or 50 terms |
| [Instant search](https://support.zendesk.com/hc/en-us/articles/4408834595738-Understanding-help-center-search-methods-instant-search-native-search-article-suggestions-KC-app#topic_ahm_lbr_vjb) queries | 300 characters or 100 terms |
| Default [snippet size](https://support.zendesk.com/hc/en-us/articles/4408894061338-About-Help-Center-end-user-search) for a search result | 120 characters |
| Content searched within an article | First 100,000 bytes This translates to approximately 25,000–100,000 characters. |

## External content limits

### General federated search limits

The following table shows the maximum limits related to federated search.

| Item | Maximum |
| --- | --- |
| External records number | Varies by plan: - Enterprise plans: 100,000 - Growth and Professional: 50,000 - Team: 10,000 You can [purchase additional data storage](https://www.google.com/url?q=https://support.zendesk.com/hc/en-us/articles/4408835043994%23topic_xwl_ycw_5lb&sa=D&source=docs&ust=1760548519557707&usg=AOvVaw17dGktVPGRGBWv1-VYytmV) if you exceed these amounts. |
| External record size | 500,000 bytes/record |
| External sources | 50 |
| External types | 20 |
| Record maximum title length | 255 characters/record |
| Crawlers | 20 |

### External content API limits

Normal [Zendesk API rate limits](https://developer.zendesk.com/api-reference/ticketing/introduction/?_ga=2.69664854.712676736.1642510794-978999859.1633961036#rate-limits) apply to the External content API if no lower rate limit is documented in the following table. For links to external content API documentation, see [Federated Search API Introduction](https://developer.zendesk.com/api-reference/help_center/federated-search/introduction/?_ga=2.140052469.712676736.1642510794-978999859.1633961036).

| Item | Maximum |
| --- | --- |
| External record creation | 770/min |

## Management permissions and user segment limits

The following table shows the maximum limits related to user segment functionality in the help center.

Note: The functionality in this section is not available on Suite Team.

| Item | Maximum |
| --- | --- |
| Total number of management permissions groups | 200 |
| Total number of user segments | 200 |
| Total number of ALL tags referenced in a user segment | 50 |
| Total number of ANY tags referenced in a user segment | 50 |
| Total number of groups referenced in a user segment | 50 |
| Total number of organizations referenced in a user segment | 50 |
| Total number of individual users (outside of tags, groups, and organizations) in a user segment | 50 |

See [Creating user segments](https://support.zendesk.com/hc/en-us/articles/4408837707290-Creating-user-segments-for-Guide-user-permissions-Guide-Professional-and-Enterprise-#topic_tql_pjf_zz) for more information about user segments and tags.

## Theme limits

The following table shows the maximum limits for themes and assets in the Help Center.

Note: The functionality in this section is not available on Suite Team.

| Item | Maximum |
| --- | --- |
| Total number of themes | 10 |
| Individual theme size | 55MB |
| Total theme assets size | 50MB |
| Individual theme asset size | 5MB |
| Individual theme asset name | 50 characters |
| Individual theme template size | 300KB |
| Total number of page templates per article, section, or category | Up to 100 each |
| Individual theme style.css size | 800KB |
| Total number of elements per page (for example, articles, posts, sections, categories, and so on) | 30 For more than 30 elements, you can add the pagination helper {{pagination}} to your [help center theme](https://support.zendesk.com/hc/en-us/articles/4408839332250) so users can paginate to view all the elements. |
| Individual theme script.js size | 800KB |
| Total number of settings in manifest.json | 200 |
| Total number of characters in a variable object identifier | 30 Only alphanumeric characters and underscores (\_) are allowed. |
| Total number of options in a list type setting | 20 |
| Total number of custom pages | 100 |

## Why are there limits?

Theme limits are enforced for a few different reasons:

- For security purposes it’s important to vet the types of files that customers are allowed to upload so that we don’t receive malicious files.
- To prevent misuse or abuse vectors, it's important to limit the total size of files.
- For performance reasons, it’s important to serve, save, import and export files quickly for customers.
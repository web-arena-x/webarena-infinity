# About help center federated search

Source: https://support.zendesk.com/hc/en-us/articles/4408830243482-About-help-center-federated-search

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Help center federated search lets your end users see content in your help center search results
that is external to your help center. This means that when an end user searches in your
help center, the search results are not just limited to your help center articles or
community posts. Federated search can extend its search to, for example, external
knowledge bases, learning management software, blogs, and pages of your website. Your
end users can also filter their search by type (for example, by blog posts).

External content search results can appear in help center searches, the [knowledge section of the context panel](https://support.zendesk.com/hc/en-us/articles/4408826700570), and in [Unified Search API](https://developer.zendesk.com/api-reference/help_center/help-center-api/search/#unified-search) responses. They do not
appear in other search-powered interfaces such as Instant Search or the Article Search
API.

You can use either of the following methods to implement federated search in your help
center:

- **Web crawler** - The web crawler lets you implement federated search in your
  help center without developer resources. You can set up multiple crawlers in your
  help center search settings to crawl and index different content in the same or
  different websites.
- **Federated Search API** - This REST API lets you ingest records of your external
  content into the Zendesk search indexes. This method requires that your developers
  build and maintain a middleware layer to integrate the site that hosts the external
  content with the help center.

You can use the API and the crawler simultaneously. However, if you delete a source or a
type via the API, then any crawler that is creating or updating records for the deleted
source or type will stop working.

This article covers the following topics:

- [About the web crawler method](#topic_j4h_3vc_x4b)
- [About the Federated Search API
  method](#topic_n5q_nvc_x4b)
- [External content sources and
  types](#topic_f3d_tcy_x4b)

## About the web crawler method

You can set up one or more web crawlers to crawl and index external content in the
same or different websites that you want to make available to users searching in
your help center.

To set up the web crawler for federated search, see [Using a web crawler to index external content](https://support.zendesk.com/hc/en-us/articles/4593564000410).

## About the Federated Search API method

Zendesk provides a REST API that lets your developers build custom integrations to
ingest external content records into your help center search indexes. To ingest
external content for search, developers must integrate the application hosting your
external content with the external content API.

![Zendesk Federated Search explained diagram](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/zendesk_federated_search_explained_diagram.png)

Once configured, the API ingests external content records and adds them to the help
center search indexes. Indexed records can then be made available to the help center
search engine when responding to user search queries.

Note: If
your help center theme was created before September 25, 2019, you might need to
[modify your theme to use federated
search](https://support.zendesk.com/hc/en-us/articles/4408832681626#topic_tn4_sgw_frb).

To configure federated search using the API, build your own integration with the
Zendesk REST API then ingest the content you want to show up in your search results.
See the [Federated Search](https://developer.zendesk.com/api-reference/help_center/federated-search/introduction/) API reference
documentation.

After you set up federated search, you need to select the content that you want to
include and exclude in help center search results. See [Including external content in your help center search
results.](https://support.zendesk.com/hc/en-us/articles/4593607942298)

You can also include external content in search results in the knowledge section of
the context panel for agents. See [Configuring the knowledge section in the context
panel](https://support.zendesk.com/hc/en-us/articles/7263163614874).

## External content sources and types

Regardless of the setup method you use, each content record ingested by federated
search is associated with a content source and a content type, which are used to
filter search results by your end user. Source refers to the origin of the external
content, such as a forum, issue tracker, or learning management system. Type refers
to the kind of content, such as blog posts, tech notes, or bug reports. See [Managing source and type filters for external content in your
help center](https://support.zendesk.com/hc/en-us/articles/4593648456730).

You can define sources and types either using the Federated Search API or when
setting up the web crawler. If you define sources and types using the API, they will
be available for selection during the web crawler setup. Similarly, if you create a
content source and type when you set up the web crawler, they will be reflected in
the [External Content Types](https://developer.zendesk.com/api-reference/help_center/federated-search/external_content_types/) and [External Content Sources](https://developer.zendesk.com/api-reference/help_center/federated-search/external_content_sources/) APIs.

You can configure your search results to include or exclude external content sources.
When [external content is included in a help center
search](https://support.zendesk.com/hc/en-us/articles/4593607942298), search filters group content by source and type names, making it
easier for users to find the information they are looking for. “Source” groups
content by point of origin (for example blog) and “Type” groups content by the kind
of content it is (for example developer documentation).

Consider useful groupings and names for your external content sources and types when
creating them, as that will help your end users easily filter and locate the content
that they are searching for in your help center.
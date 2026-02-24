# About search sources in the help center

Source: https://support.zendesk.com/hc/en-us/articles/4890968422298-About-search-sources-in-the-help-center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Enterprise |

When users search the help center, they are searching all knowledge base articles
and community posts in your native help center. In addition, depending on the search sources
that you define and enable, your search can also include:

- Articles and community posts from other help centers
- Content from external sources, if federated search is enabled

See the following sections for more information about each of these search
sources:

- [About multiple help center
  search](#topic_f1z_s3b_w5b)
- [About external content search](#topic_dlz_w3b_w5b)

## About multiple help center search

When you add [multiple Support brands](https://support.zendesk.com/hc/en-us/articles/204108983) to your account, you can
create a separate help center for each brand with its own knowledge base. You can then
configure your help center search settings to let users search for content across multiple
help centers in your account. You can also choose to include or exclude community content
from each help center that you select.

If you want to search for community posts from multiple help centers, you must enable
community as a search source in each help center's search settings. If you do not have
community enabled in the help center that contains the community post you want to surface in
search for other help centers, it will not appear in the search results for those help
centers. For example, if your account includes two brands (Brand A and Brand B), and you
want community results from Brand A to appear in Brand B's help center search, then you must
enable the communities for both Brand A and Brand B. If the community for Brand A is not
enabled, then Brand B will not be able to surface search results from that community. See
[Enabling search across multiple help centers](https://support.zendesk.com/hc/en-us/articles/4408821552666).

When you include multiple help centers and communities in your account as search
sources, the content from those sources is searched alongside your native help center when
[users perform search queries](../end-user-guide-for-help-center/help-center-guide-for-end-users.md#search_content). The resulting
content is then grouped under the appropriate source names on the search results page,
making it easier for users to find the information they are looking for.

In the example below, users can see all content that comes from the Zendesk help
center under the Source filter, and can easily select the article they are looking for
within that brand.

![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/search-crawler-guide-filter.png)

To lmanage search sources for multiple help centers, see [Enabling search across multiple help centers](enabling-search-across-multiple-help-centers.md).

## About external content search

When you set up [help center federated search](https://support.zendesk.com/hc/en-us/articles/4593564000410), either using a search crawler or
the Federated Search API, you define external content sources that you want to bring
into your help center.

Once you define external content sources, you
can configure your help center search settings to select which of these sources you want
to include in your help center search results. Then, when users perform a search query,
the help center searches the external content, articles, and community posts (if
configured to do so), and displays the results on the search results page. Results are
grouped by the content source (for example, blog, website, or learning management
system).

In the example below, the Source filter shows external content
grouped by the Camera Obscura help center brand, as well as an external blog and
website. Users can easily select the article they are looking for within each
grouping.

![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/guide-ew-search-results-page.png)

You
can create external content sources during federated search setup and crawler setup, and
you can edit or delete sources at any time. Specifically, you can [edit search filters](https://support.zendesk.com/hc/en-us/articles/4593648456730) to edit the source or type names
that you defined during setup, or to delete a source or type altogether.

To manage
search sources for external content, see [Including external content in your help center search
results](including-external-content-in-your-help-center-search-results.md).
# Using a web crawler to index external content

Source: https://support.zendesk.com/hc/en-us/articles/4593564000410-Using-a-web-crawler-to-index-external-content

---

The web crawler lets you crawl and index external content for usewherever you use external content in your Zendesk accountwithout developer resources. You can set up multiple crawlers to crawl and index different content in the same or different websites. You can also crawl a list of specific URLs without having to crawl an entire site.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

The web crawler lets you crawl and index external content for use [wherever you use external content in your Zendesk account](https://support.zendesk.com/hc/en-us/articles/9822956298010)
without developer resources. You can set up multiple crawlers to crawl and index
different content in the same or different websites. You can also crawl a list of
specific URLs without having to crawl an entire site.

When users perform a search in your help center, relevant external content discovered by
the crawler is ranked and presented on the search results page, where users can filter
the results and click the links to view the external content link in another browser
tab.

This article covers the following topics:

- [About the web crawler](#topic_vs5_js2_dhc)
- [Setting up a web crawler](#topic_a4k_kfl_h2c)

## About the web crawler

You can set up one or more web crawlers to crawl and index external content in the
same or different websites. Content from crawled websites and pages within websites
are made available [wherever you use external content in your Zendesk
account](https://support.zendesk.com/hc/en-us/articles/9822956298010). External sites that you want to crawl must have a [sitemap](https://www.sitemaps.org/)
that lists the pages for the web crawler. In addition, the pages you want to crawl
must be public (non-authenticated).

When you create a web crawler, you can either crawl an entire site or limit the crawl
to up to five pages that you specify during setup. If you choose to:

- **Crawl the entire site**, the crawler automatically locates the sitemap
  associated with the starting URL or sitemap you specify, then uses it to
  crawl all pages within that site.
- **Limit your crawl to individual pages**, you can specify up to five URLs
  that you want to crawl. The **Limit crawl to these URLs**  option is
  automatically selected if you enter more than one URL. However, if you enter
  just one starting URL, you can still manually select this option to restrict
  the crawl to a single page. If you enter a sitemap, this option is
  deselected and disabled, as the crawler must crawl all pages within the
  sitemap.

When you create a new crawler, the name that you assign to the crawler will be used
to create the Source value. [Source values](https://support.zendesk.com/hc/en-us/articles/4890968422298) are used as filters in your help center
search. If you want to change the name later, you can always edit or assign a
different source name. See [Managing web crawlers](https://support.zendesk.com/hc/en-us/articles/4708551571098).

After they've been configured, crawlers are scheduled to run periodically, visiting the pages in
the sitemap and ingesting content from those sources into the help center search
indexes. Web crawlers index content that is in the page source on the initial page
load, even if it's hidden by a UI element, such as an accordion. However, since
crawlers do not run JavaScript, they do not crawl content that is rendered by
JavaScript or other content that is dynamically rendered after the initial page
load.

Web crawlers don't crawl links on the pages they visit; they only visit the pages in
the sitemap that they are configured to use. If the crawler fails to collect
information from a website during a regularly scheduled crawl (for example, if the
website is down or if there are network issues), the help center will retain the
results from the previous crawl, which will continue to be searchable in the help
center.

## Setting up a web crawler

You can set up multiple crawlers in your help center to crawl and index different
content in the same or different websites. When setting up a web crawler, consider
the following:

- The web crawler does not work with websites that use [gzip](https://www.gnu.org/software/gzip/) file compression encoding. You will not see search results
  from these sites.
- A crawl-delay will not be respected by the web crawler when set on external
  site robots.txt records.
- The changefreq tag doesn't affect the web crawler in any way.

Note: You are responsible for using the help center web
crawler in compliance with all applicable laws and the terms and conditions of
the relevant websites. You should only add sitemaps where you own the domain
associated with such sitemaps. By using the help center web crawler, you confirm
that you own the domains for all sitemaps added to the crawler and that you have
the right to crawl such websites.

**To set up the web crawler**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_settings.png)) in the sidebar.
2. Click **Search settings**.
3. Under **Crawlers**, click **Manage**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-search-settings-2026.png)
4. Click **Add Crawler**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-ew-add-crawler-no-crawler.png)
5. Click **Continue**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Crawler-connect-to-website.png)
6. In **Sync content from a website**, enter the following:
   - **Crawler name** that you want to assign to the crawler. This
     name identifies your web crawler on the crawler management list, and
     is used to create the search source value used as the filter in your
     help center search.
   - **Start URLs** for the site or pages that you want to crawl. If
     you want to:
     - **Crawl an entire website**, then enter the primary
       domain (for example, zendesk.com) or the sitemap path (for
       example, zendesk.com/sitemap.xml)
     - **Limit crawling to individual pages**, enter the
       domain/page value in this field (for example,
       test.com/faq.htm). Click **+ Add another** to add up to
       five URLs.

       When you select this option, the crawler will
       only crawl and index the start URLs specified during
       setup.![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/One+Click+Sync+Content.png)
7. Click **Sync**.

   The web crawler is added to the Crawlers page. Within
   24 hours, the crawler will fetch and parse the specified sitemap. When
   the sitemap processing succeeds, the crawler begins to crawl the pages
   and index its content. If the crawler fails, the crawler owner will
   receive an email notification with troubleshooting tips to help resolve
   the issue. The crawler will try again periodically.

   Note: Zendesk/External-Content is the user agent for
   the web crawler. To prevent the crawler from failing due to a
   firewall blocking requests, whitelist (or allow-list)
   **Zendesk/External-Content**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-oneclick-crawlerspage.png)

If you're setting up a web crawler to pull in external content for:

- Help center search, then you need to select the content that you want to
  include and exclude in help center search results. See [Including external content in your help
  center search results.](https://support.zendesk.com/hc/en-us/articles/4593607942298)
- Knowledge section of the context panel for agents, see [Configuring Knowledge](https://support.zendesk.com/hc/en-us/articles/7263163614874) in the
  context panel.
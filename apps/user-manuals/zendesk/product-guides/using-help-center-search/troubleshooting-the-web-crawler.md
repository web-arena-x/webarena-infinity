# Troubleshooting the web crawler

Source: https://support.zendesk.com/hc/en-us/articles/4593607724186-Troubleshooting-the-web-crawler

---

The web crawler lets you crawl and index external content for usewherever you use external content in your Zendesk accountwithout developer resources (seeSetting up the web crawler). You can use this article to troubleshoot crawler setup and page errors that you may encounter while setting up the web crawler in your application.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

The web crawler lets you crawl and index external content for use [wherever you use external content in your Zendesk account](https://support.zendesk.com/hc/en-us/articles/9822956298010)
without developer resources (see [Setting up the web crawler](https://support.zendesk.com/hc/en-us/articles/4593564000410)). You can use this article to
troubleshoot crawler setup and page errors that you may encounter while setting up the
web crawler in your application.

This article contains the following topics:

- [Crawler setup errors](#topic_exy_t5p_ytb)
- [Record errors](#topic_j4h_3vc_x4b)
- [Robot.txt errors](#topic_nch_5wh_zgc)

## Crawler setup errors

Crawler setup errors are generated when the web crawler cannot run successfully.
Crawler setup errors generate an email notification that is sent to the crawler
owner configured during web crawler setup.

### Domain ownership could not be verified

The web crawler attempts to verify domain ownership each time it runs, which can
take up to 24 hours. If the domain verification fails, the crawler owner is
notified by email and the [Crawlers page](https://support.zendesk.com/hc/en-us/articles/4708551571098) will show a Crawl status
of "Domain verification failed."

To troubleshoot domain verification errors, verify the homepage of your website
(otherwise known as the index or root page) is up and publicly available. The
page should not have any user login, password, IP restrictions, or other
authentication requirements.

### Sitemap could not be processed

The web crawler uses the sitemap defined at [crawler setup](https://support.zendesk.com/hc/en-us/articles/4593564000410) each time it runs. If
the sitemap cannot be processed, the crawler owner receives an email
notification and the crawler will not run. If this happens, verify the
following:

- The web crawler is pointing to the correct sitemap URL and can
  locate it successfully. You can edit the crawler to view the current
  sitemap URL. See [Managing web crawlers](https://support.zendesk.com/hc/en-us/articles/4708551571098).
- The sitemap is served and publicly available. The page should
  not be restricted by any user login, password, IP restrictions, or other
  authentication.
- The sitemap is an XML URL sitemap that follows the [Sitemaps XML
  protocol.](https://www.sitemaps.org/protocol.html#validating).

## Record errors

Record errors occur when there are no setup errors, but the web crawler cannot
successfully scrape and index the pages defined in the crawler sitemap ([see Setting up the web crawler](https://support.zendesk.com/hc/en-us/articles/4593564000410)). When a record error
occurs, an email notification is sent to the crawler owner with a link to a CSV file
that lists the affected pages and their associated errors.

### Locale not detected

The error "Locale not detected" indicates that the web crawler could
not detect any locale or the detected locale does not match any current help
center locales.

To determine the locale of a record, the crawler tries the following
approaches. The first successful strategy determines the locale of the
records.

1. Extract the locale from the lang attribute in the <html>
   tag.
2. Extract the locale from the Content-Language header.
3. Extract the locale from the <meta> tag.
4. Perform textual analysis of the content (CLD - Compact
   Language Detection).

The "Locale not detected" error results from of one of the following issues:

- The locale or language identified does not match a locale or language
  configured in any help center in your account. To see which languages are
  configured in each help center in your account, see [Configuring your help center to support
  multiple languages](https://support.zendesk.com/hc/en-us/articles/4408827609882). Find the locale codes for your configured
  languages in [Zendesk language support by
  product](../multiple-language-support/zendesk-language-support-by-product.md#h_01EYXD488X3XK23TG9VPG0W6KS).
- The web crawler could not determine a locale or language.

To resolve this issue, verify the following:

- The lang attribute in the html tag matches a locale from the help
  center.
- The HTTP Content-Language header matches a locale from the Help center.
- The meta element with the Content-Language set in the http-equiv attribute
  matches a locale from the help center.

See [Understanding web crawler locales](https://support.zendesk.com/hc/en-us/articles/4707428787354).

### Title not detected

The error "Title not detected" indicates that the web crawler could not
detect the title of a record. The web crawler uses the following approaches to
determine the title of a record:

1. Extract the content of the <title> tag.
2. Extract the content of the <h1> tag.
3. Extract the textual content from the <body> tag.

The first successful strategy determines the locale of the records. The
crawler only indexes the first 255 characters of the extracted content. The
record is not indexed if the above strategies didn’t determine any content.

To resolve this issue, make sure the affected page has one of the tags listed
above.

### Body not found

The error "Body not found" indicates that the web crawler could not
detect the body of a page. To resolve this error, make sure the affected page is
properly marked with the <body> tag.

### HTTP [status code]

If the error code field in the CSV for a record contains HTTP and a
status code, it means that the page could not be indexed because the page could
not be accessed. If the page could be successfully indexed (HTTP 2xx) you will
not receive an HTTP status code error.

The most common error codes are:

- **404 - Page not found** - The page either does not exist or was moved to
  another URL. To resolve this issue, make sure the sitemap that the crawler
  is using is current and that all URLs in the [sitemap point to existing
  pages](https://support.zendesk.com/hc/en-us/articles/4593564000410).
- **403 - Forbidden** - The crawler is restricted from accessing the page
  due to some access control mechanism, such as it being behind a log in or IP
  address restriction. To resolve this issue, verify the following:
  - You have added Zendesk/External-Content, the web crawler user agent,
    to your allowlist.
  - The pages you want to index are publicly accessible, as the crawler
    cannot crawl pages with restricted access. If the pages you want to
    crawl and index cannot be made publicly accessible then you should
    explore indexing them using the Federated Search (External Content)
    API. See [Setting up the Zendesk Federated
    Search API.](https://support.zendesk.com/hc/en-us/articles/4699774781338)
- **5xx - Server error** - The page could not be crawled due to a [server error](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#5xx_server_errors). The site may be
  temporarily unavailable. To resolve this issue, visit the one or more of the
  pages with this error to make sure the site is up. If the site is down,
  contact the site administrator. When the error is fixed, wait for the
  crawler to run again within its regular cadence (every 12-24 hours).

### Invalid URL domain

The error "Invalid URL domain" indicates the URL of the page listed in
the sitemap is not on the domain you configured during [crawler setup](https://support.zendesk.com/hc/en-us/articles/4593564000410).

To resolve this issue, verify that the domain of the page that
triggered the error is on the same domain as is defined for your web crawler. If
the page linked in your sitemap is pointing to a page that is hosted on a
different domain from the one configured during crawler setup, you can do one of
the following:

- Set up a new web crawler for the affected page.
- Move the page from the external domain to the domain configured for the web
  crawler.

### Undetermined

The error "Undetermined" may be caused by one or more of the
following:

- **You have exceeded the external records limit for your instance
  -** If you've exceeded the [external records limit](https://support.zendesk.com/hc/en-us/articles/4408831783962#topic_ndw_vxj_ytb), the latest
  external records in excess of the limit will not be indexed or updated. To
  resolve this issue you can do one or more of the following:
  - Delete some of your crawlers, whereby the external record of those
    pages is deleted in your instance and then the pages previously not
    indexed due to hitting the limit can be indexed. See [Managing web
    crawlers.](https://support.zendesk.com/hc/en-us/articles/4708551571098)
  - Delete individual records via the [Federated Search API](https://support.zendesk.com/hc/en-us/articles/4699774781338).
    However, if the crawler indexing this page is still active or if a
    custom API integration that adds this page is active, the page will
    reappear next time the crawler runs or the integration syncs.
  - Remove pages that one or more crawlers are using from the sitemap.
    The next time the crawler runs it will re-index the remaining pages
    and delete the ones removed from the sitemap.
  - Point one or more crawlers to a sitemap with fewer pages. The next
    time the crawler runs it will re-index the remaining pages and
    delete the ones removed from the sitemap.
- **The page is using JavaScript location redirects** - The web crawler
  does not observe [JavaScript location
  redirects](https://developer.mozilla.org/en-US/docs/Web/API/Window/location#example_1_navigate_to_a_new_page). If the page uses JavaScript location redirects,
  the crawler cannot reach the content of the page.

  To resolve this issue,
  do one of the following:

  - Make sure the sitemap points directly to the page you want to
    index.
  - Implement [HTTP redirects](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Redirections).

## Robot.txt errors

A robots.txt file tells the crawler which parts of a website it's allowed
to access. Its primary purpose is to prevent overloading a website with excessive
crawl requests.

Rather than being a configuration step, robots.txt acts as a set of
guidelines that informs the crawler whether it can crawl the entire site or specific
sections. The only time customers need to engage with robots.txt is when the crawler
is blocked or the robots.txt file is invalid. In these cases, the system will
generate one of the following errors that must be addressed before the site can be
successfully crawled and synced.

### **Crawl blocked by website**

This error occurs when the robots.txt file is configured to prevent all
user agents, including the crawler, from accessing the site.

To ensure the Zendesk crawler has permission to access the site while optionally
blocking other crawlers, you can add an override rule to the robots.txt file to
allow the Zendesk crawler.

Example 1: Allow only Zendesk/External-Content

```
User-agent: Zendesk/External-Content
Allow: /
```

Example 2: Block Googlebot

```
User-agent: Googlebot
Disallow: /
```

### Invalid robots.txt file

This error occurs when the robots.txt file exists but contains syntax
errors or invalid rules, making it unreadable by crawlers and causing them to
ignore or cancel the crawl.

To resolve this issue, review and correct your robots.txt file to
ensure it adheres to the proper syntax and accurately specifies crawler
permissions. Use online tools, such as [Google’s Robots Testing Tool](https://developers.google.com/search/docs/crawling-indexing/robots/create-robots-txt),
to validate your robots.txt file.
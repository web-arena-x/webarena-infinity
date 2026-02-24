# Importing knowledge sources to power generative replies in advanced AI agents

Source: https://support.zendesk.com/hc/en-us/articles/8357749301658-Importing-knowledge-sources-to-power-generative-replies-in-advanced-AI-agents

---

Knowledge sources are the information your advanced AI agent uses to create AI-generated answers to questions from your customers. Adding knowledge sources to your AI agent lets it generate answers to help customers without requiring you to script every response.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | AI agents - Advanced |

Knowledge sources are the information your advanced AI agent uses to create AI-generated answers to questions from your customers. Adding knowledge sources to your AI agent lets it generate answers to help customers without requiring you to script every response.

This article contains the following topics:

- [About knowledge sources](#topic_qlm_13w_cfc)
- [Importing a knowledge source](#topic_kpz_13w_cfc)

Related articles:

- [Managing imported knowledge sources for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/9962106058906)
- [Configuring search rules for knowledge sources for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/9185497386394)

## About knowledge sources

You can import the following different types of knowledge source into an advanced AI agent:

- **Help centers**: Web-based help centers powered by Zendesk, Salesforce, or Freshdesk.
- **Confluence**: Confluence sites or spaces that your organization uses to store content.
- **CSV files**: CSV files formatted with article information.

 Importing CSV files is a good solution for importing knowledge bases that aren't natively supported or that are protected by single sign-on (SSO).
- **Content imported with a web crawler**: Information from a webpage or set of webpages.

 This option is best suited for importing information from a knowledge base, FAQ, or product description page. It is less suited to e-commerce web shops. For e-commerce pages, Zendesk recommends [building an integration](https://support.zendesk.com/hc/en-us/articles/8357756844442) capable of retrieving relevant product information and adding that information in a [dialogue](https://support.zendesk.com/hc/en-us/articles/8357749494810) or [generative procedure](https://support.zendesk.com/hc/en-us/articles/8979864563610).

You can add multiple knowledge sources to a single AI agent. For example, you can import articles from multiple Zendesk help centers, multiple CSV files, or a combination of both. Nevertheless, we recommend keeping the overall number of knowledge sources within a reasonable limit. Having lots of sources can in some cases lead to reduced accuracy and increased latency.

It’s important to understand that your AI agent doesn't search live data in a help center, file, or website. Instead, the information is imported into the AI agent on a one-time or recurring basis. The AI agent uses this imported information when generating its replies.

## Importing a knowledge source

Client admins can import the following types of knowledge sources for an AI agent:

- [Zendesk help center](#topic_ehq_b3w_cfc)
- [Salesforce help center](#topic_sxl_c3w_cfc)
- [Freshdesk help center](#topic_d31_d3w_cfc)
- [Confluence site or space](#topic_mjn_2mx_chc)
- [CSV file](#topic_hvw_f3w_cfc)
- [Web-crawled content](#topic_amk_g3w_cfc)

### Importing a Zendesk help center

Client admins can import a Zendesk help center.

**To import a Zendesk help center**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Knowledge**.
3. On the Knowledge sources tab, click **Add source**.

   The Add source pane opens.
4. In **Type**, select **Zendesk**.
5. In **Help center URL**, enter your subdomain, including the help center locale (for example, *https://yoursubdomain.zendesk.com/hc/en-us*).

   If you don't provide a locale, the help center's default locale is uploaded.
6. In **Source name**, enter a name for your source.

   This name is used in reporting within AI agents - Advanced.
7. In **Import frequency**, select how often the help center content should be reimported:
   - **Daily**: Content is reimported every day excluding Sundays and the 15th of the month. Not recommended unless your knowledge source is updated very frequently.
   - **Weekly**: Content is reimported each week on Sunday.
   - **Monthly**: Content is reimported on the 15th of each month.
   - **Never**: Content is imported once and is never reimported.

     The exact timing of a reimport isn't guaranteed. The reimport is processed during the day it's scheduled for, but might not always be ready at a consistent time.

     Regular reimporting keeps the AI agent up to date. For most organizations, a weekly or monthly cadence is fine. Remember that you can always manually reimport if new changes need to be reflected outside the scheduled reimport.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_knowledge_importing_zendesk.png)
8. If you want to import restricted articles:
   1. Toggle **Import private articles** on.
   2. In **Email**, enter the email address of a user authorized to access the restricted content.

      This is typically the email address of a Knowledge admin.
   3. In **API access token**, enter an [API token that you generate](https://support.zendesk.com/hc/en-us/articles/4408889192858#topic_bsw_lfg_mmb) for this purpose.
9. Click **Import**.

Note: When importing restricted articles, if the email or API token is incorrect, no warnings or errors are presented. Instead, only public articles are imported, not restricted articles. It's highly recommended to double-check the credentials before importing and test that the AI agent can answer questions using restricted articles after the import has finished.

### Importing a Salesforce help center

Client admins can import a Salesforce help center.

**To import a Salesforce help center**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Knowledge**.
3. On the Knowledge sources tab, click **Add source**.

   The Add source pane opens.
4. In **Type**, select **Salesforce**.
5. Click **Sign in to Salesforce**.
6. Log in to your Salesforce environment.
7. In **Help center URL**, enter the full URL of your Salesforce help center.
8. In **Source name**, enter a name for your source.

   This name is used in reporting within AI agents - Advanced.
9. In **Import frequency**, select how often the help center content should be reimported:
   - **Daily**: Content is reimported every day excluding Sundays and the 15th of the month. Not recommended unless your knowledge source is updated very frequently.
   - **Weekly**: Content is reimported each week on Sunday.
   - **Monthly**: Content is reimported on the 15th of each month.
   - **Never**: Content is imported once and is never reimported.

     The exact timing of a reimport isn't guaranteed. The reimport is processed during the day it's scheduled for, but might not always be ready at a consistent time.

     Regular reimporting keeps the AI agent up to date. For most organizations, a weekly or monthly cadence is fine. Remember that you can always manually reimport if new changes need to be reflected outside the scheduled reimport.
10. Click **Import**.

### Importing a Freshdesk help center

Client admins can import a Freshdesk help center.

**To import a Freshdesk help center**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Knowledge**.
3. On the Knowledge sources tab, click **Add source**.

   The Add source pane opens.
4. In **Type**, select **Freshdesk**.
5. In **Help center URL**, enter the full URL of your Freshdesk help center.

   You can add your whole help center, or only a certain section of your help center.
6. In **Source name**, enter a name for your source.

   This name is used in reporting within AI agents - Advanced.
7. In **Import frequency**, select how often the help center content should be reimported:
   - **Daily**: Content is reimported every day excluding Sundays and the 15th of the month. Not recommended unless your knowledge source is updated very frequently.
   - **Weekly**: Content is reimported each week on Sunday.
   - **Monthly**: Content is reimported on the 15th of each month.
   - **Never**: Content is imported once and is never reimported.

     The exact timing of a reimport isn't guaranteed. The reimport is processed during the day it's scheduled for, but might not always be ready at a consistent time.

     Regular reimporting keeps the AI agent up to date. For most organizations, a weekly or monthly cadence is fine. Remember that you can always manually reimport if new changes need to be reflected outside the scheduled reimport.
8. In **API access token**, enter an API token that you generate in Freshdesk for this purpose.
9. Click **Import**.

### Importing a Confluence site or space

Client admins can import a Confluence site or space.

Confluence connections are created and managed in Knowledge. You must [create a Confluence connection in Knowledge](https://support.zendesk.com/hc/en-us/articles/9796599390874) before you can connect a Confluence site or space to your advanced AI agent.

Unlike other knowledge sources for advanced AI agents, you can’t specify a reimport frequency for Confluence content. Confluence connections automatically sync every 24 hours, but you can [manually resync the content](https://support.zendesk.com/hc/en-us/articles/9796584600218#topic_x2c_xlb_xgc) if needed.

**To import a Confluence site or space**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Knowledge**.
3. On the Knowledge sources tab, click **Add source**.

   The Add source pane opens.
4. In **Type**, select **Confluence**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_import_confluence_source_authorize.png)
5. In **Domain**, enter the URL of your Zendesk subdomain (for example, `https://yoursubdomain.zendesk.com`).
6. In **Email**, enter the email address of a Zendesk admin.
7. In API access token, enter an [API token that you generate](https://support.zendesk.com/hc/en-us/articles/4408889192858#topic_bsw_lfg_mmb)
   for this purpose.
8. Click **Authorize**.
9. Select a Confluence site or space that’s already been connected to your Zendesk account, or [create a new Confluence connection](https://support.zendesk.com/hc/en-us/articles/9796599390874#topic_ftg_xjt_wgc).

   You can select more than one.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_import_confluence_source_select.png)
10. Click **Save**.

The Confluence site or space you selected is added to your list of knowledge sources.

### Importing a CSV file

Client admins can import a CSV file as a knowledge source.

**To import a CSV file**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Knowledge**.
3. On the Knowledge sources tab, click **Add source**.

   The Add source pane opens.
4. In **Type**, select **File (CSV)**.
5. Click **Select knowledge source CSV file**.
6. Select the CSV file you want to import.

   See [Required formatting for the CSV file](#topic_nv3_n3w_cfc) to ensure your file is properly formatted.
7. In **Source name**, enter a name for your source.

   This name is used in reporting within AI agents - Advanced.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_knowledge_importing_csv.png)
8. Click **Import**.

Note: CSV files cannot be reimported automatically. If your content changes, you need to update the CSV file or create a new one and import it again.

#### Required formatting for the CSV file

The CSV file you upload as a knowledge source must have one row for each article you want to import. The file must include the following columns:

- **title**: The title of the article.
- **content**: The full content of the article.
 - The content can contain HTML tags, so there's no need to strip those out. In fact, tags can help as they give structure to the articles, and that structure helps the AI agent understand the article sections.
 - The content can also contain Markdown, but the Markdown must be valid or else the content of that cell will not be imported.
    Additionally, if the Markdown has been written in such a way that the cell is a single line of more than 2,000 characters, importing the cell fails without showing any warnings.

You can also include the following optional columns:

- **labels**: A list of label names separated by a space. The values can be anything you want to categorize content by.
- **locale**: Used to organize articles by language or market. While the values can technically be anything, it's recommended to follow standard locale notation (for example, en-US or fi-FI).
- **article\_url**: The external web address where the article can be found. This is used in source attribution in the widget and reporting within AI agents - Advanced.

The file format must also use:

- Commas (,) as a column separator and double quotes (") as the string quote character.
- The first row for column headers.
- ASCII characters only. CSV files fail to import if they contain any non-ASCII characters.

You can download a template at the bottom of this article.

### Importing content with a web crawler

Client admins can import website content using a web crawler.

For more information about web crawler imports, see [Best practices for using a web crawler to import content for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/9961827483162) and [Troubleshooting issues with web crawler imports for advanced AI agents](https://support.zendesk.com/hc/en-us/articles/9961828111258).

Note: Currently, you can't use the web crawler on a site protected by single sign-on (SSO). Instead, you can [import a CSV file](#topic_hvw_f3w_cfc).

**To import web-crawled content**

1. In AI agents - Advanced, [select the advanced AI agent](https://support.zendesk.com/hc/en-us/articles/8357756913178#topic_t25_qvj_tdc) you want to work with.
2. Click **Content** in the sidebar, then select **Knowledge**.
3. On the Knowledge sources tab, click **Add source**.

   The Add source pane opens.
4. In **Type**, select **Web crawler**.
5. In **Source name**, enter a name for your source.

   This name is used in reporting within AI agents - Advanced.
6. Select **Crawl exact URL** if you want the web crawler to import information only from webpages listed in the Start URLs field, not including any sub-pages.

   When this option is not selected, the web crawler applies a maximum crawling depth of 15 sub-pages for any URLs listed in Start URLs.
7. In **Start URLs**, enter the URLs you want the web crawler to go through.

   List each URL on a separate line.
8. In **Import frequency**, select how often the crawled content should be reimported:
   - **Daily**: Content is reimported every day excluding Sundays and the 15th of the month. Not recommended unless your knowledge source is updated very frequently.
   - **Weekly**: Content is reimported each week on Sunday.
   - **Monthly**: Content is reimported on the 15th of each month.
   - **Never**: Content is imported once and is never reimported.

     The exact timing of a reimport isn't guaranteed. The reimport is processed during the day it's scheduled for, but might not always be ready at a consistent time.

     Regular reimporting keeps the AI agent up to date. For most organizations, a weekly or monthly cadence is fine. Remember that you can always manually reimport if new changes need to be reflected outside the scheduled reimport.
   - ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_knowledge_importing_web_crawler.png)
9. (Optional) Expand **Crawler settings** to configure advanced crawler settings.

   See [Configuring advanced crawler settings](#topic_zsr_p3w_cfc) for details.

   Note: These settings are recommended only for organizations with complex technical requirements. Many organizations do not need these settings.
10. (Optional) Expand **HTML processing** to configure advanced HTML settings.

    See [Configuring advanced HTML settings](#topic_sll_s3w_cfc) for details.

    Note: These settings are recommended only for organizations with complex technical requirements. Many organizations do not need these settings.
11. Click **Import**.

#### Configuring advanced crawler settings

1. [Under the Crawler settings heading](#topic_amk_g3w_cfc), in **Crawler type**, select one of the following options:
   - **Adaptive switching between browser and raw HTTP (Default)**: Fast and renders JavaScript content if present.
   - **Headless browser (Firefox + Playwright)**: Reliable, renders JavaScript content, best in avoiding blocking, but might be slow.
   - **Raw HTTP client (Cheerio)**: Fastest, but doesn’t render JavaScript content.
   - **Raw with JavaScript**: Crawl the page as if using JavaScript.
2. Select **Include URLs** or **Exclude URLs** to customize the crawling scope set in the Start URLs field above.

   In the field below each setting, enter the URLs you want to include or exclude. Enter each URL on its own line.

   These settings affect only the links found while crawling sub-pages. If you want to crawl a page, make sure to specify its URL in the Start URLs field.

   For example, if the URL structure is inconsistent as in the example below:

   - Start URL:
     `https://support.example.com/en/support/home`
   - Article URL:
     `https://support.example.com/en/support/solutions/articles/…`You can add the following URL in the **Include URLs** field:
   - `https://support.example.com/en/support/**`

   This way, the web crawler will include all of the articles, even though their path is different from the starting URL.

   As another example, the following page is very broad and includes irrelevant pages (for example, the careers page):
   - Start URL: `https://www.example.com/en`To exclude these irrelevant pages, you can add the following
   URL in the **Exclude URLs** field:
   - `https://www.example.com/en/careers/**`This way, the web crawler will exclude all of the content from
   the careers page and its sub-pages.

   Tip: More powerful than plain text, *globs* are patterns that let you use special characters to create dynamic URLs for the web crawler to search. Here are a few examples:
   - `https://support.example.com/**` lets the crawler access all URLs starting with https://support.example.com/.
   - `https://{store,docs}.example.com/**` lets the crawler access all URLs starting with https://store.example.com/ or https://docs.example.com/.
   - `https://example.com/**/*\?*foo=*` allows the crawler to access all URLs that contain foo query parameters with any value.Learn more about globs and test them on the [DigitalOcean
   website](https://www.digitalocean.com/community/tools/glob?comments=true&glob=https%3A%2F%2Fexample.com%2Fscrape_this%2F%2A%2A&matches=false&tests=https%3A%2F%2Fexample.com%2Ftools%2F&tests=https%3A%2F%2Fexample.com%2Fscrape_this%2F&tests=https%3A%2F%2Fexample.com%2Fscrape_this%2F123%3Ftest%3Dabc&tests=https%3A%2F%2Fexample.com%2Fdont_scrape_this).
3. In **Max pages to crawl**, enter the maximum number of pages the web crawler will go through, including the starting URL.

   This includes the starting URL, pagination pages, pages with no content, and more. The web crawler will automatically stop after reaching this limit.
4. In **Max crawling depth**, enter the maximum number of links the web crawler will follow from the starting URL.

   The starting URL has a depth of 0. Pages linked directly from the starting URL have a depth of 1, and so on. Use this setting to prevent accidental web crawler runaway.
5. In **Proxy configuration**, select one of the following options:
   - **Datacenter (Default)**: Fastest method to scrape data.
   - **Residential**: Reduced performance, but less likely to be blocked. Ideal for when the default proxy is blocked or when you need to crawl from a specific country.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_knowledge_importing_crawler_settings.png)

#### Configuring advanced HTML settings

1. [Under the HTML processing heading](#topic_amk_g3w_cfc), in **Keep HTML elements**, enter a CSS selector to keep only specified HTML elements.

   All other content will be removed, helping you focus only on relevant information.
2. In **Remove HTML elements**, choose which HTML elements to remove before converting to text, Markdown, or saving as HTML.

   This helps exclude unwanted content.
3. In **Expand clickable elements**, enter a valid CSS selector matching DOM elements that will be clicked.

   This is useful for expanding collapsed sections in order to capture their text content.
4. In **HTML transformer**, select one of the following values to define how to clean up the HTML to keep only important content and remove extraneous content (for example, navigation or pop-ups):
   - **Extractus**: (Not recommended) Uses the Extractus library.
   - **None**: Removes only the HTML elements specified in the Remove HTML elements option above.
   - **Readable text**: Uses Mozilla's Readability library to extract the main article content, removing navigation, headers, footers, and other non-essential elements. Works best for article-rich websites and blogs.
   - **Readable text if possible**: Uses Mozilla's Readability library to extract the main content, but falls back to the original HTML if the page doesn't appear to be an article.
     This is useful for websites with mixed content types, such as articles or product pages, as it preserves more content on non-article pages.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_knowledge_importing_html_processing.png)
5. In **Wait for dynamic content**, enter the number of seconds the crawler should wait for dynamic content to load. By default, it waits five seconds or until the page finishes loading, whichever comes first.
6. In **Soft wait for selector**, enter CSS selectors for HTML elements that the crawler should wait to load before extracting content.

   If the selected element isn't present, the crawler still crawls that page.

   List each CSS selector on a separate line.
7. In **Wait for selector**, enter CSS selectors for HTML elements that the crawler must wait to load before extracting content.

   If the selected element isn't present, the crawler doesn't crawl that page.

   List each CSS selector on a separate line.
8. In **Max scroll height**, enter the maximum number of pixels the crawler should scroll.

   The crawler scrolls the page to load more content until the network is idle or this scroll height is reached. Set this to 0 to disable scrolling completely.

   This setting doesn't apply when using the raw HTTP client, as it doesn't run JavaScript or load dynamic content.
9. In **Make containers sticky**, enter CSS selectors for HTML elements where child content should be kept, even if it's hidden.

   List each CSS selector on a separate line.

   This is helpful when using the Expand clickable elements option on pages that remove hidden content from the page entirely.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aiaa_knowledge_importing_html_processing_2.png)
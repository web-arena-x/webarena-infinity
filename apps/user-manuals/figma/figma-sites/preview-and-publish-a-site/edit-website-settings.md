# Edit website settings

Source: https://help.figma.com/hc/en-us/articles/31242875661591-Edit-website-settings

---

Figma Sites was released in [open beta](https://help.figma.com/hc/en-us/articles/4406787442711) at Config 2025. [Learn more about what’s included in the beta.](https://help.figma.com/hc/en-us/articles/4406787442711)

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the file

Update your website’s settings to help search engines understand your content, improve accessibility, determine how your content displays on social media, and secure your website.

To access settings, click the **Site settings** icon in the left navbar of your sites file. Select **General** to edit settings that affect the entire site—or navigate directly to a specific page’s settings.

Here are the settings that are available site-wide, or on a per-page basis:

| | **Entire site** | **Per page** |
| --- | --- | --- |
| [Title](#h_01JTH79EDP2FVD1N9XQ0PJGHS7) | ✓ | ✓ |
| [Meta description](#h_01JTH79EDPDNHZ7D2QVJG40FMS) | ✓ | ✓ |
| [Social sharing image](#h_01JTH79EDQSPS32NPYBY99JE06) | ✓ | ✓ |
| [Language code](#h_01JTH79EDQ4NWT25YBMZN5V9TP) | ✓ | ✓ |
| [Google Analytics](#h_01JTH79EDQBHS5Y8B05XKN2SMQ) | ✓ | X |
| [Manage inclusion in search engine results](#h_01JTH79EDQ3CTPK6P9JN42F10D) | ✓ | ✓ |
| [Add a favicon](#h_01JTH79EDQP5KCN074Q73C1CG8) | ✓ | X |
| [Manage published site access](#h_01K57S6JDE5CQSXPGQVWRXGGZ5) (requires paid plan) | ✓ | X |
| [Add a cookie consent banner](#h_01K5CD0Q09R36BKK1EJKGA0GB7) (requires paid plan) | ✓ | X |
| [Custom code](#h_01JTH79EDQNQ3DC6K2ATGC6W0Q) | ✓ | X |

**Tip**: From **Settings**, you can also [review and manage the publishing status](https://help.figma.com/hc/en-us/articles/31242845959703) of your site, [choose your own subdomain](https://help.figma.com/hc/en-us/articles/33237655531287), and [add a custom domain](https://help.figma.com/hc/en-us/articles/31414274019863).

## Add a title

![Search result preview for "Earthling trip planner" with title "Home | Earthling" and a description of travel planning.](https://help.figma.com/hc/article_attachments/31937313355543)

The title appears in browser tabs, search engine results, and on social media. Adding a clear title helps people understand where they are in their browser, supports SEO, and improves accessibility.

If no page title is provided, Figma will display the site’s title instead. If neither is available, Figma will generate a title for the site.

## Add a meta description

![Search result preview for "Earthling trip planner" with highlighted meta description about planning memorable trips.](https://help.figma.com/hc/article_attachments/31937313361687)

A meta description is a short summary of the website or page content. It is designed to attract users and improve click-through rates from search engine results pages (SERPs).

For the entire website, the meta description ensures a consistent summary is available when specific pages do not have one.

On individual pages, you can provide a unique meta description tailored to that page; otherwise, the global meta description will be applied.

## Add a social sharing image

![Social media post by a user about booking a trip to Rome, featuring a social sharing image of a classical sculpture with the word "ROME".](https://help.figma.com/hc/article_attachments/31937329441943)

The social sharing image appears when your website—or any of its pages—is shared on social media. The site-wide social sharing image will be used whenever a page-specific image isn’t provided. If neither is available, Figma will use an image snapshot of your site instead.

We recommend using an image that is 1200px wide by 630px tall.

## Set a language code

Setting the language code for your website improves accessibility and assists browser translation features by clearly indicating its primary language.

The website language setting applies to the entire site by default, but you can specify a different language on individual pages if needed.

ISO language codes assign unique identifiers to languages. Some of the most common language codes include:

- **ar** – Arabic
- **de** – German
- **en** – English
- **es** – Spanish
- **fr** – French
- **ja** – Japanese
- **hi** – Hindi
- **ru** – Russian
- **pt** – Portuguese
- **zh** – Chinese

[View a complete list of ISO language codes on Wikipedia](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes).

## Add a Google Analytics ID

Connect your site to a Google Analytics property to get insights into how people are using your published website.

[Review the instructions from Google on how to find your Google Analytics ID.](https://support.google.com/analytics/answer/9539598?hl=en)

**Note:** Please note that you are responsible for ensuring your site complies with applicable laws, including any applicable to cookies, privacy and data collection.

**Note**: Only Google Analytics is supported at this time, but we’re aiming to add support for more analytics providers in the future.

## Exclude the website—or individual pages—from search engine results

Enable this setting to instruct search engine robots not to index your site or show it in search results.

Checking the box will add a `<meta name="robots" content="noindex">` tag to the header of your site or to individual pages.

## Add a favicon

![Browser tab showing "Earthling – Home" title, URL, and a highlighted favicon icon.](https://help.figma.com/hc/article_attachments/31937313363991)

A favicon provides a small visual representation of your website in browser tabs, search results, and bookmarks.

To add a favicon to your site, place an image or design on the canvas in your site file, then choose it in the settings modal.

**Tip:** For best results, we recommend using a 48px x 48px image or frame.

## Manage published site access

### Choose who can access the published site Organization Enterprise

On the Organization and Enterprise plans, you can choose whether to publish your site on the open web, or restrict it to an internal audience. If a file is published internally:

- Any logged-in member of your organization can view it
- Guests and anyone outside your organization cannot access it

**Note**: If you don’t have the option to set the audience to **Anyone on the web,** it’s likely an admin has [disabled publishing to the open web.](https://help.figma.com/hc/en-us/articles/31242876956183)

### Add password protection to your site Paid plans

![](https://help.figma.com/hc/article_attachments/34347130848151)

When password protection is enabled, visitors must enter a password to view your published site’s content, including metadata such as the page title and description.

You can apply a single password to the **whole site** or to **individual pages**. Keep the following in mind when applying a password to individual pages:

- Password protection remains in place even if the URL path changes—for example, if you rename `/portfolio` to `/clients`.
- When publishing a [CMS page](https://help.figma.com/hc/en-us/articles/35222938006679), all dynamic pages generated from that CMS path will share the same password protection. For example, if you password-protect your CMS page `/blog`, any associated pages like `/blog/article-1` and `/blog/article-n` will also be protected.

When setting a password, you can create your own or use one automatically generated by Figma:

- **Custom passwords** must be at least four characters long and may include any combination of characters
- **Figma-generated passwords** combine four random words, making them strong and unique

The password will automatically apply to your published site as soon as you save it. When making changes, you don’t need to republish—although the changes may take a minute or two to take effect.

**Note:** If you add a password to a published site which has not been [excluded from search engine results](edit-website-settings.md#h_01JTH79EDQ3CTPK6P9JN42F10D), some metadata may continue to appear in search listings. Once password protection is enabled, search engines will no longer be able to index the site, and it will typically disappear from results over time. If you want to speed up the process, you can [request removal through Google Search Central](https://developers.google.com/search/docs/crawling-indexing/remove-information).

Once set, you can’t view a password again. If you forget to copy it, you’ll need to create a new one. When you change the password, anyone with prior access will need to enter the new password the next time they refresh or navigate to a different page within the site.

**Note**: You may experience some restrictions when setting a password:

- If you can't write your own password, your organization likely [requires autogenerated passwords only](https://help.figma.com/hc/en-us/articles/5726756336791).
 Your organization may also [require password protection](https://help.figma.com/hc/en-us/articles/31242876956183)
 for all published sites.
- You can't add a password if the audience is set to internal-only.
- You can’t set passwords on individual pages if your organization [requires password protection](https://help.figma.com/hc/en-us/articles/31242876956183)
 for all published sites.

## Add a cookie consent banner to your site Paid plans

![](https://help.figma.com/hc/article_attachments/35034761455383)

Figma Sites includes a built‑in cookie consent banner that lets visitors approve, reject, or manage non‑essential cookies, like those used by analytics and third-party embeds.

[Learn more about how the cookie banner works.](https://help.figma.com/hc/en-us/articles/34883553489687)

## Add custom code to your site for ad tracking or analytics

You can insert custom code snippets at the start or end of your site’s head or body tags.

For instance, loading critical tags like analytics in the head ensures they execute early, while non-critical elements like a chat widget can be placed at the end of the body to avoid slowing down the main page content.

## Frequently asked questions

### **Sharing a link to my site shows outdated or incorrect metadata. How can I fix it?**

First, make sure you’ve published the latest version of your site with any updated metadata. If everything is published but other platforms still show old information, it’s likely due to caching.

Most social platforms cache link metadata—such as titles, descriptions, and preview images—the first time a URL is shared. Even after you update your page, these platforms may continue displaying the older data. To refresh the preview, you can “bust the cache” by running your URL through the platform’s debugging or preview tool, which forces it to re-scrape the latest metadata.

**Tools to refresh metadata:**

- **Facebook:** [Sharing Debugger](https://developers.facebook.com/tools/debug/)
- **LinkedIn:** [Post Inspector](https://www.linkedin.com/post-inspector/)
- **X (Twitter):** [Card Validator](https://cards-dev.twitter.com/validator)
- **Slack:** Previews refresh automatically over time, or you can force a new unfurl by sharing a slightly modified link (e.g., adding `?v=2` to the end of the URL).
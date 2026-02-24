# Add a cookie consent banner to your site

Source: https://help.figma.com/hc/en-us/articles/34883553489687-Add-a-cookie-consent-banner-to-your-site

---

Figma Sites was released in [open beta](https://help.figma.com/hc/en-us/articles/4406787442711) at Config 2025. [Learn more about what’s included in the beta.](https://help.figma.com/hc/en-us/articles/4406787442711)

Who can use this feature

Available on [all plans](https://help.figma.com/hc/en-us/articles/360040328273)

Requires edit access to the file

Cookies are small pieces of data a website stores in your browser to remember information across visits, like login status, preferences, or activity.

Figma Sites includes a built‑in cookie consent banner that lets visitors approve, reject, or manage non‑essential cookies, like those used by analytics and third-party embeds.

As a site owner, this helps you with comply with regulations like GDPR in the EU and CCPA/CPRA in California.

**Note**: As stated in our [Terms of Service](https://www.figma.com/legal/tos/), it is your responsibility as a user to ensure your content complies with applicable laws. Any information provided to you in this article is not legal advice and should not be relied upon as such.

## How it works

![Cookie consent popover at the bottom left of a webpage offering options to reject all, manage, or accept all cookies.](https://help.figma.com/hc/article_attachments/35034758586007)

When enabled, visitors from certain geographic regions will see a cookie consent banner across every page on their first visit to your site. This lets them refine which cookies they’ll allow. For regions that don’t require cookie consent, visitors won’t see a banner.

If they want, visitors can click **Manage** to specify which cookies they’ll allow from the following categories:

- **Essential**: Required cookies for basic site functionality and can’t be turned off by visitors.
- **Analytics:** Helps you understand how people use your site—e.g., page views, traffic sources, and basic events—so you can improve performance and content. This is especially relevant if you’re using Google Analytics on your site.
- **Personalization:** Remembers a visitor’s choices and can tailor parts of the experience to those preferences.
- **Marketing:** Measures ad effectiveness and supports audience building or retargeting across sites and services (for example, ad pixels or some social media tags). If disabled, related pixels and certain embeds may not load.

!["Allow cookies to view this content" placeholder on a YouTube embed when non-essential cookies are disabled.](https://help.figma.com/hc/article_attachments/35034758588695)

If a visitor rejects all cookies, or generally disables any non-essential cookies, embeds on your site won’t load for them. Figma will show an **Allow cookies to view this content** placeholder on the content, and visitors can reopen their cookie settings to change their preferences if needed.

![Small cookie preferences banner attached to the bottom right of the site.](https://help.figma.com/hc/article_attachments/35034710180631)

Once they’ve made a choice, the banner hides and Figma remembers their preference for the website in the browser. Visitors can click into their cookie preferences at any time to updates their preferences.

### Understanding implied vs explicit consent

Figma will automatically adjust the cookie consent banner depending on the compliance requirements of the visitor’s region:

- **Implied consent**: People are opted into cookies by default. If they don’t interact with the cookie consent banner, all site cookies will work automatically.
- **Explicit consent**: People are opted out of non-essential cookies by default. If they don’t accept or manage their cookies, no cookies will load on the site.

**Implied consent countries**

- Australia
- Hong Kong
- Indonesia
- Kenya
- Mexico
- New Zealand
- Nigeria
- Philippines
- South Africa
- Thailand
- United States

**Explicit consent countries**

- Andorra
- Argentina
- Austria
- Belgium
- Brazil
- Bulgaria
- Chile
- Croatia
- Cyprus
- Czechia
- Denmark
- Estonia
- Finland
- France
- Germany
- Greece
- Hungary
- Iceland
- India
- Ireland
- Italy
- Japan
- Latvia
- Liechtenstein
- Lithuania
- Luxembourg
- Malaysia
- Malta
- Morocco
- Netherlands
- Norway
- Poland
- Portugal
- Qatar
- Romania
- Russia
- Singapore
- Slovakia
- Slovenia
- South Korea
- Spain
- Sweden
- Switzerland
- United Kingdom

## Enable a cookie consent banner

### 1. Enable cookie consent

1. Open your site file and click **Settings**.
2. In the left sidebar, select **General**, then navigate to **Cookie consent**.
3. Click the toggle to enable cookie consent.

### 2. Preview the implied or explicit consent banner

Click the toggle to preview the implied and explicit experience. Figma will automatically adjust the cookie consent banner depending on the compliance requirements of the visitor’s region.

### 3. Choose a language, style, and position

There are two styles you can use for your banner:

1. **Popover:** a small card you can anchor to any corner of the page.
2. **Banner:** a horizontal bar that appears at the **top** or **bottom** of the page. Fixed to the width of the viewport.

### 4. Add a privacy policy link

The cookie consent banner requires a link to the privacy policy governing your site. This link can point to a page on your site, or to an external site.

1. In the **Privacy policy** field, click the **dropdown** to choose a page from your site, or paste an external link.
2. Click **Save**.

### 5. Test the cookie consent banner

The cookie consent banner appears when you preview the site. It’s also available to test on the published site. Click on a webpage on the canvas to preview it with the cookie banner. After making a selection, reload the site file to reset the cookie consent banner to it’s first-visit state.

**Note**: When previewing, Figma displays the [explicit consent banner](#h_01K59TKGGPVG587F8QRMR8HRDT) by default.

To test the banner on your published site, visit your site’s URL and verify the banner appears. To test the first‑visit experience, open the site in a private or incognito window or clear the site’s cookies in your browser. This approach won’t work if you’re in a geographic region that doesn’t require cookie consent.

**Tip:** You can adjust the style, language, or policy link of your cookie banner at any time. [Republish your site](https://help.figma.com/hc/en-us/articles/31242845959703) to push changes live.

## Frequently asked questions

**What happens if people reject cookies on my site?**

It depends on the features used by your site. If your site uses embeds, those won't load without enabling cookies. If your site uses any scripts that require third party cookies—for example, if you’ve set up Google Analytics—those scripts won’t work for people who have rejected analytics or marketing cookies.

**Why isn’t the banner showing on my published site?**

Here are three things to check:

1. Make sure cookie consent is toggled **On**, a **Privacy policy** link is set, and you’ve **published** the site after saving settings.
2. Test in a private or incognito window to avoid cached consent.
3. Check the [list of geographic regions](#h_01K59TKGGPVG587F8QRMR8HRDT) to make sure the banner should appear to you as a visitor.

**Does this make my site compliant everywhere?**

Figma’s cookie consent feature is a tool to help with compliance. Since requirements differ by region and use case, we recommend consulting with legal counsel for guidance specific to your site.

**I need to reference the cookie settings in a code layer. How do I do that?**

If your code layer needs to read a user’s cookie settings, we recommend taking a look at the [cookie consent reference guide](https://www.figma.com/code-docs/cookie-consent-mode) in our developer documentation.
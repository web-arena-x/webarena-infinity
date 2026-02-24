# Improving your online store performance

Source: https://help.shopify.com/en/manual/online-store/web-performance/improving-web-performance

---

# Improving your online store performance

Your online store is made up of a set of features, such as theme code, apps, images, videos, carousels, social media feeds, and analytics. These features can enhance the visitor experience and extend your site's capabilities.

However, each feature that you add to your online store can impact your store's performance. Some features can slow down your site or create unexpected behaviors that can impact user experiences.

Web performance focuses on optimizing user experience. Currently, web performance focuses on three major areas which are also reflected in the [Core Web Vitals](https://performance.shopify.com/blogs/blog/key-web-performance-metrics):

* Loading speed, measured by Largest Contentful Paint (LCP)
* Layout stability, measured by Cumulative Layout Shift (CLS)
* Responsiveness to user interaction, measured by Interaction to Next Paint (INP)

Optimizing web performance means that your customers are more likely to stay on your site and convert.

## On this page

* [Optimizations for your online store](improving-web-performance.md#optimizations-for-your-online-store)
* [Factors that impact web performance](improving-web-performance.md#factors-that-impact-web-performance)
* [Testing tools](improving-web-performance.md#testing-tools)
* [Understanding third-party performance recommendations](improving-web-performance.md#understanding-third-party-performance-recommendations)
* [Troubleshooting slow loading pages](improving-web-performance.md#troubleshooting-slow-loading-pages)
* [Get support with online store performance](improving-web-performance.md#get-support-with-online-store-performance)
* [Technical information and resources for troubleshooting](improving-web-performance.md#technical-information-and-resources-for-troubleshooting)

## Optimizations for your online store

Your online store has web optimization built into it. Web optimization is also built into any new features. You don’t need to do anything special to take advantage of the following features:

* Your online store is hosted on [fast, global servers](https://www.shopify.com/website/hosting) and doesn't limit your store's bandwidth. You can check the status of your Shopify store on [Shopify Status](https://shopifystatus.com).
* Your online store has a content delivery network (CDN) run by [Cloudflare](https://www.cloudflare.com) that ensures that your online store loads quickly around the globe. You can check the CDN status on the [Cloudflare status page](https://www.cloudflarestatus.com).
* To keep load times fast, images are automatically optimized using [image CDN](https://cdn.shopify.com). Combined with your theme code, the image CDN can serve the best image format that's also resized and compressed to keep file sizes small.

## Factors that impact web performance

For Shopify stores, the following are the biggest factors that impact web performance:

* Your online store theme
* The apps you’ve installed
* Any additional third-party code you’ve manually added to your store, including tag managers and the tags within them

This means that you should focus on the following to improve your web performance:

* Use an up-to-date, optimized theme. All the [Horizon family of themes](https://themes.shopify.com/collections/horizon-themes), and [Online Store 2.0 themes by Shopify](../themes/managing-themes/versions.md) are free and optimized for web performance. Additionally, many other third-party themes are also optimized for web performance. You can review the latest [theme performance data](https://performance.shopify.com/pages/theme-performance-data-table).
* If your theme offers page transitions or other animations, then compare your web performance before and after activating them. Animations can slow down pages.
* Avoid adding too many sections to page templates in your theme. High numbers of sections on pages can lower web performance.
* If you have collections with large amounts of products in them, then consider activating pagination to limit the number of products that load at one time.
* Evaluate your installed apps and third-party code to ensure that they're creating enough value to offset any potential performance losses.
* Audit your tag manager to remove any unused or low-value tags. Learn more about [best practices for tags and tag managers](https://web.dev/articles/tag-best-practices).

## Testing tools

You can use the following tools to investigate your online store's performance:

* Web Performance reports: Shopify's [Web Performance reports](web-performance-reports.md) use Core Web Vitals to measure how real users experience your online store.
* PageSpeed Insights: You can run your own reports using Google's [PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights) to view more detailed metrics for pages in your store.

## Understanding third-party performance recommendations

Third-party performance scanning tools might suggest changes to improve your store's speed. However, many of these recommendations are already implemented by Shopify or don't apply to Shopify stores.

### Optimizations already included in Shopify

Your Shopify store automatically includes the following performance optimizations:

**Content Delivery Network (CDN):** Shopify provides a world-class CDN at no additional charge, ensuring fast global performance. All assets are served using HTTP/2, reducing overhead compared to older protocols.

**Browser caching:** Shopify sets browser caching for cacheable resources to one year, the maximum possible duration. This means that repeat visitors to your store will experience faster loading times.

**Gzip compression:** Shopify employs gzip compression on CSS, JavaScript, documents, and pages to reduce bandwidth and improve load times. Keep-alive is also enabled for multiple file retrieval.

**Image optimization:** Shopify automatically compresses JPG images using advanced algorithms, balancing compression and visual appeal. Images are often served in WebP format for better compression and faster loading.

**File minification:** Shopify automatically minifies CSS and JavaScript files when they're requested by your storefront, reducing file sizes without affecting functionality.

### When third-party recommendations don't apply

Third-party scanning tools might suggest changes that aren't relevant to Shopify stores:

* **Server-level configurations:** Recommendations about server setup, HTTP headers, or caching policies are already optimized by Shopify's infrastructure.
* **CDN implementation:** Suggestions to add a CDN are unnecessary since Shopify includes a high-performance CDN by default.
* **Compression settings:** Recommendations about enabling compression are already implemented across Shopify's platform.

### Acting on relevant recommendations

Focus on recommendations that relate to your store's specific content and features:

* **Image optimization:** Ensure your uploaded images are appropriately sized and use recommended formats.
* **App evaluation:** Consider whether installed apps provide enough value to offset any performance impact.
* **Theme optimization:** Choose themes optimized for performance and limit the number of sections on page templates.

## Troubleshooting slow loading pages

If your store is loading slowly, follow these steps to identify and resolve the issue:

### Step 1: Verify the issue

1. Test your store's loading speed yourself from different devices and internet connections.
2. Ask others to test your store to confirm it's not a local issue with your internet connection.
3. Use testing tools like [PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights) to get specific performance metrics.

### Step 2: Identify the cause

**Check for excessive apps:** Too many apps loading assets on your storefront can slow performance. Review your installed apps and remove any that aren't essential for sales.

**Review large images:** Pages with numerous high-quality images can load slowly. Optimize your images or reduce the number displayed. Learn more about [recommended image sizes](https://help.shopify.com/en/manual/products/product-media).

**Identify slow scripts:** If your site hangs as a blank page before loading all at once, use your browser's developer tools to identify slow-loading scripts. Contact the app or theme developer for resolution.

### Step 3: Take action

**Remove unnecessary apps:** Uninstalling an app doesn't automatically remove its code from your theme. You might need to contact the app developer for complete removal instructions.

**Optimize images:** Use appropriate file formats (JPG for photos, PNG for graphics with transparency) and resize images to match their display size.

**Evaluate theme performance:** Consider switching to a performance-optimized theme if your current theme is causing significant slowdowns.

## Get support with online store performance

If you use a [free theme from Shopify](https://themes.shopify.com/collections/free-themes), then Shopify Support might be able to assist you with basic performance improvements.

If you use a third-party theme and need assistance, then you must contact [your theme developer](../themes/theme-support%23paid-themes.md), hire a [Shopify web performance expert](https://performance.shopify.com), or hire a [Shopify Partner for site performance and speed](https://www.shopify.com/partners/directory/services/expert-guidance/guidance-for-improving-your-site-performance-and-speed). Learn more about [hiring a Shopify Partner](https://help.shopify.com/en/manual/partner-directory).

If your performance problem is coming from an app, then you can contact [your app developer](https://help.shopify.com/en/manual/apps/getting-support).

If you have a development team or agency partner, then you can also reach out to them for further assistance.

## Technical information and resources for troubleshooting

If you’re a developer seeking to improve performance for a Shopify storefront, theme, or app, then you can review the following resources for each Core Web Vital. Learn more about [performance best practices for Shopify Themes](https://shopify.dev/docs/themes/best-practices/performance).

### Loading speed

Largest Contentful Paint (LCP) measures loading speed, based on how fast the largest element on the screen becomes visible. Time to first byte (TTFB) and first contentful paint (FCP) are supporting metrics which help you better understand where the root cause of the problem is coming from. You can learn more about [debugging common causes for slow loading in Shopify Liquid storefronts](https://performance.shopify.com/blogs/blog/debugging-common-causes-for-slow-loading-in-shopify-liquid-storefronts).

### Visual stability

Cumulative Layout Shift (CLS) measures visual stability, based on how much the content shifts around unexpectedly during loading. For a deep-dive on debugging CLS, read [*How to optimize Cumulative Layout Shift (CLS) on Shopify sites*](https://performance.shopify.com/blogs/blog/how-to-optimize-cumulative-layout-shift-cls-on-shopify-sites).

### Interactivity

Interaction to Next Paint (INP) measures interactivity based on how long it takes the page to become responsive to most user actions. For example, user actions such as clicking a link or a button.

If you’re suffering from poor INP, then most likely you have too much JavaScript in your store from either theme code, app code, or third party/tag manager code. Work on cleaning up your worst offenders. Learn more about [*3 ways to find your worst JavaScript offenders for page load*](https://performance.shopify.com/blogs/blog/3-ways-to-find-your-worst-javascript-offenders-for-page-load). If you’re still having issues with INP, then learn more with the resources on [web.dev](https://web.dev/articles/inp).
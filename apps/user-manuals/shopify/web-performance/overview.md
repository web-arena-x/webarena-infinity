# Overview of web performance

Source: https://help.shopify.com/en/manual/online-store/web-performance/overview

---

# Overview of web performance

Web performance is measured by key metrics called *Core Web Vitals*. These metrics quantify your online store's performance, and optimizing the values can improve the [shopping experience of your customers](overview.md#experience-and-conversion), your [conversion rate](overview.md#experience-and-conversion), and your store's [discoverability](overview.md#discoverability).

Your online store's performance can be influenced by several factors, such as the following areas:

* Apps
* Third-party libraries and services
* Analytic libraries
* Theme code
* The quantity and size of images and videos

By making strategic [adjustments](improving-web-performance.md) to your online store, you can improve your performance metrics and ranking.

## On this page

* [Measuring your web performance](overview.md#measuring-your-web-performance)
* [How web performance impacts your store](overview.md#how-web-performance-impacts-your-store)
* [Online store features vs. web performance](overview.md#online-store-features-vs-web-performance)
* [Explore your web performance metric summary and reports](overview.md#explore-your-web-performance-metric-summary-and-reports)
* [Frequently asked questions about web performance scores](overview.md#faq)

## Measuring your web performance

Web performance is measured by Core Web Vitals, which include the following performance measurements:

* **Largest Contentful Paint (LCP)** measures loading speed, based on how fast the largest element or main content becomes visible to visitors. A good LCP score is achieved when the main content is loaded within 2.5 seconds from the start of the page load.
* **Interaction to Next Paint (INP)** measures interactivity based on how long it takes the page to become responsive to most user actions, such as clicking a link or a button. An INP score of less than 200 milliseconds is considered a good performance as the page becomes interactive quickly.
* **Cumulative Layout Shift (CLS)** measures visual stability, based on how much the content shifts around unexpectedly when navigating around the page. A CLS score of less than 0.1 is considered a good performance.

For your web performance to be considered "good" by search engines such as Google, at least 75% of your page loads need to achieve **Good** scores across all Core Web Vitals. The web performance reports show this 75th percentile measurement to help you track your performance.

In addition to the Core Web Vitals, Google evaluates other factors, including the following examples:

* Mobile compatibility
* Safe browsing
* HTTPS security
* The absence of intrusive interstitials, which are page elements that obstruct a complete view of the content, such as promotional pop-ups or age verification

These factors together help evaluate a webpage's performance and user experience.

Learn more about [Core Web Vitals and Google search results](https://developers.google.com/search/docs/appearance/core-web-vitals).

## How web performance impacts your store

Your online store’s performance can impact the [shopping experience of your customers](overview.md#experience-and-conversion), your [conversion rate](overview.md#experience-and-conversion), and your store's [discoverability](overview.md#discoverability).

Learn more about [why web performance matters](https://performance.shopify.com/blogs/blog/why-web-performance-still-matters).

### Experience and conversion

When your online store loads quickly and interactions are smooth, it provides a positive experience to all visitors regardless of their device or connection speed. If a site is slow or difficult to navigate, then visitors are more likely to [leave before they buy something](https://www.shopify.com/enterprise/site-performance-page-speed-ecommerce). By improving your store's web performance, you can enhance user experience and increase [conversion rates](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/behaviour-reports#online-store-conversion-over-time).

### Discoverability

Search engines such as Google [use page speed as a ranking factor](https://webmasters.googleblog.com/2020/05/evaluating-page-experience.html). If your online store pages perform poorly across the Core Web Vitals, then they might be ranked lower, even if your store is otherwise [optimized for search engines](https://help.shopify.com/en/manual/promoting-marketing/seo). By improving web performance, you're improving your store's chances of being ranked higher in search and getting more visibility for your business.

## Online store features vs. web performance

Your online store is made up of a set of features, such as theme code, apps, images, videos, carousels, social media feeds, and analytics. These features can enhance the visitor experience and extend your site's capabilities.

However, each feature that you add to your online store can impact your store's Core Web Vitals. Some features can slow down your site or create unexpected behaviors that can impact user experiences.

When you consider adding a feature to your store, you should weigh the benefits of the feature against its impact to the Core Web Vitals. You might need to find the balance between user experience and web performance.

Ask yourself the following questions when considering features for your store:

* **What will help customers make the decision to purchase from the store?**
  + For example, consider whether your customers would prefer a simple homepage with links to detailed product pages, or a more powerful home page where they can quickly view and buy products.
* **What functionality should exist at the top of the page to drive conversion?**
  + For example, branding elements, featured images, and a checkout cart are all features that can impact performance but increase conversion.
* **What functionality can load later as customers scroll down the page?**
  + For example, analytics and product reviews don't need to be loaded immediately when a customer visits your store. You might need to consult your theme or app developers to understand if a feature is loading right away.

## Explore your web performance metric summary and reports

You can learn how your store performs across the Core Web Vitals by viewing your [web performance reports](web-performance-reports.md). The reports and performance metric summary display how your store ranks across all 3 Core Web Vitals and provides actionable insights for improving.

You can also explore [factors that impact your web performance](improving-web-performance.md) and how to address them.

## Frequently asked questions about web performance scores

* [**Why don't I have scores yet?**](overview.md#no-scores)
* [**Why do I have traffic but no Core Web Vital scores?**](overview.md#traffic-no-scores)
* [**Why do I have scores for some metrics but not others?**](overview.md#some-scores)
* [**Why did one of my scores change?**](overview.md#scores-change)
* [**Why are the scores on my web performance reports different from other tools?**](overview.md#different-scores-tools)

### Why don't I have scores yet?

The following are some reasons why you might not have a score for your core web vitals yet:

* Your store is password-protected: If your online store is password-protected, then you won’t have the real-user traffic necessary to generate Core Web Vitals. You need to remove the password page to allow users to visit your site.
* You don’t have traffic yet: You might not have had any page views to your online store to generate real-user metrics. If you haven't had any traffic, then you can use a free performance analysis using synthetic data, such as [PageSpeed Insights](https://pagespeed.web.dev).

### Why do I have traffic but no Core Web Vital scores?

Core Web Vitals are a Google product and currently only available on Firefox and Chromium-based browsers. Modern browsers are built upon similar technologies and so the existing data still represents an accurate depiction of how your users experience the website.

Both Largest Contentful Paint and Interaction To Next Paint are anticipated to become available in one of the upcoming Safari versions. Learn more about cross-browser interoperability in the [Interop 2025 project](https://webkit.org/blog/16458/announcing-interop-2025/#core-web-vitals).

### Why do I have scores for some metrics but not others?

Each metric measures a different aspect of performance and user interactions. For example, Largest Contentful Paint measures page load, whereas Interaction to Next Paint measures interactions with buttons or links. If there are no interactions with the elements on the page, then the INP metric might not have a score.

### Why did one of my scores change?

Scores can fluctuate due to traffic amount or changes made to your online store. If there are big fluctuations due to low traffic, then try changing to a weekly or monthly filter.

Your scores can also change when you make changes to your online store. For example, you might have imported several new products, created several new collections, changed your theme, or introduced a new app. Learn about the factors that can [impact your online store performance](improving-web-performance.md).

### Why are the scores on my web performance reports different from other tools?

The scores in your web performance reports might differ from other tools due to the following factors:

* The data in the web performance reports is based on the UTC standard, which might differ from other platforms' timezones.
* The web performance reports collect data differently by gathering a broader data set from all Chromium browsers (Chrome, Opera, Edge, Samsung Internet) and Firefox. Tools such as Google's PageSpeed Insights use the CrUX report for opted-in Chrome browsers only. Learn more about [CrUX data](https://web.dev/articles/crux-and-rum-differences).

### What does it mean if my store has a low performance score?

There's a balance to consider between your site's features and speed. A lower score means your store could be optimized to perform better and become more accessible to all types of customers, including those using mobile devices, slower internet connections, or older browsers.

For example, if your homepage video receives significant engagement but your homepage has a low performance score, you need to weigh whether the video provides enough value to offset the performance impact.

There's no such thing as a perfect speed score, and the closer you get to 100, the more difficult it becomes to improve further. Focus on optimizing your store for your specific business needs rather than achieving the highest possible score.

### How is my performance score calculated?

Your performance score combines data from your home page, most visited product page, and most visited collection page from the last 7 days. The system uses real user data (called Real User Metrics or RUM) from visitors using Chromium-based browsers and Firefox.

Each page score represents actual visitor experiences, not simulated tests. This means the scores reflect how real customers experience your store under various conditions.

### Why is my score different from similar stores?

Your store is compared to other Shopify stores with similar sales volumes. This comparison helps you understand your performance relative to stores of similar size and complexity.

Factors that can affect how your store compares to others include:

* The complexity of your theme and customizations
* The number and type of apps you use
* Your product catalog size and image optimization
* Your target market and customer device preferences

### When should I be concerned about my performance score?

Focus on improvement if:

* Your scores are consistently in the "Poor" range across multiple metrics
* You notice a significant drop in performance without making changes to your store
* Customer feedback indicates slow loading times or poor user experience
* Your conversion rates are declining alongside performance scores

Don't worry too much if:

* Some individual pages or dates show moderate performance while overall trends are good
* Your scores fluctuate slightly due to normal traffic variations
* You've intentionally chosen features that impact performance for business reasons
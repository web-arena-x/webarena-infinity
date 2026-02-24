# Web performance reports

Source: https://help.shopify.com/en/manual/online-store/web-performance/web-performance-reports

---

# Web performance reports

Optimizing your online store's performance can enhance your customers' shopping experience, increase your store's discoverability, and increase conversion rates. Your web performance reports can help you understand how your store performs across industry standards for loading speed, interactivity, and visual stability, known as Core Web Vitals.

The reports display how your storefront performs across Core Web Vitals: loading speed, interactivity, and visual stability. The reports contain information about desktop and mobile experiences, the distribution of experiences within given performance rankings, and display how any changes you’ve made impact your storefront experience, such as app installs, theme updates, and new code.

Due to the tracking and calculation processes, the data in this report may be delayed by up to 36 hours.

Learn more about [how web performance is measured](overview.md).

## On this page

* [View your store's web performance data](web-performance-reports.md#view-reports)
* [Web performance metric summary](web-performance-reports.md#web-performance-metric-summary)
* [Web performance over time reports](web-performance-reports.md#web-performance-over-time-reports)
* [Web performance by page URL reports](web-performance-reports.md#web-performance-by-page-url-reports)
* [Web performance by page type reports](web-performance-reports.md#web-performance-by-page-type-reports)
* [Using the web performance reports](web-performance-reports.md#how-to-use)

## View your store's web performance data

To view your store's web performance reports, you need to have the [Reports staff permission](https://help.shopify.com/en/manual/your-account/users/roles/permissions/store-permissions#analytics-permissions). To get a dashboard populated with Real User Metrics (RUM), you must [remove your online store's password protection](../themes/password-page.md#remove-password-protection-from-your-online-store).

You can access the web performance over time reports from the performance metric summary on the **Themes** page, or you can access all your web performance reports from the **Reports** list in your Shopify admin.

### View the performance metric summary

The performance metric summary displays on the [**Themes**](https://admin.shopify.com/themes) page of your Shopify admin, and gives you a quick summary of your store's 3 Core Web Vitals over time. Learn more about the [performance metric summary](web-performance-reports.md#web-performance-metric-summary).

#### Steps:

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Optional: Use the date picker to display the data from the selected date range. You can select between **Today**, **Last 7 days**, and **Last 30 days**.
3. Optional: Use the performance metric summary to access a report:

   * Click **LCP P75 (ms)** to access the [**Largest Contentful Paint: Over Time** report](https://admin.shopify.com/analytics/reports/largest_contentful_paint_over_time).
   * Click **INP P75 (ms)** to access the [**Interaction to Next Paint: Over Time** report](https://admin.shopify.com/analytics/reports/interaction_to_next_paint_over_time).
   * Click **Cumulative Layout Shift** to access the [**Cumulative Layout Shift: Over Time** report](https://admin.shopify.com/analytics/reports/cumulative_layout_shift_over_time).
   * Optional: Click **Sessions by Device Type** to access the [**Sessions by device type** report](https://admin.shopify.com/analytics/reports/sessions_by_device_type).

### View the web performance reports

There are multiple web performance reports available in the [**Reports**](https://admin.shopify.com/analytics/reports) list of your Shopify admin. You can customize these reports to display the data that you want using the configuration panel or ShopifyQL query editor.

Learn more about [using Shopify reports](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types).

#### Steps:

1. From your Shopify admin, go to **Analytics** > [**Reports**](https://admin.shopify.com/analytics/reports).
2. In the **Search reports** field, search for the report that you want to access directly:

   * To display all web performance reports, search using a colon `:`.
   * To display the reports about Largest Contentful Paint, search using the keyword `contentful`.
   * To display the reports about Interaction to Next Paint, search using the keyword `next`.
   * To display the reports about Cumulative Layout Shift, search using the keyword `cumulative`.
3. Click the name of the report that you want to open.

## Web performance metric summary

The web performance metric summary gives you insights into the performance of your online store, based on real user data from the past 30 days. It evaluates your store against the 3 [Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals), and assigns a ranking of **Good**, **Moderate**, or **Poor** to each metric. This ranking reflects the top 75% of user experiences.

The web performance metric summary includes the following information:

* Your store's Largest Contentful Paint (LCP) ranking, which measures loading speed, based on how fast the largest element on the screen becomes visible.
* Your store's Interaction to Next Paint (INP) ranking, which measures interactivity, based on the amount of time it takes for the browser to paint the next frame or display a change on screen after a user interaction, such as clicking a link or button.
* Your store's Cumulative Layout Shift (CLS) ranking, which measures visual stability, based on how much the content shifts around unexpectedly when navigating around the page.
* Your store's online visitor sessions, divided by device type.

The following are the available rankings for the 3 Core Web Vitals in the web performance metric summary:

Table listing the target metrics for the 3 Core Web Vitals, and their descriptions.

| Core Web Vital | Ranking | Target Metric | Description |
| --- | --- | --- | --- |
| **Largest Contentful Paint (LCP)** | **Good** | Less than or equal to 2500ms | Most users experience a fast page load. |
| **Moderate** | Greater than 2500ms and less than 4000ms | Some users experience a fast page load, but there's room for improvement. |
| **Poor** | Greater than 4000ms | Most users experience a slow page load. This should be improved. |
| **Interaction to Next Paint (INP)** | **Good** | Less than or equal to 200ms | Most users experience good responsiveness on pages. |
| **Moderate** | Greater than 200ms and less than 500ms | Some users experience good responsiveness on pages, but there's room for improvement. |
| **Poor** | Greater than 500ms | Most users experience slow responsiveness on pages, which will be frustrating and should be improved. |
| **Cumulative Layout Shift (CLS)** | **Good** | Less than or equal to 0.1 | Most users experience a stable layout as the page loads. |
| **Moderate** | Greater than 0.1 and less than 0.25 | Some users experience a stable layout as the page loads, but there's room for improvement. |
| **Poor** | Greater than or equal to 0.25 | Most users experience an unstable layout as the page loads, which can annoy users and should be improved. |

If your rankings in any metric are **Moderate** or **Poor**, then you should consider using the Web Performance reports to determine what might be causing the issue, and taking steps to resolve it.

## Web performance over time reports

You can review your site's web performance over time for the 3 Core Web Vitals from your [web performance reports](web-performance-reports.md#view-reports):

* [**Largest Contentful Paint: Over Time**](https://admin.shopify.com/analytics/reports/largest_contentful_paint_over_time)
* [**Interaction to Next Paint: Over Time**](https://admin.shopify.com/analytics/reports/interaction_to_next_paint_over_time)
* [**Cumulative Layout Shift: Over Time**](https://admin.shopify.com/analytics/reports/cumulative_layout_shift_over_time)

By default, the data displays for the 75th percentile of the relevant Core Web Vital, in milliseconds, but you can use the report's [configuration panel](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/reports-overview#configuration-panel) to customize the report to meet your needs. You can also adjust various **Dimensions** and **Filters** such as time range, date grouping, and device type, to best reflect the traffic to your site. Learn more about [customizing your reports](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/custom-reports).

The line chart visualization displays how changes made to your online store, such as app installations, theme updates, and new code, have impacted the Core Web Vital over time. This visualization contains the following additional elements:

* The web performance **Summary** score, factored over the selected date range.
* Event annotation tags, represented as numbered vertical lines in the graph, which you can hover over to view more information about potential changes in your store that could affect the web performance.
* Web performance score thresholds, represented by a horizontal line across the graph, which indicate the threshold between **Good**, **Moderate**, and **Poor** results.

The bar chart in the distribution metric column of the [data table](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/reports-overview#data-table) displays how many page visits fall into each performance category: good (green), moderate (yellow), or poor (red).

## Web performance by page URL reports

You can review your site's web performance for each individual page URL for the 3 Core Web Vitals from your [web performance reports](web-performance-reports.md#view-reports):

* [**Largest Contentful Paint: Page URL**](https://admin.shopify.com/analytics/reports/largest_contentful_paint_by_page_url)
* [**Interaction to Next Paint: Page URL**](https://admin.shopify.com/analytics/reports/interaction_to_next_paint_by_page_url)
* [**Cumulative Layout Shift: Page URL**](https://admin.shopify.com/analytics/reports/cumulative_layout_shift_by_page_url)

By default, the data displays the events for the 75th percentile of the relevant Core Web Vital, in milliseconds, but you can use the report's [configuration panel](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/reports-overview#configuration-panel) to customize the report to meet your needs. You can also adjust various **Dimensions** and **Filters** such as time range, date grouping, and device type, to best reflect the traffic to your site. Learn more about [customizing your reports](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/custom-reports).

These reports don't contain a graphical visualization. They display only the [data table](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/reports-overview#data-table). By default, the primary dimension in the table is **Page path**. The bar chart in the distribution metric column displays how many page visits fall into each performance category: good (green), moderate (yellow), or poor (red).

## Web performance by page type reports

You can review your site's web performance separated by page type for the 3 Core Web Vitals from your [web performance reports](web-performance-reports.md#view-reports):

* [**Largest Contentful Paint: Page Type**](https://admin.shopify.com/analytics/reports/largest_contentful_paint_by_page_type)
* [**Interaction to Next Paint: Page Type**](https://admin.shopify.com/analytics/reports/interaction_to_next_paint_by_page_type)
* [**Cumulative Layout Shift: Page Type**](https://admin.shopify.com/analytics/reports/cumulative_layout_shift_by_page_type)

By default, the data displays for the 75th percentile of the relevant Core Web Vital, in milliseconds, but you can use the report's [configuration panel](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/reports-overview#configuration-panel) to customize the report to meet your needs. You can also adjust various **Dimensions** and **Filters** such as time range, date grouping, and device type, to best reflect the traffic to your site. Learn more about [customizing your reports](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/custom-reports).

These reports don't contain a graphical visualization. They display only the [data table](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/reports-overview#data-table). By default, the primary dimension in the table is **Page type**. The bar chart in the distribution metric column displays how many page visits fall into each performance category: good (green), moderate (yellow), or poor (red).

## Using the web performance reports

After your web performance metric summary has a sufficient amount of data to display a score for the Core Web Vitals, you can use the performance reports to narrow down potential issues that might be impacting your web performance scores. When you've identified pages or elements that might be impacting your web performance, you can make an informed decision on where and how you want to optimize your store.

Keep in mind that certain factors are beyond your control, such as a customer's device, network, and location. Customers around the world visit your store using different devices and internet connections, which means your store might load faster or slower for them depending on these factors. As long as the overall metric is good, don't worry too much if some dates or pages fall into the moderate or poor categories.

You can follow these general steps to investigate opportunities for web performance optimization:

1. Review the [performance metric summary](web-performance-reports.md#web-performance-metric-summary) for an overview of which Core Web Vital scores might need optimization.
2. For a specific Core Web Vital, use the 3 associated reports to drill-down further into the data for your store:
   * Use the **Over Time** reports to investigate when impacts to a particular score might have occurred.
   * Use the **Page Type** reports to investigate whether certain [page templates](../themes/theme-structure/templates.md) are indicating an impact to web performance.
   * Use the **Page URL** reports to investigate whether specific pages are indicating an impact to web performance.
3. Based on the time period, pages, and elements that you identify as impacting your web performance, you can then move forward with improving your Core Web Vital score with more confidence in what specifically could be causing the issue.

To learn how to improve online store performance, visit [*Improving your online store performance*](improving-web-performance.md).
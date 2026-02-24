# Storefront search

Source: https://help.shopify.com/en/manual/online-store/storefront-search

---

# Storefront search

When customers search your online store, the results that display are built on an AI-powered search infrastructure:

* Core [search features](storefront-search.md#online-store-search) are available by default to all Shopify merchants that have an online store. This includes predictive search and typo tolerance, where typing mistakes are automatically matched to words that closely resemble the misspelling.
* The [Shopify Search & Discovery app](storefront-search.md#search-and-discovery) includes settings and features that allow you to further customize your store's search experience, as well as set up product search filters and product recommendations.

## On this page

* [Online store search](storefront-search.md#online-store-search)
* [Shopify Search & Discovery app](storefront-search.md#search-and-discovery)
* [Custom storefronts and headless search](storefront-search.md#custom-storefronts-and-headless-search)

## Online store search

Your online store has built-in, AI-powered search functionality that operates from a search bar or search field on your website.

Your customers can input their search term and get results from across all of your store's products, blog posts, and pages.

### Read more

* [Search behavior in your online store](storefront-search/search-behavior.md)
* [Predictive search](storefront-search/predictive-search.md)
* [Managing searchability](storefront-search/managing-searchability.md)

## Shopify Search & Discovery app

[Shopify Search & Discovery](https://apps.shopify.com/search-and-discovery)

Install Shopify Search & Discovery from the Shopify App Store.

The [Shopify Search & Discovery](https://apps.shopify.com/search-and-discovery) app gives you more control over how customers discover your products online. You can use the app to customize product search results and product recommendations in your online store in the following ways:

* Create custom filters to let customers refine their search and collection pages by multiple categories, which can display more relevant results.
* Create synonym groups to ensure that different words with the same meaning return the same results.
* Feature particular products in search results.
* Adjust result types in search and predictive search.
* Recommend related products on product pages to add to the recommendations that are automatically generated.

To use certain features of Shopify Search & Discovery, your staff members need the following [staff permissions](https://help.shopify.com/en/manual/your-account/users/roles/permissions):

* **Products**: Required for editing product recommendations, product boosts, and filters.
* **Online Store Search and Navigation**: Required for editing filters and synonyms.
* **Reports**: Required for viewing analytics.

### Read more

* [Adding filters with Search & Discovery](storefront-search/search-and-discovery-filters.md)
* [Modifying search with Search & Discovery](storefront-search/search-and-discovery-modify-search.md)
* [Customize product recommendations with Search & Discovery](storefront-search/search-and-discovery-recommendations.md)
* [Shopify Search & Discovery reports and analytics](storefront-search/search-and-discovery-analytics.md)

## Custom storefronts and headless search

If you're building a custom storefront or headless commerce experience, then you can use the Shopify Search & Discovery app features with the [Storefront API](https://shopify.dev/docs/api/storefront). This allows you to implement the same search capabilities available in Shopify themes in your custom storefront.

The Storefront API provides search and predictive search queries that support:

* Natural language search functionality
* Product boosts and synonym groups configured in the Search & Discovery app
* Custom filters for product availability, price, and product attributes
* Predictive search dropdown interfaces

To optimize search performance in custom storefronts, set up [search tracking](https://shopify.dev/docs/custom-storefronts/building-with-the-storefront-api/search-discovery/search-tracking) to help Shopify's search infrastructure learn from customer interactions and improve results.

For more information about implementing search in custom storefronts, refer to the [Search and discovery developer documentation](https://shopify.dev/docs/custom-storefronts/building-with-the-storefront-api/search-discovery).
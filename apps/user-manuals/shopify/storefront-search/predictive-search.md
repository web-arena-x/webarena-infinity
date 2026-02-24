# Predictive search

Source: https://help.shopify.com/en/manual/online-store/storefront-search/predictive-search

---

# Predictive search

Predictive search displays suggested results as you type. It helps your customers refine their search without being redirected to a search results page, and quickly explore your store by seeing top results for suggested search terms, products, collections, and more.

You can customize the behavior of predictive search with the free first-party [Shopify Search & Discovery](../storefront-search.md#search-and-discovery) app.

## On this page

* [Considerations for predictive search](predictive-search.md#considerations-for-predictive-search)
* [Search behaviour](predictive-search.md#search-behaviour)
* [Searchable properties](predictive-search.md#searchable-properties)
* [Searchable translations](predictive-search.md#searchable-translations)

## Considerations for predictive search

Review the following considerations for using predictive search on your online store.

### Plan requirements

Predictive search is available as part of your online store search only if your store is on one the following [pricing plans](https://www.shopify.com/pricing):

* Grow
* Advanced
* Plus

### Result limits

Predictive search presents customers with a limited set of highly relevant results.

By default, a maximum of 10 possible results display across all the queried result types. Because of this limit, there are typically more results available on the dedicated [search results page](../storefront-search.md) of your store.

### Theme compatibility

For predictive search to display on your store, it must be a feature of your published theme. Predictive search is available for [compatible themes](../themes/managing-themes/versions.md#features), and can be added to custom storefronts using the [Predictive Search API](https://shopify.dev/docs/api/ajax/reference/predictive-search).

### Language compatibility

Your store's primary locale determines which predictive search behaviors are supported.

* Collection suggestions are based on the store's primary language. A customer's search won't be compared to a collection's translated content.
* Query suggestions are available in English only, and require both the store's primary language and the customer's online store session to be in English.
* Predictive search isn't available in all languages. Refer to the developer documentation for the complete [list of supported languages](https://shopify.dev/docs/api/ajax/reference/predictive-search#supported-languages).

## Search behaviour

Predictive search can return product, page, blog post, collection, and query results.

Query results are suggested search terms that are based on the words and phrases from your product catalog, as well as from past customer searches. Choosing a query result will return a page of search results for that search term.

By default, predictive search will return query, product, collection, and page results. You can customize which types of results change this setting in the free first-party [Shopify Search & Discovery](https://apps.shopify.com/search-and-discovery) app.

## Searchable properties

Search results for predictive search are based on the searchable properties of the different possible result types. By default, the following properties are searched:

Default searchable properties for predictive search

| Resource | Property |
| --- | --- |
| Products | Title |
| Product type |
| Variant title |
| Vendor |
| Pages | Title |
| Collections | Title |
| Blog posts | Title |

## Searchable translations

You can translate your store's content with apps, such as Shopify's [Translate & Adapt](https://help.shopify.com/en/manual/international/localization-and-translation#requirements) app.

For more information on translations and searchable properties, refer to the developer documentation on the [Predictive Search API](https://shopify.dev/docs/api/ajax/reference/predictive-search#searchable-properties).
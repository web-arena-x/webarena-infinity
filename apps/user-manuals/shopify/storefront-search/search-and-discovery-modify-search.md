# Modifying search with Shopify Search & Discovery

Source: https://help.shopify.com/en/manual/online-store/storefront-search/search-and-discovery-modify-search

---

# Modifying search with Shopify Search & Discovery

You can use the Search & Discovery app to modify online store search and [predictive search](predictive-search.md). You can make the following customizations to your online store search results:

* Adjust the type results returned in search results.
* Assign specific search terms to your products to feature them in search results.
* Create synonym groups to ensure that different words with the same meaning return the same results.
* Adjust the display of [combined listings products](https://help.shopify.com/en/manual/products/combined-listings-app) in search results.

## On this page

* [Considerations for customizing search results](search-and-discovery-modify-search.md#considerations-for-customizing-search-results)
* [Semantic understanding](search-and-discovery-modify-search.md#semantics)
* [Adjusting search result type](search-and-discovery-modify-search.md#search-result-types)
* [Adjusting combined listings](search-and-discovery-modify-search.md#search-combined-listings)
* [Customizing product boosts](search-and-discovery-modify-search.md#product-boosts)
* [Customizing synonyms](search-and-discovery-modify-search.md#synonyms)
* [Adjusting combined listings](search-and-discovery-modify-search.md#search-combined-listings)

## Considerations for customizing search results

Review the following considerations for customization your online store search results with the Search & Discovery app:

* Product boosts aren't applied when a search query contains [search syntax](../storefront-search.md).

## Semantic understanding

Semantic search is one of Shopify's AI-powered online store search behaviors that uses related words, concepts, categories and other contexts to improve and expand search results.

The online store search's semantic understanding checks for related words and categories, and relationships between concepts.

Semantic understanding uses attributes of your products such as the product's description, and image data, such as text that's part of the image itself and colors, to improve search results.

For example, you have an online store that sells shoes in different styles and for different occasions. A customer searches for `christmas party shoes`. You don't have any products that use the terms `christmas` or `party` anywhere in your products, but you do sell pumps that come in multiple colors, including red.

Instead of returning only search results containing the words `christmas`, `party`, or `shoes`, your online store search results expand to include related products by associating related terms. For example, `christmas` is associated with the colors `green` and `red`, and `party shoes` can be associated with common shoe styles for parties, such as `pumps`.

As a result, the red pumps display in the customer's search results.

### Considerations for semantic search

Semantic search capability in your online store search is available only if your store meets the following requirements:

* Your store has fewer than 200,000 products.
* Your store is on one the following [pricing plans](https://www.shopify.com/pricing):
  + Grow
  + Advanced
  + Plus
* Semantic search capability doesn't apply to [predictive search](predictive-search.md).
* Semantic search capibility isn't supported for the Japanese locale.

### Activating semantic search

You can activate semantic search from the **Settings** page of the Search & Discovery app.

#### Steps:

1. From your Shopify admin, go to **Apps** > [**Search & Discovery**](https://admin.shopify.com/apps/search-and-discovery).
2. Click **Settings**.
3. Scroll to the **Search relevance** section.
4. Optional: To test the feature, click **Try it out**. A theme preview opens with Semantic Search activated.
5. Click **Turn on** to activate Semantic Search.

## Adjusting search result type

Your store's search functions can return different types of results, such as products, pages, and blog posts. To keep your search results as relevant as possible for your customers, you can specify which types of results you want your [online store search](../storefront-search.md) and [predictive search](predictive-search.md) to return. The following settings can be adjusted in the **Settings** section of your Shopify Search and Discovery app, but these settings can be [overwritten by your published theme](search-and-discovery-modify-search.md#type-requirements).

**Search results:** Choose what result types are requested for the [search results page](../storefront-search.md) of your online store. The options that you can select are product, page and blog post results. By default, all result types are requested.

**Predictive search results:** Choose what result types are requested for the [predictive search](https://shopify.dev/docs/themes/navigation-search/search/predictive-search) component of your online store. The options that you can select are product, page, blog post, collection and query results. By default, a request asks for query, product, collection and page results.

**Out of-stock-products:** Choose how to display results for unavailable products for both the search results page and predictive search. Out of stock products can be displayed, hidden or placed last in the returned results. The setting adjusts the behavior for both search and predictive search. By default, unavailable products are displayed after all other matching results.

### Requirements

Search result type settings apply when your online store theme does not specify the `type` query parameter in requests to the [online store search](https://shopify.dev/themes/navigation-search/search) or [predictive search](https://shopify.dev/api/ajax/reference/predictive-search) endpoints. If your theme sends a `type` query parameter, then the result type setting is overwritten. Contact your theme's developer if the search settings changes aren't displayed in your online store.

## Adjusting combined listings

You can choose how [combined listing](https://help.shopify.com/en/manual/products/combined-listings-app) products display in your search results and [predictive search](predictive-search.md) in the **Settings** section of your Shopify Search and Discovery app. By default, only child products are displayed. However, you can update the app settings to display parent products only, or both parent and child products.

To have access to this setting, your store must contain combined listing products, or have the [Combined Listings app](https://apps.shopify.com/combined-listings) installed.

#### Steps:

1. From your Shopify admin, go to **Apps** > [**Search & Discovery**](https://admin.shopify.com/apps/search-and-discovery).
2. Click **Settings**.
3. In the **Products** section, select one of the following options for search results for combined listings:

   * Click **Only show child products** to display only the child products of combined listings.
   * Click **Only show parent products** to display only the parent products of combined listings.
   * Click **Show both** to display both the parent and child products of combined listings.
4. Click **Save**.

## Customizing product boosts

You can assign specific search terms to your products to help them display in search results. When a customer searches your store using the search terms that you have assigned to a product, the product ranks higher in the search results on your online store. For example, suppose that you sell coffee and have released a new decaf coffee variant. To help increase its visibility in your store, you can assign the search term "decaf coffee" to your new product for it to always display when a customer uses that search term in your store's search.

### Requirements

A product's position in search results is boosted only if the product is available for sale. Sold out products are listed at the end of search results so that customers can find and purchase currently available products.

Product boosts might be overridden based on your store's [setting](search-and-discovery-modify-search.md#search-combined-listings) for displaying combined listings in search.

### Best practices for product boosts

Online store search is designed to return the most relevant search results. The results are adjusted based on changes to your products, collections, and customer activity. When you boost a product, it's listed above the search results that are usually returned for the related queries. You can use the following best practices for product boosts to ensure that you're building an effective customer experience:

* Boost a single product, or small number of products, for specific search terms. Boosting a large number of products might cause other relevant products to display lower in search results.
* It isn't necessary to boost common misspellings of search terms or both the singular and plural version of search terms. Shopify has built-in strategies to account for this when creating search results. Learn more about how [online store search in the online store](../storefront-search.md) works.
* Consider [creating a synonym group](search-and-discovery-modify-search.md#create-a-synonym-group) instead of boosting search terms if you're trying to associate common customer search terms with your products. Synonyms won't boost products to the beginning of search results necessarily, but they're a useful strategy for improving the positioning of products in search results.

### Create a product boost

Search terms can be multiple words. A maximum of 10 search terms can be added to a product boost.

#### Steps:

1. From your Shopify admin, go to **Apps** > [**Search & Discovery**](https://admin.shopify.com/apps/search-and-discovery).
2. Click **Search**, and then click **Product boosts**.
3. Click **Create product boost**.
4. Select the products that you want to promote in search results.
5. For each search term that you want to add, type in the term and then click **Add**.
6. Click **Save**.

### Edit product boosts with metafields

You can use [metafields](https://help.shopify.com/en/manual/custom-data/metafields) to edit product boosts.

#### Steps:

1. From your Shopify admin, go to **Apps** > [**Search & Discovery**](https://admin.shopify.com/apps/search-and-discovery).
2. Select multiple products from the **Product boosts** page.
3. Click **Bulk edit** to open the [Bulk Editor](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/bulk-editing).
4. Choose product boosts for each product, and then click **Save**.

You can also edit metafields from other apps, such as [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow).

The changes that you make to the metafield "Search product boosts" are synced with the product boosts in the Search & Discovery app.

## Customizing synonyms

Although you give your products a specific name, some of your customers might be searching for that product using a different term. For example, you might sell bags called `slings`, but some customers know them as `belt bags`. To help those customers find the bags that they're searching for, you can create a synonym group for `belt bags` and `slings`. Shopify treats these terms as exact matches for one another, which improves the relevancy of a customer's search result.

### Considerations

Review the following consideration for how synonyms can impact search results:

* If a synonym has multiple words separated by a space, such as "belt bag", then the synonym is used as a [phrase search](search-behavior.md#phrase-search) when returning synonymous search results. A phrase search returns results where the words appear in the exact order of the synonym. For example, if you have a synonym group with both `sling` and `belt bag` then search results are affected in the following ways:
* Searching for `sling` will match products that contain the word `sling` and products that contain the phrase `belt bag`.
* Searching for `belt bag` will match products that contain the words `belt` and `bag`, and products that contain the word `sling`.
* Synonyms aren't considered in search results in the following scenarios:
* Synonyms aren't used for matches on product `sku` and `barcode` fields.
* Synonyms aren't used when a search query contains [search syntax](search-behavior.md#search-syntax).

### Requirements

Review the following considerations for creating custom synonym groups, and behaviors of synonyms that can impact search results.

Custom synonym groups have the following requirements:

* Each synonym can be a single word or up to 5 words. There is a maximum of 20 synonyms per synonym group, and a maximum of 1000 synonyms for the entire store.
* Each synonym must be unique to your whole store, there can't be the same synonym in multiple synonym groups.

### Best practices

You can use the following best practices for synonyms to ensure that you're building an effective customer experience:

* Review your store's report on [top online store search results with no results](https://help.shopify.com/en/manual/reports-and-analytics/shopify-reports/report-types/default-reports/behaviour-reports#searches-with-no-results) to determine if you can create relevant synonyms for any of the search terms that return no results for customers.
* Synonyms in a group should be clear substitutes for one another. Avoid creating synonym groups with loosely related terms, such as having both "men" and "boys" in the same group, as it might cause relevant results to display lower in search results.
* You don't need to create synonyms for common misspellings of search terms. Shopify has built-in strategies to account for this when creating search results. Learn more about [typo tolerance in online store search](search-behavior.md#typo-tolerance).
* If a synonym group contains a compound word, consider adding its open, closed, or hyphenated versions. For example: "belt bag", "beltbag" and "belt-bag". Alternate spellings of compound words aren't considered in the default online store search behavior, but might be popular among your customers.

### Create a synonym group

You can create custom synonym groups in the **Synonyms** section of the Search & Discovery app.

#### Steps:

1. From your Shopify admin, go to **Apps** > [**Search & Discovery**](https://admin.shopify.com/apps/search-and-discovery).
2. Click **Search**.
3. Click **Synonyms**, and then click **Create synonym group**.
4. For each word or phrase, enter the term, and then click **Add**.
5. Enter a synonym group title. Synonym group titles are used by the app to help display your synonym groups. The title doesn't affect search results on your online store.
6. Click **Save**.

## Adjusting combined listings

You can choose how [combined listing](https://help.shopify.com/en/manual/products/combined-listings-app) products display in your search results and [predictive search](predictive-search.md) in the **Settings** section of your Shopify Search and Discovery app. By default, only child products are displayed. However, you can update the app settings to display parent products only, or both parent and child products.

To have access to this setting, your store must contain combined listing products, or have the [Combined Listings app](https://apps.shopify.com/combined-listings) installed.

#### Steps:

1. From your Shopify admin, go to **Apps** > [**Search & Discovery**](https://admin.shopify.com/apps/search-and-discovery).
2. Click **Settings**.
3. In the **Products** section, select one of the following options for search results for combined listings:

   * Click **Only show child products** to display only the child products of combined listings.
   * Click **Only show parent products** to display only the parent products of combined listings.

* Click **Show both** to display both the parent and child products of combined listings.

4. Click **Save**.
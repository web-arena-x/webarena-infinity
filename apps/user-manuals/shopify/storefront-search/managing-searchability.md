# Managing searchability

Source: https://help.shopify.com/en/manual/online-store/storefront-search/managing-searchability

---

# Managing searchability

You can manage searchability for your products, pages, and blog posts in the following ways:

* Adjust the publishing status to add or remove products from your store, or [set the product status as **Unlisted**](https://help.shopify.com/en/manual/products/details/product-details-page#unlisted-products) which means the products don't display in Shopify-powered [collection pages](https://help.shopify.com/en/manual/products/collections), [search results](search-behavior.md) including [predictive search](predictive-search.md), or [product recommendations](search-and-discovery-recommendations.md), or in [Shopify Catalog](https://help.shopify.com/en/manual/promoting-marketing/seo/shopify-catalog).
* Install the [Search & Discovery](https://apps.shopify.com/search-and-discovery) app to customize search results for Shopify's built-in storefront search.
* Adjust your theme's code to customize search results.

## On this page

* [Customizing your search](managing-searchability.md#customizing-your-search)
* [Making products, pages, and blog posts searchable](managing-searchability.md#searching-for-products-pages-articles)
* [Hiding products, pages, and blog posts from search engines and sitemaps](managing-searchability.md#search-hide-resources)
* [Bulk editing search visibility](managing-searchability.md#bulk-editing-search-visibility)
* [Troubleshooting search visibility issues](managing-searchability.md#troubleshooting-search-visibility-issues)

## Customizing your search

You can customize your search results, such as limiting the type of results and boosting specific products in search results, with the [Search & Discovery](https://apps.shopify.com/search-and-discovery) app.

Learn more about the Search & Discovery app in the [app's documentation](../storefront-search.md#search-and-discovery).

For more advanced customizations, you can edit your theme code to change the how search results are requested. This type of customization requires knowledge of web design languages such as HTML, CSS, JavaScript, and [Liquid](https://shopify.dev/docs/api/liquid). Learn more about customizing at [Shopify.dev](https://shopify.dev/themes/navigation-search/search).

## Making products, pages, and blog posts searchable

Products, pages, and blog posts need to be published on your online store to be returned in search results. In addition, resource types that are [hidden from search engines](managing-searchability.md#search-hide-resources) aren't searchable.

To make products, pages, and blog posts visible on your online store, set the following settings in your Shopify admin:

List of visibility settings on products, pages, and blog posts.

| Resource Type | Visibility settings |
| --- | --- |
| Product | Publish your product in the [Online Store channel](https://help.shopify.com/en/manual/products/add-update-products) |
| Page | [Publish](../add-edit-pages.md#publish-or-unpublish) the page |
| Blog post | Set the blog post to [visible](../blogs/publishing-blogs.md#set-visibility-in-bulk) |

## Hiding products, pages, and blog posts from search engines and sitemaps

You can hide specific products, blog posts, or pages from search engines with the following methods:

* [Hiding a product using unlisted product status](managing-searchability.md#unlisted)
* [Adding a custom metafield](managing-searchability.md#seo-hidden-metafield)
* [Adding customer metadata with the GraphQL Admin API](https://shopify.dev/api/examples/marketing-seo#hide-a-resource-from-search-engines-and-sitemap)
* [Adding metatags to your theme code](https://help.shopify.com/en/manual/promoting-marketing/seo/hide-a-page-from-search-engines#metatags)

### Hiding a product using unlisted product status

If you want to have a product discoverable only by direct URL, then you can unlist your product.

When you set a product as **Unlisted**, the product is hidden from internet search, [Shopify Catalog](https://help.shopify.com/en/manual/promoting-marketing/seo/shopify-catalog), and your store's sitemap. Unlisted products also don't display in Shopify-powered [collection pages](https://help.shopify.com/en/manual/products/collections), [search results](search-behavior.md) including [predictive search](predictive-search.md), or [product recommendations](search-and-discovery-recommendations.md) in your storefront.

Learn more about [unlisted product status](https://help.shopify.com/en/manual/products/details/product-details-page#unlisted-products).

### Adding a custom metafield in your Shopify admin

You can add a [custom metafield](https://help.shopify.com/en/manual/custom-data/metafields) of `seo.hidden` to a page, blog post, or product in your Shopify admin, and then set the metafield value to `1` to hide the page, blog post, or product from sitemaps, search engines, and your [online store search](../storefront-search.md).

`seo.hidden` is a system metafield that can be used by third-party apps for data storage when they're hiding a resource from search engines and sitemaps. If you receive a message that says **Namespace and key. seo.hidden. Namespace and key are already taken. View metafields without a definition**, then `seo.hidden` is being used by third-party apps and isn't available to modify in the Shopify admin. If you want to add definitions to each content type that's already using `seo.hidden`, then you can [create a definition for existing metafields](https://help.shopify.com/en/manual/custom-data/metafields/metafield-definitions/migrating-metafields-to-a-definition#definitions-for-existing-metafields).

### Considerations for using a custom metafield with products

If you want a product to be accessible only by using a direct URL, then consider [setting the product status as **Unlisted**](https://help.shopify.com/en/manual/products/details/product-details-page#unlisted-products) instead of using the `seo.hidden` metafield. An unlisted product is hidden from sitemaps and search engines, and it also doesn't display in your store's Shopify-powered collection pages, search results, or product recommendations, or in [Shopify Catalog](https://help.shopify.com/en/manual/promoting-marketing/seo/shopify-catalog).

If a product has **Unlisted** status and the `seo.hidden` metafield is set to `1`, then **Unlisted** status is prioritized for how the product is displayed and discovered.

### Compare product visibility

Review the following table for a comparison of product visibility when using unlisted product status or the `seo.hidden` metafield. You can't publish unlisted products to [Shop](https://help.shopify.com/en/manual/online-sales-channels/shop).

Descriptions of the impacts of Unlisted product status and the seo.hidden metafield

| Feature/functionality | Product visibility with Unlisted status | Product visibility with seo.hidden metafield |
| --- | --- | --- |
| Internet search | ✘ | ✘ |
| [Shopify Catalog](https://help.shopify.com/en/manual/promoting-marketing/seo/shopify-catalog) | ✘ | ✘ |
| Sitemap | ✘ | ✘ |
| Storefront search | ✘ | ✘ |
| Product page (Online Store and custom storefronts) | ✔ | ✔ |
| Product page (Shop) | ✘ | ✔ |
| Storefront collections | ✘ | ✔ |
| [Product recommendations](search-and-discovery-recommendations.md) | ✘ | ✔ |
| [Shop](https://help.shopify.com/en/manual/online-sales-channels/shop) (home feed/store pages/category pages/search results) | ✘ | ✘ |
| Third-party sales channels | ✘ | ✔ |

### Create a custom metafield

1. From your Shopify admin, go to **Settings** > [**Metafields and metaobjects**](https://admin.shopify.com/settings/custom_data).
2. Under **Metafield definitions**, select the eligible resource type (**Products**, **Pages**, or **Blog posts**) that you want to hide.
3. Click or tap **Add definition**.
4. Set the following fields:

   * Give the metafield a **Name** such as `SEO Hidden`, and then select the name from the list.
   * Set **Namespace and key** to `seo.hidden`.
   * Optional: Give a brief description, such as `"Hides the resource from search engines when value is 1"`.
5. Configure the custom field values by doing the following actions:

   1. Click or tap **⊕ Select type** and then select **Integer**.
   2. Select **One value**.
   3. In the **Validations** section, set the **Maximum value** to be `1`.
6. Click **Save**.
7. In your Shopify admin, navigate to the page, blog post, or product that you want to hide from search engines.
8. In the **Metafields** section, set the value of the **SEO Hidden** metafield to `1`.
9. Click **Save**.

To make the page, blog post, or product visible to search engines again, delete the **SEO Hidden** metafield value, leaving it blank, and then save your changes.

## Bulk editing search visibility

If you need to hide multiple products from search at the same time, then you can use the Bulk Editor to modify the SEO Hidden metafield for many products simultaneously.

### Using the Bulk Editor for search visibility

#### Steps

1. From your Shopify admin, go to the Bulk Editor by visiting this URL, replacing `STORENAME` with your store name:
   `https://admin.shopify.com/store/STORENAME/bulk?edit=metafields.seo.hidden%3Anumber&resource_name=Product`
2. You can view all your products listed with their **SEO Hidden** field values.
3. Click in the **SEO Hidden** field for each product you want to hide from search.
4. Enter `1` to hide the product from search, or `0` to make it searchable again.
5. Click **Save** at the top of the page.

## Troubleshooting search visibility issues

If products aren't appearing in search results even though they're published and active, then review these common causes and solutions.

### Products missing from storefront search

**Possible causes:**

* **SEO Hidden metafield**: Products might have the `seo.hidden` metafield set to `1`. Check the product's metafields and change the value to `0` if needed.
* **Search & Discovery app settings**: If you have the [Search & Discovery](https://apps.shopify.com/search-and-discovery) app installed, check if out-of-stock products are hidden in **Search & Discovery** > **Settings** > **Out of Stock Products**.
* **Store reactivation delay**: If your store was previously inactive due to subscription issues, products might take up to 36 hours to be re-indexed for search after reactivation.
* **Bulk action delays**: Products updated through bulk actions might take several hours to appear in search results. Individual product updates typically process within a few minutes.

### Verifying search visibility

To check if a product has search visibility issues:

#### Steps

1. Navigate to the product page in your admin.
2. Add `/metafields.json` to the end of the product URL.
3. Find a metafield with:
   * **Namespace**: `seo`
   * **Key**: `hidden`
   * **Value**: `1`

If you find this metafield with a value of `1`, the product is hidden from search. Change the value to `0` to make it searchable.

### Search & Discovery app compatibility

If you're using the [Search & Discovery app](https://apps.shopify.com/search-and-discovery), then be aware that:

* App settings might override default search behavior
* Custom filters and boosts only work with Shopify's native search
* Third-party search apps might not use Shopify's search infrastructure
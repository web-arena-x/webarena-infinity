# Customize product recommendations with Shopify Search & Discovery

Source: https://help.shopify.com/en/manual/online-store/storefront-search/search-and-discovery-recommendations

---

# Customize product recommendations with Shopify Search & Discovery

Some themes have recommended products sections that display complementary and related products to customers on your product pages. These recommendations can be customized using the Shopify Search & Discovery app.

For product recommendations to display on your store, you need to use a theme that includes a [complementary products section](search-and-discovery-recommendations.md#complementary-products-block) and [product recommendations section](../themes/customizing-themes/common-customizations/add-product-recommendations.md), and then add that section to your product pages.

## On this page

* [Product recommendation requirements](search-and-discovery-recommendations.md#product-recommendation-requirements)
* [Complementary products](search-and-discovery-recommendations.md#complementary)
* [Related Products](search-and-discovery-recommendations.md#related-products)
* [Create product recommendations](search-and-discovery-recommendations.md#create-product-recommendations)
* [Edit product recommendations in bulk with metafields](search-and-discovery-recommendations.md#edit-product-recommendations-in-bulk-with-metafields)
* [Complementary products](search-and-discovery-recommendations.md#complementary-products-block)
* [Customizing the appearance of complementary products](search-and-discovery-recommendations.md#customizing-the-appearance-of-complementary-products)
* [Complementary products block settings](search-and-discovery-recommendations.md#complementary-products-block-settings)

## Product recommendation requirements

A recommended product displays on the product page only if the following criteria are met:

* It isn't sold out (for related products, the product can also display if **continue selling when out of stock** is activated; for complementary products, the product must have inventory above 0).
* It doesn't have [**Unlisted** product status](https://help.shopify.com/en/manual/products/details/product-details-page#unlisted-products).
* It has a price higher than $0.00.
* It isn't a gift card.
* It is published to your Online Store sales channel.
* It isn't currently in the visitor's cart.

For both related and complementary products, the product must be set to **Active**. If inventory quantity is 0 but **continue selling when out of stock** is activated, then the product can display in the related products list, but not in the complementary products list. Complementary products must have stock above 0 to display.

These requirements help that customers discover and purchase currently available products.

## Complementary products

Complementary products are products often bought in addition to a selected product. You can display complementary products to help customers discover new products and increase your online store sales.

### Best practices for complementary product recommendations

Recommending relevant products can lead to more sales or larger cart sizes. Use the following best practices to choose complementary product recommendations:

* Choose product recommendations that you're confident customers will find useful.
* Choose products that would be considered a good add-on to the original product.
* Choose products that are lower or equivalent in cost to the original product.

## Related Products

Related products are products that are similar to a selected product. You can display potential substitutes to help customers discover other similar products they might want to purchase.

### Best practices for related product recommendations

The products that you recommend can increase the chance that a customer will find relevant products, which can lead to increased sales. Consider the following best practices when designing a product recommendation strategy for your online store:

* Choose product recommendations that you're confident customers will find useful.
* Allow automatically generated product recommendations to display with your custom recommendations, because the automatically generated recommendations adjust to reflect changes to your products and customer activity. This will also make sure recommendations are displayed when your custom product recommendations are sold out or unpublished.
* Be sure that your [theme settings are displaying](../themes/customizing-themes/common-customizations/add-product-recommendations.md) the amount of product recommendations you want.

### Automatically generated product recommendations

Related product recommendations are automatically generated for each product in your store. When you're customizing recommendations for a product in the Search & Discovery app, you can get a preview of the generated recommendations.

Shopify has built-in strategies to adjust these product recommendations based on products that are commonly purchased together, have a similar product description, or products in related collections. Each strategy has its own requirements in order to be used:

* Purchase history: The product needs previous sales to assess buying behavior.
* Product description: Only available to merchants with an English storefront.
* Related collections: Used when recommendations based on purchase history and product descriptions aren't available.

It's not possible to edit the generated product recommendations, but you can [add your own recommendations](search-and-discovery-recommendations.md#create-product-recommendations) manually.

The generated recommendations for a product change frequently. It is common to have different recommendations when you revisit a product page as Shopify suggests new products that might be more relevant to shoppers. The product recommendations previewed in the Search & Discovery app will often be different than storefront for this reason.

### Adjusting combined listings in recommendations

You can choose how [combined listings](https://help.shopify.com/en/manual/products/combined-listings-app) display in auto-generated recommendations in the **Settings** section of the Shopify Search and Discovery app. By default, only child products are displayed. However, you can update the app settings to display parent products only, or both parent and child products.

To have access to this setting, your store must contain combined listing products, or have the [Combined Listings app](https://apps.shopify.com/combined-listings) installed.

#### Steps:

1. From your Shopify admin, go to **Apps** > [**Search & Discovery**](https://admin.shopify.com/apps/search-and-discovery).
2. Click **Settings**.
3. In the **Products** section, select one of the following options for auto-generated product recommendations for combined listings:

   * Click **Only show child products** to display only the child products of combined listings.
   * Click **Only show parent products** to display only the parent products of combined listings.
   * Click **Show both** to display both the parent and child products of combined listings.
4. Click **Save**.

## Create product recommendations

Customize product recommendations that display on your product page.

### Steps:

1. From your Shopify admin, go to **Apps** > [**Search & Discovery**](https://admin.shopify.com/apps/search-and-discovery).
2. Click **Product recommendations**, and then click **Add recommendations**.
3. Select a product that you want to customize product recommendations for.
4. Select up to 10 **Complementary products**.
5. Select up to 10 **Related products** to recommend. Set the product to display only the custom recommendations or to display both custom recommendations and automatically generated recommendations.
6. Click **Save**.

### Hiding auto-generated recommendations for a product

You can choose to hide auto-generated product recommendations for individual products. This setting must be configured for each product separately.

## Edit product recommendations in bulk with metafields

You can use [metafields](https://help.shopify.com/en/manual/custom-data/metafields) to edit product recommendations.

#### Steps:

1. From your Shopify admin, go to **Apps** > [**Search & Discovery**](https://admin.shopify.com/apps/search-and-discovery).
2. Select multiple products from the Recommendations page.
3. Click **Bulk edit** to open the [Bulk Editor](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/bulk-editing).
4. Choose product recommendations for each product and click **Save**.

You can also edit metafields from other apps, like [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow).

Edits to the following [Shopify standard metafields](https://shopify.dev/apps/metafields/definitions/standard#list-of-standard-metafield-definitions) will change the product recommendations that are displayed to visitors to your online store. The changes that you make to the metafields are synced with the Search & Discovery app.

List of Shopify standard metafields that result in changes to product recommendations on your store if you edit the metafields.

| Name | Description |
| --- | --- |
| Related products | A list of related products recommendations that you manually select. This list doesn't include recommendations generated by Shopify. |
| Related products settings | Controls how selected product recommendations are displayed. Accepted values:   * `only manual`: display only selected recommendations * `ahead`: display selected products ahead of auto-generated product recommendations |
| Complementary products | A list of complementary product recommendations that you manually select. |

## Complementary products

You can add the complementary products block to your product pages in the theme editor. Learn how to use the [Shopify Search & Discovery](https://apps.shopify.com/search-and-discovery) app to [choose complementary products](search-and-discovery-recommendations.md#complementary) for your website's product pages.

Displaying complementary products to customers makes it easier for them to discover new products, and can help increase online store sales.

The heading and layout of the complementary products block are determined by your theme.

## Customizing the appearance of complementary products

Complementary products is a *block* on the product information section of your product pages, and is only available in [compatible themes](../themes/managing-themes/versions.md#features). You can customize the appearance of your complementary products block from your product pages. You can have only one complementary product block on a product page at a time.

#### Steps:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to edit, and then click **Edit theme**.
3. Click **Products**.
4. Select **Default product**, or the product template that you want to edit.
5. Take one of the following steps:

* If your product information section has a complementary products block, then click **Complementary products**.
* If your product information section doesn't have a complementary products block, then click **+ Add block**, and then select **Complementary products**.

6. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap the **…** button.
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage themes**.
4. Find the theme that you want to edit, and then tap **Edit theme**.
5. Tap **Templates**.
6. Tap **Products**.
7. Select **Default product**, or the product template that you want to edit.
8. Take one of the following steps:

* If your product information section has a complementary products block, then tap **Complementary products**.
* If your product information section doesn't have a complementary products block, then tap **+ Add block**, and then select **Complementary products**.

9. Tap **Save**.

You can hide the complementary products block by clicking the eye icon. If you want to remove the block from your theme completely, then you can [delete the block](../themes/theme-structure/sections-and-blocks.md#remove-section-or-block).

## Complementary products block settings

You can customize how your complementary products display to your customers.

### Basic display setting

Basic display settings for complementary products block settings in Shopify.

| Setting | Description |
| --- | --- |
| **Heading** | The title of the block. |
| **Show as collapsible row** | When selected, the content displays as collapsed under a row tab. When a customer clicks a title, the tab expands to display additional content. |
| **Icon** | Select an icon to pair with your heading when complementary products are displayed as a collapsible row. |

### Product display configuration

Configuration for displaying products in the complementary products block.

| Setting | Description |
| --- | --- |
| **Maximum products to show** | Select the maximum number of complementary products to display. Select a value between 1 and 10. |
| **Number of products per page** | The number of complementary products that you want to display per slider page. Select a value between 1 and 4. |
| **Pagination style** | The style of the slider navigation that displays below the images.   * **Dots** * **Counter (default)** * **Numbers** |
| **Image ratio** | Determines the aspect ratio of the product card images.   * **Portrait** * **Square (default)** |

### Additional functionalities

Settings for additional functionalities in the complementary products block.

| Setting | Description |
| --- | --- |
| **Enable quick add button** | The "quick add" button allows customers to add a product to their cart from the product card. If the product has variants, then the button reads **Choose options** and displays the product details in a pop-up. The customers can then select their desired variants, add to cart, check out immediately with the **Buy it now** option, or else click to view a product's full details. The [**Buy it now**](../dynamic-checkout.md) option needs to be set up separately from the product page to display in the quick add options. When the **Buy it now** option isn't set up, customers can still add the product to their cart. |
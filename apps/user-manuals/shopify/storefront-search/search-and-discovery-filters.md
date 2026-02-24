# Adding filters with Shopify Search & Discovery

Source: https://help.shopify.com/en/manual/online-store/storefront-search/search-and-discovery-filters

---

# Adding filters with Shopify Search & Discovery

You can use the Shopify [Search & Discovery app](https://apps.shopify.com/search-and-discovery) to create filters for your online store that let customers refine which products are displayed on collection pages and in search results. For example, a store that sells watches could create filters for brand name, price, dial size, and water resistance.

## On this page

* [Requirements](search-and-discovery-filters.md#requirements)
* [Considerations for adding filters](search-and-discovery-filters.md#considerations)
* [Filter types](search-and-discovery-filters.md#filter-types)
* [Edit filters](search-and-discovery-filters.md#edit-filters)
* [Rename filters](search-and-discovery-filters.md#rename-filters)
* [Filter values](search-and-discovery-filters.md#filter-values)
* [Visual filters](search-and-discovery-filters.md#visual-filters)
* [Filter behavior](search-and-discovery-filters.md#filter-behavior)
* [Filter translations](search-and-discovery-filters.md#filter-translations)
* [Troubleshooting filters](search-and-discovery-filters.md#troubleshooting-filters)

## Requirements

Filters are available for any [compatible theme](../themes/managing-themes/versions.md#features), and custom storefronts that use either the [filter Liquid API](https://shopify.dev/api/liquid/objects#filter) or [Storefront API](https://shopify.dev/api/storefront) for their online store. Learn [how to display filters](../themes/customizing-themes/common-customizations/storefront-filters.md) in your [compatible theme](../themes/managing-themes/versions.md#features).

If your theme doesn't support filters, then you can still create filters in the Shopify Search & Discovery app, but they won't be displayed to customers.

You can determine whether your store's theme supports filtering by going to **Content** > [**Menus**](https://admin.shopify.com/content/menus) in your Shopify admin. If your theme doesn't support filtering, then a message is displayed in the **Collection and search filters** section.

## Considerations for adding filters

Review the following considerations for using the Shopify Search & Discovery app:

* Collections that contain more than 5,000 products don't display filters. Consider dividing large collections into smaller collections that can display filters. For example, instead of creating a single `Women` fashion collection, you can create smaller collections based on the type of apparel, such as `Tops`, `Jeans`, and `Boots`.
* A search that produces more than 100,000 results doesn't display filters.
* A filter can display a maximum of 100 filter values on your store. If your filter has more than 100 possible values, then some values won't be displayed to customers. You can reduce the number of possible filter values by [grouping similar values](search-and-discovery-filters.md#grouping-filter-values). A filter group can have a maximum of 200 unique filter values, and your store can have a maximum of 1,000 filter groups across all selected filter settings.
* In the Shopify Search & Discovery app, a filter displays a maximum of 1,000 filter values. Metafield filters might display fewer than 1,000 values because there is a limit to how many metafields in the store are checked for unique values. Filter values not displayed in the app can still be displayed on your store to customers, provided the filter is displaying fewer than 100 filter values.
* Translations aren't supported for the **Vendor** and **Tags** filter values. The product tag filter only displays to customers shopping in your store's default language. Vendor filter values are always based on your store's default language.
* Filter value translations are based on the languages published for your online store, and won't display [translations for markets](https://help.shopify.com/en/manual/international/localization-and-translation#managing-languages) set up with [international sales tools](https://help.shopify.com/en/manual/international).
* The price filter doesn't display for currencies other than your shop's default currency.

## Filter types

All stores can display the same standard filters and you can create custom filters unique to your product catalog. You can have a combination of standard and custom filters, up to a maximum of 25 filters for your store.

Each filter source can only be used one time for a store's filters. For example, if you have the **Price** filter active on your store, then **Price** is greyed out and can't be selected as the source for a new filter.

### Standard filters

Standard filters for **Availability**, **Category**, **Price**, **Product type**, **Tags**, and **Vendor** are available to all stores.

### Custom filters

Custom filters are based on the product options, [metafields](https://help.shopify.com/en/manual/custom-data/metafields), or [metaobjects](https://help.shopify.com/en/manual/custom-data/metaobjects) used in your store.

#### Product option filters

Product option filters are based on the product options you've added to your products.

For example, if you've added a "Size" product option to your clothing products with values like "Small", "Medium", and "Large", then a corresponding "Size" product option filter option will be available in the Search & Discovery app.

#### Product metafield filters

Product metafield filters are based on product metafields that are assigned to all products in the store.

#### Category metafield filters

Category metafield filters are based on product metafields that are assigned to specific [product categories](https://help.shopify.com/en/manual/products/details/product-category).

#### Variant metafield filters

Variant metafield filters are based on product variant metafields assigned to all product variants in the store.

#### Standard product attributes

Standard product attributes, derived from Shopify's [Standard Product Taxonomy](https://help.shopify.com/en/manual/products/details/product-category), are automatically created as product metafield definitions when you assign a category to your products. The associated metafields are metaobject references. The corresponding metaobject definitions are **standard** so cannot be modified (fields cannot be added, removed, or edited). One of the fields includes a **taxonomy reference value**.

In the Search & Discovery app, the sources for these attributes display as either of the following options:

* [**Product metafields**](search-and-discovery-filters.md#product-metafield-filters): When assigned to all products.
* [**Category metafields**](search-and-discovery-filters.md#category-metafield-filters): When assigned to specific product categories.

#### Metafield filters

All metafield filters, whether they are category, product, or variant metafields, are based on a metafield definition. Learn how to [add a metafield definition](https://help.shopify.com/en/manual/custom-data/metafields/metafield-definitions). You can create metafield filters for the following value types:

* Single line text
* Single line text (List)
* Decimal
* Integer
* True or false
* Metaobject reference
* Metaobject reference (List)

After your metafields are set up on your products or variants, you can select the metafield definition as a filter when [editing your filters](search-and-discovery-filters.md#edit-filters).

## Edit filters

1. From your Shopify admin, go to **Apps** > [**Search & Discovery**](https://admin.shopify.com/apps/search-and-discovery).
2. Click **Filters**, and then click **Add filter**.
3. Click the **Source** field, and then select a filter source that you want to make available to your customers.
4. Optional: [Rename the filter](search-and-discovery-filters.md#rename-filters).
5. Optional: Change the [filter behavior](search-and-discovery-filters.md#customizing-filter-behavior).
6. Optional: Change the [visual display](search-and-discovery-filters.md#visual-filters).
7. Optional: Select filter values to [group together as a single value](search-and-discovery-filters.md#grouping-filter-values).
8. Optional: [Sort filter values](search-and-discovery-filters.md#sorting-filter-values).
9. Click **Save**.

You can also reorder filters from the **Filters** section. Click and drag individual filters into the order that you want to display the filters to customers.

## Rename filters

You can change the customer-facing name of any existing filter in your store.

Changing the filter name won't change information about the filter's source. For example, renaming a filter based on a product option won't change that option's name which is displayed on the individual product pages.

#### Steps:

1. From your Shopify admin, go to **Apps** > [**Search & Discovery**](https://admin.shopify.com/apps/search-and-discovery).
2. Click **Filters**, and then click the filter that you want to rename.
3. In the **Filter label** field, enter your new label.
4. Click **Save**.

## Filter values

Only filter values that apply to products of a collection or search result display on your store.

There are different [sorting rules](search-and-discovery-filters.md#sorting-filter-values) applied to filter values, and you can [use metafield filters](search-and-discovery-filters.md#add-metafield-filters) for more control over sorting and displayed values.

### Group filter values

You can group multiple filter values together to display as a single filter value to customers. For example, you have a product with a `Color` option that includes `Onyx`, `Ebony`, and `Midnight`. You can group these values together under a single filter named `Black`. A filter group can have a maximum of 200 unique filter values, and a store can have a maximum of 1,000 filter groups.

#### Steps:

1. From your Shopify admin, go to **Apps** > [**Search & Discovery**](https://admin.shopify.com/apps/search-and-discovery).
2. Click **Filters**, and then click **Add filter** or click the name of an existing filter.
3. If the filter is based on a [standard product attribute](search-and-discovery-filters.md#standard-product-attributes), then click **Manage values** and choose an option. Learn more about [grouping standard product attribute filters](search-and-discovery-filters.md#grouping-standard-product-attribute-filters).
4. In the **Values** section, select the values that you want to group as a single filter value. You can use the search bar to find more filter values.
5. Click **Create group**.
6. Enter a name for the group. This is the single filter value displayed to customers.
7. Click **Done**.
8. Click **Save**.

#### Grouping standard product attribute filters

Filters based on [standard product attributes](search-and-discovery-filters.md#standard-product-attributes) offer a unique grouping feature. You can access the feature by clicking **Manage values**, where you have the option to choose either **Automatic** or **Manual** grouping:

* **Automatic**: Values are automatically grouped around their taxonomy base value. For instance, if your Color filter includes `Light red`, `Burgundy`, and `Ruby`, then they'll all be grouped under their base value `Red`. You can customize the group label and swatch, but you can't add or remove values.
* **Manual**: Values are initially ungrouped and can be grouped [based on the steps above](search-and-discovery-filters.md#grouping-steps).

#### Limitations

The **Category** filter does not support grouping.

### Sorting filter values

You can sort filter values in a way that best suits your store's needs. We offer two sorting orders:

* [Automatic Sort](search-and-discovery-filters.md#automatic-sort)
* [Manual Sort](search-and-discovery-filters.md#manual-sort)

#### Automatic Sort

Filter values are displayed in ascending order by default, both alphabetically and numerically. For example, a product option filter of `Shoe sizes` will display the values from smallest to largest.

Filter values that start with a number and end with a word, such as `60 watts`, will be displayed next to filter values that end with the same word. For example, a product option filter of `Age` with the filter values `2 years`, `6 months`, `3 years`, and `2 months` will be sorted in the following order:

* 2 months
* 6 months
* 2 years
* 3 years

Custom sort orders are applied for filters named `Size`, so that common sizing terms are displayed in the correct order. For example, `XS` (extra small) comes before `S` (small).

New filter values will be sorted automatically.

#### Manual sort

Manual sorting allows you to choose the display order of filter values. After saving a manual sort order, any new filter values are displayed at the end of the list until you update the sort order.

#### Steps:

1. From your Shopify admin, go to **Apps** > [**Search & Discovery**](https://admin.shopify.com/apps/search-and-discovery).
2. Click **Filters**, and then choose an existing filter or [create a new filter](search-and-discovery-filters.md#edit-filters).
3. Under **Sort**, select *Manually*.
4. Drag values to rearrange. Alternatively, you can select multiple values and click **Move to top** or **Move to bottom** to reposition them together.
5. Optional: Click **Reorder for me** to [sort with Shopify Magic](search-and-discovery-filters.md#sort-with-shopify-magic)
6. Click **Save**.

### Sort with Shopify Magic

You can use [Shopify Magic](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/shopify-magic) to sort values in a logical order based on the filter name and its values. Filters using [swatch filters](search-and-discovery-filters.md#visual-filters) consider the hex codes and their position on the color wheel to decide the sort order.

The **Reorder for me** button will sort your values with Shopify Magic. If the new order doesn't meet your expectations, then you can click the **Undo reorder** button to restore your manually sorted order, or re-arrange the values to better suit your store's requirements.

### Customize empty filter values

To help customers find available products, you can handle empty filter values by either moving them to the bottom of the list, or hiding them entirely. This allows customers to focus on values with matching results. For example, you sell T-shirts in different colors and sizes. All colors except `Red` are out of stock. If you move empty values to the bottom, then `Red` will display first in the `Color` filter. If you hide empty values, then only the `Red` option will be displayed in the `Color` filter.

#### Steps:

1. From your Shopify admin, go to **Apps** > [**Search & Discovery**](https://admin.shopify.com/apps/search-and-discovery).
2. Click **Settings**.
3. In the **Filters** > **Empty values** section, select one of the following options:

   * To hide empty filter values, select **Hide**. A filter is hidden entirely if all filter values are empty.
   * To move empty filter values to the bottom of the value list, select **Show at the end**.
   * To keep empty filter values sorted by the default sorting logic, select **Show in default order**.
4. Click **Save**.

### Excluding filter values

If you need more control over the values that are displayed to customers, then you can use a metafield filter with only the values that you want to be displayed on your store.

For example, you might want to use product tags for purposes other than storefront filters, such as [smart collection](https://help.shopify.com/en/manual/products/collections/smart-collections) conditions or [admin product list filtering](https://help.shopify.com/en/manual/products/searching-filtering#filter-your-product-list). A [metafield type](https://help.shopify.com/en/manual/custom-data/metafields/metafield-definitions/metafield-types) of single line text or [list type](https://help.shopify.com/en/manual/custom-data/metafields/metafield-definitions/metafield-lists) can be used instead of the product tag filter type.

## Visual filters

Filter values can include visual elements such as colors, patterns, or more detailed imagery. For example, a `Fabric color` filter can display a small color swatch for each filter value.

To create visuals with your filter values, use any of the following filter types based on a metaobject reference:

* [category metafield filters](search-and-discovery-filters.md#category-metafield-filters)
* [product metafield filters](search-and-discovery-filters.md#product-metafield-filters)
* [variant metafield filters](search-and-discovery-filters.md#variant-metafield-filters)

### Adding a standard product attribute filter

#### Steps:

1. From your Shopify admin, go to **Apps** > [**Search & Discovery**](https://admin.shopify.com/apps/search-and-discovery).
2. Click **Filters**.
3. Click **Add filter** or click an existing filter.
4. Click the **Source** field, and then select a filter of type Category Metafield or Product Metafield that is based on a [standard product attribute](search-and-discovery-filters.md#standard-product-attributes).
5. Click **Manage values**.
6. Choose either [**Automatic** or **Manual** for grouping](search-and-discovery-filters.md#grouping-filter-values).
7. Select **Include swatch**. You can leave this option unselected for text only.
8. To use images as swatches, select **Use images when available**.
9. Click **Save**.

### Adding a custom metafield filter

You can add a [custom metafield filter](search-and-discovery-filters.md#add-metafield-filters) based on a metaobject reference. Before you add a custom metafield filter, review the following requirements and best practices:

### Requirements for visual filters based on custom metafields

To create visuals for [custom metafield filters](search-and-discovery-filters.md#add-metafield-filters), they must meet the following requirements:

* A metaobject that meets the following criteria:
 + At least one **color** field or one **file** field with images. Both fields can only support **one value**, lists of values aren't supported.
 + A field to name the filter value. It must only allow **one value**, a list of values cannot be used as a filter name. The field can be any of the following types:
    - single line text
    - decimal
    - integer
    - boolean (true or false)
* A metafield definition that meets the following criteria:
 + The definition is made for either a **Product** or **Variant**.
 + The metafield type is **Metaobject** and references the metaobject definition created in the previous step.
 + Set whether the metafields allow either **one entry** or a **list of entries** of the metaobject.
* Both the metaobject and metafield definitions need to have [storefront access](https://help.shopify.com/en/manual/custom-data/options) activated.

### Best practices for visual filters based on custom metafields

Product variant filters will link to more relevant variants on search results and collection pages. For example, showing only red products when a red color swatch is clicked. Use variant metafields for the metaobject reference to use variant-level filtering. If linking to specific variants isn't important for your filter, then use product metafields instead.

A metaobject definition for a color swatch should have both a color and an image field. You don't need to provide a value for both, but this will give you the option of using either field in the future.

If your products or variants have multiple colors you could filter on, then set your metafield definition to allow a **list of entries**. This lets you assign multiple metaobject entries to a single item and each one will display as a filter value on your store.

#### Steps:

1. From your Shopify admin, go to **Apps** > [**Search & Discovery**](https://admin.shopify.com/apps/search-and-discovery).
2. Click **Filters**.
3. Click **Add filter** or click an existing filter.
4. Click the **Source** field, and then select a filter of type Category, Product or Variant metafield.
5. Set the **Label** field for filter values by selecting a metafield.
6. Check **Include visual** and select a visual style:

   * Choose **Swatch** for small color swatches or patterns. Set the swatch content by selecting:
     + A color field for the **Swatch color**.
     + An image field for the **Swatch pattern**.
   * Choose **Image** for icons, logos, or other graphics that shouldn't be cropped. Set the content by selecting an image field for the **Image**.

## Filter behavior

Only filters that can apply to the products on a collection page or search result are displayed.

Choosing filter values from different filters is an **and** condition that can decrease the number of products displayed. For example, choosing `Red` from a `Color` filter and `8` from a `Size` filter returns products that are both red and size 8.

By default, choosing filter values from the same filter is an **or** condition that can increase the number of results. For example, choosing `Red` and `Green` values from a `Color` filter returns all the products that are red or green. Certain filter types can use an **and** condition for their filter values instead. Learn how to [customize filter behavior](search-and-discovery-filters.md#customizing-filter-behavior) with the Shopify Search & Discovery app.

The number of products displayed also depends on whether the filters are product-level or variant-level filters. For example, a customer might choose multiple Color values from a product option filter, but only one product is displayed. This is because product options are variant-level filters and all the colors belonged to that single product's variants.

### Customizing filter behavior

For product tag, metafield list and metaobject reference list filters, you can choose the filter condition between values to be either the default **or** condition or the **and** condition. For example, with **and** filtering, choosing `New` and `Sale` from a product tag filter only returns products that have both those tags.

#### Steps:

1. From your Shopify admin, go to **Apps** > [**Search & Discovery**](https://admin.shopify.com/apps/search-and-discovery).
2. Click **Filters**, and then click **Add filter**.
3. Click the **Source** field, and then select a filter source that you want to make available to your customers.
4. Choose the behavior to apply to the filter values inside the **Logic** section.
5. Click **Save**.

## Filter translations

Filter labels, values, and groups can be translated into your store's other [supported languages](https://help.shopify.com/en/manual/international/localization-and-translation#managing-languages). You can translate content with translation apps such as the [Shopify Translate & Adapt](https://help.shopify.com/en/manual/international/localization-and-translation#requirements).

When there isn't translated content for filters, the store's default language is used.

Filter values are based on the translated content for your products and product variants.

It's possible to have a different number of values for a filter between languages. For example, your store's default language is English, and you also add French as a supported language. Your `Color` filter values include the value `Brown`. English has one common word for brown, and French has two common words. Your translation app automatically translates the `Brown` filter value into either `Brun` or `Marron` across the store's products. Your storefront filters will display one value for brown in the `Color` filter in English, and two values for brown in French.

To keep only one translation for each filter value, you need to edit the product's translated content with a translation app.

### Market languages

Filter value translations don't support additional instances of a language [setup for specific markets](https://help.shopify.com/en/manual/international/localization-and-translation#manage-markets-languages). For example, an online store can have product translations for French and two additional French translations for the Canada and France markets. In this case, all the filter values are based on the general French language, even when customers are shopping in French for those specific markets.

Filter labels and filter groups support language translations for specific markets.

## Troubleshooting filters

Review the following solutions to common filter issues:

### Price filter missing in multi-currency stores

If you have [international pricing](https://help.shopify.com/en/manual/international/pricing) or multiple currencies activated, then the price filter doesn't display when customers select any currency other than your store's default currency. This is a current limitation of the price filter functionality.

### Troubleshooting filter display issues

If a filter exists but doesn't show all expected products or filter options, the issue might be related to your store's search indexing. This can happen when:

* You've recently added new metafield values to products
* Products were recently updated with new filter-related information
* Your store's search data is out of sync

To resolve indexing issues, try these steps:

1. Wait 24-48 hours for automatic re-indexing to complete
2. Make a small update to affected products (such as adding a space to the product title) and save to trigger re-indexing
3. Contact Shopify Support if the issue persists

### Product option filters showing unexpected values

Product option filters display values based on your product variant option titles. If a filter shows unexpected values or missing options:

* Verify that your product option names match exactly across products (for example, use "Color" consistently instead of mixing "Color" and "Color:")
* Ensure that products using the filter have the product option configured

### Filters not displaying

Filters might not display in certain situations due to product limits:

* **Collections**: Filters are hidden if a collection contains more than 5,000 products
* **Search results**: Filters are hidden if search results return more than 100,000 products

If your collection or search results exceed these limits, then filters won't be available to customers on that page.

### Filter values missing or incomplete

Filters have limits on the number of unique values that can be displayed:

* **Tags**: Up to 5,000 unique tag values
* **Product options and attributes**: Up to 1,000 unique values
* **Metafields**: Some values might be missing depending on how the metafield is structured

If you're missing filter values, then verify that you haven't exceeded these limits.

### Filter translation issues

If filters or filter values aren't appearing correctly in different languages:

* Verify that the content is translated in your translation app
* Remember that product tag and vendor filters only display in your store's default language
* Use metafield filters for better translation support across multiple languages
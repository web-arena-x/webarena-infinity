# Using the Product Catalog to define products and services in Sell

Source: https://support.zendesk.com/hc/en-us/articles/4408832174746-Using-the-Product-Catalog-to-define-products-and-services-in-Sell

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

![Available on Sell Growth plans and above](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/plan_available_sell_pee.png)

You can use the Product Catalog to define the products (goods) used with your deals, which adds another layer of management to your pipeline.

While the Product Catalog uses the term "product" to refer to these goods, the term also refers to any services your company offers.

To add and edit products in the catalog, and to add or hide the Products widget on a deal pipeline, you must have admin rights. All other users have view-only access to the catalog and cannot see the unit cost data.

This article contain the following topics:

- [Setting up and adding products to your catalog](#topic_fg3_c42_jtb)
- [Working with multiple currencies](#topic_ozp_c42_jtb)
- [Adding products to a deal](#topic_ssy_c42_jtb)
- [Hiding the Products widget](#topic_ac2_xcf_twb)

## Setting up and adding products to your catalog

You need to set up your catalog before you can add your products. To add new products and edit existing ones, you must have admin permissions. Contact your admin if you need assistance.

**To set up your product catalog**

1. On the Sell sidebar, click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)).
2. Under **Customize**, click [Products](https://app.futuresimple.com/settings/products).

Before you can add products to deals, you must activate the product widget for deals

**To activate the Product widget for deals**

1. Under **Customize**, click **Layouts**.
2. Click the **Deals** tab.
3. Under **Deal widgets**, click **Products**.

   Note: You must manually add the Products widget to each deal pipeline that you want products to be available in.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_products_widget_deals.png)

You can see your product catalog, and the Product widget and can now add products to your catalog.

**To add a product to your catalog**

1. Click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/settings_icon.png)).
2. Under **Customize**, click [Products](https://app.futuresimple.com/settings/products).
3. In the top, right corner, click **Create Product**.
4. In the **Create product** panel to the right, enter the relevant information for your product in the following fields:
   - **Name:** (required field) the name of the product
   - **SKU:** an inventory number or code. You can search your catalog for the product using the name or the SKU.
   - **Active:** you can add an active product to a deal. If a product is inactive, it is still listed in the catalog, but you cannot use it on new deals (until it's reactivated). New products are set as active by default.
   - **Description:** a brief note describing the product.
   - **Unit Price:** the price of a single item. This is the basis for calculating the discount, markup, and selling price values.

     Note: You can choose one or more currencies for the unit price. Click **Add** (**+**) next to the unit price to add multiple currencies for the product (see [Working with currencies](https://support.zendesk.com/hc/en-us/articles/4408832174746-Using-the-Product-Catalog-to-define-products-and-services-in-Sell-Enterprise-and-Elite-#h_8fdb7c1e-ec8c-48b0-a4d5-dce11be412f4)).
   - **Max Discount:** the maximum discount you want to allow your team to offer on a product (up to 100%).
   - **Max Markup:** the maximum markup you want to allow your team to add to the product's unit price. This lets you increase the value of a product in a given deal. There is no upper limit to the maximum markup.
   - **Pricing Variation:** shows the range of prices available for a single item of the product. This is based on the unit price, maximum discount, and maximum markup settings.

     Note: For products that have a unit price of zero, the Pricing Variation does not display.
   - **Unit cost:** (Admin-only field) lets you record the price of manufacturing or purchasing a single item of the product. If you have specified multiple currencies, all currencies display. This field is not included in any of the above calculations.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_products_create.png)
5. Click **Save**. Your product is now listed in your product catalog. You can add multiple products at a time. If you want to leave without saving, click **Cancel**.

   To view all previously added products, click **View Catalog.**

## Working with multiple currencies

You can select any base currency for your product.

**To add a separate price for a given product in multiple currencies**

1. In the Sell **Product Catalog**, go to the item you want to add a currency to.
2. In the **Unit price** field, click the **Add** (**+**) icon to choose and add one of the currencies available in Sell to the item.

Products with prices available in more than one currency have **+ \*more** next to the unit price. The number (for example, +4 more) represents the number of currencies that are available. For more information about currencies in Sell, see [Working with currencies in Sell](https://support.zendesk.com/hc/en-us/articles/4408845920794)

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_products_unit_price_currency.png)

## Adding products to a deal

In the Products column, you can see the products associated with each deal, the total the total value of the products (converted to the deal's currency), and any discounts you've applied.

**To add products to an existing deal**

1. Click the deal you want to add products to.
2. In the **Products** widget, in the right column, click **Add product** (**+**).

   Note: When creating a new deal, you can add products to that deal by clicking **Add products** in the **Deal info** dialog.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_products_add_product.png)
3. In the **Product catalog**, select the checkbox next to the products you want to add to the deal.
4. When you've selected all of the products you want to add to the deal, click **Next** to go to the summary.
5. In the **Add products** summary dialog, review the products you've selected. At this point you can also add a discount, change the price or currency for the product, and the quantity.
6. To add additional products, click **Add products** below the list, and type the name of the product you want to add.
7. The **Set products value as deal value** checkbox is selected by default and sets the deal value based on the total value of the products listed. To add the value to your deal manually, deselect this checkbox.
8. To add a global discount to all of the products listed (instead of manually setting a discount for individual products), select the **Add total discount %** checkbox.
9. Click **Save**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_products_summary_deals.png)
10. The products that you added to the deal are now visible in the Products widget. You can also see the total value of the products associated with the deal in the deal's currency, and the global discount (if you applied one). If you applied discounts to individual products manually, then you must go to the deal summary and click **Edit deal** to see it reflected in the widget.

    ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_products_widget.png)

Product prices in currencies other than the deal's currency are converted to the equivalent amount in the deal's currency and shown as the (Total) Products Value. The (Total) Products Value is updated daily, based on current exchange rates (see [Working with currencies](https://support.zendesk.com/hc/en-us/articles/4408832174746-Using-the-Product-Catalog-to-define-products-and-services-in-Sell-Enterprise-and-Elite-#h_8fdb7c1e-ec8c-48b0-a4d5-dce11be412f4)). For example, if your deal's currency is euros, and you set the price for a product in dollars, the product's price in dollars remains the same, but the (Total) Products Value, in euros, changes.

Only the top five products of the deal display in the widget. If there are more products than the five listed, click the **More** (**...**) icon.

You can add products to a deal when quick-adding a deal from the Sales Pipeline. You can also filter your Deals by products in the [Sales Pipeline view.](https://support.zendesk.com/hc/en-us/articles/4408828764826)

## Hiding the Products widget

If sales reps don't need to see product details in a deal pipeline, admins can hide the Product widget from them. However, if you hide the Products Catalog, sales reps can't select products for their deals. Hiding the Products widget does not remove your product catalog; the contents of your catalog are retained for your account, in case you want to make it visible again in the future.

**To hide the Products widget**

1. On the Sell sidebar, click the **Settings** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/sell_icon_settings.png)).
2. Under **Customize** > **Layouts**, click the **Deals** tab.
3. In the **Deal widgets** column on the right, click **Edit**.

The Products widget is no longer visible on the deal pipeline. To add products to the deal, you must access the Product catalog via Settings.
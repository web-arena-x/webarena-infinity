# Change your catalog page

Source: https://help.shopify.com/en/manual/online-store/themes/customizing-themes/common-customizations/change-catalog-page

---

# Change your catalog page

All Shopify stores have a page with the URL `your-store.com/collections/all` that lists all of the visible products in the store. This is the store's catalog page. By default, products on the catalog page are displayed in alphabetical order. You can create a collection to control the order in which your products are displayed on this page.

## On this page

* [Create a collection to control your catalog page](change-catalog-page.md#create-a-collection-to-control-your-catalog-page)

## Create a collection to control your catalog page

You can create a collection with the title `All` to control the order in which products are displayed on your catalog page.

#### Steps:

1. From your Shopify admin, go to **Products** > [**Collections**](https://admin.shopify.com/collections).
2. Click **Create collection**.
3. Enter `All` as the title for the collection.
4. In the **Collection type** section, select **Smart**.
5. Select **Product price** from the first dropdown list.
6. Select **is greater than** from the second dropdown list.
7. Enter `$0`.
8. Optional: To hide products that are out of stock, add the condition **Inventory stock is greater than 0**.
9. Click **Save**.

Now that you have created your `All` collection, you can sort the products within it. Scroll to the **Products** section and select an option from the **Sort** drop-down menu. If you select **Manually**, then you can rearrange your products by using their drag and drop handles `⋮⋮`.

If you want to change the title of your `All` collection, then you can edit it now that the collection has been created. It is important, however, that the handle of the collection remains set as `all`. You can confirm this by scrolling to the **Search engine listing preview** section, and clicking **Edit website SEO**. The **URL and handle** text box should display a URL that ends in `/all`. If the URL ends in something different, then change it to `/all`, and click **Save**.

The changes that you make to the order of your products in this collection will be reflected on the catalog page of your online store.
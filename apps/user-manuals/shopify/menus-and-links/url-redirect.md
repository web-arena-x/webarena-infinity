# Creating and managing URL redirects

Source: https://help.shopify.com/en/manual/online-store/menus-and-links/url-redirect

---

# Creating and managing URL redirects

URL redirects can be used to redirect traffic from one web page to another. When you change a URL on your Shopify store, you can create a URL redirect to ensure your customers can still find what they're looking for.

For example, if you delete a product, then you can set up a URL redirect so that when customers enter the URL for that product, they're redirected to a similar product on your store.

## On this page

* [Considerations for creating URL redirects](url-redirect.md#considerations-for-creating-url-redirects)
* [Create a URL redirect](url-redirect.md#create-url-redirect)
* [URL redirects and online store visibility](url-redirect.md#url-redirects-and-online-store-visibility)
* [Redirects and subfolders](url-redirect.md#redirects-and-subfolders)
* [Managing your URL redirects](url-redirect.md#manage-url-redirect)

## Considerations for creating URL redirects

Before you create any URL redirects, review the following considerations:

* You can't redirect URLs that begin with the following prefixes: `/apps`, `/application`, `/cart`, `/carts`, `/orders`, `/services`, or `/shop`.
* You can't redirect URLs that use fixed Shopify paths: `/products`, `/collections`, `/collections/all`.
* You can redirect only from broken URLs. Broken URLs display error messages, such as **Page not found** or **404**, on a page or in the page title. If the URL still loads a valid webpage, then the URL redirect won't work.
* You can create a maximum of 100,000 URL redirects unless your store is on the Plus plan, which has a maximum of 20,000,000 URL redirects.
* URL redirects aren't supported on [customer account menus](understanding-navigation.md#customer).

### Common redirect scenarios

Understanding these scenarios can help you set up redirects more effectively.

### Additional URL redirect limitations

Review these additional limitations that can affect URL redirect functionality:

**Reserved URL paths**

Certain URL paths are reserved by Shopify and cannot be used for redirects:

* `/collections/vendors`, `/collections/types`, `/collections/all`
* `/apps/`, `/a/`, `/community/`, `/tools/`
* MyShopify domain paths ending in `/shop` or `/services`

**Collection tag filtering**

You cannot create redirects for URLs that use collection tag filtering (such as `yourstore.com/collections/collection-name/tag-name`). Even if no products exist with that tag, the URL path is still considered valid and cannot be redirected.

**HTML file extensions**

URLs ending in `.html` cannot be redirected to the same URL without `.html`. Shopify treats these as the same URL because the platform automatically handles HTML formatting for cleaner URLs.

**Query strings and special characters**

URLs containing query strings (such as `/brands/dell.html?_bc_fsnf=1&interface=interface_type`) might not work as expected with URL redirects.

**International markets and subfolders**

URL redirects don't automatically apply to all market subfolders. If you need to redirect specific locales (such as `yourstore.com/en-ca/old-page` to `yourstore.com/en-fr/new-page`), then you must create individual redirects for each subfolder.

**301 redirect caching**

301 redirects are cached by browsers and search engines. If you remove a redirect after customers have accessed it, then the redirect might continue to work in their browsers until the cache expires.

## Create a URL redirect

You can create a URL redirect. When creating a redirect, the new URL can be a relative URL, such as `/collection/shirts`, or a full URL, such as `http://www.example.com/collection/shirts`. To redirect traffic within your [primary domain](https://help.shopify.com/en/manual/domains/domains-terminology), use a relative URL. To redirect outside your [primary domain](https://help.shopify.com/en/manual/domains/domains-terminology), use a full URL. URL redirects start working immediately.

You can also add Liquid to your **Redirect from** and **Redirect to** fields. Full field validation can't be performed when using Liquid in your paths.

#### Steps:

1. From your Shopify admin, go to **Content** > [**Menus**](https://admin.shopify.com/content/menus).
2. Click **View URL Redirects**.
3. Click **Create URL redirect**.
4. In **Redirect from**, enter the old URL that you want to redirect visitors from.
5. In **Redirect to**, enter the new URL that you want to redirect visitors to. To redirect to your store's home page, enter `/`.
6. Click **Save redirect**.

### Troubleshooting URL redirects

URL redirects start working immediately. If your redirect isn't working immediately, then you can try the following troubleshooting steps:

* Review both **Redirect from** and **Redirect to** URLs for any typos.
* Ensure the **Redirect from** URL doesn't have an active page.
* Ensure that the **Redirect from** URL isn't a [fixed path or contains a prefix that you can't redirect](url-redirect.md#considerations-for-creating-url-redirects).
* Clear your browser's cache and test the redirect again or try on another device.

### Additional redirect troubleshooting

**404 page redirects to home page in theme editor**

If your 404 page redirects to the home page when viewing it in the theme editor, check whether you have a redirect set up from `/404` to `/` (your home page). This type of redirect interferes with the theme editor's ability to display your 404 page. Remove this redirect to resolve the issue.

**Redirect Limit Exceeded API errors**

If you encounter "Redirect Limit Exceeded" errors when using the Admin API, then this error isn't related to your store's URL redirect limit (100,000 redirects). Instead, it indicates that an API request is causing too many server redirects. If you're experiencing this error, then consider reaching out to the [Shopify Community](https://community.shopify.dev) or contact the developer of any third-party apps that might be causing the issue.

## URL redirects and online store visibility

You can use URL redirects with your online store's visibility settings to temporarily redirect customers from hidden content to active content.

For example, if you have a `/collections/fall` collection that you want to temporarily hide during summer and redirect customers to `/collections/summer`, you can:

1. Change the fall collection's **Online store visibility** to **Hidden**.
2. Create a URL redirect from `/collections/fall` to `/collections/summer`.

When the fall collection is hidden, the `/collections/fall` URL becomes a 404 page, which allows the redirect to work. Customers who visit `/collections/fall` are automatically redirected to `/collections/summer`.

**Important**: If you later change the collection's **Online store visibility** back to **Visible**, the URL redirect is automatically deleted because redirects only work for URLs that return 404 errors. You would need to recreate the redirect if you hide the collection again.

This behavior also applies to products. You can set products to **Draft** status or remove them from all sales channels to make them return 404 errors and become eligible for URL redirects.

## Redirects and subfolders

Creating a URL redirect applies to all language or market subfolders set up using international sales tools.

For example, your primary market is the United States on `example.com`. You also have a market for Canada on a subfolder at `example.com/en-ca`. You decide to stop selling a blue t-shirt on your store, so you delete the product, and then create a single URL redirect from `/products/blue-t-shirt` to `/collections/t-shirts`.

After creating the URL redirect, customers in the United States who try to visit `/products/blue-t-shirt` are automatically redirected to `example.com/collections/t-shirts`, and customers in Canada who try to visit `example.com/en-ca/products/blue-t-shirt` are automatically redirected to `example.com/en-ca/collections/t-shirts`.

You can still create individual redirects for each subfolder if you want to redirect people to a different destination for each market.

## Managing your URL redirects

You can manage your URL redirect list in the following ways:

* [Filter URL redirects by date](url-redirect.md#filter-url-redirects-by-date)
* [Save a URL redirect filter](url-redirect.md#save-url-redirect-filter)
* [Delete a URL redirect filter](url-redirect.md#delete-url-redirect-filter)
* [Edit the name of a URL redirect filter](url-redirect.md#edit-url-redirect-filter-name)
* [Edit URL redirects individually](url-redirect.md#edit-url-redirects-individually)
* [Edit multiple URL redirects at the same time](url-redirect.md#edit-multiple-url-redirects)
* [Export your URL redirects](url-redirect.md#export-your-url-redirects)
* [Import your URL redirects](url-redirect.md#import-your-url-redirects)
* [Delete URL redirects](url-redirect.md#delete-url-redirects)

### Filter URL redirects by date

1. From your Shopify admin, go to **Content** > [**Menus**](https://admin.shopify.com/content/menus).
2. Click **URL redirects**.
3. Click **Date added**.
4. From the drop-down menu, choose the date period that you want to filter.

### Save a URL redirect filter

1. From your Shopify admin, go to **Content** > [**Menus**](https://admin.shopify.com/content/menus).
2. Click **URL redirects**.
3. Create a filter using the search box or by [filtering URL redirects by date](url-redirect.md#filter-url-redirects-by-date).
4. Click **Save filters**.
5. Select a name for your filter.
6. Click **Save filters**. Filters are saved as a new tab at the top of the list.

### Delete a URL redirect filter

1. From your Shopify admin, go to **Content** > [**Menus**](https://admin.shopify.com/content/menus).
2. Click **URL redirects**.
3. Select the filter that you want to delete.
4. Click **Saved**.
5. Click **Remove tab**, and then click **Remove**.

### Edit the name of a URL redirect filter

1. From your Shopify admin, go to **Content** > [**Menus**](https://admin.shopify.com/content/menus).
2. Click **URL redirects**.
3. Select the filter that you want to edit.
4. Click **Saved**.
5. Edit the tab name, and then click **Save filters**.

### Edit URL redirects individually

1. From your Shopify admin, go to **Content** > [**Menus**](https://admin.shopify.com/content/menus).
2. Click **URL redirects**.
3. Click the URL redirect that you want to edit.
4. Enter the changes.
5. Click **Save redirect**.

### Edit multiple URL redirects at the same time

You can edit URL redirects in bulk. To learn more about editing multiple URL redirects at the same time, refer to [using Bulk actions](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/bulk-actions).

#### Steps:

1. From your Shopify admin, go to **Content** > [**Menus**](https://admin.shopify.com/content/menus).
2. Click **URL redirects**.
3. Select the URL redirects that you want to edit.
4. Click **Edit redirect**.
5. Enter the changes.
6. Click **Save**.

### Export your URL redirects

1. From your Shopify admin, go to **Content** > [**Menus**](https://admin.shopify.com/content/menus).
2. Click **URL redirects**.
3. Click **Export**.
4. Choose which redirects you want to export.
5. Select which type of CSV file you want to export.
6. Click **Export URL redirects**.

### Import your URL redirects

You can import your existing URL redirect to Shopify. You can download and view a [sample URL redirect CSV file](/csv/sample-redirect-template.csv) to use as a template.

#### Steps:

1. From your Shopify admin, go to **Content** > [**Menus**](https://admin.shopify.com/content/menus).
2. Click **URL redirects**.
3. Click **Import**.
4. Click **Add File** and select a CSV file.
5. Click **Upload file**.
6. Review the import.
7. Click **Import redirects**.
8. Click **Close**.

### Delete URL redirects

You can delete URL redirects. To learn more about deleting multiple URL redirects at the same time, refer to [using Bulk actions](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/bulk-actions).

#### Steps:

1. From your Shopify admin, go to **Content** > [**Menus**](https://admin.shopify.com/content/menus).
2. Click **URL redirects**.
3. Select the URL redirects that you want to delete.
4. Click **Delete selected redirects**.
5. Click **Delete** to confirm your decision.
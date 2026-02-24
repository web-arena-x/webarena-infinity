# Adding a favicon to your store

Source: https://help.shopify.com/en/manual/online-store/images/add-favicon

---

# Adding a favicon to your store

A favicon, or favorites icon, is a small image or logo that displays next to a web page's name. You can find favicons on your browser tabs, as well as on browser pages that list websites, such as the bookmarks page. You can add a favicon to your online store to help strengthen your brand and to add a polished look to your website.

## On this page

* [Creating a favicon](add-favicon.md#creating-a-favicon)
* [Add a favicon to your online store](add-favicon.md#add-a-favicon-to-your-online-store)
* [Troubleshooting favicons](add-favicon.md#troubleshooting-favicons)

## Creating a favicon

You can use a free favicon generator website to create a custom favicon, or you can create your own. To find a favicon generator, search the internet for `free favicon generator`.

The ideal image size for a favicon is either 16x16 pixels or 32x32 pixels. If your favicon image size is too large, then it will be reduced to 32x32 pixels when you upload it to Shopify.

## Add a favicon to your online store

You can add a favicon to your online store if you're on the Basic plan or higher. You can't add a favicon to your online store if you're on the Starter plan.

#### Steps:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to add a favicon for, and then click **Edit theme**.
3. Click the gear icon to access **Theme settings**.
4. Depending on your theme version, click **Logo** or **Favicon**.
5. In the **Favicon image** section, click **Select image**, and then do one of the following:

   * To select an image that you've already uploaded to your Shopify admin, you can search for or find the image, and then select it with the checkbox.
   * To select an image from your local computer, click **Add images**, open the image from your local computer, and then select it with the checkbox.
6. Click **Done**.
7. Optional: Add alt text to your favicon image by taking the following actions:

   1. In the **Favicon image** section, click **Edit**.
   2. In the **Preview and edit** dialog, enter a brief description of the image in the **Alt text** field.
   3. Click **Save**.
8. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap
   .
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to add a favicon for, and then tap **Edit theme**.
5. Tap **...** > **Theme settings**.
6. Depending on your theme version, tap **Logo** or **Favicon**.
7. In the **Favicon image** section, tap **Select image**, and then do one of the following:
   * To select an image that you've already uploaded to your Shopify admin, you can search for or find the image, and then select it with the checkbox.
   * To select an image from your local device, tap **Add images**, open the image from your local device, and then select it with the checkbox.
8. Tap **Done**.
9. Add alt text to your favicon image by taking the following actions:
   1. In the **Favicon image** section, tap **Edit**.
   2. In the **Preview and edit** dialog, enter a brief description of the image in the **Alt text** field.
   3. Tap **Save**.
10. Tap **Save** or **✓**.

## Troubleshooting favicons

If you're having issues with your favicon, then review the following troubleshooting steps.

Troubleshoot favicon not displaying in Google search results

If your favicon isn't displaying in Google search results, then make sure that you've [submitted your sitemap](https://help.shopify.com/en/manual/promoting-marketing/seo/find-site-map) to Google so that your store information can be crawled.

According to [Google's documentation](https://support.google.com/webmasters/answer/9290858), a favicon isn't guaranteed to display in search results even if all [guidelines](https://support.google.com/webmasters/answer/9290858) are met.

Troubleshoot favicon not displaying on Customer Accounts or Checkout pages

Favicons don't display on Customer Accounts and Checkout pages unless you're on the Shopify Plus plan. Additionally, favicons don't display when viewing your theme through the Theme Editor, because the Theme Editor is part of the Shopify admin and doesn't reflect your live storefront.

If you're on the Shopify Plus plan and want to set a favicon on Customer Accounts and Checkout pages, then you need to use the Branding API or Checkout Blocks. The favicon doesn't appear automatically, and can't be set in the theme editor or checkout editor in the admin. To learn more about using the Branding API, refer to the following developer documentation:

* [Add a favicon to checkout](https://shopify.dev/docs/apps/build/checkout/styling/add-favicon)
* [checkoutBrandingUpsert mutation](https://shopify.dev/docs/api/admin-graphql/2024-10/mutations/checkoutbrandingupsert)
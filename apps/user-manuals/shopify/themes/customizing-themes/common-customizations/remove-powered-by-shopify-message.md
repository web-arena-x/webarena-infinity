# Remove 'Powered by Shopify' from your online store

Source: https://help.shopify.com/en/manual/online-store/themes/customizing-themes/common-customizations/remove-powered-by-shopify-message

---

# Remove 'Powered by Shopify' from your online store

You can remove the "Powered by Shopify" message when you don't want it displayed in your store. Removing the message can create a cleaner footer and a more customized brand experience.

## On this page

* [Edit the default theme content](remove-powered-by-shopify-message.md#edit-the-default-theme-content)
* [Edit the theme code](remove-powered-by-shopify-message.md#edit-the-theme-code)

## Edit the default theme content

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to edit, and then click **…** > **Edit default theme content**.
3. In the **Filter items** search box, enter `powered`. This will bring up both the **Powered by Shopify** and **Powered by Shopify HTML** boxes.
4. In the **Powered by Shopify** box, enter a single space. If your store is password-protected, then you can repeat this step for the **Powered by Shopify HTML** box, which appears on your store's **Opening soon** page.
5. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap the icon.
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to edit, and then tap **…** > **Edit default theme content**.
5. In the **Filter items** search box, enter `powered`. This will bring up both the **Powered by Shopify** and **Powered by Shopify HTML** boxes.
6. In the **Powered by Shopify** box, enter a single space. The faded placeholder text in the box disappears. If your store is password-protected, then you can repeat this step for the **Powered by Shopify HTML** box, which displays on your store's **Opening soon** page.
7. Tap **Save** or **✓**.

## Edit the theme code

If the "Powered by Shopify" message is still displayed in the footer after you update the default theme content, then you might need to modify the theme code.

#### Steps:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to edit, and then click **…** > **Edit code**.
3. In the **Sections** directory, click the `footer.liquid` file.
4. Use `ctrl` + `F` on a PC or `command` + `F` on a Mac to locate the following Liquid tag and delete it:

```
{{ powered_by_link }}
```

5. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap the icon.
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to edit, and then tap **…** or **⋮** > **Edit code**.
5. Locate the following Liquid tag and delete it:

```
{{ powered_by_link }}
```

6. Tap **Save** or **✓**.

If you use a [free theme from Shopify](https://themes.shopify.com/collections/free-themes), then you can contact Shopify Support for help with this tutorial. To learn more, refer to [Support for themes](../../theme-support.md).
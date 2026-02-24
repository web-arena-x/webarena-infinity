# Password page

Source: https://help.shopify.com/en/manual/online-store/themes/password-page

---

# Password page

You can restrict visitor access to your online store by adding a password. Your password page is the landing page where you allow customers to enter your store with the password that you provide.

When your password page is active, search engines find and display only the password page of your online store. Other pages, such as product pages, are hidden and aren't displayed in search results.

## On this page

* [Add your online store password](password-page.md#add-password-protection-to-your-online-store)
* [Remove your online store password](password-page.md#remove-password-protection-from-your-online-store)
* [Password page sections](password-page.md#password-page-sections)
* [Edit your password page settings](password-page.md#edit-your-password-page-settings)
* [Hide the footer on your password page](password-page.md#hide-the-footer-on-your-password-page)
* [Edit the theme code for your password page](password-page.md#edit-the-theme-code-for-your-password-page)

## Add your online store password

You can add password protection for your online store.

#### Steps:

1. From your Shopify admin, go to **Online Store** > [**Preferences**](https://admin.shopify.com/online_store/preferences).
2. In the **Store access** section, select **Password protection**.
3. In the **Password** field, enter the password that you want to add to your online store and restrict access with. Don't use the same password that you use to log in to your Shopify admin.
4. Optional: In the **Message to your visitors** field, enter the message that you want to display to visitors on the password page. If you don't want to display a message, then leave this field blank.
5. Click **Save**.

## Remove your online store password

If you remove password protection, then anyone can visit your online store.

You can remove password protection from your online store only after you [pick a pricing plan](https://help.shopify.com/en/manual/your-account/manage-billing/managing-your-bills/billing-plan-changes#change-plan). If you pick a plan during a free trial, then you won't be charged any subscription fees until your free trial expires.

#### Steps:

1. From your Shopify admin, go to **Online Store** > [**Preferences**](https://admin.shopify.com/online_store/preferences).
2. In the **Store access** section, deselect **Password protection**.
3. Click **Save**.

## Password page sections

The password page displays when a customer visits your website and password protection is active on your online store.

By default, the password page has its own **Password header** and **Password footer** sections in the theme editor, and the page also contains an **Email signup banner** section.

The **Password header** section displays a different header on the password page from the one that you set for the rest of your online store.

The **Email signup banner** section is intended to provide a way for customers to subscribe to your email marketing from the password page so that they can learn more about your business, such as when your online store will open.

## Edit your password page settings

You can edit the content that displays on your password page, such as the text, colors, and typography from the [theme editor](customizing-themes/theme-editor/features-overview.md). The specific customization settings for each theme depend on your theme's developer and theme version. Learn more about finding your [theme version](managing-themes/versions.md).

#### Steps:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to edit, and then click **Edit theme**.
3. Click the **Home page** drop-down menu, and then click **Password**.
4. To edit the sections on the password page, take the following steps:

   1. Click the section that you want to edit. Most themes have header, content or template, and footer sections.
   2. Make your changes to the section's settings and options.
   3. Optional: Add other [sections and blocks](theme-structure/sections-and-blocks.md) to your password page.
   4. Click **Save**.
5. You can edit your [theme settings](customizing-themes/theme-editor/theme-settings.md), such as typography, color, social media and favicon settings, to customize your password page. These settings also apply to the rest of your theme. To edit the theme settings, take the following steps:

   1. Click the **Theme settings** gear icon.
   2. Click the settings category that you want to edit.
   3. Make your changes to the theme settings.
   4. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap
   .
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to edit, and then tap **Edit theme**.
5. Tap the **Home page** drop-down menu, and then tap **Password**.
6. To edit the sections on the password page, tap **Sections**, and then take the following steps:
   1. Tap the section that you want to edit. Most themes have header, content or template, and footer sections.
   2. Make your changes to the section's settings and options.
   3. Optional: Add other [sections and blocks](theme-structure/sections-and-blocks.md) to your password page.
   4. Tap **Save**.
7. You can edit your [theme settings](customizing-themes/theme-editor/theme-settings.md), such as typography, color, social media and favicon settings, to customize your password page. These settings also apply to the rest of your theme. To edit the theme settings, take the following steps:
   1. Tap **…** or **⋮**, and then tap **Theme settings**.
   2. Tap the settings category that you want to edit.
   3. Make your changes to the theme settings.
   4. Tap **Save** or **✓**.

## Hide the footer on your password page

You can hide the footer section on your password page.

#### Steps:

1. From your Shopify admin, go to **Online Store** > [**Preferences**](https://admin.shopify.com/online_store/preferences).
2. In the **Store access** > **Password protection** section, find the **Message to your visitors** field, and then paste the following code either above or below any existing content in the field:

```
<style>footer { display: none; }</style>
```

3. Click **Save**.

## Edit the theme code for your password page

If you want to make customizations that aren't available in the theme settings, then you can [edit the theme code](customizing-themes/edit-code/edit-theme-code.md) for your password page.

#### Steps:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to edit, click the **…** button to open the actions menu, and then click **Edit code**.
3. In the **sections** directory, click the `.liquid` file that you want to edit. Search for file names containing `password-header` or `password-footer`.
4. Make your code changes in the file.
5. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap
   .
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to edit, tap the **…** button to open the actions menu, and then tap **Edit code**.
5. In the **sections** directory, tap the `.liquid` file that you want to edit. Search for file names containing `password-header` or `password-footer`.
6. Make your code changes in the file.
7. Tap **Save** or **✓**.

To learn more about the `password.liquid` template, refer to [*password.liquid*](https://shopify.dev/themes/architecture/templates/password).
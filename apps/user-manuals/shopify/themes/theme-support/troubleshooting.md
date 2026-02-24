# Troubleshooting your online store theme

Source: https://help.shopify.com/en/manual/online-store/themes/theme-support/troubleshooting

---

# Troubleshooting your online store theme

This guide helps you troubleshoot common issues with your online store theme, including display problems, missing elements, and functionality issues. Complete the general troubleshooting steps first before moving to specific issue troubleshooting. If you're still having issues after following this guide, then you can contact your theme's support team.

## On this page

* [Step 1: General troubleshooting](troubleshooting.md#step-1-general-troubleshooting)
* [Step 2: Select the theme issue](troubleshooting.md#step-2-select-the-theme-issue)
* [Step 3: Contact support](troubleshooting.md#step-3-contact-support)

## Step 1: General troubleshooting

Complete these steps to locate the source of the issue in your theme:

1. **Verify the issue isn't local to your device**: Local issues are usually a result of device or browser settings, or internet connection issues. Try the following steps:
   * Clear your browser cache and cookies. If you're logged in to the Shopify Help Center with your Shopify account, then clearing your browser cache and cookies logs you out of your account.
   * Try incognito mode, another device, or the [Shopify app](https://www.shopify.com/install/detect).
   * Try using mobile data or another internet connection.
   * Verify your browser is up to date.
   * Verify the browser isn't set to block all cookies, because some apps might not display correctly without cookies.
   * Verify you aren't using a Virtual Private Network (VPN) or have a firewall activated that blocks Shopify.
2. **Test the issue on another theme**: If you're still experiencing the issue on other devices, browsers, or internet connections, then the issue isn't a local issue and can be replicated. Visit the [Theme Store](https://themes.shopify.com) and install a new version of the theme and test whether the issue is still present on the latest version of the theme. Installing a different theme, such as a [free Shopify theme](https://themes.shopify.com/collections/free-themes), is also good practice, because you can determine whether the issue is due to that specific theme or if all themes are experiencing the same issue. After testing out other themes:
   * If the issue is only present on your current theme and an updated and uncustomized version of the theme, then you might need to [get support for your theme](../theme-support.md#where-to-find-support-for-your-theme).
   * If your issue is only present on the current theme, then there might be some theme code that is causing issues. If you recently updated your theme code, then you can [roll back to an older version of your theme code](../customizing-themes/edit-code/edit-theme-code.md#roll-back). If you haven't modified the code in the theme, then you might want to review your theme settings. For example, if the **Add to Cart** button isn't displaying, then review the colors for **Buttons** in your theme settings and verify they're different and contrasting colors.
   * If the issue is present on all themes, then it might be due to your Shopify admin settings, apps, or other issues.
3. **Test if the issue is from an app**: If you recently installed or updated any apps that affect your storefront, then you might want to uninstall the app temporarily. If the issue isn't present after uninstalling the app, then you can contact the app developer's support team for more help in getting it to display correctly on your storefront. Learn more about [getting help with your apps](https://help.shopify.com/en/manual/apps/getting-support). If the issue is still present after uninstalling the app, then the app isn't the source of the issue.

## Step 2: Select the theme issue

Troubleshoot image display issues

Images might display differently from what you're expecting, but that might be due to the image itself not being compatible with what you're using the image for in your theme. Verify the [image dimensions](https://help.shopify.com/en/manual/products/product-media/product-media-types#images) are correct in the image you're using. Review the following list of common display issues that might occur when uploading an incompatible image:

* If your header displays larger and your logo image displays smaller than you're expecting, then it might be due to whitespace in the logo image file. Whitespace in the logo image file can cause the logo to display smaller and your header might display larger due to the whitespace. Edit the image file to verify it's cropped around the logo and there is no whitespace.
* If your slideshow image is being cropped, then this is by design to verify that the images display the same on mobile as on desktop. Because content displays much smaller on a mobile screen, there is a lot of detail that can be lost by shrinking the content. Instead, the content is cropped to verify that the details aren't lost. A portrait image, which is taller than it is wide, can also take up significant space on desktop. This is why slideshow images have a maximum height. You can [add a focal point](../../images/theme-images.md#focal-points) to your slideshow images to verify the focal point is always the center of the slideshow image.

 **Adaptive height option:** Many Shopify themes include an adaptive height setting for slideshows that adjusts the slideshow height to match the first image slide, reducing cropping across different screen sizes. This feature is available in all currently supported themes developed by Shoify.
* If a GIF image isn't displaying correctly and it's been added to your storefront with the rich text editor, such as in the product description or in a blog post, then it might be due to the image size. You can correct this by clicking the GIF in the rich text editor, and then click **Edit image**. In the **Image size** dropdown menu, select **Original**. You can then resize the GIF by clicking and dragging the corners of the image inward to make it smaller or outward to make it larger.
* If your images have a significant color change on your storefront from your original image, then your images might not be in the standard Red Green Blue (sRBG) colors. To fix this color change, save your file in a photo editing application as a sRBG. Common terms for this are "Web optimize", "Adjust image for Web", or "Save for Web." Learn more about [color profiles](../../images/theme-images.md#image-color-profiles).
* If your product images on your collection pages aren't aligning, then you might need to adjust the aspect ratio in the product image files so that they're the same height to width ratio, and then upload the product image again. You can also use an [image editing app from the Shopify App Store](https://apps.shopify.com/search?q=image+edit).

Troubleshoot product or collection display issues

Review the following issues for your specific issue and steps to help you troubleshoot:

* **Products missing**: If your products are missing from your storefront, then you might need to review the **Status** and your **Sales Channels** in the **Publishing** section of your product in your Shopify admin. Verify that the product status is **Active** and that the product is available to the **Online Store**.
* **Collections missing**: If your collections are missing from your storefront, then you might need to review the **Sales channels** in the **Publishing** section of the collection in your Shopify admin. Verify that the collection is available to the **Online Store**, and that your collection is added to your menus.
* **Collections displayed but products missing**: If your collections are displaying but there are products missing, then you might need to review any tag filters for the collection in your [**Menus**](https://admin.shopify.com/content/menus) settings. Verify that there are no tags in the **Filter collection with tags** field that might cause products to not display.
* **Currency not correct**: If your currency isn't displaying correctly for products or in your collections, then you might want to review the **Currency display** in the **Store defaults** section in **Settings** > **General** to verify that there isn't any additional code. Learn more about [formatting how currency displays to your customers](https://help.shopify.com/en/manual/international/pricing/currency-formatting).
* **Some products display differently**: If some products or collections are displaying differently than the others, then review the **Theme template** assigned to the products or collections in your Shopify admin.
* **Cannot edit product or collection templates**: If the default product or collection templates appear greyed out and unclickable in the theme editor, then you need to make at least one product or collection available to the Online Store sales channel. You can't edit these default templates without having products or collections available to preview the changes. Learn more about [changing the availability of a collection](https://help.shopify.com/en/manual/products/collections/make-collections-available) and [setting product availability in your sales channels](https://help.shopify.com/en/manual/products/add-update-products#product-availability).

Troubleshoot translated content display issues

If your translated content doesn't display properly or is missing from your storefront, then there might be outdated translations or missing translations for the content. The content might also be in a specific template for a market. Whenever you add any new content in your default language, remember to run automatic translation again, or manually add new translations.

The following statuses can apply to translated content:

* **Translated**: The content has translations available.
* **Outdated**: The content in the default language has been updated, but the translations don't reflect any updates.
* **Untranslated**: There are no translations for this content type.

When reviewing your translated content, update any untranslated or outdated content and your translated content should then display correctly.

Learn more about [translating and localizing your store](https://help.shopify.com/en/manual/international/localization-and-translation).

Troubleshoot theme editor and storefront differences

If your storefront and your theme editor don't display the same information, then review the theme template you're editing. You might need to make edits to update your theme templates to display the correct information.

Market overrides allow you to create different storefronts for different markets and display translated content. You might have been inadvertently working within a specific market or B2B when making updates. Locate the content with the **Market** drop-down menu in your theme editor to make sure it's in the correct markets.

Learn more about [market overrides](../customizing-themes/store-contextualization/understanding-markets-and-overrides.md).

Troubleshoot mobile and desktop display differences

All themes available in the Shopify Theme store are responsive themes, meaning that the theme adapts to the size of the screen. In the theme editor, you can switch the screen size view during theme editing to verify that your pages and images display correctly. Learn more about [viewing different screen sizes in the theme editor](../customizing-themes/theme-editor/features-overview.md#screen-sizes).

Many of the sections and blocks have mobile settings that you can customize. For example, you can set the **Number of columns on mobile** in the [**Related products** section](../theme-structure/sections-and-blocks.md). You can review the section settings related for mobile for each template to troubleshoot any display issues on mobile screen sizes.

Some theme features might display differently on mobile than desktop in order to verify the theme is accessible on all screen sizes. For example, on a desktop screen size, your slideshow might have a text overlay, where the text displays on top of the image often with an image color opacity or text shadow. However, on mobile screen sizes, the text might display below the slideshow. This is an accessibility feature by design so that the text is readable on any screen size. If the text was an overlay instead, then it would display very small on mobile making it difficult to read.

If your featured collection section or collection pages display inconsistent sizes or aren't aligning when viewing your storefront on mobile, then it might be due to inconsistent aspect ratios. Image grids, such as product images that display within a collection or featured collection, are built to be responsive for the screen size. If you have inconsistent aspect ratios for your images within the image grid, then they might display differently depending on the screen size. Square product images that are 2048 px by 2048 px usually work best in product grids. Update your images to have a consistent aspect ratio for optimization across all screen sizes. Learn more about [image aspect ratio](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/media-editor#understanding-image-aspect-ratio).

Troubleshoot rich text editor issues

Sometimes HTML code that is added in your rich text editor conflicts with your theme code. If the issue is present on a single page, such as a product page, page, or blog post, then it might be because of extra HTML. This can sometimes be added from copying and pasting text from another site.

**Review the HTML code**

You can review the HTML code in the rich text editor.

#### Steps:

1. Navigate to the page in your admin.
2. Click **Display HTML** button to review the HTML code.
3. Locate any HTML code that might cause display issues and remove it.
4. Click **Save**.

**Clear the formatting**

You can highlight a portion of the text and clear the HTML formatting.

#### Steps:

1. Navigate to the page in your admin.
2. Highlight the text with the formatting issues.
3. Click the **🚫** button.
4. Click **Save**.

Learn more about the [rich text editor](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/rich-text-editor).

Troubleshoot redirect to unsupported URL

If your storefront includes code that redirects users to URLs that aren't connected to your shop, then verify that the redirect has been deactivated when you visit the theme editor.

For example, this type of redirect might be added to a storefront to direct customers to different Shopify stores depending on their location. This type of redirect code could exist in either your theme or an app that you installed.

To verify your redirect doesn't interfere with the editor experience, use a reference to the `window.Shopify.designMode` variable in JavaScript to deactivate the redirect when you visit the theme editor. This variable is set to `true` when the storefront is loaded in the editor, and `false` when it isn't.

Troubleshoot dynamic content in theme blocks

If you have collapsible blocks or other theme blocks displaying the same content on all product pages, then you need to set up dynamic sources with metafields. This commonly happens when merchants add product-specific information such as ingredients or care instructions to one product, but it displays on all products.

**Collapsible blocks display same text on all products**

When you add content directly to a collapsible block in your theme editor, that content appears on all product pages. To display product-specific content, you need to use dynamic sources with metafields:

1. In your Shopify admin, go to **Settings** > **Metafields** > **Products**.
2. Click **Add definition**.
3. Enter a **Name** for your metafield, then click **Select content type**.
4. Select **Text** and **Multi-line text**.
5. Click **Save**.
6. Go to a product page in your admin and scroll to the metafields section at the bottom of the page.
7. Add your product-specific content to the metafield you created.
8. In your theme editor, go to the product template and find your **Collapsible row** section.
9. In the **Row content** setting, click the button.
10. Select your metafield from the available options.
11. Save your changes.

Now each product will display its own content when the metafield is filled in, and no content will display if the metafield is empty for that product.

Learn more about [displaying metafields on your online store](https://help.shopify.com/en/manual/custom-data/metafields/displaying-metafields-on-your-online-store) and [using metafields and metaobjects with dynamic sources](../theme-structure/sections-and-blocks.md#metafields-and-dynamic-sources).

Troubleshoot code error messages

If there's a syntax error in your theme code, then an `HTML error found` or `Theme error` warning message displays in your [theme editor](https://admin.shopify.com/themes/current/editor). The error message displays the Liquid file that contains the error.

A `The theme you're looking for couldn't be found` warning message might display when there is any broken HTML. A page can fail to load in the theme editor for many reasons, such as the following reasons:

* network connection issues
* invalid Liquid code in your theme

You can locate the code changes in your theme code and correct the code, or revert the file to before the code change.

#### Steps:

1. Click the `.liquid` section file that's linked in the error message or review the files for recent changes. This takes you to the **Edit HTML/Cascading Style Sheets (CSS) page**, and the file opens in the code editor.
2. Browse through the code in the file and try to find invalid HTML or Liquid. The code editor displays potential syntax errors in red. Common problems include the following:
   * Extra closing HTML tags, for example, a closing `</div>` without an opening `<div>`
   * Extra unclosed HTML tags, for example, an opening `<div>` without a closing `</div>`
   * Malformed HTML tags, for example, `<div class="my-class"` without a `>`
   * Malformed Liquid code
   * Broken HTML in an included theme snippet file
3. After you've found the problem, correct the code in your theme file, or revert the code by selecting a past version in **Recent changes**.
4. Click **Save**.
5. Click **Edit theme** to return to the theme editor, and confirm that the error message is gone.
6. Navigate to your storefront to verify that it displays as expected.

#### "Exceeded maximum number of unique handles" error

If you display a Liquid error message such as "Exceeded maximum number of unique handles for all\_products" on your homepage, then this usually means you've added too many Featured Product sections to your homepage (typically more than 20 sections in most themes).

To resolve this:

1. In your Shopify admin, go to **Online Store** > **Themes**.
2. Find your current theme and click **Edit theme**.
3. Navigate to your homepage.
4. Remove some Featured Product sections to stay within the theme's limits.
5. Consider using Featured Collection sections instead, which can display multiple products more efficiently and improve your store's performance.

Troubleshoot payment icons not displaying in footer

Payment icons are typically included by default in most themes' footers to show customers which payment methods you accept. If payment icons aren't appearing in your theme's footer, then you can check the following:

1. In your theme editor, navigate to the **Footer** section and verify that the **Show payment icons** setting is activated.
2. In your Shopify admin, go to **Settings** > **Payments** and verify that there is at least one active payment method. Some payment methods might require completion of account setup before their icons display.
3. If you're using a third-party payment gateway, then the payment icons might not appear due to platform limitations.

If you've verified these settings and the payment icons still aren't displaying, then you might need to [get support for your theme](../theme-support.md).

## Step 3: Contact support

If you're still having issues with your theme after completing the troubleshooting steps in this guide, then you can [get support for your theme](../theme-support.md).
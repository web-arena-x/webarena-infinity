# Choosing a social media image

Source: https://help.shopify.com/en/manual/online-store/images/showing-social-media-thumbnail-images

---

# Choosing a social media image

When you share a link to your online store on social media, such as on Facebook or Pinterest, you can display a thumbnail image in your post.

## On this page

* [Showing featured images](showing-social-media-thumbnail-images.md#showing-featured-images)
* [Setting the social sharing image in your admin](showing-social-media-thumbnail-images.md#setting-the-social-sharing-image-in-your-admin)
* [Social sharing image priority](showing-social-media-thumbnail-images.md#social-sharing-image-priority)
* [Social sharing image field displays blank](showing-social-media-thumbnail-images.md#social-sharing-image-field-displays-blank)
* [Social sharing image doesn't display on social media](showing-social-media-thumbnail-images.md#social-sharing-image-doesn-t-display-on-social-media)
* [Previewing your images](showing-social-media-thumbnail-images.md#previewing-your-images)

## Showing featured images

For all of the [free themes from Shopify](https://themes.shopify.com/collections/free-themes), when you post a link from your online store to social media, the featured image for that page is shown. The following page types have featured images:

* Product pages
* Collection pages
* Blog posts

For pages that don't have featured images, such as your homepage or an About us page, the social sharing image of your online store is displayed.

## Setting the social sharing image in your admin

In the [Online Store preferences](https://admin.shopify.com/online_store/preferences) of your store, you can add a default image to be used when a featured image for the page can't be found.

### Steps:

1. From your Shopify admin, go to **Online Store** > [**Preferences**](https://admin.shopify.com/online_store/preferences).
2. In the **Social sharing image and SEO** section, add a new image or change an existing image:

* To add a new image, click **Add image**.
* To change an existing image, click **Change image**.

4. Select the image from your device that you want to display on social media.
5. Click **Save**.

If the image in search engine results is outdated after you update the image in your admin, then you need to [re-submit your sitemap](https://help.shopify.com/en/manual/promoting-marketing/seo/find-site-map).

### Logo fallback image

When a social sharing image isn't manually uploaded, then Shopify uses images added to your theme as a fallback. Shopify might use the value of one of the following theme settings:

* **Header** > **Logo** (preferred)
* **Theme settings** > **Checkout** > **Logo**

If the logo's size doesn't meet the recommended dimensions or is on a transparent background, then Shopify fills the area with a color from **Theme settings** > **Colors** > **Background**. If this setting isn't available, then Shopify uses the **Theme settings** > **Checkout** > **Main content area** > **Background colour**. The following image illustrates a background color being used as padding:

## Social sharing image priority

The social sharing image in **Online Store** > **Preferences** serves as a fallback when no other image can be found. Images are selected in the following priority order:

1. **Theme code images**: Images hard-coded directly in your theme files (highest priority).
2. **Theme settings images**: Images uploaded to theme settings for social media or checkout.
3. **Online Store Preferences image**: The default fallback image uploaded to **Settings** > **Online Store** > **Social sharing image**.

This hierarchy ensures that intentional design choices in your theme take precedence over automatic fallbacks.

## Social sharing image field displays blank

If the social sharing image field in **Settings** > **Online Store** > **Preferences** appears blank, then the social shares might be pulling the image from your theme settings instead. Review the following locations in your theme editor for images:

* **Theme settings** > **Checkout** > **Logo**
* **Theme settings** > **Social media** or **Social sharing**

If both locations are blank, then social shares can't pull a relevant image and leaves the field blank. You can manually upload an image to the **Social sharing image** field in your online store preferences.

## Social sharing image doesn't display on social media

Some themes only display images uploaded to theme settings on social media posts. If you uploaded an image to **Settings** > **Online Store** > **Preferences** but it doesn't display when you share links, then verify that you also have an image uploaded in your theme's social media settings.

## Previewing your images

Shopify's free themes use [Open Graph tags](https://ogp.me) to give social media platforms information about your website. Open Graph is used by Facebook, Twitter, LinkedIn, Pinterest, and other services. You can preview what your social image might look like on some platforms with tools like [Twitter's Card Validator](https://cards-dev.twitter.com/validator), [Facebook's Crawler](https://developers.facebook.com/tools/debug) and [LinkedIn's Post Inspector](https://www.linkedin.com/post-inspector).
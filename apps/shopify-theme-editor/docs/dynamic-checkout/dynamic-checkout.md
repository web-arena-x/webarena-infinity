# Showing accelerated checkout buttons on your online store

Source: https://help.shopify.com/en/manual/online-store/dynamic-checkout/dynamic-checkout

---

# Showing accelerated checkout buttons on your online store

Accelerated checkout buttons are an alternative to the **Add to cart** button for single products. With accelerated checkout buttons, customers can skip the cart and go directly to the checkout. Customers can choose to check out with Shopify, or with another familiar accelerated checkout method. This helps to speed up the payment process and lets customers check out using a method that they're comfortable with.

## On this page

* [Overview](dynamic-checkout.md#overview)
* [Compatibility](dynamic-checkout.md#compatibility)
* [Update your theme to use accelerated checkout buttons](dynamic-checkout.md#update-your-theme-to-use-accelerated-checkout-buttons)
* [Display accelerated checkout buttons on product pages](dynamic-checkout.md#show-dynamic-checkout-buttons-on-product-pages)
* [Display accelerated checkout buttons on a featured product section](dynamic-checkout.md#display-accelerated-checkout-buttons-on-a-featured-product-section)
* [Hide accelerated checkout buttons on product pages](dynamic-checkout.md#hide-accelerated-checkout-buttons-on-product-pages)
* [Hide accelerated checkout buttons on a featured product section](dynamic-checkout.md#hide-accelerated-checkout-buttons-on-a-featured-product-section)
* [Display accelerated checkout buttons for some products but not for others](dynamic-checkout.md#display-accelerated-checkout-buttons-for-some-products-but-not-for-others)

## Overview

The accelerated checkout button displays beside or below the **Add to cart** button, depending on your theme and the customer's device. There are two different kinds of accelerated checkout buttons:

* Unbranded buttons display **Buy it now** text. If a customer clicks an unbranded **Buy it now** button, then they skip the cart and go to the checkout.

* Branded buttons include the logo for third-party accelerated checkout methods. If a customer clicks on a branded button for a third-party accelerated checkout method, such as Apple Pay, then they go to the checkout for that method with their information pre-populated. Learn more about [accelerated checkouts](https://help.shopify.com/en/manual/payments/accelerated-checkouts). The following third-party accelerated checkout methods are available:
  + [Amazon Pay](https://help.shopify.com/en/manual/payments/accelerated-checkouts/amazonpay/amazon-pay)
  + [Apple Pay](https://help.shopify.com/en/manual/payments/accelerated-checkouts/apple-pay)
  + [Google Pay](https://help.shopify.com/en/manual/payments/accelerated-checkouts/google-pay)
  + [PayPal](https://help.shopify.com/en/manual/payments/paypal)
  + [Shop Pay](https://help.shopify.com/en/manual/payments/shop-pay/shop-pay)
  + [Venmo](https://help.shopify.com/en/manual/payments/paypal/supported-providers)

Each payment method has specific requirements before it displays as a branded button.

The kind of accelerated checkout button that displays to your customers depends on the following factors:

* your [payment settings](https://admin.shopify.com/settings/payments)
* whether [Shop Promise](https://help.shopify.com/en/manual/fulfillment/setup/shop-promise) is active, which will prioritize [Shop Pay](https://help.shopify.com/en/manual/payments/shop-pay) over other checkouts
* the customer's browser
* the customer's device
* the customer's personal payment history

When you [add accelerated checkout buttons to your online store](add-buttons.md), your options are to display or hide the accelerated checkout buttons, but you can't customize whether branded or unbranded accelerated checkout buttons display. The branded buttons display depending on payment methods that you've activated in your [payment settings](https://admin.shopify.com/settings/payments). If you don't have a third-party accelerated checkout method activated, then only the unbranded button is displayed. You can [customize the color and fonts of your unbranded accelerated checkout buttons](customize-button.md), but you can't customize the branded versions of the buttons.

If you use gift cards or discount codes in your store, then customers can still enter the codes at checkout.

After you add accelerated checkout buttons to your online store, you can [test the accelerated checkout buttons](test-buttons.md) for the payment methods you've activated.

## Compatibility

There are a few cases where accelerated checkout buttons might not be suitable for your online store. Before you include accelerated checkout buttons on your online store, consider their compatibility with the following features:

* [Apps](dynamic-checkout.md#apps)
* [Cart attributes](dynamic-checkout.md#cart-attributes)
* [Products, payment settings, and button text](dynamic-checkout.md#products-payment-settings-and-button-text)

### Apps

Accelerated checkout buttons might conflict with certain apps.

If you use any of the following kinds of apps, then accelerated checkout buttons might not be compatible with your online store:

* Currency converters
* Apps that interact with the cart
* Apps that take customers to an external checkout

### Cart attributes

Accelerated checkout buttons don't support cart attributes. Cart attributes are custom form fields that you can use to collect additional information from your customers on the cart page.

Examples of cart attributes include the following additions to the cart page:

* Terms and conditions checkboxes
* Gift-wrapping options
* Delivery date pickers

If you rely on cart attributes, then accelerated checkout buttons aren't suitable for your online store.

### Products, payment settings, and button text

Before you include accelerated checkout buttons on your online store, consider the following details:

* Accelerated checkout buttons can only be used to buy a single variant of a product. However, if you display a quantity selector on the product page, then customers can buy more than one of that product. For example, a customer can use an accelerated checkout button to buy three baking cups in aqua, but not to buy one in aqua and one in purple. Unless your online store receives many orders for one kind of product, then accelerated checkout buttons might not benefit your sales.
* If you don't have a third-party accelerated checkout method active in your [payment settings](https://admin.shopify.com/settings/payments), then the unbranded version of the accelerated checkout button is the only version that will display.
* The unbranded version of the accelerated checkout button includes **Buy it now** text. If your **Add to cart** button displays **Buy it now** or other custom text, then this might confuse customers.

## Update your theme to use accelerated checkout buttons

Accelerated checkout buttons are available on all current versions of the themes in the [Shopify Theme Store](https://themes.shopify.com). If you're using an older version of a theme, then you can [update your theme](../themes/managing-themes/updating-themes.md) to use accelerated checkout buttons. If you don't want to update your theme, then you can [edit your theme code](../themes/customizing-themes/edit-code/edit-theme-code.md).

## Display accelerated checkout buttons on product pages

You can adjust your theme settings in the theme editor to display accelerated checkout buttons.

Depending on your [theme version](../themes/managing-themes/versions.md), the buttons might be labelled **Dynamic checkout buttons** instead.

#### Steps:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Click **Edit theme** next to the theme that you want to edit.
3. Click the **Home page** drop-down menu.
4. Click **Products**, and then select the template that you want to edit.
5. In the **Product information** section, click **Buy buttons**.
6. Select **Show accelerated checkout buttons**.
7. Click **Save**.
8. Optional: [Test your accelerated checkout buttons](test-buttons.md).
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap
   .
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage themes**.
4. Find the theme that you want to edit, and then tap **Edit theme**.
5. Tap **Templates**.
6. Select **Product pages**.
7. Tap the **Product pages** or **Product** section.
8. Check **Show accelerated checkout button**.
9. Tap **Save**.
10. Optional: [Test your accelerated checkout buttons](test-buttons.md).

## Display accelerated checkout buttons on a featured product section

Most themes include a setting to include accelerated checkout buttons on a featured product section.

#### Steps:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Click **Edit theme** next to the theme that you want to edit.
3. Click an existing featured product section, or click **Add section** > **Featured product** to add a new featured product section.
4. In the **Featured product** section, click **Buy buttons**.
5. Select **Show accelerated checkout buttons**.
6. Click **Save**.
7. Optional: [Test your accelerated checkout buttons](test-buttons.md).
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap
   .
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to edit, and then tap **Edit theme**.
5. Tap **Edit**.
6. Tap an existing featured product section, or tap **Add section** to add a new featured product section.
7. Enter your product details and check **Show accelerated checkout button**.
8. Tap **Save**.
9. Optional: [Test your accelerated checkout buttons](test-buttons.md).

## Hide accelerated checkout buttons on product pages

You can hide all of the accelerated checkout buttons on your product pages, but you can't hide specific accelerated checkout buttons.

#### Steps:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Click **Edit theme** next to the theme that you want to edit.
3. Click the **Home page** drop-down menu.
4. Click **Products**, and then select the template that you want to edit.
5. In the **Product information** section, click **Buy buttons**.
6. Deselect **Show accelerated checkout buttons**.
7. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap
   .
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage themes**.
4. Find the theme that you want to edit, and then tap **Edit theme**.
5. Tap **Templates**.
6. Select **Product pages**.
7. Tap the **Product pages** or **Product** section.
8. Uncheck **Show accelerated checkout button**.
9. Tap **Save** or **✓**.

## Hide accelerated checkout buttons on a featured product section

You can hide all of the accelerated checkout buttons on your featured product sections, but you can't hide specific accelerated checkout buttons.

#### Steps:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Click **Edit theme** next to the theme that you want to edit.
3. Click the featured product section.
4. Deselect **Show accelerated checkout buttons**.
5. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap
   .
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to edit, and then tap **Edit theme**.
5. Tap **Edit**.
6. Tap the featured product section.
7. Uncheck **Show accelerated checkout button**.
8. Tap **Save** or **✓**.

## Display accelerated checkout buttons for some products but not for others

If you want to display accelerated checkout buttons for some products but not for others, then you can create an alternate template. An alternate template is a duplicate theme code template that you can edit without affecting the original. By using an alternate product template, you can display accelerated checkout buttons for products that use one template and hide them for products that use the other.

To create an alternate product template, refer to [*Create a new template*](../themes/theme-structure/templates.md#create-a-new-template).

After you create an alternate product template and [assign it to a product](../themes/theme-structure/templates.md#apply-a-new-template-to-a-product), you can display or hide accelerated checkout buttons for that product.

#### Steps:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Click **Edit theme** next to the theme for which you created an alternate template.
3. Go to the product page for a product to which you've assigned the alternate template.
4. In the **Product information** section, click **Buy buttons**.
5. To display an accelerated checkout button for products that use the alternate template, select **Show accelerated checkout button**. To hide an accelerated checkout button for products that use the alternate template, deselect **Show accelerated checkout button**.
6. Click **Save**. The changes are applied to any product that uses the alternate template.
7. Optional: [Test your accelerated checkout buttons](test-buttons.md).
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap
   .
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage themes**.
4. Find the theme for which you created an alternate template, and then tap **Edit theme**.
5. In the theme editor, go to the product page for a product to which you've assigned the alternate template.
6. Tap the **Product pages** or **Product** section.
7. To display an accelerated checkout button for products that use the alternate template, check **Show accelerated checkout button**. To hide an accelerated checkout button for products that use the alternate template, uncheck **Show accelerated checkout button**.
8. Tap **Save**. The changes are applied to any product that uses the alternate template.
9. Optional: [Test your accelerated checkout buttons](test-buttons.md).
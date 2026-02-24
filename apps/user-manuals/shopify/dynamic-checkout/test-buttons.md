# Testing your accelerated checkout buttons

Source: https://help.shopify.com/en/manual/online-store/dynamic-checkout/test-buttons

---

# Testing your accelerated checkout buttons

The kind of accelerated checkout button that displays to your customers depends on the following factors:

* your [payment settings](https://admin.shopify.com/settings/payments)
* whether [Shop Promise](https://help.shopify.com/en/manual/fulfillment/setup/shop-promise) is active, which will prioritize [Shop Pay](https://help.shopify.com/en/manual/payments/shop-pay) over other checkouts
* the customer's browser
* the customer's device
* the customer's personal payment history

You can test your accelerated checkout buttons to review all the different configurations that might display to your customers. Before you test your accelerated checkout buttons, make sure that you [add them to your online store](add-buttons.md).

#### Steps:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Click **View your store**.
3. To test the button on a product page, go to a product page. To test the button on a featured product section, stay on the home page.
4. In your browser's address bar, add one of the following strings to the end of the current URL, and then press `Enter` to reload the page:

   * **Shop Pay** - `?shopify-debug=true&show=Shop`
   * **Amazon Pay** - `?shopify-debug=true&show=Amazon`
   * **Apple Pay** (Safari only) - `?shopify-debug=true&show=Apple`
   * **Google Pay** - `?shopify-debug=true&show=Google`
   * **PayPal** - `?shopify-debug=true&show=PayPal`
   * **Venmo** (United States only)- `?shopify-debug=true&show=Venmo`
   * **Unbranded** - `?shopify-debug=true&show=checkout` For example, the URL to test the accelerated checkout button for Amazon Pay might display in this way: `https://mystore.myshopify.com/products/myproduct?shopify-debug=true&show=Amazon`
5. Repeat to test accelerated checkout buttons for other payment methods configured in your payment settings.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap .
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage themes**.
4. Tap **View your store**.
5. To test the button on a product page, go to a product page. To test the button on a featured product section, stay on the home page.
6. In your browser's address bar, add one of the following strings to the end of the current URL, and then press `Enter` to reload the page:
   * **Shop Pay** - `?shopify-debug=true&show=Shop`
   * **Amazon Pay** - `?shopify-debug=true&show=Amazon`
   * **Apple Pay** (Safari only) - `?shopify-debug=true&show=ApplePay`
   * **Google Pay** - `?shopify-debug=true&show=Google`
   * **PayPal** - `?shopify-debug=true&show=PayPal`
   * **Venmo** (United States only)- `?shopify-debug=true&show=Venmo`
   * **Unbranded** - `?shopify-debug=true&show=checkout` For example, the URL to test the accelerated checkout button for Amazon Pay might display in this way: `https://mystore.myshopify.com/products/myproduct?shopify-debug=true&show=Amazon`
7. Repeat to test accelerated checkout buttons for other payment methods configured in your payment settings.
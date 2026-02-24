# Accelerated checkout buttons compatibility

Source: https://help.shopify.com/en/manual/online-store/dynamic-checkout/compatibility

---

# Accelerated checkout buttons compatibility

There are a few cases where accelerated checkout buttons might not be suitable for your online store. Before you add accelerated checkout buttons to your online store, consider their compatibility with the following features:

* [Apps](compatibility.md#apps)
* [Cart attributes](compatibility.md#cart-attributes)
* [Products](compatibility.md#products)
* [Payment settings](compatibility.md#payment-settings)
* [Button text](compatibility.md#button-text)

### Apps

Accelerated checkout buttons might conflict with certain apps.

If you use any of the following kinds of apps, then accelerated checkout buttons might not be compatible with your online store:

* currency converters
* apps that interact with the cart
* apps that take customers to an external checkout

### Cart attributes

Accelerated checkout buttons don't support cart attributes. Cart attributes are custom form fields that you can use to collect additional information from your customers on the cart page.

Examples of cart attributes include the following additions to the cart page:

* terms and conditions checkboxes
* gift-wrapping options
* delivery date pickers

If you rely on cart attributes, then accelerated checkout buttons aren't suitable for your online store.

### Products

Accelerated checkout buttons can be used to buy only single variants of a product. However, if you display a quantity selector on the product page, then customers can buy more than one of that variant. For example, a customer can use an accelerated checkout button to buy two red t-shirts, but not a red t-shirt and a blue t-shirt.

Gift card products with [active recipient fields](../themes/customizing-themes/common-customizations/add-gift-card-recipient-fields.md) won't display accelerated checkout buttons. This is because the recipient information needs to be collected before proceeding to checkout.

### Payment settings

If you don't have a third-party accelerated checkout method activated in your [payment settings](https://admin.shopify.com/settings/payments), then the unbranded version of the accelerated checkout button is the only version that will display.

### Button text

The unbranded accelerated checkout button displays **Buy it now** text. If your **Add to cart** button also displays **Buy it now** or other custom text, then this might confuse customers.
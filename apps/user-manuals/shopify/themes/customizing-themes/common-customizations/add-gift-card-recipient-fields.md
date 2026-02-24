# Add recipient fields to your gift card products

Source: https://help.shopify.com/en/manual/online-store/themes/customizing-themes/common-customizations/add-gift-card-recipient-fields

---

# Add recipient fields to your gift card products

You can activate the following recipient fields for your [gift card products](https://help.shopify.com/en/manual/products/gift-card-products):

* **Recipient email**
* **Recipient name** (optional)
* **Message** (optional)
* **Send on** date (optional)

Customers who buy a gift card product have an option to send the gift card with a custom message to their chosen recipient. Your customer can send the gift card immediately after buying it, or they can send the gift card on a scheduled date. Scheduled gift cards are sent approximately between 4:00 am–10:00 am in the purchasing customer's timezone.

The recipient gets a personalized email that contains the custom message and the gift card code. Your customer receives a notification that contains the gift card code, and the notification confirms that the gift card was sent to the recipient.

## On this page

* [Activate the gift card recipient information form](add-gift-card-recipient-fields.md#activate-the-gift-card-recipient-information-form)
* [Gift card notification templates](add-gift-card-recipient-fields.md#gift-card-notification-templates)
* [Check if your notification templates contain the gift card recipient information fields](add-gift-card-recipient-fields.md#check-gift-card-template-fields)

## Activate the gift card recipient information form

The gift card recipient information form might not be available on some themes. You can confirm whether your theme has the option to activate the gift card recipient information form.

If the option to activate the gift card recipient information form isn't displayed, then your theme doesn't support the gift card recipient feature. You can [find out how to update your theme](../../managing-themes/updating-themes.md).

#### Steps:

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to edit, and then click **Edit theme**.
3. In the theme editor, click the **Home page** dropdown, and then click **Products** > **Default product**.
4. In the **Preview** section of the sidebar, click **Change**.
5. In the **Select product** section, find your gift card product, and then select the gift card product.
6. In the **Product information** section, click the **Buy buttons** block.
7. Select **Show recipient information form for gift card products**.
8. Click **Save**.

You should also [make sure that your gift card notifications contain the gift card recipient information fields](add-gift-card-recipient-fields.md#check-gift-card-template-fields).

## Gift card notification templates

There are two different [*Notifications*](https://help.shopify.com/en/manual/fulfillment/setup/notifications) that might be sent when a gift card is purchased from your store.

### New gift card

This is the notification someone receives when they're the recipient of a gift card. The **New gift card** notification is sent in the following scenarios:

* You create a gift card in your Shopify admin and issue it directly to a customer.
* A customer buys a gift card for themselves without completing the gift card recipient information form.
* Someone receives a gift card as a gift.

### Gift card receipt

This is the notification your customer receives when they purchase a gift card and complete the gift card recipient information form. The **Gift card receipt** notification confirms to your customer that a gift card has been sent to their chosen recipient.

## Check if your notification templates contain the gift card recipient information fields

If you have modified your gift card notification templates or added new languages, then the gift card recipient information fields might not be included in your templates.

You can revert your changes and go to the default templates that contain the gift card recipient information fields, or you can manually add the fields to your templates.

You need to do this for each language that you support with your notifications.

### Revert changes to your notifications

Desktop

1. From your Shopify admin, go to **Settings** > [**Notifications**](https://admin.shopify.com/settings/notifications).
2. Click **Customer notifications**.
3. In the **Gift cards** section, click **New gift card** or **Gift card receipt**.
4. Click **Edit code**.
5. Click **Revert to default**.
6. In the dialog, click **Revert changes**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap  > **Settings**.
2. In the **Store settings** section, tap **Notifications**.
3. Tap **Customer notifications**.
4. In the **Gift cards** section, tap **New gift card** or **Gift card receipt**.
5. Tap the **Edit code** icon.
6. Tap **Revert to default**.
7. In the dialog, tap **Revert changes**.

### Add new fields to your notifications

If you want to keep any changes you've made to your gift card notification templates, then you can manually add the gift card recipient information fields to your templates.

The recipient information fields are documented in the [gift card recipient Liquid reference](https://shopify.dev/docs/api/liquid/objects/gift_card#gift_card-recipient).

#### Steps:

Desktop

1. From your Shopify admin, go to **Settings** > [**Notifications**](https://admin.shopify.com/settings/notifications).
2. Click **Customer notifications**.
3. In the **Gift cards** section, click **New gift card** or **Gift card receipt**.
4. Click **Edit code**.
5. Add the gift card recipient information fields to your notification. Refer to the documentation on how to [*Edit notification templates*](https://help.shopify.com/en/manual/fulfillment/setup/notifications/customizing-notification-template).
6. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap  > **Settings**.
2. In the **Store settings** section, tap **Notifications**.
3. Tap **Customer notifications**.
4. In the **Gift cards** section, tap **New gift card** or **Gift card receipt**.
5. Tap the **Edit code** icon.
6. Add the gift card recipient information fields to your notification. Refer to the documentation on how to [*Edit notification templates*](https://help.shopify.com/en/manual/fulfillment/setup/notifications/customizing-notification-template).
7. Tap **Save** or **✓**.
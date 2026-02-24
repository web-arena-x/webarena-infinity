# Setting your online store preferences

Source: https://help.shopify.com/en/manual/online-store/setting-up/preferences

---

# Setting your online store preferences

You can edit the title and meta description of your online store, add tracking codes, and activate a password page on the [**Preferences**](https://admin.shopify.com/online_store/preferences) page.

## On this page

* [Edit the title and meta description for your home page](preferences.md#edit-title-and-meta-description)
* [Adding or removing your online store password](preferences.md#add-or-remove-the-password-page)
* [Setting up automatic redirection for your international visitors](preferences.md#automatic-redirection)
* [Protecting your online store with hCaptcha](preferences.md#protect-your-store-with-hcaptcha)

## Edit the title and meta description for your home page

You can set the page title and meta description for your online store home page. These display in search engine results. Use descriptive text and keywords to improve the search engine ranking for your online store. Learn more about [search engine optimization](https://help.shopify.com/en/manual/promoting-marketing/seo).

#### Steps:

1. From your Shopify admin, go to **Online Store** > [**Preferences**](https://admin.shopify.com/online_store/preferences).
2. In the **Social sharing image and SEO** section, enter a title and meta description for your store.
3. Optional: Click **Add image** to add a [social media image](../images/showing-social-media-thumbnail-images.md) to your online store.
4. Click **Save**.

## Adding or removing your online store password

You can restrict visitors access to your online store by adding the password page in the **Password protection** section. The password page is a landing page that requires any visitor to provide a password to visit your online store. If you want your customers to access your online store, then you can provide them with the password to your online store.

Learn more about [adding, removing, and customizing the password page](../themes/password-page.md).

## Setting up automatic redirection for your international visitors

When you activate automatic redirection, the online storefront that matches the location preferences of your customers is automatically displayed. You can also activate language redirection, which detects a customer's browser language and automatically switches the storefront to match, when that language is available.

Learn more about [setting up automatic storefront redirection for international customers](https://help.shopify.com/en/manual/international/automatic-redirection).

## Protecting your online store with hCaptcha

hCaptcha helps analyze the behavior of visitors to your online store to block spam from bots. hCaptcha also reduces friction for real users by eliminating captcha challenges and is enabled by default on all Shopify stores.

hCaptcha can display in the following locations of your online store:

* In [contact, newsletter signup, and comment forms](preferences.md#contact-comment).
* On [login, create account, and password recovery pages](preferences.md#hcaptcha-login-account-register).

To learn more about editing hCaptcha in themes, visit [Shopify.dev](https://shopify.dev/themes/trust-security/captcha).

### Activate or deactivate hCaptcha on your online store

hCaptcha is activated by default on all Shopify stores. Information about hCaptcha is available to all visitors. hCaptcha continuously monitors the visitor’s behavior to determine whether it’s a human or a bot.

If hCaptcha can't determine whether a visitor is a bot, then it will either return an error, or potentially redirect the user to a page to solve an interactive challenge.

hCaptcha isn't compatible with custom code or third-party apps that add CAPTCHA. If you have custom code or a third-party app that adds CAPTCHA and you have hCaptcha activated, then your customers might experience issues with hCaptcha. To ensure hCaptcha works for your customers, remove custom code and deactivate CAPTCHA on third-party apps.

The hCaptcha logo displays on any form with hCaptcha activated, when the user interacts with the form:

#### Steps:

1. From your Shopify admin, go to **Online Store** > [**Preferences**](https://admin.shopify.com/online_store/preferences).
2. In the **Spam protection** section, you can check to activate or uncheck to deactivate hCaptcha for that location:

   * [**Enable hCaptcha on contact and comment forms**](preferences.md#contact-comment).
   * [**Enable hCaptcha on login, create account, and password recovery pages**](preferences.md#hcaptcha-login-account-register).

### hCaptcha on contact and comment forms

Use hCaptcha on contact forms and blog comments to minimize incoming spam from bots. hCaptcha is activated by default on all Shopify stores.

When activated, all form submissions will perform an invisible (non-interactive) challenge. Challenges assessed as suspicious will result in a redirect to the `/challenge` page to solve an interactive puzzle, or click an "I'm a human" checkbox.

Even when hCaptcha is deactivated in admin, customers who make multiple comments or enter comments from email addresses that hCaptcha considers suspicious are redirected to the page where they can complete the interactive challenge flow described above.

### hCaptcha on customer login, account, and register forms

Use hCaptcha on [legacy customer account](https://help.shopify.com/en/manual/customers/customer-accounts/legacy-customer-accounts) login pages, create account pages, and password recovery forms to minimize unwanted traffic to your online store. hCaptcha is activated by default on all Shopify stores.

When hCaptcha is activated, suspicious traffic might encounter one or both of the following friction points:

* An interactive challenge immediately after submitting the form
* A "CAPTCHA failed" error message, if there is a very high certainty that the interaction isn't from a human

#### Update for hCaptcha on customer login, account, and register forms

If an admin alert displays in your Shopify admin to update your customer login form, customer account form, or customer register form, then you need to update the connection between hCaptcha and these forms by March 7, 2025. This ensures that customers can continue to log in, access their accounts, and check out on your store without disruption.

You need to take one of the following actions to update your connection between hCaptcha and customer forms on your store:

* [Upgrade to customer accounts](https://help.shopify.com/en/manual/customers/customer-accounts/new-customer-accounts/manage#set-up-customer-accounts) to give customers access to passwordless login using a one-time 6-digit verification code. In addition to a faster login and checkout experience, the customer accounts verification process doesn't require hCaptcha. Learn more about [customer accounts](https://help.shopify.com/en/manual/customers/customer-accounts/new-customer-accounts).
* To continue using legacy customer accounts, update your theme to configure the upgraded version of hCaptcha on your store. For more information, refer to Shopify's [*CAPTCHA*](https://shopify.dev/docs/storefronts/themes/trust-security/captcha) developer documentation.
* If you want to continue using legacy customer accounts, and no longer want hCaptcha to display on your store, then [deactivate hCaptcha](preferences.md#activate-deactivate-hcaptcha).
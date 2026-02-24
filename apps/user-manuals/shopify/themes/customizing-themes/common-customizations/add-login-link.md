# Add a customer login link to your theme

Source: https://help.shopify.com/en/manual/online-store/themes/customizing-themes/common-customizations/add-login-link

---

# Add a customer login link to your theme

If you're using [customer accounts](https://help.shopify.com/en/manual/customers/customer-accounts/new-customer-accounts), and a login link doesn't display in your theme header for customers to login, then you can add a customer login link to your theme.

## On this page

* [Check for a login link on your theme](add-login-link.md#check)
* [Add a login link to your theme](add-login-link.md#add)

## Check for a login link on your theme

Many themes include login links by default. Before you proceed with this tutorial, check if login links are supported on your theme.

#### Steps:

1. From your Shopify admin, go to **Settings** > [**Customer accounts**](https://admin.shopify.com/settings/customer_accounts).
2. Turn on the **Show login links** toggle button.
3. After you turn on login links, visit your online store as though you're a customer, and check for the profile icon in your store header to log in.
4. If the profile icon doesn't display, then follow the steps to add a login link to your theme.

## Add a login link to your theme

If a profile icon doesn't display in your online store header that lets customers log in to your store, then you can add a login link to your theme.

#### Steps:

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme you want to edit, click the **…** button to open the actions menu, and then click **Edit code**.
3. In the **Sections** folder, open the `header.liquid` file.
4. Add the following snippet of code to the `header.liquid` file, and then click **Save**.

* To direct customers to customer accounts after login:

```
{% if customer %}
 <a href="{{ routes.account_url }}">Account</a>
{% else %}
 <a href="{{ routes.account_login_url }}">Login</a>
{% endif %}
```

* To direct customers back to the online store after login:

```
{% if customer %}
 <a href="{{ routes.account_url }}">Account</a>
{% else %}
 <a href="{{ routes.storefront_login_url }}">Login</a>
{% endif %}
```
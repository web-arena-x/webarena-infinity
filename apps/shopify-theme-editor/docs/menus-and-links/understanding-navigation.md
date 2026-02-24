# Understanding menus

Source: https://help.shopify.com/en/manual/online-store/menus-and-links/understanding-navigation

---

# Understanding menus

When you set up your online store, consider how you want customers to find your products and information about your business. This can help you make decisions about your online store menus, and how to set up your menus.

## On this page

* [Default menus](understanding-navigation.md#default-menus)
* [Comparing menus in different themes](understanding-navigation.md#comparing-navigation)
* [Troubleshooting issues with your menus](understanding-navigation.md#troubleshooting-issues-with-your-menus)

## Default menus

Your online store has two default menus that display on every page: the main menu and the footer menu. You can [add, remove, or edit menu items](editing-menus.md) in your online store's default menus.

If you use [customer accounts](https://help.shopify.com/en/manual/customers/customer-accounts/new-customer-accounts), then a customer account main menu is also included on your store by default.

You can [add, remove, or edit menu items](editing-menus.md) in your online store's default menus. All menus can include online pages such as products, collections, webpages, blog posts, and customer account pages, as well as links to other websites. You can also create [drop-down menus](drop-down-menus.md) within your main menu and customer account menu.

### Main menu

The main menu displays on every page of your online store. The main menu usually displays as items across the width of the header, or else as a list of items in a sidebar. A customer might view your main menu to find your products and information about your business, such as an "About us" page.

Your main menu has the following two default menu items:

* **Home**: the main page of your online store
* **Catalog**: a page that displays all of your products

### Footer menu

The footer menu usually displays as items across the width of the footer. A customer might view your footer menu to find information about your store policies and contact information.

### Customer account menu

The customer account main menu displays on your online store, as well as anywhere that you use your customer account header, such as a [mobile app](https://shopify.dev/docs/storefronts/headless/mobile-apps). Learn more about [customizing your customer account menus](https://help.shopify.com/en/manual/customers/customer-accounts/new-customer-accounts/customize#customer-accounts-menu).

### Other menus

Depending on your store's theme, you might be able to add a new menu by editing the settings in the theme's **Header** section. If your theme doesn't let you add a new menu by editing theme settings, then you can [customize your theme code](https://shopify.dev/themes/navigation-search/navigation) to add a new menu. You can also hire a Shopify Partner to make the changes for you.
Learn more about [hiring a Shopify Partner](https://help.shopify.com/en/manual/partner-directory).

## Comparing menus in different themes

Every theme has a different design, so your menus might display differently on different themes.

For a demonstration, go to any theme in the [Shopify Theme Store](https://themes.shopify.com/themes) and click **View Demo**.

## Troubleshooting issues with your menus

Menu issues can be from multiple factors. Review the following areas of your admin and your theme to ensure that the menu is configured properly and you have no incompatibility issues:

* Review the menu item to ensure the link and link type are correct.
* Ensure that the link is set correctly. If you're linking to a sub-menu, then you might need to adjust the link type or remove any unnecessary nesting.
* Ensure your theme allows the type of menu you're trying to create. For example, if you're creating a multi-level drop-down menu, then your theme needs to support that menu type.
* Review your theme settings to ensure the correct menu is linked.
* Ensure there is no custom code in your theme that's causing the menu issues. You can [roll back your theme code](../themes/customizing-themes/edit-code/edit-theme-code.md#roll-back) to test that the code is causing a conflict.
* Review your apps to ensure they aren't overriding your menu with a menu in the app.

### Common navigation issues

**Menu changes not appearing on storefront**

If menu changes in your admin don't appear on your storefront, then review these areas:

1. **Theme menu settings**: Verify that your theme is using the correct menu. Check your theme settings in **Header** and **Footer** sections to confirm the selected menu matches the one you're editing.
2. **Menu apps**: Navigation apps (such as "Mega Menu" apps) create menus within the app instead of using your admin menu settings. If you have a menu app installed, then either update the app settings or uninstall the app to use your default navigation.
3. **Old navigation structure**: Stores created before nested navigation was available might need menu restructuring. Consider recreating your menus using the current nested format instead of linking to separate menus.

### Theme compatibility issues

**Theme doesn't support multilevel navigation**

Some older theme versions don't support multilevel (three or more levels) drop-down menus. If your nested menus aren't displaying properly, then your theme might need updating. All Online Store 2.0 themes support multilevel navigation, but older sectioned themes might require updates to support multiple menu levels.
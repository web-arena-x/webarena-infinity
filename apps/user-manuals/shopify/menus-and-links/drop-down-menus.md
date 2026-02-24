# Set up drop-down menus in your online store

Source: https://help.shopify.com/en/manual/online-store/menus-and-links/drop-down-menus

---

# Set up drop-down menus in your online store

You can use drop-down menus to group products, collections, or pages together and make it easier for customers to navigate your online store. For example if you have a lot of products, then you might want to add them to collections and then use a drop-down menu from the main menu to organize the collections. This can help customers find the type of products that they're looking for.

You can also [add, remove, or edit menu items](editing-menus.md) in drop-down menus or in your default menus.

You can view and change your online store menus from **Content** > [**Menus**](https://admin.shopify.com/content/menus) in your Shopify admin.

## On this page

* [Nesting menu items to build drop-down menus](drop-down-menus.md#nesting-menu-items-to-build-drop-down-menus)
* [Add a drop-down menu from the main menu](drop-down-menus.md#add-a-drop-down-menu-from-the-main-menu)
* [Footer menu integration](drop-down-menus.md#footer-menu-integration)
* [Theme compatibility considerations](drop-down-menus.md#theme-compatibility-considerations)
* [Determining whether your theme supports nested drop-down menus](drop-down-menus.md#determining-whether-your-theme-supports-nested-drop-down-menus)
* [Best practices for drop down menus](drop-down-menus.md#best-practices-for-drop-down-menus)
* [Troubleshooting common issues](drop-down-menus.md#troubleshooting-common-issues)
* [Customizing theme code for drop-down menus](drop-down-menus.md#customizing-theme-code-for-drop-down-menus)

## Nesting menu items to build drop-down menus

You can build drop-down menus by creating or moving menu items so that they're nested below a top-level item. The top-level item displays in the main menu on your online store, and the nested menu items display in a drop-down menu. The top-level item can have up to two levels of nested drop-down menus.

All themes will display nested items as drop-down menus from the main menu, and some themes will display nested items as drop-down menus in other locations.

The main menu and drop-down menus display in different locations in your online store depending on your [theme](../themes.md). Some themes display an icon beside the name of a drop-down menu in the main menu to help customers recognize that a drop-down menu is there.

## Add a drop-down menu from the main menu

You can [add a drop-down menu](drop-down-menus.md) from any of the menu items in the main menu.

#### Steps:

Desktop

1. From your Shopify admin, go to **Content** > [**Menus**](https://admin.shopify.com/content/menus).
2. Click the name of your main menu.
3. Choose one of the main menu items to be the header of your drop-down menu, or [add a new menu item](editing-menus.md#add-menu-item). If you don't want the header to link to anything, then enter `#` in the **Search or paste a link** field for the header menu item.
4. To add a menu item to include in the drop-down menu, complete the following tasks:

   1. Click **Add menu item**.
   2. In the **Name** field, enter a name for your menu item.
   3. In the **Search or paste a link** field, enter or select a destination for your menu item.
5. Click **Add**, and then click and drag the menu item to nest it below the header menu item.
6. Click **Save menu**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap .
2. In the **Contents** menu, tap the icon, and then tap **Menus**.
3. Tap the name of your main menu.
4. Choose one of the main menu items to be the header for your drop-down menu, or [add a new menu item](editing-menus.md#add-menu-item) to be the header. If you don't want the header to link to anything, enter `#` in the **Search or paste a link** field for the header menu item.
5. To add a menu item to include in the drop-down menu, complete the following tasks:
   1. Tap **Add menu item**.
   2. In the **Name** field, enter a name for your menu item.
   3. In the **Search or paste a link** field, enter or select a destination for your menu item.
6. Tap **Add**, and then tap and drag the menu item to nest it below the header menu item.
7. Tap **Save** or **✓**.

## Footer menu integration

Drop-down menus can also be implemented in footer menus.

#### Steps:

1. From your Shopify admin, go to **Content** > [**Menus**](https://admin.shopify.com/content/menus).
2. Optional: Follow the same [nesting principles used for main menus](drop-down-menus.md#nesting-menu-items-to-build-drop-down-menus), such as dragging menu items under a header item to create a drop-down structure by clicking and dragging the items into place.
3. Enter `#` in the **Link** field for header items that shouldn't link to a page (for example, "Support" or "Explore" headers).

## Theme compatibility considerations

Review the following considerations for adding drop-down menus to your theme:

* Most themes support up to two levels of nested drop-down menus. Check your [theme's documentation](../themes/theme-support/documentation.md) or test nested items to confirm compatibility.
* Some themes might require CSS adjustments to improve mobile usability. Don't customize your theme if you aren't familiar with theme code. Learn more about [customizing your theme](../themes/customizing-themes/edit-code/edit-theme-code.md).

## Determining whether your theme supports nested drop-down menus

To determine if your current theme supports the maximum number of nested drop-down menu levels you want to implement, you can use the following resources:

1. Check your theme's documentation: Review the [theme's documentation](../themes/theme-support/documentation.md) for specific information about menu capabilities and supported nesting levels.
2. Test the nested items: Create a test menu structure with your desired number of nested levels and verify that it displays correctly on both desktop and mobile devices.

Most themes support up to two levels of nested drop-down menus. If you're experiencing issues with drop-down menus, verify that your theme supports the number of nested levels you're trying to implement, as some themes might require additional customization to support multiple levels of nesting.

## Best practices for drop down menus

Review the following best practices to create a useful menu structure that works well across all devices:

* Use descriptive labels, such as "Shop by Category", for top-level menu items with `#` links.
* Ensure that menus are optimized on mobile devices. You can test menus on mobile devices to confirm that drop-down menus expand as expected.
* Add seven or fewer top-level menu items to avoid overcrowding.
* Use clear and descriptive link titles. For example "Collections" and "Summer dresses".
* Each menu can have up to 10,000 items, and your store can have up to 1,000 menus total. Any menu item with sub-items in a drop-down menu count as a separate menu toward this limit.

### Drop-down menu accessibility

Most themes implement drop-down menu headers as buttons rather than clickable links. This is an intentional accessibility design that helps customers who use assistive technology understand navigation structure.

When a top-level menu item controls a drop-down submenu, it functions as a button to expand the menu rather than as a link to a new page. This approach ensures that customers using screen readers or other assistive devices can properly navigate your store's menu system.

If you want customers to access a main category page (such as "All Products" or "All Collections"), then add this as the first item within the drop-down menu itself instead of making the header clickable.

## Troubleshooting common issues

Review the following solutions to common problems you might encounter when setting up navigation menus:

* **Mobile menu redirects**: If a top-level menu link redirects to a new page when you tap it, then check the menu in your Shopify admin to confirm that the menu link field is `#`.
* **Visibility issues**: If nested items don't display, then make sure that they're dragged fully under the header item and indented in the **Menus** interface. Confirm that your theme supports the number of nested levels that you have set up.
* **Theme compatibility**: If you're experiencing issues with drop-down menus, verify that your theme supports the number of nested levels you're trying to implement. Some themes might require additional customization to support multiple levels of nesting.
* **Nested menu creation blocked**: If you encounter the error "Menu cannot contain nested menus. Opt in the nested navigation feature to use this", then your store might need the nested navigation feature activated. This typically affects stores created before 2018. Contact Shopify Support if you encounter this error.
* **Wrong menu displaying**: If you have multiple navigation links pointing to the same page (such as your home page), then your theme might display the wrong submenu. Ensure each navigation section links to a unique page to avoid confusion.
* **Menu items disappearing**: If menu links disappear without being deleted, check whether you've deleted the products, collections, or pages that the menu items linked to. Deleting the linked resource also removes the menu item.

## Customizing theme code for drop-down menus

For themes requiring deeper customization, you can consider [customizing your theme code](../themes/customizing-themes/edit-code/edit-theme-code.md).
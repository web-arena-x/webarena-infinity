# Customizing your theme for specific markets or Shopify B2B

Source: https://help.shopify.com/en/manual/online-store/themes/customizing-themes/store-contextualization/create-and-manage-overrides

---

# Customizing your theme for specific markets or Shopify B2B

You can create, edit, or remove market overrides from the theme editor in the **Online Store** > [**Themes**](https://admin.shopify.com/themes) section of your Shopify admin. You can also manually add sections or blocks to markets with overrides from the store Default, and reset your market templates to the store Default.

## On this page

* [Edit an existing section or block](create-and-manage-overrides.md#edit-an-existing-section-or-block)
* [Add a section or block](create-and-manage-overrides.md#add-a-section-or-block)
* [Manually add a section or block](create-and-manage-overrides.md#manually-add-a-section-or-block)
* [Add the Quick order list section to your product page](create-and-manage-overrides.md#quick-order-list)
* [Resetting your market to store Default](create-and-manage-overrides.md#resetting-your-market-to-store-default)

## Edit an existing section or block

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Click the **Market** drop-down menu at the top of the page, and then select a market that you want to customize.
3. Use the drop-down menu to select a market that you want to customize.
4. Edit the section or block that you want to change for the market.
5. Click **Save**.

## Add a section or block

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Click **Edit theme** next to the theme that you want to edit.
3. Click the **Market** drop-down menu at the top of the page, and then select a market that you want to customize.
4. Add a section or block for the market.
5. In the **Overriding section order** or **Overriding block order** dialog, click **Continue**. The **Overriding section order** dialog displays only one time per template although the **Overriding block order** dialog displays only one time per editing session.
6. Click **Save**.

## Manually add a section or block

When you add a section or block to the store Default, it's automatically added to all other markets, except for markets with a custom section order. If you want the added section or block to display in a market that has a custom section order, then you need to manually add the section or block.

#### Steps:

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Click **Edit theme** next to the theme that you want to edit.
3. Click the **Market** drop-down menu at the top of the page, and then select a market that you want to customize.
4. Click **Add section**.
5. In the **FROM STORE DEFAULT** section, click the section that you want to manually add to your market.
6. Click **Save**.

## Add the Quick order list section to your product page

The **Quick order list** section optimizes the shopping experience for bulk ordering and B2B customers.

If you use a [free theme from Shopify](https://themes.shopify.com/collections/free-themes), version 11.0.0 or later, then you can add the **Quick order list** section to your **Products** template, so that your business-to-business (B2B) customers can easily purchase multiple quantities across different product variants.

#### Steps:

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Click **Edit theme** next to the theme that you want to edit.
3. Click the **Market** drop-down menu at the top of the page, and then select a market that you want to customize.
4. Click the **Template** drop-down menu.
5. Click **Products**, and then select a product.
6. In the **Template** section, click **Add section** > **Quick order list**.
7. Click **Save**.

After you add the **Quick order list** section, consider hiding the following blocks, because all purchases will be completed using the quick order list:

* Buy buttons block
* Quantity selector block
* Variant picker block

## Resetting your market to store Default

You can reset the market's inheritance with the store Default content and layout by clicking the icon. For more information on how sections are grouped into a page template, refer to [section groups](../theme-editor/customizing-sections.md#section-groups).

Understanding reset actions

| Reset action | Description | Example |
| --- | --- | --- |
| **Reset a setting or visibility override on a section or block** | When you reset a setting or visibility override on a section or block, you're removing a specific override that was applied to the section or block. After the override is removed, the setting in the section or block will return to inheriting values used in the store Default. | |
| **Reset an entire section or block from the menu** | When you reset an entire section or block, you're removing all of the override settings that were applied to that section or block. After the overrides are removed, the section or block will return to inheriting all of the setting values used in the store Default. | |
| **Reset an entire template or section group** | When you reset a template, you're removing all of the override settings that were applied to the template sections, including changes made to the order of the sections. | |

#### Steps:

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Click **Edit theme** next to the theme that you want to edit.
3. Click the **Market** drop-down menu at the top of the page, and then select a market that you want to customize.
4. Find the template that you want to reset, and click the icon.
5. Click **Save**.
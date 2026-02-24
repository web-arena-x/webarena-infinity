# Adapting themes for specific markets

Source: https://help.shopify.com/en/manual/online-store/themes/customizing-themes-for-markets

---

# Adapting themes for specific markets

If you've [created](https://help.shopify.com/en/manual/markets-new/manage#create-market) at least one market, then you can adapt your theme for your different markets. Adapting your theme for specific markets helps you to create a better experience for customers in those markets. For example, you can make the following customizations:

* highlight different collections on your home page for different markets
* promote a sale on product pages for a specific market
* add messaging to your store that's relevant to specific markets

## On this page

* [Customizing themes for markets](customizing-themes-for-markets.md#customize-theme)
* [Resetting theme customizations for a market](customizing-themes-for-markets.md#reset-customizations)
* [Change theme inheritance](customizing-themes-for-markets.md#change-inheritance)

## Customizing themes for markets

When you customize a theme, you can select whether you want to edit your store default, or a specific market.

The store default is the standard appearance of your theme, without any customizations for specific markets. The default layout and content of your theme can be inherited by or overridden for other markets. Changes that are made to the store default apply to all markets, unless they're overridden.

You can select which market you want to edit from the markets drop-down menu. The markets for which you’ve already customized your theme are displayed first, followed by the markets for which you have yet to customize your theme in the **More customizable markets** section.

When you customize a theme setting in **Store default**, that change applies to all your markets, unless this setting was already customized in a specific market. Changes are applied to your theme settings in the following order:

* Store default: customizing a store default theme setting affects your theme for all your markets and submarkets, unless that setting has already been customized for a market or submarket.
* Market: customizing a theme setting for a market affects your theme for the market, and for all that market's submarkets, unless that setting has already been customized for a submarket.
* Submarket: customizing a theme setting for a submarket affects only that submarket.

#### Steps:

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Click **Edit theme** next to the theme that you want to edit.
3. Click **Store default** to open the markets menu.
4. Select the market that you want to customize.
5. Make your [desired customizations](../themes.md) to sections or blocks for that market, or add new sections or blocks.
6. Click **Save**.

## Resetting theme customizations for a market

Any customization that you make to your theme for a specific market can be reset to the store default.

Table of reset types for markets theme customizations.

| Reset type | Description | Steps |
| --- | --- | --- |
| Individual setting | When you reset a setting override in a market, the setting returns to inheriting settings from the parent market. | In the theme editor, click the reset button next to the title of the setting. |
| Section or block | When you reset an entire section or block in a market, all of the settings for that section or block return to inheriting settings from the parent market, including the order of blocks. | In the theme editor, click **…** next to the title of the section or block, and then click the reset button. |
| Template or section group | When you reset an entire template or section group in a market, all of the settings for that template or section group return to inheriting settings from the parent market, including the order of the sections and blocks. | In the theme editor, click the reset button next to the title of the template or section group. |
| All theme customizations for a market | When you delete all your customizations for a market, all of its settings return to inheriting settings from the parent market, including the order of the sections and blocks. | On your **Markets** page, click the market that you want to reset. In the **Customized** section, click the delete icon next to **Online Store**. |

## Change theme inheritance

When you customize your theme for a submarket, you can change which market the customizations are inherited from. This is referred to as changing the *source of inheritance*. When you change the source of inheritance for a theme, the following are the available options:

* the store default (`@default`)
* any parent market for which the theme has already been customized

#### Steps:

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme you want to edit, click **…**, and then click **Edit code**.
3. Open the `markets.json` file.
4. Find the section of the code that controls market inheritance.
5. Locate the market that you want to edit the source of inheritance for, and replace the `"parent":` value with the market value that you want it to inherit from.
6. Click **Save**.

For example, you make theme customizations to your Canada market. Those changes are currently based on your store's default settings.

If you then decide to customize your theme for the North America market, by default Canada will be updated to inherit from North America, and any theme customizations that you make for the North America market are automatically applied to the Canada market.

If you wish, you can adjust your customizations for Canada to inherit from the store default instead.
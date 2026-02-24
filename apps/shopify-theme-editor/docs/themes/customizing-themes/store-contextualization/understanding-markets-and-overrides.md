# Understanding markets and market overrides for your theme

Source: https://help.shopify.com/en/manual/online-store/themes/customizing-themes/store-contextualization/understanding-markets-and-overrides

---

# Understanding markets and market overrides for your theme

If you have multiple markets, then you can create overrides in the theme editor for specific [international markets](https://help.shopify.com/en/manual/international) or [B2B](https://help.shopify.com/en/manual/b2b) by modifying sections or blocks in the theme editor in your Shopify admin.

Your theme has a store Default, which is the base layout for all markets. Changes that you make in store Default apply to all markets. If you modify a section or block in a market other than the store Default, then the theme editor creates an override for that section, block, or template.

If a market has a section or block with an override, then that section or block no longer automatically inherits updates when you update the store Default. Any areas unaffected by the override will still inherit updates.

If you make a change in your store Default, and that change doesn't apply to a market with an override, then you can [manually apply those changes](create-and-manage-overrides.md#manually-add-a-section-or-block) to your markets.

## On this page

* [Market drop-down menu options](understanding-markets-and-overrides.md#market-drop-down-menu-options)
* [Identifying market overrides](understanding-markets-and-overrides.md#identifying-market-overrides)
* [Market language](understanding-markets-and-overrides.md#market-language)

## Market drop-down menu options

Markets help you adapt your online store experience for different customers. In the theme editor, you can select the market you want to edit from the **Market** drop-down menu.

Understanding the Market drop-down menu options

| Option | Description |
| --- | --- |
| Default | The store Default is used to create a default layout and content that other markets can inherit or override. Changes made to the store Default apply to all markets unless they're overridden. |
| Market name | All of your markets are displayed in the market drop-down menu. You can select a market to make changes that apply only to that specific market. |
| B2B | If you're on the Shopify Plus plan and you use Shopify B2B, then the B2B option is displayed in the market drop-down menu. You can select the B2B option and make changes that apply to the B2B market. |

### Market overrides

You can use the theme editor to create any of the following types of market overrides:

Understanding market overrides

| Market override type | Description | Effect on inheriting updates from store Default |
| --- | --- | --- |
| Setting | Changing a setting, such as an image or text creates a setting override. For example, in the store Default, the Announcement bar text is "Hello", but in the Canada market, you change the Announcement bar text to "Howdy". | If you update a setting in the store Default, then the setting in the market with the override doesn't inherit that update. Other updates to the section or other settings from the store default, for example adding a block to a Rich text section, are still inherited in the market with the setting override. |
| Visibility | Changing the visibility of a section or block creates a visibility override. For example, in the Canada market, you hide an Image with text section. | If you update the visibility in the store Default, then the visibility in the market with the override is not inherited. Other updates to the section from the store default, for example adding a block to a Rich text section, are still inherited in the market with the visibility override. |
| Custom section order | Changing the section order by adding, removing, or reordering a section creates a custom section order override. For example, in the Canada market, the order of sections is different from the store Default. | The following updates from the store Default aren't inherited:  * Adding a new section. * Reordering a section.  The following updates from the store Default are still inherited:  * Setting changes to a block or section. * Visibility changes to a block or section. * Adding, removing, or reordering blocks within sections. * Deleting a section. * Any changes to section groups. For example, if the override is in the Template, then a change in the store Default to the Footer is still inherited.  If you want to include a newly-added section in a market with a custom section order, then you can add the section manually. This added section will inherit any future updates from the store Default. |
| Custom block order | Changing the block order by adding, removing, or reordering a block in a section creates a custom block order override. For example, the order of blocks in a Rich text section in the Canada market is different from the store Default. | If you update the block order in the store Default by adding or reordering a block, then the block order in the market with the override is not inherited. The following updates from the store Default are not inherited:  * Adding a new block to the section. * Reordering blocks in the section.  The following updates from the store Default are still inherited:  * Setting changes to a block or section. * Visibility changes to a block or section. * Adding, removing, or reordering sections. * Deleting a block or section. * Any changes to section groups. For example, if the override is in the Template, then a change in the store Default to the Footer is still inherited.  If you want to include a newly-added block in a market with a custom block order, then you can add the block manually. This added block will inherit any future updates from the store Default. |

## Identifying market overrides

You can identify market overrides in the theme editor by checking for the following labels or icons:

Icons and labels for market overrides in the theme editor

| Market override type | Icon or label |
| --- | --- |
| Setting | A  icon is shown next to the affected setting, block, or section. |
| Visibility |
|
| Added section | A icon is displayed next to the added section and all of its blocks.   Its section group displays a "Customized section order" label. |
| Removed or reordered section | The affected section group displays a "Customized section order" label. |
| Added block | A  icon is displayed next to the added block.   A  icon is displayed next to the block's section. |
| Removed or reordered block | A  icon is displayed next to the block's section. |

## Market language

If your store's primary language isn't available for a market, then you need to use a translation app to customize content in the market's language. You can't modify sections or blocks in the theme editor unless the primary language is available to the market. Learn more about [managing market languages](https://help.shopify.com/en/manual/international/localization-and-translation#manage-markets-languages).
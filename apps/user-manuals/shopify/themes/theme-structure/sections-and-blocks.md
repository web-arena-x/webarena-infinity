# Sections and blocks

Source: https://help.shopify.com/en/manual/online-store/themes/theme-structure/sections-and-blocks

---

# Sections and blocks

You can use sections in your theme to create the layout that you want for your online store. Sections are made up of different types of blocks that each have a specific function, such as text, buttons, single images, a collage of images, or links.

Sections and blocks provide flexibility in how you arrange your content, and allow you to control the style and feel of your online store without the need to edit code, including the following customization options:

* You can rearrange sections in your templates, and rearrange blocks within sections.
* Sections and blocks can have specific customization settings.
* You can connect compatible sections and blocks to display dynamic information on your online store from custom data, such as adding [care instructions for your products](https://help.shopify.com/en/manual/custom-data/metafields/using-metafields). Learn more about connecting [dynamic sources](sections-and-blocks.md#dynamic-source-selector).

The sections and blocks that are available in the theme editor depend on your theme and theme version. For example, your theme might have a **Slide** block that you can add only to a **Slideshow** section, and a **Heading** text block that you can add to all of your theme's sections. For more information about which options are available to you, refer to your theme's documentation.

### Section and block maximum limits

Sections and blocks have the following maximum limitations:

* Each [template](templates.md) can have up to 25 sections.
* Each template can have up to 1250 blocks across all sections. The exact number of blocks, and the number of each type of block that you can add to each section depend on the section and block sources, and are specified by the theme designer for your theme. For example, if your theme has an **Email signup** section, then you might only be able to add one **Email form** block.
* Blocks that support nesting can have up to eight levels of nested blocks.

## On this page

* [Block sources](sections-and-blocks.md#block-sources)
* [Customizing your theme templates with sections and blocks](sections-and-blocks.md#sections-and-blocks)
* [Add a section](sections-and-blocks.md#add-section)
* [Edit a section](sections-and-blocks.md#edit-section)
* [Rearrange a section or block](sections-and-blocks.md#rearrange)
* [Duplicate a section or block](sections-and-blocks.md#duplicate-section)
* [Copy and paste blocks](sections-and-blocks.md#copy-paste-blocks)
* [Hide or delete a section or block](sections-and-blocks.md#remove-section-or-block)
* [Renaming a section or block](sections-and-blocks.md#rename-section-or-block)
* [Working with blocks](sections-and-blocks.md#blocks)
* [Add a block](sections-and-blocks.md#add-block)
* [Use metafields and metaobjects with dynamic sources](sections-and-blocks.md#metafields-and-dynamic-sources)

## Block sources

Depending on your theme's structure, and the apps that you have installed, your theme might contain a variety of sections that accept blocks from different sources. When you add a block to a section, all available blocks for that section display in the block picker. Depending on your theme and theme version, you can add the following types of blocks to sections in your theme:

* [**App blocks**](../customizing-themes/apps.md#app-blocks) are blocks that adds functionality to your theme. You can use an app block to reposition areas of your theme added by your installed apps to a specific area of a page in your theme.
* [**Section blocks**](sections-and-blocks.md#theme-blocks) are blocks that are defined within a specific section.
* [**Theme blocks**](sections-and-blocks.md#theme-blocks) are blocks that are defined within your theme and can have dynamic functionality, such as nesting.

Your theme can contain some sections that use [section blocks](sections-and-blocks.md#section-blocks) and other sections that use [theme blocks](sections-and-blocks.md#theme-blocks). A single section can accept either theme blocks or section blocks, but not a mixture both.

The availability of app blocks within sections depend on the app's functionality, and whether the section can accept app blocks.

### Section blocks

Section blocks are blocks that are designed for a specific section. A section can have limits for the types of section blocks, and limit the number of a certain type of block that you can add.

### Example of a section with section blocks

For example, your theme has an **Email signup** section. You can use this section to add a newsletter signup form so that customers can subscribe to your newsletter. After you add the **Email signup** section, you can add one of each of the following blocks:

* an **Email form** block
* a **Heading** block
* a **Subheading** block

If you add the **Email form** block and click **Add block** to add another block, then the **Email form** block no longer displays as an option in the block picker. This limitation helps prevent any issues with capturing the customer's email, and ensures that the customer can easily enter their email address.

If you've added all three of the available blocks for the **Email signup** section, then the block picker displays a message that all available blocks have been used.

### Theme blocks

Theme blocks are blocks that are defined within your theme and can have dynamic functionality, such as nesting. Sections that accept theme blocks can accept a variety of different blocks, depending on the section's structure. A section that accepts theme blocks might accept all available theme blocks, a specific subset of blocks, or blocks unique to that section. Theme blocks might also have the following behaviors:

* Some blocks support nesting, so that you can nest blocks within other blocks up to eight levels.
* Some sections have required blocks. You can customize or hide these blocks, but you can't re-order or delete them.
* Some blocks display automatically in a section when certain conditions are met.

### Example of a section with theme blocks

For example, your theme has a **Slideshow** section with theme blocks.

In the slideshow section of your theme, when you click **Add block**, you can select a **Slide** block from the block picker. No other block types are available. If you try to add a **Slide** block to another section in your theme, such as an **Image banner** section, then **Slide** isn't available. This is an example of a restricted block.

After you add a **Slide** block to the **Slideshow** section, you can click **Add block** to add additional blocks to any **Slide** blocks in the **Slideshow** section, such as a **Heading**, **Image**, **Button**. These blocks are nested in the **Slide** block. This is an example of a nested block.

If you add a second **Slide** block to the **Slideshow** section, then the theme automatically adds a **Slideshow controls** block. This block displays buttons that visitors to your site can click to navigate from one slide to the another. You can customize the style of buttons or hide the controls, but you can't remove or delete the block. This is an example of a required block that displays conditionally.

### Theme block compatibility

To access theme blocks, your theme must have sections that support theme blocks. You can check whether your theme supports theme blocks in your theme's code. If there's a **blocks** directory in the sidebar of the liquid editor, then you're using a theme that supports theme blocks. You can also check your theme's documentation.

#### Steps:

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Next to the theme that you want to check, click the button, and then click **Edit Code**.
3. In the sidebar, search for the blocks folder.

## Customizing your theme templates with sections and blocks

When you open the theme editor, your store's home page loads by default. You can use the drop-down menu to select a different template, such as products, collections, pages, or blogs, or use the search bar in the template drop-down to search for a specific template. When you select a template, it loads into the theme editor, and any changes you make are previewed in the editor.

## Add a section

Add a new section to any page in your online store.

#### Steps:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to edit, and then click **Edit theme**.
3. Customize your home page, or click the **Home page** drop-down menu and then select the template that you want to add a section to.
4. In the sidebar, click **Add section**, and then take one of the following steps:

   * Select a section from the list.
   * Use the **Search sections** field to find a specific section, and then select it.
5. Customize your new section by taking any of the following steps:

   * Edit the settings and content of your new section.
   * Edit the settings and content of the default blocks that load with the section.
   * Click **Add block** to [add a new block](sections-and-blocks.md#add-block).
6. Optional: To rearrange the order of the sections on your page, hover on the section name and then click and drag the button.
7. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap the icon.
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to edit, and then tap **Edit theme**.
5. Customize your home page, or tap the **Home page** drop-down menu and then select the template that you want to add a section to.
6. Tap **Sections**, then tap **Add section**, and then take one of the following steps:

   * Select a section from the list, and then tap **Add**.
   * Tap the button to search for a specific section, select your section, and then tap **Add**.
7. Customize your new section by taking any of the following steps:

   * Edit the settings and content of your new section.
   * Edit the settings and content of the default blocks that load with the section.
   * Tap **Add block** to [add a new block](sections-and-blocks.md#add-block).
8. Optional: To rearrange the order of the sections on your page, tap and drag the section.
9. Tap **Save** or **✓**.

## Edit a section

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to edit, and then click **Edit theme**.
3. Edit a section on your home page, or click the **Home page** drop-down menu and then select the template that contains the section that you want to edit.
4. In the sidebar, click a section name to load the content into the preview window and access the settings and options that are available for you to edit.
5. Optional: Click individual blocks to edit the blocks within a section.
6. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap the icon.
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to edit, and then tap **Edit theme**.
5. Edit a section on your home page, or tap the **Home page** drop-down menu and then select the template that contains the section that you want to edit.
6. Tap **Sections**, and then tap a section name to load the content into the preview window and access the settings and options that are available for you to edit.
7. Optional: Tap individual blocks to edit the blocks within a section.
8. Tap **Save** or **✓**.

## Rearrange a section or block

You can change the order of sections on your page templates and rearrange blocks within those sections. Additionally, you can move compatible blocks between different sections. For example, if your homepage features two **Slideshow** sections, then you can drag a **Slide** block from one slideshow to the other.

You can't move a block to a different section if the block type is incompatible or if the section has already reached its maximum limit for blocks. If you try to move a section or block to an invalid location, then it will return to its original position.

You can also use the preview inspector to rearrange sections. Learn more about using the [preview inspector in the theme editor](../customizing-themes/theme-editor/preview-inspector.md).

#### Steps:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to edit, and then click **Edit theme**.
3. To edit a section or block on your home page, either select it directly or use the **Home page** drop-down menu to choose the specific template that contains the section or block you want to edit.
4. Click and hold the and then drag the block or section to a new location.
5. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap the icon.
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Next to the theme that you want to edit, tap **Edit theme**.
5. To edit a section or block on your home page, either select it directly or use the **Home page** drop-down menu to choose the specific template that contains the section or block you want to edit.
6. Tap **Sections** > **Edit**.
7. Tap and hold the and then drag the block or section to a new location.
8. Tap **Done**.
9. Tap **Save** or **✓**.

## Duplicate a section or block

You can duplicate a section or block to create an identical copy of that section or block.

After you duplicate a block, the new block is added to the same section. If you want to move the block to a new section or change the block order, then you can [rearrange the block](sections-and-blocks.md#rearrange). You can also [copy a block, and then paste it directly into a different section instead](sections-and-blocks.md#copy-paste-blocks).

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to edit, and then click **Edit theme**.
3. Duplicate a section or block on your home page, or click the **Home page** drop-down menu and then select the template that contains the section or block that you want to duplicate.
4. Right click the section or block that you want to duplicate, and then click **Duplicate**.
5. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap the icon.
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Next to the theme that you want to edit, tap **Edit theme**.
5. Duplicate a section or block on your home page, or tap the **Home page** drop-down menu and then select the template that contains the section or block that you want to duplicate.
6. Tap **Sections** > **Edit**.
7. Tap > **Duplicate**.
8. Tap **Save** or **✓**.

## Copy and paste blocks

If you want to use the same block in multiple sections, then you can easily copy it and paste it into a different section. You can also copy and paste a block within the same section, or you can choose to [duplicate the block](sections-and-blocks.md#duplicate-section) instead. A duplicated block will retain all the settings and content of the original block.

#### Steps:

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Next to the theme that you want to edit, click **Edit theme**.
3. To copy and paste a block on your home page, either select it directly or use the **Home page** drop-down menu to choose the specific template that contains the section or block you want to edit.
4. Right click the block that you want to duplicate and then click **Copy**.
5. In the same section, or a different section, right click in the section and then click **Paste**.
6. Click **Save**.

## Hide or delete a section or block

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to edit, and then click **Edit theme**.
3. Hide or delete a section or block on your home page, or click the **Home page** drop-down menu and then select the template that contains the section or block that you want to hide or delete.
4. Optional: To hide a section or block from your online store, hover on a section or block name, and then click the button.
5. Optional: To delete a section or block from your online store, hover on a section or block name, and then click the button.
6. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap the icon.
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to edit, and then tap **Edit theme**.
5. Hide or delete a section or block on your home page, or tap the **Home page** drop-down menu and then select the template that contains the section or block that you want to hide or delete.
6. Tap **Sections**, and then tap the section or block that you want to hide or delete.
7. Optional: To hide a section or block from your online store, tap > **Hide**.
8. Optional: To delete a section or block from your online store, tap > **Remove**.
9. Tap **Save** or **✓**.

## Renaming a section or block

By default, a section or block's title in the theme editor sidebar menu and settings details is set to the block or section type, such as "Collection" or "Text".

For blocks, if the block settings contains a text field, such as a heading or description, then that text is also appended to the title in the sidebar menu. If there is more than one text field, then the first text field that has content is appended. When you change the text in the text field, then the block title changes to include the updated text. A section or block name can't be blank.

For example, you add a **Multicolumn** section to your page template with **Column** blocks. The column block includes has a **Heading** setting with the default text `Column`, and a **Description** setting with the default text `Pair text with an image to focus on your chosen product, collection, or blog post.` both. The default section title is `Multicolumn`. The default **Column** block title is `Column - Column`. If you remove the text from the **Heading** section, then block title updates to `Column - Pair text with an imag...`

You can rename any section or block to a custom name from the section or block's settings in the theme editor sidebar menu.

#### Steps:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to edit, and then click **Edit theme**.
3. Click the section or block that you want to rename.
4. Update the title in either of the following ways:

* Click the title, and then edit or enter a new name.
* Click > **Rename**, and then enter a new name.

5. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap the icon.
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to edit, and then tap **Edit theme**.
5. Tap or swipe to open the section menu.
6. Tap the section or block that you want to rename to open the settings.
7. Tap > **Rename**, and then enter a new name.
8. Tap **Save** or **✓**.

## Working with blocks

Blocks are customizable modules that you use to add content to the sections in your templates. You can use blocks to add text, images, links, buttons, and more.

Shopify themes have sections and blocks that you can customize. Some sections have fixed block types, which means that you can choose only from the blocks that are made available to that section by the theme designer.

Other sections allow you to select any block, but there's a limit on the total number of blocks that you can add to the section. If your section reaches the maximum number of blocks available, then the **Add block** option is greyed out and you can't click or tap it.

You can use the search to find a specific block by name, or select a block from the block picker drop-down menu. Your theme's blocks might be sorted into categories in the block picker, such as **Collection** for blocks with a collection picker, or **Media** for image and video blocks.

A preview of the block displays in the block picker so that you can review the block's display before you add it.

## Add a block

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to edit, and then click **Edit theme**.
3. You can add a block to a section on your home page, or click the **Home page** drop-down menu and then select the template that you want to add a block to.
4. Hover over the section that you want to add a block to, click **Add block**, and then take one of the following steps:

   * Select a block from the list.
   * Use the **Search blocks** field to find a specific block, and then select it.
5. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap the icon.
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to edit, and then tap **Edit theme**.
5. You can add a block to a section on your home page, or tap the **Home page** drop-down menu and then select the template that you want to add a block to.
6. Tap **Sections**, then tap **Block** for the section that you want to add a block to, and then take one of the following steps:

   * Select a block from the list.
   * Tap the button to search for a specific block, and then select your block.
7. Tap **Save** or **✓**.

## Use metafields and metaobjects with dynamic sources

You can use [metafields](https://help.shopify.com/en/manual/custom-data/metafields) and [metaobjects](https://help.shopify.com/en/manual/custom-data/metaobjects) to display dynamic information on your online store. If you have a theme that supports metafields, then you can connect a metafield to a compatible section or block settings in the theme editor.

For example, if you sell candles, then you might want to display burn times for each candle available on your store. After you set up a product metafield for `Burn time` in the **Custom data** section of your Shopify admin settings, you can add a text block to your product template's main section. In the text block, you can click the button on the text setting and select the **Burn time** metafield. Burn time information will now display on your products.

If you have a Shopify theme, then you can connect most metafields and metaobjects to your theme by using the theme editor. If you're using other themes, or if you want to add custom data types that your theme doesn't support, then you can [edit your theme code](../customizing-themes/edit-code/edit-theme-code.md#edit-your-theme-code) or hire a Shopify Partner to help you.
Learn more about [hiring a Shopify Partner](https://help.shopify.com/en/manual/partner-directory).

Not all sections or blocks support dynamic sources. Check your [theme's architecture version](../managing-themes/versions.md) and available customization options in [the theme editor](../customizing-themes/theme-editor/features-overview.md) to determine whether your theme supports dynamic sources.

You can display dynamic information in your online store by adding sections or blocks that can use dynamic sources. Dynamic sources can be used in any template, section, or block that displays compatible resources (product, collection, page, blog and blog post). You need to [add your metafield](https://help.shopify.com/en/manual/custom-data/metafields) before you can connect it in your templates. Refer to [*Dynamic sources*](https://shopify.dev/themes/architecture/settings#dynamic-sources) for more information about using metafields and metaobjects with dynamic sources in your theme.

After you complete the setup process, follow the steps below to connect dynamic sources to sections or blocks in your theme, using the button.

#### Steps:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to edit, and then click **Edit theme**.
3. Edit a section or block on your home page, or click the **Home page** drop-down menu and then select the template that contains the section or block that you want to edit.
4. In the sidebar, click a section or block name to load the content into the preview window and access the settings and options that are available for you to edit.
5. Click the button for the relevant content type that you want to edit, and then [connect your dynamic source](sections-and-blocks.md#dynamic-source-selector).
6. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap the icon.
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to edit, and then tap **Edit theme**.
5. Edit a section or block on your home page, or tap the **Home page** drop-down menu and then select the template that contains the section or block that you want to edit.
6. Tap **Sections**, and then tap a section or block name to load the content into the preview window and access the settings and options that are available for you to edit.
7. Tap the button for the relevant content type that you want to edit, and then [connect your dynamic source](sections-and-blocks.md#dynamic-source-selector).
8. Tap **Save** or **✓**.

Learn more about [displaying metafields on your online store](https://help.shopify.com/en/manual/custom-data/metafields/displaying-metafields-on-your-online-store) and [displaying metaobjects on your online store](https://help.shopify.com/en/manual/custom-data/metaobjects/connecting-to-your-online-store).

### Dynamic source selector

You can use the dynamic source selector to connect the correct dynamic source directly in the theme editor. Review the following key features of the dynamic source selector:

* You can reference dynamic sources from various resources, where applicable. For instance, if you connect a setting to a block that is connected to both a product resource and a page resource, then you can use the drop-down menu in the dynamic source selector to specify whether you want to search for metafields associated with either the product or the page resource.
* The dynamic source selector has a search and filter functionality to help you find the metafield that you need.
* The dynamic source selector lets you choose [category metafields](https://help.shopify.com/en/manual/custom-data/metafields/category-metafields). These are additional attributes that become available when you assign a [product category](https://help.shopify.com/en/manual/products/details/product-category) to a product. Accessing these metafields allows you to connect dynamic sources to any relevant fields on the underlying attribute metaobject.
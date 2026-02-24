# Templates

Source: https://help.shopify.com/en/manual/online-store/themes/theme-structure/templates

---

# Templates

Templates are a group of [sections](sections-and-blocks.md) that are configured to give your online store a consistent design and feel. The sections that are available in your templates depends on your [theme](../../themes.md). In the [theme editor](../customizing-themes/theme-editor.md), you can find which templates are applied to which pages, and then edit the templates to customize the information that you display to your customers.

Your theme contains templates for different types of content. These templates types contain sections and blocks that pull content dynamically from the respective area of your Shopify admin. For example, your theme's product page template creates a page for each product published to your online store in the **Products** section of your Shopify admin.

When you edit a template, your changes apply to every page that uses the template. For example, if you add a newsletter signup form to a collections template, then all your collection pages that use the default collections template display the newsletter signup form.

You can access all of your theme's templates from the page selector in the menu bar of the theme editor.

## On this page

* [Default templates](templates.md#default-templates)
* [Edit your templates](templates.md#edit-your-templates)
* [Considerations for creating a new template](templates.md#considerations-for-creating-a-new-template)
* [Create a new template](templates.md#create-a-new-template)
* [Previewing templates](templates.md#previewing-templates)
* [Apply a new template](templates.md#apply-a-new-template)
* [Applying a new template to products or collections in bulk](templates.md#bulk-template-changes)
* [Managing your templates](templates.md#managing-your-templates)

## Default templates

Each default template has its own default sections and settings that you can edit and customize in the [theme editor](../customizing-themes/theme-editor/features-overview.md). For example, product pages have a **Product information** section and a **Related products** section by default. The specific customization settings for each theme depend on your theme's developer and theme version. Learn more about finding your [theme version](../managing-themes/versions.md).

The templates are available in your theme by default.

### Products

Your theme's product pages display information about the [products](https://help.shopify.com/en/manual/products) that you sell on your store, and where your customers can buy the products from.

By default, product pages have a **Product information** section and a **Related products** section in the theme editor.

The **Product information** section displays the details of your products, such as the title, description, price, and images. You can manage your products from the [**Products**](https://admin.shopify.com/products) page of your Shopify admin.

### Collections

Your theme's collection pages display the [collections](https://help.shopify.com/en/manual/products/collections) that you create in the **Products** > [**Collections**](https://admin.shopify.com/collections) page of your Shopify admin. specific products together in categories. You can have [smart collections](https://help.shopify.com/en/manual/products/collections/collection-types#smart-collection) and [manual collections](https://help.shopify.com/en/manual/products/collections/collection-types#manual-collection).

By default, collection pages have a **Collection banner** section and a **Product grid** section in the theme editor.

### Collections list

The collections list page displays all your collections that are available on the Online Store sales channel. For example, if you have a jewelry store, then you can add a link to your collections list page in your menu for customers to browse by the jewelry type, such as rings or necklaces. You'll need to create collections for each category.

### Gift card

When you create a [gift card](https://help.shopify.com/en/manual/products/gift-card-products), or a customer orders a gift card product, the details of that gift card are included on the gift card page, such as the gift card value or balance and redemption code.

The gift card page is part of your theme. You can [customize your theme](../customizing-themes.md) to add or adjust the style and information that's included on the gift card page.

The value of the gift card and the gift card redemption code can't be customized.

### Pages

You can make custom [pages](../../add-edit-pages.md) in your Shopify admin to create content for your customers, such as an [About Us page](../customizing-themes/common-customizations/about-us.md), or for extra information about your products.

### Cart page

The cart page on your online store is where your customers can review the items that they've added to their cart.

By default, the cart page has an **Items** section and a **Subtotal** section in the theme editor.

### Blogs

Blog pages on your online store are the homepage for any [blogs](../../blogs/adding-a-blog.md) that you create in your Shopify admin and contain all of the published blog posts in that blog.

By default, blog pages contain a **Blog posts** section in the theme editor.

### Blog posts

Blog post pages on your online store display the content of [blog posts](../../blogs/writing-blogs.md) that you create in the **Content** > [**Blog posts**](https://admin.shopify.com/content/articles) page of your Shopify admin. By default, blog post pages contain a **Blog post** section in the theme editor.

### Search page

The search page is where customers can search for and find specific products, pages, or blog posts within your online store.

By default, the search page contains a **Search results** section in the theme editor.

As well as the **Search results** section settings, you can also view and customize some of the [**Theme Settings** for search behavior](../customizing-themes/theme-editor/theme-settings.md#search-behavior), and you can add your own [section-specific **Custom CSS**](../customizing-themes/edit-code/add-css.md#custom-css).

### Password page

You can set your store to be password protected in the **Online Store** > [**Preferences**](https://admin.shopify.com/online_store/preferences) page of your Shopify admin. If your store is password protected, then the [password page](../password-page.md) displays to visitors of your online store. The password page template has a unique header and footer. You can customize the password page template from the theme editor.

### 404 page

The 404 page displays when a customer tries to visit a link to your site that doesn't exist, such as a product page for a product that you deleted from your store.

This page has no customizable settings, but you can add your own [section-specific **Custom CSS**](../customizing-themes/edit-code/add-css.md#custom-css) to your 404 page in the theme editor.

## Edit your templates

You can edit your templates to add sections to your online store. Some sections contain blocks that can be further customized, but not every [section or block](sections-and-blocks.md) has settings or content that can be edited. When you edit your templates, your changes display in real time in the theme editor preview.

#### Steps:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to edit, and then click **Edit theme**.
3. Click the **Home page** drop-down menu, and then select the template that you want to edit.
4. To add a new section to the template, click **Add section**, and then select a new section for your template.
5. Optional: To add a block to your new section, click **Add block**, and then select a new block for your section.
6. Click the new section and blocks to view their settings and options, and then make your changes.
7. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap
   .
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to edit, and then tap **Edit theme**.
5. Tap the **Home page** drop-down menu, and then select the template that you want to edit.
6. To add a new section to the template, tap **Sections** > **Add section**, select a new section for your template, and then tap **Add**.
7. Optional: To add a block to your new section, tap **Add block**, and then select a new block for your section.
8. Tap the new section and blocks to view their settings and options, and then make your changes.
9. Tap **Save** or **✓**.

## Considerations for creating a new template

Before you [create a new template](templates.md#create-a-new-template), review the following considerations:

* You can have multiple templates for your products, collections, pages, blogs, and blog posts, but you can have only 1,000 templates in total.
* You can create a new template only with a [compatible theme](../managing-themes/versions.md#features).
* All themes have a default template for collections, products, blogs, blog posts, and pages. These default templates are what your store's resources and content are displayed with, unless you create alternative templates.
* Any changes you make to a template impact all the pages that use that template. If you want to display some pages of a particular type differently, then you can create a new template based on one that already exists in your theme.
* When you create a new template from an existing template, your new template automatically populates with the same sections as your existing template. You can then remove, add, or hide sections, and edit their content as needed, without impacting the display of pages that use the existing template.

## Create a new template

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to edit, and then click **Edit theme**.
3. Click the **Home page** drop-down menu, select a template type, and then click **Create template**.
4. In the **Create a template** dialog, do the following:

   * In the **Name** field, enter a unique name for your new template.
   * In the **Based on** drop-down menu, select the existing template that you want to base your new template on.
5. Click **Create template**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap
   .
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to edit, and then tap **Edit theme**.
5. Tap the **Home page** drop-down menu, select a template type, and then tap **Create template**.
6. In the **Create a template** dialog, do the following:
   * In the **Name** field, enter a unique name for your new template.
   * In the **Based on** drop-down menu, select the existing template that you want to base your new template on.
7. Tap **Create template**.

After you create a new template, you can [apply the template](templates.md#apply-a-new-template) to an online store page that you want to use it for.

### Create a template for metaobjects

You can create a template for a web page for metaobjects. To use this feature, complete the following steps:

1. [Create a metaobject definition](https://help.shopify.com/en/manual/custom-data/metaobjects/building-a-metaobject) with [Storefront access](https://help.shopify.com/en/manual/custom-data/options) and, optionally, [activate the Web pages feature manually](https://help.shopify.com/en/manual/custom-data/metaobjects/connecting-to-your-online-store/webpages#activate-web-pages). When you create a theme template, the theme editor activates the Web pages feature.
2. [Create entries for the metaobject definition](https://help.shopify.com/en/manual/custom-data/metaobjects/creating-entries).

You can now [create a metaobject template in the theme editor](https://help.shopify.com/en/manual/custom-data/metaobjects/connecting-to-your-online-store/webpages#create-theme-template).

## Previewing templates

You can use template previews to preview how your online store resources, such as products and pages, display to your customers with a different template applied.

Templates are assigned on a product, collection, page, blog, or blog post level. You [create](templates.md#create-a-new-template) and [edit](templates.md#edit-your-templates) templates in the theme editor, but you [change a resource's assigned template](templates.md#apply-a-new-template) in your Shopify admin.

### Considerations for previewing templates

Consider the following details when previewing templates for your different online store resources:

* When you preview a products template in the theme editor, you can use products that have **Active** status or **Draft** status, but you can't preview a product that has **Archived** status.
* When you preview a collections template in the theme editor, you need to ensure that the collection has [**Online Store** activated as a sales channels](https://help.shopify.com/en/manual/products/collections/make-collections-available#change-the-availability). If a collection doesn't have **Online Store** activated as a sales channel, then you can't preview that collection with any collections templates in the theme editor.
* When you preview a pages template in the theme editor, you can use pages that have their visibility set as either **Visible** or **Hidden**.
* When you preview a blog posts template in the theme editor, you can use blog posts that have their visibility set as either **Visible** or **Hidden**.

Blogs don't have any different status or visibility parameters, so you can use a blogs template to preview any published blogs that you have in your online store.

### Preview an alternate template

You can preview how your products, collections, pages, blogs, or blog posts display with a different template applied.

#### Steps:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to preview a template with, and then click **Edit theme**.
3. Click the **Home page** drop-down menu, and then select the template that you want to use.
4. In the **Preview** section in the theme editor sidebar, click **Change**.
5. Click the resource that you want to preview with the selected template.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap the  icon.
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to preview a template with, and then tap **Edit theme**.
5. Tap the **Home page** drop-down menu, and then select the template that you want to use.
6. To select a resource to preview with the template, tap the drop-down menu again.
7. In the **Search online store** field, enter the name of the resource that you want to preview with the selected template.
8. Select your resource from the search results list.

### Previewing specific resources

You can preview how your template displays with any compatible resource in your store. For example, if you're viewing a product template, then you can test it with any product in your store.

You still need to assign the template to the resource in the Shopify Admin.

You can also search for templates and resources using the **Search** bar in the page selector, in the **Add section** or **Add block** tool, or in **App embeds**.

#### Steps:

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Next to the theme that you want to edit, click **Edit theme**.
3. From the template menu, select the template that you want to preview.
4. From the sidebar menu, in the **Preview** section, click **Change**.
5. From the **Select** menu, select the resource you want to preview.

## Apply a new template

You can change an assigned template for the following sections in a published theme:

* pages
* products
* collections
* blogs
* blog posts

You change an assigned template in your Shopify admin. The template options that display are based on the available templates only in your current live theme.

Templates for products and collections can be assigned on an individual item level, or to multiple items at the same time using the [Bulk editor](templates.md#bulk-template-changes).

### Apply a new template to a page

Desktop

1. From your Shopify admin, go to **Online Store** > [**Pages**](https://admin.shopify.com/pages).
2. Click the page that you want to apply a new template to.
3. In the **Online store** section, click the **Theme template** drop-down menu, and then select the template that you want to apply to your page.
4. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap
   .
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Pages**.
4. Tap the page that you want to apply a new template to.
5. In the **Online store** section, tap the **Theme template** drop-down menu, and then select the template that you want to apply to your page.
6. Tap **Save** or **✓**.

### Apply a new template to a product

Desktop

1. From your Shopify admin, go to [**Products**](https://admin.shopify.com/products).
2. Click a product that you want to apply a new template to.
3. In the **Theme template** section, click the drop-down menu and then select the template that you want to apply to your product.
4. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap the  icon
   .
2. Tap a product that you want to apply a new template to.
3. Tap **Online Store template**.
4. Select the template that you want to apply to your product.
5. Tap **Save** or **✓**.

### Apply a new template to a collection

1. From your Shopify admin, go to **Products** > [**Collections**](https://admin.shopify.com/collections).
2. Click a collection that you want to apply a template to.
3. In the **Theme template** section, click the drop-down menu and then select the template that you want to apply to your collection.
4. Click **Save**.

### Apply a new template to a blog

Desktop

1. From your Shopify admin, go to **Content** > [**Blog posts**](https://admin.shopify.com/articles).
2. Click **Manage blogs**.
3. Click a blog that you want to apply a template to.
4. In the **Online store** section, click the **Theme template** drop-down menu, and then select the template that you want to apply to your blog.
5. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap
   .
2. In the **Content** menu, tap the  icon, and then tap **Blog posts**.
3. Tap  or  > **Manage blogs**.
4. Tap a blog that you want to apply a template to.
5. In the **Online store** section, tap the **Theme template** drop-down menu, and then select the template that you want to apply to your blog.
6. Tap **Save** or **✓**.

### Apply a new template to a blog post

Desktop

1. From your Shopify admin, go to **Content** > [**Blog posts**](https://admin.shopify.com/content/articles).
2. Click a blog post that you want to apply a template to.
3. In the **Online store** section, click the **Theme template** drop-down menu, and then select the template that you want to apply to your blog.
4. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap
   .
2. In the **Content** menu, tap the  icon, and then tap **Blog posts**.
3. Tap a blog post that you want to apply a template to.
4. In the **Online store** section, tap the **Theme template** drop-down menu, and then select the template that you want to apply to your blog post.
5. Tap **Save** or **✓**.

## Applying a new template to products or collections in bulk

You can use the [Bulk editor](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/bulk-editing) to apply a new template to multiple products or collections in bulk.

### Apply a new template to products in bulk

1. From your Shopify admin, go to [**Products**](https://admin.shopify.com/products).
2. To edit multiple products at the same time, do one of the following:

   * To select products one by one, select the checkbox for each product.
   * To select a range of products, click to select a product, and then hold the shift key and click another product. This selects the first and last products that you clicked, and all products in between.
   * To select all products on a page, select the checkbox at the top of the product list.
   * To select all products from your store, select the checkbox at the top of the products list, and then click **Select all in this store**.
3. Click **Bulk edit**.
4. In the Bulk editor, click the **Columns** drop-down menu, and then in the **General** section, select **Template**.
5. Click the first field of the **Template** column, then hold the shift key, and then click the last field of the **Template** column. A blue shading displays around the items that you selected.
6. Click the first field that you selected, then select the template that you want from the drop-down menu, and then click **Save**.

### Apply a new template to collections in bulk

1. From your Shopify admin, go to **Products** > [**Collections**](https://admin.shopify.com/collections).
2. To edit multiple collections at the same time, do one of the following:

   * To select collections one by one, select the checkbox for each collection.
   * To select a range of collections, click to select a collection, and then hold the shift key and click another collection. This selects the first and last collections that you clicked, and all collections in between.
   * To select all collections on a page, select the checkbox at the top of the collections list.
   * To select all collections from your store, select the checkbox at the top of the collection list, and then click **Select all in this store**.
3. Click **Bulk edit**.
4. In the Bulk editor, click the **Columns** drop-down menu, and then in the **General** section, select **Template**.
5. Click the first field of the **Template** column, then hold the shift key, and then click the last field of the **Template** column. A blue shading displays around the items that you selected.
6. Click the first field that you selected, then select the template that you want from the drop-down menu, and then click **Save**.

## Managing your templates

To rename or delete a template, you need to use the [code editor](../customizing-themes/edit-code/edit-theme-code.md#edit-your-theme-code). Editing a template file might cause issues with your online store.

When you delete a template, any online store resources that had the template assigned to them are displayed with the default template until you assign a different one.

### Rename a template

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme with the template that you want to rename, and then click **…** > **Edit code**.
3. In the code editor, find the **templates** folder.
4. Right-click on the template file that you want to rename, and then select **Rename...** from the drop-down menu.
5. Enter a new name for the file.
6. Press `Enter` on your keyboard.

### Delete a template

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme you want to delete a template from, and then click **…** > **Edit code**.
3. In the code editor, find the **templates** folder.
4. Right-click on the template file that you want to delete, and then select **Delete permanently** from the drop-down menu.
5. Click **Delete**.
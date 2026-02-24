# Hide the Add to cart button on product pages

Source: https://help.shopify.com/en/manual/online-store/themes/customizing-themes/common-customizations/hide-add-to-cart-buttons

---

# Hide the Add to cart button on product pages

/manual/online-store/themes/theme-structure/templates

You can hide the option for customers to add products to their cart by customizing a product [template](../../theme-structure/templates.md) that [hides specific blocks](../../theme-structure/sections-and-blocks.md#remove-section-or-block) related to adding items to the cart. You can then assign that product template to one or more products that you don't want customers to be able to add to their cart. This means that the Add to cart button isn't displayed on the product pages that you assign your new product template to.

You might want to hide the Add to cart button from certain product pages in one of the following scenarios:

* You need customers to contact you for a quote on a product price.
* You need to have a pre-order option instead of the Add to cart button.
* You sell custom made-to-order products, and you need customers to contact you about their product requirements before making a purchase.

You can only assign product templates that are associated with your published theme to your product pages. If you create a new template in a theme that isn't the published theme, then you must first [publish the theme](../../managing-themes/publishing-themes.md) in order to assign its templates to your products.

Learn more about [creating new templates](../../theme-structure/templates.md#create-a-new-template) and [applying templates](../../theme-structure/templates.md#apply-a-new-template) to products.

## On this page

* [Hide the Add to cart button for specific products](hide-add-to-cart-buttons.md#hide-the-add-to-cart-button-for-specific-products)
* [Hide the Add to cart button for all products](hide-add-to-cart-buttons.md#hide-the-add-to-cart-button-for-all-products)

## Hide the Add to cart button for specific products

By default, products are assigned the **Default product** template. You can create a separate `not-for-sale` product template to hide the Add to cart button for one or more products, but leave other products still available for purchase on your online store.

### Create a not-for-sale product template

To customize specific products without making changes to the **Default product** template, you need to create a new product template.

#### Steps:

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to edit, and then click **Edit theme**.
3. Click the **Home page** drop-down menu, and then click **Products** > **⊕ Create template**.
4. In the **Create a template** dialog, enter a name for your new template into the **Name** field, such as `not-for-sale`, and then click **Create template**.
5. In the Sections navigation sidebar, go to the **Template** > **Product information** blocks, and then make the following changes:

   1. Hover your cursor over the **Quantity selector** block, and then click the eye icon to hide the block.
   2. Hover your cursor over the **Buy buttons** block, and then click the eye icon to hide the block.
   3. Optional: Hover your cursor over the **Price** block, and then click the eye icon to hide the block.
6. Optional: If you want to add some text on your product page to give your customers more information, such as a date when sales are expected to resume if the product is unavailable, then you can add and customize a new block with the following steps:

   1. In the **Product information** section, click **⊕ Add block** > **Text** to add a text block.
   2. Click and drag the new **Text block** to your preferred position on the product page.
   3. In the **Text** settings sidebar, add your text into the **Text** field.
   4. Select your preferred **Text style**.
7. Optional: If you want to add a contact form, then you can add and customize a new section on your product page with the following steps:

   1. In the **Template** panel, click **⊕ Add section** > **Contact Form**.
   2. Click and drag the new **Contact Form** section to your preferred position on the product page.
   3. In the **Contact Form** settings sidebar, you can customize your contact form as desired. For example, you can edit the **Heading** text field to display a call to action, such as `Send us a request to be added to our waitlist`.
8. Click **Save**.

### Assign the not-for-sale template to a single product

1. From your Shopify admin, go to [**Products**](https://admin.shopify.com/products).
2. Click the name of the product that you want to hide the Add to cart button on.
3. In the **Theme template** section, click the drop-down menu, and then select the `not-for-sale` template.
4. Click **Save**.

### Assign the not-for-sale template to multiple products in bulk

1. From your Shopify admin, go to [**Products**](https://admin.shopify.com/products).
2. Click the checkboxes next to the products that you want to hide the Add to cart button on, and then click **Bulk edit**.
3. In the [bulk editor](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/bulk-editing), click **Columns**, and then click **Template** to add the Template column to the editor table.
4. In each product row, set the **Template** to be `product.not-for-sale`.
5. Click **Save**.

## Hide the Add to cart button for all products

If you want to hide the Add to cart button for all your products but still allow customers to browse your online store, then you can customize the **Default product** template to apply changes to all existing and future products.

#### Steps:

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to edit, and then click **Edit theme**.
3. Click the **Home page** drop-down menu, and then click **Products** > **Default product**.
4. In the Sections navigation sidebar, go to the **Template** > **Product information** blocks, and then make the following changes:

   1. Hover your cursor over the **Quantity selector** block, and then click the eye icon to hide the block.
   2. Hover your cursor over the **Buy buttons** block, and then click the eye icon to hide the block.
   3. Optional: Hover your cursor over the **Price** block, and then click the eye icon to hide the block.
5. Optional: If you want to add some text on your product pages to give your customers more information, such as a date when sales are expected to resume if your products are unavailable, then you can add and customize a new block with the following steps:

   1. In the **Product information** section, click **⊕ Add block** > **Text** to add a text block.
   2. Click and drag the new **Text block** to your preferred position on the product page.
   3. In the **Text** settings sidebar, add your text into the **Text** field.
   4. Select your preferred **Text style**.
6. Optional: If you want to add a contact form, then you can add and customize a new section on your product pages with the following steps:

   1. In the **Template** panel, click **⊕ Add section** > **Contact Form**.
   2. Click and drag the new **Contact Form** section to your preferred position on the product page.
   3. In the **Contact Form** settings sidebar, you can customize the contact form as desired. For example, you can edit the **Heading** text field to display a call to action, such as `Send us a request to be added to our waitlist`.
7. Click **Save**.
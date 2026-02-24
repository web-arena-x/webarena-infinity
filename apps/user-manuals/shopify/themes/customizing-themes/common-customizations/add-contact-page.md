# Add a Contact Us page to your store

Source: https://help.shopify.com/en/manual/online-store/themes/customizing-themes/common-customizations/add-contact-page

---

# Add a Contact Us page to your store

You can add a contact page to your online store to help customers contact you with questions about your products, policies, or their orders. All Shopify themes have a built-in contact form that you can apply to the pages that you create.

## On this page

* [Create a contact page](add-contact-page.md#create-a-contact-page)
* [Customize your contact page](add-contact-page.md#customize-your-contact-page)
* [View contact form submissions](add-contact-page.md#view-contact-form-submissions)
* [Spam filtering](add-contact-page.md#spam-filtering)

## Create a contact page

You add a contact form by creating a new page with the `page.contact` template. If you want to display information above the contact form, such as response timelines or information about your brand, then use the rich text editor to add text, images or videos.

You might also want to include the following information in the **Content** box:

* A short message, such as "We'll get back to you as soon as we can"
* Your store's address, with an image of your physical storefront, if you have a retail location
* Your phone number, if you want customers to be able to reach you by phone

If you create a contact page without adding any other content, then only the contact form is displayed to customers.

#### Steps:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Pages**](https://admin.shopify.com/pages).
2. Click **Add page**.
3. In the **Title** box, type a title for your contact page, such as `Contact us` or `Get in touch`.
4. In the **Content** box, use the rich text editor to add any text, images or videos that you want to display above the contact form. You can leave this section blank.
5. In the **Online store** section, select `contact` from the **Theme template** drop-down menu.
6. Click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap .
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Pages**.
4. Tap **Add page**.
5. In the **Title** box, type a title for your contact page, such as `Contact us` or `Get in touch`.
6. In the **Content** box, use the rich text editor to add any text, images or videos that you want to display above the contact form. You can leave this section blank.
7. In the **Online store** section, select `contact` from the **Theme template** drop-down menu.
8. Tap **Save**.

After you create the contact page, you need to [add your contact page to your menu](../../../menus-and-links/editing-menus.md#add-menu-item) to display it on your online store.

## Customize your contact page

The contact page is a [template](../../theme-structure/templates.md) that you can customize in the [theme editor](../../customizing-themes.md). You can add sections to your contact page template to include additional information, for example, featured collections, blog posts, or images.

#### Steps:

Desktop

1. From your Shopify admin, go to **Online Store** > [**Themes**](https://admin.shopify.com/themes).
2. Find the theme that you want to edit, and then click **Edit theme**.
3. From the dropdown menu, click **Pages** > **Contact** to load the contact page template.
4. Click **+ Add section**, and then select a section to insert into your contact page.

* The settings and options for the section that you added will open in your sidebar.
* After you've edited your new section, click the back button to return to the template.
* Repeat the steps above to add additional sections to your contact page template.

5. Click and drag the `⋮⋮` icon to move sections up or down within your contact page.
6. When you're satisfied with the layout of your page, click **Save**.
Mobile

1. From the [Shopify app](https://www.shopify.com/install/detect), tap .
2. In the **Sales channels** section, tap **Online Store**.
3. Tap **Manage all themes**.
4. Find the theme that you want to edit, and then tap **Edit theme**.
5. Tap **Edit**.
6. From the dropdown menu, click **Pages** > **Contact** to load the contact page template.
7. Click **+ Add section**, and then select a section to insert into your contact page.

* The settings and options for the section that you added will open in your sidebar.
* After you've edited your new section, click the back button to return to the template.
* Repeat the steps above to add additional sections to your contact page template.

8. Click and drag the `⋮⋮` icon to move sections up or down within your contact page.
9. When you're satisfied with the layout of your page, click **Save**.

## View contact form submissions

Your contact form sends all submissions to your store's sender email address. You can change your sender email address on the [**Notifications**](https://admin.shopify.com/settings/notifications) settings page of your Shopify admin. If you have a third-party domain, then you might also need to [authenticate your domain](https://help.shopify.com/en/manual/intro-to-shopify/initial-setup/setup-your-email#authenticate).

If you don't want to use your store's **Sender email** address for your contact form, then you can use a free online service such as [Wufoo](https://www.wufoo.com) or [Jotform](https://www.jotform.com) to create a custom contact form that you can embed on your contact page.

## Spam filtering

The content of the `contact[body]` field of your contact form is analyzed by Shopify's spam filters. If the submission is flagged as spam, then the email is sent with a `[SPAM]` prefix in its subject. You can create an email filter to set aside emails with a subject that contains `[SPAM]`.

To make sure that you don't miss any legitimate messages that are flagged as spam by mistake, you receive all contact form submissions, including those flagged as spam.
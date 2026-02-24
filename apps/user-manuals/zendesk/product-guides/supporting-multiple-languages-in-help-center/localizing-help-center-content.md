# Localizing help center content

Source: https://support.zendesk.com/hc/en-us/articles/4408834328090-Localizing-help-center-content

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

If you've [configured your help center to support multiple languages](https://support.zendesk.com/hc/en-us/articles/4408827609882), you can add translated versions of each article in your help center, or add articles only in specific languages. The help center displays pages in different languages based on locale code in the page URL (for example, ".../hc/en-us"). Any translated article must also have parent pages (section and category), translated in the same language.

You can also display snippets of translated text on help center pages. For example, a welcome message on the home page or a company tag line in the header.

Content blocks can be used in translated articles, but do not have the same multi-language support as help center articles. See [Using content blocks in translated articles](https://support.zendesk.com/hc/en-us/articles/4486473049370).

You must be a Knowledge admin to add localized content to your help center.

Topics covered in this article:

- [Basic workflow for localizing your help center in multiple languages](#topic_lhh_znd_jk)
- [Adding translations to sections and categories to ensure translated articles display](#topic_3zx_52h_xw)
- [Adding translated articles](#topic_inn_3qy_43)
- [Adding translated text](#topic_wnw_fbg_yj)

## Basic workflow for localizing your help center in multiple languages

The following steps describe the general workflow to follow when localizing your help center content in multiple languages. If you're using AI article translation to generate your help center article translations, your workflow may vary. See [Translating articles in your help center using AI](https://support.zendesk.com/hc/en-us/articles/8717609637018).

**To localize your help center in multiple languages**

1. Configure your help center to support your other languages, if you have not already done so (see [Configuring your help center to support multiple languages](https://support.zendesk.com/hc/en-us/articles/4408827609882)).
2. Translate your articles into your supported languages. You can either do this outside of the help center, or if you have the [Copilot add-on](https://support.zendesk.com/hc/en-us/articles/5524125586330), you can use the [AI article translation tool](https://support.zendesk.com/hc/en-us/articles/9380474288154) to translate articles in your help center using AI.

   Note: To browse third party apps that can help you perform this task, see the [Zendesk Marketplace](https://www.zendesk.com/apps/).
3. Prepare your sections and categories by adding translated titles (see [Adding translations to sections and categories to ensure translated articles display](#topic_3zx_52h_xw) below).
4. Add the translated content to your help center (see [Adding translated articles](#topic_inn_3qy_43) below).
5. If needed, add translated text snippets (see [Adding translated text](#topic_wnw_fbg_yj) below).

   Many of the pre-built page elements used in your help center are already localized. For example, the element that lets users vote on an article displays "Was this article helpful?" in English and "Cet article vous a-t-il été utile?" in French. You don't need to localize the strings.
   For a list of available translated strings, see the [translation helper](https://developer.zendesk.com/apps/docs/help-center-templates/helpers#t-translation-helper) in the help center Templates docs.

It's a good idea to establish a localization process for ongoing additions and updates to your help center.

## Adding translations to sections and categories to ensure translated articles display

Any translated article must have a parent page translated in the same language. If you add a translation for an article that does not have a corresponding translation for the section or category, users will not be able to view the article in the help center (even though the article is published).

The page hierarchy is as follows: Category landing page > Section landing page >
Article. For example, if you add an article translated in German, the article must have a German section page. In turn, the German section page must have a German category page. The help center cannot display orphan articles.

When localizing your help center, it makes sense to start by adding localized versions of category pages, followed by section pages, followed by articles. This workflow guarantees that any new translated article has a parent page -- a section or category page -- that's translated in the same language so that users can view it.

You must be a Knowledge Admin to add section and category translations.

**To add a translated title for a section or category**

1. In [help center](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), navigate to an existing section or category.
2. Click **Edit section** or **Edit category** in the top menu bar.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_topmenu_editsection.png)
3. In the left sidebar, click the **Language** drop-down list, then select a language for the translation you want to add.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-edit-cat-lang-dropdown.png)

   If you do not see a drop-down menu of languages, then you first need to enable languages for your help center (see [Configuring your help center to support multiple languages](https://support.zendesk.com/hc/en-us/articles/4408827609882)).
4. Enter or paste the translated content for the name and (optionally), description.

   Keep in mind that any translated page must have a parent page translated in the same language. After you add the translation for the parent page, you can click Refresh and it will take up to three minutes before the change is registered.

   Note: You'll see a warning if you add a translation for a section that does not have a corresponding translation for the category. As a best practice to prevent these warnings, create the translated categories first, then go through and translate the sections.
5. Click **Update translation** to create the translated version of the page.
6. Repeat the steps to add more translated pages.

## Adding translated articles

Note: If you have the [Copilot add-on](https://support.zendesk.com/hc/en-us/articles/5524125586330), you can use AI article translation to translate articles and automatically add those translations to your help center. See [Translating articles in your help center using AI](https://support.zendesk.com/hc/en-us/articles/9380474288154).

You can add translated versions of existing articles or translated articles that don't have versions in other languages.

When you add translated versions of existing pages, the original article and its translated versions share the same URL except for the locale. This feature can simplify managing your content. For example, the following URLs point to the U.S. English and French versions of the same article:

`https://mondocam.zendesk.com/hc/en-us/articles/202529393`

`https://mondocam.zendesk.com/hc/fr/articles/202529393`

Users can also manually switch to a different language by selecting it from the language menu in your help center.

**To add a translated version of an existing article**

1. In [help center](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), navigate to the existing article, then click **Edit article** in the top menu bar.
2. Click the **Translation panel** icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/globe-icon.png)) on the collapsible panel.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Add-New-translation.png)
3. Click the **Add language icon** (+) to add a new language.
4. Select a language for the translation you want to add from the list.

   This list displays all languages that you've enabled across all brands in your account.

   ![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/guide-local-add-language.png)

   If you do not see a list of languages, then you first need to enable languages for your help center (see [Configuring your help center to support multiple languages](https://support.zendesk.com/hc/en-us/articles/4408827609882)).
5. Enter or paste the translated content into the draft article.

   Keep in mind that any translated page must have a parent page translated in the same language. You'll see a warning if you add a translation for an article that does not have a corresponding translation for the section or category. For example:

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_translations_missing.png)

   After you add the translation for the parent page, you can click Refresh and it will take up to three minutes before the change is registered.
6. When you are finished working on your article, do one of the following:
   - To save your new article as a draft or work in progress to publish later, click **Save**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-save-action-ftr.jpg)

     Click **Preview** to view the article in your help center.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-preview-button-newui.jpg)
   - When you're ready to publish your article, click the drop-down arrow on the **Save** button, then select **Publish**.

     To see how your published article looks in the help center, click **View**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-view-button-newui.jpg)
7. Repeat the steps to add more translated pages.

**To add a translated page with no version in another language**

1. Click **Add** in the top menu bar, then select the kind of page you want to add.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Add+article+translation.png)
2. Click the language displayed at the top of the page.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/Language+bar+select.png)
3. Select the language of the content from the list.

   This list displays all languages that you've enabled across all brands in your account.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-sel-default-lang-panel.png)
4. Enter or paste the content into the page.
5. When you are finished working on your article, do one of the following:
   - To save your new article as a draft or work in progress to publish later, click **Save**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-save-action-ftr.jpg)

     Click **Preview** to view the article in your help center.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-preview-button-newui.jpg)
   - When you're ready to publish your article, click the drop-down arrow on the **Save** button, then select **Publish**.

     To see how your published article looks in the help center, click **View**.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide-view-button-newui.jpg)

## Adding translated text

You can display snippets of translated text on help center pages. The translated variant of the text changes dynamically based on the user's language. The following are examples of where you can use translated text:

- A welcome message on the home page
- A company tag line in the header
- A legal notice in the footer
- Service alerts

Many of the pre-built page elements used in your help center are already localized. For example, the element that lets users vote on an article displays "Was this article helpful?" in English and "Cet article vous a-t-il été utile?" in French. You don't need to localize the strings. For a list of available translated strings, see the [translation helper](https://developer.zendesk.com/apps/docs/help-center-templates/helpers#t-translation-helper) in the help center Templates docs.

The workflow for adding snippets of translated text to your help center consists of the following steps:

1. [Specifying the language variants of the text in the Admin Center](#topic_zmx_5zd_jk)
2. [Inserting the dynamic content in a template in Guide](#topic_xws_vzd_jk)

This functionality uses the dynamic content feature in the Admin Center. This feature is not meant to be used to localize articles, titles, and other help center template elements that support multiple languages. See [Adding translated pages](#topic_inn_3qy_43) above and the [translation helper](https://developer.zendesk.com/apps/docs/help-center-templates/helpers#t-translation-helper) docs in help center Templates for more information.

### Specifying the language variants of the text in the Admin Center

You specify the language variants of a snippet of text in the Admin Center. For instructions, see [Providing multiple language support with dynamic content](https://support.zendesk.com/hc/en-us/articles/4408882999066). Example:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_dc_item.png)

Add the content in the same language variants as the languages you support on your help center. If you don't specify a variant for a language, nothing will be displayed in that language in the help center. For example, suppose your help center supports English and French for a Canadian website. Add English and French variants of each snippet of text.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/hc_dc_variants.png)

Make a note of the item name. You'll need it for the following step. In the previous example, the placeholder is `{{dc 'welcome_message'}}`, so the item name is "welcome\_message".

### Inserting the dynamic content in a help center template

Insert your text variants in help center templates with the [dynamic content helper](https://developer.zendesk.com/apps/docs/help-center-templates/helpers#dc-dynamic-content-helper). When the page is requested by a web browser, the template helper inserts the appropriate text variant.

Note: Do not include Curlybars in your dynamic content. Curlybar expressions placed inside dynamic content will not render correctly in the help center, but will instead appear as text.

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. Click the theme you want to edit to open it.
3. Click **Edit Code**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/theming_menu_option_edit_code.png)
4. In the **Templates** section, click the template you want to modify.

   The page opens in the code editor.
5. Add the dynamic content in your template using the [dynamic content helper](https://developer.zendesk.com/apps/docs/help-center-templates/helpers#dc-dynamic-content-helper). Example:

   ```
   {{dc 'welcome_message'}}
   ```

   If the dynamic content is missing a variant, then the default variant will be used when that locale is viewed in the help center. However, Knowledge admins, will see an error message for dynamic content that does not have a variant for the current locale when they edit the help center theme.
6. To save your changes, click **Save** at the top of the sidebar.

For more information on working with templates, see [Working with the page code](https://support.zendesk.com/hc/en-us/articles/4408839332250#topic_r5r_xlw_n3).
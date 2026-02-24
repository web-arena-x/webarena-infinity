# Configuring your help center to support multiple languages

Source: https://support.zendesk.com/hc/en-us/articles/4408827609882-Configuring-your-help-center-to-support-multiple-languages

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

Verified AI summary ◀▼

Configure your help center to support multiple languages by enabling desired languages and adding translated content. Users can select their preferred language, enhancing accessibility and user experience. Manage language settings independently from other support languages, and easily update or remove languages as needed. Ensure your knowledge base delivers content in supported languages to provide a comprehensive multilingual experience.

If you are not on a Suite plan, you must have Guide Professional or Enterprise *and* Support Professional or Enterprise for multi-language support.

You must enable all of the languages that you want to support in your help center.
For each language you enable, you can add a translated help center name as well as translated snippets of text. Your help center languages are independent of any languages you have [enabled in Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408888770714).

After you enable languages for your help center, you can [add localized help center content](https://support.zendesk.com/hc/en-us/articles/4408834328090)) so that end users can choose the language they want in your help center.

You must be a Knowledge admin to configure help center languages.

This article covers the following topics:

- [Enabling languages for your help center](#topic_ys2_kxh_tz)
- [Understanding how translated content is displayed in your help center](#trans_content)
- [Removing a help center language](#topic_d51_tjy_vgb)
- [Changing a translated help center name](#topic_ud5_kxh_tz)

Related article:

- [Configuring the default language for your help center](https://support.zendesk.com/hc/en-us/articles/4408822162330)

## Enabling languages for your help center

You can enable any help center languages you plan to support.

You can choose from any of the [help center supported languages](https://support.zendesk.com/hc/en-us/articles/4408821324826#Default_languages)
and most of the [languages that are available by request](https://support.zendesk.com/hc/en-us/articles/4408821324826#HC). If you choose a supported language, text that appears in the help center by default (for example, "search" and "comments"), is displayed in that language. If you choose a language that is not supported, default text appears in that language only if there are crowd-sourced translations.

Note: If you are not planning to translate all your articles into a chosen language, make sure your content will be displayed correctly to all users, see [Understanding how translated content is displayed in your help center](#trans_content).

You need to set up your knowledge base to [deliver content in your supported languages](https://support.zendesk.com/hc/en-us/articles/4408834328090)
for your enabled languages.

Your help center languages are enabled independently of any languages you have [enabled in Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408888770714). If you enable a language for your help center that is *not* enabled in Support, when that language is selected in your help center, the "Submit a request" form will appear in the [Support account default language](https://support.zendesk.com/hc/en-us/articles/4408887059866#topic_rtc_42j_1y).

**To enable a language in your help center**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_settings.png)) in the sidebar.
2. Select **Language settings**, then click **Add new language**.

   You can scroll or search the list. You can choose from any of the [help center supported languages](https://support.zendesk.com/hc/en-us/articles/4408821324826#Default_languages) and most of the [languages that are available by request](https://support.zendesk.com/hc/en-us/articles/4408821324826#HC), some of which have crowd-sourced translations.
3. Click the **Language** drop-down to select a language, then enter a **Help Center name** for the language.

   The help center name might be the translated name of your default help center name.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/language_add_new.png)
4. Click **Add language**.
5. Click **Add new language** again if you want to add more languages.

   A list of all your enabled languages appears on the help center **Language** page. If you've enabled multiple languages, the Help Center name should be the name of the search source.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/languages_list.png)
6. Click **Save** on the help center **Language** page when you are finished.

   Next, you need to set up your knowledge base to [deliver content in your supported languages](https://support.zendesk.com/hc/en-us/articles/4408834328090), if you haven't already done so.

## Understanding how translated content is displayed in your help center

The difference between having a language enabled and having translated content available for that language has implications on what a user sees in a help center. For example, the default language for a help center might be set to US English (en-us). The help center might also provide translated content in French (fr).

The language that a user sees in your help center is based on defaulting to the following, in order of preference:

- The language specified in the URL of the page the user is currently on (if present)
- The language set for the user's current active session
- The language preference set in the user's user profile
- The preferred language of the user's browser
- Other compatible languages specified by the user's browser

If the help center is unable to match any of these languages, then the user is directed to the [default language of your help center](https://support.zendesk.com/hc/en-us/articles/4408822162330).

These examples explain some different scenarios.

- **Scenario 1** - The user's browser language is a language that is not enabled in the help center. The user sees the article in the default language.

 That is, a user with Polish (pl) set as their default browser language accesses this link: <https://support.zendesk.com/hc/pl>. The site is not translated into Polish so they are redirected to the default language site ([support.zendesk.com/hc/en-us](https://support.zendesk.com/hc/en-us)), and will see the content in English.
- **Scenario 2** - The user's browser language is a language that is enabled in the help center, and there is translated content in that language available for that article. The user automatically sees the translated content.

 That is, if a user's default browser language is French, they see all articles that have been translated into French, even if the user has not specified the locale (fr) in the URL. If they access the link <https://support.zendesk.com/hc>, they are automatically redirected to <https://support.zendesk.com/hc/fr>.
- **Scenario 3** - The user's browser language is a language that is enabled in the help center, but there is no translated content in that language available for that article. The article will not show up in the browser language's version of the help center. If the user tries to navigate manually to that article, in a language that it has not been translated into, then the user sees a page error, or is redirected to the home page for that language.

 For example, a user with French set as their default browser language sees all articles that have been translated into French, but if any articles are not translated, they get a message that the page does not exist. This is because the fr locale has been set up, but is not populated for every article.

In all examples, if a user wants to manually change the language that they view an article in, then they must specify a different locale in the URL or change the language in the help center language drop-down menu. If the language is enabled in the help center, and has translated content available for that article, they'll see that content.

For example, if you type the URL <https://support.zendesk.com/hc/de>, you'll see German content for that page, regardless of your default browser language. Specifying a locale in the URL does not change the language in which you are browsing the help center. To browse the help center in a different language, you must use the language drop-down menu.

If you provide only some of your content in other languages, consider one of the following solutions:

- [Redirect untranslated articles to an existing language](https://support.zendesk.com/hc/en-us/articles/4408886627866-Redirecting-traffic-from-deleted-Help-Center-articles#untranslated)
- Add a default language version of the article to the translation page. In our example, this would mean copying the English article into the French translation page. See [delivering content in your supported languages](https://support.zendesk.com/hc/en-us/articles/4408834328090).

## Removing a help center language

You can disable any language you have enabled in your help center by deleting it in the help center Languages page. When you delete a language, help center articles in the deleted language are unpublished, but remain in Guide admin. If you add the language back in, the related content will be republished.

**To set up your help center for multiple languages**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_settings.png)) in the sidebar.
2. Select **Language settings**.
3. Click the options menu beside the language you want to remove, then click **Delete**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/languages_options_menu.png)

   The language is removed from your list of languages, without a confirmation dialog. You can enable it again if necessary by clicking **Add new language**.
4. Click **Save** on the help center **Language** page when you are finished.

## Changing a translated help center name

You can add a translated help center name when you enable a language. You can easily change the help center name for a language at any time.

**To change a translated help center name**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Settings** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_settings.png)) in the sidebar.
2. Select **Language settings**.
3. Click in the name field for any language, then enter a new name.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/languages_list.png)
4. Click **Save** on the help center **Language** page when you are finished.
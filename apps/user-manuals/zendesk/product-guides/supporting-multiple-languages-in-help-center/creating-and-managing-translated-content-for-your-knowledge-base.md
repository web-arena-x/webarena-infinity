# Creating and managing translated content for your knowledge base 

Source: https://support.zendesk.com/hc/en-us/articles/4408886903450-Creating-and-managing-translated-content-for-your-knowledge-base

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

You can provide
your customers with a completely localized (translated), user experience. This includes all
the words in the user interface as well as your knowledge base content.

Zendesk automatically provides localization of the user interface, including translation of
default system fields. For the Description field, Zendesk automatically translates the
default customer-facing description. If you change this value and don't use dynamic content,
the description will not be automatically retranslated.

Zendesk also provides the means to host and present your translated articles. You can also
display custom snippets of translated text on your help center pages. For example, you may
want to add a welcome message on the home page or a company tagline in the header.

In this article, we explain how you might set up and manage the authoring, translation,
publishing, and updating of your knowledge base content.

Note: Managing translated content in
your business rules and support ticket workflow is handled by a feature in the Admin Center
called [dynamic content](https://support.zendesk.com/hc/en-us/articles/4408882999066).

If you haven't already done so, you need to first enable multiple language support and then
build out the structure of your localized versions, as described in [Localizing help center content](https://support.zendesk.com/hc/en-us/articles/4408834328090).

This article covers the following topics:

- [Authoring and managing your knowledge base content](#topic_v3b_zfd_v3)
- [Your options for managing content translation](#topic_r1f_4gd_v3)
- [Use Zendesk translation integrations provided by third party translation services](#topic_uv2_331_53)
- [Use the help center API to automate the managing, handoff, and publishing of your content](#topic_p22_sw2_2db)
  - [How the Zendesk Documentation team creates and manages content and handles translations](#topic_dsr_xw2_2db)
  - [Other examples of using the help center API to integrate with a translation service](#topic_nbx_nx2_2db)
- [Managing your translations manually](#topic_wcm_dy2_2db)

## Authoring and managing your knowledge base content

There is an easy-to-use [editor](https://support.zendesk.com/hc/en-us/articles/4408839258778) and [content management tools](https://support.zendesk.com/hc/en-us/sections/206658728) to create knowledge base
articles directly in Knowledge admin. When you choose other languages to support, you can
easily create language-specific versions of your articles. A container article is created
for you, but you must provide the translated content to insert into them. See [Localizing help center content](https://support.zendesk.com/hc/en-us/articles/4408834328090).

You can author your articles directly in Knowledge admin using the editor and you can also
view and edit the underlying HTML source of those articles. See [Editing the source code of help center articles](https://support.zendesk.com/hc/en-us/articles/4408824584602).

For many Zendesk customers, the editor and content tools available in Knowledge admin are
sufficient for creating and managing knowledge base articles. However, when you decide to
start supporting other languages, your choice of a translation provider and the processes
that come with that choice may affect what tools you’ll use to author and manage your
knowledge base content.

The biggest challenges involved with managing translated content is getting the content to
and back from the translation service provider, publishing the content, and then keeping it
up to date — and, do all that with as little manual work as possible.

With those challenges in mind, let’s look at your options for managing your knowledge base
content and translations.

## Your options for managing content translation

As you saw in the previous section, you can easily create the containers for additional language
versions of your articles. However, unless you have a staff of in-house translators, you
need to find an external resource to do the translations. That means finding a way to get
your default language content to and back from those external translators.

Here are your options — in order of recommended approach.

- Use [AI translations for articles](https://support.zendesk.com/hc/en-us/articles/8717609637018), available with the
  [Copilot add-on](https://support.zendesk.com/hc/en-us/articles/5524125586330), to quickly create article translations from
  within the article editor. If your help center is configured to support multiple
  languages, you can use the AI translation tool to quickly and easily populate an article
  with translated content. AI translations for articles supports all languages currently
  supported by Knowledge.
- **Find a translation service that provides a Zendesk integration**. As you can see
  below in [Use Zendesk translation
  integrations provided by third party translation services](#topic_uv2_331_53), there are many
  translation services that are integrated with Zendesk and make the exchange of content
  and its ongoing management a fairly easy and automated process. We highly recommend that
  you consider this approach for your help center translations.
- **Create your own integration and translation handoff process using the help center
  API**. The means by which the translation agencies are able to integrate with
  Zendesk are available to you to create your own homegrown automated translation tools.
  The Zendesk Documentation team uses an implementation of the help center API to process
  our translations, and as you’ll see below in [Use the help center API to automate the managing, handoff, and
  publishing of your content](#topic_p22_sw2_2db) so do a number of Zendesk customers. This requires
  some programming, but there’s plenty of sample code available to get you started.
- **Use a manual process for managing and handing off content**. This isn’t the ideal
  way to handle translations, but if you don’t have much content it may work for you. A
  number of Zendesk customers use this approach so we include it here as well (see [Managing your translations manually](#topic_wcm_dy2_2db)).
  This approach doesn't scale well, but may help you get started before you move to a
  better, more integrated solution.

In the following sections of this article we’ll describe each of the following options in
more detail.

## Use Zendesk translation integrations provided by third party translation services

Many cloud-based translation services are available to help you manage and translate your
knowledge base content, working directly in Knowledge admin. These are end-to-end solutions
that do not require you to create any custom tools or do any programming with the help
center API.

As an example, Unbabel, a Zendesk technology partner, has an integration called [Unbabel Translate for Zendesk](https://www.zendesk.com/apps/support/unbabel-for-zendesk-support/) (available in the Zendesk
Marketplace), that provides easy access to translation services for your customer service
interactions and your knowledge base content.

Below is a list of many of the other translation services available that you can integrate.
A number of them are also available in the Zendesk Marketplace.

Note: This is for information
purposes only. We have not used or tested any of these services and therefore do not
endorse any of them. If you use or have used any of these services, feel free to share
your experiences in the [community](https://support.zendesk.com/hc/en-us/community/topics/1260801308370-Discussion-Tips-and-best-practices-from-the-community).

- [Acclaro](https://www.acclaro.com/our-technology-platform/cloud-translation-integrations/zendesk-translation-connector/)
- [Crowdin](https://support.crowdin.com/zendesk-guide-integration/)
- [GlobalLink Connect](http://www.translations.com/globallink/products/globallink_connect.html)
- [Lingotek Inside Zendesk](https://www.zendesk.com/apps/support/lingotek-inside-zendesk/)
- [Localizer.co](https://www.localizer.co/support/252548-Support-customers-by-translating-your-ZenDesk-to-their-language)
- [Lokalise](https://docs.lokalise.co/integrations/zendesk)
- [Memsource](https://www.zendesk.com/apps/support/memsource/)
- [Qordoba](https://www.zendesk.com/apps/support/qordoba/)
- [Smartling](https://www.zendesk.com/apps/support/smartling/)
- [Translate
  Media](https://www.translatemedia.com/)

All of these services are separate from Zendesk and are an additional cost. You can refer
to their websites for pricing information.

## Use the help center API to automate the managing, handoff, and publishing of your content

You can use the Zendesk [help center API](https://developer.zendesk.com/rest_api/docs/help_center/introduction) to automate the management, handoff, and
publishing of all your knowledge base content. This requires some programming skill to use
the API for this purpose, but fortunately there are a number of implementations of this
already available that you can start with.

### How the Zendesk Documentation team creates and manages content and handles translations

The default language of our help centers is English. We translate the product
documentation in German, Spanish, French, Japanese, and Brazilian Portuguese.

Although much of the content contained in Zendesk help centers is authored directly in
Knowledge admin, the product documentation, which is always translated, is created by the
technical writers on the Zendesk Documentation team. It’s authored in DITA (Document
Information Typing Architecture), which is an XML-based data model for authoring and
publishing.

The authoring tool we use to develop DITA content is [Oxygen
XML Author](https://www.oxygenxml.com/xml_author.html). It provides us with a robust technical documentation authoring
experience and the flexibility to publish our content in many formats from a single
source. Other authoring tools such as Framemaker, Arbortext, and XMetal (to mention just a
few), can also be used to create DITA content.

From the English DITA source files, we generate HTML output and publish it in our help
center.

When a localization handoff is due, we use the help center API to download selected
English articles from the help centers as HTML files, then hand off the files to a
translation agency. After the translators return translated versions of the HTML files, we
use the API to automatically upload them to the help centers.

The API client we use to manage handoff files is called ZEP (Zendesk production tools),
created by Charles Nadeau, one of the writers on the Docs team. ZEP is a collection of
command-line tools for performing various help center production tasks. The client is open
source and available on his [Github](https://github.com/chucknado/zep) page. You can read more about it in the [ZEP documentation](https://github.com/chucknado/zep/tree/master/docs) on Github.

You can think of the Zendesk Documentation team’s use of the help center API as a
partially automated process because we manually bundle and hand off the files to our
translation agency using a shared handoff folder. However, the help center API can be used
to completely automate the handoff and return of files for translations, as you’ll see
next.

### Other examples of using the help center API to integrate with a translation service

Zendesk customers GAIA GPS and Wire both used the help center API to integrate with a
translation service and automate the round trip between their help center and their
translation service providers.

**GAIA GPS** - Andrew L. Johnson from GAIA GPS used the help center API to integrate
with [Gengo](https://gengo.com/), an
online translation service. As he describes in [Localize Zendesk help center, and Make PDFs Too](http://andrewljohnson.com/article/localize-zendesk-help-center-and-make-pdfs-too/),
he built an integration to send “articles to Gengo for translation, retrieve the
translations, and post the localized articles back to Zendesk”. His code is also available
on [Github](https://github.com/trailbehind/zendesk-utils/tree/master/localize).

**Wire** - Nick, a QA Specialist at Wire, [describes](https://support.zendesk.com/hc/en-us/community/posts/115007774788-How-we-made-Wire-s-article-translation-easier-and-faster) how they used the help center API to
create an integration with [Crowdin](https://crowdin.com/), a localization management platform, which is similar to
what GAIA GPS created. You can find the code for their project on [Github](https://github.com/mykola-mokhnach/zendesk-help-center-localization).

## Managing your translations manually

Many Zendesk customers start by authoring and maintaining their knowledge base content in
Knowledge admin, and then when they start supporting other languages, find that they need to
develop a manual process for handling their translations. This usually means using a
spreadsheet and sending that file to their translation agency.

This is a manual process and involves the following steps.

- Creating a spreadsheet with a column for each language you support
- Moving your default language content into the spreadsheet
- Handing that spreadsheet off to a translation agency
- When the translation agency hands it back to you with your translated content, copying
  and pasting the translations into the language variation versions of the default
  language articles
- Using the article editor to apply any formatting, if necessary
- Publishing the translated versions of the articles, one at a time

Because the article editor allows you to access the underlying HTML of your articles, you
may want to copy those source files into your spreadsheet and hand them off to the
translation agency, especially if you’re using custom formatting and your own CSS.

With a manual approach like this, you also need a process for keeping track of changes that
you make to your default language article content and then make sure that those changes are
routinely sent to the translation agency to make sure that your language versions don’t get
out of sync.

You can mark translated versions of articles as being out of date; therefore, needing an
updated translation (see [Marking a translated article as out of date](https://support.zendesk.com/hc/en-us/articles/4408821505306#topic_3dr_lgh_cy)).

As you can imagine, this approach is time consuming and becomes very difficult to manage
when your knowledge base grows. This is why we recommend that you choose an integrated
translation solution instead. If you’re already using a translation agency that doesn’t
offer a Zendesk integration, the help center API is an excellent option for automating
handoffs and managing your article translations.
# Understanding web crawler locales

Source: https://support.zendesk.com/hc/en-us/articles/4707428787354-Understanding-web-crawler-locales

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Guide Professional or Enterprise |

A locale is a standard that specifies the language of your help center content and possibly also a regional variation of that language (for example en-US for US English or en-GB for British English). If you [configured your help center to support multiple languages](../supporting-multiple-languages-in-help-center/configuring-your-help-center-to-support-multiple-languages.md), you can [localize your help center](../supporting-multiple-languages-in-help-center/localizing-help-center-content.md) to add translated versions of content, or add content only in specific languages.

The web crawler determines the locale and language of external content when indexing content, thereby enabling it to be mapped to the help center that corresponds to that locale.

This article contains the following sections:

- [Locales in the help center](#topic_zhm_2rj_35b)
- [How the web crawler detects locales](#topic_q3l_fly_ytb)

## Locales in the help center

The help center displays pages in different languages based on locale code in the page URL (for example, ".../hc/en-us"). Any translated article must also have parent pages (section and category) translated in the same language.

The following diagram illustrates the locale tags used to specify language and regional variations of content. This tag appears in the article URL for each article in your help center (for example, https://helpcenter.zendesk.com/hc/**en-us/**articles/4408827609882).

![](https://zen-marketing-documentation.s3.us-west-1.amazonaws.com/docs/en/guide-sc-locale.png)

## How the web crawler detects locales

The web crawler contributes to your help center’s ability to handle multiple languages and locales by determining the locale and language of external content, including regional variations, and then indexing the content with the detected locale so that it can be mapped to the corresponding help center.

To determine the locale or language, the web crawler first tries to extract the locale from the `lang` attribute in the `<html>` tag to determine whether there is an exact match for the locale in any help center on the account. If there is a match, the record is indexed with the detected locale. If a locale is not detected or there is not an exact match, the crawler then tries to extract the locale from first the `Content-Language header`, and then the`<meta>` tag.

If there is no exact match for any of `lang`, `Content-Language header` or `meta` tag, the crawler tries to find help center locales that match the language subtag in `html lang` (the region part in the `lang` tag will be ignored if it exists). For example, for a page with `<html lang="en">`, if the account has US English (en-us) and British English (en-gb) enabled, the record will be indexed for both US English and British English locales.

If there is no `lang`, `Content-Language header`, or `<meta>` tag defined, the crawler performs a text analysis on the content using Compact Language Detection (CLD) to detect the language. If a language is detected, the record is indexed with enabled locales that match that language. For example, if English (en) is detected and the account has US English (en-us) and British English (en-gb) enabled, the record will be indexed for both US English and British English locales.

If there is either no locale detected or there is not a match between the detected locale and any help center translation in your account, the crawler generates a "Locale not detected" error, which is included in the error report sent to the crawler owner identified during [web crawler setup](https://support.zendesk.com/hc/en-us/articles/4593564000410-Setting-up-the-search-crawler).
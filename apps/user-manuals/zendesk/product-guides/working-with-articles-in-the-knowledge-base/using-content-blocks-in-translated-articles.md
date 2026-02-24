# Using content blocks in translated articles

Source: https://support.zendesk.com/hc/en-us/articles/4486473049370-Using-content-blocks-in-translated-articles

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Enterprise or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Guide Enterprise |

You can configure your help center to support multiple languages (see [Localizing help center content](../supporting-multiple-languages-in-help-center/localizing-help-center-content.md)) and then add translated versions of each article in your help center. The help center will display pages in the different languages based on the locale specified in the URL. To incorporate content blocks in translated articles, you can translate the content blocks and then add them to the localized articles.

When you translate a content block for use in a translated article, it does not include a reference to the original content block. Instead, the translated content block is a standalone content block that you can add to translated articles in your help center. Once you add a content block to an article, it functions the same, regardless of whether it is an original or a translated content block.

When content blocks are used this way, they retain their reusability, but must be maintained in the translated language and manually placed in relevant translated articles.

This article describes two scenarios that you can use when adding translated content blocks to translated articles in your help center. Both examples assume that you have [configured your help center to support multiple languages](../supporting-multiple-languages-in-help-center/configuring-your-help-center-to-support-multiple-languages.md) and have [localized your help center content](../supporting-multiple-languages-in-help-center/localizing-help-center-content.md) accordingly.

- [Adding a translated content block to a translated article](#topic_wgv_yfs_zsb)
- [Adding a translated content block to a group of articles translated into variations of the same language](#topic_mly_cgs_zsb)

## Adding a translated content block to a translated article

You can create and translate a content block, and then [insert that content block in articles](creating-and-inserting-reusable-information-with-content-blocks.md) that are translated into the same language. For example, if you have information about product support that applies to a group of product articles, you can translate the content block that describes your support option, and then insert it into all of the articles for that product that are translated into the same language. In this model, your German articles will contain the German version of the content block, and the French articles will contain the French content block.

If you need to change anything in the content block, you can make the change to the translated content block. The change will appear in all translated articles that contain the content block.

## Adding a translated content block to a group of articles translated into variations of the same language

Variations of a language are versions of a language that are close enough to one another to be able to share certain content. For example, although there are many differences between UK English and US English, you can still develop content that is understandable and reusable in both localizations. In situations like these, you can develop content blocks for use in multiple localized versions of the same article.

For example, you might have a content block that provides system requirements for your software. These requirements are technical and do not vary between French and French Canadian translations. In this scenario, you can create a content block with the system requirements and translate it into French. You can then insert the translated content block into both French and French Canadian translated articles that require the system requirements.

This approach is also useful for content such as disclaimers or boilerplate text that you only want to create once, maintain centrally, and reuse in multiple places, and in multiple translations.
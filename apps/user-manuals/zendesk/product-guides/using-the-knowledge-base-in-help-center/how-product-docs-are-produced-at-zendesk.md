# How product docs are produced at Zendesk

Source: https://support.zendesk.com/hc/en-us/articles/4408844161050-How-product-docs-are-produced-at-Zendesk

---

All public-facing product documentation for Zendesk is published in this Zendesk help center. Though most other teams at Zendesk create content directly in the help center, the Docs team creates and maintains the product documentation offline in DITA source files. DITA, which stands for Document Information Typing Architecture, is an XML-based data model for authoring and publishing content. Basically, DITA files are plain text XML files.

Note: The product documentation is different from the developer documentation on developer.zendesk.com. A different process is used for the developer docs.

This article covers the following topics:

- [Why DITA?](#topic_qdm_yhk_gs)
- [How we author and publish articles](#topic_ezm_pcv_4v)
- [How we manage files](#topic_fs2_t1m_f2b)
- [How we publish localized articles](#topic_p3p_zhk_gs)

## Why DITA?

DITA is an industry-standard for creating and maintaining large documentation sets. It's designed for publishing content in multiple channels from a single source. Jacquie Samuels on techwhirl.com describes the problem it tries to solve as follows:

> Writing content in Word, email, PowerPoint, WordPress, HTML, InDesign,
> FrameMaker, or any other format is equivalent to writing on stone
> tablets. Your content is essentially stuck in that format and dumb
> as a rock. Dumb content can’t be easily reused or repurposed, and
> that’s inefficient and costly.
>
> DITA is a way of writing and
> storing your content so you can manage it like an asset. It
> leverages XML (eXtensible Markup Language), to make your
> content intelligent, versatile, manageable, and
> portable.
>
> For example, content that is in DITA can be
> published to (and fully branded), PDF, HTML, RTF, PowerPoint, and
> mobile–all without ever copying and pasting anything between
> files.

(Source: [What Is DITA?](https://techwhirl.com/what-is-dita/) on TechWhirl)

Apart from separating content from format, the other benefits of DITA for the Zendesk Docs team are as follows:

- Forces us to be disciplined about content structure. A DITA file is XML. If the structure is invalid, the tool won't let us do anything with it.
- Allows us to move content around easily. We just drag a topic node from one place to another in the structure.
- Allows us to reuse content by importing chunks of content in multiple articles.
- We don't often publish PDFs but when we do, we use the DITA source files.

The DITA authoring tool we use is [Oxygen XML Author](https://www.oxygenxml.com/xml_author.html). In addition to its robust authoring environment, we rely on a host of other features, including search, validation, and XHTML transformations. Other DITA authoring tools include Framemaker, Arbortext, and XMetal (to mention a few).

Note: Be aware that DITA has a steep learning curve in terms of both setup and authoring.

## How we author and publish articles

The writers use Oxygen XML Author to create or update content in the DITA files. Because DITA was created to allow multi-channel publishing from a single source, the DITA text files contain no styling. All they contain is structured content. For the web channel, all the styling is provided by external CSS style sheets, not DITA. In our case, all the styling is provided by the style sheets in our help center theme.

When we're ready to publish (usually at the same time a product feature is released or updated), we use Author to transform the DITA to XHTML, which is a stricter version of HTML. We then publish the XHTML to the help center using the [Help Center API](https://developer.zendesk.com/api-reference/help_center/help-center-api/introduction/).

Starting with version 24, [Oxygen XML Editor](https://www.oxygenxml.com/xml_editor.html)
includes a built-in transformation scenario that can publish DITA topics to XHTML output and upload them directly as articles to a Zendesk help center. See [DITA Map Publishing](https://www.oxygenxml.com/doc/versions/24.0/ug-editor/topics/zendesk-transformation-output.html) in XML Editor help. For a video, see [Publishing Content to Zendesk Help Center](https://www.oxygenxml.com/demo/publishing_zendesk.html) in XML Editor help.

Occasionally, we need to update many articles in a short amount of time.
For example, when Zendesk simplified its pricing and branding, hundreds of amended articles had to be published by 8 a.m. Pacific time on a specific date. In the weeks leading up to the deadline, the writers updated the DITA source files, then we used Author to batch transform the files. We pushed them to the help center using the Help Center API. Publishing them only took a few minutes.

## How we manage files

We use GitHub to manage our DITA files. Before creating or updating an article, a writer creates a branch in our repository, makes the changes, then creates a pull request. The pull request is reviewed by the other writers on the team. This has the added benefit of giving writers an opportunity to peer review each other's work.

We store images in [Amazon S3](https://aws.amazon.com/s3/), or Amazon Simple Storage Service, a scalable cloud storage service provided by Amazon Web Services (AWS). All the images in our articles are served to your browser from S3, not from the help center. The Amazon S3 service makes managing the images simpler.

## How we publish localized articles

The default language of our help centers is English. We also publish the product docs in German, Spanish, French, Japanese, Korean, Brazilian Portuguese, Italian, and Simplified Chinese.

When a localization handoff is due, we use the help center API to download selected English articles from the help center and write them to HTML files. We use the Amazon AWS API to download article images from our Amazon S3 bucket. We package the HTML files and images and hand them off to our localization vendor. After the vendor returns the translations, we upload the articles and images with the Help Center API and the AWS API.
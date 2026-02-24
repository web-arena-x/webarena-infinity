# Formatting text with Markdown

Source: https://support.zendesk.com/hc/en-us/articles/4408846544922-Formatting-text-with-Markdown

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Markdown is a simple markup language you can use to easily add
formatting, links, and images to plain text. You can use it in the following places:

- Ticket comments (from the agent interface)
- Macros
- Agent signatures
- Dynamic content
- Help center articles, including [content blocks](https://support.zendesk.com/hc/en-us/articles/4408829589274)

Markdown commands are automatically supported by your ticket and article editor. You can
enter Markdown comments to format your content, or you can use the format toolbar to add rich
content. See [Table 1](#topic_xqx_mvc_43) below for supported
Markdown commands.

Note: Markdown is not available in emails and email templates. If you enter text with Markdown
syntax, the formatting will not render and the text will remain as is. For a detailed list of
where Markdown is supported, see [Where can I use Markdown and HTML in Zendesk Support?](https://support.zendesk.com/hc/en-us/articles/4408893263770)

Topics covered in this article:

- [Adding Markdown to text](#topic_xqx_mvc_43)
  - [Bold](#topic_xqx_mvc_43__row_bj4_vjn_1n)
  - [Italics](#topic_xqx_mvc_43__row_lkm_tln_1n)
  - [Bulleted
    lists](#topic_xqx_mvc_43__row_ppv_wln_1n)
  - [Numbered
    lists](#topic_xqx_mvc_43__row_lhh_xln_1n)
  - [Nested lists](#topic_xqx_mvc_43__row_xww_xln_1n)
  - [Headings](#topic_xqx_mvc_43__row_ubd_yln_1n)
  - [Block quotes](#topic_xqx_mvc_43__row_k3l_yln_1n)
  - [Inline code](#topic_xqx_mvc_43__row_vwt_yln_1n)
  - [Code blocks](#topic_xqx_mvc_43__row_fs1_zln_1n)
  - [Images](#topic_xqx_mvc_43__row_abf_1mn_1n)
  - [Links](#topic_xqx_mvc_43__row_tf4_bmn_1n)
  - [Images that are also
    links](#topic_xqx_mvc_43__row_plc_cmn_1n)
  - [Links to tickets](#topic_xqx_mvc_43__links_tix)
  - [Horizontal line
    rule](#topic_xqx_mvc_43__horizontal_line)
  - [Line break](#topic_xqx_mvc_43__line_break)
  - [Underscore](#topic_xqx_mvc_43__line_break)
- [Pasting Markdown text from another source](#topic_ldp_nd5_25b)

## Adding Markdown to text

The following table shows examples of how you can use Markdown to add common formatting.
You don't need to preview your formatting. Your content is formatted automatically as you
enter Markdown commands.

Note: These examples demonstrate one way you can add certain formatting. There might also
be additional ways you can achieve the same formatting. There are also many more
formatting options you can add with Markdown. For more options and information, see the
[complete Markdown syntax documentation](http://daringfireball.net/projects/markdown/syntax).

You can also watch this short video.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/aw_markdown.gif)

Table 1. Examples of Markdown syntax

| Formatting | Entered text | Published text | Comments |
| --- | --- | --- | --- |
| Bold | This is how you \*\*bold\*\* text. |  | Supported |
| Italics | This is how you \*italicize\* text. |  | Supported |
| Bulleted lists | \* Bullet one (don't forget a space after the asterisk) \* Bullet two  You must type a line break before and after the list. |  | Supported. You can also start with a hyphen (-) followed by a space to create a bulleted list. |
| Numbered lists | 1. Step one 2. Step two  Do not use a hashtag (#) when creating numbered lists in Markdown, as the symbol is used for other formatting.  You must type a line break before and after the list.  Numbered lists will always start with 1, regardless of what number was pasted. If you need a list to use different numbers, you need to paste plain text. |  | Supported |
| Nested lists | \* This is the first level of this list. You can add things like images, quote blocks, or links to a nested list in addition to just text.  You must type a line break before and after the list. |  | Supported, except for content blocks and articles. For the second level of indent, press Tab after you enter the list item. Works for both bulleted and numbered lists. |
| Headings | # Heading level one (with a space after the #) ## Heading level two  ### Heading level three |  | Supported. Up to four heading levels. Up to six heading levels in content blocks. |
| Block quotes | > Block quotes have to start and end with a blank line  > And each line of the quote starts with a right angle bracket and a space |  | Supported |
| Inline code | Here is some `inline code.` |  | Supported |
| Code blocks | ``` This is a code block.  ```  Creating a blank line and then indenting the next line or lines with four spaces creates a code block too.  You must type a line break before and after the code block. |  | Supported. To exit a code block placed at the end of a comment, press the Return key three times in a row. |
| Images | ![Optional alternative text if image doesn't load](http://www.sampleurl.com/logo.png) Tip: To embed an image that's not hosted, first attach the image to the ticket. Then open the attachment, right-click the image, select **Copy image URL**, and use this link to embed your image. Doesn't work if [private attachments are enabled](https://support.zendesk.com/hc/en-us/articles/4408832757146-Enabling-attachments-in-tickets#topic_nrp_bnx_xdb). |  | Supported, except for content blocks and articles. Adding an image URL automatically turns it into an image link. When the ticket comment is submitted, the image appears in the conversation log. |
| Links | [Link display text](http://www.sampleurl.com) |  | Supported in agent signatures |
| Images that are also links | [![alt text](imageurl)](linkurl) |  | Supported in agent signatures |
| Links to tickets | We addressed this in ticket #61. |  | Not supported, yet |
| Horizontal rule line | ---  You must enter a line break before and after the hyphens.  If you have three or more dashes under a line of text, with no blank space between them, instead of creating a horizontal rule below the text, the text above will change into a header. |  | Supported |
| Line break | Line 1  &nbsp;  Line 2  &nbsp;  You must type two line breaks before each &nbsp;. | Line 1 Line 2 | Not supported, except in articles and content blocks. In articles and content blocks, type **Shift+Enter** to add a line break. |
| Underscore | This is how you \\_underscore\\_ text. | This is how you underscore text. | Not supported |
| When you enter URLs for links and images, make sure you include the full URL, including the http:// or https:// prefix. | | | |

## Pasting Markdown text from another source

You can paste Markdown from another source in the ticket composer, but not in the article
editor. Here are some things to consider when you copy Markdown text from another source and
paste it into the ticket composer:

- If you copy text with Markdown commands from a *plain text editor*, the content is
  automatically formatted as soon as you paste it. If you don't want the content to be
  automatically formatted, use **Cmd+Shift+V** (Mac) or **Ctrl+Shift+V** (Windows) to
  paste.
- If you paste text with Markdown commands from a *rich text editor*, the Markdown
  commands remain "as is". The content is not automatically formatted.
- If you copy text with Markdown commands from any type of editor into a code block in the
  ticket composer, the content is not automatically formatted. It remains "as is."
- If you paste Markdown text with code blocks or nested lists, the format is not
  automatically carried over into the ticket
  composer.
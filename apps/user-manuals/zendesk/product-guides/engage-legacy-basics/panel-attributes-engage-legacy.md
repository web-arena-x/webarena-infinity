# Panel Attributes (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731475641498-Panel-Attributes-Engage-Legacy

---

## Panel Attribute Basics

Panel Attributes will appear full-width in the Contact Attributes panel and can be customised to use different color themes. You can also use basic markdown formatting.

![](https://support.zendesk.com/hc/article_attachments/9731466890906)

Like other enhanced attributes in Engage, you make an attribute a Panel by using a prefix in the attribute name. To control the text, and theme you need to use a basic JSON structure as the attribute value. The text value also supports markdown format. You can use the Attribute Builder tool below to help generate this value.

The example above would look something like this:

```
panel_AuthenticationResult: {"text":"## Diagnostic Result\n\n1. Authentication **Failed**\n1. Test Two *Running*","theme":"info"}
```

**Themes:** Refer to [this article on Label Attributes](https://support.zendesk.com/hc/en-us/articles/9696142331034) for more information on Available Themes

## Formatting with Markdown

Text in Panel Attributes support Basic Syntax Markdown formatting. This can be used for simple styling such as bold or underline. Or more advanced formats such as links, headings and images.

**Further Reading:** Refer to this [useful cheat sheet](https://www.markdownguide.org/cheat-sheet/) to learn more about markdown

‍

## Attribute Builder

Attribute Text

Theme
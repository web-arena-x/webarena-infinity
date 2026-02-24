# Panel attributes in Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9696112973210-Panel-attributes-in-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Panel attributes in Contact Center allow you to display detailed information to agents using full-width panels with customizable color themes. You can enhance these panels with Markdown for text styling, such as bold or headings. Use a JSON structure to define text and themes, making it easier to present clear, organized information. Explore themes and Markdown to optimize your contact attributes panel.

Panel attributes in Zendesk for Contact Center give you tools to present detailed information to agents.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_pa_1.png)

This article contains the following topics:

- [Panel attribute basics](#topic_zf4_4jh_pgc)
- [Formatting panel attributes with Markdown](#topic_ttk_12g_rgc)

## Panel attribute basics

Panel attributes appear full-width in the contact attributes panel and can be customized to use different color themes. Additionally, you can use basic markdown formatting.

Like other enhanced attributes in Contact Center, you make an attribute a panel by using a prefix in the attribute name. To control the text, and theme you must use a basic JSON structure as the attribute value. The text value also supports markdown format. You can use the Attribute Builder tool below to help generate this value.

The example above would look something like this:

```
panel_AuthenticationResult: {"text":"## Diagnostic Result\n\n1. Authentication **Failed**\n1. Test Two *Running*","theme":"info"}
```

For information about the available themes, see [label attributes](https://support.zendesk.com/hc/en-us/articles/9696142331034).

## Formatting panel attributes with Markdown

Text in panel attributes support basic syntax Markdown formatting. This can be used for simple styling, such as bold or underline or more advanced formats such as links, headings and images.

You can learn more about Markdown at the [Markdown Guide](https://www.markdownguide.org/cheat-sheet/) website.
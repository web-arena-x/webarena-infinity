# About the system font stack

Source: https://support.zendesk.com/hc/en-us/articles/4408887168026-About-the-system-font-stack

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

A *font stack* is a list of fonts and font keywords used to let a browser know our preferred and fallback fonts. For example, a font stack could be "Helvetica Neue, Arial, sans-serif" which would indicate Helvetica Neue as our most-preferred font (if available), and then Arial (which is on most computers), and lastly a generic sans-serif font, which is vague but guarantees we won’t accidentally show a serif font like Times New Roman.

Zendesk now uses a *system font stack* , which identifies your operating system and applies the font it natively uses for its own interface. Because your operating system is optimized for these fonts, they tend to load more quickly, feel and look good, render crisply, and have a very complete set of supported characters. Previously, Zendesk used Proxima Nova as its default font.

Here's Zendesk's system font stack:

```
body 
{font-family: system-ui, -apple-system, 
BlinkMacSystemFont, “Segoe UI”, 
Roboto, Oxygen-Sans, Ubuntu, Cantarell, 
“Helvetica Neue”, Arial, sans-serif; }
```

This stack is reflected across the entire Support product.

## Operating system and browser specifics

### Windows

While most browsers on Windows OS, including IE and Edge, don’t support a keyword to use the system font, we're still able to match it by including the font “Segoe UI” in our font stack.

### macOS

Apple provides a new font keyword, -apple-system, that will resolve to the system font. Today, that is [San Francisco](https://developer.apple.com/ios/human-interface-guidelines/visual-design/typography/). Apple has changed their system font before, and may again one day. When that happens, users on the latest operating system will see that font on websites using the font keyword; users on older systems will still see San Francisco.

### Everywhere else

Chrome now supports "system-ui," a font keyword that resolves to the system font on *all* operating systems (including Windows, Mac, and Linux). More browsers will add this keyword soon. And we’ve included some Linux-specific fonts in our stack in the meantime.

## Why system fonts?

System fonts are superior to non-system fonts in terms of kerning and readability. See the sections below for more details.

### Kerning

Both system fonts for Windows OS and Mac OS have fonts that come with kerning by default. Kerning refers to letter spacing that makes wide and thin letters feel much more readable. Some web fonts, like Proxima Nova, required enabling and tweaking of kerning settings.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/kearning3.png)

Proxima Nova:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/proximanova2.png)

System font stack:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/systemfontstack3.png)

### Readability

The system fonts typically are thicker than the current Proxima Nova font. This makes it easier to read and highlights the contrast between the text and the background. Though the font is a bit bigger, it won't affect how much information you see on the screen because the container sizes have not changed.
# Understanding Liquid markup and Zendesk Support

Source: https://support.zendesk.com/hc/en-us/articles/4408883291290-Understanding-Liquid-markup-and-Zendesk-Support

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

If you're familiar with placeholders in Zendesk Support, then you already know something about Liquid markup. It's the templating language we use to enable them. Placeholders are used in automations, macros, triggers, and widgets as containers for dynamically generated ticket and user data. What you may not know about Liquid markup is that you can also use it to customize how this data is selected and displayed as output. This is because Liquid also allows you to create simple programming logic such as case statements, if statements, for loops, and so on.

By writing simple control statements directly in the comment/description action in macros and the email user action in automations and ticket triggers, you can accomplish in one automation, macro, or trigger what you used to have to do in multiple automations, macros, and triggers. You can also customize how comment text is presented. This isn't supported for messaging triggers.

You can find the Liquid documentation at [Liquid for Designers](https://github.com/Shopify/liquid/wiki/Liquid-for-Designers). All of the elements of the language are described in detail. Here, however, is a brief introduction to how it works.

Liquid is a templating language for rendering email and HTML. Liquid is the mechanism that enables the automated placement of data in comments and email notifications using placeholders.

There are two types of markup in Liquid:

- Output, which is text output contained in double curly brackets.
- Tags, which contain the programming logic that determines how the data is expressed with placeholders.

If you simply equate ***output*** with ***placeholder***, you're about half way to understanding what Liquid is and how it's used. What you may not know about Liquid output however is that in addition to expressing ticket and user data, there are also methods available to manipulate text strings and arrays. In Liquid, these methods are referred to as ***filters***. Using a filter you can transform text to uppercase characters, for example. But that's one of the simplest examples of what filters can be used for. See the Liquid documentation for more information.

The other half of understanding of how Liquid can be used comes from knowing what tags are and how they are used. Tags provide the programming logic that you can use to select and present data.

Using Liquid tags you can create:

- if else statements
- case statements
- for loops
- cycles
- variable assignments

For more examples of how Liquid markup can be used, see the following articles:

- [Using Liquid markup to support multiple languages in automations, macros, and triggers](https://support.zendesk.com/hc/en-us/articles/4408842967578)
- [Modifying a ticket trigger to return a response based on business hours](https://support.zendesk.com/hc/en-us/articles/4408829256218)
- [Using Liquid markup to customize the formatting and placement of text in comments and email notifications](https://support.zendesk.com/hc/en-us/articles/4408832790042)
- [How can I format placeholders with liquid markup?](https://support.zendesk.com/hc/en-us/articles/4408836545562)
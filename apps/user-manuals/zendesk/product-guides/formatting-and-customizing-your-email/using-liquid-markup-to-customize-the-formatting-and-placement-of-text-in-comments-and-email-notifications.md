# Using Liquid markup to customize the formatting and placement of text in comments and email notifications

Source: https://support.zendesk.com/hc/en-us/articles/4408832790042-Using-Liquid-markup-to-customize-the-formatting-and-placement-of-text-in-comments-and-email-notifications

---

By default, many business rules use the {{ticket.comments\_formatted}} placeholder to include comments into email notifications. If you want more control over how the comments are presented to requesters, you can access more details about comments and their attachments using Liquid markup.

Note: Liquid markup is not supported for help center article notifications such as email notifications sent to followers. An alternative is to follow the steps in [Using the email template with multiple brands](https://support.zendesk.com/hc/en-us/articles/4408832356762).

A comment is an element within a ticket and there are a number of placeholders available that you can use to include comments in email notifications. For example, you can include all comments, public comments, the last comment, etc (see [Comment data](https://support.zendesk.com/hc/en-us/articles/4408886858138-Zendesk-placeholders-reference#topic_jkz_opl_rc)).

If you want more control over how comments are displayed in email notifications, you can use Liquid markup and a for loop, as in this example:

```
{% for comment in ticket.comments %}

   Comment:
   {{comment.created_at}}
   {{comment.created_at_with_time}}
   {{comment.author.name}}
   {{comment.value}}

   Attachment:
   {% for attachment in comment.attachments %}
   {{attachment.filename}}
   {{attachment.url}} 

   {% endfor %}

{% endfor %}
```

This returns the items in both arrays (ticket.comments and comment.attachments). In other words, the properties for every comment and attachment contained in the ticket.

If you want to only return the last comment, you can use the `limit` and `offset` attributes as in the following example:

```
{% for comment in ticket.comments limit:1 offset:0 %}
```

You can do a lot with arrays in for loops. Refer to the Liquid documentation ([Liquid for Designers](https://github.com/Shopify/liquid/wiki/Liquid-for-Designers)) for more details.

For more information on how Liquid markup can be used, see [Understanding Liquid markup and Zendesk Support](https://support.zendesk.com/hc/en-us/articles/4408883291290).
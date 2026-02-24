# Label Attributes (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731499231514-Label-Attributes-Engage-Legacy

---

Standard attributes are great for giving agents context about the contact they are handling. But sometimes you need to callout specific information that cant be missed. Label Attributes in Engage are simple but powerful way to do just that.

## Label Attribute Basics

Label Attributes will display at the top of the Contact Attributes panel and can be customised to use different color themes and icons.

![](https://support.zendesk.com/hc/article_attachments/9731475216794)

Like other enhanced attributes in Engage, you make an attribute a Label by using a prefix in the attribute name. To control the text, theme and icon you need to use a basic JSON structure as the attribute value. You can use the Attribute Builder tool below to help generate this value.

The example above would look something like this:

```
label_AuthenticationResult: {'text':'OTP Authentication Passed', 'theme':'success', 'icon':'checklist-2' }
```

**Note:** The text from the attribute name (eg. Authentication Result) will not appear in the interface.

### Using Multiple Labels

If you have multiple Label Attributes they will be ordered alphabetically by attribute name. For example, **label\_AuthenticationResult** will appear before **label\_ShippingStatus**.

![](https://support.zendesk.com/hc/article_attachments/9731499271066)

You can use numbers in the attribute names for finer control over ordering. Eg. **label\_1\_ShippingStatus** would move this to the front of the list.

![](https://support.zendesk.com/hc/article_attachments/9731450187802)

## Available Themes

The Theme will control what color is used for the label and best used to convey additional meaning to the information you are displaying. There are 4 themes available that are consistent with other alerts and banners in the Engage UI. If you don't specify a theme the label will display as a neutral grey.

![](https://support.zendesk.com/hc/article_attachments/9731438508826)

## Available Icons

The icon set available is the same as Utilities. It should provide enough variety to cover a range of common use-cases.

## Attribute Builder

Fill in the details below and then copy to clipboard. You can then paste the attribute value in a Contact Flow Block.

Attribute Text

Theme

Icon

‍
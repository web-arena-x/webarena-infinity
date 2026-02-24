# Using label attributes in Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9696142331034-Using-label-attributes-in-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Label attributes help you highlight crucial information in the contact attributes panel using customizable colors and icons. By adding a prefix to an attribute name and using a JSON structure, you can create labels that stand out. You can order multiple labels alphabetically or numerically, apply themes for added meaning, and choose from a variety of icons to suit different needs.

Standard attributes are great for giving agents context about the contact they are handling. However, sometimes you need to callout specific information that cant be missed. Label attributes can be used to accomplish this.

Label attributes are displayed at the top of the contact attributes panel and can be customised to use different color themes and icons.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_la_1.png)

Like other enhanced attributes in Contact Center, you make an attribute a label by adding a prefix to the attribute name. To control the text, theme and icon you need to use a basic JSON structure as the attribute value. You can use the attribute builder tool to help generate this value.

The example above would look something like this:

```
label_AuthenticationResult: {'text':'OTP Authentication Passed', 'theme':'success', 'icon':'checklist-2' }
```

Note: The text from the attribute name (for example, authentication result) is not shown in the Contact Center app.

This article contains the following topics:

- [Using multiple labels](#topic_mpn_55m_rgc)
- [Using themes](#topic_utv_55m_rgc)
- [Using icons](#topic_cjw_lrg_pgc)

## Using multiple labels

If you have multiple label attributes, they will be ordered alphabetically by attribute name. For example, **label\_AuthenticationResult** will appear before **label\_ShippingStatus**.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_la_2.png)

You can use numbers in the attribute names for finer control over ordering.
For example, . **label\_1\_ShippingStatus** would move this to the front of the list.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_la_3.png)

## Using themes

Themes control the color used for the label and is best used to convey additional meaning to the information you are displaying. There are four themes available that are consistent with other alerts and banners in Contact Center. If you don't specify a theme the label will display in gray.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_la_4.png)

## Using icons

The icon set available is the same as for utilities and provides icons that cover a variety of common use cases.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_la_5.png)
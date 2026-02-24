# Displaying attributes to agents

Source: https://support.zendesk.com/hc/en-us/articles/9790998800410-Displaying-attributes-to-agents

---

You can display custom contact attributes to agents at the top of the main panel of Contact Center.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Display custom contact attributes to agents in the main panel to enhance customer interactions. Use plain text, emojis, and URLs for attributes, and create buttons with the `btn_` prefix for quick actions. Customize label and panel attributes for better visibility. Set attributes in the contact flow using the **Set Contact Attributes** block or **Invoke Lambda Function** block, and prefix with `agt_` for agent relevance.

You can display custom contact attributes to agents at the top of the main panel of Contact Center.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_extra_5.png)

This article contains the following topics:

- [About attributes](#topic_wrl_5zt_ygc)
- [Displaying attributes to agents](#topic_dth_hkg_wgc)

## About attributes

Keep in mind the following for the various attributes.

### Attribute content

Attributes in Amazon Connect support plain text, but do support emojis (Unicode). You can also add line breaks by using `\\n` .

Example: `agt_diagnosticResults"="❌ Line Connection - Down\\n❌ Modem not connected`

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_extra_6.png)

Contact Center detects any URLs in attributes and renders them as links.

### Button content

You can use the attribute prefix `btn_ admins` can create buttons in the contact attribute block. You can create as many buttons as you'd like.

Keep in mind:

- Buttons show in Active Contacts and Historical
- URLs are not validated
- Links open in a new tab

Example: `btn_view_ticket"="https://someticket.com/1234`

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_extra_7.png)

You can also configure a button attribute to open a utility using a special url format: `lm-utility://{{Utility ID}}?location=main`.

The location parameter, either main or side, controls whether the utility opens in the main panel or in the side panel:

To find the Utility ID, edit the utility in Settings. The ID is the last section of the url.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_extra_8.png)

### Label attributes

Label Attributes display at the top of the Contact Attributes panel and can be customized to use different color themes and icons. For more information, see [Using label attributes in Contact Center](https://support.zendesk.com/hc/en-us/articles/9696142331034).

### Panel attributes

Panel Attributes display full-width in the Contact Attributes panel and can be customized to use different color themes.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/cc_extra_9.png)

## Displaying attributes to agents

Any attributes you want to display needs to be set in the contact flow.

**To display attributes do one of the following**

- Use the **Set Contact Attributes** block to create a user-defined attribute. An example of this can be seen in the image below.
- Use the **Invoke Lambda Function** block to trigger a Lambda function that sets contact attributes using the UpdateContactAttributes API.

Rather than display all contact attributes here, admins can choose to display attributes that are useful for the agents by adding **agt\_** to the beginning of the attribute name. Attribute names can’t contain spaces, so you can use underscores (\_) or camelCase to separate words.

Example: `agt_affected_account"="04224422554`
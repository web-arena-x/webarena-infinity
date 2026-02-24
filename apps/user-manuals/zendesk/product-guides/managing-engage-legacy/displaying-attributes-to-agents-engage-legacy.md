# Displaying Attributes to Agents (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731466218650-Displaying-Attributes-to-Agents-Engage-Legacy

---

Custom contact attributes can be displayed to agents in the main panel of Engage.

## How to display attributes to agents

Any attributes you would like to display need to be set in the contact flow. There are two ways to do this:

1. Use the **Set Contact Attributes** block to create a user-defined attribute. An example of this can be seen in the image below.
2. Alternatively, use the **Invoke Lambda Function** block to trigger a Lambda function that sets contact attributes using the UpdateContactAttributes API.

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731449736986)

Engage will display chosen contact attributes in the contact attributes block at the top of the main panel.

![](https://support.zendesk.com/hc/article_attachments/9731437879194)

Rather than display all contact attributes here, Admins can choose to display attributes that are useful for the agents by adding **agt\_** to the beginning of the attribute name (i.e. the attribute key).

Because attribute names can’t contain spaces you can use underscores (\_) or camelCase to separate words.

For example: “agt\_affected\_account"="04224422554".

## Attribute content

Attributes in Connect only support plain text but do support emojis (Unicode). You can also add line breaks by using **\\n** .

### Example

"agt\_diagnosticResults"="❌ Line Connection - Down\\n❌ Modem not connected"

![](https://support.zendesk.com/hc/article_attachments/9731449753626)

Engage will also detect any urls (http://website.com) in attributes and render them as links.

## Button contact attributes

By using a attribute prefix **btn\_** admins can create buttons in the contact attribute block.

### Details

- You can create as many buttons as you like
- Buttons will show in Active Contacts and Historical
- Urls are not validated
- Links will open in a new tab

### Example

“btn\_view\_ticket"="https://someticket.com/1234"

![](https://support.zendesk.com/hc/article_attachments/9731449768346)

### Opening Utilities with Buttons

You can also configure a button attribute to open a utility using a special url format: **lm-utility://{{Utility ID}}?location=main**.

The location parameter will control where the utility will open:

- main - opens in the main panel
- side - opens in the side panel

To find the Utility ID edit the utility in Settings, the ID is the last section of the url.

![](https://support.zendesk.com/hc/article_attachments/9731437914394)

‍

## Label Attributes

Label Attributes display at the top of the Contact Attributes panel and can be customised to use different color themes and icons. You can find out how they work in this [in-depth article](https://support.zendesk.com/hc/en-us/articles/9696142331034)

![](https://support.zendesk.com/hc/article_attachments/9731474765594)

## Panel Attributes

Panel Attributes display full-width in the Contact Attributes panel and can be customised to use different color themes. You can find out how they work in this [in-depth article](https://support.zendesk.com/hc/en-us/articles/9696112973210)

![](https://support.zendesk.com/hc/article_attachments/9731474778650)
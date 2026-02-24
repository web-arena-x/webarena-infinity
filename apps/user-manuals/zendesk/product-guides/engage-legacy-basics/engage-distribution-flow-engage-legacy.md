# Engage Distribution Flow (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731466352410-Engage-Distribution-Flow-Engage-Legacy

---

Local Measure Engage transforms Amazon Connect into a true Omni-Channel solution by expanding the list of channels that can be routed by Amazon Connect.

‍

## Distribution Contact Flow

Local Measure Engage leverages a single 'Distribution' contact flow as the entry point for these channels. All these contacts are routed as 'CHAT' and are tagged with user defined attributes which identify the channel, which allows for custom routing per channel.

The below figure illustrates such a contact flow:

![](https://support.zendesk.com/hc/article_attachments/9731498811290)

In the above example:

1. A 'Check contact attributes' block is used to check the channel. As all Local Measure enabled channels are routed as 'CHAT', we check for this channel and split these out.
2. A second 'Check contact attributes' block is used to evaluate a user defined variable called 'user\_type'. The value of this attribute defines the channel. The table below defines the values for the various channels.
3. The outputs of this block can then be connected to additional contact flow blocks to define the routing logic for each. While the example above simply specifies a working queue and then transfers to the queue, a real life use case would most likely transfer each channel to another contact flow which will contain the routing logic to be used for that channel.

| Channel | user\_type |
| --- | --- |
| Email | ses |
| SMS | sms |
| Facebook Messenger | facebook |
| Instagram Direct messages | instagram |
| WhatsApp | whatsapp |
| Line | line |
| WeChat | wechat |

The first step in enabling any of the Local Measure channels, is to create a contact flow such as the one above. Once the contact flow has been created and saved in your Amazon Connect instance, you need to set this contact flow as the entry point for all the Local Measure Channels.

To do this, log into Local Measure Engage and navigate to the settings page (you will need Admin access to Engage for this) by clicking on the setting cog.

![](https://support.zendesk.com/hc/article_attachments/9731449863066)

Next, click 'Channels' and then 'Edit contact flow'.

![](https://support.zendesk.com/hc/article_attachments/9731438020122)

In the resulting popup window, select the contact flow you created from the dropdown list and click save.

![](https://support.zendesk.com/hc/article_attachments/9731466393626)

Any channels via Local Measure will now be using this contact flow as the entry point for Amazon Connect routing.

‍
# Using Web Widget (Classic) to embed customer service in your website

Source: https://support.zendesk.com/hc/en-us/articles/4408836216218-Using-Web-Widget-Classic-to-embed-customer-service-in-your-website

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support** | Team, Professional, or Enterprise |

Location: Admin Center > Channels > Classic > Web Widget

Note: This article applies to accounts using Web Widget (Classic). If you're using the messaging Web Widget, see [Creating a messaging Web Widget](https://support.zendesk.com/hc/en-us/articles/4409103246874).

In this article, we’ll introduce you to Web Widget (Classic), Zendesk’s legacy embeddable customer support interface. Web Widget (Classic) allows you to add contact options – help center, contact form, voice, and chat – to your website or help center, so that your customers can get immediate help from a single interface, in whatever form they like best.
including:

- Search help center articles for immediate self-service.
- Submit a support request using a contact form.
- Request a callback, or view a phone number that they can call instead.
- Start a live chat with an agent.

This article includes these sections:

- [About Web Widget (Classic)](#topic-1)
- [Browser requirements for Web Widget (Classic)](#topic_rzl_q2n_4r)
- [Understanding the end-user experience](#topic_bkd_qgd_bq)
 - [Self service](#topic_tyk_qv2_wfb)
 - [Live chat](#topic_flv_qv2_wfb)
 - [Phone calls](#topic_ojq_rv2_wfb)
 - [Contact forms](#topic_yj3_sv2_wfb)

## About Web Widget (Classic)

Web Widget (Classic) is a separate web application that you embed in a web page that gives customers access your help center and the agents in your other Zendesk support channels. It can encourage customers to self-serve, whenever possible, by using help center articles. It can also make it easier to get help from an agent by reducing the number of steps required to access a contact form, request a call back, and start a chat.

All of these things can be done from a single interface. The customer doesn't need to go from your home page to your help center, open their email application, or search your website to find a email address to contact you.

You can add the Web Widget (Classic) to your website or help center. It appears in the bottom corner by default.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/new_widget_cph_v3.png)

You must be an administrator to set up and manage the Web Widget (Classic).

The first thing you need to do is configure the components you want in the widget (see [Configuring the Components in your Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408838063258)), and then you can add the widget code your website or help center (see [Adding Web Widget (Classic) to your website or help center](https://support.zendesk.com/hc/en-us/articles/4408821673242)).

For a complete list of documentation about the Web Widget (Classic), see [Web Widget (Classic) resources](https://support.zendesk.com/hc/en-us/articles/4408833907354).

## Browser requirements for Web Widget (Classic)

Web Widget (Classic) is supported on the following browsers.

| Device type | Browsers |
| --- | --- |
| Desktop computers | - Google Chrome: Latest two versions - Microsoft Edge - Mozilla Firefox: Latest two versions - Apple Safari: Latest version |
| Mobile devices | - iOS Safari: Latest two versions - Android browser: Latest version - Chrome Mobile for Android and iOS: Latest version |

## Understanding the end-user experience

In Web Widget (Classic), you can enable components to combine knowledge base search, live chat, phone calls, and contact forms. The end user experience depends on what options are enabled and whether agents are online.

When multiple components are enabled in the Web Widget (Classic), components are presented to end users in a specific sequence, at different times, rather than all at once.

Components are presented in this order:

1. [Self service](#topic_tyk_qv2_wfb)
2. [Live chat](#topic_flv_qv2_wfb)
3. [Phone calls](#topic_ojq_rv2_wfb)
4. [Contact forms](#topic_yj3_sv2_wfb)

For more information about how visitors can use these components, keep reading.

## Self service

If the help center is enabled in the Web Widget (Classic), customers are presented with help center search first. When the Web Widget (Classic) opens, it includes both self-service and the contact button.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_contextual_help.png)

When you search, up to nine results appear, if matches are found. The customer can click an article in the list and it opens in Web Widget (Classic).

If Contextual Help is enabled in Web Widget (Classic), up to three suggested articles appear below the search box. The suggested articles are determined by the page URL from which the customer accessed the Web Widget (Classic), or it is chosen by the administrator using advanced customizations (see [About Contextual Help for the Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408824357402)).

## Live chat

This is an overview about how live chat works in Web Widget (Classic) from a visitor’s perspective. It’s meant to give administrators and agents a general idea about how it works, but it doesn’t cover all scenarios—the exact appearance and behavior of live chat in Web Widget (Classic) depends on how it was configured by the administrator.

Visitors to your website can use live chat functions in Web Widget (Classic) from a desktop or mobile browser (see [Customizing the Chat widget for mobile devices](https://support.zendesk.com/hc/en-us/articles/4408834237338)).

Your visitors can perform these chat-related activities from the Web Widget (Classic):

- [Starting chats from Web Widget (Classic) launcher](#topic_u2p_b2f_wfb)
- [Receive proactive chats](#topic_gjl_cpf_wfb)
- [View conversation history](#topic_st4_1pf_wfb)
- [Customize the avatar, name, and byline of the chat Concierge section](#topic_nnq_2pf_wfb)
- [Send and receive attachments with chats](#topic_s11_b2f_wfb)
- [Adjust sound, request transcripts, edit contact details, and end chats](#topic_r3b_12f_wfb)
- [Translate chats](#topic_otg_zdf_wfb)
- [End and rate chats](#topic_yxm_pdf_wfb)
- [Popping out Web Widget (Classic) during chats](#topic_dwz_hn5_dgb)

For more information, see [Setting up Zendesk Chat in Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408825767962).

### Starting chats from Web Widget (Classic) launcher

When live chat is enabled in Web Widget (Classic), the appearance of the launcher to end users depends on which other contact options are enabled.

| | |
| --- | --- |
| **Launcher appearance** | **Contact options and agent availability** |
| | If live chat is the only contact option enabled in Web Widget (Classic) and a Chat agent is online, the launcher includes the Chat icon and says **Chat**. |
| | If live chat and the help center are enabled, when a chat agent is online, the launcher includes the Chat icon and says **Help**. |
| | The chat badge is a special launcher that allows a customer to get support from a chat agent immediately. If the chat badge is enabled, chat is the only contact option enabled in the Web Widget (Classic), and a Chat agent is online, the chat badge appears on the page instead of the regular Web Widget (Classic) launcher. |
| | If Chat is the only contact option enabled and no agents are online, the launcher does not display. |

Once the customer opens Web Widget (Classic), they see this:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_hc_chat_v2.png)

When the customer clicks **Live chat**, what they see next depends on whether the pre-chat form is enabled.

| | |
| --- | --- |
| If the pre-chat form is enabled, the customer fills in the form, then clicks **Start Chat** | If the pre-chat form is *not* enabled, the customer can start the chat right away. |

If an agent is available when the customer clicks the launcher, but the then agent signs off before the chat begin, the customer sees a message indicating that the Chat agent is not available.

### Receiving proactive chats

Agents can see who is the currently on your site and decide whether to proactively contact a visitor before they request a chat. For example, you might want to reach out to visitors who have items their shopping cart, but are taking too long to complete their purchases. For more information, see [Browsing your site's visitors](https://support.zendesk.com/hc/en-us/articles/4408821265178), [Using Zendesk Chat](https://support.zendesk.com/hc/en-us/articles/4408824240026-Using-Zendesk-Chat), and [Targeting key visitors with proactive chat](https://support.zendesk.com/hc/en-us/articles/4408883473178).

### Viewing conversation history

If visitor authentication is enabled in the Web Widget (Classic), authenticated visitors can see their past chats. For more information about visitor authentication, see [Enabling authenticated visitors in the Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408838925082) and [Conversation history in Web Widget (Classic) for authenticated visitors](https://support.zendesk.com/hc/en-us/articles/4408821977114).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/chat_history_ex.png)

### Customize the avatar, name, and byline of the chat Concierge section

Before visitors connect with a support agent, they see the avatar, name, and byline of the chat Concierge. For more information, see [Customizing the Chat widget concierge](https://support.zendesk.com/hc/en-us/articles/4408828059546#topic_zxl_qll_4fb).

### Sending and receiving attachments with chats

Visitors can send and receive attachments. Clicking the attachments icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_chat_attach_file.png)) opens a standard file selection dialog box, but you can also drag and drop files into the Web Widget too. For more information about attachments, see [Managing file sending options](https://support.zendesk.com/hc/en-us/articles/4408886202394).

### Adjusting sound, requesting transcripts, editing contact details, and ending chats

Visitors can use the expandable menu at the bottom (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_chat_expand_menu.png)) to turn sounds on and off, request a transcript of the chat, edit their contact details, or end the chat. For more information about transcripts, see [Automatically send chat transcripts with email piping](https://support.zendesk.com/hc/en-us/articles/4408883226650). For more information about editing contact details, see [Editing Visitor Profile settings](https://support.zendesk.com/hc/en-us/articles/4408887640730).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_chat_expand_menu_open.png)

### Translating chats

If Chat detects that the agent and visitor are using different languages, the **Show translated** link appears in the conversation. Visitors can click this link to translate the agent’s replies into their language. The translation is performed by [Google Translate](https://translate.google.com/).

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_chat_translate.png)

### Ending and rating chats

When the visitor is ready, they can end the chat by clicking the end chat (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_chat_end.png)) icon. They can also end the chat from the expandable menu (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_chat_expand_menu.png)).

Visitors can rate a chat as good or bad using the thumbs up (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_chat_rate_good.png)) and thumbs down (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_chat_rate_good.png)) icons at any time during the chat. After they rate the chat, the **Leave a comment button** appears, so they can add a comment, if desired.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_chat_rate_v3.png)

If the visitor doesn’t rate the chat after a little while, the agent can prompt the visitor to rate the chat by making the **Rate this chat button** appear.

For more information about chat ratings, see [Measuring visitor satisfaction with chat rating](https://support.zendesk.com/hc/en-us/articles/4408883190682).

### Popping out Web Widget (Classic) during chats

WhenChat is enabled in the Web Widget (Classic), visitors can click the pop-out icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_popout_icon_v2.png)) to pop-out the Web Widget (Classic) to it's own browser window.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_popout_window.png)

The Web Widget (Classic) becomes separate from the website and receives a unique URL. It can be moved around and is no longer anchored to the website.

You can share the URL to the Web Widget (Classic) popout in a range of marketing communications, inviting the user to engage directly with you without having to be on your website.

## Phone calls

When call options are enabled in Web Widget (Classic), the appearance of the launcher to end users depends on which other contact options are enabled.

| | |
| --- | --- |
| **Launcher appearance** | **Contact options and agent availability** |
| | If voice is the only contact option enabled in Web Widget (Classic) *and* an agent is online, the launcher includes the call icon and says either **Request a callback** or **Call us**, depending on your configuration. |
| | If voice and the help center are enabled in Web Widget (Classic), and an agent is online, the button says **Help**. |
| | If voice, the help center, and chat, or contact forms are enabled in Web Widget (Classic), and agents are online, the launcher includes a question icon and says **Help**. |

When Web Widget (Classic) opens, the exact of call options in Web Widget (Classic) depends on the how it's configured by the administrator and the status of agents (see [Configuring voice options in Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408824310426)). Depending on your configuration, customers can:

- View a phone number that they can call
- Request a callback
- View the average wait time for a callback

The following examples show how call options might appear, depending on your configuration.

| | |
| --- | --- |
| | |
| If voice is the only option enabled in Web Widget (Classic) and it is configured to allow callback requests, and then you click the launcher, the callback form displays. | If voice is the only contact option enabled and it is configured for **Call Us** only, your phone number displays. |
| If voice and the help center are enabled, and other contact options are enabled (for example, chat or contact form), after a help center search the customer can access Talk from the **Contact us** button. | If voice and the help center are enabled, and chat and contact form are disabled, after a help center search the **Contact us** button says **Request a callback** (or **Call us**) instead. |
| | |

## Contact forms

Your customers can submit a ticket from Web Widget (Classic) to receive an email reply to their inquiry. The contact form is enabled in Web Widget (Classic) by default.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/widget_enduser_leavemsgattatchment_selected.png)

By default, the contact form includes fields for the customer's name, email address, and a description of the problem. If the administrator enabled multiple ticket forms in Web Widget (Classic) (see [Configuring the components in your Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408838063258)), then the customer can choose from multiple ticket forms. If not, then only the default contact form appears.

Tickets submitted through Web Widget (Classic) contain the tag `web_widget`.
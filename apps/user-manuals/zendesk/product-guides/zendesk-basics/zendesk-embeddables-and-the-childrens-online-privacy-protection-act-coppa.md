# Zendesk Embeddables and the Children's Online Privacy Protection Act (COPPA)

Source: https://support.zendesk.com/hc/en-us/articles/4408887182746-Zendesk-Embeddables-and-the-Children-s-Online-Privacy-Protection-Act-COPPA

---

The [Children's Online Privacy Protection Act (COPPA)](http://www.coppa.org) applies to websites that are collecting personal information from children under 13 years of age. As stated in our [Privacy policy](https://www.zendesk.com/company/privacy/), children under 13 years of age should not submit any personal information via our websites or services. This includes our on-demand Zendesk customer service solution available online at [https://www.zendesk.com](https://www.zendesk.com/).

We understand that some of our customers might be subject to COPPA, so if you are required to comply with the COPPA regulations, then you have probably already appropriately updated your policies and processes.

This article provides practical tips for how you can avoid collecting personal information for each of the [Zendesk Embeddables](https://www.zendesk.com/embeddables/) (Web Widget, Support SDKs, and Chat SDKs) without interfering with your COPPA compliance program if a child contacts you in your mobile app.

This article is not intended to provide you with legal advice on whether and how you are required to comply with COPPA and related regulations. Instead, this article is meant to provide you with functionality suggestions when using our services so as to not interfere with your compliance with COPPA and its requirements.

This article covers the following:

- [Defining a few terms](#terms)
- [Web Widget](#webwidget)
- [Zendesk Chat Widget](#zopimwidget)
- [Support SDK](#supportsdk)
- [Unity SDK](#unitysdk)
- [Chat SDK](#chatsdk)

---

## Defining a few terms

Here’s a list of the abbreviations or specific terms in this article.

- **Agent:** A person acting on behalf of the support manager, using Zendesk to handle support queries from end-user.
- **API:** Application programming interface.
- **App:** A piece of software designed to run on a device. In the context of this article, an app could run on the web or natively on the Android or iOS platform.
- **COPPA:** [Children's Online Privacy Protection Act](http://www.coppa.org).
- **End user:** The person using your service or website, and who might request support or browse your Help Center.
- **JSON:** JavaScript Object Notation, a lightweight data-interchange format.
- **JWT:** JSON Web Token, a method of authentication between Zendesk and your own user identity management/authentication service.
- **SDK:** Software development kit, designed to make it easier for you to build your application using Zendesk functionality.
- **UI:** User Interface, the visual element of your app, with which your end-user interacts.
- **Zendesk Chat:** The chat service by Zendesk, used for end-User to agent real time text chat.

---

## Web Widget (Classic)

Web Widget (Classic) enables you to embed Help Center search and articles, ticket creation, and live chat on your website.

There are two options that, when enabled, allow your end-users to contact you: contact form and chat. You can access these settings in your Zendesk in the [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410). [See Configuring the components in your widget.](https://support.zendesk.com/hc/en-us/articles/4408836216218#topic_j1f_4gd_bq)

**![](https://support.zendesk.com/hc/article_attachments/4408894706842/COPPA_1.png)**

Contact form option If you have the contact form option enabled, the end-user’s email address is a required field because it is the only way to respond. To avoid collecting the data of minors, you should not use the Web Widget for creating tickets. You should disable this option.

Chat option If you have the chat option enabled, the Web Widget will respect the settings you have configured in Zendesk Chat. See the next section about Zendesk Chat widget.

---

## Zendesk Chat Widget

The Zendesk Chat widget enables you to embed live chat on your website.

Pre-chat form and visitor profile By far, the easiest way to ensure that no personal information is collected is to disable the pre-chat form and visitor profile. When configured in this way, the Zendesk Chat widget does not ask for any information, but instead initiates an anonymous chat when the end-user clicks it.

To disable the pre-chat form and visitor profile, toggle both features off in their settings pages. See [Editing the pre-chat form](https://support.zendesk.com/hc/en-us/articles/4408882974234) and [Editing visitor profile settings](https://support.zendesk.com/hc/en-us/articles/4408887640730).

**![](https://support.zendesk.com/hc/article_attachments/4408894706458/COPPA_2.png)**

If you need to use the pre-chat form (eg. to set the correct department for the chat) then it is possible to make the identity not required. The option to provide the information is, however, still displayed to the end-user, and so may not be suitable for your COPPA compliance requirements. If the fields are filled in, the information will be stored.

If setting fields to simply ‘not required’ meets your unique needs, you can do so easily. To make these fields not required, in the [Pre-Chat Form settings](https://support.zendesk.com/hc/en-us/articles/203688996), ensure that the Require Identity option is deselected.

You can learn more about the Pre-Chat Form [here](https://support.zendesk.com/hc/en-us/articles/203688996-Using-the-Pre-Chat-form). You can learn more about the Visitor Profile [here](https://support.zendesk.com/hc/en-us/articles/216742068).

Offline messages When you are outside of your working hours, or you have no agents signed in, there is the option to accept offline messages. When enabled, this requires end-users to provide their name and email address.

Offline messages can be disabled if you do not wish to collect this kind of information. Instructions on how to manage offline messages are [here](https://support.zendesk.com/hc/en-us/articles/217295247), and you can disable them.

Chat transcript End-users have the option to request a copy of the chat transcript. To do this, they must supply their email address. This email address is not recorded against the end-user profile, and is used only to service the request for the transcript.

---

## Support SDK

The Support SDK enables you to add Help Center search and articles, ticket creation, and ticket update functionality into your Android and iOS apps.

When creating tickets, you might want to avoid collecting personal information. There are two authentication methods available when using the Support SDK, and both authentication types enable you to set some basic identifying parameters.

- **JWT authentication:** This enables you to identify end-users from your own database of users, and this information is required for the end-user to proceed. If using JWT authentication, email is a required piece of information.
- **Anonymous authentication:** This does not require details from the end-user, but will accept them if provided. If using anonymous authentication, it is possible to create an identity with no identifying information present.

Creating an identity without name or email You can find instructions in our developer documentation on how to update your code. Android instructions are [here](https://developer.zendesk.com/documentation/classic-web-widget-sdks/support-sdk/android/sdk_set_identity/#setting-an-anonymous-identity) and iOS instructions are [here](https://developer.zendesk.com/documentation/classic-web-widget-sdks/support-sdk/ios/sdk_set_identity/#setting-an-anonymous-identity). Both include code snippets.

Keeping your users informed If you do not collect your end-user’s email address, you will need a way to share ticket updates with them in your app. To do this using the Support SDK, ensure that the Conversations feature is enabled in your app settings in Zendesk.

To enable Conversations:

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4408838272410), click the **Channels**icon (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)) in the sidebar, then select **Classic > Mobile SDK**.
2. Click the app you want to update, then click the **Customization** tab.
3. Click the toggle next to Conversations to **On**, then click **Save**.

**![](https://support.zendesk.com/hc/article_attachments/4408894706074/COPPA_3.png)**

If you are using the Support SDK’s default UI with Conversations enabled, the ability to create, view, and update tickets is included in that UI already. If you are using providers ([Android](https://developer.zendesk.com/documentation/classic-web-widget-sdks/support-sdk/android/api_providers/), [iOS](https://developer.zendesk.com/documentation/classic-web-widget-sdks/support-sdk/ios/api_providers/)) and your own interface, make sure that you build your UI to include these features. This will avoid breaking communication lines with your end-users if you intend to reply.

For push notifications, the Zendesk service supports Urban Airship ([Android](https://developer.zendesk.com/documentation/classic-web-widget-sdks/support-sdk/android/handle_push_notifications_ua/), [iOS](https://developer.zendesk.com/documentation/classic-web-widget-sdks/support-sdk/ios/handle_push_notifications_ua/)) and the Webhook API ([Android](https://developer.zendesk.com/documentation/classic-web-widget-sdks/support-sdk/android/handle_push_notifications_wh/), [iOS](https://developer.zendesk.com/documentation/classic-web-widget-sdks/support-sdk/ios/handle_push_notifications_wh/)). You can set this up in the admin settings of your Zendesk (Admin > Support SDK > Your App > Customization > Push Notifications).

**![](https://support.zendesk.com/hc/article_attachments/4408889683098/COPPA_4.png)**

## Unity SDK

The Unity SDK has the same options mentioned above for the Support SDK. For more details on the authentication types and the support of conversations, see the [developer documentation](https://developer.zendesk.com/embeddables/docs/unity-native-sdk/overview).

---

## Chat SDK

The Chat SDK does not currently offer features for COPPA compliance.
# Adding and configuring the Apple Messages for Business channel

Source: https://support.zendesk.com/hc/en-us/articles/8030634178458-Adding-and-configuring-the-Apple-Messages-for-Business-channel

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Professional or Enterprise |

Verified AI summary ◀▼

Integrate Apple Messages for Business to connect with customers on Apple devices using live and AI agents. Register with Apple, meet subscription requirements, and configure the channel in the Admin Center. Utilize features like rich messages, quick replies, and Apple Pay to enhance interactions. Add a "Message Us" button to your site for easy access, and manage conversations effectively.

Adding Apple Messages for Business to your Zendesk configuration lets your end users
connect with both live and advanced AI agents through the Messages app on their Apple
devices. Apple Messages for Business is designed to allow businesses to provide rich,
engaging experiences in messaging to their customers on Apple devices, while protecting
user privacy and security.

This article includes the following sections:

- [Requirements for using Apple Messages for Business with Zendesk](#topic_nw4_gzn_5dc)
- [Understanding Apple Messages for Business](#topic_wkf_gzn_5dc)
- [Adding the Apple Messages for Business channel in the Admin Center](#topic_wlk_hzn_5dc)
- [Configuring the Apple Messages for Business channel](#topic_ww4_hzn_5dc)
- [Additional functionality with Apple Messages for Business](#topic_msw_hzn_5dc)

After the channel is configured, agents can [respond to Apple Message tickets in the Agent Workspace](https://support.zendesk.com/hc/en-us/articles/8661305451418).

## Requirements for using Apple Messages for Business with Zendesk

Apple Messages for Business requires all businesses to [register with Apple](https://register.apple.com/messages) before rolling out the Apple Messages for Business
channel. Apple maintains a rigorous process to ensure that all brands using Apple
Messages for Business provide high-quality conversational experiences. During the
implementation, you’ll need to complete a comprehensive onboarding process. You can
see the complete [end-to-end checklist of requirements here](https://register.apple.com/resources/messages/messaging-documentation/end-to-end).
See Apple’s [Getting Started with Apple Messages for
Business](https://register.apple.com/resources/messages/messaging-documentation/register-your-acct) page for more information.

To start the process, create an internal test account with Apple. After
completing the experience review, Apple converts the internal test account into a
commercial account in the Apple Business Register. You must submit brand
information, including addresses and logos, to Apple for approval. As part of this
process, you’re prompted to select a Messaging Service Provider. As a Messaging
Service Provider, Zendesk is certified by Apple to provide services and solutions
for your Apple Messages for Business needs. At the end of the registration process,
you’ll receive a unique Messages for Business ID that you can use to connect to Sunshine
Conversations.

In addition to Apple’s requirements, your Zendesk account must meet the following
requirements to use Apple Messages for Business:

- You must have a Zendesk Suite or Support Suite Professional, Enterprise, or
  Enterprise+ subscription with [messaging](https://support.zendesk.com/hc/en-us/articles/4408846454682) activated, or a Support
  standalone Professional or Enterprise subscription with Chat activated.
- You must be running an active [AI agent](https://support.zendesk.com/hc/en-us/articles/6970583409690) or [third-party bot](https://support.zendesk.com/hc/en-us/articles/5064149334426).
- You must have purchased a [Professional Services](https://www.zendesk.com/customer-experience/professional-services/) package.
  Contact your account executive or our [sales team](https://www.zendesk.com/contact/) for more information.

## Understanding Apple Messages for Business

With Apple Messages for Business, end-user requests submitted to your Zendesk account
through Apple Messages move through your messaging configuration and create a ticket
in the Agent Workspace (unless an advanced AI agent solves the request).

Live and advanced AI agents can view and respond to Apple Messages for Business
tickets in the Agent Workspace [like any other ticket](https://support.zendesk.com/hc/en-us/articles/4408843683226). In addition, there are rich
conversational features specific to Apple Messages for Business that agents can use to
build a more interactive customer experience.

Use the links in the table for more information from Apple about these features, and
see [Working with Apple Messages for Business in the
Agent Workspace](https://support.zendesk.com/hc/en-us/articles/8661305451418) for details on using them in customer interactions.

| Feature | Description | End-user experience example |
| --- | --- | --- |
| [Rich link messages](https://register.apple.com/resources/messages/msp-rest-api/type-richlink) | URLs sent by live or advanced AI agents are recognized and sent as rich links.  Target websites must use [OpenGraph tags](https://ogp.me/) for rich link messages to work correctly. |  |
| [Quick reply messages](https://register.apple.com/resources/messages/msp-rest-api/type-interactive#quick-reply-message.md) | Sends quick reply choices to the end user. Recommended for responses with 2-5 options. |  |
| [List picker message](https://register.apple.com/resources/messages/msp-rest-api/type-interactive#list-picker-message) | Allows single selection, multi-selection, and multi-selection with icons for sent and received list pickers and images. Recommended for responses with more than five options, when you want to provide more information with each option, or when you want to include images with options. |  |
| [Time picker message](https://register.apple.com/resources/messages/msp-rest-api/type-interactive#time-picker-message) | Sends time pickers and icons to the end user, allowing them to add the appointment to their calendar, view it on a map, and view calendar conflicts. |  |
| [Apple Pay message](https://register.apple.com/resources/messages/msp-rest-api/type-interactive#apple-pay-message) | Sends an Apple Pay payment request to the end user. |  |
| [Authentication message](https://register.apple.com/resources/messages/msp-rest-api/type-interactive#authentication-message) | Requests OAuth2 inline authentication from the end user. |  |
| [iMessage apps](https://register.apple.com/resources/messages/msp-rest-api/type-interactive#imessage-app) | Supports iMessage apps for advanced interactions in the conversation. |  |
| [Form message](https://register.apple.com/resources/messages/msp-rest-api/type-interactive#form-message) | Sends pre-defined forms to the end user. |  |
| [Construct payload API](https://register.apple.com/resources/messages/msp-rest-api/construct-payload) | Supports construct payload API for App Clips in rich link interactions. |  |

## Adding the Apple Messages for Business channel in the Admin Center

When your account meets the requirements described above, you can add the Apple
Messages for Business channel to your Zendesk account.

**To add the Apple Messages for Business channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click **Add channel** and select **Apple Messages for Business**.
3. On the Add Apple Messages for Business page, enter the
   following information:
   - **Channel name**: The name that appears in the
     channels list.
   - **Business ID**: Your Messages for Business account ID. You can get
     this ID in your Apple Business Register by going to **Messages for
     Business Account Links** > **Links** and copying the
     ID.

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/amb-apple_biz_page.png)
4. Click **Add channel**. The channel’s configuration page opens. You can [continue to configure the
   channel](#topic_ww4_hzn_5dc), or click **Save settings** to use it as-is or
   configure later.

   Without further configuration, incoming end-user requests
   from Apple Messages are routed to live or advanced AI agents as
   determined by your account setup.

## **Configuring the Apple Messages for Business channel**

An Apple Messages for Business channel’s settings page has the following
configuration tabs:

- [Configuring Apple Messages for Business basic settings](#topic_rp2_h2n_ydc)
- [Configuring auto-responder settings](#topic_qhj_h2n_ydc)
- [Configuring the Message Us button](#topic_xnn_h2n_ydc)

### Configuring Apple Messages for Business basic settings

The Basics tab includes the following fields:

- **Channel name** (editable): The name given to the
  channel.
- **Business ID** (view-only): The Messages for
  Business account ID.
- **OAuth secret** (editable): The [OAuth (or client)
  secret](../account-access/using-oauth-authentication-with-your-application.md#topic_ay4_2g1_gcc) created to verify authentication messages.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/amb-basics_tab-ac.png)

**To edit the Basics tab**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click the Apple Messages for Business channel you want to
   configure to open its settings page.
3. On the **Basics** tab, update the channel name or OAuth client
   secret.
4. Click **Save settings**.

### Configuring auto-responder settings

The Responses tab configures the auto-responder, which sends
messages automatically to an end user when you receive their messages. See [Sending automatic responses to social
messages](https://support.zendesk.com/hc/en-us/articles/4408838007578) for more detailed information on using and configuring the
auto-responder.

The tab also lists any [conversation bots](https://support.zendesk.com/hc/en-us/articles/7232810932250) added to the
Apple Messages for Business channel.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/amb-responses_tab-ac.png)

**To use the auto-responder for your Apple Messages for
Business channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click the Apple Messages for Business channel you want to
   configure to open its settings page.
3. Click the **Auto-responder** tab.
4. Click **Enable auto-responder**, then enter a message
   for your end users.
5. Click **Save settings**.

### Configuring the Message Us button

Adding a Message Us button to your website, mobile app, or help center
lets your end users discover and connect to your Apple Messages for Business
account.

To display a Message Us button, you’ll need to [configure the button’s visual
elements](#topic_xmy_sjn_ydc) and [add the
HTML code snippet](#topic_gfd_tjn_ydc) to each page on the website or mobile app where it
should be displayed.

#### Configuring visual elements

You can customize the appearance of the Message Us button
using Apple’s pre-approved options.

**To customize
the Message Us button**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click the Apple Messages for Business channel you want
   to configure to open its settings page.
3. Click the **Message Us button** tab.
4. Configure the following options:
   - **Language**: Use the dropdown menu to
     select the language your button is using.
   - **Style**: Use the dropdown menu to select
     one of Apple’s approved messages. The options in this
     menu are determined by the language selected above.
   - **Color**: Select **Dark** or
     **Light**:

     ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/amb-message_us-dark.png)![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/amb-message_us-light.png)
5. Click **Save settings**. You can now [add the Message Us
   button](#topic_gfd_tjn_ydc) to your website, mobile app, or help center.

#### Adding the Message Us button

After configuring the options above, you can add the code snippet
to your website, mobile app, or help center.

**To add the Message Us button to a website or mobile app**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click the Apple Messages for Business channel you want to
   configure to open its settings page.
3. Click the **Message Us button** tab.
4. Copy the code snippet to your clipboard.
5. On each page where the button should appear, paste the
   snippet into the HTML before the closing tag.

**To add the Message Us button to your help center**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click the Apple Messages for Business channel you want to
   configure to open its settings page.
3. Click the **Message Us button** tab.
4. Copy the code snippet to your clipboard.
5. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design**
   (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
6. On the theme you want to edit, click **Customize**, then
   click **Edit Code**.
7. In the **Templates** section, click the template you
   want to modify and add the snippet before the template’s closing
   tag.
8. Click **Save**.

## **Additional functionality with Apple Messages for Business**

When added to your Zendesk configuration, Apple Messages for Business
includes the following capabilities:

- [Creating rich messages](#topic_hx2_k2n_ydc)
- [Closing conversations](#topic_z2n_k2n_ydc)

### Creating rich messages

To build a rich experience for your end users, you can create [rich message templates](https://support.zendesk.com/hc/en-us/articles/8661305451418#topic_mtf_4b4_ydc) that your live
or advanced AI agents can send to the end user. You can create rich message
templates using [API](https://docs.smooch.io/rest/v1/#templates) or by installing the [Interactive Messaging Templates app](https://www.zendesk.com/marketplace/apps/support/966326/interactive-messaging-templates/) on
your Zendesk Suite Professional or higher account. This free app was developed
in partnership with Zendesk.

When the Interactive Messaging Templates app is installed, admins can
create a library of rich messages for Apple and any other channel, any agents
can use those rich messages right from within the ticket pane.

### Closing conversations

End users contacting you through Apple Messages for Business can choose to leave
the messaging conversation, which prevents live and advanced AI agents from
continuing the conversation in the Apple Messages for Business channel.

When an end user leaves a messaging conversation with a live agent:

- The messaging session ends.
- In the composer, the Apple Messages for Business channel option
  is deactivated for that conversation. Agents can’t respond to the end
  user in the messaging conversation.
- Agents can contact the end user through other available
  channels.
- Agents can add Internal notes to the related ticket.
- Agents can update the ticket status as needed.
- If the end user sends a reply in the conversation, a new ticket
  is created.

When an end user closes a conversation with an advanced AI agent:

- The advanced AI agent can’t send replies to the end user.
- If the end user sends another reply to the conversation a ticket is created
  in the Agent Workspace and assigned to a live agent or group based on your
  [routing configuration](https://support.zendesk.com/hc/en-us/articles/4408831658650).
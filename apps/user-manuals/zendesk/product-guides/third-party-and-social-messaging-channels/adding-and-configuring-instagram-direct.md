# Adding and configuring Instagram Direct

Source: https://support.zendesk.com/hc/en-us/articles/4408835013018-Adding-and-configuring-Instagram-Direct

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Social Messaging add-on |

Verified AI summary ◀▼

Add your Instagram Direct channel to manage direct messages and story interactions as tickets. Configure settings to control message responses, including auto-responders and a "Message Us" button for easy customer access. Note that replies must be made within the platform to sync with Instagram, and adhere to Instagram's response windows to ensure message delivery.

Location: Admin Center > Channels > Messaging and social > Messaging

Customers without Zendesk Suite must have Support and Chat with the Social Messaging add-on to use this feature.

You can add your business Instagram account to Zendesk so incoming Instagram direct messages and story replies become tickets. Tickets are not created for comments or replies on posts, reels, or other Instagram content.

Your agents can see and respond to these tickets in Zendesk like any other ticket. Agents must reply directly to the ticket in Support for replies to appear on both Zendesk and Instagram. Agent replies made directly within Instagram are not added to the Support ticket. See [Receiving and sending messages in the Zendesk Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408843683226).

This article contains the following topics:

- [Adding the Instagram Direct channel](#topic_yqd_dds_x4b)
- [Configuring the Instagram Direct channel](#topic_qsm_dds_x4b)

## Adding the Instagram Direct channel

The first step is to add Instagram Direct to your channels. Read on or watch the video below to learn more about the setup process.

Instagram setup flow (1:29)

**To add an Instagram Direct channel**

1. In the Instagram app, go to **Settings** > **Messages and story replies** > **Message controls** > **Connected tools** > **Allow access to messages**.
2. Under **Connected Tools**, toggle on **Allow access to messages**.

   Note: This step must be performed in the Instagram mobile app. It cannot be performed via Instagram Web.
3. Open your Zendesk admin account.
4. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png) **Channels** in the sidebar, then select **Messaging and social > Messaging**.
5. Click **Add channel** and select **Instagram Direct** from the drop-down.
6. Click **Continue with Instagram** to open the Instagram set-up flow.

   The set-up flow will ask you for the following information. Follow the instructions in the flow to add this information.

   | Action | Description |
   | --- | --- |
   | Authenticate to your Facebook profile | This is the admin profile linked to your company's Facebook Business Manager. You can **Continue** with the existing profile or sign in to another account. |
   | Provide permission to share your Instagram Account with Zendesk. | Zendesk needs this permission to connect your Instagram Professional Business Account to the Agent Workspace. |
   | Provide permission to share your Facebook Page(s) with Zendesk. | Zendesk needs this permission to connect your Instagram Professional Business Account to the Agent Workspace. We recommend that you select all pages. |
   | Accept the selected permissions | These permissions are needed to send and receive messages from Agent Workspace. |
7. When you've finished the set-up flow, click **Done**.
8. Select the Instagram channel you wish to connect from the drop-down, then click **Next**.
9. Assign a name to the new Instagram channel you are connecting, then click **Add channel**. Note that agents need to add comments to an Instagram message from within the Zendesk Agent Workspace.

   Note: Replies made directly in Instagram will not add a comment to the related ticket.

As with Facebook Messenger, Instagram Direct allows a business only seven days to respond to the end user before the messaging window closes. To prevent messages from being sent but not delivered, the composer will be blocked after the messaging window is closed. The only way to re-open is if the end user sends a new message.

Additionally, Instagram requires that you respond to an end user’s initial message within 24 hours, either by agent engagement, or with an automated message using the [auto-responder](https://support.zendesk.com/hc/en-us/articles/4408838007578) or [chatbot](https://developer.zendesk.com/documentation/custom-data/conversations/building-a-chatbot-integration-with-zendesk/#chatbots-for-messaging).

## Configuring the Instagram Direct channel

After you’ve added Instagram to your social messaging channels, you can configure how it appears and functions.

**To configure the Instagram Direct channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png) **Channels** in the sidebar, then select **Messaging and social > Messaging**.
2. Click the Instagram channel you want to configure to open its **Edit** page.
3. Update the information in the [Basics](#topic_c4b_fds_x4b), [Auto-responder](#topic_o4f_fds_x4b), and [Message Us button](#topic_dlk_fds_x4b) tabs, as described in the sections below.
4. Click **Save** after updating the information in each tab.

### The Basics tab

The Basics tab is populated with the channel and Instagram profile names.

**To edit the Basics tab**

1. Click in each text box to edit these names.
2. Click **Save** when you’re done.

If multiple brands are attached to your Zendesk account, you’ll also have a dropdown menu to select a brand to connect to the Instagram channel. You can only attach one brand to the channel. If your account has only one brand, this option does not appear under the Basics tab.

### The Auto-responder tab

The auto-responder sends messages automatically to an end user when you receive their messages. See [Sending automatic responses to social messages](https://support.zendesk.com/hc/en-us/articles/4408838007578) for more detailed information on using and configuring the auto-responder.

If you choose to use the auto-responder

1. Click **Enable auto-responder**, then enter a message for your customers.
2. Click **Save** when you’re done.

### The Message Us button tab

Adding a Message Us button to your website, mobile app, or help center allows customers to discover and connect to your Instagram account, where they can request and receive support via Instagram Direct.

If you choose to add a Message Us button, you’ll need to configure the following elements, then add the HTML code snippet to each page on the website or mobile app where it should be displayed.

#### Configurable options

As you make the selections below, a preview of the button is updated on the right side of the channel page.

- **Color**: Choose a gradient style for the button, **Dark gray** or **White**.
- **Size**: Select **Compact** or **Regular**.
- **Corner radius**: This number determines how rounded the button’s corners are. Enter a number from 0 (right angle) to 20 (near quarter-round).
- **Label**: Enter the text you want displayed on the button.
- **Width**: Enter the length you want your button (up to 400 pixels).

#### Adding the Message Us button

After you’ve configured the options above, you can add the code snippet to your website, mobile app, or help center.

**To add the Message Us button to a website or mobile app**

1. Copy the code snippet to your clipboard.
2. Paste the snippet into the HTML of every page that should include the button before the closing tag.

**To add the Message Us button to your help center**

1. In [Knowledge admin](https://support.zendesk.com/hc/en-us/articles/9041943683354#topic_b5q_nwn_s2c), click **Customize design** (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/guide_icon_customize.png)) in the sidebar.
2. On the theme you want to edit, click **Customize**, then click **Edit Code**.
3. In the **Templates** section, click the template you want to modify, and add the snippet before the template’s closing tag.
4. Click **Save**.
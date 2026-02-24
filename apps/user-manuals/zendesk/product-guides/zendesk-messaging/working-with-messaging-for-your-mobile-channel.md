# Working with messaging for your mobile channel

Source: https://support.zendesk.com/hc/en-us/articles/4408834810394-Working-with-messaging-for-your-mobile-channel

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

This article applies to Zendesk accounts using the messaging Web Widget. If you are using the classic Web Widget, see [Activating messaging when migrating from Web Widget (Classic)](https://support.zendesk.com/hc/en-us/articles/4408832031898).

You can provide messaging functionality on your mobile app through Android, iOS, and Unity SDKs. You can customize and configure an SDK's appearance and other settings in the Admin Center, then provide your developer with the Channel ID they will need to complete the integration following the [official developer documentation](https://developer.zendesk.com/documentation/zendesk-web-widget-sdks/).

This article includes the following topics:

- [Creating a new mobile channel for messaging](#topic_cbc_x1t_xnb)
- [Customizing and configuring the Zendesk mobile SDKs](#topic_kzg_ync_gnb)
- [Installing messaging on your mobile app](#topic_ig1_2sq_gnb)

## Creating a new mobile channel for messaging

Before configuring the Android, iOS, or Unity SDK, you'll need to create your mobile channel in the Zendesk Admin Center and then assign it to a brand before you can customize and configure it, as described below.

**To create a new Android/iOS channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click the **Add Channel** button, then select your channel:
   **Android**, **iOS**, or **Unity**.
3. On the Add Android/iOS/Unity SDK page, configure each of the sections:
   - **Start with the basics**: Enter a channel name. If your account has multiple brands, use the drop-down menu to select a brand.
     Click **Next**.
   - **Install in your app**: Copy the Channel ID that your development team can use to install the mobile SDK into your app. Use the provided link to view [detailed instructions](https://developer.zendesk.com/documentation/zendesk-web-widget-sdks/)
     for installing your selected SDK. Click **Next**.
   - **Make it your own**: Select a Primary color using the picker or by entering a hexadecimal number. Enter a channel title to display in the messaging header. You can refine these selections later in the configuration sections. Click **Next**.

     The channel's edit page opens, where you can continue [configuring your mobile SDK's appearance and messaging behavior](#topic_kzg_ync_gnb).

## Customizing and configuring the Zendesk mobile SDKs

Zendesk mobile SDKs include multiple components that you can customize to best represent your business. The settings described in this section are used to configure how messaging looks and behaves in your mobile app.

Note: You need to wait 10 minutes, then restart your mobile app for saved configuration changes to appear .

**To configure messaging for your mobile channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click the mobile channel you want to update.
3. Click the tab with the components you want to customize. Use the links below to view more detailed information on the options available on each tab:

   - [Basics](#topic_hw2_dsq_gnb)
     (channel name)
   - [Style](#topic_qsl_dsq_gnb)
     (SDK appearance)
   - [Responses](#topic_lth_sfv_ttb)(Business hours, first message, and AI agent activation)
   - [Notifications](#topic_ic5_dsq_gnb)
     (Push notification settings – Android and iOS only)
   - [Authentication](#topic_yq5_vfv_ttb)
     (Security settings)
   - [Installation](#topic_ig1_2sq_gnb)
     (Channel ID and help center embed)

### The Basics tab

The Basics tab includes an editable Channel name field.

The Channel name field is populated with the name used in the [initial channel setup](#topic_cbc_x1t_xnb). Update this name if needed to make it easy to identify in your channels list.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/mobile_sdk_basics_tab.png)

Click **Save** after making any updates.

### The Style tab

The Style tab includes the appearance-related components of the SDK.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/mobile_sdk_style_tab.png)

You can update the following:

- **Primary color**, the main color of the launcher button and SDK header. Enter a hexadecimal number, or click the color swatch to open a color picker.
- **Message color**, the color of the bubble around customer messages.
 Enter a hexadecimal number, or click the color swatch to open a color picker.
- **Action color**, the color of any buttons or tappable elements in the conversation, such as Quick Reply messages. Enter a hexadecimal number, or click the color swatch to open a color picker.
- **Title**, text which appears at the top of the SDK's conversation screen – usually your business or brand name.
- **Description** (optional) a short piece of text under the title.
 This can be information you want to share or a tagline, for example.
 Enter the description in the text box.

Click **Save** after making any updates.

### The Responses tab

The Responses tab allows you to customize the first message, which greets your customers when they initiate a messaging conversation in your mobile app. You can [apply a support schedule](https://support.zendesk.com/hc/en-us/articles/4408834810394-Working-with-messaging-in-your-Android-and-iOS-SDKs#topic_k4c_fgv_ttb) to create separate default responses for your working hours and [add an AI agent](https://support.zendesk.com/hc/en-us/articles/4408834810394-Working-with-messaging-in-your-Android-and-iOS-SDKs#topic_xyj_hgv_ttb).

#### **Applying Support schedules to the channel**

When you apply an established [Support schedule](https://support.zendesk.com/hc/en-us/articles/4408842938522) to your mobile channel, you can create different responses for customers based on whether they contact you during or outside of your set office hours. You can apply any of your Support schedules to the responses.

If you do not apply a Support schedule, customers receive the same response, regardless of the time or day they initiate a messaging conversation.

Note: Support schedules are not available on all Suite plans. If your plan does not offer schedules, you can use [out-of-office triggers](https://support.zendesk.com/hc/en-us/articles/4408842866074)
to manage basic responses.

**To apply a business hours schedule to your mobile channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click the name of the channel you want to edit. The Edit channel page opens.
3. Click the **Responses** tab.
4. Expand the **Business hours** section, and use the drop-down to select a saved Support schedule. If you have not created a Support schedule, you can skip this step.
5. Expand the **Response during business hours** section and update as described in [Customizing the default messaging response](#topic_gwp_fgv_ttb).
   Repeat for the **Response outside of business hours section**, if applicable.
6. Click **Save**.

If you remove the business hours schedule, the Response during business hours settings are applied.

#### **Customizing the default messaging response**

Whether you are using the business hours option or not, you can customize the response your customers receive when they launch a conversation.

**To customize your automated response**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click the name of the channel you want to edit. The Edit channel page opens.
3. Click the **Responses** tab.
4. Expand the **Response during business hours** section.
   The default messaging response information is displayed in the text boxes.
5. Update the following:

   - **First message**: Use the default message ("We're offline right now. Leave your details so we can get back to you later.”), or enter custom text that appears when a customer initiates a messaging conversation in your mobile app.
   - **Customer details**: Use the drop-down to select the information (Name and/or Email) you want to request from the customer before transferring them to an agent.
     Customers must enter information into these fields before being handed off to an agent.

     Note:
     These settings may be impacted by your [end-user authentication configuration](https://support.zendesk.com/hc/en-us/articles/4411666638746).
   - **Follow-up message**: Enter the text that appears after the customer submits the requested details.
6. If you're using business hours, expand the **Response outside of business hours** section and update the information as described in the previous step.
7. Click **Save**.

#### **Adding an AI agent**

At the bottom of the section, you have the option to add an AI agent to your messaging configuration, which allows you to offer highly customized and automated support to your customers.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/responses_ww_enable_bot.png)

See [Creating an AI agent for your web and mobile channels](https://support.zendesk.com/hc/en-us/articles/4408824263578).

If you have already created an AI agent, you have the option of deactivating it and returning to the default messaging response.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/responses_ww_disable_bot.png)

Note: When you delete an AI agent, any connected channels will revert to the [default response settings](https://support.zendesk.com/hc/en-us/articles/4500737327258-Configuring-messaging-responses-for-web-and-mobile-channels#topic_kzg_ync_gnb)
configured above.

### The Notifications tab (Android and iOS only)

The Notifications tab is where you can set up push notifications for the Zendesk Android or iOS SDK.

The required steps for configuring Android and iOS notifications differ. Choose the procedure below that matches your setup.

**To configure push notifications for your Android channel**

First, create your service account key JSON file which contains your credentials needed for the next steps.

1. In the [Firebase console](https://console.firebase.google.com/), create a new project if you do not already have one.
2. Click **Settings > Service Accounts**.
3. Click **Generate New Private Key**, then confirm by clicking **Generate Key**.
4. Save the JSON file to a secure location.

In most migration scenarios, the Firebase Cloud Messaging (FCM) v1 API is enabled by default. If you encounter errors when trying to contact the endpoint, ensure that **Firebase Cloud Messaging API** is enabled in the list of APIs and services within the [Google Cloud console](https://console.developers.google.com/apis/dashboard?project=_).

Now configure the notifications in Admin Center.

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click the name of the channel you want to edit. The Edit channel page opens.
3. Click the **Notifications** tab.
4. Enter the following information using the contents of the service account key JSON file you downloaded above:
   1. **project ID**: A unique identifier for your Firebase project.
   2. **Private key**: A key that Firebase uses for server-to-server communication.
   3. **client email**: The client email address (also called a service account email) associated with the Firebase project.
5. Click **Save**.
6. Complete the steps described in the Zendesk Developers guide for [setting up push notifications for Android](https://developer.zendesk.com/documentation/zendesk-web-widget-sdks/sdks/android/push_notifications/).

To configure push notifications for your iOS channel, you'll need an Apple developer account and a .p12 file from APNs. If you already have these, you can skip to configuring push notifications for your iOS channel.

To create an Apple developer account, enroll [here](https://developer.apple.com/programs/enroll/).

After you're enrolled, you can generate the .p12 file using these instructions from the Apple developer website.

**To generate a .p12 file**

1. Log in to the Apple Developer Member Center and navigate to the [certificates list](https://developer.apple.com/account/resources/certificates/list).
2. Click the + button at the top of the page to create a new certificate, and select Apple Push Notification service SSL (Sandbox & Production).
3. Select your app ID from the drop-down and click continue.
4. Follow the instructions to generate a Certificate Signing Request (CSR) using Keychain Access, and upload it to generate your certificate.
5. Once the certificate is ready, download it to your computer and double-click it to open it in Keychain Access.
6. Right-click the certificate you created, and select Export "Apple Push Services:
   {your-app-id}."
7. Choose a password and save the .p12 file to your computer.

Now, you're ready to configure your push notifications.

**To configure push notifications for your iOS channel**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click the name of the channel you want to edit. The Edit channel page opens.
3. Click the **Notifications** tab.
4. Upload the .p12 file from APNs and enter the certificate password.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/mobile_sdk_iOS_notifications_tab.png)
5. Click **Save**.
6. Complete the steps described in the Zendesk Developers guide for [setting up push notifications for iOS](https://developer.zendesk.com/documentation/zendesk-web-widget-sdks/sdks/ios/push_notifications/).

### The Authentication section

See [Authenticating end users in messaging](https://support.zendesk.com/hc/en-us/articles/4411666638746).

## Installing messaging on your mobile app

To install messaging on your mobile app, your you'll need to give your developers a Channel key. You can find the Channel key, along with a link to the Zendesk developer documentation, in the Installation section.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/mobile_sdk_installation_tab.png)

**To obtain the Channel ID**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Hover your cursor over the brand you want to update, click the options icon (
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ticket_field_options_icon.png)), then click **Edit**.
3. Click the **Installation** section.
4. Under **Channel ID**, click the **Copy** button to save the key to your clipboard.
5. Send this information to your developers.
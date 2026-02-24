# Using the Google Play integration

Source: https://support.zendesk.com/hc/en-us/articles/4408828952602-Using-the-Google-Play-integration

---

Zendesk has an integration to transform Google Play Store reviews into Zendesk Support tickets, allowing Google Play developers to respond to reviews through the Zendesk Support platform. The Zendesk Google Play integration can fetch up to 200 reviews every two minutes (or 6,000 per hour). If your Play Store app receives more than 200 reviews in a two-minute window, only the first 200 are fetched. Moreover, agents can reply 500 times per day by default. This is due to limitations in the Google Play Store API.

Note: You can only synchronize Google Play reviews with Zendesk that were created after you set up the integration.

When responding to a Google Play review, the character reply limit is 350 characters. If that limit is exceeded, Zendesk automatically truncates the message to 350 characters.

This article covers the following topics:

- [Installing the Zendesk Google Play integration](#topic_nm2_hsm_sv)
- [Setting up your Google Play account and app](#topic_nbv_hsm_sv)
- [Completing your Google Play integration](#topic_olv_wln_sv)

For general information on channels, see [About Zendesk channels](https://support.zendesk.com/hc/en-us/articles/4408824097050).

Note: When an agent responds to a ticket via Google Play, their agent signature is not applied.
Manually add any important information in the signature to the agent's comment.

## Installing the Zendesk Google Play integration

To use the Google Play integration, you'll need to install the app from the Zendesk Marketplace. When the installation is complete, the app is added to the My Apps section of your Zendesk Support apps page in Admin Center.

**To install the Google Play integration**

1. Go to the [Google Play Reviews](https://www.zendesk.com/marketplace/apps/support/86800/google-play-reviews/) app in the Zendesk App Marketplace.
2. Read the description, then click **Install**.
3. If prompted, select the Zendesk account to install the app, then click **Install**.
4. View or edit the installation information if needed, then click **Install**.

## Setting up your Google Play account and app

After you have installed the Google Play integration, you'll need the following to connect it to Zendesk Support:

- A [Google Play Developer account](https://support.google.com/googleplay/android-developer/answer/6112435?hl=en).
- An app you created and published in the Google Play app store. For information on app development, see [Android for Developers](https://developer.android.com/).

Once your app is published, you need to:

- Configure your account and the app
- Upload the JSON file provided

This section includes basic instructions on performing these tasks.

**To configure your Service Account**

1. Navigate to the [Google Cloud Console](https://console.cloud.google.com/iam-admin/serviceaccounts).
2. Select an existing project or use the following steps to create a new one:
   1. Click **CREATE PROJECT**.
   2. On the New Project page, enter the app name under **Project name**.
   3. Select a **Location**.
   4. Click **CREATE**. You are redirected to the Service Accounts page.
3. Click **+ CREATE SERVICE ACCOUNT**.
4. Choose a name for your Service Account, then click **CREATE AND CONTINUE**.
5. Click the **Role** drop-down menu and select **Owner**.
6. Click **Continue**, then click **Done**. You are redirected to the Service Accounts page.
7. Search for the newly created Service Account in the search text box and click the link in the Email column.
8. Click the **Keys** tab > **ADD KEY** > **Create new key**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/google_play_create_account.png)
9. Select **JSON** as the Key Type, then click **Create**. A JSON file downloads to your device.

**To configure your Google Play app**

1. Navigate to the [Google Play Console](https://play.google.com/console).
2. Click **Users and permissions** in the left sidebar.
3. Click **Invite new users**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/google_play_configure_app.png)
4. In the **User details** field on the Invite user page, enter the email address of the newly created Service Account and set an access expiry date.
5. Under the Permissions section, click **Add app** and select the app to grant the Service Account user permission, then click **Apply**.
6. You are presented with a list of permissions you can grant your user. Different permissions will be automatically selected depending on the role you choose. We recommend keeping the default permissions for the selected role, making sure the **Reply to reviews** permission is selected.
7. Click **Apply**, then click **Invite User**.

## Completing your Google Play integration

Now that you have your Google Play app and account configured, return to your Zendesk Support admin page and finish configuring your integration.

**To configure your Google Play integration**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click
   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_apps_integrations_icon.png)
   **Apps and integrations** in the sidebar, then select **Apps > Channel apps**.
2. Click the **Google Play** integration link.
3. Click the **Accounts** tab.
4. Click **Add account**.
5. In the **App Name** field, give your account a name (it can be any name).
6. In the **App ID** field, enter the ID for your app, which can be found in the Google Play Developer Console.
7. Upload the JSON file downloaded when you created your Service Account.
8. Click **Save Changes**.
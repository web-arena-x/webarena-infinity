# Publish Drawings

Source: https://v2.support.procore.com/product-manuals/drawings-project/tutorials/publish-drawings

---

## Background

After drawings have been uploaded and reviewed, they will be in âunpublishedâ status until they are published. Unpublished drawings are only visible to Drawings tool 'Admin' users, and do not update the Current Drawings. Additionally, drawings will not be visible on mobile devices until they have been published. After drawings have been published, they will be viewable to all users with access to the project's Drawings tool.

## Things to Consider

- **Required User Permissions:**

 - 'Admin' permissions on the Drawings tool.
- **Prerequisites:**

 1. [Upload Drawings](/process-guides/user-guide-bidding-and-estimating-integration/upload-drawings)
 2. [Review Drawings](/process-guides/user-guide-bidding-and-estimating-integration/review-and-confirm-drawings)
- **Additional Information:**

 - Drawings can be left unpublished for internal review, subcontractor pricing, or to restrict access to only Drawings tool 'Admin' users.
 - Publishing a newer revision of an obsolete drawing makes it current, while publishing an older revision of an obsolete drawing during backfilling keeps it obsolete.
 - [Drawing log subscribers](/product-manuals/drawings-project/tutorials/subscribe-to-the-drawings-log) : Upon publication and distribution, drawings trigger email notifications for drawing log subscribers and push notifications for enabled mobile users. See [Enable Push Notifications for Drawings (iOS)](/product-manuals/drawings-ios/tutorials/enable-push-notifications-for-drawings-ios) and [Manage Project Settings (Android)](/process-guides/getting-started-procore-app-android/manage-project-settings).

    - ***Important*****!** Subscribed users only receive notifications for published and distributed drawings; the publisher must select "Publish & Distribute" rather than "Publish." See [Who receives a notification for updates in the Drawings tool?](/faq-who-receives-a-notification-for-updates-in-the-drawings-tool)

##### Note

When projects are connected via the [Connection Manager](/product-manuals/connection-manager-project/) tool, any Drawings published in the upstream project will automatically copy to the downstream project. See [User Guide: Procore Connect for Drawings](/process-guides/user-guide-procore-connect-for-drawings/).

## Steps

After the results of auto-labeling/OCR are confirmed on a new drawing upload, the drawings will have an âunpublishedâ status until they are published. You will notice the following banner in the list page.

1. Navigate to the **Drawings** tool.
2. Click into the drawing set that contains the uploaded drawings.
3. Click the **Publish** drop-down menu in the banner above the list.
4. Click one of the following options:

   - Click **Publish & Distribute** to publish the drawings and send a notification email and push notification to drawings log subscribers.
   - Click **Publish** to publish the drawings without sending a notification email to drawings log subscribers.
5. All of the drawings in the upload will be published and available to the team on mobile devices and on the web.
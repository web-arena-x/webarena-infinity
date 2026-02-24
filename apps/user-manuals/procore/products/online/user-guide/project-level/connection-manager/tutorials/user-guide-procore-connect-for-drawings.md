# User Guide: Procore Connect for Drawings - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/connection-manager/tutorials/user-guide-procore-connect-for-drawings

---

Table of Contents

**Table of Contents**

- Welcome 
  - [Overview](https://support.procore.com/#)
  - [Considerations](https://support.procore.com/#)
  - [Permissions](https://support.procore.com/#)
- Upstream Account 
  - [Set Connection Approval Preference](https://support.procore.com/#)
  - [Approve or Reject Connections (if review is required)](https://support.procore.com/#)
  - [Publish Drawings to your Upstream Project](https://support.procore.com/#)
- Downstream Account 
  - [Initiate a Project Connection](https://support.procore.com/#)
  - [Publish Drawings to your Downstream Project](https://support.procore.com/#)
- [Frequently Asked Questions](https://support.procore.com/#)
- [Conclusion](https://support.procore.com/#)

## Overview

Procore Connect for Drawings enables Procore customers to connect their projects so that drawings can be copied and kept in sync with the upstream project. The connection is one-way and copies published drawings from an upstream source project to a downstream connected project.

Learn more about [Procore Connect in Procore.](https://www.procore.com/platform/connect "https://www.procore.com/platform/connect")

Why connect projects?

When projects are connected, drawings are easily shared with collaborators working on your project. This eliminates silos and reduces duplicate data entry. Some of the key benefits include:

- Automatically sharing published drawings with downstream collaborators.
- Eliminating the need for downstream collaborators to download drawings and re-upload them into their own projects for their teams to access.
- Downstream collaborators are automatically notified when new drawings or revisions are published in the upstream account, and are available to review and publish.
- Drawings titles and metadata are kept in sync with the upstream account, ensuring a single source of truth and reducing the likelihood of potential mistakes.
- Connected data is retained in the downstream company's account for record keeping and reporting.

Downstream permissions requirements to connect projects are comparable to how upstream accounts currently allow collaborators to access drawing information. The upstream account is always notified about new connections and can disconnect projects if needed.

### How does it work?

|  |  |
| --- | --- |
| clipboard_e2ea98eb2648ecdb6a85666d5cc5adfa7.png | Project connections are always initiated by the downstream project.  The connection depends on the upstream company's approval preference. If review is not required, the projects will be automatically connected. If review is required, a connection request will be sent to the upstream company to review and manually approve or reject.  As the upstream project uploads and publishes drawings, those drawings are copied to the downstream project. The drawings are copied in an unpublished state for the downstream project to review and publish in their project.  After the drawings are published in the downstream company's project, users with access to the downstream project's drawings tool can view the connected drawings that originated from the upstream company's project |

## Considerations

- Projects with more than 100,000 drawing revisions can not be connected.
- Project connections can only be initiated by the downstream project.
- A downstream project can only connect to one upstream project. However, note that an upstream project can support multiple downstream connections.
- A downstream project in a connection cannot act as an upstream project in a different connection.
- Markups from the upstream project’s drawings are not copied to the downstream project.
- Custom fields are not included when copied from the upstream project.
- Connections can only be made with ‘active’ projects. Inactive projects are not supported.
- GovCloud accounts will not be able to participate in a project connection.
- Drawings only sync one-way from an upstream project to a downstream project. It is not possible for the downstream project to upload drawings to a connected drawing set.
- If projects are disconnected, they cannot be reconnected.
- If projects are disconnected, the downstream project can not connect to a new upstream project.

## Permissions

Learn which user permissions are required to take the described actions in this tool.

##### Important

Some actions that impact this tool are done in other Procore tools. See the [User Permissions Matrix](../../../../../../references/user-permissions-matrix-web.md) for the full list of actions taken in all other tools.

| | The action is available on Procore's Web, iOS, and/or Android application. Click to view the article.

![icon-mindtouch-table-check.png](https://support.procore.com/@api/deki/files/91423/icon-mindtouch-table-check.png?revision=3&size=bestfit&width=18&height=18) Users can take the action with this permission level.

![icon-mindtouch-table-check.png](https://support.procore.com/@api/deki/files/407609/icon-mindtouch-table-check-gp.png?revision=1&size=bestfit&width=18&height=18) Users can take this action with this permission level AND one or more additional requirements, like [granular permissions](https://support.procore.com/products/online/user-guide/company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template "Grant Granular Permissions in a Project Permissions Template").

| Action | None | Read Only | Standard | Admin | Notes |
| --- | --- | --- | --- | --- | --- |
| Approve or Reject Project Connection Request  [Web](#s214828 "Approve or Reject Project Connection Request") |  |  |  | check-green2.png |  |
| Configure Advanced Settings  [Web](https://support.procore.com/products/online/user-guide/project-level/connection-manager/tutorials/configure-advanced-settings-connection-manager "Configure Advanced Settings: Connection Manager") |  |  |  | check-green2.png |  |
| Disconnect a Connected Project  [Web](https://support.procore.com/products/online/user-guide/project-level/connection-manager/tutorials/disconnect-a-connected-project "Disconnect a Connected Project") |  |  |  | check-green2.png |  |
| Initiate a Request to Connect Projects  [Web](#s214831 "Initiate a Project Connection") |  |  |  | icon-mindtouch-table-check.png | Users must also have ‘Read only’ level permissions or higher to the Drawings tool in both the upstream and downstream projects. |
| View Project Connections  [Web](https://support.procore.com/products/online/user-guide/project-level/connection-manager/tutorials/view-project-connections "View Project Connections") |  | check-green2.png | check-green2.png | check-green2.png |  |

## Set Connection Approval Preference

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings,' click **Connection Manager**.
3. To automatically approve connections, mark the checkbox to 'Allow users with existing access to the Drawings tool to connect their project without Admin approval. (Recommended)'.  
   OR  
   Clear the checkmark to require a connection request be sent for review before manually accepting or rejecting a project's request to connect.
4. Click **Save**.

## Approve or Reject Connections (if review is required)

## Objective

To approve or reject requests to connect projects using the project's Connection Manager tool.

## Background

Procore Connect enables a connection between two separate Procore projects. The connection is one-way and copies published data from an upstream source project to a downstream connected project in an unpublished state.

Upstream company accounts can choose to automatically approve connections, or require review to manually accept or reject a downstream project's request to connect. See [Configure Connection Approval Settings](#s204050 "Configure Project Connection Settings"). Follow these steps if you chose to review and manually accept each connection.

## Things to Consider

- [Required User Permissions](#s203903 "Connection Manager - Permissions")
- If you reject a request by mistake, the project can request a connection again that you can review and approve.
- An upstream project can support connections with multiple downstream projects. For example, multiple subcontractor companies (downstream) projects can connect to a single general contractor (upstream) project and receive data.
- For both upstream and downstream accounts, users on the Connection Manager tool email distribution list are notified of new connections, disconnections, and connection requests (if review is required). See [Connection Manager: Configure Advanced Settings](https://support.procore.com/products/online/user-guide/project-level/connection-manager/tutorials/configure-advanced-settings-connection-manager "Configure Advanced Settings: Connection Manager").
- Projects can be disconnected by the upstream or downstream account at any time. See [Disconnect Connected Projects](https://support.procore.com/products/online/user-guide/project-level/connection-manager/tutorials/disconnect-a-connected-project "Disconnect a Connected Project").

## Steps

1. Navigate to the project's **Connection Manager** tool.
2. Under 'Downstream Projects' click **Review Request**.
3. Click **Approve** to approve the connection.  
   OR  
   Click **Reject** to decline the connection.

## See Also

- [Configure Connection Approval Settings](#s204050 "Configure Project Connection Settings")

## Publish Drawings to your Upstream Project

When projects are connected, any published drawings in your upstream project are automatically copied to the downstream project. Just follow the standard steps in your project to:

1. [Upload Drawings](../../drawings/tutorials/upload-drawings.md#Steps "Upload Drawings")
2. [Review and Confirm Drawings](../../drawings/tutorials/review-and-confirm-drawings.md#Steps "Review and Confirm Drawings")
3. [Publish Drawings](../../drawings/tutorials/publish-drawings.md#Steps "Publish Drawings")

## Initiate a Project Connection

1. Navigate to the project's **Connection Manager** tool.
2. Click **Connect**.
3. Select the upstream company and project.  
   *Note:* If you are connecting to a project within the *same* company, look for the 'Current Company' section in the 'Upstream Company' dropdown to select your company's name.
4. Click **Next**.
5. Select at least one feature for this connection, then click **Next**.
6. Review the Considerations, then click **Connect Projects** to initiate the project connection.

If the upstream company chose to automatically approve connections, your projects automatically connect. If the upstream company's settings require manual review for accepting or rejecting connections, Procore sends a request to the upstream company for review.

## Publish Drawings to your Downstream Project

After the drawings are copied from the upstream project, they will have an "unpublished" status until they are published by the downstream project.

1. Navigate to the **Drawings** tool.
2. Select the **Drawing Sets** tab.
3. Select the drawings you want to publish:

   - **Option 1.** To publish multiple drawings sets in bulk:

     1. Mark the checkboxes next to each drawing set that contains new drawings you want to publish, or mark the root checkbox to select all drawing sets.
     2. Click one of the following options:

        - Click **Publish and Distribute** to publish the drawings and send a notification to drawings log subscribers. See [Who receives a notification for updates in the Drawing tool?](https://support.procore.com/faq/who-receives-a-notification-for-updates-in-the-drawings-tool "Who receives a notification for updates in the Drawings tool?")
        - Click **Publish** to publish the drawings without sending a notification to drawings log subscribers.  
            
          ![bulk-publish-connected.png](https://support.procore.com/@api/deki/files/477324/bulk-publish-connected.png?revision=1)
   - **Option 2.** To publish all drawings in a single drawing set:

     1. Click **View** next to the drawing set that contains the new drawings.
     2. Click the **Publish** drop-down menu in the banner above the list and select one of the following options:

        - Click **Publish and Distribute** to publish the drawings and send a notification to drawings log subscribers. See [Who receives a notification for updates in the Drawing tool?](https://support.procore.com/faq/who-receives-a-notification-for-updates-in-the-drawings-tool "Who receives a notification for updates in the Drawings tool?")
        - Click **Publish** to publish the drawings without sending a notification to drawings log subscribers.  
            
          ![publish-drawings.png](https://support.procore.com/@api/deki/files/45166/publish-drawings.png?revision=2)
   - **Option 3.** To publish some drawings in a single drawing set:

     1. Click **View** next to the drawing set that contains the new drawings.
     2. Mark the checkboxes next to each drawing or division of drawings that you want to publish, or mark the root checkbox to select all drawings.
     3. Click one of the following options:

        - Click **Publish and Distribute Selected** to publish the drawings and send a notification to drawings log subscribers. See [Who receives a notification for updates in the Drawing tool?](https://support.procore.com/faq/who-receives-a-notification-for-updates-in-the-drawings-tool "Who receives a notification for updates in the Drawings tool?")
        - Click **Publish Selected** to publish the drawings without sending a notification to drawings log subscribers.  
            
          ![publish-selected-drawings.png](https://support.procore.com/@api/deki/files/477323/publish-selected-drawings.png?revision=1)

Published connected drawings will be available to users with 'Read Only' level permissions or higher to the Drawings tool.

## Frequently Asked Questions

###### What Drawing Information is Copied to the downstream Project?

Here is some of the information that is copied:

- Drawings, without markup
- Drawing number, title, and obsolete status
- Drawing area name and description
- Drawing discipline name and position
- Drawing date and received date
- Revision number and status
- Drawing set date and name

##### Note

- Custom fields are not included in the metadata copy from the upstream project to the downstream project.
- Connect drawing metadata can not be modified by the downstream project.

###### Is Markup supported?

Markups made in upstream drawings are not copied to the drawings in the downstream project. However, as the downstream project, you can add additional markup to the connected drawings. These markups will remain in your project and will not be copied or published back to the upstream project. Markups added by the downstream project on a connected drawing are retained when a new version of the drawing is added by the upstream project.

###### What happens when the upstream project deletes a Drawing or Drawing Area?

If the upstream project deletes a drawing, the deleted drawing will be removed from the Drawings log page in the downstream company. Drawing areas will remain but without the deleted drawing. Drawing Admins in the downstream project can view deleted drawings in the 'Deleted Drawing Revisions' report in the downstream project’s Drawings tool.

###### Can I choose which Drawings & Drawing Areas get copied to the downstream project?

No. All published drawings and drawing areas in the project are copied and kept in sync with the upstream project. This is a limitation of the Beta.

###### How long does it take for Drawings to copy?

Copying drawings to the downstream project can take up to one hour. You will receive an email notification once the drawings have been successfully copied and are ready to review and publish.

###### Can I review connected Drawings and Revisions before publishing them in my project for my team to access?

Yes, when drawings and revisions are copied to your downstream project, they are an unpublished state. A user with ‘Admin’ permissions on the Drawings tool can review the drawings before publishing them to your team.

###### Who is notified when drawings are copied?

You can select who is notified when unpublished drawings are copied, and ready to be reviewed and published to your project. Notifications are managed in the Settings of the Drawings tool. See [Configure Advanced Settings: Drawings](../../drawings/tutorials/configure-advanced-settings-drawings.md#Connected_Project "Configure Advanced Settings: Drawings").

###### Can I distinguish between my Drawings and Connected Drawings?

Yes. You will see a ****connected****![]() icon indicating which drawings have been copied from the upstream project.

###### Will my field team be able to see Connected Drawings on the Procore mobile app?

Yes. The mobile app shows the connected drawings and will have the ****connected****![]() icon to distinguish them.

###### Can I add Drawings to a Connected Drawing Area?

No, you cannot add your drawings to a connected Drawing Area. However, you may add your own Drawing Areas and drawings to any 'unconnected' Drawing Area in your account. These will not sync to the upstream project.

###### Can I delete Connected Drawings from a downstream project?

No. At this time connected drawings can't be deleted from a downstream project.

## Conclusion

Thank you for using the Procore Connect for Drawings beta. Please provide feedback through the **Share Feedback** button in the Connection Manager tool, and via the surveys sent by Procore.
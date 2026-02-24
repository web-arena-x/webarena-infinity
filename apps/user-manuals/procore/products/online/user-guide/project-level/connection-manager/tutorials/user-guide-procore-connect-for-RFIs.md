# User Guide: Procore Connect for RFIs - Procore

Source: https://support.procore.com/products/online/user-guide/project-level/connection-manager/tutorials/user-guide-procore-connect-for-RFIs

---

Table of Contents

**Table of Contents**

- Welcome 
 - [Overview](https://support.procore.com/#)
 - [Considerations](https://support.procore.com/#)
 - [Permissions](https://support.procore.com/#)
- Upstream Account 
 - [Set Connection Approval Preferences](https://support.procore.com/#)
 - [Approve or Reject Connections (if review is required)](https://support.procore.com/#)
 - [Close an RFI](https://support.procore.com/#)
- Downstream Account 
 - [Initiate a Project Connection](https://support.procore.com/#)
 - [View External RFIs on a Downstream Project](https://support.procore.com/#)
 - [Linking Internal and External RFIs](https://support.procore.com/#)
 - [Create an External RFI 360 Report](https://support.procore.com/#)
- [Frequently Asked Questions](https://support.procore.com/#)
- [Conclusion](https://support.procore.com/#)

## Overview

Procore Connect for RFIs enables Procore customers to connect their projects so that non-private RFIs can be copied and kept in sync with the upstream project. The connection is one-way and copies closed RFIs from an upstream source project to a downstream connected project.

### Benefits

- **Eliminate Manual Work**: Ensures all stakeholders have copies of finalized RFIs.
- **Improved Visibility**: Read-only copies of closed RFIs can be searched, exported to PDF, and included in reports.
- **Secure & Permanent Access**: Once copied, RFIs remain accessible even if the connection is later severed.

### How it Works

![connection-manager-workflow-rfis-edit.png](https://support.procore.com/@api/deki/files/553557/connection-manager-workflow-rfis-edit.png?revision=1)

### Connection Information

- **Initiation**: Downstream customers (typically Subcontractors, Owners, or GCs within Owner projects) initiate a connection via the Connection Manager in their project.
- **Connections**: Upstream projects allow unlimited downstream connections, while downstream projects are limited to a single upstream connection.
- **Previously Closed RFIs**: Upon connection, all closed RFIs will be synced with the downstream project.
- **Connection Severed**: If the upstream project severs the connection, previously copied RFIs remain in your project permanently.

### Connected RFI Details

- **Read-Only**: Connected RFIs are read-only and cannot be edited in Downstream projects. These appear in the RFI tool as External RFIs.
- **Included Data**: The following fields are included: Subject, Question & Attachment(s), Responses & Attachment(s), RFI Number, Responsible Contractor, Status, RFI Manager, Received From, Date Initiated, Due Date, Private, Coversheet (PDF), and Linked Drawings (PDF).
- **Copied RFIs**: All closed RFIs are copied across accounts.
- **Status Updates**: If a closed RFI in the Upstream project is reopened or deleted, the status update will reflect in the Downstream External RFIs.
- **Access**: External RFIs are accessed via a new "External Items" tab in the RFI tool. RFI administrators and users with the new "View External Items" granular permission can view them. Users do not need permissions in the Upstream project.

## Considerations

- No change to RFI creation process.
- No new custom notifications for External RFIs.
- Not currently supported:
 - Private RFIs
 - Mobile access to External  RFIs
 - Procore Document Management (PDM) attachments (not to be confused with legacy Documents tool. [Learn more](https://en-gb.support.procore.com/faq/what-is-the-difference-between-the-documents-and-document-management-tools-in-procore))
- A downstream project in a connection cannot act as an upstream project in a different connection.
- Project connections can only be initiated by the downstream project.
- Connections can only be made with ‘active’ projects. Inactive projects are not supported.
- GovCloud accounts will not be able to participate in a project connection.
- If projects are disconnected, they cannot be reconnected.
- If projects are disconnected, the downstream project can not connect to a new upstream project.

## Permissions

## 

Learn which user permissions are required to take the described actions in this tool.

##### Important

Some actions that impact the Connection Manager tool are performed in other Procore tools. All permissions listed refer to the Connection Manager unless stated otherwise. For a complete list of actions and permissions across all tools, refer to the [User Permissions Matrix](https://support.procore.com/references/user-permissions-matrix-web "User Permissions Matrix - Web").

| | The action is available on Procore's Web, iOS, and/or Android application. Click to view the article.

![icon-mindtouch-table-check.png](https://support.procore.com/@api/deki/files/91423/icon-mindtouch-table-check.png?revision=3&size=bestfit&width=18&height=18) Users can take the action with this permission level.

![icon-mindtouch-table-check.png](https://support.procore.com/@api/deki/files/407609/icon-mindtouch-table-check-gp.png?revision=1&size=bestfit&width=18&height=18) Users can take this action with this permission level AND one or more additional requirements, like [granular permissions](https://support.procore.com/products/online/user-guide/company-level/permissions/tutorials/grant-granular-permissions-in-a-project-permissions-template "Grant Granular Permissions in a Project Permissions Template").

| Action | None | Read Only | Standard | Admin | Notes |
| --- | --- | --- | --- | --- | --- |
| Approve or Reject Project Connection Request [Web](#s214828 "Approve or Reject Project Connection Request") | | | | check-green2.png | |
| Configure Advanced Settings [Web](https://support.procore.com/products/online/user-guide/project-level/connection-manager/tutorials/configure-advanced-settings-connection-manager "Configure Advanced Settings: Connection Manager") | | | | check-green2.png | |
| Disconnect a Connected Project [Web](https://support.procore.com/products/online/user-guide/project-level/connection-manager/tutorials/disconnect-a-connected-project "Disconnect a Connected Project") | | | | check-green2.png | |
| Initiate a Request to Connect Projects [Web](#s214831 "Initiate a Project Connection") | | | | icon-mindtouch-table-check.png | Users must also have ‘Read only’ level permissions or higher to the RFI tool in both the upstream and downstream projects. |
| View Project Connections [Web](https://support.procore.com/products/online/user-guide/project-level/connection-manager/tutorials/view-project-connections "View Project Connections") | | check-green2.png | check-green2.png | check-green2.png | |
| View External RFIs on a Downstream Project [Web](#s258036 "View External RFIs on a Downstream Project") | | check-green2.png + View External Items | check-green2.png + View External Items | check-green2.png | Users with Read Only or Standard permissions to the RFI tool must also have the ‘View External Items’ granular permission for RFIs to view connected RFIs. |

## Set Connection Approval Preferences

1. Navigate to the Company level **Admin** tool.
2. Under 'Tool Settings,' click **Connection Manager**.
3. To automatically approve connections, mark the checkbox to 'Allow users with existing access to the Drawings tool to connect their project without Admin approval. (Recommended)'. 
   OR Clear the checkmark to require a connection request be sent for review before manually accepting or rejecting a project's request to connect.
4. Click **Save**.

## Approve or Reject Connections (if review is required)

## Objective

To approve or reject requests to connect projects using the project's Connection Manager tool.

## Background

Procore Connect enables a connection between two separate Procore projects. The connection is one-way and copies published data from an upstream source project to a downstream connected project in an unpublished state.

Upstream company accounts can choose to automatically approve connections, or require review to manually accept or reject a downstream project's request to connect. See [Configure Connection Approval Settings](#s204050 "Configure Project Connection Settings"). Follow these steps if you chose to review and manually accept each connection.

## Things to Consider

- [Required User Permissions](https://support.procore.com/products/online/user-guide/project-level/connection-manager/permissions "Connection Manager - Permissions")
- If you reject a request by mistake, the project can request a connection again that you can review and approve.
- An upstream project can support connections with multiple downstream projects. For example, multiple subcontractor companies (downstream) projects can connect to a single general contractor (upstream) project and receive data.
- For both upstream and downstream accounts, users on the Connection Manager tool email distribution list are notified of new connections, disconnections, and connection requests (if review is required). See [Connection Manager: Configure Advanced Settings](https://support.procore.com/products/online/user-guide/project-level/connection-manager/tutorials/configure-advanced-settings-connection-manager "Configure Advanced Settings: Connection Manager").
- Projects can be disconnected by the upstream or downstream account at any time. See [Disconnect Connected Projects](https://support.procore.com/products/online/user-guide/project-level/connection-manager/tutorials/disconnect-a-connected-project "Disconnect a Connected Project").

## Steps

1. Navigate to the project's **Connection Manager** tool.
2. Under 'Downstream Projects' click **Review Request**.
3. Click **Approve** to approve the connection. 
   OR Click **Reject** to decline the connection.

## See Also

- [Configure Connection Approval Settings](#s204050 "Configure Project Connection Settings")

## Close an RFI

1. Navigate to the project's **RFIs** tool.
2. Click the **Items** tab. 
   This lists all project's RFIs in the **Draft** and **Open** statuses. You can close an RFI in either status.
3. Click **View** next to the RFI you want to close.

   ##### Tip

   Before you close the RFI, you can edit the **Distribution List** to add one or more users from the company in the **Responsible Contractor** field. See [Edit an RFI](https://support.procore.com/products/online/user-guide/project-level/rfi/tutorials/edit-an-rfi "Edit an RFI"). If the RFI email settings for the project are configured to send emails to users on an RFI's **Distribution List** when an RFI is closed, adding those users to the **Distribution List** will ensure they receive an email notification when the RFI is closed. See [When does the RFIs tool send email notifications?](https://support.procore.com/faq/when-does-the-rfis-tool-send-email-notifications "When does the RFIs tool send email notifications?")
4. Click **Close RFI**button at the top of the page.
5. A green banner will appear to confirm the RFI has been closed.

## Initiate a Project Connection

## Objective

To initiate a connection between two projects in the same Procore company account or between two projects at different Procore company accounts.

## Background

Procore Connect enables a connection between two separate Procore projects. The connection is one-way and copies published data from an upstream source project to a downstream connected project in an unpublished state.

Only the users at the downstream company account can initiate a connection. Upstream company accounts can choose to automatically approve connections, or require review to manually accept or reject a downstream project's request to connect. See [Configure Connection Approval Settings](#s204050 "Configure Project Connection Settings"). Projects can be disconnected by the upstream or downstream account at any time.

## Things to Consider

- [Required User Permissions](https://support.procore.com/products/online/user-guide/project-level/connection-manager/permissions "Connection Manager - Permissions")
- Only the downstream company account can initiate a connection with an upstream account's project.
- A downstream project can only connect to one upstream project.
- GovCloud accounts will not be able to participate in a project connection.
- Projects with more than 100,000 drawing revisions can not be connected.
- For both upstream and downstream accounts, users on the Connection Manager tool email distribution list are notified of new connections and connection requests (if review is required). See [Connection Manager: Configure Advanced Settings](https://support.procore.com/products/online/user-guide/project-level/connection-manager/tutorials/configure-advanced-settings-connection-manager "Configure Advanced Settings: Connection Manager").

## Steps

1. Navigate to the project's **Connection Manager** tool.
2. Click **Connect**.
3. Select the upstream company and project. 
   *Note:* If you are connecting to a project within the *same* company, look for the 'Current Company' section in the 'Upstream Company' dropdown to select your company's name.
4. Click **Next**.
5. Select at least one feature for this connection, then click **Next**.
6. Review the Considerations, then click **Connect Projects** to initiate the project connection.

If the upstream company chose to automatically approve connections, your projects automatically connect. If the upstream company's settings require manual review for accepting or rejecting connections, Procore sends a request to the upstream company for review.

## See Also

- [Configure Connection Approval Settings](#s214831 "Initiate a Connection Request to Connect Projects")
- [About Procore Connect](https://support.procore.com/products/online/user-guide/project-level/connection-manager/tutorials/about-procore-connect "About Procore Connect")

## View External RFIs on a Downstream Project

##### In Beta

This feature is currently in beta for Procore customers. See [User Guide: Procore Connect for RFIs](user-guide-procore-connect-for-RFIs.md).

## Background

Procore's External RFI feature streamlines collaboration for users working on the same construction project across different accounts. This feature automatically copies closed RFIs from an upstream project (typically managed by a General Contractor or Owner) to downstream projects (used by Subcontractors or other Owners). This eliminates manual work, improves visibility, and ensures secure and permanent access to finalized RFIs.

## Things to Consider

- **Required User Permissions**:
 - 'Admin' permissions to the RFI tool. 
    OR
 - 'Read Only' or 'Standard' permissions with the 'View External Items' granular permission to the RFI tool.
- **Additional Information**:
 - External RFIs are read-only and cannot be edited in Downstream projects.
 - If the upstream project severs the connection, previously copied RFIs remain in your project permanently.
 - Not currently supported:
    - Private RFIs
    - Mobile access to Connected RFIs
    - Procore Document Management (PDM) attachments (not to be confused with legacy Documents tool. [Learn more](https://en-gb.support.procore.com/faq/what-is-the-difference-between-the-documents-and-document-management-tools-in-procore))

## Steps

### View External RFIs

1. Navigate to the project's **RFIs** tool.
2. Click the **External Items** tab. 
   *Note:* The External Items tab appears only with an active Connection Manager connection.
3. Click **View** next to the RFI you want to view.

### Filter External RFIs

1. Click the **External **Items****tab.
2. Click the****filter**** ![icon-filter2.png](https://support.procore.com/@api/deki/files/280258/icon-filter2.png?revision=1&size=bestfit&width=17&height=17) icon and select from the following options:
   - ****Revision.****Filters the list by current revisions OR by all revisions including outdated RFIs.
   - **Linked to your Project's RFIs.**Shows only RFIs linked to Internal RFIs.
   - ****Status****. Filters the list by the status of the RFI. **Note:** this does NOT include RFIs in the recycle bin.
     - The Recycled Status filters track if an external RFI has been recycled and its current status within the recycle bin.
   - **Last Updated At.**Select a time frame to search between or a single time to search from to filter by the last date an RFI was updated.
   - ****Responsible Contractor****. Filters the list by the contractor or subcontractor with responsibility for completing the work related to the RFI.
   - ****Received From****. Select the person from whom the RFI was received.
   - **Date Initiated.** Select a time frame to search between or a single time to search from to filter by the date an RFI was initiated.
   - **Closed Date.**Select a time frame to search between or a single time to search from to filter by the date an RFI was closed.
   - **Due Date.**Select a time frame to search between or a single time to search from to filter by the date an RFI was due.
   - ****RFI Manager****. Filters the list by the [RFI Manager](../../../../../../references/construction-management/glossary-of-terms.md#RFI_Manager_(Coming_Soon) "Glossary of Terms").
   - **Connection Status.**Filters the list by Connected OR Disconnected RFIs.
3. To clear one filter, click the '**x**' next to its name. 
   OR To clear all filters, click ****Clear All****.

## Linking Internal and External RFIs

##### In Beta

This feature is currently in beta for Procore customers. See [User Guide: Procore Connect for RFIs](user-guide-procore-connect-for-RFIs.md).

## Background

After connecting your project, link Internal and External RFIs to comprehensively track the relationship between your RFI and its corresponding **external record** (via Procore Connect). Linking improves data integrity by creating a clear audit trail, allowing project teams to easily reference an inquiry and its corresponding official external response

## Things to Consider

- **Required User Permissions**:
 - 'Admin' permissions to the RFI tool. 
    OR
 - 'Read Only' or 'Standard' permissions with the 'View External Items' granular permission to the RFI tool.
    - To see the "**Copy to My Response**" option on a linked external RFI, you must have the required permissions to respond. See [Respond to an RFI](../../rfi/tutorials/respond-to-an-rfi.md).
    - External RFIs can only be linked to Internal RFIs the user is authorized to access.
    - A link established to a private Internal RFI will not be visible to users who lack the required permissions for that private RFI.
- **Additional Information**:
 - RFIs can be linked to each other regardless of their current status: Draft, Open, Closed, Closed - Draft, Closed - Revised.
 - RFIs located in the Recycle Bin cannot be linked.
 - Disconnecting the project does **not** remove the External RFI from the list.
 - RFI links created in the downstream project **do not** sync to the upstream project.

## Prerequisites

Ensure your project is actively connected via Connection Manager or [Initiate a Project Connection](#s214831).

## Steps

### Linking **from** Internal RFIs

1. Navigate to the project’s **RFIs** tool.
2. In the **Items** tab, click **View** next to the desired RFI.
3. Click the **Link to External RFI** button. 
   *Note:* This button will appear as **Manage Links** if items have already been linked to the RFI.
4. In thewindow that appears, select one or more External RFIs to link from the dropdown menu. To remove an RFI from your selection, click the ‘**x**’ next to its name.
5. Click **Save.**
6. A green banner will confirm the link was successful. The External RFI(s) will now appear in the **Linked RFIs** section of your Internal RFI.
7. Click the **caret icon****![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAA1UlEQVR4AdTUywnEIBAG4CENpJyUkJQUT+JJS9ISLMcKdpmDsF6y48wPEmEQn58j6PZZVDZaVN4BO+copQS5I3HGHe21VRfBIYQhUwQugq/ron3fhyStuAg+joNKKVBcBHOqaFwMo/EpGIlPwyhcBSNwNWzFTbAFN8OMa8IM11rpPE9qrQ1+jJHu+x76fhsmWIvyAdSwBVXDVlQFI9BpGIVOwUhUDKNRMZxznn6nvPlTiJ6T9374DP59Dk9gHxPBPLljveY+S4hhRlAo7zUF8wJULIO/AAAA//8ZEr3PAAAABklEQVQDAPWIGdTyQngWAAAAAElFTkSuQmCC)**to expand Linked RFI details and view the official responses and attachments.
8. To use this information in your own response,click'**Copy to My Response**’**.**

### Linking **to** Internal RFIs

1. Navigate to the project’s **RFIs** tool.
2. Click the **External Items** tab.
3. Click **View** next to the desired **External RFI**.
4. Click the **Link to Your Project RFI** button. 
   *Note:* This button will appear as **Manage Links** if items have already been linked to the RFI.
5. In thewindow that appears, select one or more Internal RFIs to link from the dropdown menu. To remove an RFI from your selection, click the ‘**x**’ next to its name.
6. Click **Save**.
7. A green banner will confirm the link was successful. The Internal RFI(s) will now appear in the **Linked RFIs** section of your External RFI.

## Create an External RFI 360 Report

## Background

The 360 Reporting tool empowers you to generate comprehensive reports combining data from various sources within your project. This guide focuses specifically on creating a 360 Report to analyze External RFI data.

## Things to Consider

- **Required User Permissions**:
 - 'Admin' permissions to the RFI tool.
 - 'Read Only' and 'Standard' permissions with the 'View External Items' granular permission to the RFI tool.
- **Additional Information**:
 - External RFI 360 reports are only available in downstream projects.

## Steps

1. Navigate to the project level 360 Reporting tool.
2. Click **+ Create Report**.
3. Select **360 Report**.
4. Select **Project Execution**.
5. Click **Continue**.
6. Enter the **report name** in the upper left corner.
7. Enter the **report description** below the report name.
8. Under **Configure Columns**, two data sets are available for External RFI reporting:
   - **External RFI**
   - **External RFI Response**
9. Select relevant columns then click **Load Data**.
10. When finished, click **Save**.

## Frequently Asked Questions

###### Does this feature change how I submit new RFIs to GCs?

No. This feature only copies closed RFIs for data retention. Future updates may include cross-project creation capabilities.

###### What is an "External RFI"?

A read-only RFI automatically copied into a downstream project after it was closed in the upstream project.

###### What RFIs are copied across accounts?

All non-private RFIs. Support for private RFIs is under consideration (timeline TBD).

###### What happens if I connect to an upstream project that already has previously completed RFIs?

Once the connection is activated, all completed, non-Private RFIs from that moment on will be copied as External RFIs in your downstream project AND all previously completed, non-Private RFIs will also be backfilled into your project as External RFIs, ensuring you have a complete record of closed RFIs from the upstream project.  Depending on the number of RFIs in the upstream project it may take several minutes for the backfill process to copy over the PDFs for coversheet attachments and linked drawings.

###### Does this change email notifications for closed RFIs?

No. Email notifications remain unchanged. The copied RFI is an additional feature.

###### Can I configure notifications when External RFIs arrive in my project?

No.

###### Who can view External RFIs in Downstream projects?

RFI administrators and users with the new "View External Items" granular permission.

###### Are External RFIs accessible on mobile?

Not yet. Mobile support is planned with the ability to link External and Local RFIs.

###### What happens if a closed RFI in the Upstream project is reopened or deleted?

The status update will reflect in the Downstream External RFIs, ensuring near real-time visibility.

###### Do users need permissions in the Upstream project to see Connected RFIs?

No. All access to these read only External Items is managed within the downstream project.

###### Can External RFIs be edited in Downstream projects?

No, they are read-only

###### Can I link External RFIs to drawings or other tools?

Not directly, but in the near future you will be able to link an External RFI to a Local RFI, then link the Local RFI as per normal capabilities.

## Conclusion

Thank you for using the Procore Connect for RFIs beta. Please provide feedback through the ****Share Feedback**** button in the Connection Manager tool, and via the surveys sent by Procore.
# RFIs (Android)

Source: https://v2.support.procore.com/product-manuals/rfis-android/permissions

---

Table of Contents

## Permissions

Learn which user permissions are required to take the described actions in this tool.

##### Â Important

Some actions that impact this tool are done in other Procore tools.

| | The action is available on Procore's Web, iOS, and/or Android application.

Users can take the action with this permission level.

Users can take this action with this permission level AND one or more additional requirements, like [granular permissions](/faq-what-are-permissions-in-procore-and-how-do-they-work).

[What granular permissions are available for the project's RFIs tool?](/faq-what-granular-permissions-are-available-for-the-projects-rfis-tool)

| [RFI Tutorials](/product-manuals/rfi-project/tutorials) Action | None | Read Only | Standard | Admin | Notes |
| --- | --- | --- | --- | --- | --- |
| Add a Related Item to an RFI Web |  |  |  |  |  |
| Add Assignees to an RFI  Web |  |  |  |  | 'Standard' level users must first be designated as an '**Assignee**' and must be the current '**Ball In Court**' person. |
| Change the Status of an RFI Web iOS Android |  | - Act as RFI Manager | - Act as RFI Manager |  | Users with the '[Act as RFI Manager](/faq-what-is-the-rfi-manager-role)' granular permission must also have one of the following attributes:   - Be assigned as the 'RFI Manager' on the RFI - Be the RFI's creator |
| Choose an 'Official Response' for an RFI Web iOS Android |  | - Act as RFI Manager OR - Mark Official Responses | - Act as RFI Manager OR - Mark Official Responses |  | - Users with the '[Act as RFI Manager](/faq-what-is-the-rfi-manager-role)' granular permission must also have one of the following attributes:    - Be assigned as the 'RFI Manager' on the RFI   - Be the RFI's creator - Users with the Mark Official Responses' granular permisison must also have one of the following attributes:    - Be the RFI's creator   - Be an Assignee   - Be Distribution List Member |
| Close an RFI Web iOS Android |  | - Act as RFI Manager | - Act as RFI Manager |  | - Users with the '[Act as RFI Manager](/faq-what-is-the-rfi-manager-role)' granular permission must also have one of the following attributes:    - Be assigned as the 'RFI Manager' on the RFI   - Be the RFI's creator |
| Configure Settings: RFIs Web |  |  |  |  |  |
| Create a Change Event from an RFI Web iOS Android |  |  |  |  | Users also need 'Standard' level permissions or higher on the project's **Change Events** tool. |
| Create a Potential Change Order from an RFI Web |  |  |  |  | To create a Potential Change Order from an RFI, the following must also be true:   - The RFI is created. - The prime contract must be in the 'Approved' status. - The Change Events tool must be disabled on the project, and the Prime Contracts tool must be configured for two (2) or three (3) tier change orders.    - If the Change Events tool is enabled, follow the steps in [Create a Change Event from an RFI](/product-manuals/rfi-project/tutorials/create-a-change-event-from-an-rfi) instead. |
| Create an Instruction from an RFI Web |  |  |  |  | Users must also have 'Standard' level permissions or higher on the project's **Instructions** tool. |
| Create a Draft RFI   Web iOS Android |  |  |  |  |  |
| Create an RFI Web iOS Android |  |  | - Act as RFI Manager |  |  |
| Create and View a Custom RFI Report Web |  |  |  |  |  |
| Create RFIs on a Drawing  Web iOS Android |  |  | - Act as RFI Manager | - Act as RFI Manager | Users must also have 'Standard' level permissions or higher to the project's **Drawings** tool. |
| Customize the Column Display in the RFIs Tool   Web |  |  |  |  |  |
| Delete a Response to an RFI   Web |  |  |  |  |  |
| Delete an RFI   Web |  |  |  |  |  |
| Designate the Default RFI Manager for a Project's RFIs   Web |  |  |  |  |  |
| Download RFI Attachments   iOS |  |  |  |  |  |
| Draft an RFI with Assist Web |  |  |  |  |  |
| Edit a Custom RFI Report You Created   Web |  |  |  |  |  |
| Edit Any Custom RFI Report   Web |  |  |  |  |  |
| Edit a Draft RFI You Created   Web iOS Android |  |  |  |  |  |
| Edit Any RFI   Web iOS Android |  | - Act as RFI Manager | - Act as RFI Manager |  | - Users with the granular permission must also be one of the following:    - Assigned as the 'RFI Manager' on the RFI   - The RFI's creator |
| Export an RFI   Web |  |  |  |  |  |
| Export the RFIs List to CSV or PDF   Web |  |  |  |  |  |
| Forward an RFI by Email   Web iOS Android |  |  |  |  |  |
| Forward an RFI for Review   Web |  |  |  |  | Users must also be designated as an **Assignee** for the RFI and be the current **Ball In Court** person. |
| Link Existing RFIs on a Drawing   Web iOS Android |  |  |  |  | Users must also have 'Standard' level permissions or higher to the project's **Drawings** tool. |
| Link Internal and External RFIs on a Downstream Project Web |  | - View External Items | - View External Items |  |  |
| Perform Bulk Actions on RFIs   Web |  |  |  |  |  |
| Reopen an RFI   Web iOS Android |  | - Act as RFI Manager | - Act as RFI Manager |  | Users with the granular permission must also be one of the following:   - Assigned as the 'RFI Manager' on the RFI - The RFI's creator |
| Respond to an RFI   Web iOS Android |  |  |  |  | Users with 'Standard' level permissions without a granular permission must also be an **Assignee** or a **Distribution List** member for the RFI. |
| Respond to an RFI   Web iOS Android |  | - Act as RFI Manager | - Act as RFI Manager |  | - 'Read Only' users with the granular permission must also be assigned as the 'RFI Manager' on the RFI - 'Standard' users with the granular permission must also have one of the following attributes:    - Be assigned as the 'RFI Manager' on the RFI   - Be the RFI's creator   - Be an Assignee   - Be a Distribution List Member |
| Resize the Column Width in the RFIs Log   Web |  |  |  |  |  |
| Retrieve an RFI from the Recycle Bin   Web |  |  |  |  |  |
| Revise an RFI   Web |  |  | - Act as RFI Manager |  |  |
| Search and Filter RFIs   Web iOS Android |  |  |  |  |  |
| Share a Custom RFI Report   Web |  |  |  |  |  |
| Shift the Ball in Court on a RFI   Web |  | - Act as RFI Manager | - Act as RFI Manager |  | Users with the granular permission must also be one of the following:   - Assigned as the 'RFI Manager' on the RFI - The RFI's creator |
| Summarize RFIs with Assist Web |  |  |  |  |  |
| View External RFIs on a Downstream Project Web |  | - View External Items | - View External Items |  |  |
| View RFIs (Not Draft, Not Private)   Web iOS Android |  |  |  |  |  |
| View RFIs (Private, Not Draft)   Web iOS Android |  |  |  |  | 'Read Only' and 'Standard' users must also be the RFI's **Assignee** or on the **Distribution List**. |
| View RFIs (Private, Draft)   Web iOS Android |  |  |  |  | 'Read Only' and 'Standard' users must also be the RFI's **RFI Manage**r or **Creator**. |
| View RFIs for Users Within Your Company (Private, Not Draft)   Web iOS Android |  | - View Private RFIs Associated with Users within Same Company | - View Private RFIs Associated with Users within Same Company |  | For users with the granular permission, you or a user in your company must also be the **Assignee** or on the **Distribution List.** |
| View RFIs for Users Within Your Company (Including Private and Draft)   Web iOS Android |  | - View Private RFIs Associated with Users within Same Company | - View Private RFIs Associated with Users within Same Company |  | For users with the granular permission, you or a user in your company must also be the RFI's **RFI Manager** or **Creator**. |
| View RFI Response (Any)   Web |  |  |  |  | 'Read Only' and 'Standard' users must be the RFI's **RFI Manager** or **Creator**. |
| View RFI Responses (Official)   Web |  |  |  |  | If you can view the RFI, you can review the response. |
| View RFI Responses (Unofficial, Show Official Responses Disabled)   Web |  |  |  |  | If you can view the RFI, you can review the response. |
| View RFI Responses (Unofficial, Show Official Responses Enabled)   Web |  |  |  |  | 'Read Only' and 'Standard' users must also be the **RFI's Assignee**, **RFI Manager**, on the **Distribution List**, or the **Creator** of the response. |
| View the Distribution History of a Custom RFI Report   Web |  |  |  |  |  |
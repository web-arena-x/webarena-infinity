# Create a Change Event (Android)

Source: https://v2.support.procore.com/product-manuals/change-events-android/tutorials/create-a-change-event-android

---

## Background

Creating a change event allows you to prepare for the cost of a change before it becomes an actual cost. For example, if a project manager is anticipating the need to change the paint colors of a project, they can start preparing for that cost by creating a change event, which describes the estimated financial cost of the change as well as which cost codes will be affected. After creating a change event, they can then create an RFQ (Request for Quote), which is sent to the appropriate subcontractors for pricing. When RFQs are created and responded to by the assigned subcontractors, change orders can then be created based upon the submitted quote.

## Things to Consider

- **Required User Permissions:**

 - 'Standard' or 'Admin' level permissions on the project's Change Events tool.
- **Additional Information:**

 - You can configure what items are created with the **quick create** icon, see [Configure Quick Create Settings](/product-manuals/project-overview-screen-ios/tutorials/configure-quick-create-settings-ios).
 - This action can be performed offline. Tasks performed offline sync with Procore once a network connection is reestablished.
 - **Alternate ways to create change events**:

    - To learn how to use other Procore platforms and tools to create a change event, see [Which Procore tools can I use to create a change event?](/faq-which-procore-tools-can-i-use-to-create-a-change-event)

## Prerequisites

- [Configure Settings: Change Events](/product-manuals/change-events-project/tutorials/configure-advanced-settings-change-events)

## Steps

1. Open the **Procore** app on an Android mobile device and select a project. 
   *Note:* This loads the Tools screen for the project.
2. Tap the **quick create** icon and select **Change Event**. 
    OR Tap the **Change Events** tool and tap the **create** icon.
3. Tap into the following fields to add the appropriate information:

   - **Title:** Provide a descriptive title for the change event. The change event's title is displayed as the subject in the list view.
   - **Status:** Select one of the following options:\* **Open:** 'Open' is the default status when you first create a change event. This indicates that the change event is active, and users can manage items within the event (RFQs, Budget Modifications, Commitment PCOs, Prime PCOs).\* **Closed:** Tap 'Closed' once all necessary change orders and RFQs have been created and the event is considered complete.\* **Pending:** Tap 'Pending' if the change event requires approval before it can be closed out.\* **Void:** Tap 'Void' if no change came from the event. Setting the change event as 'Void' is an alternative to deleting the change event as a record will be kept on the log page for future reference.   
     *Note:* If you mark a change event as 'Void,' that change event will be hidden on the Change Events log page. To view voided events, select 'Void' or 'All (Include Void)' from the Status list under Filters on the Change Events log page.
   - **Description:** Add a description relevant to the change event.
   - **Add Attachments:** Add any relevant attachments from one of the following options:\* **Camera:** Tap to take and add a photo from your mobile device's camera.\* **Photos:** Tap to add a photo or file saved to your mobile device.\* **Files:** Tap to add an existing photo from your mobile device's library.
   - **Scope:** Select one of the following options:\* **TBD:** Tap 'TBD' if the cost of the change event is unknown.\* **In Scope:** Tap 'In Scope' if the cost is covered in the original contract\* **Out of Scope:** Tap 'Out of Scope' if the cost was not covered in the contract, signifying that the change order will likely be submitted to the client as an additional cost.
   - **Type:** Select a cost type associated with the change event.
   - **Change Reason:** Select a reason for the change. To configure change reasons, see [Set Default Change Management Configurations](/product-manuals/admin-company/tutorials/set-the-default-change-management-configurations).
4. Tap **Create**.
# Create a T&M Ticket (iOS)

Source: https://v2.support.procore.com/product-manuals/tm-tickets-ios/tutorials/create-a-tm-ticket-ios

---

## Things to Consider

- [Required User Permissions](/product-manuals/tm-tickets-ios/permissions)
- You can configure what items are created with the **quick create**  icon, see [Configure Quick Create Settings](/product-manuals/project-overview-screen-ios/tutorials/configure-quick-create-settings-ios).

## Prerequisites

- [Best Practices for Configuring T&M Tickets](/product-manuals/tm-tickets-project/tutorials/best-practices-for-configuring-tm-tickets)

## Steps

1. Open the **Procore** app on an iOS mobile device and select a project.
2. Tap the **quick create**  icon and select **T&M Ticket**.  
   OR  
   Tap the **T&M Tickets** tool and tap the **create**  icon.
3. Tap to enter information into the following fields as appropriate:

   - **Description**: Enter a short description of the work for the T&M Ticket.
   - **Status**: The status of your ticket will update automatically when certain conditions have occurred.

     - **In Progress**: This is the default status when a ticket is created and has not been signed by the Company or Customer Signee.
     - **Ready for Review**: The ticket will update to this status when the assigned Company Signee has verified the ticket's labor, equipment, and material to indicate that it is ready for customer review.
     - **Field Verified**: The ticket will update to this status when the Customer Signee has verified and signed it.
     - **Closed**: Tickets can be set to 'Closed' status on the desktop app to indicate that the ticket is closed or has been sent to the client and should not be edited.  
       *Note:* Tickets can only be moved to the 'Closed' status on the desktop app and cannot be edited on the mobile app. To edit a closed ticket, you will need to reopen it from the desktop app. For instructions on how to close or reopen a ticket, see [Close or Reopen a T&M Ticket](/product-manuals/tm-tickets-project/tutorials/close-or-reopen-a-tm-ticket).
   - **Performed On**: This field defaults to the current day.
   - **Locations**: Tap to select the location where the work is being performed.  
     *Note:* Users with 'Admin' permissions or users who have the "Manage Locations" granular permission enabled on the Admin tool can add a location. See [Add Tiered Locations to a Project](/product-manuals/admin-project/tutorials/add-multi-tiered-locations-to-a-project).
   - **Ordered by**: Select the users who ordered the ticket.  
     *Note*: A user must be recorded in the Project level Directory tool to be selected from this list. To add someone to the project directory, see [Add a Person to the Project Level Directory (iOS)](/product-manuals/directory-ios/tutorials/add-a-person-to-the-project-level-directory-ios).
   - **Reference #**: Enter the Change Order number that will be associated with the T&M ticket.
4. **Attachments:**

   - **Camera** **:** Tap to open your device's camera and take a photo to add to your T&M ticket.
   - **Photos:** Tap to select an image from your device's photo library or Procore Photos. After you select the photos, click **Add** or **Done**.
   - **Files:** Tap to select a saved file from your device's files
5. In the 'Labor' section, under 'Employees', tap on the following fields to enter information as needed:

   - **Employee**: Select the employee from the Workers list.  
      Note: To add a worker to the list, see [Add a Worker (iOS)](/product-manuals/crews-ios/tutorials/add-a-worker-ios).
   - **Classification**: Select the employeeâs classification from the list.
   - **Hours**: Enter the number of working hours the employee performed.
   - **Time Type**: Select the time type for the work.
6. Tap **Apply**.
7. In the 'Materials' section, under 'Quantities', tap on the following fields to enter information as needed:

   - **Material**: Enter the type of material used.
   - **Material Description**: Enter a description of the material or the invoice number for the material delivery.
   - **Unit**: Select a unit of measurement from the list.
   - **Quantity**: Enter the quantity of materials needed.
8. Tap **Apply**.
9. In the 'Equipment' section, under 'Quantities', tap on the following fields to enter information as needed:

   - **Equipment Name:** Select the equipment used from the list.
   - **Equipment Description**: Type any relevant information about the equipment item such as the type, equipment ID number, or delivery ID number.
   - **Hours**: Type in the number of hours the equipment was used.
10. Tap **Apply**.
11. In the 'Approvals' section, under 'Company Signee', select the user from the list.
12. Under 'Customer Signee', select the customer name from the list.
13. *Optional:* In the 'Notes' section, under 'More Information', type in any additional information as needed.
14. Tap **Save**.
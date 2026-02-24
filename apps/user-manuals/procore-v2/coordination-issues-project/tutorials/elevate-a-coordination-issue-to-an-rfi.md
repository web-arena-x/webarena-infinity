# Elevate a Coordination Issue to an RFI

Source: https://v2.support.procore.com/product-manuals/coordination-issues-project/tutorials/elevate-a-coordination-issue-to-an-rfi

---

## Background

During a project's coordination phase, clashes and other construction issues are often identified and tracked as coordination issues. This allows project teams to collaborate and resolve design conflicts informally and efficiently. It's an effective way to manage the day-to-day back-and-forth communication required to refine the building model.

However, some issues cannot be resolved informally or may require a formal, contractual response from a member of the design team or another key stakeholder. When a coordination issue requires an official, documented question and answer, it should be elevated to a Request for Information (RFI). This ensures the query is formally tracked in the project's RFIs tool and that the response becomes part of the official project record, providing necessary clarification that could impact cost, schedule, or scope.

The issue's status automatically updates based on the RFI's progress:

- **Elevated**: The issue's status changes to 'Elevated' as soon as it's linked to an RFI. The status reverts to *Elevated* if the RFI is reopened without an 'Official' response.
- **Released**: The status changes to 'Released' after someone adds an 'Official' response to the RFI. The status remains *Released* if the RFI is reopened once the 'Official' response is logged.

## Things to Consider

- **Required User Permissions:**

 - You need both of the following:

    - 'Admin' level permissions on the project's Coordination Issues tool.
    - 'Standard' or 'Admin' level permissions on the project's RFIs tool. *Note:* Users with 'Standard' level permissions on the project's Coordination Issues and RFIs tools can elevate issues they have created to an RFI.
- **Additional Information:**

 - You can elevate a coordination issue to a new draft RFI or link it to an existing RFI. Once elevated, you cannot close it or elevate it again until the linked RFI is closed. An issue can only be elevated once. If you need to reverse this action, you can unlink the RFI from the issue.

## Steps

View steps for one of the following:

- **From the Procore Plugin**

 - Elevate a Coordination Issue to a New RFI
 - Elevate a Coordination Issue to an Existing RFI
- **From the Coordination Issues Tool**

 - Elevate a Coordination Issue to a New RFI
 - Elevate a Coordination Issue to an Existing RFI

### From the Procore Plugin

#### Elevate a Coordination Issue to a New RFI

1. Open NavisworksÂ® and your model on your computer. See [Getting Started Using the Procore Plugin](/product-manuals/coordination-issues-project/tutorials/getting-started-procore-plugin-for-coordination-issues).
2. With the Procore tab selected, click **Issues List**.
3. Hover over the issue that you want to elevate to an RFI.
4. Click **Info**.
5. Click the **ellipsis** (**...**) icon, then click **Elevate to RFI**.
6. Fill out the following fields:

   - **Subject**: Provide a descriptive title for the RFI. The RFI's subject is displayed as the RFI's title in the list view.
   - **Question**: Enter your question and any additional background information that may be needed to properly answer the question.
   - **Attachments**: Attach any supplemental information to the RFI.   
     *Note:* All snapshots of the viewpoint will automatically be added as attachments on the RFI.
   - **Location**: Select the location associated with the RFI from the drop-down menu. *Note:* New locations can be added to the project's Admin tool. See [Add Tiered Locations to a Project](/product-manuals/admin-project/tutorials/add-multi-tiered-locations-to-a-project).
   - **RFI Manager**: Select an RFI Manager from the drop-down list. See [What is the RFI Manager role?](/faq-what-is-the-rfi-manager-role) *Notes:*

     - By default, the name of designated RFI Manager appears here. See [Designate the Default RFI Manager for a Project's RFIs](/product-manuals/rfi-project/tutorials/designate-the-default-rfi-manager-for-a-projects-rfis).
     - If you are a user with 'Admin' permissions on the RFIs tool, you may select yourself or another user with 'Admin' permissions from the list.
     - If you are a user with 'Standard' permissions, this list only populates with the names of users who have 'Admin' permissions to the RFIs tool. You may only select another user with 'Admin' permissions from the list.
7. Click **Create Draft**. *Notes:*

   - A Draft RFI will be created in the RFIs tool when elevating a coordination issue to an RFI.
   - An RFIs tool 'Admin' user will need to [Edit the Draft RFI](/product-manuals/rfi-project/tutorials/edit-an-rfi) and change its status to "open" in order for the RFI's workflow to begin.

#### Elevate a Coordination Issue to an Existing RFI

1. Open the NavisworksÂ® application on your computer.
2. Open the model you want to view.
3. Click the **Procore** tab to open the Procore plugin.
4. In the All Issues list, hover over the issue that you want to elevate to an RFI, then click **Info**.
5. Click the ellipsis (**...**) icon. Then click **Elevate to RFI**.
6. Click **Choose an Existing RFI**.
7. Locate the RFI to which you want to elevate a coordination issue. 
   *Tip!* Enter an RFI number or subject in the search bar to search for an RFI, or scroll through them.
8. Click the RFI to select.
9. Click **Link to this RFI**. *Note:* The coordination issue will automatically be elevated to the RFI.

### From the Coordination Issues Tool ââââââ

#### Elevate a Coordination Issue to a New RFI

Elevating a coordination issue creates a draft RFI in the project's RFIs tool.

1. Navigate to the project's Coordination Issues tool on [app.procore.com](http://app.procore.com/).
2. Click the **Issue** link to view its details in the side panel.
3. Click the icon to open the **More Options** menu and choose **Elevate to RFI**.
4. Complete these RFI fields:

   - **Subject.** Enter a descriptive title for the RFI. This title will appear in the list view of the RFIs tool.
   - **Question.** Enter your question. Include details to help others answer it.
   - **Drawings**. Select a drawing. If your project uses **Drawing Areas**, select the area first, then select the drawings you want to attach and click **Add**.
   - **Attachments**: Attach any other supplemental information. Any existing views or attachments will be automatically included in the RFI.
   - **Location**: Select the RFI's location from the drop-down menu. To add new locations, see [Add Tiered Locations to a Project](/product-manuals/admin-project/tutorials/add-multi-tiered-locations-to-a-project).
   - **RFI Manager**: Select the RFI Manager from a list of users with 'Admin' level permissions on the RFIs tool. If available, the existing project's RFI Manager is selected automatically. To learn more, see [What is the RFI Manager role?](/faq-what-is-the-rfi-manager-role)
5. Click **Create Draft**. A confirmation banner appears with a link to the draft. An 'Admin' on the RFIs tool must set the RFI's status to *Open* to start the workflow. You cannot close or re-elevate the original issue until the new RFI is closed.

#### Elevate a Coordination Issue to an Existing RFI

1. Navigate to the project's Coordination Issues tool on [app.procore.com](http://app.procore.com/).
2. Click the **Issue** link to view its details in the side panel.
3. Click the icon to open the **More Options** menu and choose **Elevate to RFI**.
4. Type an RFI number or some keywords to find the RFI with the **Search** box.
5. Click the matching RFI in the list of matches to select it.
6. Click **Elevate to Existing RFI.** A confirmation banner appears with a link to the RFI. An 'Admin' on the RFIs tool must set the RFI's status to *Open* to start the workflow. You cannot close or re-elevate the original issue until the new RFI is closed.

## Next Steps

- [Edit an RFI](/product-manuals/rfi-project/tutorials/edit-an-rfi)
- [Respond to an RFI](/product-manuals/rfi-project/tutorials/respond-to-an-rfi)
- [Close an RFI](/process-guides/user-guide-procore-connect-for-RFIs/close-an-rfi)
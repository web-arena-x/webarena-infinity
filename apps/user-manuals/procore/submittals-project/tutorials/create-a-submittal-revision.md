# Create a Submittal Revision

Source: https://v2.support.procore.com/product-manuals/submittals-project/tutorials/create-a-submittal-revision

---

## Things to Consider

- **Required User Permissions:**

  - *To create a revision for a submittal that you created:*

    - 'Read Only' or 'Standard' level permissions on the project's Submittals tool with the ['Create Submittal' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on your permissions template.
    - 'Standard' level permissions on the project's Submittals tool without a permissions template assigned to you.
  - *To create a revision for a submittal that you did not create:* 'Standard' level permissions on the project's Submittals tool and be designated as the [Submittal Manager](/glossary-of-terms).
  - *To create a revision for any submittal:* 'Admin' level permissions on the project's Submittals tool.
- **Additional Information:**

  - You can only create a revision for the most current revision of submittal. For example, if a submittal at Revision 0, you can only create Revision 1. To learn more, see [What is a submittal revision?](/faq-what-is-a-submittal-revision)

## Steps

1. Navigate to the project's **Submittals** tool. This reveals the Submittals page.
2. In the Submittals log, locate the desired submittal. Then click **View**. This opens the submittal in view mode.
3. Click the vertical ellipsis, then click **Create Revision**. This opens the 'Create Revision' page. *Note*: This button is only visible and available when you are viewing the most current revision of a submittal. You can only create a new revision from the most recent one.
4. Scroll to the 'General Information' area and note that all of the general information from the previous revision is inherited. In addition, the revision number is automatically incremented by one (n +1). In the example below, the previous revision number was 1, so Procore automatically increments the new revision number to 2.
5. Revise the following submittal information as needed:

   - **Title**. The descriptive name that best summarizes the information in the submittal.

     Title
   - **Spec Section**. Denotes the corresponding section from the project's specifications book. See [Where do the selections in the 'Specification Sections' drop-down list in the Submittals tool come from?](/faq-where-do-the-selections-in-the-spec-sections-drop-down-list-come-from)

     Spec Section
   - **Received From**. The contact for the responsible contractor who provided the submittal information to the project team.

     Received From
   - **Submittal** **Package.** The [submittal package](/glossary-of-terms) that contains the submittal. In Procore, adding submittals to a package is optional. The decision to add submittals to a submittal package is based on your project's requirements, which is determined by your company's or project's management team. For instructions, see [Create a Submittal Package](/product-manuals/submittals-project/tutorials/create-a-submittal-package).

     Submittal Package
   - **Status**. The current status of the submittal. Only a user with 'Admin' level permission to the Submittals tool can change a submittal's status. See [What are the default submittal statuses in Procore?](/faq-what-are-the-default-submittal-statuses-in-procore) and [What is a 'Draft' Submittal?](/faq-what-is-a-draft-submittal)

     Status
   - **Cost Code**. The [cost code](/glossary-of-terms) for the submittal. Cost codes are managed in the 'Cost Code' segment in Procore's [Work Breakdown Structure](https://support.procore.com/products/online/work-breakdown-structure).

     Cost Code
   - **Type**. The information type associated with the submittal. The default type selections in Procore include: *Document*, *Pay Request, Payroll,* *Plans*, *Prints*, *Product Information*, *Product Manual*, *Sample*, *Shop Drawing*, *Specification,* and *Other*. See [Create Custom Submittal Types](/product-manuals/admin-company/tutorials/create-custom-submittal-types).

     Type
   - **Location**. The location at the job site for the submittal. This can be an existing location from the Location list or a tiered location. See [Add Tiered Locations to a Project](/product-manuals/admin-project/tutorials/add-multi-tiered-locations-to-a-project).

     Location
   - **Private**. Indicates privacy settings for the submittal. When a submittal is marked 'Private', it is only visible to users with 'Admin' level permissions on the Submittals tool, users in the Submittal Workflow, and members of the submittal's Distribution List. Users with the ['View Private Submittals Associated to Users within Same Company' granular permission](/product-manuals/permissions-company/tutorials/grant-granular-permissions-in-a-project-permissions-template) enabled on their permissions template can also view a submittal marked 'Private' if another user in their company is associated with the submittal. See [Mark a Submittal as Private](/product-manuals/submittals-project/tutorials/mark-a-submittal-as-private).

     Private
   - **Description**. Informative details, notes, and/or actions that describe the submittal.

     Description
   - **Attachments**. Attach any relevant files. You have these options:

     - Click **Attach File(s)** and then choose the appropriate option from the shortcut menu that appears.  
        OR
     - Use a drag-and-drop operation to move files from your computer into the grey **Drag and Drop File(s)** box.

     Attachments

     - *Note:* If the previous revision of the submittal had any file attachments, you will need to reattach them in the new revision, if desired. Attachments are NOT carried over between revisions.
   - **Submittal Workflow**. The people assigned to complete the [submittal workflow](/glossary-of-terms). In Procore, the submittal workflow includes two roles: a [submitter](/glossary-of-terms) and the approvers who are responsible for performing/completing the [approval process](/glossary-of-terms). Typically, approvers are members of the design team.

     Submittal Workflow
   - **Distribution List**. The people who will receive email notifications from Procore as the submittal progresses through the [submittal workflow](/glossary-of-terms). If your project team has created any distribution lists in the Project Directory, you can select those lists here. See [Add a Distribution Group to the Procore Directory](/process-guides/set-up-a-project-directory/invite-users-to-procore)).

     Distribution List
   - **Related Items**. Any related items that have been added to the submittal (i.e., drawings, documents, plans, and so on). See [Add a Related Item to a Submittal](/product-manuals/submittals-project/tutorials/add-a-related-item-to-a-submittal).

     Related Items
   - **Custom Fields**â. If your company has added custom text fields for use with the Submittals tool, enter the required data as specified by your project team in these fields. See [Configure Advanced Settings: Submittals Tool](/product-manuals/submittals-project/tutorials/configure-settings-submittals-tool).

     Custom Fields
6. Choose from the following:

   - **Create & Send Emails**: Use this option to create the new submittal revision and send it to the designated submittal approver(s), as well as all members on the submittal's distribution list (optional).
   - **Create But Do Not Send Emails**: Use this option to only create the new revision but not send any email notifications.
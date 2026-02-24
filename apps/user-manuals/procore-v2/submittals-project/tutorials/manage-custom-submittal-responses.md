# Manage Custom Submittal Responses

Source: https://v2.support.procore.com/product-manuals/submittals-project/tutorials/manage-custom-submittal-responses

---

## Background

Users with âAdminâ level permission to the projectâs Submittals tool can configure a wide range of customized submittal responses using the new 'Submittal Responses' link in the Configure Submittals Settings page. A *submittal response* is a list of pre-defined responses (e.g., APPROVED, APPROVED AS NOTED, REVISE AND RESUBMIT, REJECTED, and so on) that can be applied to a submittal by reviewers during the review and approval process.

##### Examples

There are a variety of reasons an organization might want to customize their submittal responses. For example:

- **To match specific contract language**.  
   Some organizations use the term âREVIEWEDâ in place of âAPPROVED or âREVIEWED AS NOTEDâ in place of âAPPROVED AS NOTED.â
- **To match the actions on the submittals review rubber stamp that your company traditionally used to process hard-copy submittals**.  
   Some organizations may prefer to use âFURNISH AS NOTEDâ and âNO EXCEPTIONS TAKENâ in place of âAPPROVED AS NOTEDâ.
- **To use commonly understood acronyms instead of spelled words**.  
   Some organizations may prefer reviewers to use specific acronyms such as: A (in place of âAPPROVEDâ), AAN (in place of âAPPROVED AS NOTEDâ), R&R (in place of âREVISE AND RESUBMIT).

## Things to Consider

- **Required User Permissions:**

  - 'Admin' level permissions on the project's Submittals tool
- **Default Submittal Responses:**

  - Procore provides eight (8) submittal responses by default. See [What are the default submittal responses in Procore?](/faq-what-are-the-default-submittal-responses-in-procore)
  - You can create up to twelve (12) custom submittal responses for six (6) out of the eight (8) default submittal responses  
    *Note*: The system limits these responses to only one custom response (1) per project: PENDING and SUBMITTED.
- **Requirements:**

  - Each submittal response requires a minimum of one (1) entry.
  - Each submittal response is limited to a maximum of 255 characters. For best readability, Procore recommends creating responses with 20 characters or fewer.

## Steps

1. Navigate to the project's **Submittals** tool.
2. Click the **Configure Settings**  icon. This reveals the âSubmittal Settingsâ page.
3. Click **Submittal Responses**.
4. Locate the submittal response that you want to change.
5. Choose from the following options:

   - **Change a Custom Submittal Response**: You can change an existing response to a custom value for all eight (8) of the default submittal responses in Procore.

     - Click the pencil icon next to a response to edit it.
     - Type in the new name for the response.
     - Click **Edit Response** to save your changes.
   - **Add a New Custom Submittal Response:** You can add up to twelve custom submittal responses for several of the default submittal responses in Procore. For three (3) of the responses (FORWARDED FOR REVIEW, PENDING, and SUBMITTED), the system limits you to only one (1) custom response.

     - Click **Add Response**.
     - Select the associated default response.
     - Enter your custom response, and click **Add Response** to save. *Note: You can modify the associated default response by clearing the selection and making a new one.*
   - **Delete a Custom Submittal Response:** You can only delete the custom responses that have been added to the system. Each of the default responses can be customized, but not deleted.

     - Click the delete icon next to the desired response.
     - When prompted to confirm you want to delete the response, click **Delete Response.**

### Where Do Custom Submittal Responses Appear?

After customizing your responses, they will appear as selections in any space in the Submittals tool where default responses are visible, such as filters or in the response selection screen in a submittal workflow.
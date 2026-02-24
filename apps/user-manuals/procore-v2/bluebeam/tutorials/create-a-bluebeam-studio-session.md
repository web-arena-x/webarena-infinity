# Create a Bluebeam Studio Session

Source: https://v2.support.procore.com/product-manuals/bluebeam/tutorials/create-a-bluebeam-studio-session

---

##### In Beta

The Procore + Bluebeam integration is currently in beta and can be enabled with [Procore Explore](/product-manuals/admin-company/tutorials/manage-features-with-procore-explore).

## Background

Once you enable the Procore Submittals + Bluebeam integration, you can create a Bluebeam Studio Session from a Submittal item that has PDF documents attached in Procore.

## Things to Consider

- **Requirements:**

 - **Procore Tool:** Access to the Submittals tool within your Procore project(s).
 - **Bluebeam Login Credentials:** Email address and password of your Bluebeam account.
- **Additional Information:**

 - **One Session per Revision:** The Procore Submittals + Bluebeam integration supports the creation of only one Bluebeam Studio Session per Submittal Revision. Multiple sessions cannot be generated for different steps within the workflow.
 - **Snapshot in Time:** Data is only synced between Procore and Bluebeam at two intervals: when the session is initially created and when the session is finalized.

    - If additional PDFs are attached to the Submittal in Procore after the Studio Session has been created, those files will not be automatically included in the Bluebeam Session. You will need to add them manually within Bluebeam.
    - If approvers are added to the Submittal workflow in Procore after the session is created, they will not be automatically invited to the Bluebeam Session. You will need to invite them manually within Bluebeam.

## Prerequisites

[Sign in to Bluebeam from Procore](/product-manuals/bluebeam/tutorials/sign-in-to-bluebeam-from-procore)

## Steps

1. Navigate to a Submittal item within the Procore Submittals tool.
2. Ensure that relevant PDF documents are attached. You can add them in the **General Information** section of the Submittal or as part of a response within the Submittal workflow. 
   *Note:* A blue banner will appear at the top of the Submittal item view.
3. Click the option within the blue banner to log in with your Bluebeam credentials.
4. Click **Allow Access** to connect Procore with your Bluebeam account.
5. After logging in, click **Start Bluebeam Session** in the blue banner to:

   - Send all attached PDF documents from the current Submittal revision to a new Bluebeam Studio Session.
   - Automatically invite the Submittal Manager and all current Approvers in the Submittal workflow to the Studio Session, enabling them to markup PDF documents and participate. 
     *Note:* Once the session is created, the blue banner will update to display a link to the Bluebeam Studio Session.
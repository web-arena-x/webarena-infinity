# How to Integrate Greenhouse with Handshake

Source: https://support.joinhandshake.com/hc/en-us/articles/360058989813-How-to-Integrate-Greenhouse-with-Handshake

---

Premium partners can integrate Greenhouse with Handshake, enabling a seamless experience for posting jobs from Greenhouse in Handshake, managing hiring activities in one platform, and more.

If your company is interested in this integration, please contact your account manager to enable 'Greenhouse V2 Integration' in your company settings. Once enabled, you’ll be ready to set up your Greenhouse integration.

*Premium features are for Handshake Premium accounts only. For more information, please check out this* [*resource*](https://www.joinhandshake.com/employers-premium/)*.*

---

### 

### Integrate Greenhouse

Click each header for detailed instructions on completing your integration setup.

**Step 1: Ensure you have the appropriate account roles enabled within Greenhouse**

To complete this integration, you must have the following Greenhouse permissions:

- **Can manage all organization’s API Credentials**
- **Can manage and configure web hooks**
- **Manage custom fields** (you must be at least a **Job Admin** with this permission to enable Applications with Candidate Education)

If you do not have these permissions, contact a Greenhouse user in your organization with **Site Admin** level permissions.

**Note:** The Site Admin will need the permission **Can edit another user's advanced permissions** to apply the necessary permissions to your account.

The user with Site Admin level permissions should take the following steps:

1. Click the **Configure** icon in the upper-right corner of the page, then select **Users** from the left menu.

2. Locate and click your name to open your user page.

![Configure.png](https://support.joinhandshake.com/hc/article_attachments/35837278762903)

3. In the **User-Specific Permissions** panel, expand the **Developer Permissions** dropdown menu.

4. Check **Can manage ALL organization’s API Credentials** and **Can manage and configure web hooks**.

5. Click **Save** when finished.

![GH.Image2.png](https://support.joinhandshake.com/hc/article_attachments/25998877824791)

**Step 2: Add your user ID from Greenhouse to Handshake**

For Handshake to allow candidates to apply directly to Greenhouse Recruiting, Handshake will need the user ID of an existing Greenhouse user in your organization, or the user ID for a Greenhouse Recruiting user account that's created specifically for Handshake.  
**NOTE:** We highly recommend using a Greenhouse User ID that will not expire for this integration (i.e. if an employee leaves your company). Otherwise there may be disruptions in the integration if there are changes to this Greenhouse user. **We recommend creating a new user specifically for this integration if possible.** 
 
To locate the user ID for either an existing user (or for the new Handshake-specific user, if applicable), click the **Configure** icon ![configure_new.png](https://support.greenhouse.io/hc/article_attachments/360075153851/configure_new.png) in the upper right-hand corner and click **Users** from the left menu.

![GH_Configure_Image.png](https://support.joinhandshake.com/hc/article_attachments/25998877826199)

Once you have filtered on the correct user from the *Users* page, click **Export to Excel**.

![GH_Users_Image.png](https://support.joinhandshake.com/hc/article_attachments/25998877827223)

A spreadsheet will be downloaded to your computer. From the spreadsheet, navigate to the **User** **ID** column and copy the user ID value inline for your selected user. 
 
Within Handshake, navigate to **Company Settings**, then click **Greenhouse Integration** from the left menu. Paste the value into the Greenhouse User ID field.

*Tips: make sure to keep this page open while you complete the remaining fields.*

*![GH_User_ID_Handshake.png](https://support.joinhandshake.com/hc/article_attachments/25998877828887)*

**Step 3: Generate the Job Board API Key from Greenhouse and add it to Handshake**

Click on the **Configure** icon ![configure_new.png](https://support.greenhouse.io/hc/article_attachments/360075153851/configure_new.png) in the upper right-hand corner of the page, then click **Dev Center** on the left menu.

![GH_Dev_Center_Image.png](https://support.joinhandshake.com/hc/article_attachments/25998877829911)

 Click **API Credential Management**from the Dev Center page, then click **Create New API Key** to generate the API key for Handshake.

![GH_Api_credentials_Image.png](https://support.joinhandshake.com/hc/article_attachments/25998867300631)

From the **Create new credential dialog** *box*, give your API key a name and select **Job** **Board** from the **Type** dropdown menu. When finished, click **Create**.

Your Job Board API key for the integration is now created and configured! Navigate to your recently created Job Board API key, copy the key, and paste this value in Handshake within the **Job Board API Key** field under your Greenhouse settings.

![GH_ApI_Image_Handshake.png](https://support.joinhandshake.com/hc/article_attachments/25998877838231)

**Step 4: Generate the Harvest API Key from Greenhouse and add it to Handshake**

Click on the **Configure** icon ![configure_new.png](https://support.greenhouse.io/hc/article_attachments/360075153851/configure_new.png) in the upper right-hand corner, then click **Dev** **Center** on the left menu.

Click **API Credential Management**, then click **Create New API Key** to generate the API key for Handshake.

On the *Manage API Key Permission*s page, select all of the following API permissions:

| | |
| --- | --- |
| Applications GET: Retrieve Application GET: List Applications PATCH: Update Application | Applications_Image.png |
| Candidates GET: List Candidates GET: Retrieve Candidate POST: Add Candidate POST: Add Note POST: Add Attachment POST: Add Application POST: Add Education POST: Add E-mail PATCH: Edit Candidate | Candidates_Image.png |
| Education GET: Get degrees GET: Get disciplines GET: Get schools | Education_Image.png |
| Jobs GET: Retrieve Job GET: List Jobs | Jobs_Selection_Image.png |
| Job Posts GET: List Job Posts GET: Retrieve Job Post for Job GET: List Job Posts for Job | Job_Post_selection_Image.png |
| Sources GET: List Sources | Souces_Image.png |
| Custom Field Options GET: Custom field options POST: Create custom field options | Custom field options.png |
| Custom Fields GET: Get custom fields | Custom fields.png |

When finished, click **Update**.

Your Harvest API key for the Greenhouse/Handshake integration is now created and configured!  Navigate to your recently created Harvest API key, copy the key, and paste this value in Handshake within the **Harvest API Key** field under your Greenhouse settings.

![GH_Harvest_Api_Image_Handshake.png](https://support.joinhandshake.com/hc/article_attachments/25998867303959)

**Step 5: Create a Job board token from Greenhouse and add it to Handshake**

*To access Job Board settings, you must be a Site Admin within Greenhouse*. *If you aren't a Site Admin, you'll need to connect with a user who is, and have them follow the process below.*

Click the **Configure** icon ![configure_new.png](https://support.greenhouse.io/hc/article_attachments/360075153851/configure_new.png)in the upper-right corner of the page, then click **Job** **Board** from the left menu.

![GH_Job_Board_Image.png](https://support.joinhandshake.com/hc/article_attachments/25998867317783)

Click the **Ellipsis** **icon** (three dots) to the right of the job board, then select **Edit** **Board** **Settings** from the dropdown menu.

![GH_Edit_Board_Image.png](https://support.joinhandshake.com/hc/article_attachments/25998867324951)

Navigate to the *URL* section and copy the value in the provided field. This is the job board token for the job board you'll be using to post Greenhouse jobs from within Handshake.

![GH_URL_Image.png](https://support.joinhandshake.com/hc/article_attachments/25998867327511)

Paste this value into the **Job Board Token** field under your Greenhouse settings within Handshake.

![Job_Board_Token_Image_Handshake.png](https://support.joinhandshake.com/hc/article_attachments/25998877863447)

**Step 6: Generate a Tracking Link for the job board from Greenhouse and add it to Handshake**

Click the **Configure** icon ![configure_new.png](https://support.greenhouse.io/hc/article_attachments/360075153851/configure_new.png) in the upper-right corner of the page, then click **Job Board** on the left menu.

![GH_Job_Board_Image.png](https://support.joinhandshake.com/hc/article_attachments/25998867334935)

Select the job board you are using for this integration from the list and click the **Ellipsis icon** (three dots) to the right of the job board name. Click **Tracking** **Link** from the dropdown menu.

![GH_Tracking_Link_Image.png](https://support.joinhandshake.com/hc/article_attachments/25998877867159)

Use the **Get a Tracking Link** dialog box to configure the **Who gets credit** and **Source** fields. Click **Create Link** when finished.

![GH_Get_Tracking_Link_Image.png](https://support.joinhandshake.com/hc/article_attachments/25998867342487)

Copy the string of letters and numbers at the end of the URL (in the example above, this would be the **3478b75c3us** segment of the URL) and paste this value into the **Handshake Source Token** field in Handshake under your Greenhouse settings.

![Source_Token_Image_Handshake.png](https://support.joinhandshake.com/hc/article_attachments/25998877875991)

Once all five fields are completed within Handshake, click the blue button **Verify** at the bottom of the page and a secret key will be generated that you'll use to set up Web Hooks within Greenhouse.

![GH_Verify_Image.png](https://support.joinhandshake.com/hc/article_attachments/25998867348631)

![GH_Webhook_Image.png](https://support.joinhandshake.com/hc/article_attachments/25998877880343)

**Step 7: Configure Handshake Web Hooks within Greenhouse**

A web hook is a simple event notification system. When an event occurs within the Greenhouse platform (e.g., a candidate is hired), a payload of data about the event is sent to a specified endpoint; in this case Handshake. You'll need to create 5 web hooks to enable all necessary integration capabilities.

Before creating these web hooks within Greenhouse, you'll need to retrieve your employer ID from Handshake.

Click **Brand Page** from the left navigation bar, then copy the numerical value at the end of the associated URL for the web page.

![URL_Image.png](https://support.joinhandshake.com/hc/article_attachments/25998867353495)

To create a web hook, click the **Configure** icon ![configure_new.png](https://support.greenhouse.io/hc/article_attachments/360075153851/configure_new.png) in the upper-right corner of your home page in Greenhouse, then click **Dev Center** on the left menu. Click **Web** **Hooks** on the resulting page.

![GH_Web_Hooks_Image.png](https://support.joinhandshake.com/hc/article_attachments/25998877887255)

Fill in the following fields for each web hook, then click **Create Web hook** to complete the web hook setup. Greenhouse Recruiting will ping your endpoint. If this ping is accepted successfully, the endpoint will be created.

**Web Hook # 1:**

- **Name this web hook**: *post\_created\_handshake*
- **When**: Job Post Created
- **Endpoint URL**: https://ats.joinhandshake.com/webhooks/greenhouse/<handshake\_employer\_id>
- **Secret Key:** enter the secret key generated by completing the Greenhouse configuration page within Handshake
- **Error recipient email:** leave blank

**Web Hook # 2:**

- **Name this web hook**: *post\_updated\_handshake*
- **When**: Job Post Updated
- **Endpoint URL**: https://ats.joinhandshake.com/webhooks/greenhouse/<handshake\_employer\_id>
- **Secret Key:** enter the secret key generated by completing the Greenhouse configuration page within Handshake
- **Error recipient email:** leave blank

**Web Hook # 3:**

- **Name this web hook**: *job\_updated\_handshake*
- **When**: Job Updated
- **Endpoint URL**: https://ats.joinhandshake.com/webhooks/greenhouse/<handshake\_employer\_id>
- **Secret Key:** enter the secret key generated by completing the Greenhouse configuration page within Handshake
- **Error recipient email:** leave blank

**Web Hook # 4:**

- **Name this web hook**: *hire\_candidate\_handshake*
- **When**: Candidate has been hired
- **Endpoint URL**: https://ats.joinhandshake.com/webhooks/greenhouse/<handshake\_employer\_id>
- **Secret Key:** enter the secret key generated by completing the Greenhouse configuration page within Handshake
- **Error recipient email:** leave blank

**Web Hook # 5:**

- - **Name this web hook**: *candidate\_rejected\_handshake*
 - **When**: Candidate or prospect has been rejected
 - **Endpoint URL**: https://ats.joinhandshake.com/webhooks/greenhouse/<handshake\_employer\_id>
 - **Secret Key:** enter the secret key generated by completing the Greenhouse configuration page within Handshake
 - **Error recipient email:** leave blank

**Web Hook # 6:**

- **Name this web hook**: *new\_candidate\_application*
- **When**: candidate has submitted application
- **Endpoint URL**: https://ats.joinhandshake.com/webhooks/greenhouse/<handshake\_employer\_id>
- **Secret Key:** enter the secret key generated by completing the Greenhouse configuration page within Handshake
- **Error recipient email:** leave blank

### Additional resources

If you need assistance with setting up your Greenhouse integration or have questions during the process, contact our Support team.

*For more information on using the Greenhouse integration in Handshake, refer* [*How to Use Handshake's Greenhouse Integration*](https://support.joinhandshake.com/hc/en-us/articles/360034457353).
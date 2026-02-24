# How to Integrate your ATS with Handshake

Source: https://support.joinhandshake.com/hc/en-us/articles/26155576618647-How-to-Integrate-your-ATS-with-Handshake

---

Integrating your ATS with Handshake helps you increase efficiency, enhance the candidate experience, and connect your activities to outcomes.

The owner or admin of the company profile can seamlessly integrate their ATS with Handshake in just a few minutes.

*ATS integration is available only to Handshake Premium partners. For more information, please check out this* [*resource*](https://joinhandshake.com/employers/products/premium/talent-engagement-suite/)*!*

---

### 

### Integrate your ATS

1. Click on your name in the upper-right corner of any page, then select **Company settings** from the dropdown.

![Company settings.png](https://support.joinhandshake.com/hc/article_attachments/26155576600599)

2. From the menu on the left of the page, click **ATS Integration**., then click the gray button **Set Up Integration**.

![ATS integrations.png](https://support.joinhandshake.com/hc/article_attachments/26155621450007)

3. In the pop-up modal, either select your ATS integration or type the name of the ATS in the keyword search bar.

![Select integration .png](https://support.joinhandshake.com/hc/article_attachments/27601475626391)

- After selecting the ATS integration, the modal may display the message "Administrator role required. You must be an administrator of [Integration Name] in order to link to Handshake successfully." To continue, click the black button **I am an admin**.

![Admin role required .png](https://support.joinhandshake.com/hc/article_attachments/27601470111511)

- Review your data permissions, then click the black button **Next**.
- **Note**: Ensure that all the following permissions are enabled when configuring your API credentials with your ATS.

**Required permissions**

#### Applications

The Application Object is used to represent a candidate's journey through a particular Job's recruiting process. If a Candidate applies for multiple Jobs, there will be a separate Application for each Job if the third-party integration allows it.

**Endpoint**: /applications

**Description**: fetches all applications from the linked account

**Permissions**: read + write

**Endpoint**: /applications/%{id}

**Description**: fetches applications based on IDs

**Permissions**: read + write

#### Attachments

The Attachment object is used to represent a file attached to a candidate.

**Endpoint**: /attachments

**Description**: fetches all attachments from the linked account

**Permissions**: read + write

#### Candidates

The Candidate object is used to represent profile information about a given Candidate. Because it is specific to a Candidate, this information stays constant across applications.

**Endpoint:** /candidates

**Description:** fetches all candidates from the linked account

**Permissions**: read + write

**Endpoint**: /candidates/%{id}

**Description**: fetches candidates based on IDs

**Permissions**: read + write

**Endpoint**: /candidates/meta/post

**Description**: checks the schema of the Candidate object

**Permissions**: read + write

#### 

#### JobInterviewStage

The JobInterviewStage object is used to represent a particular recruiting stage for an Application. A given Application typically has the JobInterviewStage object represented in the current \_stage field.

**Endpoint**: /job-interview-stages/%{id}

**Description**: fetches job interview stages based on IDs

**Permissions**: read

#### Job

The Job object can be used to track any jobs that are currently or will be open/closed for applications.

**Endpoint**: /jobs

**Description**: fetches all jobs from the linked account

**Permissions**: read

#### 

#### ScreeningQuestions

The ScreeningQuestion object is used to represent questions asked to screen candidates for a job.

**Endpoint:** /jobs/%{job\_id}/screening-questions

**Description:** fetches screening questions for a job

**Permissions:** read

#### RemoteUser

The RemoteUser object is used to represent a user with a login to the ATS system.

**Endpoint**: /users

**Description**: fetches all users from the linked account

**Permissions**: read

![Data permissions.png](https://support.joinhandshake.com/hc/article_attachments/27601470115607)

4. Read the instructions provided, enter the required information (e.g., API key, username, password, or API Server URL) in the appropriate fields, and then click the black button **Next**.

- In the following screenshots, we use Smart Recruiters as the example. For instructions on other ATS integrations, refer to the guide provided in the PDF linked in the[Additional resources](#h_01JC13NPX0NZ02HVNC1CBR22A4) section at the bottom of this article.

![Enter api key.png](https://support.joinhandshake.com/hc/article_attachments/27601470117655)![Enter identifier.png](https://support.joinhandshake.com/hc/article_attachments/27601470119191)

5. The message 'Setting up your account. This might take a while!' appears, followed by a rotating black circle indicating that the account setup is in progress.

![Setting up your account.png](https://support.joinhandshake.com/hc/article_attachments/27601475639063)

6. In the next pop-up modal, you can choose to map additional fields or skip this step.

**Note**: **we recommend you skip this step, as field mapping was already set up by Handshake**.

![map additional fields.png](https://support.joinhandshake.com/hc/article_attachments/27601470124311)

7. When your account is connected, the message "Success! You've connected your account." appears. To finish your account setup, click the black button **Finish setup**.

![Success confirmation.png](https://support.joinhandshake.com/hc/article_attachments/27601475646487)

8. Next, define your application statuses mapping, then click the gray button **Save**.

- Which application statuses from your ATS should be mapped to the status “Hired” and “Rejected” in Handshake?
- Make sure to list all the application statuses that should be linked (exact matches, caps sensitive), separated by a comma. All other statuses will be automatically mapped to “Reviewed” in Handshake.

![application statuses mapping.png](https://support.joinhandshake.com/hc/article_attachments/26155576611095)

### Update integration

If you need to update your integration, please follow the steps below.

1. Click the gray button **Update integration** on the **ATS Integration** page.

![Update integration button .png](https://support.joinhandshake.com/hc/article_attachments/26155576613143)

2. In the pop-up modal, click the white button **Relink integration**, then click the black button **Finish**.

![You're connected.png](https://support.joinhandshake.com/hc/article_attachments/27601475651095)

### Additional resources

[Handshake - Admin and Owner Guide for ATS Integration](https://www.canva.com/design/DAGSdmGpy20/yuHExyoXf4fEjqiVuaaPjg/view?utm_content=DAGSdmGpy20&utm_campaign=designshare&utm_medium=link&utm_source=editor#1)
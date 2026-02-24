# How to Use Handshake's iCIMS Integration

Source: https://support.joinhandshake.com/hc/en-us/articles/10140953000599-How-to-Use-Handshake-s-iCIMS-Integration

---

Handshake’s ATS integration with iCIMS enhances efficiency, improves the candidate experience, and connects your recruitment activities to measurable outcomes.

**Note**: **The iCIMS integration module is currently unavailable for new contracts**. Premium partners can contact their Success Manager to discuss alternative solutions or address questions about this change.

All connected teammates, except Representatives, can view and post ATS jobs, although reporting and analytics are restricted to specific roles.

*Premium features are for Handshake Premium accounts only. For more information, please check out this* [*resource*](https://www.joinhandshake.com/employers-premium/)*! Premium partners should contact their Account Manager to get set up with our ATS integrations.*

Below, we have outlined the steps to post and manage a job on Handshake with iCIMS. Click each collapsible header for detailed instructions.

**Posting a job**

1. Click **Jobs** from the left navigation bar, then click the black **Create Job** buttonin the upper-right corner of the page.

- *Existing jobs in Handshake cannot be linked to iCIMS — a new job posting is required.*

2. Choose the job listing from iCIMS from the **Add job from ATS** dropdown.

- *The job must be marked as **Live** in iCIMS for it to be available in Handshake!*

![Add job from ATS.png](https://support.joinhandshake.com/hc/article_attachments/26001216505751)

3. Job details from iCIMS will automatically populate in Handshake. Confirm details are accurate and formatted as desired.

- By selecting to request a resume, you can also receive applicant packages from Handshake.

**Note****: The ability to edit an ATS URL depends on the configuration of the ATS system**.

4. Complete your job posting and post your job to schools. *For guidance, refer to* [*How to Post a Job*](https://support.joinhandshake.com/hc/en-us/articles/218693198)*.*

**Student application** *(process)*

When your job is live, students can search for and apply for the role. *To learn how students find jobs on Handshake, refer to*[*How to Search for Jobs & Internships*](https://support.joinhandshake.com/hc/en-us/articles/218693408-How-to-Search-for-Jobs-and-Internships)*.*

- When students click to apply, the iCIMS application launches.
- Students will complete their application as configured within iCIMS.
- After completing and submitting the application, their application will appear in iCIMS automatically.
- In Handshake, the student will be prompted to confirm whether their application was submitted.

**Reviewing applications in iCIMS**

Once a student submits an application, it will automatically appear in iCIMS with all of their information.

Review the application(s) as usual in iCIMS. *Learn more about* [*Viewing Profiles and Taking Action on Candidates in iCIMS Candidate Relationship Management*](https://care.icims.com/s/article/Introduction-to-the-Candidate-Profile-in-iCIMS-Nurture).

**Application status sync**

The status of the application in Handshake is refreshed every hour to match the current status in iCIMS

**Note**: If the status is directly updated in Handshake, the status will be adjusted to reflect the corresponding status in iCIMS.

**The application will reflect one of the following statuses**:

- **Pending**: Indicates the application wasn't fully submitted in iCIMS
 - The student clicked on the **Apply Externally** button on the job posting on Handshake but did not complete the external application.
- **Applied**: Indicates the application has been submitted successfully in iCIMS
- **Hired**: Application was marked as "Hired" in iCIMS
 - A job posting with only one vacancy will expire automatically in Handshake after a candidate is marked as "Hired" in iCIMS.
- **Rejected**: Application was rejected in iCIMS

**Note**: If you expire your job posting in iCIMS, the job posting will also expire in Handshake.

**Managing applicants in Handshake**

Handshake's ATS integrations automatically sync candidates that initiate the application process directly from within Handshake as well as with the external ATS posting to allow for clearer attribution in [Talent Analytics: Applicants](https://support.joinhandshake.com/hc/en-us/articles/360036928353).

The job's Applicants tab includes an additional filter titled **Origin**, which allows you to easily distinguish between applications submitted through your ATS and Handshake. *Learn more in our* [*Job Applicant Management Guide*](https://support.joinhandshake.com/hc/en-us/articles/115013307228).

*To opt out of this feature, employers can reach out to their CSM or contact Support.*

Explore our most frequently asked iCIMS integration questions. 

**FAQs**

**Does Handshake access applicants that don’t come from Handshake?**

- Handshake pulls all candidates from the specific job posted in Handshake after a candidate is referred from Handshake to apply in iCIMS. Pulling all applicants is necessary to pair candidate records between both systems, given that candidates can re-enter the application flow without the appropriate source tracking.
- Only candidates with details that match those referred from Handshake are synced. We do not log any candidates that are not paired through this matching process.

**Are jobs automatically posted in Handshake?**

- No, employers still have to post a new job in Handshake to link to iCIMS.

**Can we integrate multiple ATS’ (Greenhouse/Workday/iCIMS) simultaneously?**

- Not at this time.

**Is application status updating bi-directional?**

- No. For compliance reasons, Handshake cannot push an update from our database regarding a change to an application status. With this integration, updates to application status will only come from iCIMS to Handshake.
- This is because Handshake is not an ATS and ATS must follow certain parameters that Handshake is not required to follow, so it would be inappropriate for Handshake to make updates to an ATS’ application statuses.

**Are there any suggested workarounds for fields that do not pull over, such as the salary range disclaimer and equal opportunity statement? Or do they have to be manually completed?**

- They can only be manually completed (copy and paste).

**Can the end date and duration fields be left blank?**

- Yes. Handshake will not transfer these fields at all.

**For jobs with multiple locations, how does that work with the integration?**

- The job posting will use [Mapbox](https://www.mapbox.com/contribute/#/?q=&l=1.2378%2F32.9547%2F11) to pull the first location and map it to an address. Any additional locations can be selected in the flow.

**Do we have any options for a remote location?**

- This field is not auto-populated and if open to remote, will be input manually once details load.

**How do the paid/unpaid and salary range fields pull over?**

- These fields do not pull over at this time. Will be completed manually, if needed.

**Can Handshake display more statuses than just "Hired "or "Rejected", or can it be configured in any way?**

- Handshake will only map iCIMS states (stages) to “Hired” or “Rejected”. Handshake also uses "Pending" to indicate that the application is awaiting syncing, and "Reviewed" to indicate that the application has synced but is not currently in the "Hired" or "Rejected" statuses.

**How do we apply token tracking URLs?**

- Automatically applied as part of the external URL that auto-populates based on the “Source” token provided by the employer.

**How long is the delay between creating a new requisition in iCIMS and it appearing in the menu in Handshake?**

- Up to 1-hour. We retrieve all data routinely once per hour.

**What happens to job posts on Handshake created before the integration?**

- These jobs can still be used and treated like any post created only in Handshake but cannot be updated to sync with any job from iCIMS.
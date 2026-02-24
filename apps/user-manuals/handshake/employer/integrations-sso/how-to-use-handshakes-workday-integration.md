# How to Use Handshake's Workday Integration

Source: https://support.joinhandshake.com/hc/en-us/articles/6772611653015-How-to-Use-Handshake-s-Workday-Integration

---

Handshake’s ATS integration with Workday enhances efficiency, improves the candidate experience, and connects your recruitment activities to measurable outcomes.

All connected teammates, except Representatives, can view and post ATS jobs. However, access to reporting and analytics is limited to specific roles.

*ATS integrations are available to Talent Engagement Suite partners only*. *For more information, please check out this* [*resource*](https://www.joinhandshake.com/employers-premium/)*!*

> *Talent Engagement Suite partners should contact their Account Manager to get set up with our ATS integrations.*

Below, we have outlined the steps to post and manage a job on Handshake with Workday. Click each collapsible header for detailed instructions.

**Posting a job**

1. Click **Jobs** from the left navigation bar, then click the black **Create job** button in the upper-right corner of the page.

- *Existing jobs in Handshake cannot be linked to Workday — a new job posting is required.*

2. Choose the job listing from Workday from the **Select ATS job to link** dropdown.

- *The job must be marked as **Live** in Workday for it to be available in Handshake!*

![Select_ATS_job_to_link_.png](https://support.joinhandshake.com/hc/article_attachments/25996989096471)

3. Job details from Workday will automatically populate in Handshake. Confirm details are accurate and formatted as desired.

- By selecting to request a resume, you can also receive applicant packages from Handshake.

4. Complete your job posting and post your job to schools. *For guidance, refer to* [*How to Post a Job*](https://support.joinhandshake.com/hc/en-us/articles/218693198)*.*

**Candidate experience**

Students can search for and apply for jobs on Handshake. If your job is of interest to them, students may complete the application as required.

- Students apply by clicking **Apply Externally** on the job posting in Handshake, which launches the Workday application.
- Students complete their application as configured within Workday.
- After completing the application, their application will appear in Workday automatically within a few minutes.
- In Handshake, the job posting will prompt the student to confirm whether their application was submitted. The student can click **Yes** or **No** to confirm.

**Tip**: Target qualified candidates by creating campaigns in Handshake. *Learn more about* [*Campaigns: Create a Job Campaign*](https://support.joinhandshake.com/hc/en-us/articles/17014630910999).

**Reviewing applications in Workday**

After a student applies, their application appears automatically in Workday and includes:

- First name, last name, and email address
- Source as Handshake
- Resume and cover letter (if required)

Review the application as usual in Workday.

![review_app_in_workday.png](https://support.joinhandshake.com/hc/article_attachments/25996989095063)

**Application status updates**

Application statuses in Handshake update automatically based on changes in Workday. Updates occur hourly.

Statuses include:

- **Applied**: The applicant completed the ATS application or started it but did not complete it.
- **Hired**: Candidate marked as **Hired** in Workday. If the job has one vacancy, the posting expires automatically in Handshake.
- **Rejected**: Application rejected in Workday.

**Note**: If a job is closed in Workday, it also closes in Handshake.

**Manage applicants in Handshake**

Handshake’s ATS integrations sync candidates who begin their application in Handshake and those who apply directly through the ATS, providing employers with a unified view of applicant attribution. Learn more in [Talent Analytics: Applicants](https://support.joinhandshake.com/hc/en-us/articles/360036928353).

Handshake assigns each applicant a status based on the information received from Workday. Candidates listed as **Applied** may display one of two internal states:

- **Not Reviewed (blue dot)**: The application has not been reviewed.
- **Reviewed (no dot)**: The application was reviewed or successfully synced from the ATS.

The **Candidate applied through** filter on the **Applicants** tab allows employers to distinguish between candidates who applied through Workday and those who began their application in Handshake.

*To opt out of this feature, employers can reach out to their CSM or contact Support.*

Explore our most frequently asked Workday integration questions.

**FAQs**

**Getting started**

**1. What is the timeline for setting up and validating?** It takes 5–10 days for setup and validation to complete.

**2. Is there a testing environment?** Yes. Handshake refers to it as Staging, and validation testing takes place there. After successful testing, the configuration will move to production.

**3. What does Handshake do with non-Handshake candidate data gathered during testing?** The testing process takes place in the implementation tenant on Workday and Handshake’s development environment. The test data used will not reflect real applicant information.

**Candidate & applicant data**

**4. What is the candidate experience once the integration is complete?** Students search and apply for jobs in Handshake. When they click Apply Externally, they are taken to Workday to complete the application. Within a few minutes, the application appears in Workday automatically. The Handshake posting then prompts the student to confirm whether their application was submitted.

**5. Does Handshake access applicants that don’t come from Handshake?** Handshake pulls all candidates from the specific job posted in Handshake after a candidate is referred from Handshake to apply in Workday. Pulling all applicants is necessary to pair candidate records between both systems, since candidates may re-enter the application flow without the appropriate source tracking. Only candidates with details that match those referred from Handshake are synced. We do not log any candidates that are not paired through this matching process.

**6. What applicants do we access with the permission "Compliance re: security group ‘Get Only - Candidate Data: Job Applications"?** Refer to #5.

**Jobs & postings**

**7. Are jobs automatically posted in Handshake?** No. Employers must still post new jobs in Handshake to link them to Workday.

**8. When jobs close in Workday, are they also closed in Handshake?** Yes. Jobs close in Handshake within an hour of closing in Workday.

**Integration capabilities & limitations**

**9. Can we integrate multiple ATSs (e.g., Greenhouse, Workday, iCIMS) simultaneously?** Not at this time.

**10. Is application status updating bi-directional?** No. For compliance reasons, Handshake cannot push updates regarding changes to application statuses. Updates only flow from Workday to Handshake. Because Handshake is not an ATS, it would be inappropriate for Handshake to update an ATS’s application records.

**Technical details**

**11. Which Workday Web Service does the integration use?** Recruiting: <https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html>

**12. Does the integration require certificate updates?** No. Workday may periodically send communications about certificate updates, but these do not apply to our integration with Workday.

*Learn more about using* [*Using the Workday Integration in Handshake*](https://www.youtube.com/watch?v=STJQrNOBOpo).
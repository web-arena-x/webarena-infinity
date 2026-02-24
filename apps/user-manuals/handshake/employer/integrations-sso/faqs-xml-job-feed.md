# FAQs: XML Job Feed

Source: https://support.joinhandshake.com/hc/en-us/articles/32426275339927-FAQs-XML-Job-Feed

---

The XML feed enables employers to automate job posting from their Applicant Tracking System (ATS) to Handshake.

This article provides answers to common questions about setting up and managing the XML job feed in Handshake.

*Want to learn more about how the XML Job Feed works? Check out* [*A Guide to Handshake XML Job Feed*](https://support.joinhandshake.com/hc/en-us/articles/32407031672215).

---

**FAQs**

**Job feed requirements**

**1.** **What fields are required for the XML job feed?**

You can find the full list of required fields in our [US XML Feed requirements doc](https://docs.google.com/document/d/1oc9SwjP4nqw1ZmYaCyS5CKcnyKGfQ2uc7YD9lW7V19E/edit?tab=t.0#heading=h.e4x873vgip4m).

**Note**: We will update this document regularly as our team works to make our requirements as streamlined as possible.

**Integration settings**

**1. Where do I enter the XML URL?**

In Handshake, navigate to your **Company Settings**, then click the **Job Feed** tab located in the left-hand side menu. Paste your XML job feed URL into the **Job feed link** field, then click **Validate**.

![Job feed tab.png](https://support.joinhandshake.com/hc/article_attachments/32426253757847)

**Posting to schools**

**1. Does the XML feed post jobs to all schools / the full network?**

No. Jobs will only be posted to schools where the employer is auto-approved. Employers cannot currently select a custom list of schools.

**Note**: The job may still have certain exclusion criteria to meet, such as schools not allowing unpaid or temporary positions, and may require additional approval even if the employer is approved.

**2.** **Who can post jobs via the XML feed?**

Only users with Owner or Admin roles.

**Feed filters**

**1. Will all jobs from the XML feed be posted to Handshake automatically, or can I limit postings to only early career/entry-level roles?**

Only the jobs included in the XML feed will be posted to Handshake. If you want to limit jobs to specific types (e.g., early career roles), you must apply filters within the XML feed itself before it is sent to Handshake.

We recommend that employers or their feed providers ensure the feed contains only the intended job postings.

**Timing & job syncing**

**1. How does the job posting process work? Is manual approval needed like some ATS integrations?**

Jobs in the XML feed are imported directly into Handshake and posted automatically. No manual action is needed. When a job is removed from the feed, it is closed on Handshake and moved to the "Closed" tab.

**2. How long does it take for jobs to appear in Handshake?**

Jobs may take up to 24 hours to appear, depending on volume. If you don't see your jobs, check the XML setup page and review the activity log for errors.

**3. How often does Handshake process the XML feed?**

Handshake pulls and processes the XML file once per day.

**4. Can jobs be posted at scale?**

Yes. The system processes job feeds asynchronously to support high-volume submissions.

**Job updates and changes**

**1. What happens if I edit a job's title, description, or other content after it's been posted to Handshake?**

Once a job has been posted on HS through the XML feed ingestion, it cannot be changed without manual intervention.

For instance, if the job description or location is changed in the XML feed after the job has been posted to Handshake, the changes will not be reflected in Handshake. Employers can either:

- Open the job in Handshake and edit the job directly
- Remove the job from the XML feed and repost it with a new source\_reference\_id

**2.Does the XML feed automatically expire jobs that are closed in the ATS like our ATS integrations do?**

Yes. If a job is marked as closed in the ATS and no longer appears in the XML feed, it will be auto-archived in Handshake during the next daily sync.

**ATS and XML**

**1. Can an employer use both XML and ATS integration at the same time?**

No. Employers must choose one method. XML allows for faster and more automated job posting.

**2. Is an ATS required to use the XML feed?**

Yes. The XML feed pulls directly from the employer's ATS.

**3. Where do candidates apply? Does the XML feed push them to the ATS?**

Yes. The XML feed typically includes an apply URL that redirects applicants to the ATS. If no URL is provided, candidates can apply directly on Handshake (though this is uncommon).

**4. Does the XML feed work with all ATS platforms?**

Yes. Employers can use any ATS to generate an XML feed. No formal ATS integration is required.

**Source tracking and XML**

**1. Does Handshake have the ability to append the source to the URLs for us from the XML feed? Is the appended source customizable?**

Currently, Handshake can append the source as "Handshake" through an internal flag enabled by Support.

**Options:**

- Employers can add the source code to URLs manually before submission
- Request Handshake Support to enable the "Handshake" source flag

**Note****:** Make sure source names match what's expected in the ATS to avoid tracking errors.

**Technical details**

**1. Where does the XML feed pull data from?**

From the employer's ATS via the provided XML URL.

**2. Is XML the only format we support? Do you support other formats like FTP?**

Yes, XML is the only format we support at this time.

**3. Can employers post one job to multiple locations?**

Yes, up to 5,000 jobs per feed.

**4. Is there a job limit per feed?**

Yes. The current cap is 5,000 jobs.

**5. What happens if one job in the feed has an error?**

Valid jobs will still be posted. Errors will be logged and visible to the customer for correction.

**6. Can multiple XML files be submitted?**

Not at this time. Only one XML file per feed is supported.

Each time we process the file, we create any new postings in Handshake. If a posting is removed from the file, we will archive it.

**7. Who hosts the XML file?**

Employers must host their own XML file. Handshake does not provide hosting services. There are many options to host a file from a publicly accessible URL e.g. Google Drive, Dropbox, etc. that can be managed by the customer.

**8. Who receives notifications for XML-posted jobs?**

The Handshake Owner user receives job-related notifications. Currently, there is no way to assign different hiring team members to each job via the XML feed.

**9. How can I get IPs for Whitelisting?**

If your system requires IP allowlisting, contact Support to request this information.

**Unsupported configurations**

**1. Can I use a SOAP URL for my feed?** No. SOAP endpoints are not supported. Use a standard HTTP or HTTPS URL.

**2. Can I export CSV data to an SFTP server instead of providing an XML feed?** No. Scheduled CSV exports to SFTP are not supported as a replacement for an XML file.

**3. Can I provide an authenticated (password-protected) XML feed?** No. At the moment, authenticated or password-protected XML feeds are not supported. The XML file must be accessible via a public URL without authentication.

**Troubleshooting common errors**

Based on previous submissions, feeds often fail due to one or more of the following issues:

- **Invalid XML tags**: Spaces or unexpected characters in XML tags. 
 Example: <job title > instead of <job title>.
- **Incorrect or unexpected field values**: For example, for employment\_type, we expect Full-Time or Part-Time. If you use Onsite, Remote, or Hybrid, an error will occur.
- **Missing required fields**: Such as title and source\_reference, or missing values within tags.
- **Incomplete internship or temporary job data**: Missing duration, start\_date, or end\_date. If these fields are not provided, the job may fail to post correctly.
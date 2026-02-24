# Source Tag URL for External Applicant Tracking Systems

Source: https://support.joinhandshake.com/hc/en-us/articles/4407110993431-Source-Tag-URL-for-External-Applicant-Tracking-Systems

---

Source tags enable your ATS to recognize Handshake as the source of your candidates.

Since Handshake can only identify an applicant who clicks to apply once they have been redirected from the site, it's essential to track the source in your ATS to identify which candidates were sourced from Handshake.

**Topics:**

- [Source tags](#h_01GY5X1E003B15J6XRQNP1K73Q)
- [Configure your source tag](#h_01GY5X1KTB7P2ZN349HX7B7J3W)
- [Add a source tag to a new job](#h_01GY5X1S9RPX8HV0SQ0YSQRJJA)

### 

### Source tags

A source tag is a string of text appended to a URL that contains instructions for the ATS on how to track the referral source. Although ATS systems use different names for these tools, the purpose remains the same. Among these names are "tracking links", "source tracking", "tracking codes", and "source code".

For the ATS to automatically identify Handshake-referred applicants, source tags must be configured correctly.

Source tags are typically structured as a URL parameter. URL parameters (sometimes called query strings) are the part of the weblink that follows a single question mark. Multiple parameters can be appended to a single URL separated by ampersands.

- The following is an example of an ATS source tag: www.companyname.com/careers/jobID12345/source=Handshake

**Note**: The actual URL will be different for each employer and their respective ATS service, but they will all end with “source=Handshake”.

### Configure your source tag

To configure your source tag, refer to the support documents provided by your ATS partner. They should all have resources available to help you retrieve your source tags.

These resources should contain the following information:

- **ATS name**
- **Name of concept:** how the ATS refers to source tag
- **Example URL:** a sample job link URL with the source tag component bolded
- **Source tag structure:** a generic example of the source tag
- **Cross-session Attribution**: does the ATS support auto-tracking if the candidate leaves the site and then returns? Typically true if the source tag adds a browser cookie.
- **Configuration:** if the ATS requires each source to be configured before it can accept a new source for Handshake, a rough guide will be provided with a link to the exact instructions from the ATS provider

**Note**: If you are currently posting manually on job boards like Indeed, LinkedIn, or Glassdoor, this is likely the same process you've done before if you’re tracking those sites as candidate sources in your ATS.

If you need help configuring your source tag, contact the ATS support team for guidance on locating the correct URL.

### Add a source tag to a new job

Now that you have successfully configured your source tag, you can apply it to a new job in Handshake.

1. Click **Jobs** from the left navigation bar, then click the black **Create Job** button in the upper-right corner of the page.

- To add your source tag to a job post that was saved as a draft, click the white button **View drafts**, then select the job.
- To add your source tag to a job that isn't posted, select the status **Not Posted** from the **Status** dropdown, then select the job.

![Jobs page.png](https://support.joinhandshake.com/hc/article_attachments/25997410903191)

2. In the **Application process** section, add the source tag URL in the **External URL** field, then click the blue **Save** button in the upper-right corner of the section.

![External URL field in Application process section of job form .png](https://support.joinhandshake.com/hc/article_attachments/25997410898583)
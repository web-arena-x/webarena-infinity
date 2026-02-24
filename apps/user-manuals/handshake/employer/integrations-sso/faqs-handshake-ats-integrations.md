# FAQs: Handshake ATS Integrations

Source: https://support.joinhandshake.com/hc/en-us/articles/27605462770711-FAQs-Handshake-ATS-Integrations

---

This article addresses frequently asked questions about integrating your Applicant Tracking System (ATS) with Handshake to streamline candidate management.

*Explore additional resources on our integrations in our Help Center's* [*Integrations & SSO section*](https://support.joinhandshake.com/hc/en-us/sections/1500000844962-Integrations-SSO).

---

### 

### FAQs

**Which ATS does Handshake integrate with?**

**Greenhouse** **Workday** **Lever** **SmartRecruiters** **Jobvite** **UKG Pro** **SAP SuccessFactors** **Taleo** **Infinite BrassRing** (*formerly known as IBM Kenexa BrassRing*)

**Note**: If your ATS is not currently supported, you can still enable direct ATS applications. *Learn how to set this up in* [*How to Use Direct ATS*](https://support.joinhandshake.com/hc/en-us/articles/360004317153).

**How can I integrate my ATS with Handshake?**

To integrate your ATS with Handshake, refer to [How to Integrate your ATS with Handshake](https://support.joinhandshake.com/hc/en-us/articles/26155576618647).

**Is there documentation for integrating Workday and Greenhouse with Handshake?**

Yes, we provide detailed integration guides for both [Greenhouse](https://support.joinhandshake.com/hc/en-us/articles/360058989813) and [Workday](https://support.joinhandshake.com/hc/en-us/articles/6772611653015).

**Can I direct candidates to apply through our ATS?**

Yes, you can set up direct ATS applications. *Learn how to set this up in* [*How to Use Direct ATS*](https://support.joinhandshake.com/hc/en-us/articles/360004317153).

**Are ATS integrations included in the Talent Engagement Suite plan?**

Yes, all Talent Engagement Suite customers can integrate their ATS with Handshake. To get started, refer to the guide provided in the PDF linked in the [Additional resources](#h_01J8JDS0258XWAPJQYK3JMZDSS) section at the bottom of this article.

**What user roles can enable ATS integrations?**

Only owners and admins can enable ATS integrations, as this feature is restricted to those who have access to edit company settings.

**Does Handshake provide Candidate Analysis to know how candidates are engaging with our company?**

Yes. You can work with your account team to complete a Candidate Analysis. Candidate Analysis allows Talent Engagement Suite (TES) customers to upload a list of applicants from an external system and receive insights into which candidates can be attributed to Handshake.

*For more information on uploading data, refer to* [*Candidate Analysis*](https://support.joinhandshake.com/hc/en-us/articles/360052523873).

**Does Handshake use a third-party system for ATS integrations?**

Yes. We use Merge, a trusted API platform that offers Unified APIs that authenticate, normalize, and sync data across API providers so companies like Handshake can easily offer multiple integrations to their end customers.

Developers integrate once with Merge to offer a full category of integrations and easily maintain integration health.

*If you have questions about Merge’s security, visit* [*Merge’s Security Center*](https://www.merge.dev/security) *and* [*Trust Center*](https://trust.merge.dev/).

**How does Merge work with Handshake?**

1. Handshake has an embedded Merge Link in the Handshake platform
2. Employers enter their credentials to their ATS
3. Merge continuously syncs standardized data from their ATS to Handshake

**Where can I find the authentication guide for my ATS?**

Below, you will find links to documentation for various ATS platforms.

- [Lever](https://joinhandshake.integrations.guide/articles/6250014)
- [SmartRecruiters](https://joinhandshake.integrations.guide/articles/5528423)
- [SAP SuccessFactors](https://joinhandshake.integrations.guide/articles/5535520)
- [Taleo](https://joinhandshake.integrations.guide/articles/6203570)
- [UKG Pro](https://joinhandshake.integrations.guide/articles/9251663)

If your ATS is not listed, some providers require direct outreach to obtain an API key. Examples include:

- Infinite BrassRing
- Jobvite
- UKG Pro

**Note****:** **Do not share your API key via email with Handshake support. Input your API key directly into Handshake**.

**What is the candidate's experience once the integration is complete?**

The candidate experience depends on your ATS and where you choose to have candidates apply (Handshake vs. your ATS).

- **Apply on Handshake:** Candidates complete their application directly on Handshake, reducing drop-off rates. Recommended for most cases.
- **Apply in your ATS:** Candidates are redirected to your ATS. Be aware that this may increase candidate drop-off.

**Does Handshake track the candidate’s source in the ATS?**

Yes, Handshake can track the candidate's source. To enable this, set up automated source codes in your ATS.

*For configuration instructions, refer to* [*Setting Up Automated Source Codes for Handshake*](https://support.joinhandshake.com/hc/en-us/articles/27540400245271).

**Can we include screening questions?**

If you use Greenhouse, you can import screening questions from your Greenhouse account into Handshake.

*Learn more about Greenhouse's* [*Custom demographic questions*](https://support.greenhouse.io/hc/en-us/articles/360004588971-Custom-demographic-questions).

**Can I edit the ‘Apply on Handshake’ setting?**

Yes, you have two configuration options:

- **Option #1: Candidates apply externally in your ATS** (i.e. Disable ‘Apply on Handshake’, checked)
 - **Benefits:** Maintains your existing applicant workflow, allowing you to include custom questions at the time of application.
 - **Suggestions:** Candidates apply directly through your ATS, enabling a more detailed application process, including screening questions.
 - **Considerations**:
    - Tracking candidate sources requires a separate setup. *To automate this process, refer to* [*Setting Up Automated Source Codes for Handshake*](https://support.joinhandshake.com/hc/en-us/articles/27540400245271).
    - For Taleo users, ensure the “Allow users to change default ‘External Apply’ URLs” setting is checked.
      - For other ATS systems, we also recommend enabling this for added flexibility
    - Requiring candidates to leave Handshake to apply in your ATS may result in a non-negligible drop-off.
- **Option #2: Candidates apply in Handshake** (i.e. Disable ‘Apply on Handshake’, unchecked)
 - **Benefits:** Minimizes candidate drop-off.
 - **Considerations:** Applications will contain only basic information—name, email, resume, and sometimes a cover letter. If you need additional information, Option #1 may be better suited.

### 

### Additional resources

[Handshake - Admin and Owner Guide for ATS Integration](https://www.canva.com/design/DAGSdmGpy20/yuHExyoXf4fEjqiVuaaPjg/view?utm_content=DAGSdmGpy20&utm_campaign=designshare&utm_medium=link&utm_source=editor#1)
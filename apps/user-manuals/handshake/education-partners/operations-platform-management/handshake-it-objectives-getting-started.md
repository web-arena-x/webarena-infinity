# Handshake IT Objectives: Getting Started

Source: https://support.joinhandshake.com/hc/en-us/articles/360013563933-Handshake-IT-Objectives-Getting-Started

---

There are 3 key objectives to tackle from an IT perspective during your Handshake implementation. Use this guide as your go-to technical resource.

**All IT objectives should be complete ~4 weeks prior to your schools' student invite date.**

This timeline ensures you have a sufficient amount of time to test. If you have any questions about your school's implementation timeline, contact your Career Services point of contact or Support.

# 1. Import Student Data

**When to start:** Tackle this process as soon as you can; this is the highest priority implementation objective.

**Final deadline:** Should be completed no later than 3 weeks prior to your student invite date.

**What it involves:**

- You'll manually upload a list of records from your student information system. Use these instructions to [upload your first student data file.](https://support.joinhandshake.com/hc/en-us/articles/360012405373)
- You’ll need access to the [**Importer Tool**](https://support.joinhandshake.com/hc/en-us/articles/360016070934) to upload the initial student CSV file.
- Coordinate with your Career Services team (explore the contextual guide above) to ensure you’re pulling a list of relevant fields that support their workflows & reporting needs.
- *Please note*: Even if you later plan to automate your student sync, you MUST first set up an account and upload a full student file via the Importer.

# 2. Setup Single Sign-On

**When to start:** You can configure this at any time, as long as the setup points back to the auth\_identifier (or SSO configuration value) imported in your student file.

**Final deadline:** Finalize your configuration no later than 3 weeks prior to your student invite date. Test your SSO setup with a real, imported student account no later than 2 weeks prior to your student invite date.

**What it involves:**

- Use this [Handshake SSO login setup guide](../sso-setup-management/sso-setup-guides-in-app-setup-and-testing.md)to integrate your SSO system with Handshake for student logins. (Choose your configuration: [CAS](https://support.joinhandshake.com/hc/en-us/articles/360012361773), [SAML](https://support.joinhandshake.com/hc/en-us/articles/360012361513), or [LDAP](https://support.joinhandshake.com/hc/en-us/articles/360012362193))
- The attribute you return from this configuration will need to align with the imported auth\_identifier in your student import file. This is typically similar to the SSO configuration you might be using for other vendors on campus.
- Test, test, test! The SSO setup is vital to the student login experience, so once configured, have a real, imported student login on {yourdomain}.joinhandshake.com to confirm.

# 3. Unblock Handshake Emails

**When to start:** You can tackle this at any time (usually only takes a few minutes!).

**Final deadline:** Confirm IPs are unblocked no later than 3 weeks prior to your student invite date.

**What it involves:**

- Use this guide to[**unblock our IP addresses.**](https://support.joinhandshake.com/hc/en-us/articles/360012324954) This will ensure that the student invite, emails sent by your Career Services team, and important notifications (i.e. a student is selected for an interview) always reach your students and staff members.
- *Please note*: The domains listed on that page do not necessarily need to be unblocked, but demonstrate all domains we do send from.

# 4. Optional: Setup an Automated Student Sync

**When to start:** Once you've successfully imported your first student file.

**Final deadline:** Communicate your plans (whether you will or will not automate your sync) to your Career Services team and Handshake Support. Once you do, you can complete at any time.

**Please note:**This step is not required to implement Handshake but can be extremely beneficial for your long term data health.

**What it involves:**

- Use this process to [**automate your student data uploads.**](https://support.joinhandshake.com/hc/en-us/articles/360012323314)
- You’ll either install the AWS CLI or create a script that will send the data file to an Amazon s3 bucket (you can select your preferred cadence for the file to send).
- Once you’ve had a successful test file upload to the s3 bucket (results can be viewed in the importer tool),  proceed to upload your full production file to the s3 bucket. Then, contact Support to request a review.
- Our Support team will review, process that importer job, and then turn on the auto-run option for you!

# Additional Resources:

Hitting a question or want to learn more? Check out some of these related resources:

- [Student Data Formatting FAQs](https://support.joinhandshake.com/hc/en-us/articles/360008607874)
- [About Student Privacy in Handshake](https://support.joinhandshake.com/hc/en-us/articles/360000951508)
- [Handshake SSO Setup](../sso-setup-management/sso-setup-guides-in-app-setup-and-testing.md)
- [Unblocking & Email Delivery](https://support.joinhandshake.com/hc/en-us/articles/360012324954)
- [Security at Handshake](https://www.joinhandshake.com/security/)
- [Common Importer Errors](https://support.joinhandshake.com/hc/en-us/articles/360001032108)
- [How to Re-Upload Failed Rows](https://support.joinhandshake.com/hc/en-us/articles/360006715173)
- [CSV File/Formatting Requirements](https://support.joinhandshake.com/hc/en-us/articles/226346508)
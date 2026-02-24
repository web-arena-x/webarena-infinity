# Importer: Uploading Your First Student File

Source: https://support.joinhandshake.com/hc/en-us/articles/360012405373-Importer-Uploading-Your-First-Student-File

---

Importing student data is a vital step in implementing Handshake. It's the most efficient way to ensure that accurate student information is populated under your Handshake instance. This in turn empowers filtering, outreach, and analytics for Career Services and populates necessary student job qualifications.

# Step 1: Review the CSV File Format

Handshake accepts comma separated value files for upload. Review the expected format here:

- **[Student CSV Reference Guide](https://support.joinhandshake.com/hc/en-us/articles/233086688)**

# Step 2: Make Key Decisions

**Use this time to identify any workflow requirements -** work as a team (both Career Services and IT) to identify the key fields to support the Career Services needs and workflows.

Explore these additional references:

- [**About Student Privacy in Handshake**](https://support.joinhandshake.com/hc/en-us/articles/360000951508)
- **[Student Data Formatting FAQs](https://support.joinhandshake.com/hc/en-us/articles/360008607874)**

### **Chose the Right Attribute for your Student's "username"**

A student's primary unique identifier is their `username`

While students have other identifying attributes that must be unique in Handshake, such as `email_address` or `card_id`, the `username` is expected to **never** change, to **never** be recycled, to **always** belong to that user.

Choosing this identifier carefully will help ensure that the utmost quality data is maintained, and it prevents assigning a new student to an account that already exists, violating a student's privacy.

Decide the username before your initial student upload.

### **Choose the Right Attribute for your Student's "auth\_identifier"**

`auth_identifier` is the value on the student record that ties your SSO integration to the uploaded student record. This value should be the same as the `sso identifier` you put into Handshake.

### **Choose the Right Attribute for your Student's "card\_id"**

`card_id` is only needed if you plan to use the Handshake Checkin Kiosk / Card Swipe. If you do not use this, there is no need to include.

If you are using the kiosk, the `card_id` is the value that Handshake uses to tie the student's card back to their student record when they swipe their card to check in for events, fairs, or appointments. This value must be unique and not change per student. Please ensure that you are only sending us the unique portion of the card. The value *must* be contained within the output of the card swipe.

# Step 3: Review the Importer Training Module for Access

- Anyone who uploads data into Handshake will need access to the Importer. If you don't have access**, you must review the brief training course [here](https://youtu.be/8YXSPIB35I0).**
- Once you have completed the training course, **contact support** so we can add you to the tool!

# Step 4: Extract and Transform your SIS Data to CSV

- [Download the Student CSV Example](https://support.joinhandshake.com/hc/en-us/articles/233086688) to ensure the headers match exactly.
- Extract and transform your student registrar data from your Student Information System to meet the CSV specs.

# Step 5: Upload your File to the Importer

1. Login to the [Importer](https://importer.joinhandshake.com/)
2. Set the Importer job type to **Students**
3. Add a description to your job
4. Click `Save Job`

[![](https://files.readme.io/dd14969-Screenshot_2017-02-22_18.34.29.png)](https://files.readme.io/dd14969-Screenshot_2017-02-22_18.34.29.png)

For common problems with the upload see [here](https://support.joinhandshake.com/hc/en-us/articles/227601827-Importer-Why-is-my-file-failing-as-soon-as-I-upload-it-)

# Step 6: Review and Iterate on your Feedback

The Importer should give you detailed automated feedback on the formatting of your file. It can take a few uploads to perfect the formatting, so **if you're seeing warnings or errors, there are a few things to check:**

- **File Type:** Ensure you have a valid file type
- **Headers:** Confirm all headers & fields match the exact formatting requirements (The Importer will notify you if it finds data that we don't map).
- **Missing Fields:** Determine if values in your file are not registering. If they don't register, they will fail to import.
- **Gut Check:** Conduct a quick gut check on the data you are importing:
  - How many students are you bringing in? How many are you archiving? etc
  - Are you planning to create new accounts or update existing accounts?
  - What new majors, minors, colleges, and/or campuses were found? Should this create new ones or could these be duplicates/typos?

 You can expect to see feedback like this:

[![](https://files.readme.io/4feef9a-Screenshot_2017-02-22_19.02.04.png)](https://files.readme.io/4feef9a-Screenshot_2017-02-22_19.02.04.png)

# Step 7: Submit file for Import

- When your file is ready to import, **click "Submit and Request Run'**
- Our support team will be notified to open a request with you to get your data reviewed and imported.

[![](https://files.readme.io/04f7063-Screenshot_2017-02-22_18.41.06.png)](https://files.readme.io/04f7063-Screenshot_2017-02-22_18.41.06.png)

# More Questions?

Check out these links to learn more about the student data import.

- [Student Data FAQs](https://support.joinhandshake.com/hc/en-us/articles/360008607874)
- [Common Importer Errors](https://support.joinhandshake.com/hc/en-us/articles/360001032108)
- [Re-Uploading Failed Rows](https://support.joinhandshake.com/hc/en-us/articles/360006715173)
- [CSV File/Formatting Requirements](https://support.joinhandshake.com/hc/en-us/articles/226346508)
- [Troubleshooting: Student Card IDs and Preserving Leading Zeros](https://support.joinhandshake.com/hc/en-us/articles/115001027207)
- [Troubleshooting: Importer Date Formatting](https://support.joinhandshake.com/hc/en-us/articles/231942648)
- [Importer Help Center](https://support.joinhandshake.com/hc/en-us/sections/205492607-Importer)
- [Contacting Support](https://support.joinhandshake.com/hc/en-us/articles/28656432275863)
# How To Retrieve Raw Engage Email from S3 (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731498938650-How-To-Retrieve-Raw-Engage-Email-from-S3-Engage-Legacy

---

Engage Email leverages data stored in your AWS S3 storage. The data in S3 is in a raw email format. It is sometimes useful to analyse the raw email that is stored in S3.

Note: The contents of the bucket contain the entire email content in raw form. DO NOT SHARE THE CONTENTS OF PRODUCTION EMAILS unless you explicitly wish Local Measure to be able to access this data.

# Procedure

**Step 1.** First, Identify the contact in Amazon Connect Contact Search. This can be done by navigating to the section Contact Lens → Contact Search in the Amazon Connect UI.

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731474962074)

When identifying contacts, you can use standard attributes such as Initiation Timestamp or Agent. You can also use a custom attribute such as EmailAddress. For custom attributes, these must be configured first.

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731498972698)

**Step 2.** Once the contact is identified, use the Transcript section of the contact history to locate the lmSesEmail tag in the transcript. Copy the section within the quotation (”) marks.

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731466501914)

**Step 3.** Use a [base64 decoder tool](https://www.base64decode.org/) to decode the string copied in Step 2 to locate the email key that resides in S3. You will end up with something like `inbound/fu0318spiku90tt2ejnnf2mnnddfcv9hn59c1vg1`

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731475002522)

‍

You can also use a CLI version of this:

> echo "aW5ib3VuZC9mdTAzMThzcGlrdTkwdHQyZWpubmYybW5uZGRmY3Y5aG41OWMxdmcx" |base64 -d
inbound/fu0318spiku90tt2ejnnf2mnnddfcv9hn59c1vg1

‍

**Step 4.** Navigate to S3 in the AWS Console and locate the email bucket. Navigate to the inbound directory and search for the string yielded in Step 3. Download the contents as a file.

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731462505370)

![__wf_reserved_inherit](https://support.zendesk.com/hc/article_attachments/9731450050970)

‍
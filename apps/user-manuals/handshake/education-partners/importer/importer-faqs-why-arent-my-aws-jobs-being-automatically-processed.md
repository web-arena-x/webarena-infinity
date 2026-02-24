# Importer FAQs: Why aren't my AWS jobs being automatically processed?

Source: https://support.joinhandshake.com/hc/en-us/articles/360051871814-Importer-FAQs-Why-aren-t-my-AWS-jobs-being-automatically-processed

---

Once you've configured the Amazon CLI tool and have successfully sent a file over via AWS, these submissions can be automated - meaning, they will be automatically processed after a successful analysis. This is something that must be enabled by Handshake Support, so you'll need to reach out here to have this enabled (if you haven't already).

If you've already contacted Support to enable autorun, but your files still require manual submission, there are a few reasons why this may be occurring. Make sure to check your file for the following scenarios to ensure that autorun is working as expected:

**1) Your file name contains the word "test" or "sample".**

We will never process a job (manual or AWS) that contains 'test' or 'sample' in the name. You can include either of these words in your filename if you'd like to test the file format for analysis errors, but will need to remove these words when you are ready to submit your file for processing.

**2) 10% or more of the email addresses in your file are being updated to a new email address.**

     Check to ensure emails are being provided in a format consistent with past uploads, as updating a student's email address changes the email they enter for login. If you need to sync personal emails in your AWS uploads, please reach out to Support to allow these emails to be included in your automated uploads moving forward. 

**3) 5****0% or more of the students in your file that aren't skipped have disabled set to TRUE.**

     This is a precautionary measure set in place to ensure that a large portion of your students are not unintentionally disabled. Files of this nature can still be processed, but will require you to log into your Importer account and manually select 'request run' at the bottom of the job's overview page. Importer will first analyze for rows being skipped due to unchanged data and will refrain from processing if 50% of the remaining changed rows have the disabled column set as TRUE.

**4) Any yellow warnings or red error messages BESIDES the following checks:**

Analyzers::Users::DiffCheck:: (unless more than 50% emails updated, see #2) 
Analyzers::TypeCheck:: 
Analyzers::DuplicateAnalysis:: 
Analyzers::Users::HandshakeCheck:: 
Analyzers::RecommendedHeadersPresent:: 
Analyzers::InvalidHeadersPresent::
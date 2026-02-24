# GDPR

Source: https://support.joinhandshake.com/hc/en-us/articles/360003819213-GDPR

---

Europe’s General Data Protection Regulation (GDPR) is in effect, which impacts companies and organizations around the world that handle personal data of EU data subjects, including Handshake and our education partners. Handshake continually strengthens our strong commitment to student privacy, and we want to help our partners do the same.

 We’ve compiled the most frequent questions here for your convenience!

You can also learn more about GDPR and what it is via our blog post, [What You Need to Know About GDPR on Handshake](https://joinhandshake.com/2018/05/07/what-you-need-to-know-about-gdpr-and-your-university-on-handshake.html).

### How should institutions be determining who is an EU GDPR Subject?

GDPR covers activities that occur “within” the EU, so a conservative interpretation may identify GDPR data subjects as EU residents or EU citizens. Some institutions we’ve talked to are using the on-file address for students to determine who is residing in or a citizen of the EU to determine GDPR subject status - but you should check with your legal counsel to determine what is appropriate for your school.

### How do I update my student sync to specify which students are EU GDPR data subjects?

Whether you are using the API directly, or the CSV upload option, it’s as easy as adding the new field ‘eu\_gdpr\_subject’ and specifying “TRUE” or “FALSE”. If you are not specifying this field in your sync we’ll send reminders after each sync to the point of contact you have configured for your student sync. For more information in your student sync, refer to [Importing Student Data](../importer/importing-student-data.md).

If you're having technical trouble with your sync, you can contact our technical support team. 

 If you have other questions around GDPR you can email us at [privacy@joinhandshake.com](mailto:privacy@joinhandshake.com).

### I’m not sure how my student sync works / I’ve never used the importer.

Generally during your implementation there was likely a member of IT from your institution assigned that worked with your office. They should be able to easily update their script or system to include this field. We recommend finding who that internal point of contact is first.

If you no longer have a person who has done this before, here are a few resources to get you started:

- [Requesting Access and Workflow](https://support.joinhandshake.com/hc/en-us/articles/222574167-Importer-Requesting-Access-and-Workflow)
- [Getting Started and Running Your First File](../importer/importer-getting-started-running-your-first-file.md)
- [How to Import Students](https://support.joinhandshake.com/hc/en-us/articles/233086688-Student-Sync-How-to-Import-Students)

### What if I don't import eu\_gdpr\_subject status, and students don't select 'Yes' or 'No'?

By default, eu\_gdpr\_subject is set to 'null' (or 'No') for all students in Handshake, which is also signified by passing 'False' for this field in your imports.  If you are not updating this status, we will assume that none of your students are GDPR subjects.

NOTE: We provide all students the same rights under GDPR regardless of subject status.

### What is a Data Processing Agreement (DPA), and how do I ensure Handshake and my institution have one?

A Data Processing Agreement is an agreement a Controller must have with a Processor they transmit data to that is subject to GDPR. What that means is if you as a institution (Controller) will be processing personal data for students who are protected under GDPR, then you must have a GDPR-compliant Data Processing Agreement with Handshake (Processor) and any other vendors who process or store student data on your behalf. GDPR requires that you as the Controller are only using GDPR-compliant Processors, and having a DPA in place with your Processors contractually ensures that this is the case.  

Additionally, we include DPAs in new contracts by default, so there aren’t any additional steps beyond that. You can check your contract to see if you already have a DPA on file with us.

### Why does my institution fall under GDPR - a European regulation?

GDPR affects all businesses and organizations that process information of natural persons in Europe. This may pertain to your institution if you accept admission information from students located in Europe, if you have a campus in Europe, or if your students do study abroad in Europe. This means that GDPR may impact you, regardless of where your organization is located.

Part of the process of becoming GDPR compliant is identifying students that may be subject to GDPR. Many businesses or organizations may not be working toward GDPR compliance if they believe they do not process information for users subject to GDPR.

Please consult with your institution's counsel to determine if you need to comply with GDPR. If so, you can be confident that Handshake is GDPR compliant - but you will also want to ensure that your other vendors are as well.

Here are some additional resources on how GDPR may affect your institution:

[Inside HigherEd: European Rules (and Big Fines) for American Colleges](https://www.insidehighered.com/news/2018/03/13/colleges-are-still-trying-grasp-meaning-europes-new-digital-privacy-law)

[Inside Higher Ed: E.U. Data-Protection Law Looms](https://www.insidehighered.com/news/2017/11/06/eu-data-protection-law-looms)

### Where do I go for any other questions?

You can reach us at [privacy@joinhandshake.com](mailto:privacy@joinhandshake.com) for any questions about GDPR!
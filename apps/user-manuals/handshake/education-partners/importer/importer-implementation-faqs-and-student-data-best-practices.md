# Importer: Implementation FAQs and Student Data Best Practices

Source: https://support.joinhandshake.com/hc/en-us/articles/360045679113-Importer-Implementation-FAQs-and-Student-Data-Best-Practices

---

- **Q: I am in IMPL and preparing my first student file. What values should I set for the username field and auth\_identifier field (respectively)?**  
    
  **A:**The username value should be a unique value for each student at your institution that doesn’t change. This value serves as an identifier on each student’s account, and is used as the account ‘anchor’ when the Importer is searching for/updating student accounts from your student upload file. We’ve seen many schools use a student’s ID number in this field.  
    
  The auth\_identifier value is only used when SSO is enabled for your institution. This value is used to check against the returned attribute from your external SSO system, to authenticate each student. Students will not enter this value on login, this is a background identifier attribute. Many schools have set this value to match each student’s email\_address, or part of it.

 

- **Q: Can I use more than one format for the card\_id field?**  
    
  **A:** No - at this time, we only support a single format for student card IDs (same number of digits, same formatting, such as number of leading zeros). The reason for this is because our kiosk configuration only supports a single formatting set up. If you upload two sets of card\_id formats, only students with the corresponding format to your kiosk configuration will be able to successfully use their card to swipe/check in to events, fairs, etc.

- **Q: What happens if I try to import student data for a student that is currently pending approval to connect with our school on Handshake?A:**First, ensure that you've allowed Importer to modify identifier data. Learn more about this here: [Importer: What are Sensitive Fields and How Do I Change Them?](https://support.joinhandshake.com/hc/en-us/articles/223411787)  
    
  AWS autorun jobs cannot change identifier data, therefore, the import job must be manual to successfully connect a student to your school.  
    
  If the import job is successful, the student will be approved and added to your Handshake instance. If the import job fails, that means the student was rejected at one point by one of your school's staff members. You will need to reach out to support to connect them to your school.

- **Q: We recycle student email addresses, to save on email domain space. What do you recommend in this situation?**  
    
  **A:** We ***do not*** recommend this practice. The email\_address value is an account identifier on each user’s account, and must be unique across **all of Handshake**. If an incoming student is provided an email address associated with an existing student in Handshake, or an Alumni user, this new student will be able to request a password reset and will gain access to another student’s account (which is a serious security/privacy concern).  
    
  If you are unable to adjust this practice at your institution, extra precautions will need to be taken to ensure that your students’ accounts remain secure. Here is what we recommend:  
    
  For each graduating class (or group of students who is no longer attending your institution), you will need to submit a student upload file that will update all of their email addresses to a generic/personal email.   
    
  If you do not have a personal email address on file for a student, you’ll need to either create a separate institutional/alumni email for them, or create a dummy email address for them. The latter option is not ideal for alumni who should still have access to the platform, in case they require a password reset (in which case, they would never receive a password reset email). This is only something we recommend for alumni users whose access to Handshake will be restricted (i.e. archived). In short:  
    
  ***Do not*** recycle email addresses for alumni/graduate students **unless**:
  - The alumni accounts have been updated with a personal/generic email
  - The alumni accounts have been updated with a dummy email address and archived

- **Q: We use two separate email formats for our students (example:** [**student@handshake.edu**](mailto:student@handshake.edu) **&** [**student@mail.handshake.edu**](mailto:student@mail.handshake.edu)**). Is this recommended?**  
    
  **A:** We strongly recommend ***against*** using two separate email formats for your students in Handshake. The email\_address field is an account identifier that must be unique across *all of Handshake*. If students have access to multiple email formats, they can unintentionally create duplicate accounts in your system (one account can be created under each email format). This can cause confusion and reporting issues, especially if a student has historic data associated with multiple accounts (for example, appointments scheduled under one account, job applications under another account).  
    
  Please select a **single** email format for use in the Handshake platform, and be extremely proactive with communication to your students regarding the format they should be using, and that any accounts under another format will be deleted. If you are still unsure of the best way to move forward for your specific institution, please reach out to your Relationship Manager or the Support Team to open up a discussion with us regarding your next steps.

 

- **Q: We have some students whose names have changed, how do we update this in Handshake?**  
    
  **A:** This is generally a very painless/straightforward process - we want this process to be easy for you so that students are able to request name changes as needed (regardless of the reason)!  
    
  The following fields will need to be updated for a student if they are undergoing a name change:  
    
  **first\_name**: This will need to be updated if a student’s first name is changing.  
    
  **preferred\_name**: Also should be updated if a student’s first name is changing.  
    
  **last\_name**: Update this if a student’s last name is changing (due to marriage/divorce, or another reason).  
    
  The following fields may need to be updated if a student is undergoing a name change (depending on how your student data is uploaded):  
    
  **email\_address**: This will need to be updated if the student’s name is included in their account email address. This can be updated through a standard student upload file (sensitive fields to not need to be enabled for this).  
    
  **username**: If the student’s email\_address is being changed, and you’ve used their email address (or part of it) for their username value. Note that we do not recommend using a student’s email for their username value, due to situations like this. Their username should remain unchanging during their time at your institution. With that being said, if this does need to be updated, it will need to be done in a separate upload from a student’s email\_address update (in order for the Importer to identify which student’s account needs to be updated). You’ll need to submit one upload (non-sensitive fields update) that will update the email address, holding username constant, and a second upload (with sensitive fields enabled) that will update the username.  
    
  **auth\_identifier**: This field will also need to be updated if this value is the same as the student’s email\_address (or contains part of it). This will also need to be updated through a student upload with sensitive fields enabled.

 

- **Q: We have non-standard school years/programs - how does this impact our student upload process? How can we include this information on our students’ accounts?**  
    
  **A:** At this time, we don’t support free text/string values under the **school\_year\_name** or **primary\_education:education\_level\_name** fields - any information listed under these fields will need to adhere to the preset values we have available. If you have non-standard school years, or education levels for your students we recommend a couple of things:  
    
  -Utilize the **system\_label\_names** field for each student, including any additional program information that you’ll need for reporting/filtering/communication purposes. Free text is supported here, and multiple items can be included in a semi-colon separated list. For example:  
    
  **Pre-Med Special Program;Freelance Photographer;Dance Instructor**  
    
  -Do your best to translate these special school years and/or programs into our preset values whenever possible. These values are important for student qualifications/recommendations for job postings in Handshake. Here is an example of how you could adjust a custom school year:   
    
  For a three year program, first years could be separated into Freshman/Sophomores (or even just uploaded as Sophomores, depending on what makes more sense for your program), second years could be set as Juniors, and third years could be set as Seniors.
- **Q: How can I archive or delete an Importer job that I no longer want processed?**  
    
  A: Archiving or deleting an Importer job is something that can only be done by a Handshake admin. This isn't something that is strictly necessary, and won't have any impact on the Importer job itself if it has already begun processing or has completed processing. However, if you'd like to request this, you can do so by contacting our Support team and requesting that a specific Importer job be archived or deleted (please include the job ID or URL in your ticket).
- **Q:  Why did Importer skip student rows?**  
    
  A: Importer will skip student rows for a few potential reasons, and it will call these out in the analysis. The most common reason is that the student data has not changed since the upload immediately previous where that student's identifiers were included. Importer does this to ensure it is not processing redundant data, and facilitates faster processing for all institutions' data. It will call out the number of rows skipped due to unchanged data in the Parse and Generate analysis.   
    
  Importer can also skip if a student is present in multiple rows(Duplicate Analysis), if the email domain belongs to another institution(School Domain Analysis) or if essential information like email\_address is missing for that row.
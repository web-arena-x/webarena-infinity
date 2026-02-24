# Note Assist Guide - Frequently Asked Questions

Source: https://help.elationhealth.com/s/article/Note-Assist-Guide-FAQ

---

# **Frequently Asked Questions**

- [Access & Consent](#access-consent)
 - [Who can use Note Assist?](#qualifications)
 - [What counts as an AI-generated note?](#AI-note_definition)
 - [Why do I only get 10 free AI-generated notes each month?](#allowance_rule)
 - [Do I need patient consent to record the visit?](#consent)
- [Feature Functionalities](#features)
 - [Can I use Note Assist with any web browser?](#browser)
 - [Can I use Note Assist with all visit note formats?](#visit_note_formats)
 - [Why are 2-column visit note formats preferred?](#format_preference)
 - [Can I use Note Assist on a draft note with existing content?](#add_to_content)
 - [Does using a Visit Note Template help?](#visit_note_templates)
 - [How often does Note Assist update the note?](#update_frequency)
 - [What happens if I switch to another patient chart without finishing the recording?](#changing_patients)
 - [What happens if I close the Note Assist dialog before clicking the Finish Recording button?](#close_early)
 - [Is there a time limit for using Note Assist during a visit?](#time_limit)
 - [Does Note Assist require verbal cues to identify sections like the physical exam?](#identify_sections)
 - [Can Note Assist tell the difference between similar terms (e.g. Hypertension vs. Hypotension)?](#similar_terms)
 - [Will chit chat or side conversations be excluded from the visit note?](#chit_chat)
 - [How do I correct mistakes when recording?](#corrections)
 - [Does Note Assist add ICD-10 codes to the Assessment or Billing Details of the visit note draft?](#ICD10)
- [Transcriptions](#transcriptions)
 - [Is my data being used to train AI models?](#training_AI)
 - [Is the transcription created in real-time?](#transcription_creation)
 - [How do I access my transcripts?](#access_transcripts)
 - [How long is the transcript available?](#transcript_availability)
 - [If I amend the visit note, can I still access the transcript of the original Note Assist session?](#amend_note)
 - [If I delete and then restore a visit note draft, is the transcript also restored?](#delete_and_restore)
 - [There's missing information in the Transcript, what should I do?](#transcript_retry)
 - [Can I restore the first version of the transcript after clicking retry?](#transcript_first_version)
- [Technical Specifications & Usage](#technical_specifications)
 - [Do the patient and I need to sit close to the microphone?](#proximity_to_mic)
 - [What happens if I lose internet connection while recording?](#lose_internet)
 - [Can I use Note Assist for telehealth/virtual encounters?](#virtual_visits)
 - [Can I use Note Assist on a mobile device or tablet, if so, do I need to download an application? Which internet browsers are specifically supported on a mobile device/tablet?](#mobile)

##

###

## **Access & Consent**

### **Who can use Note Assist?**

Any Provider-Level User can start using Note Assist right away. Note Assist integrates seamlessly into your everyday workflow, delivering AI-driven documentation directly in your Elation EHR. With your [free monthly allowance of 10 AI-generated notes](https://help.elationemr.com/s/article/Note-Assist-Guide#free_allowance), you immediately save time on charting, reduce administrative burdens, and spend more of your clinical day engaged with patients rather than documentation.

### **What counts as an AI-generated note?**

An AI-generated note is defined as each time you use Note Assist in a visit note - whether the note is signed or deleted.

### **Why do I only get 10 free AI-generated notes each month?**

Your Elation subscription includes 10 AI-generated notes each month at no extra cost, allowing you to experience the benefits of AI-powered documentation firsthand. This helps you see how Note Assist can transform your charting before considering higher volume usage.

### **Do I need patient consent to record the visit?**

Yes, when using Note Assist, you may be subject to laws about recording conversations. These rules vary by location. It's your responsibility to understand the laws where you practice and get your patient’s consent—ideally before or during their visit.

Here’s an example of consent language you can use:

| |
| --- |
| *Some state and federal laws require patient consent to use ambient scribing solutions. Today, I'm using a software tool within my electronic health record system to make it easier to write my medical notes. It helps me spend more time focused on your care, and less time on the computer. This tool will listen to our conversation and convert it into a summary, which I will review and edit for accuracy. The tool will have access to the audio of our conversation during our visit, but it will not be saved. Your medical information will stay private and only shared with those you allow.*   *Do you consent to the use of this tool during our visit today and future visits?* |

[Click here for additional information about Patient Consent Regulations](https://help.elationemr.com/s/article/Patient-Consent-Regulations-Guide).

##

## **Feature Functionalities**

### **Can I use Note Assist with any web browser?**

Note Assist works on:

- **Computer/laptop:** Firefox, Chrome
- **Android devices:** Chrome
- **iPhones/iPads:** Safari

####

### **Can I use Note Assist with all visit note formats?**

**Best supported formats:**

- Complete H&P Note (2 column)
- Complete H&P Note (2 col-A/P)

These formats have more structured sections, so Note Assist can better organize content and avoid overwriting your input.

**Partially supported formats:**

- SOAP Note
- Complete H&P Note (1 column)

These formats are less structured, so formatting may be less organized.

**Unsupported formats:**

- Simple Note
- Pre-op Note
- Non-Visit Note
- Phone Note
- Email Note

Note Assist won’t work at all with these formats—even if you click **Scribe**.

### **Why are 2-column visit note formats preferred?**

2-column visit note formats offer more structure, helping Note Assist better organize the note and avoid overwriting existing content.

Here are more details around how Note Assist detects and populates specific fields in the 2 column Visit Note Formats:

- Vital readings spoken aloud during encounters will be automatically recorded directly into the appropriate vital fields in the visit note.
- Physical evaluations will be recorded in discrete **PE** (Physical Exam) fields.
- Patient instructions will be recorded in the **Care Plan**.
- Symptoms and conditions will be organized in the **HPI** section.
- Diagnoses, including suspect conditions, will be grouped and labeled in the **Assessment** and/or **Plan** sections.
 - Note Assist populates the **Assessment** section with the diagnosis name if your conversation mentions any and this jumpstarts the search for ICD-10 codes in our system. Simply click the name of a diagnosis and the system will launch the diagnosis search to narrow down the search results for you.

ℹ️   **EXCEPTIONS**

Note Assist will not generate data in the **Review of Systems** (ROS) section of any visit note formats at this time.

### **Can I use Note Assist on a draft note with existing content?**

Yes, you can use Note Assist on a draft note that already has content, such as [Visit Note Templates](https://help.elationemr.com/s/article/Note-Assist-Guide-Preparation#visit_note_templates). Note Assist will update the note with new information. If there's a conflict, the new data may replace what's already written.

### **Does using a Visit Note Template help?**

Yes, Visit Note Templates help Note Assist understand what information to include and how to organize the information in the note.

### **How often does Note Assist update the note?**

Note Assist will populate the visit note approximately every five minutes.

### **What happens if I switch to another patient chart without finishing the recording?**

Note Assist only records one chart at a time. If you open a new chart, the previous recording will pause automatically.

### **What happens if I close the Note Assist dialog before clicking the Finish Recording button?**

If you close the Note Assist dialog before clicking the **Finish Recording** button, you will be prompted to

- Click **End Session** to save and stop recording.
- Click **Keep Recording** to continue recording.

### **Is there a time limit for using Note Assist during a visit?**

No, there is no time limit. Note Assist will continue recording and transcribing until you click **Finish Recording**.

### **Does Note Assist require verbal cues to identify sections like the physical exam?**

Verbal cues aren't always required, but they can enhance accuracy. When information could belong to multiple sections, using clear verbal cues ensures it is placed in your intended section.

### **Can Note Assist tell the difference between similar terms (e.g. Hypertension vs. Hypotension)?**

Yes. Note Assist uses speech models and context clues in your conversation to make accurate guesses, similar to a human scribe. For example, if you and your patient are talking about high blood pressure or blood pressure readings that are high, it’s likely to predict that *Hypertension* was what was said and input the correct word.

### **Will chit chat or side conversations be excluded from the visit note?**

Note Assist filters out obvious chit-chat (e.g. parking questions) but may include lifestyle details if they seem relevant.

### **How do I correct mistakes when recording?**

If you made any mistakes while recording, simply speak your corrections and Note Assist will take them into consideration when generating your note contents. You can also pause the recording and start your recording again to speak any corrections.

### **Does Note Assist add ICD-10 codes to the Assessment or Billing Details of the visit note draft?**

Note Assist does not add ICD-10 codes to the visit note draft. However, Note Assist will populate the **Assessment** or **Plan** with the diagnosis name so you can launch the ICD-10 search by clicking on the diagnosis name.

##

## **Transcriptions**

### **Is my data being used to train AI models?**

No, your patient data is not being used to train AI models nor do we allow any of our third party vendors to retain or train on data. We delete patient transcript data after a short period reserved for troubleshooting or data recovery at your request.

##

###

### **Is the transcription created in real-time?**

Yes, the transcription is created real-time. If there are internet issues then the transcription may briefly fall behind, but it will catch up once the internet is stable again.

###

### **How do I access my transcripts?**

Transcripts are stored in the Note Assist dialog, and visible to you, until you sign the visit note. Click **View transcript** in the **Recording Finished** screen to see the transcript.

Once a visit note is signed, Elation keeps the transcript in an archive for 14 days. After that 14 day window, the transcript is erased from our system completely. If you have inquired about a specific transcript via conversations with our Support Team, that transcription may be kept for up to 60 days before it is erased from our system completely.

If you need access to a transcript in our archive, submit a request via **I need help** -> **Contact Elation Support** and a member of our Support Team will be able to assist you.

###

### **How long is the transcript available?**

Once a visit note is signed, Elation keeps the transcript in an archive for 14 days. After that 14 day window, the transcript is erased from our system completely. If you have inquired about a specific transcript via conversations with our Support Team, that transcription may be kept for up to 60 days before it is erased from our system completely.

If you need access to a transcript in our archive, submit a request via **I need help** -> **Contact Elation Support** and a member of our Support Team will be able to assist you.

###

### **Is the recording saved & will I have access to the audio recordings?**

No, the audio recordings are not saved and you will not have access to the audio recordings. Note Assist uses the audio recordings to generate the transcripts continually throughout the visit and then the audio recordings are erased once the transcript is available.

Before a visit note is signed, you will have access to the transcript by clicking **Scribe** and then **Transcript** at the top of the Note Assist dialog.

Once a visit note is signed, Elation keeps the transcript in an archive for 14 days. After that 14 day Note Assist dialog, the transcript is erased from our system completely. If you have inquired about a specific transcript via conversations with our Support Team, that transcription may be kept for up to 60 days before it is erased from our system completely.

If you need access to a transcript in our archive, submit a request via **I need help** -> **Contact Elation Support** and a member of our Support Team will be able to assist you

### **If I amend the visit note, can I still access the transcript of the original Note Assist session?**

Note Assist is not available when amending visit notes.

###

### **If I delete and then restore a visit note draft, is the transcript also restored?**

Yes, the transcript will be restored with the visit note draft.

### **There's missing information in the Transcript, what should I do?**

If the note is inaccurate, you can click the retry ![]() icon to try generating it again. Keep in mind that once you do, you won't be able to go back to the previous version.

### **Can I restore the first version of the transcript after clicking retry?**

No, you won't be able to go back to the previous version once you click retry.

##

## **Technical Specifications & Usage**

### **Do the patient and I need to sit close to the microphone?**

Yes. For best results, stay near the microphone and speak clearly. Check the volume bars or live transcription to confirm audio is being picked up.

### **What happens if I lose internet connection while recording?**

If you lose internet connection, Note Assist will pause recording and resume transcribing once your connection is restored. Previously recorded data will be saved and processed.

### **Can I use Note Assist for telehealth/virtual encounters?**

Yes, you can use Note Assist for telehealth/virtual encounters. However, avoid using headphones. The microphone needs to pick up the patient’s voice through your device’s speakers.

### **Can I use Note Assist on a mobile device or tablet, if so, do I need to download an application? Which internet browsers are specifically supported on a mobile device/tablet?**

Yes, you can use Note Assist on a mobile device or tablet by logging into your EHR through a supported mobile browser. Use Mobile Safari on Apple devices or Mobile Chrome on Android. If the browser isn’t already installed, you may need to download it. Note Assist does not work with the Elation Go Mobile App at this time.


*©2025 Google*

# **Related Articles**

- [Note Assist Introduction (Add-On)](Note-Assist-Guide.md)
- [Note](Note-Assist-Guide-Preparation.md) [Assist Guide - Preparing to use Note Assist](Note-Assist-Guide-Preparation.md)
- [Note Assist Guide - Using Note Assist for encounters](Note-Assist-Guide-Using-Note-Assist.md)
- [Note Assist Guide - Best Practice Recommendations](Note-Assist-Guide-Best-Practice-Recommendations.md)
- [Note Assist Guide - Microphone Set-up and Troubleshooting](Note-Assist-microphone.md)
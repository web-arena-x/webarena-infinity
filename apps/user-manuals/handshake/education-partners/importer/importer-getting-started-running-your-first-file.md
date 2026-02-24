# Importer: Getting Started + Running Your First File

Source: https://support.joinhandshake.com/hc/en-us/articles/115000733727-Importer-Getting-Started-Running-Your-First-File

---

## **What is the Importer?**

The Importer is used both internally at Handshake, and externally by our partners to analyze and import data into Handshake.

## **How does the Importer work?**

You can think of the Importer as a translator between a CSV file and Handshake. It translates a CSV file into JSON that's fed into our API and into Handshake.

The Importer will make changes in Handshake based on the file that is being uploaded. If the information in the file is different from the information in Handshake, that information will be updated accordingly.

## **How do I access the Importer?**

The Importer is an awesome tool, but it is a bit complex and handles a lot of sensitive data, so **we ask that you first watch**[**this video**](https://support.joinhandshake.com/hc/en-us/articles/360016070934)**in our Help Center and follow the instructions in the video.** After finishing, contact our Tech Support team to get access to the Importer.

After you've received access to the Importer, you will be able to import data from an external CSV file into Handshake! This article will provide you with an overview for how to upload your first file.

### **Running a File on the Importer:**

1. Visit <https://importer.joinhandshake.com/>.
2. Click "Upload New CSV" in the upper-right corner of the purple band:![](https://support.joinhandshake.com/hc/article_attachments/25995551191831)
3. Complete the steps below to upload your file:
   1. Choose the file to upload after correctly formatting and saving as a UTF-8 encoded CSV file (more information below).
   2. Choose the correct job type for the data you are uploading (more information below).
   3. Add a description of the data you are importing.
   4. Click "Save Job".

![Importer_page.png](https://support.joinhandshake.com/hc/article_attachments/25995548467223)

4. You will be taken to a page while the importer completes analysis on your file.

![](https://support.joinhandshake.com/hc/article_attachments/25995551196183)

5. Continue to refresh the page until the status reads "Ready for Submission":

![](https://support.joinhandshake.com/hc/article_attachments/25995548470423)

6. Scroll to the bottom of the page to read the agreement prior to running the file. After reading, click the box next to "I agree that this data looks appropriate and understand this import cannot be deleted". Click "Run Job".

![](https://support.joinhandshake.com/hc/article_attachments/25995548472087)

7. You will now be taken to the progress page as the importer processes your file into Handshake:

![](https://support.joinhandshake.com/hc/article_attachments/25995548472599)

8. After the file has completed running, click "View Download Results" in the upper right hand corner.

![](https://support.joinhandshake.com/hc/article_attachments/25995548474135)

9. Next, click "Download Failed Rows CSV" to see the records that failed to process and their associated error messages. More information on resolving Importer errors can be found [here](https://support.joinhandshake.com/hc/en-us/articles/360001032108).

![](https://support.joinhandshake.com/hc/article_attachments/25995551204887)

### **Requesting for a Job to be Processed on the Importer**

### For some importer job types, the Handshake importer team will need to review the file upload prior to running the data into the system to preserve data integrity and prevent any unforeseen challenges. Some examples include a user file where you are updating sensitive fields or if you are trying to import appointment types.

### In these situations, you will not be able to "Run Job" immediately (as outlined in the steps above). Instead, follow steps 1-5 exactly the same. After the importer has completed analysis on your data (step 6), instead of clicking "Run Job", **you will check the agreement box and click the blue bottom that says "Submit and Request Run":**

### 

### Your importer job will go into a queue for the Handshake team to review prior to running the file. You can expect a 24 hour turnaround for your file to be run or to receive feedback from the Handshake team.

### **Importer Job Types**

- **Students**
  - [**Importing Student Data**](https://support.joinhandshake.com/hc/en-us/articles/233086688)
  - This job type will be used to upload all of your student data into Handshake, and will provision accounts for your students. This is a critical step to ensuring ease of student access, and increasing student engagement on the platform.
- **Contacts**
  - [**Importing Employer Contacts**](https://support.joinhandshake.com/hc/en-us/articles/115002887467-Creating-an-Employer-Contact-file-for-Upload-into-Handshake)
  - All contacts that have an invalid email and/or email domain will be pushed back to your team. Feel free to update the contacts' information and send us a new file.
  - Contacts are generally employer or alumni contacts, pulled from your previous system.
  - Prior to the employer launch, you'll want to upload a list of employer contacts into Handshake - This will allow you to mass email, inviting them to join the Handshake platform.
  - Contacts are verified prior to import.
- **Appointments**
  - [**Importing Historical Appointments**](https://support.joinhandshake.com/hc/en-us/articles/115003651627)
  - Appointments are typically imported shortly after the implementation from the previous system to Handshake
- **Appointment Types**
  - [**Importing Appointment Types**](https://support.joinhandshake.com/hc/en-us/articles/115003653787)
  - Appointment types are imported early during implementation, typically when a large number of appointment types exist
- **Events**
  - [**Importing Historical Events**](https://support.joinhandshake.com/hc/en-us/articles/115002420488-Creating-a-Past-Event-File-for-Upload-into-Handshake)
- **Notes**
  - [**Importing Notes**](https://support.joinhandshake.com/hc/en-us/articles/115002426128)
  - Note imports often take place when a school is going through implementation, to pull over historical information. Other times, a staff member may be tracking their notes by some external source and need a way to mass upload those into the system.
  - Notes can be applied to Users (students or career services), Appointments, Events, or Career Fairs.

- **Labels (normal)**
  - [Importing Labels](https://support.joinhandshake.com/hc/en-us/articles/229507687-How-can-I-bulk-upload-labels-for-users-)
  - Can be used for indicating extracurricular activities, [granting permissions](https://support.joinhandshake.com/hc/en-us/articles/219132817-Permissions-in-the-School-Settings), tracking attributes for reporting, concentrations, and many other groups of users

- Labels are generally used to help classify and filter subsets of users (Students, Staff, or Contacts)
- They may also be used on appointments and events, if the [Identifiable ID](https://support.joinhandshake.com/hc/en-us/articles/115000733267) is provided

- **Buildings**
  - [**Importing Buildings**](https://support.joinhandshake.com/hc/en-us/articles/115003775048)
  - Generally only imported pre-implementation and implementation

- **Rooms**
  - [**Importing Rooms**](https://support.joinhandshake.com/hc/en-us/articles/115003775348)
  - Generally only imported pre-implementation and implementation

- **Attendees**
  - [**Importing Attendees to Created Event or Fair**](https://support.joinhandshake.com/hc/en-us/articles/228463888-How-do-I-upload-a-list-of-attendees-to-an-Event-or-Career-Fair-that-already-exists-within-Handshake-)
  - Sometimes, attendees are not tracked directly within Handshake. We can import those attendees to their correct event.
  - If your team is importing attendees frequently, we recommend contacting our Support team to review the current process and consult on how we can transition the registrations and check-ins to occur within Handshake.

Outside of manually importing your data through CSV uploads on the Importer, you can also transfer your student data using AWS S3. The section below will go through this workflow in depth.

[Student Sync: Automating Your Student Sync](https://support.joinhandshake.com/hc/en-us/articles/360012323314) - Student Data Transfer via S3

There are many ways of interacting with S3 to upload data on a regular basis, AWS S3 is very flexible and there are many clients, tools, and services written to interact with its many features.

In order of popularity, here are the methods we see for uploading data to AWS S3:

1. [AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/installing.html) - A simple python based client for uploading data (easiest to use)
2. [S3 Bash](http://tmont.com/blargh/2014/1/uploading-to-s3-in-bash) - A simple upload CLI based using only local unix tools such as curl / openssl for upload (easiest to install)
3. [REST API](http://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html) - The underlying API for AWS S3 (most flexible)

Some common AWS issues

- If your file looks like it's uploading to AWS but NOT to the Importer, then check what characters you are using
  - The following character sets are generally safe for use in key names: Alphanumeric characters: 0-9 a-z A-Z Special characters: ! - \_ . \* ' ( )
  - See [here](http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html) for more information
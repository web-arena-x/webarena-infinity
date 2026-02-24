# Data Migration Guide - How to share your legacy EHR document files with Elation

Source: https://help.elationhealth.com/s/article/How-to-share-legacy-EHR-document-files-with-Elation

---

# **Contents**

- [Overview](#overview)
 - [How do I share my legacy EHR document files with Elation?](#data_sharing_options)
- [Workflow Instructions](#workflow_instructions)
 - [1. Downloading the CyberDuck application](#downloading_CyberDuck)
 - [2. Connecting to your designated server using CyberDuck](#connect_to_S3)
 - [3. Sharing a copy of legacy EHR files with Elation](#move_files_to_CyberDuck)

# **Overview**

## **How do I share my legacy EHR document files with Elation?**

You will use a file transfer application called CyberDuck to share your legacy EHR document files with Elation. CyberDuck is a free and easy to use application. Follow the workflow instructions below to connect to CyberDuck and share your files with Elation.


# **Workflow Instructions**

## **1. Downloading the CyberDuck application**

Select the appropriate download link for your operating system below to download the CyberDuck application. Afterwards install the application to your computer/laptop.

- [For Windows Users](https://update.cyberduck.io/windows/Cyberduck-Installer-8.1.2.36557.exe)
- [For MacOS Users](https://update.cyberduck.io/Cyberduck-8.1.1.36550.zip)

## **2. Connecting to your designated server using CyberDuck**

To connect to your unique S3 server as designated by Elation:

1. Open up the CyberDuck application.
2. Right-Click (Windows) or Two-Finger Click (Mac OS) and select ‘New Bookmark’

![]()

1. A dialog box will open within CyberDuck. Input the following information:
   1. Set the connection type to “Amazon S3”.
   2. Expand ‘More Options’ and paste the information as provided in the .ZIP file sent from [support@elationhealth.com](mailto:support@elationhealth.com).
      - Server Information
      - Access Key ID
      - Secret Access Key
      - Path (including the forward slash)

![]()

1. Close the dialog box once all the above fields have been filled out. You have not established a server connection via this bookmark and you are ready to [share your legacy EHR files with Elation](#move_files_to_CyberDuck).

## **3. Sharing a copy of legacy EHR files with Elation**

To share your legacy EHR files with Elation, upload a copy of the files to the designated folder on your server using CyberDuck.

1. Double-click the newly created bookmark ([from instruction above](#connect_to_S3)). This bookmark will open a connection to Elation's file storage site for your practice.
2. Within a few seconds, you will see a folder in CyberDuck.
3. Drag and drop your data files into the folder.
   - The amount of time it takes to upload your files will depend on the size of your data set. Allow the upload to complete prior to closing CyberDuck.
   - CyberDuck will only store a copy of your data. You will continue to have the copy that was originally on your computer/laptop.
4. Once you have uploaded all your files to this folder in CyberDuck, send an email to your Data Services Manager and let them know your files are ready to be imported by Elation.
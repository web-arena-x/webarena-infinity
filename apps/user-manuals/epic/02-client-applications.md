# Chapter 2: Description of Client Applications

Source: https://downloads.datainterchange.com/Support/Manuals/EPIC/VM-0001-05%20Users%20Guide.pdf

---
## 2.1 Postbag Workstation GUI

## 2.1.1 Overview

The Postbag Workstation client is shown below,
*Figure 27 - The postbag workstation*
Every file in the system is associated with a postbag. The Postbag Workstation allows you to view the details of all files within a given postbag.
Each view in the Postbag Workstation is divided into two main sections. The top section lists the details of each postbag file, while the lower section shows the full audit trail, detailing the events that have taken place on the individual file.
The audit trail is populated whenever you click on a single file in the upper section. The audit contains details of the comms session including File Sent, File Received, File Acknowledged, as well as details of the workflow processing, showing every job that has been executed on the file as it is processed by EPIC, such as Analyse, Map, Split and Copy.

## 2.1.2 Available Views

The following views are available in the Postbag Workstation client,
- Originators Files – Shows the details of the files that belong to the originator.
If you have received a file from a trading partner, then they are the originator of the file.
- Recipients Files – Shows the details of the files that belong to the recipient. If you have sent a file to a trading partner, then they are the recipient of the file.
- Consolidated Files – Shows the combination of file details for both the originator and recipient, displaying all workflow processing as a file has progressed through the system. These details are shown as a single entry in the consolidated files view assuming your system is setup correctly using the ‘Post to Recipient’ job on the Originator’s workflow.
- Archived Files – Shows the details of all the files that have been archived.
This view does not consolidate the files, but instead simply lists all the originator and recipient files that have been archived in the system.
It is possible that these views will need to be refreshed. For example, if a file is received or some workflow processing takes place while the Postbag Workstation client is open. If this is the case, then “Refresh required” will be displayed in the bottom left of the status bar. To refresh the view, simply click View >> Refresh, press F5, or click the refresh icon on the menu bar.

## 2.1.3 Colour Coding

You can see at a glance certain information about postbag files, depending on the colour coding that has been applied to each entry. The same colour scheme is used throughout the Postbag Workstation,
- Pale blue/white = Normal
- Red/pink = Error

## 2.1.4 Using the Postbag Workstation

The Postbag workstation is designed to be used as one of the main day-to-day applications of EPIC. The details of every file in the system will be shown in this application in either the Originator or Recipient Files view.

## 2.1.4.1 Postbag Files

The main list view shows a summary of the file details, including the date and time the file was created, the originator and recipient trading partners involved, and specific file details such as size and document type.
There are however, more details related to each file, if you wish to view these details select a single file from the list and press Enter, click Actions >> File Details, click the image from the menu bar, or simply double click the file in the list directly. Each of these methods will present you with the following dialog,

*Figure 28 - Postbag file details*
The first two tab pages show an overview of the details for this postbag file and are always present. The remaining tab pages are dynamically displayed based on the communications method that corresponds to the current file, these may be OFTP, AS2, X400, etc and will show details of the communications sessions and details that were used to transmit the file.
It is not possible to edit any of the details on this dialog, it is simply for information purposes.
The Refresh button will update the details on the dialog and clicking OK will close it.

## 2.1.4.2 File Analysis

The details of EDI files and IDocs can be summarised by performing an analysis on the postbag file. To do this, select the postbag file from the list and click Actions >> File Analysis. This will bring up the following dialog,

*Figure 29 - File analysis*
The tree view on the left shows a hierarchical representation of the EDI file split into its component parts. Each node below the file node represents an interchange (intermediate hierarchical level) or a message/package (lowest hierarchical level).
The right hand side of this dialog will change depending on what is selected in the tree view. The top level node will display a summary of the whole file, while the nodes at level one correspond to interchanges within the file (UNB-UNZ) and the level two nodes correspond to the messages within that interchange (UNH UNB).
Where there is EDIFACT security information available as part of the file analysis, this will be shown on a separate tab when the file node is selected in the tree view.

## 2.1.4.3 Audit Details

Each postbag file in the system will have events associated with it. These events will be shown in the audit trail on the lower half of the Postbag Workstation.

The audit line events shown in the list view are only a summary of the whole event data. You can view the full details by double clicking an individual event, or highlighting it and clicking Actions >> Audit Details. Either of these methods will bring up the following dialog,
*Figure 30 - Postbag file audit details*
The Details page shows the full details of the event, while the Event Data page lists the full details of the comms file or the workflow parameters that were used and the Job Log page is used to display the log file that was created by this event (if applicable).
If there were errors in a map job then the audit line details for the map job includes a list of the errors in the information section.
The Previous and Next buttons at the bottom of the dialog allow you to step through all the Postbag File Events associated with the selected file.

## 2.2 Administrator’s Workstation GUI

## 2.2.1 Overview

The Administrator’s Workstation client application is shown below,
*Figure 31 - The administrator's workstation*
This application is split into two discrete categories. It shows details of files sent and received via comms together with details of workflow queue items that have been processed.
The comms views have a single section which lists the details of the files that have been received, scheduled, sent or forwarded, while the workflow views are split into two main sections. The top section lists the details of each workflow queue item, while the lower section shows the full audit trail, detailing the events that have taken place on that particular queue item.
The audit trail is populated whenever you click on a single entry in the upper section. The audit contains details of the workflow processing, showing every job that has been executed such as Analyse, Map, Split and Copy.

## 2.2.2 Available Views

## 2.2.2.1 Comms File Views

The following views are associated with comms files,
- Received Files – Shows the details of the files that have been received from an external trading partner.

- Scheduled Files – Shows the details of the files that have been scheduled, but have not yet been sent to their destination.
- Sent Files – Shows the details of the files that have been sent and transmitted to their destination.
- Forward Files – Shows the details of files that have been received and forwarded out again to another trading partner. This view is typically used in a clearing centre environment and is therefore not visible by default.
Regardless of protocol or network, every communications file will appear in one of these tab pages. There are details against each entry that list specific attributes of the comms file, including, originator and destination, file analysis, VFN, dates and times, etc.

## 2.2.2.2 Workflow Processing Views

The following views are associated with workflow processing,
- Inbound Files – Shows the details of workflow queue items that have been processed on files that have been imported into the system.
- Outbound Files – Shows the details of workflow queue items that have been processed on files that are going out of the system.
- Errors – Shows the details of any workflow queue items that have resulted in an error. This view will show all queue items, regardless of whether they are inbound or outbound to the system.
The main list view shows a summary of the workflow queue item details, including, originator and destination, workflow status, files details, dates and times, etc. There is an audit line associated with each workflow queue item which can be seen in the lower half of the application when you click on an individual file. This audit line lists the details of all the jobs that have executed on a workflow and their outcome.

## 2.2.2.3 Refreshing

It is possible that these views will need to be refreshed. For example, if a file is received or some workflow processing takes place while the Administrator’s Workstation client is open. If this is the case, then “Refresh required” will be displayed in the bottom left of the status bar. To refresh the view, simply click View >> Refresh, press F5, or click the refresh icon on the menu bar.

## 2.2.3 Colour Coding

You can see at a glance certain information about comms files and workflow queue items, depending on the colour coding that has been applied to each entry. The same colour scheme is used throughout the Administrator’s Workstation,

**All workstation views:**
- Pale blue/white = Normal
- Red/pink = Error

**Scheduled Files:**
- Red/pink = Has a status of “Send Failed” and will not be sent again
- Yellow = Suspended
- Light orange = One of the following:
- Scheduled with attempts greater than 0
- Partly sent with attempts greater than 1 and a last error
- Partly sent with attempts greater than 2

## 2.2.4 Using the Administrator's Workstation

The Administrator’s Workstation is designed to be used as an administrative tool for viewing and manipulating the comms files and workflow queue items in the system. The communication files will be present in the Received, Scheduled, Sent or Forwarded tab pages, while the workflow processing details will be present in the Inbound, Outbound or Error tab pages.
The main lists views show a summary of either the comms files or the workflow queue items, with details including dates and times, the trading partners involved, the current status and file details including size and document type.

## 2.2.4.1 Comms Files

If you receive a file via comms, then an entry will appear in the Received Files tab page. If you schedule a file to a trading partner, then it will appear in the Scheduled Files tab page until a call is made and the file it transmitted, at which point, the entry will subsequently appear in the Sent Files tab page.
It is possible to view the full details of a communications file by selecting a single entry in the list view and clicking Actions >> Comms File Details, or double clicking the entry. Both of these methods will display the following dialog,

*Figure 32 - Comms file details*
This dialog is dynamically loaded depending on the type of file being viewed and the communications protocol in use.
The Overview tab page shows the details of the parties involved, together with a brief summary of the transmission details including VFN, status and date times.
The File Details and File Analysis tab pages itemise the details of the comms file itself, showing the file status and protocol specific data together with an analysis of the physical EDI file.
Session tab pages will also be present on this dialog detailing the communication sessions that were involved in the transmission of this file.

## 2.2.4.2 Workflow Queue Items

Any file that goes through a workflow will appear in either the Inbound or Outbound tab page. Each workflow queue item is shown as a single entry in the main list view with details relating to the details of the queue item and its current status.
The list view simply shows a summary of the core details, in order to display the full details you must select an individual item and select Actions >> Workflow Details, or double click the single entry. Both of these methods will display the following dialog,
*Figure 33 - Workflow queue item details*
The Overview section displays the current status of the workflow queue item as it progresses through the system, together with a brief outline of the file details.
The Document Details tab page is only relevant to EDI files and recognised non EDI files (such as IDoc files). It gives the analysis-specific details of the file, such as the codes of the originator and destination and the format and type of the file.
The Workflow tab page displays information about the jobs that have been carried out on the file. Current workflow and Current job will only be populated if the file is still being processed.
The Additional Details page shows a list of properties associated with the file, and the value of each property. These fields are currently only used for SAP files and will contain information about the IDoc in the file.

## 2.2.4.3 Audit Trail

The Audit Trail is only applicable to the workflow tab pages. It lists the details of all the jobs that have taken place on a workflow queue item. The list view simply shows a summary of the audit details, in order to view the full details you can either double click a single entry, or select Actions >> Audit Details. Both of these methods will display the following dialog,
*Figure 34 - Audit details*
The Details page provides all the known information about the selected audit line.
The Job parameters page lists all the parameters that were provided for the action to be performed.
If the Job which generated the audit line produced a job log, this will be accessible on a further page tab, entitled Job Log.
If there were errors in a map job then the audit line details for the map job includes a list of the errors in the information section.
The Previous and Next buttons at the bottom of the dialog allow you to step through all the Audit Lines associated with the selected file. If there is only one Audit Line associated with the file, then both the Previous and Next buttons will be disabled.

## 2.3 Communications Monitor GUI

## 2.3.1 Overview

The Communications Monitor client application is shown below,
*Figure 35 - The communications monitor*
The Communications Monitor is a very simple client application that allows you to view details of your current log and all your current and recent communications sessions. Details of finished communications sessions are kept on the screen for 5 minutes, though this value can be configured if you wish, using the Tools >> Options menu option.
The Communications Monitor allows you to see the current status of the communications within the system, including:
- The current status of each active session
- Log details for all sessions in the list
- A list of calls in retry mode, or recently failed.
The screen is divided into two sections: at the top section shows the details of your communications sessions, while the lower section shows the details of your current system log. Note that the system log may contain log messages that are not connected with communications.
It is possible to initiate calls to a trading partner network from the communications monitor application, simply click Actions >> Call Network.

## 2.3.2 Colour Coding

Each line of the comms monitor log is colour-coded as follows,
- Black = Normal
- Blue = Trace/Protocol messages
- Orange = Warning messages
- Red = Error messages

## 2.3.3 Using the Communications Monitor

There is little that can be done from the communications monitor, this clients’ primary use is as a monitoring tool of the communications between you and your trading partners.

## 2.3.3.1 Monitoring a Call

When a transmission is in session with a trading partner, the communications monitor will display the details in the upper section. This will be populated with a unique session ID, the call direction, network, status and start time.
*Figure 36 - Comms in session*
If files are exchanged during a session, a summary will be displayed in this upper section,
*Figure 37 - Comms summary*
The lower section of the communications monitor shows the full details of the session. Depending on the log levels you have setup will determine the level of detail that is displayed.

*Figure 38 - Comms details*
If a call should fail, the failure reason will be present in this view.

## 2.3.3.2 Dismissing a Session

Once a session has completed it will remain, by default, in the upper section of the communications monitor for 5 minutes if successful, or forever if the session failed.
If you wish to clear failed sessions or completed sessions before this time, you must select the sessions in the upper list view, then click Action >> Dismiss.
This will remove the session from the communications monitor, but will not remove any files that may have been transmitted.

## 2.4 ENGDAT Workstation GUI

## 2.4.1 Overview

The EPIC ENGDAT Workstation client application is shown below,
*Figure 39 - The ENGDAT workstation*
The ENGDAT Workstation is a specialised version of the Administrator’s Workstation, designed for the day-to-day exchange and handling of ENGDAT folders between trading partners.
ENGDAT is a specification produced by ODETTE describing how CAD and CAM files can be transferred between two parties.
From the ENGDAT Workstation, you can view received ENGDAT folders, as well as extracting them or submitting them to the workflow manager. You can also edit, delete and create new ENGDAT folders and schedule the folders for transmission.

## 2.4.2 Available Views

The following views are available in the ENGDAT Workstation client,
- Inbound Folder View – Shows ENGDAT folders received from your trading partners. These may have been partly received, received or acknowledged.
- Outbound Folder View – Shows folders created in EPIC. These may have been scheduled for transmission, or sent to a trading partner.

Both views can be customised with filtering, column ordering and sorting.
Individual files in received or scheduled folders can be viewed within the Administrator’s Workstation.

## 2.4.3 Using the ENGDAT Workstation

## 2.4.3.1 Extracting an ENGDAT Folder

Once you have received an ENGDAT folder, you can download all the files contained within that folder from the EPIC server and copy them to a directory of choice on your local machine.
There are three different ways that you can extract an ENGDAT folder, each of which are available from the Actions menu,
- Extract Folder – This allows you to extract the folder and leave the files in the ENGDAT folder unchanged. Any compressed files will remain compressed and the files will be given the same filenames as those on the EPIC server.
- Extract Folder with ENGDAT Filenames – This option will extract the folder, but the extracted files will be named according to the filenames used in the ENGDAT message. Any compressed files will remain compressed.
- Extract and Decompress Folder – This option will extract the folder and decompress and compressed ZIP files in the folder at the same time. The filenames will be set to those used in the ENGDAT message.
Each option displays a standard browser dialogue, which will let you browse for the directory in which to place the extracted files. Once you have selected a directory, click ‘OK’ to extract the ENGDAT files to the directory. Alternatively, you may select ‘Cancel’ to abort the action.

## 2.5 EPIC Monitor GUI

## 2.5.1 Overview

The EPIC Monitor client application is shown below,
*Figure 40 - EPIC Monitor Client*
This monitoring application displays all the connected master and satellite servers in the EPIC farm, listing the details of each server in the lower half.
The diagram shows how the servers are connected and indicates the server name together with the IP Address of the machine where it is running.
If there are no satellite servers connected, then only the master will be displayed.

## 2.5.2 Available Views

## 2.5.2.1 Servers

This section lists the servers that are present in the EPIC farm and provides details of each, including the IP address, number of allocated tasks, runtime and memory usage.

## 2.5.2.2 Tasks

The tasks section lists all the available tasks that can be distributed amongst the EPIC servers. The task name, instance ID and status are all listed, together with the name of the server that is running the individual task.

## 2.5.2.3 Clients

The clients section indicates all the client applications that are connected to the EPIC servers. The machine name, client application and username (if using security) are all listed.

## 2.5.3 Using the EPIC Monitor

There is an automatic refresh feature within the EPIC Monitor which means that this application will update itself with new information every given time interval.
The status of all the servers and tasks will be reflected in the GUI.

# Chapter 3: Frequent Tasks

Source: https://downloads.datainterchange.com/Support/Manuals/EPIC/VM-0001-05%20Users%20Guide.pdf

---
## 3.1 Checking your Postbag for Files

To see the files that are in the postbag of the originator, open the Postbag Workstation and click on the Originators Files view. To see the files that are in the postbag of the recipient, open the Postbag Workstation and click on the Recipients Files view.
*Figure 41 - Postbag files inbound*
For outgoing files, the file originator is the Internal Company and the file’s ultimate recipient is one of the Trading Partners. For incoming files, the file originator is one of the Trading Partners and the file’s ultimate recipient is the Internal Company.
Upon entering the system, postbag files are always given the status of New and will not be available to users until the status has been changed. There are various states that the postbag file can take. These are,
- New – The file has arrived in the postbag and is currently being processed
- Held – The file has been explicitly held and is awaiting manual release
- Released – The file has been released and is available for collection or postage
- Taken – The file has been collected or posted

There is a column that indicates which postbag the file is in and you can limit the views to a single postbag by setting up a filter.

## 3.2 Checking for Received Comms Files

Any files that have been received via comms will show up in both the Postbag Workstation and the Administrator’s Workstation.
To view received comms files from the Postbag Workstation, open the client and select the Originators Files view. Selecting a single file will show the details of the file being received via comms in the audit trail. A file that has been successfully received and acknowledged will show entries including File Receiving, File Received and File Acknowledged.
To view the received comms files from the Administrator’s Workstation, open the client and select the Recipients Files view. There is a File Status column which will show “Received” for files that have been successfully received from a Trading Partner, and “Acknowledged” for files that have been successfully received and acknowledged.

## 3.3 Monitoring Workflow Processing

Any file that is processed on a workflow will show up in both the Postbag Workstation and the Administrator’s Workstation. When a single file is selected in either client, the full details of the progression through the workflow are listed in the audit trail. This allows you to see the processing has taken place on each file and whether there were any errors.
The Postbag Workstation separates files into those in the Originators Postbag (Originators Files view) from those that are in the Recipients Postbag (Recipients Files view).
The Administrator’s Workstation separates files that have come into the system (Inbound Files view) from those that have gone out of the system (Outbound Files view).
In both cases, it is possible to view the workflow processing that has taken place on a file by opening the client, selecting the necessary view (Inbound or Outbound) and selecting the file you wish to see the details of. The audit trail will show the processing stages that have taken place. There is a separate column against the files on a workflow to indicate the status. This will typically show New, Current or Processed depending on the current stage of the workflow processing.
If processing has taken place on a file, then it is possible the view will become out of date. If this is the case then “Refresh required” will be displayed in the bottom left of the status bar. To refresh the view, simply click View >> Refresh, press F5, or click the refresh icon on the menu bar.

## 3.4 Manually Submitting a File to a Workflow / Postbag

Files can be submitted to a Postbag or Workflow directly from either the Administrator’s Workstation or the Postbag Workstation. You may wish to do this if the file has been received by some means other than via comms and you do not want to setup a monitor directory for importing files.
To submit a new file, click Actions >> Submit New File, or click on the icon.
The following dialog will be displayed,
*Figure 42 - Submit new file*
From here, you will need to enter the location of the file to be submitted and then select the postbag that this file is to be submitted to. If you choose to submit the file to the Unsorted Postbag, then you will have to specify the Workflow that is to be used to process this file.
Once you are happy with the details of the file to submit, click the Submit button.
If the submission is successful, you will see the message “File submitted successfully” appear at the bottom of the dialog.
The dialog will remain open, allowing you to submit more files if required.
Click the Close button when you have finished.
The details of your newly submitted file will appear as entries in both the Administrator’s Workstation and the Postbag Workstation (refreshing the views may be required).

## 3.5 Manually Scheduling a File to a Trading Partner

It is possible to schedule a file directly from the Postbag Workstation. This bypasses all workflows, and simply schedules a given file to a trading partner.

To schedule a file, open the Postbag Workstation and click on the Recipient Files view. From here, click Actions >> Schedule File, or click on the schedule file icon . This will open the following dialog,
*Figure 43 - Schedule file*
You can schedule both EDI and Non-EDI files using this dialog. Simply browse for the location of the file on disk, or enter the full path of the file in the text field.
If the file to schedule is an EDI file, then an implicit analysis will take place upon scheduling to determine the originator and recipient. However, if the file is Non EDI, then you will have to specify the Originator and Recipient mailboxes to be used for transmission.
After the file has been selected, you can setup additional details such as the file priority, earliest date/time to send and the virtual filename.
Once you are happy with the file to schedule and the associated details, click the Schedule button. If the file is scheduled successfully, a message to that effect will appear at the bottom of the dialog.
If the earliest transmission date and time is in the past when the dialog is closed, then an automatic call will be made to the Trading Partner and EPIC will attempt to transmit the file.
After the file has been scheduled, it will appear as a single entry in the Postbag of the recipient and no workflow processing will take place on the file. If you wish to submit a file to a specific workflow, please refer to the section entitled ‘Manually Submitting a File to a Workflow / Postbag’.

## 3.6 Checking that an outbound file has been sent

Any file that has been sent to a trading partner will appear in the Sent Files view of the Administrator’s Workstation. There is a Status field that indicates whether the file has been transmitted to the trading partner successfully and whether it has been acknowledged.
It is also possible to view the sent files from the Postbag Workstation. The transmission details will appear as entries in the audit trail of the file in the Recipients Files view. A successful transmission will show Comms File Sending, Comms File Sent and Comms File Acknowledged.

## 3.7 Calling a Trading Partner

There are three ways of manually initiating a call to a trading partner,
- From the Administrator
- From the Administrator’s Workstation and Postbag Workstation
- From the Communications Monitor

When a call is made, all files that have been scheduled for that network will be sent to the trading partner. Similarly, any files waiting to be received will be obtained from the trading partner during the communications session.

## 3.7.1 Administrator

To make a call from the Administrator, start the EPIC Administrator application and open the Comms section. Select the Trading Partner whose connection you want to test and open the Status page. You will be presented with the following tab page,

*Figure 44 - Network status*
The Administrator has the advantage over the over methods in so much that test calls can be made in addition to standard calls.
A test call will initiate a call to the Trading Partner without sending him any data.
However, if the Trading Partner has any data for you, he will send it. A test call can be initiated by clicking the Test call button.
A standard call will initiate a call to the Trading Partner, where any scheduled data will be exchanged between both parties. A standard call can be initiated by clicking the Call button.
Click the Refresh button to see the results of the call. The Files Sent and Files Received fields will show you if any data was exchanged with the Trading Partner during the call.

## 3.7.2 Administrator’s Workstation and Postbag Workstation

Both the Administrator’s Workstation and the Postbag Workstation allow you to initiate calls to a trading partner. Start either application and select Actions >> Call Network or click the call button on the menu bar . The following dialog will be displayed,
*Figure 45 - Call network*
This dialog shows all the external networks (i.e. for trading partners and clearing centres) that are defined in the EPIC system, with their associated protocol and the status of the last attempted call to each network.
Select the network(s) you wish to call and click the Call button. EPIC will attempt to make a connection to the selected network(s) and transmit any relevant files for those networks.
Double-clicking on a network on this dialog will also result in a call being made to that network.

## 3.7.3 Communications Monitor

To make a call from the Communications Monitor, start the EPIC Communications Monitor application and select Actions >> Call Network. You will be presented with the same network selection dialog as in the Administrator’s Workstation and Postbag Workstation, where the operation for making calls remains the same.

## 3.8 Monitoring Calls to a Trading Partner

The Communications Monitor application can be used to see the details of the communications sessions that take place between you and your trading partners.
Whenever a call is made, entries will appear in the communications monitor showing details of the session together with a count for the number of files and acknowledgements that have been transmitted between parties.
The diagram below shows the details of a typical communications session where files have been exchanged between trading partners,
*Figure 46 - Monitoring calls to a trading partner*

## 3.9 Starting / Stopping the Server

Depending on how your system is setup determines how your server should be started and stopped.

## 3.9.1 Starting

If you are running EPIC as an Application then the server is started by clicking Start >> Programs >> Data Interchange Plc >> EPIC >> Server. A small icon should appear in the system tray (bottom right of the Windows Taskbar, next to the clock) automatically starting the server.
It is also possible to start the server using the EPIC Console Window. Simply open the console, type “Start” and press enter.
If running as a System Service, then the server should start when your machine boots up. If this is not the case, then you can view the Windows Services by clicking Start >> Control Panel >> Administrative Tools >> Services. From here, select the EPIC Service and click Action >> Start.
The Windows Services applet is shown below for reference purposes,
*Figure 47 - System services*

## 3.9.2 Stopping

If you are running EPIC as an Application then the server is stopped by right clicking on the EPIC system tray icon (bottom right of the Windows Taskbar, next to the clock) where a context menu will appear. Simply left click on Stop to stop the server, or Shut Down to exit the application completely.
The EPIC Console Window can also be used to stop the server. Simply open the console, type “Stop” and press enter.
If running as a System Service, then the server can be stopped by using the Windows Services applet. Click Start >> Control Panel >> Administrative Tools >> Services to open the list of services on the local machine. From here, select the EPIC Service and click Action >> Stop.

## 3.10 Viewing the Log Files

Logging is a very useful feature of the EPIC software. Most of the time you will probably not come into contact with it, but it can be used to help you sort out any problems, in conjunction with our Support department.
There are various types of log within EPIC: the Server log, the Startup log and the Client logs. The Server log and the Startup log are always used, but the Client logs are an optional feature.
Unless you have given a specific directory in which the server log files should be stored, they will typically be located in one of the following locations,
- C:\Program Files\DIP\EPIC\x.x.x.xxx\Log
- C:\ProgramData\DIP\EPIC\x.x.x.xxx\Log

All log files are stored in plain text format on your PC and can be opened in most common text editors such as Notepad or WordPad.

## 3.11 Changing a Filter

Filters are a useful tool and are available in all client applications. They allow you to restrict what is shown in the view by selecting a given date range, originator / recipient, file status, etc.
A filter can be applied by pressing Ctrl+F, clicking View >> Filter or by clicking on the filter icon from the menu bar , All of these methods will bring up a filter dialog similar to the one shown below,

*Figure 48 - Filter dialog*
From here you can specify various options that will be used to restrict the main list view.
There are different filters depending on the view that is currently active. Details such as companies and postbags are shown in combo boxes, allowing you to choose one, whereas checkboxes and radio buttons may also be present to allow multiple selections of a filterable entity.
The filter will only be applied if you click OK.
The yellow banner just above the list view will show you a summary of the filter details that have been applied.
*Figure 49 - Filter summary banner*

# EPIC User's Guide

Source: https://downloads.datainterchange.com/Support/Manuals/EPIC/VM-0001-05%20Users%20Guide.pdf

---

EPIC
User's Guide
VM-0001-05

Copyright Data Interchange Plc
Peterborough, England, 2012.

All rights reserved. No part of this document may be disclosed to
third parties or reproduced, stored in a retrieval system, or
transmitted in any form or by any means, electronic, mechanical,
photocopying, recording or otherwise, without the prior written
permission of Data Interchange Plc.

This book details the tasks involved in operating EPIC on a daily basis.
This book is intended for people who carry out daily operational tasks using EPIC.
You should be familiar with the business processes within your organization and with basic
computer operation.
System Overview

VM-0001-01
Administrator's Guide

VM-0001-04

About this book:
Who this book is for:
What you need to use this book:
Related Publications:

User's Guide
iii
Table of Contents
1
1.1
1.2
1.2.1
1.3
1.4
1.5
1.6
1.7
1.8
1.8.1
1.8.2
1.8.3
1.8.1
1.8.2
1.8.3
1.8.4
1.8.5
1.8.6
1.9
1.9.1
1.9.2
1.9.3
1.9.4
1.9.5
1.9.6
1.9.7
1.9.8
1.9.9
1.9.10
1.9.11
1.9.12
1.9.13
1.9.14
2
2.1
2.1.1
2.1.2
2.1.3
2.1.4
2.2
2.2.1
2.2.2
2.2.3
2.2.4
2.3
2.3.1
2.3.2
2.3.3
2.4

4
Application Components
2.4.1
2.4.2
2.4.3
2.5
2.5.1
2.5.2
2.5.3
3
3.1
3.2
3.3
3.4
3.5
3.6
3.7
3.7.1
3.7.2
3.7.3
3.8
3.9
3.9.1
3.9.2
3.10
3.11

User's Guide
v
Table of Figures

vi
Application Components

Application Components

1
1
Application Components

## 1.1 Introduction

In this section we will show you what the EPIC applications look like, what their
function is and, in general terms, how to use them. For full details of how to use
each application please refer to the appropriate chapters later in this guide.
The EPIC applications, listed below with their shortcut icons, are:
EPIC Administrator

Postbag Workstation

Administrator’s Workstation

Communications Monitor

ENGDAT Workstation

EPIC Monitor

Batch Administrator

You can start each of the applications from their short cut on your desktop, or
from the Start menu, using Start >> Programs >> Data Interchange Plc >>
EPIC.

## 1.2 EPIC Administrator

The EPIC Administrator is the administrative control centre of EPIC. Before you
can begin to use EPIC to process your files, you must use the EPIC
Administrator to set up all your details, including information about your
company, your trading partners, and your communication details. The EPIC
Administrator is also used to set up the EPIC application to suit your system
requirements.
The usage of the EPIC Administrator is beyond the scope of this document. A
brief overview is given below, however, for full details on how to use this
application to configure your system, please refer to the separate Administrator’s
Guide manual.

2
Application Components

### 1.2.1 What does the Administrator do?

The EPIC Administrator consists of four configuration and management areas –
the System Administrator, the Comms Administrator, the Workflow Administrator
and the Tasks Administrator.

#### 1.2.1.1 System Administrator

The System Administrator is responsible for the administrative aspects of the
EPIC system. It covers such areas as the System Log, System Settings,
Retention Periods, Schedules, Event Actions, Users and User Groups.

#### 1.2.1.2 Comms Administrator

The Comms Administrator is responsible for all matters relating to the EPIC
communication system. It covers such areas as your own company's internal
networks, your trading partners and their communication details, the
communication details of the clearing centres you have accounts with, and sub-
systems.

#### 1.2.1.3 Workflow Administrator

The Workflow Administrator allows you to configure how you want EPIC to
process the files in your system. Its flexibility means that you can process any file
from any trading partner in exactly the way you require. Processing 'channels'
can be defined according to trading partner, data source and data type.

#### 1.2.1.4 Tasks Administrator

The Tasks Administrator contains numerous setup wizards that allow basic
details of the system to be configured. The wizards take you through, in a step
by step process, the details required by EPIC in order to setup the
communications between you and your trading partner.

## 1.3 Postbag Workstation

The Postbag Workstation is one of the core applications of EPIC that you will
typically use on a day-to-day basis.
It allows you to track the files in each postbag within the system, linking the
communications details of files sent and files received, together with any
workflow processing that has taken place on a per file basis.

## 1.4 Administrator’s Workstation

The Administrator’s Workstation is one of the core applications of EPIC that you
will typically use on a day-to-day basis.
Initially, unless restrictions have been made under EPIC security, you can see a
list of inbound and outbound workflow files, files that have been received, sent or

Application Components

3
scheduled via EPIC comms, as well as error files and archived files. You can
also manually schedule files and extract files from the system.

## 1.5 Communications Monitor

The communications monitor allows users to view statistics and live information
about communications sessions in EPIC. This client application is purely a
monitor and therefore has very little functionality.

## 1.6 EPIC Monitor

EPIC can be configured to run in a multi-server environment, dynamically
distributing the workload to individual servers in the farm.
The Server Monitor application lets you view the configuration of your EPIC
system, detailing all master and satellite servers, allowing you to easily
determine the tasks that are running on the individual machines.

## 1.7 Batch Administrator

The EPIC Batch Interface allows you to automate tasks such as setting up new
Comms entries, scheduling files for immediate sending and many other tasks.
If you have a sequence of operations to be performed regularly or if you want
EPIC to be run by non-computer personnel, you may automate it by setting it to
run in batch mode.
The Batch Administrator allows you to configure the settings for running EPIC in
batch mode.

## 1.8 Common Features

There are various features of EPIC that are used throughout the system. These
common features are outlined below.

### 1.8.1 Menu bar

Each application has a menu bar at the top showing several menu options.
Figure 1 - The menu bar
The options common to each application are:

File

View

Tools

Help
Selecting any of these options will present you with further options.

4
Application Components

#### 1.8.1.1 File option

The File menu item contains options allowing you to Log off, Disconnect and
Exit.
The Log off option is applicable only if User Security is enforced. It allows you to
change the user of the application without closing the application down. For full
details of this option see: ”Connecting to the Server”.
The Disconnect option will disconnect the current client application from the
EPIC server. You can reconnect using the Connect button on the "Lost
connection" dialog that appears.
The Exit option will close the current EPIC client application.

#### 1.8.1.2 View option

The View menu item contains a variety of sub-options that differ according to the
application you are looking at. Typical items within the View option include
Refresh and Filter.
The Refresh option will reload the current view, ensuring the most up to date
data is being shown.
The Filter option will bring up a separate dialog, allowing you to apply a filter to
the current view, thereby restricting the data that will be displayed.

#### 1.8.1.3 Tools option

The Tools menu item contains sub-menu items for Options, Upgrade Settings
and Change Password.
The Options dialog allows you to configure certain information within the current
EPIC application. It also allows you to select the language in which you want to
run the current EPIC application. For full details of this dialog, please refer to the
section entitled "Options dialog".
The Upgrade Settings option will only be available if you have any previous
versions of EPIC installed on your computer. This option allows you to copy
settings, such as those from filters and display styles, from a previous version to
the current version. For full details of this option see: “Select Certificate Dialog “
The Change Password option is only applicable if user security is enforced. It
allows you to change your password at any time while using an application. For
full details of this option, please refer to the section entitled "Change password
dialog".

#### 1.8.1.4 Help option

The Help menu item provides access to the page(s) of the EPIC online Help
manual that describe and explain the application, a link to the DIP homepage
and a dialog giving technical details about the application.

Application Components

5

### 1.8.2 Status Bar

The status bar tells you about the status of the current application. It is located at
the very bottom each application where there should be 5 different status boxes.
If there are fewer, it means the application is not connected to the server. You
must be connected to the server in order to use the application.
Figure 2 - The status bar
 Box 1 – tells you the status of the application e.g. Ready. It will also inform
you if the displayed data is out of date – just click the Refresh icon to update
it.
 Box 2 – tells you if the application is connected to or disconnected from the
server
 Server – tells you the name of the application running on the server to which
the application is connected (in this case, EPIC)
 Machine – tells you the name of the machine (computer) on which the server
is installed
 Username – tells you the logon name of the user who is currently using the
application (this is only applicable if user security is being used)

### 1.8.3 Tab pages

Tabs allow you to see different pages of the screen you are looking at. They are
usually found at the top of the information on the screen, and look like the page
markers of a binder. Each tab displays an icon and a caption, to indicate the
contents of the page it is marking. Simply click on the tab with your mouse to
open that page.
Figure 3 - Tab pages

### 1.8.1 Default tab pages

Whenever a tab page is used to separate details within EPIC, a default tab page
option will be available. The default tab page is the one that will be shown to you
first. Typically, the default page will be the first tab that is available.
If you want to change the default page setting for any section, this is how they
work.

6
Application Components
At the top of every tab page is a title banner (typically yellow), at the right-hand
side of which is the default page tickbox. If the box is ticked, it indicates that this
is the default page for this section. If you prefer a different page to be the default,
simply select the tickbox from one of the other pages. Next time you open up this
section, the default page will be the one you have chosen.

### 1.8.2 Mandatory fields

Within most of the EPIC applications, there are dialogs which require you to
provide information. Some of this information is optional i.e. you may provide it if
you wish or omit it if you prefer. Other information is mandatory i.e. you must
provide it before EPIC will allow you to close that dialog. All mandatory fields
have been given a bright blue background.

### 1.8.3 Context menus

A context menu is a dynamically loaded list of options and actions that can be
performed depending on the area of the application your mouse cursor is
residing.
Context menus are not visible until you hold your mouse over the data area of a
page and click the right mouse button.  A menu will then appear next to the
cursor, from which you can select an option by highlight it and pressing the left
mouse button.
Figure 4 - Context menu
1.8.4
"Hot" keys
For people who prefer to use the keyboard rather than the mouse, a hot key can
be used as a quick way to get at menu options from the menu bar.
To use the menu bar with the keyboard, press the Alt key to make the "hot keys"
visible on the menu bar. Each option on the menu bar will now have a letter
underlined to indicate the hot key. Having pressed the Alt key, press the letter
indicated by the hot key of the option you want e.g. Alt+F for the File options.
This will show you a dropdown menu which you can then navigate in two ways.

Application Components

7
One way is by using the up and down arrow keys on your keyboard. When the
option you want is highlighted, hit the Enter key to select it.
The other way is by using the hot key of the dropdown menu item you want (the
hot key will be indicated by being underlined). To use the appropriate hot key,
just press the matching letter on the keyboard. This method is indicated in the
user guide by the convention Alt+F+P for example.
Hot keys are also used on dialog buttons in exactly the same way.

### 1.8.5 Short cuts

Short cuts are something you will become familiar with as you use EPIC. They
allow you to get to menu options directly instead of making your way via
dropdown menus etc.  When you begin, if you are using the menu bar options,
you will see that alongside some of the dropdown options is a reference to one
or more keyboard keys. For example, if you select the View menu option, the
resulting dropdown menu shows Filter…. Ctrl+F and Refresh F5. These are the
short cuts for these particular options. Once you have remembered the short cut
keys, you can use the short cut from the main view to go straight to the option.
For example, pressing Ctrl+F from the Inbound Files view within the Workstation
will take you straight to the Inbound Files filter dialog.

### 1.8.6 Radio buttons

These are a feature of some dialogs, such as filter dialogs. Radio buttons allow
you to choose between two or more mutually exclusive options. Their
appearance is of a small white circle alongside a description of each option. The
currently chosen option is indicated by a black spot in the radio button.

## 1.9 Common dialogs

There are several dialogs that you may come across in any of the EPIC
applications. These are described below.

### 1.9.1 Connecting to the Server

EPIC runs on a client-server architecture. This means that each client application
must know where the server is in order to connect to it. By default, the client
applications point to the local machine (127.0.0.1).
If a client cannot connect to the server, or the connection is lost for some reason,
you will be presented with the following dialog,

8
Application Components
Figure 5 - Could not connect
The message box will show a countdown from 30 seconds, at which point the
application will attempt to connect to the server again. If you want to try and
connect to the server before the countdown ends, press the Connect button. If
the connection still cannot be made, the message box will appear again.
If you do not press the Connect button, the application will try to connect to the
server every 30 seconds until it is successful.
There are several possible reasons why you might be unable to connect to the
server, such as:

The server has been shut down

The server's cable has become unplugged

The server has been renamed

The server has been moved from one machine to another
If you have reason to believe that the server has been renamed, or that the
location of the server has changed, press the Server button. This will expand the
dialog to show you the current information about the name and location of the
server.

Application Components

9
Figure 6 - Server details
If you know the new location or new server name, type it into the Server machine
field (this accepts both IP Addresses and Hostnames). If necessary, type the
new port number into the Port field too. If the server is configured such that you
are required to use SSL to connect, select the check box. If necessary, enter the
port number and click the button to the right of the field to select an SSL
certificate. For more information on selecting a certificate, see the section
entitled ‘Select Certificate Dialog’.
Now click the Connect button again. If you are still unable to gain a connection to
the server after this, please refer to your IT Manager.
If you want to stop trying to connect, press the Exit button.

### 1.9.2 Logon dialog

The Logon dialog will only be a feature of EPIC if User Security is being
enforced.
If you are using User Security, the Logon dialog will appear whenever you try to
start an EPIC application or whenever you select the File >> Log Off option from
any of the EPIC applications. Logging off enables another user to log on without
having to close the application first.
If logging off, you will first be asked if you are sure you want to log off the current
user, with the message box below (the banner content will depend on which
application you are currently logged on to).

10
Application Components
Figure 7 - Logoff confirmation
Click Yes to proceed with the logoff, or No to remain logged on.
If you click Yes, or if you are starting an application, you will then see the
following dialog:
Figure 8 - Logon credentials
If logging off, you can now leave the computer, ready for the next user to come
along.
The next user types his username in the Username field, and, if he has been set
up to use passwords, his password in the Password field.
There are a few rules about the characters that may be used in the password:
The password must contain at least 5 characters, up to a maximum of 12
characters
The password must be alphanumeric i.e. it may only include numbers and letters
and the underscore character (no punctuation and no spaces are permitted)
The password is case sensitive.
Click OK to proceed with the logging on of the new user, or Exit if you have
decided instead to close the application.

### 1.9.3 Change password dialog

The Change password dialog will only be a feature of EPIC if User Security is
being enforced.
The Change password dialog, shown below, will appear if you select the Tools
>> Change password option from any of the EPIC applications.

Application Components

11
Figure 9 - Change password
This dialog allows you to change the password of the user who is currently
logged on to the application from which you have opened the dialog.
The password of someone who is not logged on can only be changed from the
Users section of the EPIC Administrator.
Type in the current password of the user in the Old password field.
Type in the new password in the New password field.
Type the same new password in the Confirm password field.
There are a few rules about the characters that may be used in the password:
The password must contain at least 5 characters, up to a maximum of 12
characters
The password must be alphanumeric i.e. it may only include numbers and letters
and the underscore character (no punctuation and no spaces are permitted)
The password is case sensitive.
Click OK to keep the new password, or Cancel to keep the current password.

### 1.9.4 Options dialog

An Options dialog is accessible from each of the EPIC applications. The settings
shown in the Options dialog are only applicable to the application in which you
are viewing them. Likewise, any changes you make will only affect the particular
application in which you make those changes.
The Options dialog in the Communications Monitor has an extra page that is
described in the "Comms Monitor Options dialog" section below.
When you click on the Tools >> Options menu item, you will see the following
dialog.

12
Application Components
Figure 10- The options dialog
All the Options dialogs share four common tab pages, Language, Logging,
Colours and Server.

#### 1.9.4.1 Language page

The Language page dialog is shown below.
Figure 11 - Language settings
This page allows you to change the language in which the application is
displayed. Changes made here affect most of the text displayed in the

Application Components

13
application, including text on buttons, page tabs, field captions and most reports.
It does not change the language of the Help files.
Use the dropdown arrow to view the available languages – there are numerous
languages available including English, German (Deutsch), Spanish (Español),
French (Français) and Chinese (simplified). If you select a different language you
will see a message warning that you will have to close the application before the
change can take effect.
Click the OK button to return to the Options dialog. You may continue to use
EPIC until it is convenient for you to close it down. Then next time you open that
application, the language change will take effect.

#### 1.9.4.2 Logging page

The Logging page dialog is shown below.
Figure 12 - Logging settings (Disabled)
When you first open the Logging page, none of the fields are enabled i.e. you
cannot edit them. This is because, most of the time, you will never need to use
client-side logging.
By default, no log messages are generated by the applications – all log
messages in the System Log refer only to activity on the EPIC Server. Server log
messages can be viewed using the System Log section of the EPIC System
Administrator.
If you want to change the settings of the client side log settings, place a tick in
the "Enable client side logging" tick box. This will enable all the fields, as shown
in the dialog below.

14
Application Components
Figure 13 - Logging settings (Enabled)
You can now choose a directory to which the log messages for this application
will be written. You may type in a directory of your choice, but the default
directory will take the form of one of the following (depending on your operating
system),
C:\Users\Username\AppData\Local\DIP\EPIC\Installation Directory\Log\
C:\Documents
and
Settings\Username\Local
Settings\Application
Data\DIP\EPIC\Installation Directory\Log\
Where Installation Directory indicates the current build you have installed e.g.
1.0.0.025.
The files in each of these log directories will be named according to the following
naming convention:

The first 3 characters represent the type of log file (e.g. PBG for the Postbag
Workstation)

The next 8 digits will be the date of the log in DDMMYYYY format (in the
example below, the date is 24072008 i.e. July 24th 2008)

The next 6 digits will be the time of the log in HHMMSS format (in the
example below, the time is 101741 i.e. 10:17a.m. and 41 seconds.

Each file ends with .log

Example – PBG24072008101741.log
Using the Logging page you can also choose how much information, and of what
kind, is written to the client log. There are three message types to choose from.
By default, only General messages are selected, as these are probably the most
useful for general purposes. If more detailed information is required by our

Application Components

15
Support department, they may suggest that you select one or more of the
remaining message types too.

#### 1.9.4.3 Colours page

The colours page dialog is shown below,
Figure 14 - Colour settings
This allows you to specify the colour scheme that is used for the banner text and
backgrounds visible in the EPIC application.

#### 1.9.4.4 Server page

The server page dialog is shown below,

16
Application Components
Figure 15 - Server settings
This section allows you to configure the details that the client application uses to
connect to the EPIC server. There are two main sections, Server details and SSL
details.
The Server details are mandatory as these specify the IP address and port of the
server that the application is connecting to.
The SSL details are only required if you are connecting to the server over a
secure connection. If you wish to use SSL, tick the box named ‘Use SSL’. You
will then have to provide the SSL port of the server you are connecting to and the
certificate that is being used for the SSL connection.

### 1.9.5 Comms Monitor Options dialog

The Comms Monitor options dialog has an extra page, described below. For
details of the other pages, please refer to the section entitled "Options dialog".

Application Components

17
Figure 16 - Communications monitor view options
This dialog is divided into two sections: Finished sessions and Failed sessions.
The default setting for finished sessions is to remove them from the Comms
Monitor view after 5 minutes. You can change the number of minutes to suit your
system. If required, you can temporarily select the "Keep finished sessions
forever" option. Once you have deselected it again, the normal operation will
commence once more.
The default setting for failed sessions is to keep them in the Comms Monitor
view forever. This enables you to see how many failed sessions have occurred
and to investigate the reason why. Any failed sessions that you are no longer
interested in can be removed from the Comms Monitor view using the Dismiss
option from the main menu.

### 1.9.6 Select Certificate Dialog

The Select Certificate dialog allows you to choose the certificate to encrypt and
or sign data.

18
Application Components
Figure 17 - Select certificate
Use the Certificate store dropdown to select the appropriate certificate store i.e.
the store where the certificate you want to use is kept and the Certificate
dropdown to select the individual certificate you want to use.
If the certificate store you have selected contains no key certificates of the type
you require (i.e. private or public, depending on the function for which you are
selecting the certificate), the Certificate field will display a message to that effect,
telling you to select another store.
The Properties section shows the details relating to the selected certificate.
Properties include:

Whether or not the certificate encapsulates a private key

The signature algorithm

Issuer details

Validity dates
The validity of the certificate will be displayed using one of the following images,

The certificate is valid

The certificate is invalid
If the certificate is invalid, then the first line of the properties will indicate the
failure reason.
If the certificate you want is not held in any of the certificate stores in the
dropdown list, you can import another certificate by clicking on the Import button.
This will bring up the ‘Import Certificate Dialog’.

Application Components

19
If you are unable to select or import a certificate, you can create your own
certificate by clicking on the Create button. This will bring up the ‘Create
Certificate Dialog’ dialog.

### 1.9.7 Import Certificate Dialog

The import certificate dialog allows you to import a certificate from a file into your
system. It is possible to import certificates in any of the following formats,

PFX: Personal Information Exchange – PKCS#12

P7B: Cryptographic Message System – PKCS#7

CER/PEM: Encoded X.509 Certificate
The following dialog allows you to perform the certificate import,
Figure 18 - Import certificate
If you know the path of the certificate file you wish to import, then type it into the
Certificate file field. If you prefer to browse for the file on disk, then click the
Browse button.
Once you have selected a certificate file, the certificate dropdown list will be
populated with a list of certificates that the file contains (in most cases a
certificate file contains a single certificate, but sometimes it contains more). Use
the dropdown arrow to select the certificate you want from that file. Any
properties of that certificate will be displayed in the Properties section.
Click the Import button to complete the import process and return to the ‘Select
Certificate Dialog’.

### 1.9.8 Create Certificate Dialog

This dialog allows you to create a self-signed certificate with a private key and
install it in the root certificate store. Self-signing allows you to create a trusted
certificate without needing to obtain one from a third-party issuer.

20
Application Components
Figure 19 - Create certificate
The issuer details allow you to provide information that can be viewed in the
Properties section when choosing a certificate. You may specify the details for
the Common Name and Organisation which you wish to give to this certificate as
well as the Organisation Unit that this certificate is to be associated and the
country in which this certificate was issued.
If you wish to export the public key for this certificate to another file, select the
Export tickbox and use the Browse button to choose the name and location of
the file where you want to export it.
Once you have provided the required details, click the Create button to create
the certificate. You will be returned to the ‘Select Certificate Dialog’, where you
will now see that your self-signed certificate has been added to the root
certificate store and can be selected. The Issuer details you provided on the
Create certificate dialog can be viewed in the Properties section against the
‘Issuer’ caption.

### 1.9.9 Upgrade settings dialog

The Upgrade EPIC settings dialog is the same for all applications, though each
will refer to the application you are currently using.

Application Components

21
Figure 20 – Upgrade settings
To upgrade your settings, you need to select a previous version of EPIC to
upgrade from.
Previous versions that have been installed in the default EPIC installation
directory will be listed in the main window of this dialog, so you will normally just
select one of them to upgrade from, by highlighting it.
If you have installed a previous version of EPIC somewhere other than in the
default directory, you can use the Browse button to find it.
If you use the Browse button, you will see the Select settings file dialog, as
shown below.
Figure 21 - Browse for settings configuration file
The file type you have to use (i.e. the appropriate configuration file) will be
provided for you in the 'Files of type' field. You need to search for a file with that

22
Application Components
name in the directory where you have installed a previous version of EPIC.
When you have found it, double-click on it to return to the Upgrade EPIC settings
dialog, where the directory name will now be displayed in the field alongside the
Browse button.
Having selected the previous version to upgrade from, click the Upgrade button
to proceed with the upgrade. Or click the Cancel button to abandon the upgrade
procedure.
If you proceed with the upgrade, you will then see the following message box,
informing you that the upgrade was successful.
Figure 22 - Settings upgraded
Click OK to return to the application you are using.

### 1.9.10 Timeout dialog

The Timeout dialog may appear when you have requested EPIC to do something
that may take a few minutes to complete. It gives you the option to cancel the
request if you wish.
If you want to cancel the request, click the Cancel button. You will be returned to
the previous screen.
If you prefer to wait until the action has been completed, you need take no
action.

### 1.9.11 Waiting for Response dialog

The Waiting for Response dialog may appear when you have requested EPIC to
do something that may take a few minutes to complete.
This dialog does not give you the option to cancel your request. The type of
action you have requested is one that must be completed before control is
returned to you.

### 1.9.12 Help About… dialog

The Help About dialog is accessible from the menu bar of any of the EPIC
applications. Click Help >> About Application, where Application is the name of
the application you are currently looking at. The example below shows the Help
About dialog from the Postbag Workstation application.

Application Components

23
Figure 23 - About dialog
This dialog is divided into three sections: Product details, Registration details and
Data Interchange Plc.
The Product details section shows the version of the Client application and the
EPIC Server. These details are important and should be quoted if you ever need
to contact Data Interchange Plc for support purposes.
The Registration Details section shows the registered User Name, your
Company name and the product Serial Number. These details should also be
quoted if you ever need to contact Data Interchange Plc for support purposes.
The final section gives the contact details for Data Interchange Plc. You will need
these if you ever have to contact Data Interchange Plc for support purposes.

### 1.9.13 Displayed Tab Pages

It is possible to change the tab pages that are displayed within the workstation
applications. For example, you may wish to turn off the Received Files view in
the Administrator’s Workstation if you only use EPIC to send files.
The view manager can be accessed from the main menu, using View >> Views
which will present you with the following dialog,

24
Application Components
Figure 24 - View manager
This dialog lists all the available views for the current application, together with a
description of what each displays and whether the view is currently Shown or
Hidden.
To Show or Hide any of the views, highlight the appropriate line and click the
Show or Hide button, as appropriate. The value in the Shown column will
indicate the change you have made.
Click OK to save the changes and return to the current files view with the new
tab page selections applied, or Cancel to quit the dialog without saving your
changes.

### 1.9.14 Visible Columns

The columns that are displayed in the workstation clients are fully customisable.
It is possible to switch individual columns on and off, change the order that they
appear and alter the order for sorting the data.
The column editor can be accessed from the main menu, using View >>
Columns which will present you wish the following dialog:

Application Components

25
Figure 25 - Column editor (display order)

#### 1.9.14.1 Display Order

The display order shows all the columns that can be configured in the main
display view. The left hand side shows the columns (in display order) that are
already visible in the current files view, while the right hand side shows the
columns (in alphabetical order) that are currently hidden from the view.
To make hidden columns visible, highlight the required Hidden column(s) and
click the Add button.
To hide visible columns, highlight the required Visible column(s) and click the
Remove button.
Once you have decided on the columns you want to be displayed, you can alter
the order in which they are shown on the screen by using the Move buttons.
Highlight one or more Visible columns and click the Up or Down button to move
the selected column(s) up or down one position in the list. Repeat until the
column(s) are in the position in which you want them to appear.
The top-to-bottom order of the columns in the list will be their left-to-right order
when they are displayed on the screen.
If you want to restore the default column settings for the view, simply click the
Defaults button.

#### 1.9.14.2 Sort Order

The Sort Order section of the column editor dialog is shown below,

26
Application Components
Figure 26 - Column editor (sort order)
Here you can determine how the contents of the columns are to be sorted.
This dialog lists all the available columns, not just those that will be displayed on
the screen. This means that the sort order of displayed columns can be affected
by the sort order of hidden columns.
The three Sort buttons are used to determine the order the data is displayed in
the view. The sort direction can be changed by highlight one or more items in the
list and clicking the appropriate Sort button,

Sort in an Ascending fashion

Do not sort by this column

Sort in a Descending fashion
Use the two Move buttons to change the priority in which columns will be sorted.
Highlight one or more items in the list and click the appropriate arrow button to
move the selected column(s) up or down one position in the list. Repeat until the
column(s) are in the position in which you want them. N.B. This does not affect
the order of the actual columns, but does affect the order the data is displayed.
If you are not interested in sorting any columns by value, simply leave the Sort
direction of all the columns as None (the default option). If all columns are set to
None, the order of columns in the list will not have any effect on the way data is
displayed on screen.
If you want to restore the default column settings for the view, simply click the
Defaults button.

Application Components

27
Once you are happy with the column arrangement and sort order, click OK to
save your changes and return to the Current Files page, or click Cancel to leave
this dialog without saving your changes.

Description of Client Applications

29
2
Description of Client Applications

## 2.1 Postbag Workstation GUI

### 2.1.1 Overview

The Postbag Workstation client is shown below,
Figure 27 - The postbag workstation
Every file in the system is associated with a postbag. The Postbag Workstation
allows you to view the details of all files within a given postbag.
Each view in the Postbag Workstation is divided into two main sections. The top
section lists the details of each postbag file, while the lower section shows the
full audit trail, detailing the events that have taken place on the individual file.
The audit trail is populated whenever you click on a single file in the upper
section. The audit contains details of the comms session including File Sent, File
Received, File Acknowledged, as well as details of the workflow processing,
showing every job that has been executed on the file as it is processed by EPIC,
such as Analyse, Map, Split and Copy.

### 2.1.2 Available Views

The following views are available in the Postbag Workstation client,

30
Description of Client Applications
 Originators Files – Shows the details of the files that belong to the originator.
If you have received a file from a trading partner, then they are the originator
of the file.
 Recipients Files – Shows the details of the files that belong to the recipient. If
you have sent a file to a trading partner, then they are the recipient of the file.
 Consolidated Files – Shows the combination of file details for both the
originator and recipient, displaying all workflow processing as a file has
progressed through the system. These details are shown as a single entry in
the consolidated files view assuming your system is setup correctly using the
‘Post to Recipient’ job on the Originator’s workflow.
 Archived Files – Shows the details of all the files that have been archived.
This view does not consolidate the files, but instead simply lists all the
originator and recipient files that have been archived in the system.
It is possible that these views will need to be refreshed. For example, if a file is
received or some workflow processing takes place while the Postbag
Workstation client is open. If this is the case, then “Refresh required” will be
displayed in the bottom left of the status bar. To refresh the view, simply click
View >> Refresh, press F5, or click the refresh icon on the menu bar
.

### 2.1.3 Colour Coding

You can see at a glance certain information about postbag files, depending on
the colour coding that has been applied to each entry. The same colour scheme
is used throughout the Postbag Workstation,

Pale blue/white = Normal

Red/pink = Error

### 2.1.4 Using the Postbag Workstation

The Postbag workstation is designed to be used as one of the main day-to-day
applications of EPIC. The details of every file in the system will be shown in this
application in either the Originator or Recipient Files view.

#### 2.1.4.1 Postbag Files

The main list view shows a summary of the file details, including the date and
time the file was created, the originator and recipient trading partners involved,
and specific file details such as size and document type.
There are however, more details related to each file, if you wish to view these
details select a single file from the list and press Enter, click Actions >> File
Details, click the
image from the menu bar, or simply double click the file in
the list directly. Each of these methods will present you with the following dialog,

Description of Client Applications

31
Figure 28 - Postbag file details
The first two tab pages show an overview of the details for this postbag file and
are always present. The remaining tab pages are dynamically displayed based
on the communications method that corresponds to the current file, these may
be OFTP, AS2, X400, etc and will show details of the communications sessions
and details that were used to transmit the file.
It is not possible to edit any of the details on this dialog, it is simply for
information purposes.
The Refresh button will update the details on the dialog and clicking OK will
close it.

#### 2.1.4.2 File Analysis

The details of EDI files and IDocs can be summarised by performing an analysis
on the postbag file. To do this, select the postbag file from the list and click
Actions >> File Analysis. This will bring up the following dialog,

32
Description of Client Applications
Figure 29 - File analysis
The tree view on the left shows a hierarchical representation of the EDI file split
into its component parts. Each node below the file node represents an
interchange (intermediate hierarchical level) or a message/package (lowest
hierarchical level).
The right hand side of this dialog will change depending on what is selected in
the tree view. The top level node will display a summary of the whole file, while
the nodes at level one correspond to interchanges within the file (UNB-UNZ) and
the level two nodes correspond to the messages within that interchange (UNH-
UNB).
Where there is EDIFACT security information available as part of the file
analysis, this will be shown on a separate tab when the file node is selected in
the tree view.

#### 2.1.4.3 Audit Details

Each postbag file in the system will have events associated with it. These events
will be shown in the audit trail on the lower half of the Postbag Workstation.

Description of Client Applications

33
The audit line events shown in the list view are only a summary of the whole
event data. You can view the full details by double clicking an individual event, or
highlighting it and clicking Actions >> Audit Details. Either of these methods will
bring up the following dialog,
Figure 30 - Postbag file audit details
The Details page shows the full details of the event, while the Event Data page
lists the full details of the comms file or the workflow parameters that were used
and the Job Log page is used to display the log file that was created by this
event (if applicable).
If there were errors in a map job then the audit line details for the map job
includes a list of the errors in the information section.
The Previous and Next buttons at the bottom of the dialog allow you to step
through all the Postbag File Events associated with the selected file.

34
Description of Client Applications

## 2.2 Administrator’s Workstation GUI

### 2.2.1 Overview

The Administrator’s Workstation client application is shown below,
Figure 31 - The administrator's workstation
This application is split into two discrete categories. It shows details of files sent
and received via comms together with details of workflow queue items that have
been processed.
The comms views have a single section which lists the details of the files that
have been received, scheduled, sent or forwarded, while the workflow views are
split into two main sections. The top section lists the details of each workflow
queue item, while the lower section shows the full audit trail, detailing the events
that have taken place on that particular queue item.
The audit trail is populated whenever you click on a single entry in the upper
section. The audit contains details of the workflow processing, showing every job
that has been executed such as Analyse, Map, Split and Copy.

### 2.2.2 Available Views

#### 2.2.2.1 Comms File Views

The following views are associated with comms files,
 Received Files – Shows the details of the files that have been received from
an external trading partner.

Description of Client Applications

35
 Scheduled Files – Shows the details of the files that have been scheduled,
but have not yet been sent to their destination.
 Sent Files – Shows the details of the files that have been sent and
transmitted to their destination.
 Forward Files – Shows the details of files that have been received and
forwarded out again to another trading partner. This view is typically used in
a clearing centre environment and is therefore not visible by default.
Regardless of protocol or network, every communications file will appear in one
of these tab pages. There are details against each entry that list specific
attributes of the comms file, including, originator and destination, file analysis,
VFN, dates and times, etc.

#### 2.2.2.2 Workflow Processing Views

The following views are associated with workflow processing,
 Inbound Files – Shows the details of workflow queue items that have been
processed on files that have been imported into the system.
 Outbound Files – Shows the details of workflow queue items that have been
processed on files that are going out of the system.
 Errors – Shows the details of any workflow queue items that have resulted in
an error. This view will show all queue items, regardless of whether they are
inbound or outbound to the system.
The main list view shows a summary of the workflow queue item details,
including, originator and destination, workflow status, files details, dates and
times, etc. There is an audit line associated with each workflow queue item
which can be seen in the lower half of the application when you click on an
individual file. This audit line lists the details of all the jobs that have executed on
a workflow and their outcome.

#### 2.2.2.3 Refreshing

It is possible that these views will need to be refreshed. For example, if a file is
received or some workflow processing takes place while the Administrator’s
Workstation client is open. If this is the case, then “Refresh required” will be
displayed in the bottom left of the status bar. To refresh the view, simply click
View >> Refresh, press F5, or click the refresh icon on the menu bar
.

### 2.2.3 Colour Coding

You can see at a glance certain information about comms files and workflow
queue items, depending on the colour coding that has been applied to each
entry. The same colour scheme is used throughout the Administrator’s
Workstation,

36
Description of Client Applications
All workstation views

Pale blue/white = Normal

Red/pink = Error
Scheduled Files

Red/pink = Has a status of “Send Failed” and will not be sent again

Yellow = Suspended

Light orange = One of the following:

Scheduled with attempts greater than 0

Partly sent with attempts greater than 1 and a last error

Partly sent with attempts greater than 2

### 2.2.4 Using the Administrator's Workstation

The Administrator’s Workstation is designed to be used as an administrative tool
for viewing and manipulating the comms files and workflow queue items in the
system. The communication files will be present in the Received, Scheduled,
Sent or Forwarded tab pages, while the workflow processing details will be
present in the Inbound, Outbound or Error tab pages.
The main lists views show a summary of either the comms files or the workflow
queue items, with details including dates and times, the trading partners
involved, the current status and file details including size and document type.

#### 2.2.4.1 Comms Files

If you receive a file via comms, then an entry will appear in the Received Files
tab page. If you schedule a file to a trading partner, then it will appear in the
Scheduled Files tab page until a call is made and the file it transmitted, at which
point, the entry will subsequently appear in the Sent Files tab page.
It is possible to view the full details of a communications file by selecting a single
entry in the list view and clicking Actions >> Comms File Details, or double
clicking the entry. Both of these methods will display the following dialog,

Description of Client Applications

37
Figure 32 - Comms file details
This dialog is dynamically loaded depending on the type of file being viewed and
the communications protocol in use.
The Overview tab page shows the details of the parties involved, together with a
brief summary of the transmission details including VFN, status and date times.
The File Details and File Analysis tab pages itemise the details of the comms file
itself, showing the file status and protocol specific data together with an analysis
of the physical EDI file.
Session tab pages will also be present on this dialog detailing the communication
sessions that were involved in the transmission of this file.

#### 2.2.4.2 Workflow Queue Items

Any file that goes through a workflow will appear in either the Inbound or
Outbound tab page. Each workflow queue item is shown as a single entry in the
main list view with details relating to the details of the queue item and its current
status.
The list view simply shows a summary of the core details, in order to display the
full details you must select an individual item and select Actions >> Workflow

38
Description of Client Applications
Details, or double click the single entry. Both of these methods will display the
following dialog,
Figure 33 - Workflow queue item details
The Overview section displays the current status of the workflow queue item as it
progresses through the system, together with a brief outline of the file details.
The Document Details tab page is only relevant to EDI files and recognised non-
EDI files (such as IDoc files). It gives the analysis-specific details of the file, such
as the codes of the originator and destination and the format and type of the file.
The Workflow tab page displays information about the jobs that have been
carried out on the file. Current workflow and Current job will only be populated if
the file is still being processed.
The Additional Details page shows a list of properties associated with the file,
and the value of each property. These fields are currently only used for SAP files
and will contain information about the IDoc in the file.

#### 2.2.4.3 Audit Trail

The Audit Trail is only applicable to the workflow tab pages. It lists the details of
all the jobs that have taken place on a workflow queue item. The list view simply

Description of Client Applications

39
shows a summary of the audit details, in order to view the full details you can
either double click a single entry, or select Actions >> Audit Details. Both of
these methods will display the following dialog,
Figure 34 - Audit details
The Details page provides all the known information about the selected audit
line.
The Job parameters page lists all the parameters that were provided for the
action to be performed.
If the Job which generated the audit line produced a job log, this will be
accessible on a further page tab, entitled Job Log.
If there were errors in a map job then the audit line details for the map job
includes a list of the errors in the information section.
The Previous and Next buttons at the bottom of the dialog allow you to step
through all the Audit Lines associated with the selected file. If there is only one
Audit Line associated with the file, then both the Previous and Next buttons will
be disabled.

40
Description of Client Applications

## 2.3 Communications Monitor GUI

### 2.3.1 Overview

The Communications Monitor client application is shown below,
Figure 35 - The communications monitor
The Communications Monitor is a very simple client application that allows you
to view details of your current log and all your current and recent
communications sessions. Details of finished communications sessions are kept
on the screen for 5 minutes, though this value can be configured if you wish,
using the Tools >> Options menu option.
The Communications Monitor allows you to see the current status of the
communications within the system, including:

The current status of each active session

Log details for all sessions in the list

A list of calls in retry mode, or recently failed.
The screen is divided into two sections: at the top section shows the details of
your communications sessions, while the lower section shows the details of your
current system log. Note that the system log may contain log messages that are
not connected with communications.
It is possible to initiate calls to a trading partner network from the
communications monitor application, simply click Actions >> Call Network.

Description of Client Applications

41

### 2.3.2 Colour Coding

Each line of the comms monitor log is colour-coded as follows,

Black = Normal

Blue = Trace/Protocol messages

Orange = Warning messages

Red = Error messages

### 2.3.3 Using the Communications Monitor

There is little that can be done from the communications monitor, this clients’
primary use is as a monitoring tool of the communications between you and your
trading partners.

#### 2.3.3.1 Monitoring a Call

When a transmission is in session with a trading partner, the communications
monitor will display the details in the upper section. This will be populated with a
unique session ID, the call direction, network, status and start time.
Figure 36 - Comms in session
If files are exchanged during a session, a summary will be displayed in this upper
section,
Figure 37 - Comms summary
The lower section of the communications monitor shows the full details of the
session. Depending on the log levels you have setup will determine the level of
detail that is displayed.

42
Description of Client Applications
Figure 38 - Comms details
If a call should fail, the failure reason will be present in this view.

#### 2.3.3.2 Dismissing a Session

Once a session has completed it will remain, by default, in the upper section of
the communications monitor for 5 minutes if successful, or forever if the session
failed.
If you wish to clear failed sessions or completed sessions before this time, you
must select the sessions in the upper list view, then click Action >> Dismiss.
This will remove the session from the communications monitor, but will not
remove any files that may have been transmitted.

Description of Client Applications

43

## 2.4 ENGDAT Workstation GUI

### 2.4.1 Overview

The EPIC ENGDAT Workstation client application is shown below,
Figure 39 - The ENGDAT workstation
The ENGDAT Workstation is a specialised version of the Administrator’s
Workstation, designed for the day-to-day exchange and handling of ENGDAT
folders between trading partners.
ENGDAT is a specification produced by ODETTE describing how CAD and CAM
files can be transferred between two parties.
From the ENGDAT Workstation, you can view received ENGDAT folders, as well
as extracting them or submitting them to the workflow manager. You can also
edit, delete and create new ENGDAT folders and schedule the folders for
transmission.

### 2.4.2 Available Views

The following views are available in the ENGDAT Workstation client,
 Inbound Folder View – Shows ENGDAT folders received from your trading
partners. These may have been partly received, received or acknowledged.
 Outbound Folder View – Shows folders created in EPIC. These may have
been scheduled for transmission, or sent to a trading partner.

44
Description of Client Applications
Both views can be customised with filtering, column ordering and sorting.
Individual files in received or scheduled folders can be viewed within the
Administrator’s Workstation.

### 2.4.3 Using the ENGDAT Workstation

#### 2.4.3.1 Extracting an ENGDAT Folder

Once you have received an ENGDAT folder, you can download all the files
contained within that folder from the EPIC server and copy them to a directory of
choice on your local machine.
There are three different ways that you can extract an ENGDAT folder, each of
which are available from the Actions menu,
 Extract Folder – This allows you to extract the folder and leave the files in the
ENGDAT folder unchanged. Any compressed files will remain compressed
and the files will be given the same filenames as those on the EPIC server.
 Extract Folder with ENGDAT Filenames – This option will extract the folder,
but the extracted files will be named according to the filenames used in the
ENGDAT message. Any compressed files will remain compressed.
 Extract and Decompress Folder – This option will extract the folder and
decompress and compressed ZIP files in the folder at the same time. The
filenames will be set to those used in the ENGDAT message.
Each option displays a standard browser dialogue, which will let you browse for
the directory in which to place the extracted files. Once you have selected a
directory, click ‘OK’ to extract the ENGDAT files to the directory. Alternatively,
you may select ‘Cancel’ to abort the action.

Description of Client Applications

45

## 2.5 EPIC Monitor GUI

### 2.5.1 Overview

The EPIC Monitor client application is shown below,
Figure 40 - EPIC Monitor Client
This monitoring application displays all the connected master and satellite
servers in the EPIC farm, listing the details of each server in the lower half.
The diagram shows how the servers are connected and indicates the server
name together with the IP Address of the machine where it is running.
If there are no satellite servers connected, then only the master will be displayed.

### 2.5.2 Available Views

#### 2.5.2.1 Servers

This section lists the servers that are present in the EPIC farm and provides
details of each, including the IP address, number of allocated tasks, runtime and
memory usage.

46
Description of Client Applications

#### 2.5.2.2 Tasks

The tasks section lists all the available tasks that can be distributed amongst the
EPIC servers. The task name, instance ID and status are all listed, together with
the name of the server that is running the individual task.

#### 2.5.2.3 Clients

The clients section indicates all the client applications that are connected to the
EPIC servers. The machine name, client application and username (if using
security) are all listed.

### 2.5.3 Using the EPIC Monitor

There is an automatic refresh feature within the EPIC Monitor which means that
this application will update itself with new information every given time interval.
The status of all the servers and tasks will be reflected in the GUI.

Frequent Tasks
47
3
Frequent Tasks

## 3.1 Checking your Postbag for Files

To see the files that are in the postbag of the originator, open the Postbag
Workstation and click on the Originators Files view. To see the files that are in
the postbag of the recipient, open the Postbag Workstation and click on the
Recipients Files view.
Figure 41 - Postbag files inbound
For outgoing files, the file originator is the Internal Company and the file’s
ultimate recipient is one of the Trading Partners. For incoming files, the file
originator is one of the Trading Partners and the file’s ultimate recipient is the
Internal Company.
Upon entering the system, postbag files are always given the status of New and
will not be available to users until the status has been changed. There are
various states that the postbag file can take. These are,

New – The file has arrived in the postbag and is currently being processed

Held – The file has been explicitly held and is awaiting manual release

Released – The file has been released and is available for collection or
postage

Taken – The file has been collected or posted
There is a column that indicates which postbag the file is in and you can limit the
views to a single postbag by setting up a filter.

48
Frequent Tasks

## 3.2 Checking for Received Comms Files

Any files that have been received via comms will show up in both the Postbag
Workstation and the Administrator’s Workstation.
To view received comms files from the Postbag Workstation, open the client and
select the Originators Files view. Selecting a single file will show the details of
the file being received via comms in the audit trail. A file that has been
successfully received and acknowledged will show entries including File
Receiving, File Received and File Acknowledged.
To view the received comms files from the Administrator’s Workstation, open the
client and select the Recipients Files view. There is a File Status column which
will show “Received” for files that have been successfully received from a
Trading Partner, and “Acknowledged” for files that have been successfully
received and acknowledged.

## 3.3 Monitoring Workflow Processing

Any file that is processed on a workflow will show up in both the Postbag
Workstation and the Administrator’s Workstation. When a single file is selected in
either client, the full details of the progression through the workflow are listed in
the audit trail. This allows you to see the processing has taken place on each file
and whether there were any errors.
The Postbag Workstation separates files into those in the Originators Postbag
(Originators Files view) from those that are in the Recipients Postbag (Recipients
Files view).
The Administrator’s Workstation separates files that have come into the system
(Inbound Files view) from those that have gone out of the system (Outbound
Files view).
In both cases, it is possible to view the workflow processing that has taken place
on a file by opening the client, selecting the necessary view (Inbound or
Outbound) and selecting the file you wish to see the details of. The audit trail will
show the processing stages that have taken place. There is a separate column
against the files on a workflow to indicate the status. This will typically show
New, Current or Processed depending on the current stage of the workflow
processing.
If processing has taken place on a file, then it is possible the view will become
out of date. If this is the case then “Refresh required” will be displayed in the
bottom left of the status bar. To refresh the view, simply click View >> Refresh,
press F5, or click the refresh icon on the menu bar
.

Frequent Tasks
49

## 3.4 Manually Submitting a File to a Workflow / Postbag

Files can be submitted to a Postbag or Workflow directly from either the
Administrator’s Workstation or the Postbag Workstation. You may wish to do this
if the file has been received by some means other than via comms and you do
not want to setup a monitor directory for importing files.
To submit a new file, click Actions >> Submit New File, or click on the
icon.
The following dialog will be displayed,
Figure 42 - Submit new file
From here, you will need to enter the location of the file to be submitted and then
select the postbag that this file is to be submitted to. If you choose to submit the
file to the Unsorted Postbag, then you will have to specify the Workflow that is to
be used to process this file.
Once you are happy with the details of the file to submit, click the Submit button.
If the submission is successful, you will see the message “File submitted
successfully” appear at the bottom of the dialog.
The dialog will remain open, allowing you to submit more files if required.
Click the Close button when you have finished.
The details of your newly submitted file will appear as entries in both the
Administrator’s Workstation and the Postbag Workstation (refreshing the views
may be required).

## 3.5 Manually Scheduling a File to a Trading Partner

It is possible to schedule a file directly from the Postbag Workstation. This
bypasses all workflows, and simply schedules a given file to a trading partner.

50
Frequent Tasks
To schedule a file, open the Postbag Workstation and click on the Recipient Files
view. From here, click Actions >> Schedule File, or click on the schedule file icon
. This will open the following dialog,
Figure 43 - Schedule file
You can schedule both EDI and Non-EDI files using this dialog. Simply browse
for the location of the file on disk, or enter the full path of the file in the text field.
If the file to schedule is an EDI file, then an implicit analysis will take place upon
scheduling to determine the originator and recipient. However, if the file is Non-
EDI, then you will have to specify the Originator and Recipient mailboxes to be
used for transmission.
After the file has been selected, you can setup additional details such as the file
priority, earliest date/time to send and the virtual filename.
Once you are happy with the file to schedule and the associated details, click the
Schedule button. If the file is scheduled successfully, a message to that effect
will appear at the bottom of the dialog.
If the earliest transmission date and time is in the past when the dialog is closed,
then an automatic call will be made to the Trading Partner and EPIC will attempt
to transmit the file.
After the file has been scheduled, it will appear as a single entry in the Postbag
of the recipient and no workflow processing will take place on the file. If you wish
to submit a file to a specific workflow, please refer to the section entitled
‘Manually Submitting a File to a Workflow / Postbag

Frequent Tasks
51
’.

## 3.6 Checking that an outbound file has been sent

Any file that has been sent to a trading partner will appear in the Sent Files view
of the Administrator’s Workstation. There is a Status field that indicates whether
the file has been transmitted to the trading partner successfully and whether it
has been acknowledged.
It is also possible to view the sent files from the Postbag Workstation. The
transmission details will appear as entries in the audit trail of the file in the
Recipients Files view. A successful transmission will show Comms File
Sending, Comms File Sent and Comms File Acknowledged.

## 3.7 Calling a Trading Partner

There are three ways of manually initiating a call to a trading partner,

From the Administrator

From the Administrator’s Workstation and Postbag Workstation

From the Communications Monitor
When a call is made, all files that have been scheduled for that network will be
sent to the trading partner. Similarly, any files waiting to be received will be
obtained from the trading partner during the communications session.

### 3.7.1 Administrator

To make a call from the Administrator, start the EPIC Administrator application
and open the Comms section. Select the Trading Partner whose connection you
want to test and open the Status page. You will be presented with the following
tab page,

52
Frequent Tasks
Figure 44 - Network status
The Administrator has the advantage over the over methods in so much that test
calls can be made in addition to standard calls.
A test call will initiate a call to the Trading Partner without sending him any data.
However, if the Trading Partner has any data for you, he will send it. A test call
can be initiated by clicking the Test call button.
A standard call will initiate a call to the Trading Partner, where any scheduled
data will be exchanged between both parties. A standard call can be initiated by
clicking the Call button.
Click the Refresh button to see the results of the call. The Files Sent and Files
Received fields will show you if any data was exchanged with the Trading
Partner during the call.

### 3.7.2 Administrator’s Workstation and Postbag Workstation

Both the Administrator’s Workstation and the Postbag Workstation allow you to
initiate calls to a trading partner. Start either application and select Actions >>
Call Network or click the call button on the menu bar
. The following dialog
will be displayed,
Figure 45 - Call network
This dialog shows all the external networks (i.e. for trading partners and clearing
centres) that are defined in the EPIC system, with their associated protocol and
the status of the last attempted call to each network.
Select the network(s) you wish to call and click the Call button. EPIC will attempt
to make a connection to the selected network(s) and transmit any relevant files
for those networks.
Double-clicking on a network on this dialog will also result in a call being made to
that network.

Frequent Tasks
53

### 3.7.3 Communications Monitor

To make a call from the Communications Monitor, start the EPIC
Communications Monitor application and select Actions >> Call Network. You
will be presented with the same network selection dialog as in the Administrator’s
Workstation and Postbag Workstation, where the operation for making calls
remains the same.

## 3.8 Monitoring Calls to a Trading Partner

The Communications Monitor application can be used to see the details of the
communications sessions that take place between you and your trading partners.
Whenever a call is made, entries will appear in the communications monitor
showing details of the session together with a count for the number of files and
acknowledgements that have been transmitted between parties.
The diagram below shows the details of a typical communications session where
files have been exchanged between trading partners,
Figure 46 - Monitoring calls to a trading partner

## 3.9 Starting / Stopping the Server

Depending on how your system is setup determines how your server should be
started and stopped.

### 3.9.1 Starting

If you are running EPIC as an Application then the server is started by clicking
Start >> Programs >> Data Interchange Plc >> EPIC >> Server. A small icon

54
Frequent Tasks
should appear in the system tray (bottom right of the Windows Taskbar, next to
the clock) automatically starting the server.
It is also possible to start the server using the EPIC Console Window. Simply
open the console, type “Start” and press enter.
If running as a System Service, then the server should start when your machine
boots up. If this is not the case, then you can view the Windows Services by
clicking Start >> Control Panel >> Administrative Tools >> Services. From
here, select the EPIC Service and click Action >> Start.
The Windows Services applet is shown below for reference purposes,
Figure 47 - System services

### 3.9.2 Stopping

If you are running EPIC as an Application then the server is stopped by right
clicking on the EPIC system tray icon (bottom right of the Windows Taskbar, next
to the clock) where a context menu will appear. Simply left click on Stop to stop
the server, or Shut Down to exit the application completely.
The EPIC Console Window can also be used to stop the server. Simply open
the console, type “Stop” and press enter.
If running as a System Service, then the server can be stopped by using the
Windows Services applet. Click Start >> Control Panel >> Administrative
Tools >> Services to open the list of services on the local machine. From here,
select the EPIC Service and click Action >> Stop.

Frequent Tasks
55

## 3.10 Viewing the Log Files

Logging is a very useful feature of the EPIC software. Most of the time you will
probably not come into contact with it, but it can be used to help you sort out any
problems, in conjunction with our Support department.
There are various types of log within EPIC: the Server log, the Startup log and
the Client logs. The Server log and the Startup log are always used, but the
Client logs are an optional feature.
Unless you have given a specific directory in which the server log files should be
stored, they will typically be located in one of the following locations,

C:\Program Files\DIP\EPIC\x.x.x.xxx\Log

C:\ProgramData\DIP\EPIC\x.x.x.xxx\Log
All log files are stored in plain text format on your PC and can be opened in most
common text editors such as Notepad or WordPad.

## 3.11 Changing a Filter

Filters are a useful tool and are available in all client applications. They allow you
to restrict what is shown in the view by selecting a given date range, originator /
recipient, file status, etc.
A filter can be applied by pressing Ctrl+F, clicking View >> Filter or by clicking
on the filter icon from the menu bar
,  All of these methods will bring up a
filter dialog similar to the one shown below,

56
Frequent Tasks
Figure 48 - Filter dialog
From here you can specify various options that will be used to restrict the main
list view.
There are different filters depending on the view that is currently active. Details
such as companies and postbags are shown in combo boxes, allowing you to
choose one, whereas checkboxes and radio buttons may also be present to
allow multiple selections of a filterable entity.
The filter will only be applied if you click OK.
The yellow banner just above the list view will show you a summary of the filter
details that have been applied.
Figure 49 - Filter summary banner
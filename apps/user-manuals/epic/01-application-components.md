# Chapter 1: Application Components

Source: https://downloads.datainterchange.com/Support/Manuals/EPIC/VM-0001-05%20Users%20Guide.pdf

---

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

## 1.2.1 What does the Administrator do?

The EPIC Administrator consists of four configuration and management areas –
the System Administrator, the Comms Administrator, the Workflow Administrator
and the Tasks Administrator.

## 1.2.1.1 System Administrator

The System Administrator is responsible for the administrative aspects of the
EPIC system. It covers such areas as the System Log, System Settings,
Retention Periods, Schedules, Event Actions, Users and User Groups.

## 1.2.1.2 Comms Administrator

The Comms Administrator is responsible for all matters relating to the EPIC
communication system. It covers such areas as your own company's internal
networks, your trading partners and their communication details, the
communication details of the clearing centres you have accounts with, and sub-
systems.

## 1.2.1.3 Workflow Administrator

The Workflow Administrator allows you to configure how you want EPIC to
process the files in your system. Its flexibility means that you can process any file
from any trading partner in exactly the way you require. Processing 'channels'
can be defined according to trading partner, data source and data type.

## 1.2.1.4 Tasks Administrator

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

## 1.8.1 Menu bar

Each application has a menu bar at the top showing several menu options.
*Figure 1 - The menu bar*
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

## 1.8.1.1 File option

The File menu item contains options allowing you to Log off, Disconnect and
Exit.
The Log off option is applicable only if User Security is enforced. It allows you to
change the user of the application without closing the application down. For full
details of this option see: ”Connecting to the Server”.
The Disconnect option will disconnect the current client application from the
EPIC server. You can reconnect using the Connect button on the "Lost
connection" dialog that appears.
The Exit option will close the current EPIC client application.

## 1.8.1.2 View option

The View menu item contains a variety of sub-options that differ according to the
application you are looking at. Typical items within the View option include
Refresh and Filter.
The Refresh option will reload the current view, ensuring the most up to date
data is being shown.
The Filter option will bring up a separate dialog, allowing you to apply a filter to
the current view, thereby restricting the data that will be displayed.

## 1.8.1.3 Tools option

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

## 1.8.1.4 Help option

The Help menu item provides access to the page(s) of the EPIC online Help
manual that describe and explain the application, a link to the DIP homepage
and a dialog giving technical details about the application.

## 1.8.2 Status Bar

The status bar tells you about the status of the current application. It is located at
the very bottom each application where there should be 5 different status boxes.
If there are fewer, it means the application is not connected to the server. You
must be connected to the server in order to use the application.
*Figure 2 - The status bar*
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

## 1.8.3 Tab pages

Tabs allow you to see different pages of the screen you are looking at. They are
usually found at the top of the information on the screen, and look like the page
markers of a binder. Each tab displays an icon and a caption, to indicate the
contents of the page it is marking. Simply click on the tab with your mouse to
open that page.
*Figure 3 - Tab pages*

## 1.8.1 Default tab pages

Whenever a tab page is used to separate details within EPIC, a default tab page
option will be available. The default tab page is the one that will be shown to you
first. Typically, the default page will be the first tab that is available.
If you want to change the default page setting for any section, this is how they
work.

At the top of every tab page is a title banner (typically yellow), at the right-hand
side of which is the default page tickbox. If the box is ticked, it indicates that this
is the default page for this section. If you prefer a different page to be the default,
simply select the tickbox from one of the other pages. Next time you open up this
section, the default page will be the one you have chosen.

## 1.8.2 Mandatory fields

Within most of the EPIC applications, there are dialogs which require you to
provide information. Some of this information is optional i.e. you may provide it if
you wish or omit it if you prefer. Other information is mandatory i.e. you must
provide it before EPIC will allow you to close that dialog. All mandatory fields
have been given a bright blue background.

## 1.8.3 Context menus

A context menu is a dynamically loaded list of options and actions that can be
performed depending on the area of the application your mouse cursor is
residing.
Context menus are not visible until you hold your mouse over the data area of a
page and click the right mouse button.  A menu will then appear next to the
cursor, from which you can select an option by highlight it and pressing the left
mouse button.
*Figure 4 - Context menu*
1.8.4
"Hot" keys
For people who prefer to use the keyboard rather than the mouse, a hot key can
be used as a quick way to get at menu options from the menu bar.
To use the menu bar with the keyboard, press the Alt key to make the "hot keys"
visible on the menu bar. Each option on the menu bar will now have a letter
underlined to indicate the hot key. Having pressed the Alt key, press the letter
indicated by the hot key of the option you want e.g. Alt+F for the File options.
This will show you a dropdown menu which you can then navigate in two ways.

One way is by using the up and down arrow keys on your keyboard. When the
option you want is highlighted, hit the Enter key to select it.
The other way is by using the hot key of the dropdown menu item you want (the
hot key will be indicated by being underlined). To use the appropriate hot key,
just press the matching letter on the keyboard. This method is indicated in the
user guide by the convention Alt+F+P for example.
Hot keys are also used on dialog buttons in exactly the same way.

## 1.8.5 Short cuts

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

## 1.8.6 Radio buttons

These are a feature of some dialogs, such as filter dialogs. Radio buttons allow
you to choose between two or more mutually exclusive options. Their
appearance is of a small white circle alongside a description of each option. The
currently chosen option is indicated by a black spot in the radio button.

## 1.9 Common dialogs

There are several dialogs that you may come across in any of the EPIC
applications. These are described below.

## 1.9.1 Connecting to the Server

EPIC runs on a client-server architecture. This means that each client application
must know where the server is in order to connect to it. By default, the client
applications point to the local machine (127.0.0.1).
If a client cannot connect to the server, or the connection is lost for some reason,
you will be presented with the following dialog,

*Figure 5 - Could not connect*
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

*Figure 6 - Server details*
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

## 1.9.2 Logon dialog

The Logon dialog will only be a feature of EPIC if User Security is being
enforced.
If you are using User Security, the Logon dialog will appear whenever you try to
start an EPIC application or whenever you select the File >> Log Off option from
any of the EPIC applications. Logging off enables another user to log on without
having to close the application first.
If logging off, you will first be asked if you are sure you want to log off the current
user, with the message box below (the banner content will depend on which
application you are currently logged on to).

*Figure 7 - Logoff confirmation*
Click Yes to proceed with the logoff, or No to remain logged on.
If you click Yes, or if you are starting an application, you will then see the
following dialog:
*Figure 8 - Logon credentials*
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

## 1.9.3 Change password dialog

The Change password dialog will only be a feature of EPIC if User Security is
being enforced.
The Change password dialog, shown below, will appear if you select the Tools
>> Change password option from any of the EPIC applications.

*Figure 9 - Change password*
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

## 1.9.4 Options dialog

An Options dialog is accessible from each of the EPIC applications. The settings
shown in the Options dialog are only applicable to the application in which you
are viewing them. Likewise, any changes you make will only affect the particular
application in which you make those changes.
The Options dialog in the Communications Monitor has an extra page that is
described in the "Comms Monitor Options dialog" section below.
When you click on the Tools >> Options menu item, you will see the following
dialog.

*Figure 10- The options dialog*
All the Options dialogs share four common tab pages, Language, Logging,
Colours and Server.

## 1.9.4.1 Language page

The Language page dialog is shown below.
*Figure 11 - Language settings*
This page allows you to change the language in which the application is
displayed. Changes made here affect most of the text displayed in the

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

## 1.9.4.2 Logging page

The Logging page dialog is shown below.
*Figure 12 - Logging settings (Disabled)*
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

*Figure 13 - Logging settings (Enabled)*
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

Support department, they may suggest that you select one or more of the
remaining message types too.

## 1.9.4.3 Colours page

The colours page dialog is shown below,
*Figure 14 - Colour settings*
This allows you to specify the colour scheme that is used for the banner text and
backgrounds visible in the EPIC application.

## 1.9.4.4 Server page

The server page dialog is shown below,

*Figure 15 - Server settings*
This section allows you to configure the details that the client application uses to
connect to the EPIC server. There are two main sections, Server details and SSL
details.
The Server details are mandatory as these specify the IP address and port of the
server that the application is connecting to.
The SSL details are only required if you are connecting to the server over a
secure connection. If you wish to use SSL, tick the box named ‘Use SSL’. You
will then have to provide the SSL port of the server you are connecting to and the
certificate that is being used for the SSL connection.

## 1.9.5 Comms Monitor Options dialog

The Comms Monitor options dialog has an extra page, described below. For
details of the other pages, please refer to the section entitled "Options dialog".

*Figure 16 - Communications monitor view options*
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

## 1.9.6 Select Certificate Dialog

The Select Certificate dialog allows you to choose the certificate to encrypt and
or sign data.

*Figure 17 - Select certificate*
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

If you are unable to select or import a certificate, you can create your own
certificate by clicking on the Create button. This will bring up the ‘Create
Certificate Dialog’ dialog.

## 1.9.7 Import Certificate Dialog

The import certificate dialog allows you to import a certificate from a file into your
system. It is possible to import certificates in any of the following formats,

PFX: Personal Information Exchange – PKCS#12

P7B: Cryptographic Message System – PKCS#7

CER/PEM: Encoded X.509 Certificate
The following dialog allows you to perform the certificate import,
*Figure 18 - Import certificate*
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

## 1.9.8 Create Certificate Dialog

This dialog allows you to create a self-signed certificate with a private key and
install it in the root certificate store. Self-signing allows you to create a trusted
certificate without needing to obtain one from a third-party issuer.

*Figure 19 - Create certificate*
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

## 1.9.9 Upgrade settings dialog

The Upgrade EPIC settings dialog is the same for all applications, though each
will refer to the application you are currently using.

*Figure 20 – Upgrade settings*
To upgrade your settings, you need to select a previous version of EPIC to
upgrade from.
Previous versions that have been installed in the default EPIC installation
directory will be listed in the main window of this dialog, so you will normally just
select one of them to upgrade from, by highlighting it.
If you have installed a previous version of EPIC somewhere other than in the
default directory, you can use the Browse button to find it.
If you use the Browse button, you will see the Select settings file dialog, as
shown below.
*Figure 21 - Browse for settings configuration file*
The file type you have to use (i.e. the appropriate configuration file) will be
provided for you in the 'Files of type' field. You need to search for a file with that

name in the directory where you have installed a previous version of EPIC.
When you have found it, double-click on it to return to the Upgrade EPIC settings
dialog, where the directory name will now be displayed in the field alongside the
Browse button.
Having selected the previous version to upgrade from, click the Upgrade button
to proceed with the upgrade. Or click the Cancel button to abandon the upgrade
procedure.
If you proceed with the upgrade, you will then see the following message box,
informing you that the upgrade was successful.
*Figure 22 - Settings upgraded*
Click OK to return to the application you are using.

## 1.9.10 Timeout dialog

The Timeout dialog may appear when you have requested EPIC to do something
that may take a few minutes to complete. It gives you the option to cancel the
request if you wish.
If you want to cancel the request, click the Cancel button. You will be returned to
the previous screen.
If you prefer to wait until the action has been completed, you need take no
action.

## 1.9.11 Waiting for Response dialog

The Waiting for Response dialog may appear when you have requested EPIC to
do something that may take a few minutes to complete.
This dialog does not give you the option to cancel your request. The type of
action you have requested is one that must be completed before control is
returned to you.

## 1.9.12 Help About… dialog

The Help About dialog is accessible from the menu bar of any of the EPIC
applications. Click Help >> About Application, where Application is the name of
the application you are currently looking at. The example below shows the Help
About dialog from the Postbag Workstation application.

*Figure 23 - About dialog*
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

## 1.9.13 Displayed Tab Pages

It is possible to change the tab pages that are displayed within the workstation
applications. For example, you may wish to turn off the Received Files view in
the Administrator’s Workstation if you only use EPIC to send files.
The view manager can be accessed from the main menu, using View >> Views
which will present you with the following dialog,

*Figure 24 - View manager*
This dialog lists all the available views for the current application, together with a
description of what each displays and whether the view is currently Shown or
Hidden.
To Show or Hide any of the views, highlight the appropriate line and click the
Show or Hide button, as appropriate. The value in the Shown column will
indicate the change you have made.
Click OK to save the changes and return to the current files view with the new
tab page selections applied, or Cancel to quit the dialog without saving your
changes.

## 1.9.14 Visible Columns

The columns that are displayed in the workstation clients are fully customisable.
It is possible to switch individual columns on and off, change the order that they
appear and alter the order for sorting the data.
The column editor can be accessed from the main menu, using View >>
Columns which will present you wish the following dialog:

*Figure 25 - Column editor (display order)*

## 1.9.14.1 Display Order

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

## 1.9.14.2 Sort Order

The Sort Order section of the column editor dialog is shown below,

*Figure 26 - Column editor (sort order)*
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

Once you are happy with the column arrangement and sort order, click OK to
save your changes and return to the Current Files page, or click Cancel to leave
this dialog without saving your changes.
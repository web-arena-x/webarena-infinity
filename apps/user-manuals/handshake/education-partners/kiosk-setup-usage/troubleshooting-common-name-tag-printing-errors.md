# Troubleshooting Common Name Tag Printing Errors

Source: https://support.joinhandshake.com/hc/en-us/articles/360000837168-Troubleshooting-Common-Name-Tag-Printing-Errors

---

This article provides different solutions to common Dymo printer errors. If you're unable to resolve your error or you do not see your error listed here, please contact support.

Topics:

- [“No Printer Found” Error](#01GT2VB9E34N6DK8N0G33CBV39)
- [“Couldn’t retrieve name tag information” Error](#01GT2VF22F4HK5J1X19NXAPPJR)
- [Name tag failing to print despite “Your name tag is printing” message](#01GT2VGV84RF32ZVAYRKQRGD32)

**Note**: kiosks are not available for virtual fairs; when students launch a session, Handshake records that as a checkin for reporting purposes.

## "No Printer Found" Error

### Suggestion 1: Make sure you're using correct devices

Make sure you are using the same printer that was initially connected to the laptop on setup.

The error "No Printer Found" can occur if you connect a different printer to the computer than the one that was originally connected when the software was installed. 

If you know a different printer was connected originally, you can either connect that original printer, or skip to the steps for re-installing Dymo software below (to accommodate your current printer).

### Suggestion 2: Test in several browsers

Try printing a name tag in a different browser. We recommend testing in:

- Chrome
- Firefox
- Safari (on Mac) or Edge (on PC)

If the name tag prints in another browser, try clearing your original browser's cache.

### Suggestion 3: Re-install the software

If you've tested in different browsers and are still getting an error, uninstall the Dymo software and reinstall.

First, uninstall Dymo from your computer.

Before reinstalling, **unplug the printe****r** (remove the USB connection from the computer).

After uninstalling the software and unplugging the printer, follow the steps below to re-install.

1. Refer to the [Dymo Compatibility Chart](https://www.dymo.com/compatibility-chart.html) for the correct software download.

2. Scroll down to the All Software Versions table, then select the most recent version of DYMO Label Software or Connect.

**Note**: If using LabelWriter 550, the most recent version of DYMO Connect is required (v1.4.3). LabelWriter 550 isn't compatible with DYMO Label Software.

3. When installing the software, keep the printer unplugged from the computer. The instructions will tell you exactly when to connect it!

Additional considerations:

- If you're currently using DYMO Label Software on a 450 or 450 Turbo, and you'd like to upgrade to DYMO Connect, you'll need to fully uninstall DYMO Label Service and its corresponding web service before reinstalling the software.
- Only one DYMO LabelWriter printer should be added to local printers in the settings. Make sure to remove others that won’t be used.
- When installing 550 on a Mac, a terminal window will pop up and ask for your Password to be input — this is the password for your user login to your computer. This is necessary for the web service to be trusted. You may also need to enable the extension via security settings.
- If DYMO Connect isn't installing on a Mac, confirm that the web service is connected. Click the DYMO.WebApi icon in the top navigation bar, then click Diagnose. The DYMO Connect service will begin running.
  - If you receive an error connecting, click Reset.
  - If you receive a trust certificate error, make sure ‘Always Trust’ is selected for each of the Trust settings. To check, locate your Keychain Access, then double-click **Localhost**.

This should get you up and running smoothly!

### Advanced troubleshooting

If you're still running into issues, you can add the following addresses as trusted sites:

- [app.joinhandshake.com](http://app.joinhandshake.com/)
- [(school domain).joinhandshake.com](http://ucf.joinhandshake.com/)

## 

## "Couldn’t retrieve name tag information" Error

### Suggestion 1: Test in several browsers

Try opening the kiosk in a different browser. We recommend testing in:

- Chrome
- Firefox
- Safari (on Mac) or Edge (on PC)

### Suggestion 2: Change the XML

You can either use the XML we provide at our dedicated article [Name Tag XML Formatting (DYMO 450 or 450 Turbo)](https://support.joinhandshake.com/hc/en-us/articles/360005841133), or you can create your own using Dymo Label Writer.

If you change the XML and your kiosk was still running, close and open the kiosk again so it can process the new XML information.

**Note:** We do not recommend creating the XML from *Dymo Connect*. If you created an XML from Dymo Connect, use one of the XML we provide in the above linked article instead.

## Name tag failing to print despite “Your name tag is printing” message

### Suggestion 1: Check your print queue for any errors

Resolve these errors and attempt to print again.

### Suggestion 2: Set Dymo as the primary printer

If setting Dymo as the primary printer does not resolve the issue, remove other printers connected to your device.

### Suggestion 3: Check that Dymo has successfully installed on your device

If you were installing Dymo, ensure that the installation has completed before attempting to print again.
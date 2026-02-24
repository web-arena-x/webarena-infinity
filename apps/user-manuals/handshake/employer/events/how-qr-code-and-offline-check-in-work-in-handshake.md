# How QR Code and Offline Check-In Work in Handshake

Source: https://support.joinhandshake.com/hc/en-us/articles/34042581374231-How-QR-Code-and-Offline-Check-In-Work-in-Handshake

---

Students can check in to your event either by using a shared kiosk device, such as a tablet or laptop, or by scanning a QR code with the Handshake mobile app.

This article describes how QR code check-ins function, outlines offline mode capabilities, and highlights key limitations, particularly when custom questions are included.

*For instructions on launching the kiosk for your event, refer to* [*Launching a Check-In Kiosk*](https://support.joinhandshake.com/hc/en-us/articles/34040828612887)*.*

### 

### Overview of check-in methods

Handshake supports two primary check-in options for in-person events:

- **Kiosk device**: Students check in using a shared device provided by your team (e.g., a tablet or laptop).
- **QR code**: Students scan a printed QR code using the Handshake mobile app on their personal device.

Both options allow attendees to record their check-in and complete any required fields configured in your kiosk setup.

### 

### QR code check-in requirements

To successfully check in using a QR code:

- The student must have the **Handshake mobile app** installed.
- Their device must be connected to the internet to fully load the check-in interface and display any custom questions.

*Students without the app or internet access may not be able to complete check-in via QR code*.

### Offline mode in kiosks

Handshake kiosks support **offline mode**, allowing check-ins even when internet access is unavailable. The process is as follows:

- The kiosk must be launched online before it can operate offline.
- After launch, check-ins are stored locally on the device.
- When the device reconnects to the internet, the check-in data automatically syncs to Handshake.
- If the device is shut down before syncing, reopen the kiosk on the same device to upload the saved data.

### Limitations with offline QR code check-in

QR code check-in behavior depends on the student’s mobile device, not the kiosk. If a student scans a QR code without an internet connection, the following may occur:

- If the Handshake app is installed, the student’s profile data (e.g., name and email) may still pre-fill.
- **Custom questions** (e.g., competencies, areas of interest, job preferences):

 - Will not appear if the app cannot load the kiosk configuration due to a lack of internet.
 - If the questions are loaded before losing connection, the student can still complete them.
 - Any questions that fail to load will not be displayed or saved.
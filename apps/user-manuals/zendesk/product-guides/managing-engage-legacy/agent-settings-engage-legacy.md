# Agent Settings (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731394142874-Agent-Settings-Engage-Legacy

---

This article provides a step-by-step walkthrough on accessing and configuring various settings, from general preferences like language selection and phone type to specific audio and notification configurations. For agents using Jabra devices, we also delve into detailed setup instructions and troubleshooting advice to ensure optimal integration with Amazon Connect and Engage.

## How to access agent settings

You can access agent settings by clicking on the icon in the bottom left corner of your dashboard.

![](https://support.zendesk.com/hc/article_attachments/9731410513434)

‍

## General Settings

In general settings, you as the agent have the option to choose your language, type of phone you are using and how frequently you want missed contacts to automatically be cleared.

![](https://support.zendesk.com/hc/article_attachments/9731430298906)

Under **Language** click on the dropdown to select your preferred language.

The Language set controls 3 aspects of Engage:

1. The language displayed throughout the Engage UI
2. The date formats displayed throughout the Engage UI
3. The language used by Smart Tools to perform grammar checks, lengthen and shorten messages

![](https://support.zendesk.com/hc/article_attachments/9731430307098)

Under **Phone type** you can select whether you are using a soft phone or a desk phone. If you select Desk phone, desk phone number should be included with the area code.

![](https://support.zendesk.com/hc/article_attachments/9731410551578)

There is an option to automatically close missed conversations after a set amount of time. Select the dropdown under the **Automatically close missed contacts** to see the following:

![](https://support.zendesk.com/hc/article_attachments/9731430330650)

## Audio Settings

In audio settings, you can change audio settings relating to your microphone, speaker and ringtone.

![](https://support.zendesk.com/hc/article_attachments/9731491241498)

Under the **Microphone** and **Speaker** settings you can choose to use the system default microphone and speaker, or any custom microphones / speakers configured on your computer.

![](https://support.zendesk.com/hc/article_attachments/9731491255066)

‍

Looking at the **Ringtone** settings, you can choose a custom ringtone by clicking the dropdown and selecting one of the options. You can click on **Play preview** to hear the selected ringtone.

![](https://support.zendesk.com/hc/article_attachments/9731410614170)

Use the slider to increase or decrease the volume under the **Ring tone volume** setting option.

## Notification Settings

In notifications settings, you can enable or disable the browser notification settings by clicking on the tick box next to **Enable browser notifications**.

You can also enable notifications for when a new message arrives, enable this by ticking the box next to **New message notifications**.

Control the volume for the new message notification by using the slides under **New message notification volume**.

You can also choose to receive notifications on a secondary device by ticking the box next to **Secondary notification**.

![](https://support.zendesk.com/hc/article_attachments/9731394283674)

## Jabra Call Control Settings

If you are using a Jabra device, you can tick the box next to **Enable Jabra Call Controls** under the Jabra Call Control setting option.

If you choose to enable it, this will integrate the call control functionality from your Jabra device into Engage. Please note you will have to follow the Jabra installation instructions in order to set up this correctly.

![](https://support.zendesk.com/hc/article_attachments/9731404200346)

Once you have changed the settings, click on **Save** at the bottom right of the page.

## Jabra Installation

Jabra Call Control for Amazon Connect needs the following software to be installed on Contact Center Agents PCs to enable call control:

·   Jabra Chrome Host (PC/Mac application)

·   Jabra Browser Integration Extension (browser extension).

### How to Install Jabra

Install the native Jabra Chrome Host for your operating system to all Agent PCs.

1. You can find it in the software integration kit that you downloaded, you can also download it from GitHub using this link:

[Jabra Browser Integration.](https://github.com/gnaudio/jabra-browser-integration/tree/master/downloads)

2. Download and deploy the Jabra Browser Integration Extension as a chrome extension. You can find a link to the chrome extension in the software integration kit, you can also download it from GitHub using this link:

[Jabra Browser Integration Extension.](https://chrome.google.com/webstore/detail/jabra-browser-integration/okpeabepajdgiepelmhkfhkjlhhmofma)

Guide to install on mass deploy on PC can be found on GitHub, use this link:

[Deployment](https://github.com/gnaudio/jabra-browser-integration/blob/master/docs/Deployment.md)

Please note: If Jabra Chrome Host or the Jabra Browser Integration extension are not installed, an error message is displayed in the web browser console and a download link is provided.

[.callout-primary]Remember: Jabra Call Control must be enabled in Agent Settings[.callout-primary]

### Troubleshooting

Some things to check before raising a bug:

Jabra software needs to be installed on the agent's PC or Mac. This will normally be done by IT - so please make sure they have this installed before raising a bug ticket that the headset is not working.

**Make sure that the Jabra Call Control settings is switched on and saved.** If it is switched on and saved, please ask the agent to hard refresh the page if they are experiencing issues. This is not required every time this control is changed but is a good troubleshooting step to employ to make sure the setting is working.

Operating systems supported by the integration:

- Windows 64 bit, Windows 8.1, or newer
- Windows 32 bit, Windows 8.1, or newer
- macOS, 10.14, or newer.

Browsers supported by the integrations:

- Google Chrome from version 87
- Jabra says they also support Chromium and Microsoft Edge, but these are NOT supported by Amazon Connect and will not work with Engage.

The headset may not be supported - here you will find a list of supported headsets:<https://www.jabra.com.au/business/for-your-platform/amazonwebservices/amazonconnect>

To access the Jabra installation guide for Amazon Connect from Jabra, click [here](https://developer.jabra.com/site/global/software/amazon-connect/index.gsp?_gl=1*fcbb0k*_ga*NDA1MzQ4NzAuMTY5MDQ2OTcwMA..*_ga_PKCKVQ89WH*MTY5MDQ2OTcwMC4xLjEuMTY5MDQ2OTg2MS4wLjAuMA..*_ga_CJZJ6YKVXE*MTY5MDQ2OTcwMC4xLjEuMTY5MDQ2OTg2MS41My4wLjA.).

‍
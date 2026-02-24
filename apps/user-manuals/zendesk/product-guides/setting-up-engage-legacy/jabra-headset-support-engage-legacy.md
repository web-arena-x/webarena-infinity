# Jabra Headset Support (Engage Legacy)

Source: https://support.zendesk.com/hc/en-us/articles/9731466630298-Jabra-Headset-Support-Engage-Legacy

---

We recommend following the steps in the **Jabra Installation guide.** The information below has been taken from the guide.

### Jabra Software to be Installed

Jabra Call Control for Amazon Connect needs the following software to be installed on Contact Center Agents PCs to enable call control:

- Jabra Chrome Host (PC/Mac application)
- Jabra Browser Integration Extension (browser extension).

#### How to Install

Install the native Jabra Chrome Host for your operating system to all Agent PCs.

1. You can find it in the software integration kit that you downloaded, you can also download it from GitHub using this link: [Jabra Browser Integration.](https://github.com/gnaudio/jabra-browser-integration/tree/master/downloads)
2. Download and deploy the Jabra Browser Integration Extension as a chrome extension. You can find a link to the chrome extension in the software integration kit, you can also download it from GitHub using this link: [Jabra Browser Integration Extension.](https://chrome.google.com/webstore/detail/jabra-browser-integration/okpeabepajdgiepelmhkfhkjlhhmofma)

Guide to install on mass deploy on PC can be found on GitHub, use this link: [Deployment](https://github.com/gnaudio/jabra-browser-integration/blob/master/docs/Deployment.md)

**Please note:** If Jabra Chrome Host or the Jabra Browser Integration extension are not installed, an error message is displayed in the web browser console and a download link is provided.

### Enabling Jabra Headset Support in Local Measure

#### Jabra Call Control must be enabled in Agent Settings

To enable Jabra Headset support in Engage, go to **Agent Settings** and make sure you have **Enable Jabra Call Controls** selected. Click **Save.**

![](https://support.zendesk.com/hc/article_attachments/9731466658074)

## Troubleshooting

Some things to check:

- Jabra software needs to be installed on the agent's PC or Mac.
- Make sure that the **Jabra Call Control** settings is switched on and saved.
- Operating systems supported by the integration:
- Windows 64 bit, Windows 8.1, or newer
- Windows 32 bit, Windows 8.1, or newer
- macOS, 10.14, or newer.
- Browsers supported by the integrations:
- Google Chrome from version 87
- Jabra say they also support Chromium and Microsoft Edge, but these are NOT supported by Amazon Connect and will not work with Engage.
- Check the list of supported headsets: <https://www.jabra.com.au/business/for-your-platform/amazonwebservices/amazonconnect>

‍
# Using Jabra devices with Contact Center

Source: https://support.zendesk.com/hc/en-us/articles/9467119250202-Using-Jabra-devices-with-Contact-Center

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Integrate Jabra devices with Contact Center to enable call control functionality. Ensure Jabra is installed on your computer, typically by IT, using Jabra Chrome Host and Browser Integration Extension. Supported on Windows 8.1+, macOS 10.14+, and Chrome 87+. Activate Jabra call control in agent settings and use a supported headset. Refer to the Jabra installation guide for further details.

Agents using Jabra devices can integrate call control functionality from their Jabra device
into Zendesk for Contact Center. To do, agents must [turn on the device in agent settings](https://support.zendesk.com/hc/en-us/articles/9459094228250), and Jabra must be installed on
the agents computer as described in this article. Typically this is done by your IT
department.

This article contains the following topics:

- [Installing Jabra](#topic_kb1_dmy_xfc)
- [General information for the Jabra
  installation](#topic_g4q_2my_xfc)

## Installing Jabra

Jabra needs to be installed on the agent's computer, typically by your IT department. The
following software must be installed to support Jabra Call Control for Amazon Connect:

- Jabra Chrome Host (PC/Mac application)
- Jabra Browser Integration Extension (browser extension)

**To install Jabra**

1. Install the native Jabra Chrome Host for your operating system.

   You can find it in
   the software integration kit or you can download the Jabra browser integration from
   GitHub.
2. Download and deploy the Jabra Browser Integration Extension as a chrome extension.

   You can find a link to the Chrome extension in the software integration kit or you can
   [download the Jabra browser integration
   extension](https://chrome.google.com/webstore/detail/jabra-browser-integration/okpeabepajdgiepelmhkfhkjlhhmofma).

If Jabra Chrome Host or the Jabra Browser Integration extension are not installed, an
error message appears in the web browser console and a download link is provided.

Admins can mass-deploy Jabra to agents' computers.

## General information for the Jabra installation

To use the integration, agents must [turn on Jabra call control](https://support.zendesk.com/hc/en-us/articles/9459094228250) in agent settings. You might need to
ask the agent to hard refresh the page if they are experiencing issues.

The following operating systems are supported by the integration:

- Windows 64 bit, Windows 8.1, or newer
- Windows 32 bit, Windows 8.1, or newer
- macOS, 10.14, or newer

The following browser is supported by the integration:

- Google Chrome from version 87

  Although Jabra supports Chromium and Microsoft Edge,
  these are not supported by Amazon Connect and will not work with Contact
  Center.

Be sure the agent is using a [supported headset](https://www.jabra.com.au/business/for-your-platform/amazonwebservices/amazonconnect).

Refer to the [Jabra installation guide for Amazon Connect](https://developer.jabra.com/site/global/software/amazon-connect/index.gsp?_gl=1*fcbb0k*_ga*NDA1MzQ4NzAuMTY5MDQ2OTcwMA..*_ga_PKCKVQ89WH*MTY5MDQ2OTcwMC4xLjEuMTY5MDQ2OTg2MS4wLjAuMA..*_ga_CJZJ6YKVXE*MTY5MDQ2OTcwMC4xLjEuMTY5MDQ2OTg2MS41My4wLjA.) if
needed.
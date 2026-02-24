# Configuring Contact Center browser notifications

Source: https://support.zendesk.com/hc/en-us/articles/9459091042970-Configuring-Contact-Center-browser-notifications

---

Contact Center supports desktop notifications to keep agents informed of incoming contacts whether Contact Center is in active use or running in the background. To get desktop notifications from Contact Center you must configure notifications in Contact Center, the browser, and the operating system. Additionally, you need to ensure that the browser doesn't deactivate or put Contact Center to sleep.

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **Add-on** | Zendesk for Contact Center |

Verified AI summary ◀▼

Allow browser notifications so you don’t miss incoming contacts when Contact Center is running in the background. Turn on notifications in your Contact Center agent settings, then allow notifications in your browser and operating system settings. When a notification appears, click it to open Contact Center.

Contact Center supports notifications to keep agents informed of incoming contacts whether Contact Center is in active use or running in the background. To get notifications from Contact Center you must configure notifications in Contact Center, the browser, and the operating system. Additionally, you need to ensure that the browser doesn't deactivate or put Contact Center to sleep.

This article contains the following topics:

- [Turning on notifications in Contact Center](#config_notifs_cc)
- [Configuring your browser for notifications from Contact Center](#config_notifs_browser)
- [Configuring your operating system to allow browser notifications](#config_notifs_os)
- [Viewing Contact Center notifications](#view_notifs)
- [Troubleshooting notifications](#troubleshoot_notifs)

## Turning on notifications in Contact Center

Before you can use notifications, you need to turn them on in Contact Center.

**To activate Contact Center notifications**

1. In [Contact Center](https://support.zendesk.com/hc/en-us/articles/9696121449114), select **Agent Settings** > **Notification settings**.
2. Click **Enable browser notifications**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lm_graphics_rs_5.png)
3. Click **Save**.

The first time you receive a notification, your browser will prompt you to allow notifications. Example for Chrome:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lm_graphics_rs_6.png)

If you don't see a prompt, check the address bar for a Notifications blocked message. Click the message, then click Allow for this site in Chrome or Allow in Firefox.

## Configuring your browser for notifications from Contact Center

To ensure you receive Contact Center notifications even when you're using other applications, you need to allow browser notifications from Contact Center, allow Amazon Connect cookies, and prevent browsers from putting Contact Center to sleep.

**To allow browser notifications**

In your browser settings, allow notifications from these sites:

- `https://support.zendesk.com:443`
- `https://1162894.apps.zdusercontent.com:443`

**To allow Amazon Connect cookies**

In your browser settings, add these domains to allow third-party cookies settings:

- `[*.]`[`amazon.com`](http://amazon.com/)
- `[*.]connect.aws`
- `[*.]my.connect.aws` (or your specific instance URL)

For example, for Chrome add these domains in `chrome://settings/cookies`, for Edge in `edge://settings/content/cookies`, and for Firefox in `about:preferences#privacy` and scroll down to the Cookies and Site Data section.

**To prevent browsers from putting Contact Center to sleep**

In your browser settings, ensure that tab discarding and notification suppression doesn't apply to Zendesk apps.

Chrome: Disable Memory Saver
:   1. Open Settings > Performance or enter `chrome://settings/performance` in the address bar.
    2. Under "Always keep these sites active", then click Add.
    3. Enter `[*.]zendesk.com` and click Add to save.

Edge: Stop Sleeping Tabs
:   1. Enter `edge://settings/system` in the address bar.
    2. Locate the **"Never put these sites to sleep"** section.
    3. Click **Add** and enter `[*.]zendesk.com`.

Firefox: Prevent Tab Discarding
:   1. Type `about:config` in your address bar and press **Enter**.
    2. Click **"Accept the Risk and Continue."**
    3. Search for `browser.tabs.unloadOnLowMemory` and double-click it to set it to **false**.

## Configuring your operating system to allow browser notifications

In addition to configuring browser notifications in Contact Center and your browser, you also need to configure your operating system to allow the browser to show you notificaitions on the desktop.

**To activate notifications on macOS**

- In System Settings > Notifications on your macOS, check that your browser has the Allow notifications option selected.

  Note: If there are 2 entries for your browser, then allow notifications for both.

**To activate notification on Windows**

- In the Notifications & actions section of Windows Settings, check that your browser has the Get notifications from these senders option selected.

## Viewing Contact Center notifications

How you view notifications depends on the browser and operating system you use.

**To view notifications from Contact Center**

Click the notification to open Contact Center. If available, click the **Accept** or **Reject** option.

Examples of call and chat notifications on macOS:

|  |  |
| --- | --- |
|  |  |

Example of a chat notification on Windows 10:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/lm_graphics_rs_2.png)

## Troubleshooting notifications

Use the following troubleshooting tips if you have problems with notifications, make sure you:

- Activated notifications in Contact Center agent settings.
- Allow the site to send notifications.
- Allow the browser to send notifications to the operating system.
- Have an up-to-date operating system and browser version.
- Are using a supported browser: Chrome, Edge, and Firefox only.

If the problem persists, you can reset site settings by clicking the padlock or settings icon next to the web address. You'll then need to [reconfigure browser notifications](#config_notifs_browser).
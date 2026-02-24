# Download Linear

Linear is available on browsers, macOS, Windows, iOS and Android. 

![Image showing Linear icon](https://webassets.linear.app/images/ornj730p/production/02a966c3cd681da332c12dbd92735ff3ad01bb7f-2160x1326.png?q=95&auto=format&dpr=2)

## Overview

Linear is available as a desktop application, from the browser, as native mobile apps or on tablets as a Progressive Web App (PWA).

> [!NOTE]
> We recommend using our desktop clients and mobile apps for the best experience.

## Desktop Clients 

Linear is available for macOS Intel, macOS Apple Silicon, and Windows. Download the desktop app at [linear.app/download](https://linear.app/download).

The benefits of using the desktop app are:

* Notifications are integrated with the native OS. This is especially useful to Safari users since Safari does not support our browser notification system (made with PushAPI).
* Linear is always on and the dock quickly alerts you of unread notifications.
* Keyboard shortcuts have less risk of conflicting with browser-based presets or custom shortcuts.
* Tab support within the app

## Browsers

The Linear web app can be access by logging in to [linear.app](https://linear.app). Linear will launch directly in your browser window.

Nearly all functionality in the desktop app including offline mode is available on the web in most browsers. We support the most recent three versions of Chrome, Firebox and Safari. 
 
**Open in desktop app:** This browser preference opens Linear links in the desktop app if installed. Universal links can be configured from the browser version [Account > Preferences > Behavior > Open in desktop app](https://linear.app/settings/account/preferences).

> [!NOTE]
> **Brave Shields**
> 
>   
> Brave users should disable "Brave Shields" for the linear.app domain to allow the website to connect to and open the desktop app automatically.

## iOS and Android

Linear on mobile lets you unblock work wherever you are and complement use of Linear on other clients. Download these apps from the App Store or Google Play Store, or learn more [here](https://linear.app/mobile).

On both apps, tabs offer entrypoints to common mobile workflows:

### Home

Review your assigned, created or subscribed issues through “My issues”, quickly access your favorites, and explore teams to view their issues, cycles, and triage queues.

### Inbox

Check your Inbox and take action on notifications by sending comments or updating issues directly from the app. Your inbox syncs with Linear on other clients and supports reading, snoozing and deleting your notifications.

### Create issues

Create issues through the center tab. Add more context by attaching media from your camera roll and use rich formatting like codeblocks and quotes.

### Search

Search for issues or projects across your workspace.

### Settings

Switch workspaces, customize your notification schedule, change between light and dark themes or send feedback.



You can also use Linear on your mobile or tablet devices through your browser with our PWA. Go to [linear.app](https://linear.app) to sign in. 

## Having Trouble?

### Real time sync and offline

Linear automatically syncs all changes in realtime as they happen. This is critical to your team's ability to collaborate well and work quickly. If for some reason changes cannot be sent to the backend, the app will store changes locally and re-try whenever connectivity is restored (e.g. internet is back up).

You'll start seeing the words "Syncing" appear next to the workspace name at the top of your sidebar when the app detects that there are a lot of changes waiting to be synced or when sending changes take longer than expected. The number next to it shows how many changes are waiting to be sent. They'll be reloaded and retried even if you restart the application before restoring connectivity.

> [!NOTE]
> **Offline mode is designed as a failsafe and not a full-fledged feature.** 
> We do not check the creation date of each change before updating data. This means that if you make a lot of edits while in offline mode, you could overwrite changes from someone on your team (e.g. if you edited the issue description or they had updated status).

### Network requests to localhost

We periodically check if the Linear desktop app is installed on your computer. We achieve this by sending network requests to your localhost (your computer) on different ports. Each port check helps us determine if our desktop app is running. This then allows us to seamlessly open certain URLs directly in the desktop app, enhancing your user experience and ensuring better integration between our web and desktop applications. 
 
The ports we check are `44450`, `18450`, and `33234`.

### Automatic app updates

For updates, the desktop app downloads and installs updates automatically in the background. To disable automatic updates for MacOS:

#### **Terminal**

`defaults write /Users/$USER/Library/Preferences/com.linear AutoUpdateDisabled -bool YES`

Use the following command to re-enable automatic updates: `defaults write /Users/$USER/Library/Preferences/com.linear AutoUpdateDisabled -bool NO`

#### Plist

Using a `/Users/$USER/Library/Preferences/com.linear.plist` file deployed through MDM, the contents would be:



```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<key>AutoUpdateDisabled</key>
<true/>
</plist>
```

## FAQ

<details>
<summary>Do you support Linux?</summary>
We may in the future but it's not on the roadmap for now. Linux users can use Linear on one of our supported browsers.
</details>

<details>
<summary>My app is stuck in offline mode.</summary>
Being stuck in offline mode may relate to a known Chromium bug. Please toggle your wifi off and on again from your computer's menubar.
</details>

<details>
<summary>Can I open a Linear URL in the desktop app automatically? </summary>
Yes, using a `linear://` protocol followed by the rest of the URL will open that page in the desktop app instead of a browser.
</details>

<details>
<summary>I'm seeing a "Couldn't open in desktop app" error, how do I resolve this?</summary>
If accessing Linear in browser and encountering a _Local Network access was denied_ error unexpectedly when attempting to navigate through links, this can indicate a browser-specific configuration that blocks Local Network Access.   


![Local Network access was denied error, "Couldn't open in desktop app"](https://webassets.linear.app/images/ornj730p/production/af3a2265ff0a5a9e67e93b702a0cea8caf08f785-917x297.png?q=95&auto=format&dpr=2)

To resolve, navigate into your browser settings and search for _Local Network Access_—you should spot the configuration specific to Linear under _Site Settings_: 


![linear.app Allowed local network access](https://webassets.linear.app/images/ornj730p/production/032fbed63738c8603cf6b48b90a26c4d2012be00-1456x218.png?q=95&auto=format&dpr=2)

 
After clicking into this setting, ensure _Local network access_ is set to _Allow_:

![Local network access settings configured to Allow](https://webassets.linear.app/images/ornj730p/production/7ba14535c3e6b31a708c878e3ec7c64d351780e6-1384x210.png?q=95&auto=format&dpr=2)

Note that these screenshots are specific to Chrome, and other affected browsers’ navigation may look slightly different—feel free to reach out to [support@linear.app](mailto:support@linear.app) if you’re having trouble spotting this!
</details>

# Notifications

Receive alerts on important updates in the Linear desktop app, mobile app, Slack, or email.

![Linear app settings page showing notification settings](https://webassets.linear.app/images/ornj730p/production/e96ceb63af7f0d20f769ac8be820e1dcdbe53d41-2396x1634.png?q=95&auto=format&dpr=2)

## Overview

You’ll always see notifications in your Linear inbox. For real-time alerts, you can use the Linear desktop app, mobile app, Slack, or email digests.

## Configure

Go to [Settings > Account > Notifications](https://linear.app/settings/account/notifications) to manage your notifications.

You can customize for the types of updates you'd like to receive from Linear such as changelogs, DPA updates and other communications.

Notification are categorized by channel: Desktop, Mobile, Email, and Slack. A green dot next to a channel will signify this method is enabled and a gray dot means it is disabled.

![Notification methods](https://webassets.linear.app/images/ornj730p/production/e2983e8b986d5d2c15e0c1cc19437482d267706b-1394x692.png?q=95&auto=format&dpr=2)

To enable a notification, click into the method and click the toggle to turn on the notification. Below will be a list of the types of notifications for that method you want to receive.

![Notification methods toggles](https://webassets.linear.app/images/ornj730p/production/49686646084da26890322ca285d164f8c916cf05-1386x908.png?q=95&auto=format&dpr=2)

Notifications are grouped. For example, if you want notifications for status changes on an issue, you will be notified if the status, priority, or blocking relationship of that issue has been changed. You cannot select _only_ status changes.

## Notification timing

Desktop, mobile and Slack notifications are sent in real-time. Email digests send with time delays based on urgency, and are only sent if you haven't already read the Linear inbox notification.

### Email digests

Email digests send a summary of unread notifications. They're configured to send out after a certain amount of time has elapsed depending on properties such as issue status.

You can opt to send a notification email immediately if an issue assigned to you is marked urgent or breaches SLA and/or delay low priority emails outside for work hours until the next day. Work hours are defined as 8 am - 6 pm in your timezone. 

![Email digest delivery preferences](https://webassets.linear.app/images/ornj730p/production/2559f25585b9a4c52184985fb09895c83f4138e7-1416x660.png?q=95&auto=format&dpr=2)

## Subscribing to an issue

Subscribing to an issue will determine whether you will receive a notification for that issue based on your notification preferences. You are automatically subscribed to an issue when you create them, are assigned to them, are @mentioned in an issue comment or description, or if you use the menu in the Activity section to subscribe manually. If you are @mentioned in a comment in an issue thread, you will be automatically subscribed to the thread, but not to the overall issue.

To manage subscriptions, open issues individually and then press `Shift` `S` to subscribe or `Cmd/Ctrl` `Shift` `S` unsubscribe. View all subscribed issues under [My Issues > Subscribed](https://linear.app/my-issues/subscribed).

## FAQ

<details>
<summary>My notifications are enabled. Why am I not receiving them?</summary>
If you have Linear open in multiple tabs or both the Desktop and website app open, it's possible that notifications are sent to one but not the other. The workaround is to only use one version of Linear at a time. If none of those apply, please reach out to our support team.
</details>

<details>
<summary>Do you support browser-based notifications?</summary>
Browser-based desktop notifications are no longer supported in Linear, and cannot be configured unless they were already active in your current browser. To receive notifications, use the Linear desktop app, mobile app, Slack, or email digests instead.
</details>

<details>
<summary>Why isn't the red badge showing up on the Linear icon in my dock?</summary>
Please check that you've enabled notifications for Linear in the macOS settings as well as marked to show the red badge icon. 

![System preferences sho the allow notifications and badge app icon setting](https://webassets.linear.app/images/ornj730p/production/780eb04423b06d23ce195336722b84bb75af702a-1330x1160.png?q=95&auto=format&dpr=2)
</details>

<details>
<summary>What status changes generate notifications?</summary>
When "Status changes" is selected in Notification settings, issue completions and cancelations will notify you if you subscribe to the issue. 

If you wish to configure notifications for issues entering a specific status, consider setting up a [view subscription](https://linear.app/docs/custom-views#view-subscriptions).
</details>

<details>
<summary>Is there a limit to how many notifications you can keep in your inbox?</summary>
We will retain up to 500 notifications in your inbox. If you have more than 500 notifications, we will only keep the most recent 500 and remove any older notifications.
</details>

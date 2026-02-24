# Initiative and Project updates

Keep teams and leaders aligned with structured updates on the health and progress of Initiatives and Projects, available in Linear and Slack.

![Initiative updates view in Linear](https://webassets.linear.app/images/ornj730p/production/f66eac289e2ba135172cf414b51fcc5ba5c2db2f-3312x1732.png?q=95&auto=format&dpr=2)

## Overview

Initiative and Project updates are structured reports that keep teams and leaders informed on progress and alignment. They consist of a health indicator that provides high-level signal of the current state and a rich text description for deeper insights into status, challenges, and next steps.

Initiative updates help leaders and teams stay aligned on high-level goals while still providing visibility into the projects that contribute to them. Project updates focus on individual projects, ensuring teams stay informed on progress at a more granular level. Updates can be viewed in Linear and sent to Slack channels.

![Project update health indicators](https://webassets.linear.app/images/ornj730p/production/3a1609dc34b766530571d44ac4a2da30f825ae4d-3598x2700.png?q=95&auto=format&dpr=2)

## Configure Initiative updates

Initiative updates can be configured by admins in [Workspace Settings](https://linear.app/settings/initiatives). Once Initiatives are turned on, Admins can set up reminders to ensure Initiative owners post updates consistently. These settings allow you to choose how often reminders are sent, such as weekly or biweekly, and specify the day and time when reminders will appear. Reminders are only sent when there is an Initiative owner.

Admins can also configure a default Slack channel where all Initiative updates are sent. Creating a dedicated channel, such as #initiative-updates, helps ensure updates are visible and accessible to the entire team.

## Configure Project updates

Configure project updates for your workspace under [workspace settings](https://linear.app/settings/projects). Select a Slack channel where updates will go (we recommend a dedicated one such as #project-updates) and set optional reminders to remind project leads to post an update at a regular cadence (e.g. post an update weekly on Wednesdays).

Configure notifications for specific projects by clicking the bell icon in the project's header. From there, you can link the project to its own Slack channel (e.g. #p-project-name) to send updates and notifications there. 

> [!NOTE]
> A project must be associated with at least 1 public team for its updates to appear in the channel chosen from the workspace-level project settings. For private-team only projects, you will need to configure separate notifications.

### Keyboard

`G` then `S` to go to _Settings > Updates_ to configure updates

`Shift `+` U` to open project updates panel on a project page

`O` then `P` to go to a project and enable project notifications to Slack channels by clicking on the bell button

`G` then `S` to go to _Settings > Notifications_ to configure personal notifications for projects. You can configure for Desktop, Mobile, Email and Slack.

### Mouse

* Navigate to any project or roadmap view to post an update by clicking _Update_ in the top right corner
* Click on your avatar to go to _Settings > Account > Notifications_ to enable personal notifications for projects
* Navigate to any project and enable project notifications to Slack channels by clicking on the bell icon

### Command menu

`settings` to go to _Settings > Account > Notifications_ to enable personal notifications for projects

`open project` to go to a project and enable project notifications to Slack channels by clicking on the bell button

## Basics

### Create Initiative and Project updates

Updates can be created from the Project Overview or Initiative Overview page. The owner or lead is responsible for posting the first update, after which any workspace member can write subsequent updates.

To draft or edit an update, click the pencil icon in the top-right corner of the latest update in the Initiative or Project overview page. When writing an update, you can highlight text to apply formatting and upload files to provide supporting context.

Select a health indicator—_On track, At risk, or Off track_—to represent the current state of the Initiative or Project. 

![Health status for Initiative and Project Updates in Linear](https://webassets.linear.app/images/ornj730p/production/ed5ece3832c555a0d48ef2a70212008ca49a55de-1774x462.png?q=95&auto=format&dpr=2)

### View Initiative and Project updates

The most recent update is displayed on the Project Overview or Initiative Overview page. To view previous updates, click on the _Updates_ tab.

When viewing a list of Initiatives, you can also click on the health status to see the most recent updates.

Updates appear in chronological order, and anyone can react with emoji to express sentiment. You can also view updates in Slack if they have been configured to post there.

To share an update, you can copy a link or copy it as Markdown using the `⌘/Ctrl` `K` action menu.

> [!NOTE]
> **How we work**: The project lead adds weekly project updates. As well as viewing these in Linear, we have these set up to appear in a specific channel in our Slack workspace. We can then easily discuss each update in a Slack thread originating from the original posted message.   
>   
> During weekly syncs, we'll review project updates directly in Linear. We take a few minutes to silently read them and emoji react depending on how we'd like to discuss them in the meeting. ✋ means you have a question, ▶️ means you want to see a demo, and we usually see a few others like 🚀🙌 🥳.

### Updates tab

Visit the updates tab to see the history of all updates and changes to a project or initiative. 

Updates appear in chronological order along with any changes to properties such as the target date, members, and milestones. On initiatives, you can enable a display option to also see updates from sub-initiatives and projects, so all relevant information appears in one place.

### Progress reports for Initiatives and Projects

Project updates include a concise overview of project progress since the last update. It covers information such as project delays, changes in the target date, assignment of new leads, progress towards milestones, and overall progress. These updates help you track project changes and effectively communicate progress to stakeholders.

If progress appears when drafting a project update, you can choose to exclude it from posting by clicking _Hide details_. Overall project progress must have changed by more than 2% since the last update in order for progress details to appear here.

For Initiative updates, if the Initiative owner has changed since the previous update, or there has been a change in target date or status, this will automatically be included in the update.

### Manage notifications

Updates can be sent to Slack, delivered to your Linear Inbox, or both, depending on your preferences. Notifications can be configured at both the workspace and individual update level to ensure teams stay informed in the way that works best for them.

Admins can configure a default Slack channel for all Initiative and Project updates in Workspace Settings or through the Slack integration settings. We recommend using dedicated channels such as #initiative-updates and #project-updates to keep updates organized.

For individual Initiatives and Projects, you can override the default Slack channel by clicking the bell icon in the respective view. This allows you to select a custom Slack channel for updates (e.g., #p-project-name), ensuring the right audience is kept in the loop.

If Slack notifications are enabled, edits to updates will also be reflected in Slack. Additionally, you can enable Inbox notifications in your account settings to receive updates directly in your Linear Inbox.

### Initiative and project update comments

It’s possible to comment under Initiative and Project updates to discuss them further. The person who wrote the update and anyone who participates in the thread will receive notifications in their Linear Inbox.

If the Slack integration is enabled and updates are posted in a Slack channel, comments will be bi-directionally synced between Linear and Slack. This ensures that all messages in the Slack thread will sync back to the update in Linear, just as Slack comments on issues [sync with Linear](https://linear.app/docs/slack#sync-threads).

### Initiative and Project update reminders

Admins can enable update reminders in Workspace Settings to ensure Initiative and Project updates are posted consistently. Once enabled, you can customize the frequency of reminders, choosing whether they are sent daily or at a set interval (e.g., weekly or biweekly). You can create custom schedules and also specify the day and time for reminders. Leads will receive reminders in the designated time window in their local timezone.

Reminders are sent for _active_ Initiatives and Projects with statuses in the _started_ category, and only to the Initiative owner or project lead. If an update isn’t made after the initial reminder, follow-up nudges will be sent 1 working day later, and 2 working days after this.

When selecting a reminder time, note that reminders may not be sent precisely at the chosen hour but will be delivered within the hour selected or shortly after.

### Project-level update schedule

You can also change the update schedule for an individual project from the bell icon on the project view menu. Toggle between the following options for your project:

* Follow the workspace default notification schedule
* Set a custom schedule for this project
* Never receive update reminders for this project

![custom schedule settings for project updates](https://webassets.linear.app/images/ornj730p/production/b437ead6477d22c77b1def389a22d218274a02ad-1464x921.png?q=95&auto=format&dpr=2)

### Project staleness

When project update reminders are enabled, in-progress projects that are overdue for updates will reflect this for easier monitoring. If an update schedule is configured for a project, its health icon will reflect when an update has been missed. Projects that remain overdue for an extended period will have their icon turn grey to indicate inactivity.

Projects are marked _Update Missing_ when both of the following are true:

* The last project update was _On Track_
* An update is one reminder cycle + 3 days overdue past the expected update frequency

Projects will instead show _No Update expected_ if they completed or their update schedule is set to _Never_.

A dashed outline indicates a update project update is slightly overdue before the health icon turns grey and the status changes

You can filter projects by " Date > latest project update" (e.g. “before 1 week ago”) for more control.

![Date and health filters on Project View](https://webassets.linear.app/images/ornj730p/production/ffbec8348ab58cf0dd16f1e2568af9caa26aa4b6-1260x465.png?q=95&auto=format&dpr=2)

## FAQ

<details>
<summary>Can I edit an existing project update?</summary>
Yes. When viewing project updates, you'll see the edit pencil icon appear when hovering over any project updates you created. If you are not the creator of the update, you will need to ask the creator to make the update.
</details>

<details>
<summary>Can I delete an existing project update?</summary>
Yes. Just click on the `… `icon beside the project update you'd like to delete and select the delete option from the pop-up menu which appears.
</details>

<details>
<summary>Can I emoji react to a project update?</summary>
Yes. When viewing a project update, hover over it to see the emoji reaction icon appear. Click to add an emoji reaction.
</details>

<details>
<summary>Why am I not receiving project update reminders?</summary>
To receive a project update reminder, the following applies:

* You must be the project lead
* The project must have "In Progress" as its status
* You must not have posted an update in the last 24 hours 


If the above conditions are true but you are still not receiving project update reminders, reach out to us for help.
</details>

<details>
<summary>What happens when you send updates to multiple Slack channels?</summary>
Instead of posting project updates to each of the channel separately, we now post one project update post to a main channel and then forward this post to other channels.
</details>

<details>
<summary>My project update comments are not coming through or are not syncing</summary>
In order to benefit from syncing comments between Slack and Linear, you need to make sure that the latest version of the Slack integration is installed in your workspace. An Admin of your Linear workspace can use the "Reconnect" button in the integration settings for Slack.
</details>

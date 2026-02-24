# Slack

Combine Linear with Slack to keep everyone in sync.

![Linear logo and Slack logo](https://webassets.linear.app/images/ornj730p/production/42ec7d05b6dd1e64e3803ac7752b7e2c325058a5-2880x1620.png?q=95&auto=format&dpr=2)

## Overview

Create Linear issues from Slack messages, sync threads between Slack and Linear, set up personal and channel-specific notifications, display rich unfurls in Slack and more.

![Video](https://webassets.linear.app/files/ornj730p/production/8474a8ec745ef700c0bf06890abc2a05352c4443.mp4)

## Configure

### Integration setup

Go to [Settings > Features > Integrations > Slack](https://linear.app/settings/integrations/slack) to connect your Slack account to Linear. You must be a Linear admin to do this. 

Once this has been completed, others in your Linear workspace can:

* Use Linear agent by mentioning @Linear
* Create Linear issues from the _More actions_ menu on Slack messages or by using the `/linear` command on all plans
* Take quick actions from Linear links shared in your Slack workspace
* View rich unfurls in Slack that show key issue, comment, document, initiative or project details
* Enable personal Slack notifications
* Send team and project updates to dedicated Slack channels

### Notifications setup

Slack notifications are available for teams, projects, and individuals. Once the initial integration has been configured, any user can set up these notifications. 

#### Team notifications

Set up **team notifications** from team general settings or from the integration [settings](https://linear.app/settings/integrations/slack) page. Authenticate to Slack and then choose a channel for the notifications to post to.

#### Project notifications

Set up **project notifications** from individual project pages. Click on the bell in the titlebar on the top right of the app, authenticate to Slack, and choose a channel for the notifications to post to.

#### Personal notifications

Set up **personal Slack notifications** from [notification settings](https://linear.app/settings/account/notifications). Authenticate to Slack and then choose which notifications to receive.

#### View Subscriptions

Click the bell icon at the top of a view, then the _Configure_ button next to _Slack notifications_. Turn on the toggle and authorize Linear to post to a particular channel. Choose whether to be notified for when an issue is added to the view, completed/canceled, or both.

Moving forwards, notifications for these selected changes will be sent as messages to the chosen Slack channel.

### Connect multiple Slack workspaces

Linear's Enterprise plan supports connecting multiple Slack workspaces to Linear to use the Slack integration. If you're using Slack's Enterprise Grid plan for example, this would allow you to use the Slack integration across your workspaces. To add a new workspace, go to Linear's Slack integration settings and click the `+` button under connected workspaces. You must hold Admin permissions on an Enterprise Linear plan in order to enable this feature.

## Linear agent for Slack

Mention `@linear` in discussions on Slack, and the Linear agent will create issues informed by your conversation's context. Use natural language to specify issue details or simply let the agent infer what's needed.

For example, try:

* @linear file a bug, assign me
* @linear make feature requests from this thread
* @linear file to the Rideshare Loyalty project

To use this functionality, send `/invite @linear` to the desired Slack channel before sending. This feature is available to users in your Slack workspace with Linear accounts.

In [settings](https://linear.app/settings/integrations/slack), you can choose to allow Slack’s workflow builder to mention @Linear agent to support automating actions.

> [!NOTE]
> To use Linear Agent in group DMs, you have to invite the Linear Agent at the creation of group DM.

### Set Linear agent guidance

Linear agent considers instructions you write in Slack integration [settings](https://linear.app/settings/integrations/slack) on how to create issues. Use this field to refine the agent's behavior and give it more context about how you use Slack. 

You might give it context about your channel naming structure and how it relates to your Linear projects, what statuses you prefer it create in, the team it should use when unsure, and more.

Outside of this field, the agent also uses contextual clues to help infer where to create issues (for example, if you're sending project updates from a project to a channel that sounds related, issues created in that channel will favor creation in that project.)

## Create issues with message actions

You can also create issues using the _More actions_ menu on a Slack message if you prefer to specify all the details of your created issue.

If you select a team in the resulting window that uses default templates, that template's text will appear in the description field. Only Linear users in your Slack workspace can create issues with this integration. 

> [!NOTE]
> If you're interested in allowing non-Linear users in your Slack workspace to create issues, consider using [Asks](https://linear.app/docs/linear-asks) instead.

### Use templates

Your issue templates in Linear can also be used in Slack. Add templates to your Slack integration from [workspace template settings](https://linear.app/settings/templates) or the [Slack](https://linear.app/settings/integrations/slack) settings page. Admins can make up to 10 issue templates available in your Slack integration, which any Linear members in your Slack workspace can view and apply during issue creation. If you have a default template set for your team, it’ll show up as an additional template option after the team has been selected.

Templates in private teams are not available to the Slack integration (nor in other integrations that support templates like Intercom and Zendesk.) If you need to allow users to create issues using templates in private teams, consider using [Asks](https://linear.app/docs/linear-asks) where this use-case is supported.

### Sync threads

![Image showing a synced thread in Linear that also posts to Slack](https://webassets.linear.app/images/ornj730p/production/fa1449871ae3ec87e600bd34708505162578c054-5760x3538.png?q=95&auto=format&dpr=2)

> [!NOTE]
> To use synced threads in private channels, invite the integration using `/invite @Linear`. Synced threads are not available in DMs.

To create a synced thread, create an issue from Slack through the _More actions_ menu on a Slack message. 

When you click _Submit_, you'll also create a synced comment thread in the Linear issue by default. Both threads will update as replies are sent in either location, and we'll also update the synced thread in Slack when the issue is completed or canceled, or reopened after being completed or canceled.

When people in your company report issues in Slack, syncing threads is a great way to keep them in the loop regardless of whether they're in your Linear workspace. Comments made in the synced Linear thread will also appear in Slack, and the Slack thread will be updated when the issue is completed or canceled. 

If an issue synced to a Slack thread is marked as a duplicate of another issue, we'll also update the Slack thread where the duplicate was created once the canonical issue is resolved.

### Add Slack messages to existing issues

There are a few options to link Slack messages to existing Linear issues.

#### Sync existing Slack thread with Linear issue

If there is not already a synced thread on the issue, you can choose to sync with an existing Slack thread. To do so, paste the issue's URL into the thread and send the message. Select the overflow menu from inside the unfurl and choose "Sync thread". 

![syncing a Linear thread manually](https://webassets.linear.app/images/ornj730p/production/cbeb13764b09360f5e94824645ed7bad148ab041-1556x829.png?q=95&auto=format&dpr=2)

#### Attach the Slack message's URL in Linear

To associate a Slack message to a Linear issue without syncing, copy the Slack message's URL through the overflow menu on that message. In the Linear issue, use `Control L` to add that URL as an attachment. No updates or messages will be sent to the Slack message when linking this way.

#### Link to issue from Slack

On an issue in Slack, use the overflow menu to select "Link existing issue". Search for and select the issue to associate the Slack message with the Linear issue. With this type of linking, no terminal updates will be sent to the Slack thread, and no synced thread will be created.

### Notifications functionality

#### Team notifications

Team notifications will post updates to a specific Slack channel when issues in that team are created, receive comments, and/or update status. 

We recommend creating a separate #linear or #linear-team channel in Slack for these updates, especially if you choose the option to post status updates (we post every time an issue status changes).

#### Project notifications

Projects have two types of notifications: Slack channel notifications and personal notifications. 

Project Slack channel notifications will post updates to a specific Slack channel when issues in that team are created, receive comments, and/or update status. 

Personal notifications for projects are not directly tied to Slack. They'll subscribe you to receive a notification whenever an issue is created in a project, which you will get in the Inbox (and personal Slack notifications if you have set those up to receive those in [notification settings](https://linear.app/settings/account/notifications)).

#### Personal notifications

Receive the same notifications in Slack that you normally get in Inbox, email, or desktop push notifications. Once enabled, the notification settings page will let you choose which issue, project, and team updates you want to receive via Slack. A Linear app will appear under Apps in your Slack workspace which is where these notifications will be sent.

### Rich unfurls and issue actions 

Once you've connected the integration for Slack, we'll show expanded links anytime you post issue, project, document, or initiative links from public teams in Slack.

 URLs associated with private Linear teams never unfurl. Unfurling can be disabled in Settings > Integrations > Slack if desired.

#### Issue links

**Issue links** show the issue title, description, status, assignee, and creation date. 



They also give other Linear users in Slack the option to update the assignee, comment on the issue, and subscribe or unsubscribe to the issue directly from Slack. You can also engage Slack sync in an existing thread from this menu.

#### Project links

**Project links** in Slack will show a preview with the project name, description, status and target date.

#### Issue IDs

Whenever you mention an issue ID in Slack , a reply with the issue link is automatically added in thread. To prevent clutter, repeated mentions of the same issue ID in this thread within 60 minutes won't generate additional replies. After 60 minutes, posting the issue ID in this thread will prompt a new link reply. Mentioning this issue ID in additional messages or threads elsewhere during this 60 minutes will generate a reply. You can disable this feature in 'Linear settings > Integrations > Slack' if desired.

## FAQ

<details>
<summary>Is there a slash command for creating issues?</summary>
You can use the `/linear` command in Slack as a lightweight way to create an issue.

This action will be confirmed by an ephemeral message in Slack which is only displayed to you. `/linear` is not supported in Slack threads, for Slack sync or for uploading files to issues.
</details>

<details>
<summary>When creating an issue from Slack, why does the title and description populate with the original message content?</summary>
This is intentional behaviour. There's rarely a scenario where you will create an issue without having to change the title or the description in some way. We choose to populate both the issue title and the issue description with the message text so that there's a higher chance you won't need to change both prior to creating the issue.
</details>

<details>
<summary>Can anyone in my Slack workspace create Linear issues?</summary>
Only users with Linear accounts can create issues in Slack using the Linear integration. Slack Guests cannot install or approve apps in Slack, so they'll be unable to use the Linear integration even if they have a Linear account. 

Everyone in your Slack workspace will be able to see team and project notifications pushed to Slack channels and issues created in channels as long as they are part of the Slack channel.

We do have an integration which enables non-Linear users to create issues for workspaces on on our Business and Enterprise plans: [Linear Asks](https://linear.app/docs/linear-asks).
</details>

<details>
<summary>Can I get in touch with Linear's team on Slack? </summary>
Yes! Separate from the integration, you can also [join our community](https://linear.app/join-slack) on Slack! We have a community of Linear users who share tips, feedback, and discuss how they're using Linear with their team. There's also an #api channel for people building apps on our GraphQL API.
</details>

<details>
<summary>How can I access additional support for this integration?</summary>
Please contact us at support@linear.app for any feedback or issues around using the Linear integration for Slack.
</details>

<details>
<summary>How does the integration collect, manage, and store third-party data?</summary>
Our privacy policy is [here](https://linear.app/privacy) and you can refer to our security FAQs [here](https://linear.app/docs/security) for further information.
</details>

<details>
<summary>Can I link a Slack thread to an Linear issue over API to create a synced thread?</summary>
Yes, you can link an existing Slack thread to a Linear issue over our API. To do so, pass `syncToCommentThread: true` in the input to the `attachmentLinkSlack` mutation (documentation is available [here](https://studio.apollographql.com/public/Linear-API/variant/current/schema/reference/objects/Mutation?query=attachmentLinkSlack#attachmentLinkSlack).)
</details>

<details>
<summary>Slack URLs aren't unfurling in Linear after installing this integration</summary>
If you are not seeing the expected preview of Linear issues in Slack, please check the following: 

#### Slack Preferences

Certain preview types may be blocked by Slack’s Messages and Media settings.   
 
If you are seeing an empty preview block in Slack when a Linear issue is mentioned, please toggle on “Show text previews of linked websites” in your Slack Preferences > Messages & Media > In-line media and links

![Slack Messages and Media Settings toggled on](https://webassets.linear.app/images/ornj730p/production/459fe5bfcd919ab55ead0bd67b6dab71d42e7898-377x153.png?q=95&auto=format&dpr=2)

#### Installation Order

If your org installed Linear Asks first and the Slack integration discussed on this page second, unfurls will not work for the regular Slack integration. To fix this:

1. Disconnect both the Asks and Slack integrations from Linear.
2. Disconnect Asks from the [Slack Marketplace](https://instance.slack.com/marketplace/A04RHP43AKH-linear-asks?next_id=0&tab=settings)

![Disconnect connected workspace](https://webassets.linear.app/images/ornj730p/production/98546c65ca6fb71b615df4631d3cb11d4bd64750-703x406.png?q=95&auto=format&dpr=2)

![Disconnect connected workspace](https://webassets.linear.app/images/ornj730p/production/adec2590b6f0181b3028a9c19534c49625dcdd44-723x539.png?q=95&auto=format&dpr=2)

* On the Slack side, go to Tools & settings -> Manage apps. Linear Asks should not appear in the list of installed apps (Linear may still appear if other users in the workspace have personal Slack integrations installed, but this is fine)

![Manage apps in Slack](https://webassets.linear.app/images/ornj730p/production/d845d745081aed4e5faa33baa0c0bcbf3a808ac9-651x761.png?q=95&auto=format&dpr=2)

* Reconnect the Slack integration in Linear
 * Unfurls for public team issues should now work in Slack
 * Templates available to Slack will need to be reconfigured
* Reconnect the Asks integration in Linear. You will have to manually re-add the Asks bot to any channels you have configured for Asks in Slack.
 * Asks team to Linear channel configuration is retained after reconnecting, but you will need to toggle the available templates on for each team.
</details>

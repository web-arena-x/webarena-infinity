# Discord

Combine Linear with Discord keep everyone in sync.

![Linear logo and Slack logo](https://webassets.linear.app/images/ornj730p/production/3cb5427465846c01e025bfa502231d96530d4682-2880x1620.png?q=95&auto=format&dpr=2)

## Overview

Create issues and search for them from the Discord app. The wrap command will post a summary of your day's work in the channel.

### Discord

`/linear issue` to create an issue in Linear

`/linear search` to search and then post an issue

`/linear wrap` to share a summary of your issue updates in the last 24 hours

## Configure

Connect to your Discord server to create issues from Discord messages, search issues, and use the wrap command.

### Integration setup

A Linear admin must first enable the integration for the workspace. One they have, you can go to [Settings > Features > Integrations > Discord](https://linear.app/settings/integrations/discord) to connect your Discord account to Linear. Every Linear user must individually link their account in order to use the Linear integration in Discord.

Once connected, anyone with a Linear account will be able to do the following:

* Create Linear issues from Discord with the `/linear issue` command. 
* Search and display Linear issues in Discord
* Post a wrap, a summary of your days work, in your Discord channel.

## Basics

### Create issues

Type the `/linear issue` command into any channel to create a Linear issue. You will need to fill in the issue title and team and you will also have the option to add a description, status, assignee and project.

### Search issues

Type the `/linear search` command into any channel to search Linear issues on your workspace. The application uses the same search as the app, so you can search for issues by `issue ID` or words in the title, description, or comments. Once you select the relevant issue and click enter, this will be posted to the channel for all members to see.

### Post your daily wrap

Type the `/linear wrap` command into any channel and click enter to post a summary of any issues you started or completed in the past day.

### Link Discord messages in Linear issues

#### Mouse

* Click on contextual menu icon `…` to the top right of the issue
* Click _Add link_
* Click _Discord message_

#### Command menu

`discord` when in issue view, then select _Link Discord message…_

### Unlink issues

You can remove a Discord link from the Linear issue by right-clicking on the issue attachment.

### Filter for Discord links

From any Linear view, you can filter by issues linked to Discord messages. Click `F` then select `Links` and then select `Discord`.

## FAQ

<details>
<summary>Why does the Discord integration need the "Read Message History" permission?</summary>
We need it in order to fetch individual message data when linking a Discord message to an issue with the "Link Discord message" action.
</details>

<details>
<summary>Will you support project update notifications for Discord?</summary>
It's something we'd like to support in the future, but no timeline on if/when that might be yet. If you'd like to see it, let us know at [support@linear.app](mailto:support@linear.app) as we track demand.
</details>

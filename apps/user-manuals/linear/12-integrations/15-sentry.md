# Sentry

Our integration with Sentry lets you create Linear issues from Sentry and create links between Linear and Sentry issues.

![Linear and Sentry logos](https://webassets.linear.app/images/ornj730p/production/00e683be1ab8349d22269ba76ff9fd667c9b05b5-2880x1620.png?q=95&auto=format&dpr=2)

## Overview

Create new Linear issues from Sentry exceptions and link Sentry exceptions to existing Linear issues. Once enabled, the option will show up in Sentry under _Linked Issues_. When a Linear issue is completed, any linked Sentry issues will be automatically resolved. Re-assigning an issue in Linear will update the assignee on linked Sentry issues, too. Read more about the integration on [Sentry](https://sentry.io/integrations/linear/).

### Keyboard

`G` then `S` to go to _Settings > Workspace > Integrations > Sentry_

Use mouse to interact with Sentry links in Linear

### Mouse

* Click the Avatar to go to to go to _Settings > Workspace > Integrations > Sentry_
* Click on link to go open in Sentry
* Right-click on link to remove it

### Command menu

`settings` to go to _Settings > Workspace > Integrations > Sentry_

## Configure

Enable the integration in Linear from [workspace settings](https://linear.app/settings/integrations/sentry). 

## Basics

### Create issues

When viewing a Sentry issue, go to the right sidebar and select Create Linear issue, then fill out the quick form. We pre-fill the description with the Sentry issue details and you'll add the title, team, assignee and priority. 

### Link issues

When viewing a Sentry issue, go to the right sidebar and select _Link Linear_ _issue,_ then search for it existing issue by ID or title. 

### Automations

We’ll automatically close Sentry issues when the linked Linear issue is resolved. We'll also update the assignee in Sentry if it changes in Linear (this will work if you use the same email for Linear and Sentry). 
 
You can also configure automatic creation of Linear issues based on issue/event alerts and metric alerts in Sentry from Alerts > Create Alert and customize your rules to create a Linear issue.

> [!NOTE]
> **Protip:** Most list or board views let you display a Sentry icon when issues are linked to Sentry issues. If the view supports this option, you'll see it as an optional field under Display properties. Clicking the icon will take you directly to Sentry, saving you a click.

### Remove links

To remove the Sentry link, right-click on the link from the Linear issue and select Remove.

## FAQ

<details>
<summary>Do you support self-hosted installations?</summary>
Unfortunately, the integration is limited to cloud accounts. This is a limitation with their integrations, reach out to Sentry if you'd like them to support this in the future.
</details>

<details>
<summary>Can you connect more than one Sentry Organisation?</summary>
Not at this time.
</details>

<details>
<summary>Why is my Linear team not showing up?</summary>
You can only use this integration for public Linear teams, private teams aren't supported. If you convert a team to private any existing connection will no longer work.
</details>

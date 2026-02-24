# Zendesk

Our Zendesk integration makes it easier for you and your team to keep track of bugs and feature requests and interact with the customers who report them.

![Linear and Zendesk logos](https://webassets.linear.app/images/ornj730p/production/cc44cb21b341c3be70dda6c9a8ef1cf698f7dd8f-2880x1620.png?q=95&auto=format&dpr=2)

## Overview 

Our Zendesk integration lets you create Linear issues from Zendesk or link existing issues to your Zendesk tickets. When linked, Linear issue information is shown inside Zendesk and a link to Zendesk is added to your Linear issue. Automate updating Zendesk tickets when its related Linear issue has been closed (Done or Cancelled). Our integration will also re-open the ticket so that your agents will be able to notify the customers.

## Configure

### Install

There are two steps to installing the Zendesk integration:

1. Install and approve Linear for your Zendesk workspace by [installing it](https://www.zendesk.com/apps/support/linear/) from Zendesk Marketplace. This will add the Linear widget to your Zendesk ticket sidebar.
2. Enable Zendesk automation from Linear's [Zendesk settings page](https://linear.app/settings/integrations/zendesk). This will enable ticket re-opening and updates to your tickets. You must be a Zendesk admin to complete this step.

After you install the Linear add-on, it will show up in the right sidebar when viewing a ticket. Each agent will have to login to their Linear account from the application to create and view issues.

### **Requirements**

Our integration requires that each Zendesk agent who installs Linear also has a Linear account, since the linked issues will be created in their name. This also allows agents to open the Linear issue to update it or add more information. This integration is available on our Business and Enterprise plans.

## Basics

### Create new issues

Create a new issue from the Zendesk widget. It will bring up a form which requires a title and that you assign the issue to a team. Optionally add priority, assignee, or labels from within Zendesk.

When linked, Linear issue information is shown inside Zendesk while viewing the related ticket. This also adds a link to the Zendesk ticket from the Linear issue.

Optionally, toggle "include message" in the widget to add message content from the customer ticket to the Linear issue description, including images if applicable.

> [!NOTE]
> Get more out of the Zendesk integration by enabling the [Triage](https://linear.app/docs/triage) feature for your teams. Any issues created from Zendesk will go to Triage when enabled (otherwise, the issues will be added to the first backlog status in your team).

### Create with Linear Agent

In addition to creating issues manually from a Zendesk ticket, you can use the _Create with Linear Agent_ option to automatically create Linear issues using AI.

When selected, Linear analyzes the entire conversation, including customer messages, support replies, metadata, and any attachments, and identifies the underlying product request or bug. The Linear Agent generates an informed title and description while pulling in the relevant context from your conversation with the customer. 

![Create a new Linear issue automatically with the Linear Agent](https://webassets.linear.app/images/ornj730p/production/06255674e4a80db8c543e292bbfae51d52af9b1b-865x610.png?q=95&auto=format&dpr=2)

A customer request is created when applicable, and the issue is routed to the desired team for review and prioritization.

To use the Linear Agent in Zendesk, enable the integration in _Settings_ > _Integrations_ > _Zendesk_ and turn on the option to allow AI-generated issues. 

![Zendesk integration settings to enable the Linear Agent for automatic issue creation](https://webassets.linear.app/images/ornj730p/production/00ef4032be96abf042dac6f746985985b98c4d23-1470x430.png?q=95&auto=format&dpr=2)

Optionally, you can also provide additional guidance to help route issues to the correct teams or templates. This guidance can include examples, team mentions, or internal rules the Linear Agent should follow when interpreting feedback.

### Use templates

Linear admins can designate up to 5 templates to be available for quick use from within the Linear integration in Zendesk. Selecting any of these templates will pre-fill issue property fields appropriately, helping to speed up issue creation and maintain a high level of data hygiene in your issues.

### **Link existing issues**

Search for issues by their issue ID or words in the title to link them. This will add a Zendesk link to the Linear issue. Zendesk's issue search works the same way as our in-app Search.

### Re-open conversations

In the integration settings page, you can automate the reopening of the linked issue when it's completed, cancelled or a comment is made. The integration will post an internal note and re-open the conversation in Zendesk so it's easy to follow up with customers.

### Link multiple issues

Sometimes customers will write in with multiple requests at one time. You can link as many Zendesk tickets to a Linear issue as you like.

### , 
,Link Zendesk tickets in Linear issues

#### Mouse

* Click on contextual menu icon `…` to the top right of the issue
* Click _Add link_
* Click _Zendesk ticket_

#### Command menu

`Front` when in issue view, then select _Link Zendesk ticket to issue…_

### Unlink issues

Click _Unlink_ from the Linear widget to remove the link between the ticket and a Linear issue. You can also remove this from the Linear issue by right-clicking on the issue link.

### **Merge duplicate reports**

It's common for support requests to relate to bugs or issues already filed in Linear. When you merge duplicate issues that have Zendesk links, we'll move any Zendesk links and comments over to the canonical issue and update the linked Zendesk ticket so that it's connected to the canonical issue and automations work.

Click _Unlink_ from the Linear widget to remove the link between the ticket and a Linear issue. You can also remove this from the Linear issue by right-clicking on the issue link.

### Filter for Zendesk links

From any Linear view, you can filter by issues linked to Zendesk tickets. Click `F` then select `Links` and then select `Zendesk`.

## FAQ

<details>
<summary>Why aren't my Zendesk tickets re-opening after Linear closes an issue?</summary>
Check to make sure that you've enabled the Zendesk integration in your Linear workspace [settings](https://linear.app/settings/integrations/zendesk) as well as in Zendesk's settings. The most common reason for this issue is that both steps of the [installation process](https://linear.app/docs/zendesk#install) have not been followed.
</details>

<details>
<summary>Will Linear comments post to Zendesk?</summary>
Yes, you can choose to add internal notes to your Zendesk ticket when comments or status changes are made in the original issue.
</details>

<details>
<summary>Can I update my Zendesk domain? </summary>
Our Zendesk integration is not designed to accommodate updating the associated Zendesk domain. If you update your Zendesk URL, here's what you can expect:

* For tickets linked to Linear issues prior to the Zendesk domain change: the linked tickets will not show up in the Linear app in Zendesk.
* Some of the automations to post internal notes _may_ still work.

If you'd like Linear to support updating your Zendesk domain, please let us know more about your use-case at support@linear.app.
</details>

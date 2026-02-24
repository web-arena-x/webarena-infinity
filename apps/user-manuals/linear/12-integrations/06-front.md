# Front

Our Front integration makes it easier for you and your team to keep track of bugs and feature requests and interact with the customers who report them.

![Linear and Front logos](https://webassets.linear.app/images/ornj730p/production/25379055474c939cc9ab698c30c0e748ad4d4264-2880x1620.png?q=95&auto=format&dpr=2)

## Overview

The Front integration lets you create and link Linear issues from Front conversations. Linked issues, their status, and assignee show up in the sidebar in Front. Linked conversations will show up in Linear issues as link attachments. When issues close, we'll automatically re-open the Front conversation so you can get back to users with an update.



This integration is available on Linear's Business and Enterprise plans.

### Keyboard

`G` then `S` to go to _Settings > Workspace > Integrations > Front_

`Ctrl` `L` (Mac) or `Alt` `Ctrl` `L` (Windows) to link from Linear issue

### Mouse

* Click the Avatar to go to to go to _Settings > Workspace > Integrations > Front_
* Select the more menu (three dots) after saving the Linear issue to link conversations from Linear

### Command menu

`settings` to go to _Settings > Workspace > Integrations > Intercom_

`link` to link Front conversations from Linear

## Configure

There are three steps to installing the Front integration (you must do them in order):

1. Install and approve Linear for your Front workspace by installing it from the [Front integrations page](https://app.frontapp.com/settings/integrations/native/edit/linear). This will add the Linear widget to your Front application sidebar.
2. Then go into Linear's settings and enable Front automation from the [Front settings page](https://linear.app/settings/integrations/front).
3. From the Front sidebar, click on the Linear widget. Sign into the account and select the workspace. 

Front users are required to have a Linear account to use the integration and create and view issues in Front. We also recommend using the Front desktop application for a better experience.

## Basics

### **Create new issues**

You can create new Linear issues from Front conversations. When linked, Linear issue information is shown inside Front while viewing the related message. A link attachment for the Front message is also shown in the Linear issue.

When creating a new linear issue, you can choose a team in which to create the issue, provide a title, and then optionally provide a description, set issue priority, assignee, and labels.

> [!NOTE]
> Get more out of the Front integration by enabling the [Triage](https://linear.app/docs/triage) feature for your teams. Any issues created from Front will go to Triage when enabled (otherwise, the issues will be added to the first backlog status in your team).

### **Link existing issues**

Search for a specific issue ID or words in the related title to link a relevant Linear issue to a Front conversation. This will add a Front link attachment to the Linear issue and gives you the option to add any image content as a comment on the issue. Front's issue search works the same way as our in-app Search.

### ,  
,Link Front conversations in Linear issues

#### Mouse

* Click on contextual menu icon `…` to the top right of the issue
* Click _Add link_
* Click _Front conversation_

#### Command menu

`Front` when in issue view, then select _Link Front conversation to issue…_

### 

### Re-open conversations

In the [Front settings page](https://linear.app/settings/integrations/front) in Linear, you can automate the reopening of the linked issue when it's completed, cancelled or a comment is made. The integration will post an internal note and re-open the conversation in Front so it's easy to follow up with customers.

### Link multiple issues

Sometimes customers will write in with multiple requests at one time. You can link as many Front messages to a Linear issue as you like.

### Unlink issues

Click _Unlink_ from the Linear sidebar in Front to remove the link between the message and a Linear issue. You can also remove this from the Linear issue by right-clicking on the issue attachment.

### **Merge duplicate reports**

It's common for support requests to relate to bugs or issues already filed in Linear. When you merge duplicate issues that have Front attachments, we'll move any Front attachments and comments over to the canonical issue and update the linked Front message so that it's connected to the canonical issue and automations work.

Click `Unlink` from the Linear sidebar in Front to remove the link between the conversation and the associated Linear issue. You can also remove this link from the Linear issue by right-clicking on the Front link attachment.

### Filter for Front links

From any Linear view, you can filter by issues linked to Front conversations. Click `F` then select `Links` and then select `Front`.



## FAQ

<details>
<summary>Do internal notes from Front get added to Linear?</summary>
No, the only option is to send comments from Linear back as internal notes in Front when a comment is made, or an issue changes status. This is configurable in Linear settings > Integrations > Front
</details>

<details>
<summary>Are templates supported?</summary>
Templates are not supported at this time in the Front integration.
</details>

<details>
<summary>Why isn't my conversation on Front reopening?</summary>
Conversations in private inboxes do not support automated comments or reopening.
</details>

# Create issues

Creating issues is the most common action taken in Linear.

![issue creation dialogue box](https://webassets.linear.app/images/ornj730p/production/25ae979891503f4780b6e837aaa71b5027c67281-1224x534.png?q=95&auto=format&dpr=2)

## Overview

Issues are always linked to a single team. They have an issue ID (team's issue identifier and unique number) and are required to have a title and a status—all other properties and relations are optional.

## Create an issue

* Use the keyboard shortcut `C` to open up an issue creation modal
* Use `V` to create an issue in full screen mode.
* Click the **Create new issue** icon in the upper left of the app.
* To create an issue from a template use `Option/Alt C`, or hold `Option/Alt `and click the **Create new issue** icon.
* Enter [https://linear.new](https://linear.new) into your browser URL bar to create new a issue. It will redirect you to the new issue creation page as long as you are logged into your Linear account.
* Issues can be created using our [GraphQL API](https://developers.linear.app/docs/graphql/working-with-the-graphql-api). Many integrations in our [directory](https://linear.app/integrations) allow creating issues from other services using this functionality.
* If you have text highlighted when you go to create an issue, this will pre-fill in the issue title.

> [!NOTE]
> Changes made to an issue's properties in the first 3 minutes are considered part of the issue creation process, and won't be added to the activity log as changes to the issue.

## Create an issue via email

Issues can be created by sending an email to a unique intake email address that routes to a team. You can also create an issue via email based off a template.

A link to the original email will be included as an attachment on the Linear issue. Attachments will be synced over, though email attachments are limited to 25 MB.

The sender of the email will not be notified when the issue is updated or resolved.

> [!NOTE]
> Refer to the [Linear Asks](https://linear.app/docs/linear-asks) feature for the ability to:
> 
> * Customize the email address you want requesters to send to
> * Reply to customer emails from Linear
> * Customize response emails

#### Create an email address

To create a email address for a Linear team, navigate to **Settings > Teams > General > Create by email** and enable the toggle.

#### Create an email address for a template

To create an email addresses for a team template:

1. Navigate to **Settings > Teams > Select Team > Templates**
2. Click the three dots on the right of the template.
3. Select **Configure email address**.
4. Enable the toggle in the pop-up.
5. Click **Continue**.

When a team template is used, the issue's title and description will be overwritten by the email contents, but the properties of the template will be applied to the new issue. Replies sent on the original email to the forwarding address will not create additional issues. 

## Create recurring issues

You can create recurring issues to automate your repeated tasks on a cadence of your choosing.

### Create a recurring issue

When creating a new issue, you can choose to make it into recurring in the issue composer using the `…`  menu and choosing _"Make recurring…"_

<details>
<summary>Creating a recurring issue from the issue composer</summary>
![Creating a recurring issue from the issue composer](https://webassets.linear.app/images/ornj730p/production/7d4cb7c61fa50aad11ca1bca4e9844ec6bd98489-1091x944.png?q=95&auto=format&dpr=2)
</details>

### Convert an existing issue into a recurring issue

To convert any issue into a recurring issue, open the issue and in the `…`  menu choose` Convert into > Recurring issue…,  
,`You can also use the `Cmd/Ctrl` + `K `menu by typing _"Convert into recurring issue"_.  
You can then choose your first due date, and the cadence at which it repeats.

### Create recurring issues in team settings

Navigate to **Team settings > Recurring issues.**  
To create a new recurring issue, click the `+` icon and set your chosen schedule of recurrence.

### Create recurring issues from templates

If you have an existing issue template you want to turn into a recurring issue you can do so. 

First create your issue and apply your chosen template.   
Once created, choose the options to convert to a recurring issue from the `…` menu or command menu. This issue will now turn into a recurring issue, and include any properties that were in the template, including sub-issues.

Recurring issues can easily be found from your **Team settings > Recurring issues**, or filtering your views using the **Recurring issues** filter.

### Cadence of recurring issues

Once you create a recurring issue, future issues in the cadence are expected to be created once the due date passes (00:01 the following day in your team’s timezone.)

> [!NOTE]
> Changes to a template in future will not affect recurring issues that were created from this template. You will need to edit the recurring issue directly or recreate it from your updated template.

## Create a new issue URL

The following links trigger the creation of a new Linear issue in any browser and you can add query parameters after any of them to pre-fill issue fields.

* [http://linear.app/team/<team ID>/new](https://linear.app/team/%3Cteam%20ID%3E/new)
* [http://linear.app/new](https://linear.app/new)
* [http://linear.new](https://linear.new/)

To pre-fill issue fields and/or properties:

1. Add a `?` at the end of the link.
2. Include the field or issue property you want to pre-set.
3. Add `=`.
4. Add the parameter you are setting.
5. Use `&` between each field or issue property when creating a string of pre-settings.

### Apply pre-set properties

We support the following query parameters:

`title` and `description`: 

* Use `+` to indicate empty space in the keyword, or fully url encode content if more complex as description can be a markdown document.
* For example, `https://linear.new?title=My+issue+title&description=This+is+my+issue+description`

`status`

* Can be set by `UUID` or name of the workflow status
* For example, `https://linear.new?status=Todo`

`priority`

* Can be set by Urgent, High, Medium or Low
* For example: `https://linear.new?priority=Urgent`

`assignee`

* Can be set by `UUID`, display name/name of the user, or `assignee=me` to assign the creator
* For example, `https://linear.new?assignee=john` or `https://linear.new?assignee=Erin+Baker` or `https://linear.new?assignee=me`.

`estimate`

* Can be set by their point number e.g. `estimate=4`
* T-shirt sizes have the following point values: No priority (0), XS (1), S(2), M (3), L (5), XL (8), XXL (13), XXXL (21)
* For example, `https://linear.app/team/LIN/new?estimate=2`

`cycle`

* Can be set by `UUID`, cycle number of a name of a cycle
* For example, `https://linear.app/team/MOB?cycle=36` or `https://linear.new/team/EU/new?cycle=focus+on+bugs`

`label`

* Use a comma between each label you want to apply
* For example, `https://linear.new/team/LIN/new?label=bug` or `https://linear.new?labels=bug,android,comments`

`project`

* Can be set by `UUID` or the name of the project
* For example, `https://linear.new/team/LIN/new?project=Project+page+improvements`

`milestone` (a `project` must be defined)

* Can be set by `UUID` or the name of the project milestone
* Project milestone can be read only if `project` is also passed in the URL
* For example, `https://linear.app/team/LIN/new?project=Project+page+improvements&projectMilestone=Beta`

`links`

* URL encoded comma delimited urls with optional title, in format `url|title` . These will be attached to the issue as link attachments. 
* For example: `https://linear.new/team/LIN/new?links=https%3A%2F%2Flinear.app%2Chttp%3A%2F%2Fgoogle.com%7CGoogle`

`Template` 

* Can be set by `UUID` 
* For example, `https://linear.app/team/LIN/new?template=30cd8534-6b24-40bb-8ee7-bb0d83df7d4f`

### Create a URL from a template

1. Go to **Settings > Team > Templates**.
2. Click the three dots to the right of the template.
3. Select **Copy URL to create issue from template**.

### Copy a URL from an issue

While on an issue's view, or an issue is highlighted or selected, open command bar by typing `Cmd/Ctrl` + `K `and select **Copy pre-filled create issue URL to clipboard**.

## Drafts

When writing an issue and navigating away to another part of the app, Linear will hide the issue modal and keep a temporary draft. The next time you go to create an issue, the editor will re-open with the previous content draft. This type of draft is saved locally and only available on the client used to create it. Logging out, restarting, or resetting Linear will clear this type of draft. 

If you use `Esc` or click on the close button, a pop-up modal will appear giving you the option to save the issue as a draft. This draft type persists across clients and will not clear on logout or reset. To access your saved drafts, open the Drafts page in your sidebar.

> [!NOTE]
> Drafts are stored for 6 months before being deleted automatically

## FAQ

<details>
<summary>Can you create issues and use keyboard shortcuts in Safari?</summary>
If Safari is stealing your focus when hitting tab during issue creation, enable this Safari advanced preference:   
  
Safari > Preferences > Advanced > Enable "Press tab to highlight each item on a webpage".

![Safari accessibility preferences modal showing press tab](https://webassets.linear.app/images/ornj730p/production/d1b238d1514c7004f9e3b3d9f4431d4bb27a8a38-992x622.png?q=95&auto=format&dpr=2)
*Safari Accessibility Preferences*
</details>

<details>
<summary>Is there an attachment file size limit when creating issues through email?</summary>
Email routing does not support sending messages with file sizes greater than 25MB. If you have attachments exceeding that, it will fail to deliver. Message body must also be less than 250,000 characters.
</details>

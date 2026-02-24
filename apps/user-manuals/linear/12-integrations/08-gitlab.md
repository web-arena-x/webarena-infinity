# GitLab

Linear supports linking your Linear issues to GitLab and automates your merge request workflows.

![Linear and GitLab logos](https://webassets.linear.app/images/ornj730p/production/d025b73f1b272515da65e8823306b88dff8aa699-2880x1620.png?q=95&auto=format&dpr=2)

## Overview

Link Linear issues to GitLab merge requests. Automate your MR workflow so that issues update when MRs are drafted, opened, merged and when reviews are requested. You can link single or multiple issues to a specific MR.

## Configure the GitLab integration

We support linking GitLab merge requests for both hosted and self-hosted installations, as long as your installation is _publicly available_. 

1. Navigate to [**Linear Settings > Features > Integrations > GitLab**](https://linear.app/settings/integrations/gitlab)
2. Click **Enable** to launch the set-up pop-up.

![Pop-up for setting up the GitLab integration](https://webassets.linear.app/images/ornj730p/production/535b00faf5fdbfad01399eb8bdaffb7ca1efa780-1002x948.png?q=95&auto=format&dpr=2)

1. Navigate to [**GitLab > User Settings > Personal Access Token**](https://gitlab.com/-/profile/personal_access_tokens) or **GitLab > Project Settings > Access Token** to create an API access token. 
 
An access token is used to query the GitLab API for further information and also used to post issue linkbacks. Because GitLab doesn't support bot accounts, linkbacks are created under the name of the token owner. It's recommended that you create a new user for Linear to act as the bot account.
2. When creating the token, set the `api` _or_ `read_api` scope. 
 
If the `read_api` scope is selected, Linear will not post linkbacks to the issue on GitLab merge requests. If using a project access token, the token needs `Reporter` role or higher.
3. **(Optional)** Enable and set a custom URL for your self-hosted GitLab installation without any path (e.g. `https://gitlab.yourcompany.com`). This URL needs to be accessible to public Internet and is only required for self-hosted installations. The earliest supported version of GitLab is 15.6. 
 
If you need to grant access to Linear's IPs, they are 35.231.147.226, 35.243.134.228, 34.140.253.14, 34.38.87.206, 34.134.222.122, and 35.222.25.142.
4. Click **Connect**.
5. Linear will generate the Webhook URL after it validates the access token. Copy and paste this URL to GitLab in either:
 1. A Group's Webhook Settings (For a company on GitLab's Premium or Ultimate tiers) to integrate all projects under it.
 2. A Project's Webhook Settings, to individually connect a specific project.
6. Enable the following Triggers:
 1. `Push events`
 2. `Comments`
 3. `Merge request events`
 4. `Pipeline events`
7. Under SSL verification, ensure **Enable SSL verification** is checked
8. Click **Save changes**.

## Link Merge Requests

### Create a new branch

Set the branch format in Linear **Settings > Workspace > Integrations GitLab > Branch format**. When viewing or selecting a Linear issue, use the _Copy git branch name_ action or shortcut `Cmd/Ctrl` + `Shift + .` It will give you a branch name with the issue ID which you can use to create a new branch in GitLab.

> [!NOTE]
> We recommend using common branch naming patterns throughout all of your teams.

### Add the issue ID in the MR title

Include the Linear issue ID (e.g. ID-123) in the MR title when creating merge requests.

### Use a magic word

Add a magic word + `issue ID` in the MR description (e.g. `Fixes ENG-123`). The integration cannot link MRs via comments or commit messages. The available magic words to link issues are: `close, closes, closed, closing fix, fixes, fixed, fixing resolve, resolves, resolved, resolving complete, completes, completed, completing.`

To link MRs to issues **without** them automating your issue status on MR merge, use the one of the contributing magic words: `_ref_, _references_, _part of_, _related to_, _contributes to_, _towards_`. When using a non-closing magic word like this, the linked MR or commit will still move the issue through other statuses per Workflow settings, but will not automate the issue's status when the MR or commit merges. Instead, it will only transition the issue through to what’s configured prior to the _On MR or commit merge_ event.

#### Link multiple Linear issues to an MR

To link multiple Linear issues to a single Merge Request, or to link a Merge Request after creating it, use the magic word linking method by including multiple closing statements in the MR description (e.g. `Fixes ENG-123, DES-5 and ENG-256`). Linking will happen after you save your changes. The Linear issue will not close until all Merge Requests have been closed/merged.

## Merge Request automation

The merge request automation allows you to select specific statuses for your Linear issues based on MR changes—saving you the hassle of updating Linear issues manually. 

Customize the MR automation in **Settings > Team > Workflow**. Since this is a team setting, it must be configured for each team in your workspace. 


![MR status automation set for the following categories: on draft mr open, on mr open, on mr review request, on mr ready for merge, on mr merge](https://webassets.linear.app/images/ornj730p/production/b26feeac53ba12d391fef53daa87a38366e4a6f2-1346x676.png?q=95&auto=format&dpr=2)

### Ready for merge automation

If you'd like to use the Merge Request automation to capture passing CI checks, please verify in GitLab that:

1. You have enabled Pipeline events under the Webhook settings for any repo part of the GitLab integration.
2. All pipelines that Linear should consider when determining if an MR is mergeable need to be merge request pipelines. GitLab documentation is available [here](https://docs.gitlab.com/ee/ci/pipelines/merge_request_pipelines.html).
3. Under ‘Merge requests’ in project settings, ‘Pipelines must succeed’ is checked.

> [!NOTE]
> If you want to capture MR approvals, please verify in **Project Settings > Merge requests** that Merge request approvals are required.

### Custom merge queues

If you use a custom merge queue that merges changes and then closes the merge request, be sure to add the `externally-merged` label **before** closing it. This tells Linear to treat the merge request as successfully merged even though it was closed.

### Branch-specific rules

You can set custom workflow automations based on particular target branches. For example, you can now configure that when a MR is merged to:

* `staging`, the issue status should change to “In QA”
* `main`, the issue status should change to “Deployed”

You can also override a default rule in a particular branch with “no action” if desired, so that issues linked to a change in that branch will not change status. Branch rules can be specified using regex, e.g: `^fea/.*` can set automations for all feature branches.

## Issue linkbacks

When an issue is linked with a merge request, Linear posts a linkback message as a comment with the issue title and description. All the merge requests are also listed in the issue details in Linear. When your MR is being reviewed in GitLab, see the avatars of up to three most recent reviewers and their review states without leaving Linear. This cross-referencing makes it faster to retain context without jumping between apps. Linkbacks are managed by the scope selected.

## Auto-assign and update status

Save yourself a few steps by toggling on our automations in **Settings > My Account > Preferences > Behavior**.

* Auto-assigns the issue to you, and/or
* Move the issue to the first Started status (which you can customize in **Settings > Team > Workflow)** when you copy the git branch name.

## Auto-linking

GitLab supports rendering URLs pointing to Linear when you mention issue IDs in GitLab. To configure this functionality, please reference GitLab's [documentation](https://docs.gitlab.com/user/project/integrations/linear/). 

## FAQ

<details>
<summary>Can I import or sync GitLab issues?</summary>
Our issue migration assistant does not support GitLab issues. We suggest customizing the CLI importer to import issues. One option is to customize the importer to support GitLab imports. Another option is to export GitLab issues to a CSV and then modify the headers and format so that it matches one of the issue trackers supported by the CLI.
</details>

<details>
<summary>How do I connect a MR that is already open?</summary>
Modify the MR title or description to link an issue. See the section on this page titled _Linking MRs to issues_.
</details>

<details>
<summary>How do I remove a MR from an issue?</summary>
Open the issue in Linear and right click on the merge request attachment to bring up an option to remove it. You can also do this through the command menu in Linear by viewing or selecting an issue, then searching for `git.`
</details>

<details>
<summary>I get a notification in Linear every time a MR is open. How can I change this?</summary>
Go to integration settings and remove linkbacks. This should reduce the notifications.
</details>

<details>
<summary>My issue title is not showing up in GitLab comments, just the issue ID. Why?</summary>
If your team is private, we won't disclose the issue title. The link will go to your Linear issue and be accessible only by users who are part of that private team.
</details>

<details>
<summary>What permissions do the integrations require?</summary>
On GitLab, we have both read and write access with their API (they don't have separate permissions for comments).
</details>

<details>
<summary>Why does Linear need an access token?</summary>
During integration setup, Linear requires an access token. The below is an exhaustive list of how that token is used:

* To get supplemental information about merge requests that isn't included in the webhooks we receive
* For posting linkbacks on linked merge requests
* To retrieve merge request information when linking an MR to an issue (for rich attachment)
* To retrieve merge request mergeability status when a pipeline completes
</details>

<details>
<summary>Why are my Linear issues not progressing to my "On MR ready for merge" status?</summary>
We currently only allow issues to transition to the status you've chosen for "On MR ready for merge" if you also have a status selected for "On MR review request or activity". Make sure that you have a status selected for this event. 


![GitLab MR workflow status events](https://webassets.linear.app/images/ornj730p/production/69971e7151c829466d84567e82fbf516db5c6390-1586x742.png?q=95&auto=format&dpr=2)
*GitLab MR workflow status events*
</details>

<details>
<summary>My GitLab integration stopped working</summary>
In GitLab's webhook settings, check that the webhook used for Linear is active. If it isn't, please send take a screenshot of its recent events and send it into [support@linear.app](mailto:support@linear.app) for further support. 

In the meantime, please click the "Test" button for the relevant webhook and confirm if you continue to see issues with the integration.
</details>

<details>
<summary>Can I add multiple GitLab instances?</summary>
It is not currently possible to connect multiple GitLab instances to your Linear workspace, you will need to select one GitLab instance to connect within your GitLab settings.
</details>

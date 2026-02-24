# GitHub

Linear supports linking your GitHub pull requests, automating workflow statuses, and syncing issues between GitHub and Linear.

![Linear logo and Github logo](https://webassets.linear.app/images/ornj730p/production/d41fdca27f9f36238e86e4c01d3cd9d91b078d6b-2880x1620.png?q=95&auto=format&dpr=2)

## Overview

The GitHub integration offers two core functionalities:

Link GitHub PRs | Sync GitHub issues
--- | ---
Automate your issue status by linking to a GitHub pull request or commit to follow their progress. | Sync Linear teams to GitHub repos of your choice, to automatically create and sync issues between Linear and GitHub. This will create a synced thread in the Linear issue so comments will sync both ways

This will only sync issues _going forward_. To import and sync historical GitHub Issues, refer to our [GitHub Issues Importer](https://linear.app/docs/github-to-linear).

### Permissions

The integration needs the following permissions for Pull Requests and GitHub Sync:

* **Read** access to checks and metadata
* **Read and write** access to issues and pull requests

Linking Linear issues to commits is handled through GitHub webhooks, which do **not** require access to your codebase.

To grant Linear **organization-level** access in GitHub, the integration must be installed by a GitHub organization owner. If you only need **repository-level** access, a repository administrator can install the integration instead.

---

## Configure

### Enable the GitHub integration

1. Go to [Setting > Features > Integrations > GitHub](https://linear.app/settings/integrations/github)
2. Click **Enable**
3. Select the GitHub organization you want to connect
4. Select **All repositories** or **Only select repositories** and choose the repositories you want to connect
5. Click **Install**
6. Authenticate into your personal Github account

#### GitHub Enterprise options

If it's relevant to your organization, GitHub Enterprise Cloud and GitHub Enterprise Server require additional setup compared to GitHub.com. See the following section for details of each.

##### GitHub Enterprise Cloud

If you're using GitHub Enterprise Cloud and have _IP Allow List_ security setting enabled, you'll also need to turn on _Enable IP allow list configuration for installed GitHub Apps_ setting to enable Linear's GitHub integration. [Read more here](https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps).

Alternatively you can grant access to Linear's IP addresses:

`35.231.147.226`

`35.243.134.228`

`34.140.253.14`

`34.38.87.206`

`34.134.222.122`

`35.222.25.142`

##### GitHub Enterprise Server (self-hosted)

We've expanded Linear's pull request automation to self-hosted GitHub Enterprise Server. You can now install the [new integration](https://linear.app/integrations/github-enterprise-server) to link Linear issues with a GitHub instance that's hosted in a custom URL. This integration doesn't require new firewall rules.

GitHub Enterprise Server will support the majority of the functionality of our existing GitHub integration with the exception of GitHub issue syncing and commit linking. [GitHub.com](https://github.com/) and Enterprise Cloud users should use our standard GitHub integration instead.

The table below provides a comparison of available features across GitHub.com, GitHub Enterprise Cloud, and GitHub Enterprise Server.

Feature | Github.com | GitHub Enterprise Cloud | GitHub Enterprise Server
--- | --- | --- | ---
Installation Method | Linear GitHub App | Linear GitHub App | Separate GHES App
IP Requirements | None | IP Allow List config required if enabled | No special firewall rules
Multiple GitHub Orgs | Yes | Yes | No
PR Linking | Yes | Yes | Yes
Branch Name Formatting | Yes | Yes | Yes
Status Automation from PRs | Yes | Yes | Yes
Magic Words for Linking | Yes | Yes | PR description only
Commit Linking | Yes | Yes | No
Github Issues Sync | Yes | Yes | No
Issues Sync → Multiple Repositories to Single Team | Yes | Yes | No

#### Add multiple GitHub organizations

Click the **+** icon under _Connected organizations_ to add another GitHub organization. This will take you through the same flow as when you connected the first organization. Currently, we support multiple organizations for the PR automation only. You will only be able to use commit linking with a single GitHub organization.

> [!NOTE]
> It is not possible to connect multiple Linear workspaces to a single GitHub organization. This is a limitation on GitHub's side. GitHub Apps can only be installed once for a GitHub organization so this means only one Linear workspace can be connected.

#### Branch format

Select the branch format you want to use when copying the branch name using `Cmd` + `Shift` + `.` from a Linear issue and pasting it into your branch name.

![Branch format setting](https://webassets.linear.app/images/ornj730p/production/9a16304705f1e90c4056d4270221b3f09ac7c71b-1362x366.png?q=95&auto=format&dpr=2)

### Personal account connection

In addition to the organization-level setup, each member should connect their personal GitHub account. This ensures that the activity feed, synced comments, and assignees are mapped directly to the connected user in Linear, rather than appearing as generic GitHub activity.

To connect your account, navigate to [Settings > Connected accounts](https://linear.app/settings/connected-accounts). Once connected, any synced activity from GitHub will be correctly attributed to you in Linear.

![Section in your Github integration settings that indicates your personal account is not yet connected.](https://webassets.linear.app/images/ornj730p/production/48fb82ecd332e000afc047dc8a8fb5459079cdd2-1362x200.png?q=95&auto=format&dpr=2)

![Connect your personal Github account to link issues with commits, PR, and branches.](https://webassets.linear.app/images/ornj730p/production/ec39f09171f32564bb2e8314bebaa85513b0b4ed-1422x466.png?q=95&auto=format&dpr=2)

### Enable commit linking

1. Turn on the toggle for **Link commits to issues with magic words** at the bottom of the GitHub settings page.
2. Go to **Settings → Webhooks** in your GitHub organization or repository.
3. Click **Add webhook** button
4. Input the Payload URL and Secret provided in Linear, and select `application/json` content type. Leave "Push events" selected.
5. Click **Add webhook**.
6. Go back to Linear and click **Done**.

![Setting to enable commit linking](https://webassets.linear.app/images/ornj730p/production/1aae774b895db809359e7fd2b080341a6b797de1-1372x250.png?q=95&auto=format&dpr=2)

### Configure GitHub Issues Sync

Watch this video to see how GitHub Issues sync works:

![Video](https://webassets.linear.app/files/ornj730p/production/27bbcb51c07b84bfc28a2fc30eb708612d1e8852.mp4)

From the _GitHub Issues_ section of the [GitHub integration settings](https://linear.app/settings/integrations/github), click the **+** icon, then select the GitHub repo and Linear team to link.

You can choose to sync:

* **One-way**: issues created in GitHub will create a synced copy in Linear, or
* **Two-way**: issues created in either the GitHub repo or Linear team will create a synced copy in the other software

![Github Issue Sync configured for two repositories, mapped to their correlated Linear teams.](https://webassets.linear.app/images/ornj730p/production/88707d9d9208d520011ef1abc28e28d63093c236-1370x620.png?q=95&auto=format&dpr=2)

![Setup for GitHub Issues Sync.](https://webassets.linear.app/images/ornj730p/production/f5210265017419b639ab32ccbe952133c74316ef-1042x980.png?q=95&auto=format&dpr=2)

Multiple repositories can be connected to create issues to a single Linear team through one-way sync when issues are created in GitHub. However, only one repo can be configured for two-way sync at a time. 

You can enable two-way sync when connecting a repo to Linear, or change this to another repo by pressing **... > Edit Link** on an existing repo connection. 

> [!NOTE]
> GitHub Issues Sync will only sync newly created issues. To sync existing GitHub Issues, you will have to import them. Refer to the [Importer](https://linear.app/docs/import-issues#github-issues) page.

Properties that are synced between Linear and GitHub issues include:

* _`Title`_
* _`Description`_
* _`Status`_  
Please note that any custom statuses set at the GitHub Project level do not sync to Linear.
* _`Assignee`_  
Linear users can connect their GitHub account from https://linear.app/settings/account/connections to be synced as the issue assignee
* _`Labels`_
* _`Sub-issues`_  
Multi-level & cross-repository/team hierarchies are supported. If parent issue is not a synced issue (e.g. it's in a different GH repo/Linear team), the sub-issue can still get synced, but will have no parent issue set on the other end.
* _`Comments`_  
Comments made not in the synced thread of the Linear issue will not get synced to the GitHub issue. This allows for private discussions.

Moving GitHub synced Linear issues between Linear teams will maintain the synced relationship. You can also transfer GitHub issues between two synced repos; this will appropriately update the team of the associated issue in Linear.

To manually stop syncing, remove the attachment from the Linear issue through its overflow menu. 

**Issue sync banners**

Once an issue is synced between GitHub and Linear, a banner will appear at the top of the issue to make this clear. The banners will display information to show current sync status or will surface any errors with syncing.

![Synced issue banners showing connected and a sync error](https://webassets.linear.app/images/ornj730p/production/d0d25688334fad6ebef18e9411daad033b77432f-2990x400.png?q=95&auto=format&dpr=2)
*GitHub sync banners in Linear, showing issue #37 is connected and #34 had a sync error.*

---



## Linking Linear issues to GitHub PRs

You can link a Linear issue using pull requests or commits.

Watch this video for a quick demo on the available linking methods:

![Video](https://webassets.linear.app/files/ornj730p/production/d97ba48f0c5840572625fd4038594b09bf35184a.mp4)

### Link through pull requests

Branch name | Pull request title | Magic words
--- | --- | ---
Include `issue ID` in the branch name

Use the _Copy git branch name_ action or shortcut Cmd/Ctrl Shift . when viewing or highlighting/selecting an issue and paste it into the new branch name in GitHub. | Include the Linear `issue ID` (e.g. ID-123) in the title when creating pull requests. | **Method**

Use a `magic word + issue ID` in the PR description or title (e.g. `Fixes ENG-123` or `Fixes https://linear.app/workspace/issue/ENG-123/title`). If the issue is unassigned when linking takes place, you will be added as the assignee of the issue.

**Magic words**

Linear offers _closing_ and _non-closing_ magic words for you to customize your workflow. When using a _closing_ magic word, Linear will move the issue to _In Progress_ when the branch is pushed and _Done_ when the commit is merged to the default branch. When using a _non-closing_ magic word, the linked PR or commit will still move the issue through other statuses per Workflow settings, but will not automate the issue's status when the PR or commit merges. Instead, it will only transition the issue through to what’s configured prior to the _On PR or commit merge_ event.

The **closing magic words** are: `close, closes, closed, closing fix, fixes, fixed, fixing, resolve, resolves, resolved, resolving, complete, completes, completed, completing`_._

The **non-closing magic words** are: `ref, refs, references, part of, related to, contributes to, toward, towards`_._

## Link multiple issues

**Link multiple issues to one PR**

Include multiple issue IDs after the magic word in the description (e.g. `Fixes ENG-123, DES-5 and ENG-256`). Linking will happen after you save your changes. Magic words must be used in the PR description, they will not work if linked in a comment on the PR.

**Link multiple PRs to one Linear issue**

You can link multiple PRs to a single Linear issue using any linking technique. The Linear issue status will be updated when the final linked PR moves to the required state from your workflow. 

For example if you have 2 PRs linked to 1 issue, you'll need merge both PRs before the Linear issue status will change. 

### Link using commits

Use a magic word before the issue ID in commit message to link issues. We'll move the issue to `In Progress` when the commit is pushed and `Done` when the commit reaches the default branch.

## Viewing a linked Linear issue

### Remove a PR from an issue

To remove a PR from a Linear issue, open the issue, click on the three dots on the PR attachment, and select **Remove**. You can also do this through the command menu in Linear by viewing or selecting an issue, then searching for `git.`

> [!NOTE]
> To link a PR that is already open, modify the PR title or description to link an issue.

### PR review state

When individual reviewers comment, request changes, or approve your PR, we'll display their avatars and their actions on the GitHub attachment visible on the linked Linear issue. You can use this feature to quickly parse the review state of your PR without needing to return to GitHub.

![PR comments and approved state displayed in Linear attachment.](https://webassets.linear.app/images/ornj730p/production/71c7f822215a7dbd92212e4e4cf15fe06412bec0-1642x190.png?q=95&auto=format&dpr=2)

If you request a team review instead of a review from specific individuals, we display "review requested" or "in review" on the GitHub attachment in place of user avatars.

### Pull request preview links

If your PR contains one or multiple preview links, this will add a preview link shortcut to the Linear issue. 

Preview links are automatically detected for popular platforms like Vercel, Netlify, Cloudflare and AWS Amplify if you have connected Linear with your GitHub repository. We also support custom preview links: pull request descriptions and comments are parsed for any markdown links ending with "preview," once these are added by the PR author or a GitHub bot. 

Multiple previews for a single PR are available in a dropdown menu, with customizable names and icons for easy identification (e.g. mobile and desktop previews). Icons are automatically chosen to reflect best their name, such as a mobile icon for mobile release links. Preview links are automatically removed after 30 days of inactivity on the PR.

![Preview links on a Linear issue](https://webassets.linear.app/images/ornj730p/production/3a621c036a7905eba1232e10ab9d0198b462ad4d-2140x1105.png?q=95&auto=format&dpr=2)

**Pull request preview link accepted formats**

#### PR description text

Links that end with "preview" in your PR descriptions and comments will get added to the Linear issue as a preview link.   
For example:   


![PR containing preview links](https://webassets.linear.app/images/ornj730p/production/2560ff47911cab9d2cd2b0a4df57810572801a98-901x649.png?q=95&auto=format&dpr=2)

#### Vercel Preview comments

Vercel comments with the following format will be added as a preview link in your Linear issue. 

![Vercel preview comment in GitHub](https://webassets.linear.app/images/ornj730p/production/56ded746ad9cab1212c73a7619cfcaf528d2cd8f-1278x531.png?q=95&auto=format&dpr=2)

#### Netlify Preview comments

Netlify comments with the following format will be added as a preview link in your Linear issue. 

![Netlify PR comment with preview](https://webassets.linear.app/images/ornj730p/production/99d538e6966157ac67473bb4a2e70db205f1aa3a-1277x575.png?q=95&auto=format&dpr=2)

---

## Workflow automation

### Issue status updates

Updates to PRs can automatically update the status of their linked Linear issues. 

Watch this video to explore more about how issue status automation works:

![Video](https://webassets.linear.app/files/ornj730p/production/8a2505bb37058e85139d4715a8568d9318016c5a.mp4)

You can customize the automation in _Settings_ > _Team_ > _Issue statuses & automations_ > _Pull request and commit automation_. Since this is a team setting, it must be configured for each team in your workspace. 

You can configure status updates when PRs are drafted, opened, have a review requested, are ready for merge, and merged. By default, we will move linked issues to "In Progress" when PRs are open and "Done" when PRs merge.

![Pull request and commit automation](https://webassets.linear.app/images/ornj730p/production/84e19df283f1da9252108a9fed0a4761697bb999-1430x896.png?q=95&auto=format&dpr=2)

> [!NOTE]
> The "Ready for merge" automation relies on GitHub reporting a stable/mergeable PR status. If any check (including non-required checks) fails, GitHub reports the PR as unstable and the automation to move issues to the ready-for-merge destination will not trigger.

### Custom merge queues

If you use a custom merge queue that merges changes and then closes the pull request, be sure to add the `externally-merged` label **before** closing it. This tells Linear to treat the pull request as successfully merged even though it was closed.

### Branch protection rules

Once a review is requested, if you do not have [branch protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule) rules set up in GitHub, the issue will skip the "review request or activity" state and move to "ready to merge”. Without branch protection rules, a PR is considered always mergeable. Please note that "ready to merge" automations will not fire if a "review request or activity" automation is not also configured. 

### Branch-specific rules

You can also set custom workflow automations based on particular target branches. 

For example, you can now configure that when a PR is merged to:

* `staging`, the issue status should change to “In QA”
* `main`, the issue status should change to “Deployed”

> [!NOTE]
> Branch rules apply only to target branches—the branch a PR is being merged _into_. Automations are not supported for source branches, the branch the PR is created _from_.

Watch this video to visualize how branch-specific rules work:

![Video](https://webassets.linear.app/files/ornj730p/production/21ec41c5cace62492df29c5cf5ec36138f0600d8.mp4)

You can also override a default rule in a particular branch with “no action” if desired, so that issues linked to a change in that branch will not change status. Branch rules can be specified using regex, e.g: `^fea/.*` can set automations for all feature branches.

![Image shows a set of default rules, rules specific to a "staging" branch.](https://webassets.linear.app/images/ornj730p/production/61ff343a87898b3f64535a1af1fc09b1da76d711-1414x862.png?q=95&auto=format&dpr=2)

### Auto-assign and move issue to start

Save yourself a few steps by toggling on our automations that auto-assign the issue to you and move it to a started status when you copy the git branch name. To set up this automation, refer to [Preferences](https://linear.app/docs/account-preferences).

---

## Other settings

### Linkbacks

When an issue is linked with a pull request, commit or GitHub Issue, Linear posts a linkback message as a comment with the issue title and description—including any images or attachments that exist within the description. All the pull requests are also listed in the issue details in Linear. This cross-referencing makes it faster to retain context without jumping between apps.

If enabled for private teams, the issue titles will not be included in the comment. The link will go to your Linear issue and be accessible only by users who are part of that private team.

![Setting for enabling or disabling linkbacks.](https://webassets.linear.app/images/ornj730p/production/524d938918c0a733d722d9a39f8c3589265dba8a-1376x490.png?q=95&auto=format&dpr=2)

### Enable Autolink

If you want to automatically resolve your Linear issue IDs (e.g. _ENG-123_) in PR descriptions or comment to links, you can enable this using GitHub's _Autolink references_ feature. See instructions on [GitHub](https://help.github.com/en/github/administering-a-repository/configuring-autolinks-to-reference-external-resources).

Use the following URL format: `https://linear.app/<workspace>/issue/ID-<num> `where `workspace` corresponds to your workspace's URL and `ID` is the issue identifier key for your team. You need to add each team separately as they all have a different ID pattern.  
  
If you change your Linear team name/ID, you may need to reconfigure the Autolink settings.

## FAQ

<details>
<summary>My integration is not working.</summary>
If you get an error when setting up your GitHub integration, or it doesn't work:

1. Disconnect the integration from GitHub's side.
2. Open Linear in the browser and reset your local database by going to [https://linear.app/reset](https://linear.app/reset).
3. Reconnect the integration in Linear settings.

These are the most common causes of errors:

* The integration got out of sync. In this case, reconnecting and resetting should fix it.
* You can only connect your GitHub account to a single Linear workspace. The workaround is to ask someone else from your org to set up the integration.
</details>

<details>
<summary>I get a notification in Linear every time a PR is open. How can I change this?</summary>
Go to integration settings and remove linkbacks. This should reduce the notifications.
</details>

<details>
<summary>GitHub Enterprise Server integration isn't linking pull requests</summary>
Make sure you completed the following steps during integration installation:

1. Copied the provided _webhook secret_ and saved it when creating the Linear GitHub App for your GHES instance. Without the secret, Linear is unable to verify requests
2. Installed the newly created app to organizations and their repos you wish to link

If you missed the step 1 during installation, you'll need to Disconnect the integration inside Linear, and remove the installation inside your GitHub's developer settings, and re-install.

If you haven't completed the step 2, but successfully created the app, you can link new organizations and repositories under "Install App" in the application's developer settings.

If you have added new organizations, or repositories, they will also need to be linked to the application under developer settings under the "Install App" menu.
</details>

<details>
<summary>Why is my "Ready for merge" workflow not triggering?</summary>
For the "Ready for merge" workflow to trigger, either review or checks are required within GitHub for this PR. Without either of these, the "Ready for merge" workflow will not trigger.

![GitHub workflow settings](https://webassets.linear.app/images/ornj730p/production/6f22958c2c097f287fc3304dddc183a08d803a0f-1332x608.png?q=95&auto=format&dpr=2)
*GitHub workflow settings*
</details>

<details>
<summary>Does the GitHub integration support squash merging?</summary>
If you have already merged multiple PRs into a single branch and you want to merge that branch into a new branch, we will not auto-detect any Linear issues that were linked in the previous PRs. You will need to link each issue anew. You can do this by mentioning the Linear issue IDs in the new PR title or by mentioning them alongside magic words in the PR description.
</details>

<details>
<summary>How can I unlink a PR from a Linear issue when the branch name includes the issue ID?</summary>
If your branch name includes a Linear issue ID, Linear will automatically link the pull request to that issue. Even if you manually unlink it, the connection can return when you push new commits or when the PR is merged.

To prevent this from happening, include the magic word `skip` or `ignore` followed by the relevant Linear issue ID in the PR description:

* `skip ENG-123`
* `ignore ENG-123`

This will fully unlink the PR and prevent status automation, even if the branch name still includes the issue ID.
</details>

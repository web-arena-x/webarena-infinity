# Pull Request Reviews 

View and comment on pull request reviews from Linear.

![Review requests interface open with a PR displayed in Linear](https://webassets.linear.app/images/ornj730p/production/e0bed483fb750f43bf6c1fc51d3be02f7b2724a6-2460x1049.png?q=95&auto=format&dpr=2)

## Overview

Access GitHub Pull Requests (PRs) from Linear to streamline the code review process.

This feature adds a dedicated Reviews section to your sidebar, where you can see all of your PRs awaiting review as well as PRs that you've been asked to review. You'll be able to view PRs, comment on them, and get notifications in your Inbox whenever a review is requested. 

You'll need to open the PR in GitHub to review the code and approve reviews, and will see those changes reflected in Linear.

Go to Reviews quickly with the shortcut `G` + `R`, or open a specific review with `O` + `R`. 

## Basics

#### Enable Reviews

![Linear Connected Accounts containing Github Toggle](https://webassets.linear.app/images/ornj730p/production/94d904656132a064ff2f1e42b9d80a7d74f5d80b-3163x863.png?q=95&auto=format&dpr=2)

To enable Reviews, make sure your personal account is connected with GitHub from [Settings > Connected Accounts](https://linear.app/settings/account/connections) and then toggle on _Enable pull request reviews inside Linear_.

#### Display and grouping

By default, PRs are grouped by Responsibility, divided between PRs that are _To Do_ (need your review), _Waiting for others_ or _Approved._

![Display Settings to Group, Order and adjust properties shown on reviews](https://webassets.linear.app/images/ornj730p/production/51035e591fd6f031878babcc337e4211b0cbc338-1185x795.png?q=95&auto=format&dpr=2)

Similar to other views in Linear, you can adjust the display settings to pick different groupings and decide whether closed PRs and drafts will show. PRs in Reviews can be grouped by _Status_, _Author, Repository_ or switched to _No Grouping_. You can also adjust the display settings to show/hide the Pull Request ID or the avatar of the reviewing user 

#### View PRs

Select a PR to view it. You'll see the PR title, description, and a link to the PR in Github. You can also see a summary of changes and checks associated with the PR.

Open the PR in GitHub to review the full PR and approve or request changes.

![PR as shown in Linear detailing review status and comments](https://webassets.linear.app/images/ornj730p/production/a6dfaf40bd82e6dd7c154162e181d30a2204f0f3-1267x1264.png?q=95&auto=format&dpr=2)

#### Comment on PRs

You'll see all comments related to the PR in the Activity section, including suggested changes from those comments. From here you can create new comments, reply to comments, or react with emoji. 

Commenting on a PR will move it from _To Do_ into _Waiting for Others_ until your comment is addressed.

#### Taking other Actions

Most of the review information is read-only in Linear for the moment, and you'll need to navigate to Github to approve the PR, comment on code inline, or perform actions like requesting other reviewers.

#### Notifications

With this feature enabled, your inbox notifications will include the following:

* **For PR Authors:** Notifications for all comments, reviews by others, and check failures on their PRs.
* **For PR reviewers**: Notifications for review requests as well as comments in PR discussion threads they're participating in.
* **Everyone:** Notifications about mentions in PRs.

## FAQ

<details>
<summary>Can I see my teammates' PRs in Reviews?</summary>
No, you can only access your PRs and PRs awaiting your review.
</details>

<details>
<summary>How do I update a PR that is showing the wrong state?</summary>
This can happen sometimes if a webhook is missed between Linear and GitHub and we fail to capture the change in PR state automatically.   
 
You can trigger an update to the PR state shown in Linear by making a small edit to the PR description in GitHub - for example adding and removing a space. 
 
Otherwise please reach out to support@linear.app with the PR IDs and we can help refresh these for you.
</details>

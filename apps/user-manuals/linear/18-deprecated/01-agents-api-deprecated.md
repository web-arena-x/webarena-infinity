# App platform

Linear will soon support agents as first-class members of Linear workspaces. You can build agents to track and analyze customer feedback, write and review code, communicate updates, manage backlogs, prioritize work, and any other application you can imagine. Agents can take the same actions that any other full members can (e.g. be assigned tasks, @-mentioned) but will be clearly identified as apps. 

To support agents, we’re introducing some new primitives to allow apps and agents to be better represented in the Linear platform. We are also overhauling our permissions system for third-party apps to allow more granular team access and management at the workspace level. These API changes are in private beta.

# Key changes

* New `actor` type "`app`" – when installed your application will appear as an app user in the workspace it was installed into (e.g. [tweet](https://x.com/mathemagic1an/status/1904293319297179871)).
* The token received for this actor type will represent the new app user and can _no longer be used for the authenticating user_ (this is a potentially breaking change if converting an existing app).
* Only a single token can exist for an app user at once, in development you will likely want to share the generated token.
* Apps permissions will be manageable by all workspace admins post-installation (coming soon)
* Apps will appear in @mention and assignment menus (Note: this will be configurable before GA)
* Apps will appear in filters and team management (e.g. create a report of issues created by your app)
* App users will _not_ be billed

# Setup

> **⚠️ Your OAuth application must first be enabled for the feature by Linear staff before any of the changes below are possible.**



1. Create your [OAuth application](https://developers.linear.app/docs/oauth/authentication) – the logo and name should match how it will appear to users inside of their Linear workspace when installed.
2. Use standard OAuth authentication with `actor=app` as an additional parameter in the authorize url to install the app in the authorizing workspace. Note that this supersedes the similarly named `actor=application`
3. Exchange the OAuth code for a token as usual ([OAuth docs](https://developers.linear.app/docs/oauth/authentication))
4. Querying the API with the token will act as the "app user" within the workspace. As such, you can find the user ID belonging to your app in the workspace with the following query:

```undefined
query Me {
 viewer {
    id
 }
}
```

# Usage

Now that you have a token for the installing workspace we recommend storing it alongside the `appId` in your database. Using the token with the API will perform actions as your app rather than the authenticating user.

If you need to also perform actions as a specific user then you should authenticate twice, once with `actor=app` and once without and store the OAuth tokens separately.

# Webhooks

Under your OAuth app configuration enable webhooks at the bottom of the config screen. There will be a new option available, "**App user notifications**" – enabling this category of events will notify your webhook when events occur that are directly relevant to your app user.

The received webhook payload will have the following shape:

```json
{
 type: "AppUserNotification",
 action: NotificationType,
 createdAt: string,
 organizationId: string,
 oauthClientId: string,
 appUserId: string,
 notification: Notification,
}
```

The `action` key will be one of the following:

```typescript
export enum NotificationType {
 issueMention = "issueMention",
 issueAddedToTriage = "issueAddedToTriage",
 issueAssignedToYou = "issueAssignedToYou",
 issueAddedToView = "issueAddedToView",
 issueUnassignedFromYou = "issueUnassignedFromYou",
 issueNewComment = "issueNewComment",
 issueCommentMention = "issueCommentMention",
 issueCommentReaction = "issueCommentReaction",
 issueThreadResolved = "issueThreadResolved",
 issueEmojiReaction = "issueEmojiReaction",
 issuePriorityUrgent = "issuePriorityUrgent",
 issueSubscribed = "issueSubscribed",
 issueUnsubscribed = "issueUnsubscribed",
 issueBlocking = "issueBlocking",
 issueUnblocked = "issueUnblocked",
 issueReminder = "issueReminder",
 issueStatusChanged = "issueStatusChanged",
 issueStatusChangedAll = "issueStatusChangedAll",
 issueReopened = "issueReopened",
 issueDue = "issueDue",
 oauthClientApprovalCreated = "oauthClientApprovalCreated",
 triageResponsibilityIssueAddedToTriage = "triageResponsibilityIssueAddedToTriage",

 // issue SLA
 issueSlaHighRisk = "issueSlaHighRisk",
 issueSlaBreached = "issueSlaBreached",

 // initiatives
 initiativeAddedAsOwner = "initiativeAddedAsOwner",
 initiativeCommentMention = "initiativeCommentMention",
 initiativeNewComment = "initiativeNewComment",
 initiativeThreadResolved = "initiativeThreadResolved",
 initiativeCommentReaction = "initiativeCommentReaction",
 initiativeMention = "initiativeMention",
 initiativeDescriptionContentChange = "initiativeDescriptionContentChange",
 initiativeReminder = "initiativeReminder",

 // projects
 projectAddedAsMember = "projectAddedAsMember",
 projectAddedAsLead = "projectAddedAsLead",
 projectCommentMention = "projectCommentMention",
 projectNewComment = "projectNewComment",
 projectThreadResolved = "projectThreadResolved",
 projectCommentReaction = "projectCommentReaction",
 projectMention = "projectMention",
 projectReminder = "projectReminder",
 projectDescriptionContentChange = "projectDescriptionContentChange",

 // milestone
 projectMilestoneCommentMention = "projectMilestoneCommentMention",
 projectMilestoneNewComment = "projectMilestoneNewComment",
 projectMilestoneThreadResolved = "projectMilestoneThreadResolved",
 projectMilestoneCommentReaction = "projectMilestoneCommentReaction",
 projectMilestoneMention = "projectMilestoneMention",
 projectMilestoneDescriptionContentChange = "projectMilestoneDescriptionContentChange",

 // documents
 documentMention = "documentMention",
 documentCommentMention = "documentCommentMention",
 documentNewComment = "documentNewComment",
 documentThreadResolved = "documentThreadResolved",
 documentCommentReaction = "documentCommentReaction",
 documentReminder = "documentReminder",
 documentMoved = "documentMoved",
 documentDeleted = "documentDeleted",
 documentRestored = "documentRestored",
 documentSubscribed = "documentSubscribed",
 documentUnsubscribed = "documentUnsubscribed",
 documentContentChange = "documentContentChange",

 // project updates
 projectUpdateCreated = "projectUpdateCreated",
 projectUpdatePrompt = "projectUpdatePrompt",
 projectUpdateMention = "projectUpdateMentionPrompt",
 projectUpdateReaction = "projectUpdateReaction",
 // project update comments
 projectUpdateNewComment = "projectUpdateNewComment",
 projectUpdateCommentMention = "projectUpdateCommentMention",
 projectUpdateCommentReaction = "projectUpdateCommentReaction",

 // initiative updates
 initiativeUpdateCreated = "initiativeUpdateCreated",
 initiativeUpdatePrompt = "initiativeUpdatePrompt",
 initiativeUpdateReaction = "initiativeUpdateReaction",
 initiativeUpdateMention = "initiativeUpdateMention",
 // initiative update comments
 initiativeUpdateNewComment = "initiativeUpdateNewComment",
 initiativeUpdateCommentMention = "initiativeUpdateCommentMention",
 initiativeUpdateCommentReaction = "initiativeUpdateCommentReaction",

 // team updates
 teamUpdateNewComment = "teamUpdateNewComment",
 teamUpdateCommentMention = "teamUpdateCommentMention",
 teamUpdateCommentReaction = "teamUpdateCommentReaction",
 teamUpdateReaction = "teamUpdateReaction",
 teamUpdateCreated = "teamUpdateCreated",
 teamUpdateMention = "teamUpdateMention",

 // feed
 feedSummaryGenerated = "feedSummaryGenerated",

 // pull requests
 pullRequestReviewRequested = "pullRequestReviewRequested",
 pullRequestReviewRerequested = "pullRequestReviewRerequested",
 pullRequestApproved = "pullRequestApproved",
 pullRequestChangesRequested = "pullRequestChangesRequested",
 pullRequestCommented = "pullRequestCommented",
 pullRequestChecksFailed = "pullRequestChecksFailed",
 pullRequestMention = "pullRequestMention",
 pullRequestCommentMention = "pullRequestCommentMention",
 pullRequestRemovedFromMergeQueue = "pullRequestRemovedFromMergeQueue",

 // customer needs (requests)
 customerNeedCreated = "customerNeedCreated",
}
```

The following action types are of particular interest to app users:

```undefined
issueMention
issueEmojiReaction
issueCommentMention
issueCommentReaction
issueAssignedToYou
issueUnassignedFromYou
issueNewComment
issueStatusChanged
```

# Known issues

* Team access cannot yet be managed post-install
* It is not possible to request `admin` scope with `actor=app`



Reach out to us in Slack or to support@linear.app if you have questions or suggestions to improve the documentation.

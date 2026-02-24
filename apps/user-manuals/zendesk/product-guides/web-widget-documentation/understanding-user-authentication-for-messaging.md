# Understanding user authentication for messaging

Source: https://support.zendesk.com/hc/en-us/articles/8851239832090-Understanding-user-authentication-for-messaging

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

When you provide conversational support, users might try to carry on a conversation across multiple devices and channels. Authentication in messaging allows you to leverage your app or website's existing authentication mechanism to propagate the user's identity to Zendesk.

Authenticated users can participate in a single conversation across devices, access current and past conversations across all of their devices, and continue conversations while switching from one channel to another. This can enhance the quality of support your agents provide and increase the security of sensitive information that might come up while agents assist your end users.

This article contains the following topics:

- [Considerations for authenticating end users](#topic_z2s_cs2_h2c)
- [Understanding the agent experience with authenticated users](#topic_phf_ws2_h2c)
- [Understanding the user experience with messaging authentication](#topic_v1k_xs2_h2c)
- [Related resources](#topic_xq1_ztf_h2c)

## Considerations for authenticating end users

Consider the following information before authenticating end users for messaging:

### Requirements

The following must be true to authenticate messaging end users:

- Zendesk [Agent Workspace](https://support.zendesk.com/hc/en-us/articles/4408821259930) is activated.
- You're using the Web Widget or mobile SDK channels for messaging.

### Limitations

The following limitations apply to messaging authentication for users:

- End-user authentication for messaging is available for the Web Widget and mobile SDK channels only.
- When using [multi-conversation messaging](https://support.zendesk.com/hc/en-us/articles/8195486407706), users can be marked as authenticated on a maximum of 100 active tickets (any status other than Solved or Closed) concurrently.

### Using help center authentication for the Web Widget

If you configure the Web Widget to use help center authentication, the user's messaging interactions in the Web Widget automatically adopt the user's logged-in identity, and the user's name and email can be shared with bots and agents that engage with the user. However, before you can use this feature, you must [turn on help center authentication](https://support.zendesk.com/hc/en-us/articles/9495852479770).

## Understanding the agent experience with authenticated users

When an end user is authenticated, agents see a green check mark icon next to the visitor's name in conversations and the end user's external ID in the user's profile.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/user_id_aw.png)

Additionally, each response posted by an end user after they're authenticated has the check mark icon.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/uc_messaging_authenticated.png)

Authenticated end users can participate synchronously in a conversation across devices.

If an end user authenticates mid-conversation, there are two possible outcomes:

- If no user exists with the external ID, the unauthenticated user is upgraded to an authenticated user, and agents will see the green check mark icon next to the user's name.
- If a user with the same external ID already exists, the unauthenticated user and all of their conversations and tickets are [merged](https://docs.smooch.io/guide/merging-users/#how-merges-work) with the authenticated user.

### Comparing the agent experience of single-conversation and multi-conversation messaging

In single-conversation messaging, each end user engages in only one conversation at a time, with a check mark appearing promptly in the user's profile after authentication. When a user authenticates mid-conversation, the user records are merged and the conversation is merged with prior conversations.

Conversely, with [multi-conversation messaging](https://support.zendesk.com/hc/en-us/articles/8195486407706), end users can participate in several conversations simultaneously through the Web Widget or your mobile app. This feature enhances the speed of support and issue resolution for customers. When a user authenticates mid-conversation, the user records are merged, but the current conversations aren't merged with prior conversations. Delayed authentication in multi-conversation messaging can result in duplicate tickets for a single issue, which agents might need to [manually merge](https://support.zendesk.com/hc/en-us/articles/4408882445594).

Additionally, with multi-conversation messaging, it's important to understand that while unauthenticated users can have an unlimited number of active tickets (any status other than Solved or Closed), after a user is authenticated, they can be marked as authenticated with the green check mark icon on a maximum of 100 active tickets at a time. In the event an authenticated user has more than 100 active tickets, Zendesk prioritizes displaying the green check mark icon on tickets based on the following criteria:

- The most recent activities involving the end user and agent
- The most recently created or updated ticket

## Understanding the user experience with messaging authentication

After you implement end-user authentication for messaging, end users shouldn't notice much of a difference. After they've been authenticated and their identity is verified with Zendesk, end users aren't prompted to provide their name or email address by AI agents for messaging as part of the [default messaging response](https://support.zendesk.com/hc/en-us/articles/4500737327258#topic_kzg_ync_gnb).

Conversations for authenticated end users are synced across devices when the end user is authenticated. Separate user records and conversations are created for unauthenticated end users. If an end user authenticates mid-conversation, the anonymous conversation that was created before they signed in is automatically merged with the authenticated conversation to provide conversational continuity.

## Related resources

See the following resources to implement authentication for messaging users:

- [Setting up user authentication for messaging](https://support.zendesk.com/hc/en-us/articles/4411666638746)
- [Enabling authenticated visitors for messaging with Zendesk SDKs](https://developer.zendesk.com/documentation/zendesk-web-widget-sdks/sdks/web/enabling_auth_visitors)
- [Turning on help center authentication for messaging](https://support.zendesk.com/hc/en-us/articles/9495852479770)
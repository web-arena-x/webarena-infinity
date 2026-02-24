# Understanding the end-user experience with multi-conversations for messaging

Source: https://support.zendesk.com/hc/en-us/articles/8195486407706-Understanding-the-end-user-experience-with-multi-conversations-for-messaging

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Verified AI summary ◀▼

Enable multi-conversations to let users handle multiple messaging chats at once, enhancing their support experience. In the Web Widget and mobile app, users can view a list of conversations, start new ones, and receive push notifications for updates. This feature supports proactive messages and integrates with AI agents, improving issue resolution without needing to navigate complex steps.

Multi-conversations let your end users conduct multiple messaging
conversations simultaneously in your Web Widget or mobile app, providing faster
resolutions to their support issues and a more satisfying customer
experience.

When you activate multi-conversations, your [AI agent behavior](https://support.zendesk.com/hc/en-us/articles/4408824263578) runs when an end user starts a new
conversation. Multi-conversations significantly impact how end users interact with your
Web Widget and mobile channels.

See [Allowing multiple conversations for your end
users](https://support.zendesk.com/hc/en-us/articles/8008427696410) for information on activating this feature.

See [Configuring multi-conversations](https://developer.zendesk.com/documentation/conversations/configuring-multi-conversations/) for
developer information about this feature.

This article includes the following sections:

- [Changes to the Web Widget experience with multi-conversations](#topic_rpg_qny_1dc)
- [Changes to the mobile experience with multi-conversations](#topic_c5z_pny_1dc)

## Changes to the Web Widget experience with multi-conversations

If you offer messaging support through the Web Widget, your end users will see
several changes when you turn on multi-conversations, including:

- [Conversations list](#topic_hk4_5ny_1dc)
- [Conversations](#topic_odv_5ny_1dc)
- [Launcher button](#topic_vk1_vny_1dc)
- [Proactive Messages](#topic_gxf_vny_1dc)

### Conversations list

When the end user clicks the launcher button, the Web Widget displays a list of
the end user’s existing conversations. Conversations are listed in descending
order based on the time of the latest message in each conversation. End users
can click a conversation to open it in the Web Widget. Inactive conversations
display the *Ended* label.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/multi-convos_list-web_widget.png)

Each conversation in the list includes the following information:

- **Title of the conversation**.
- **Avatar for the agent** who sent the latest message in the conversation.
  Your AI agent avatar displays if an agent hasn’t responded to the
  conversation. The default agent image displays if the agent doesn’t have an
  avatar.
- **Beginning of the latest message in the conversation**. The agent’s
  username precedes the message if the agent submitted the most recent
  comment, or “You” if the end user submitted the most recent comment. The
  content of the message appears in bold if the end user has not read the
  latest message.
- **Timestamp** of the latest message in the conversation.
- **Badge counter** for unread messages.

The **New conversation button** appears at the bottom of the Conversations list. Clicking
this button navigates the end user to the conversation screen and creates a new
conversation. The button doesn’t appear if you have [removed the New conversation button](https://support.zendesk.com/hc/en-us/articles/8008427696410#topic_nwd_wjy_1dc).
In this case, end users can’t create a new, separate conversation but can
continue to raise support issues in any pre-existing conversation.

### Conversations

When the end user is viewing a conversation, the Web Widget frame includes the
following features:

- **The conversation title**, by default the start date/time of the
  conversation.
- **The avatar of the agent** who sent the most recent message in the
  conversation
- **A back button** to return to the list of conversations.

Use the SunCo API to [manage conversation titles and visual
elements](https://developer.zendesk.com/documentation/conversations/configuring-multi-conversations/).

### Launcher button

When the end user clicks the launcher button to open the Web Widget, its behavior
depends on their pre-existing conversations, and whether the tickets associated
with those conversations are [active or inactive](https://support.zendesk.com/hc/en-us/articles/8008427696410#topic_qng_5cj_q2c).

- **If there are no pre-existing conversations**, a new conversation opens
  on the [Conversation
  screen](#topic_z4n_tny_1dc).

  **If there are one or more *active*
  conversations**, the most recently-updated conversation opens on
  the conversation screen. The end user can use the back button to
  navigate to the [Conversation list screen](#topic_pvc_tny_1dc).
- **If all pre-existing conversations are *inactive***, the
  conversation list screen opens allowing the end user to select the
  conversation they want to revisit or start a new conversation by tapping the
  New conversation button.

Note: If you have [removed the New conversation
button](https://support.zendesk.com/hc/en-us/articles/8008427696410#topic_nwd_wjy_1dc), end users with only one conversation always navigate to
the [Conversation
screen](#topic_z4n_tny_1dc), where their conversation displays.

### Proactive Messages

When you turn on multi-conversations, [proactive messages](https://support.zendesk.com/hc/en-us/articles/5381304334234) sent to end users
create new conversations rather than being appended to an existing
conversation.

If you [remove the New conversation button](https://support.zendesk.com/hc/en-us/articles/8008427696410#topic_nwd_wjy_1dc),
your proactive messages will stop creating new conversations. Instead,
subsequent proactive messages are appended to the latest updated
conversation.

## Changes to the mobile experience with multi-conversations

If you offer messaging support through your mobile app, your end users will see
several changes when you turn on multi-conversations, including:

- [Conversation list](#topic_pvc_tny_1dc)
- [Conversation](#topic_z4n_tny_1dc)
- [Launcher button](#topic_smw_tny_1dc)
- [Push notifications](#topic_pj3_5ny_1dc)

### Conversation list

This screen displays a list of the end user’s conversations. All conversations
appear in the list, regardless of [ticket](https://support.zendesk.com/hc/en-us/articles/4892092747162) or [messaging session](https://support.zendesk.com/hc/en-us/articles/8009788438042) status.
Conversations are listed in descending order based on the time of the latest
message in each conversation.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/multi-convos_list-mobile.png)

Each conversation in the list includes the following information:

- **Title of the conversation**.
- **Profile picture of the agent** who sent the latest message in the
  conversation. Your [AI agent avatar](https://support.zendesk.com/hc/en-us/articles/6447066520986) displays if an
  agent hasn’t responded to the conversation. The default agent image displays
  if the agent doesn’t have a profile picture.
- **Beginning of the latest message in the conversation**. The agent’s
  username precedes the message if the agent submitted the most recent
  comment, or “You” if the end user submitted the most recent comment. The
  content of the message appears in bold if the end user has not read the
  latest message.
- **Timestamp** of the latest message in the conversation.
- **Badge counter** for unread messages.
- **New conversation button**. Tapping this button navigates the end user
  to the conversations screen and creates a new conversation. The button
  doesn’t appear if you have [removed the New conversation
  button](https://support.zendesk.com/hc/en-us/articles/8008427696410#topic_nwd_wjy_1dc). In this case, end users can’t create a new, separate
  conversation but can continue to raise support issues in any pre-existing
  conversation.

### Conversation

When you turn on multi-conversations, the header on the conversation screen
includes the following features:

- **The conversation title**, by default the start date/time of the
  conversation.
- **The profile picture for the agent** who sent the most recent message in
  the conversation.

  **A back button** that navigates to the previous
  screen.

See [Customizing and configuring the Zendesk
mobile SDKs](https://support.zendesk.com/hc/en-us/articles/4408834810394#topic_kzg_ync_gnb) for information on setting these features.

Use the SunCo API to [manage conversation titles and visual
elements](https://developer.zendesk.com/documentation/conversations/configuring-multi-conversations/).

### Launcher button

When the end user taps the launcher button to open the widget, its behavior
depends on whether there are pre-existing conversations, and whether those
conversations are [active or inactive](https://support.zendesk.com/hc/en-us/articles/8008427696410#topic_qng_5cj_q2c).

- **If there are no pre-existing conversations**, a new conversation opens
  on the [Conversation
  screen](#topic_z4n_tny_1dc).

  **If there are one or more *active*
  conversations**, the most recently-updated conversation opens on
  the conversation screen. The end user can use the back button to
  navigate to the [Conversation list screen](#topic_pvc_tny_1dc).
- **If all pre-existing conversations are *inactive***, the
  conversation list screen opens, allowing the end user to select the
  conversation they want to revisit or start a new conversation by tapping the
  New conversation button.

If you have [removed the New conversation button](https://support.zendesk.com/hc/en-us/articles/8008427696410#topic_nwd_wjy_1dc),
end users with only one conversation will always navigate to the [Conversation screen](#topic_z4n_tny_1dc), where
their conversation displays.

### Push notifications

When a new message is added to a conversation, the user receives a [push notification](https://support.zendesk.com/hc/en-us/articles/4408834810394#topic_ic5_dsq_gnb) on their mobile
device. Tapping the notification takes them to the Conversation screen, with the
updated conversation open.

Notifications can be received when the end user:

- Is viewing another conversation in the app.
- Is viewing another screen in the app.
- Is not currently in the app (depending on how their notifications are
  configured).

However, new message notifications aren’t displayed if the end user is viewing
the Conversation list. Instead, the newly updated conversation moves to the top
of the list, and the new message is highlighted.
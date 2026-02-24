# Allowing end users to end messaging sessions

Source: https://support.zendesk.com/hc/en-us/articles/10046732687770-Allowing-end-users-to-end-messaging-sessions

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

| | |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

Verified AI summary ◀▼

Enable end users to end messaging sessions when they feel no further discussion is needed. This feature requires multi-conversations to be active and the ability to reopen conversations to be disabled. Note that it removes options for continuing conversations through other channels and affects CSAT surveys. Customize settings in the Admin Center to turn this feature on or off as needed.

You can allow end users to [end a messaging session](https://support.zendesk.com/hc/en-us/articles/8009788438042) with a human or AI agent if they think no further real-time discussion is needed. When an end user ends their messaging session, they’ll need to start a new conversation to contact your support team again.

This article includes the following sections:

- [Considerations when allowing end users to end messaging sessions](#topic_dmx_g13_33c)
- [Turning on the end session feature for end users](#topic_is2_wnh_ldc)
- [Turning off the end session feature for end users](#topic_q5l_wnh_ldc)
- [The end-user experience](#topic_zlj_313_33c)

Related articles:

- [About ending messaging sessions](https://support.zendesk.com/hc/en-us/articles/8009788438042)
- [Allowing agents to end messaging sessions](https://support.zendesk.com/hc/en-us/articles/8372292195354)

## Considerations when allowing end users to end messaging sessions

Consider the requirements and limitations described in this section when determining whether to allow end users to end messaging sessions.

To use this feature, your account must meet the following requirements:

- Multi-conversations[must be turned on](https://support.zendesk.com/hc/en-us/articles/8008427696410).
- The ability to reopen conversations [must be turned off](https://support.zendesk.com/hc/en-us/articles/8008427696410#topic_x5w_pdk_33c).

**Currently, this feature has the following limitations:**

- When this feature is turned on, the Web Widget options to [continue conversations through social channels](https://support.zendesk.com/hc/en-us/articles/4409103296154) are removed, and no longer available for end users.
- If you are using the legacy CSAT experience, you cannot send user satisfaction surveys after the end user ends the session.
- **Custom bot users**: If you are using [conversational control](https://support.zendesk.com/hc/en-us/articles/5514406080538#topic_fwd_ylm_y1c), when an end user ends a conversation that conversation must be returned to its default state by releasing control. This clears any active switchboard integrations, ensuring the conversation closes when the end user ends it.
 - If you are using *release control*, this happens automatically.
 - If you are using *pass control*, the conversation control is passed to another switchboard integration as defined in your configuration. You are responsible for fully managing when and how the conversation ends, and must make sure to [release control](https://developer.zendesk.com/documentation/conversations/messaging-platform/programmable-conversations/switchboard/#release-control) once your custom flow is complete. Until control is released, the conversation will remain open.

## Turning on the end session feature for end users

This feature is *off* by default for most accounts. Make sure your account configuration meets the requirements listed above before turning the feature on.

**To turn on the end session feature for end users**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click **Manage settings**.
3. Under **Advanced**, click **Ending sessions**.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/end_session-admin_center.png)
4. Select **End users can end messaging sessions at any time**
5. Click **Save settings**.

## Turning off the end session feature for end users

If you don't want end users to be able to end messaging sessions, you can turn off this behavior.

**To turn off the end session feature for end users**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. At the top of the Messaging page, click **Manage settings**.
3. Under **Advanced**, click **Ending sessions**.
4. Deselect **End users can end messaging sessions at any time**.
5. Click **Save settings**.

## The end-user experience

When you turn on the feature allowing end users to end their own messaging sessions, the action is added to their messaging UI. Additionally, any options to continue conversations through other channels are removed from the menu.

**In the Web Widget**, the End conversation button (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/end_session_button-WW.png)) is added to the widget header.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/end_session-WW-short.png)

**In mobile SDKs**, the End conversation option is added to the Options (![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/options-menu-icon-small.png)) menu.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/end-session-mobile-options.png)

When an end user clicks the option to end the session, a confirmation dialog appears at the bottom of the UI. When the end user confirms they want to end the conversation, it is noted under the final conversation message.

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/end_session_confirm-WW.png)
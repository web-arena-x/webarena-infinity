# Turning help center authentication for messaging on and off

Source: https://support.zendesk.com/hc/en-us/articles/9495852479770-Turning-help-center-authentication-for-messaging-on-and-off

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

| | |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

If you're using Web Widget for messaging, you can turn help center authentication for messaging on so that the Web Widget automatically uses the identity of end users who are signed in to the help center. In this case, the user's messaging interactions in the Web Widget automatically adopt the user's logged-in identity, and the user's name and email can be shared with bots and agents that engage with the user. You must be an admin to turn on help center authentication for the Web Widget.

This article contains the following topics:

- [Considerations for using help center authentication for messaging](#topic_dqj_y3d_1gc)
- [Turning on help center authentication](#topic_hrn_ljd_1gc)
- [Turning off help center authentication](#topic_vg3_yjd_1gc)

For more information, see [Understanding user authentication for messaging](https://support.zendesk.com/hc/en-us/articles/8851239832090).

## Considerations for using help center authentication for messaging

The following limitations apply to using help center authentication for messaging:

- To use help center authentication with the AI Agents Advanced add-on, some [custom API integrations](https://developer.zendesk.com/documentation/conversations/how-to-guides/messaging-user-data-ai-agents-advanced/) are required.
- Help center authentication can't be used for accounts using [advanced encryption (ADPP add-on)](https://support.zendesk.com/hc/en-us/articles/5043582015898).
- Legacy AI agent flows don't populate the user's email into the `system.user.email` variable.
- The Voice API call button isn't supported.
- An authenticated user's data is synchronized with Sunshine Conversations only when the user logs in to the help center and the Web Widget is initialized. Additional API-level integrations may be necessary to keep your Sunshine Conversations user data in sync.

## Turning on help center authentication

Help center authentication is configured as a Web Widget setting. For most existing Web Widgets, help center authentication is off by default. However, if you configure a new Web Widget, the setting is on by default.

**To turn on help center authentication**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click the name of the Web Widget you want to update.
3. Click the **Installation** tab.
4. Under **Add to help center**, select **Turn on help center authentication**.

## Turning off help center authentication

When necessary, you can turn off help center authentication for your Web Widget. When you turn off help center authentication, the Web Widget will continue to work as expected. However, users interacting with the Web Widget are unauthenticated.

Note: If you're embedding the Web Widget with your own code in a custom Guide theme, this setting must be turned off.

**To turn off help center authentication**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click the name of the Web Widget you want to update.
3. Click the **Installation** tab.
4. Under **Add to help center**, deselect **Turn on help center authentication**.
# Setting up Web Widget for messaging when using live chat and Web Widget (Classic)

Source: https://support.zendesk.com/hc/en-us/articles/4408832031898-Setting-up-Web-Widget-for-messaging-when-using-live-chat-and-Web-Widget-Classic

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

|  |  |
| --- | --- |
| **Support with** | Live chat and messaging Team, Professional, or Enterprise |

This article is for customers using live chat and Web Widget (Classic) who
want to move to messaging and the Web Widget.

If you never used live chat, see
[Creating a messaging Web Widget](https://support.zendesk.com/hc/en-us/articles/4409103246874) or [Creating a messaging Web Widget in accounts prior to
November 2021](https://support.zendesk.com/hc/en-us/articles/4408828655514), depending on when your account was
created.

If you currently use live chat and Web Widget (Classic) in your account, and want to move
to messaging, you need to activate messaging and convert your Web Widget (Classic) to a
messaging Web Widget. You also need to make some updates to your live chat settings. You
must be an admin to perform these tasks.

This article includes the following sections:

- [Activating messaging and the messaging
  Web Widget](#topic_lqs_rnc_gnb)
- [Understanding how activating messaging
  changes your account](#topic_nbq_ftm_jnb)
- [Understanding how Web Widget (Classic)
  settings convert to the Web Widget](#id_jnl_xtm_gnb)
- [Updating live chat settings after
  activating messaging](#topic_tgg_5xj_knb)

## Activating messaging and the messaging Web Widget

After you confirm that you
[meet the requirements for
using messaging](https://support.zendesk.com/hc/en-us/articles/4408846454682#topic_dk3_rnc_gnb)
, you can activate it in your
account.

**To activate messaging in your account**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click
   **Manage settings**.
3. On the Manage settings page, click
   **Turn on messaging for your
   account**.

   If you see an onboarding page, you need to click
   **Get
   started**
   before you can activate messaging.
4. Select
   **Turn on messaging for Web Widget (Classic)**
   to convert your Web
   Widget (Classic) to a messaging Web Widget. If you support multiple brands,
   use the drop-down menu to select the brands where you want to activate
   messaging.

   Any brand that was previously using Web Widget
   (Classic) will continue to use that widget until you convert it, so you
   can do this later if you need to. When converting the Web Widget (Classic)
   to Web Widget, most settings are automatically migrated to the new
   widget settings. See
   [Understanding how Web Widget (Classic) settings convert to the Web Widget](#id_jnl_xtm_gnb).
5. Click **Save Settings**.

   After you activate messaging, it appears in your Channels list
   with **Web Widget** listed as an active channel.
   Activating messaging updates your account in a number of
   significant ways. See [How
   activating messaging changes your account](#topic_nbq_ftm_jnb)
   .

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/messaging_page_webSDK_active.png)

## Understanding how activating messaging changes your account

When messaging is activated in your account, a number of changes
occur that impact functionality in the following areas:

- [Web Widget
  (Classic)](#topic_rpb_3tm_jnb)
- [Android, iOS, and Unity
  SDKs](#topic_p4m_hjb_k4b)
- [AI agents](#topic_wpg_3tm_jnb)
- [Agent Workspace](#topic_cyq_3tm_jnb)
- [Chat](#topic_b2y_3tm_jnb)

### Web Widget (Classic)

Web Widget (Classic) is the original iteration of the Web Widget,
configured through Zendesk Support, that allows you to offer live chat and other
Zendesk features to your customers. If you have previously configured Web Widget
(Classic) on your account, turning on messaging gives you the option to convert
it to the messaging Web Widget on a per-brand basis, or create a messaging Web
Widget for a brand that did not previously use one.

### Android, iOS, and Unity SDKs

Activating messaging does not change any previously-configured or deployed SDKs
you might be using for Android, iOS, or Unity. After messaging is activated, you
can create new Android and iOS SDKs with messaging. These are separate SDKs from
the Classic Zendesk SDKs you've been using so far, and need to be configured and
deployed separately.

### AI agents

When messaging is activated, more automation tools and options are available to you. You can use
an [AI agent](https://support.zendesk.com/hc/en-us/articles/6970583409690), which offers
more complex, automated conversations through your Web Widget or
mobile messaging channels. An AI agent is the first responder to
customer requests, and adds a lot of new functionality.

See [Creating an AI agent for your web and mobile
messaging channels](https://support.zendesk.com/hc/en-us/articles/4408824263578) for more information.

### Agent Workspace

Agent Workspace gains some additional functionality as well, including enhanced
conversation history and responding to messaging conversations at any time. See
[Agent Workspace for messaging](https://support.zendesk.com/hc/en-us/articles/4408821905434).

### Live chat

When you activate messaging, there are a number live chat-related
changes that apply to both agents and administrators.

See [How activating messaging impacts Chat settings
and capabilities](https://support.zendesk.com/hc/en-us/articles/4408834919834).

## Understanding how Web Widget (Classic) settings convert to the Web Widget

When you convert Web Widget (Classic), you're essentially switching off the
Web Widget (Classic) and migrating to the messaging Web Widget. Many of your Web
Widget (Classic) configuration settings are automatically migrated to the new widget
settings, including:

- **Widget position**: The widget and launcher will appear
  wherever you've placed it on your help center or web page.
- **Theme color**: The color setting for the launcher, contact
  button, and header are applied to the Web Widget frame.
- **Web Widget button text**: During migration, this becomes the
  launcher text. As in Web Widget (Classic), it is the text that appears in
  the launcher button.
- **Web Widget snippet**: The new messaging Web Widget and Web
  Widget (Classic) use the same snippet, so there’s no need to update it in
  order for messaging to work.
- **Help center activation**: If you've activated the Web Widget
  (Classic) in a help center, the Web Widget replaces it. The widget and
  launcher will appear wherever you've placed it on your Help Center or web
  page.

Some Web Widget (Classic) functionality is not available in the
messaging Web Widget:

- **Call options are not available**. You can still receive calls through the Agent
  Workspace.
- **Existing Javascript API code may not be supported**. We do
  recommend that you test any API code not documented as supported by the
  messaging Web Widget and let us know of any issues.

## Updating live chat settings after activating messaging

After activating messaging, a Chat admin needs to perform the following tasks:

1. Organize your agents into groups.

   For example, you can create a
   group of agents who handle specific channels, such as messaging. See
   [Adding agents to
   groups](https://support.zendesk.com/hc/en-us/articles/4408894175130#topic_wyj_dse_bc).
2. Set up
   [Support triggers to route messaging
   conversations](https://support.zendesk.com/hc/en-us/articles/4408834919834#topic_wrf_5km_jnb)to these groups.
3. Configure
   [Chat limits](https://support.zendesk.com/hc/en-us/articles/5020833543450#topic_dlr_wt1_q5)
   on the
   [Chat dashboard](https://support.zendesk.com/hc/en-us/articles/4408830603674)
   to control how many
   active messaging conversations your agents receive.
4. Educate agents on the
   [agent experience](https://support.zendesk.com/hc/en-us/articles/4408821905434).
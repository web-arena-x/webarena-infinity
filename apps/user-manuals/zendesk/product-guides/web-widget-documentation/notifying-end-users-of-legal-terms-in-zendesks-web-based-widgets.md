# Notifying end users of legal terms in Zendesk's web-based widgets

Source: https://support.zendesk.com/hc/en-us/articles/5018479936922-Notifying-end-users-of-legal-terms-in-Zendesk-s-web-based-widgets

---

[What's my plan?](https://support.zendesk.com/hc/en-us/articles/5411234991258-plan)

|  |  |
| --- | --- |
| **All Suites** | Team, Growth, Professional, Enterprise, or Enterprise Plus |

Some jurisdictions may require that you provide notice to end users of how their
information is shared with third parties, including Zendesk. Although a published
privacy policy is helpful, many customers have implemented additional notices and/or
consents. Zendesk offers several options to enable you to achieve your compliance
goals.

Zendesk offers native functionality to disclose legal terms to your end users directly
within the messaging user experience. You can seamlessly incorporate a link to your
privacy notice, which will be seamlessly surfaced to customers at the start of a
messaging conversation.

You can also custom-configure web-based conversational widgets – Web Widget, Web Widget
(Classic), and Sunshine Conversations Web Messenger – to inform your customers of a
privacy notice.

This article discusses the following methods for informing customers of information at
the beginning of a chat:

- [Adding a privacy notice](#topic_jxp_tbn_k2c)
- [Adding a cookie banner](#topic_b1h_yfd_dvb)
- [Relying on Zendesk branding](#topic_uzp_yfd_dvb)
- [Including a notice in an initial greeting](#topic_t4v_yfd_dvb)
- [Creating an AI agent with options for refusing consent (legacy AI agents and Web Widget only)](#topic_op1_zfd_dvb)

## Adding a privacy notice

You can add a privacy notice to a messaging Web Widget. The privacy notice can be
included as part of the [initial widget configuration process](https://support.zendesk.com/hc/en-us/articles/4409103246874) or [added to an existing widget](https://support.zendesk.com/hc/en-us/articles/7178617945498#topic_bhf_l5f_bbc).

When added, the text “This chat is recorded using a cloud service.” appears at the
top of the messaging widget:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/privacy_notice-ww.png)

If you’ve published your own privacy documentation, you can also include a link to it
as part of the privacy notice. This adds the text “This chat is recorded using a
cloud service and is subject to the terms of our Privacy Notice.” to the top of the
messaging widget:

![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/privacy_notice-ww_link.png)

**To add a privacy notice to a messaging widget**

1. In [Admin Center](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb), click ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/ac_channels_icon.png)
   **Channels** in the sidebar, then select **Messaging and social >
   Messaging**.
2. Click the name of the messaging widget you want to update.
3. Expand the **Basics** tab and scroll down to the **Privacy notice**
   section.

   ![](https://zen-marketing-documentation.s3.amazonaws.com/docs/en/add_privacy_notice_link.png)
4. Select **Add privacy notice**.
5. Enter a link to your own privacy notice (optional).
6. Click **Save**.

You can remove the privacy notice by deselecting the **Add privacy
notice** setting.

## Adding a cookie banner

One option is for a customer to add a banner to their website, as is done in
Europe for cookie banners, that hides or controls access to the widget. For example,
some customers have a popup stating the following:

- “This website uses cookies…”

  *as well as*
- “...we share information about your use of our site with analytics partners
  according to our Privacy Policy.”

The pop-up can be configured to hide the widget until acknowledged.

If you want the cookie banner to support a “no” option, where the widget will not
appear if the customer does not agree to the consent language, you can achieve this
via cookie consent technology.

- **For Web Widget**, see [Web Widget API: Set cookies](https://developer.zendesk.com/documentation/zendesk-web-widget-sdks/sdks/web/sdk_api_reference#set-cookies) for
  more information.
- **For Web Widget (Classic)**, see [Web Widget (Classic) API: Set
  cookies](https://developer.zendesk.com/api-reference/widget/settings#cookies) for more information.
- **For Sunshine Conversations Web Messenger,** see [Sunshine Conversations Web Messenger API: Set cookies](https://docs.smooch.io/rest/#operation/setCookie) for more
  information.

## Relying on Zendesk branding

By default, the Zendesk widgets include the Zendesk branding. While many customers
choose to remove this logo to “white label” the widget if allowed on their account,
leaving it in place signals to the end user that the widget experience is powered by
a third party.

- **For Web Widget**, see [Configuring the widget frame](https://support.zendesk.com/hc/en-us/articles/4500747797914#topic_ubc_nmd_btb) for
  more information.
- **For Web Widget (Classic)**, see [Configuring components in Web Widget
  (Classic)](https://support.zendesk.com/hc/en-us/articles/4408838063258-Configuring-components-in-Web-Widget-Classic-) for more information.
- **For Sunshine Conversations Web Messenger,** see [Web Messenger: Business profile](https://docs.smooch.io/guide/web-messenger/#business-profile)
  for more information.

## Including a notice in an initial greeting

In Web Widget, you can:

- Update the [default message](https://support.zendesk.com/hc/en-us/articles/4500737327258-Configuring-messaging-responses-for-web-and-mobile-channels) (the first message sent
  by Web Widget) to describe your privacy policy. This way, if the
  user does not proceed with a chat, no transcript will be recorded.

In Web Widget (Classic), you can:

- Configure [the pre-chat form](../configuring-the-chat-widget/enabling-the-pre-chat-form-on-the-chat-widget.md) to send a
  message to all visitors informing them of your privacy policy.
- Customize [the concierge or chat badge](https://support.zendesk.com/hc/en-us/articles/4408828059546-Customizing-the-appearance-of-your-chat-widget) to send a message to all visitors informing them of your privacy policy.

In Sunshine Conversations Web Messenger, you can code your
widget to:

- [Send an initial greeting](https://docs.smooch.io/guide/web-messenger/#receiving-the-response) in
  response that describes your privacy policy.
- Include a [prechat capture](https://docs.smooch.io/guide/web-messenger/#prechat-capture), and configure the
  greeting to send a message to all visitors informing them of your privacy
  policy.
- [Connect with a cookie bot](https://docs.smooch.io/rest/#operation/setCookie)

## Creating an AI agent with options for refusing consent (legacy AI agents and Web Widget only)

You can use [bot builder](https://support.zendesk.com/hc/en-us/articles/4408838909210) to create an AI agent that
informs all visitors of the privacy policy terms. If the user does not consent to
this, you should configure bot builder to *not* transfer their conversation to
an agent (after which a transcript is stored).

Admins can put in a message prior to the transfer step to let end users
know they will be transferred to an agent and let them know of your privacy policy
terms.